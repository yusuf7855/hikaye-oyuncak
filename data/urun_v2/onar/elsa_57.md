# Editör görevi (onarım): Elsa, onarım partisi 57

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar57.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar57.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0214 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0214
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'güneş', fiil 'selamlamak', sıfat 'zarif'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: koşarken buz sepetine çarptı ve buzlar döküldü | özür diledi ve buzları birlikte topladılar
@tohum: elsa-0214
@degisim: zarif -> büyük
Kıyıda güneş parlıyordu. Elsa limana gelen büyük bir gemiyi selamlamak için koşuyordu. Acele ederken Kristoff'un buz dolu sepetine çarptı ve buzlar yere döküldü. Kristoff yerdeki buzlara üzgün üzgün baktı. Elsa hemen durdu ve Kristoff'tan özür diledi. Sonra eğildi ve buzları onunla birlikte tek tek topladı. Sepet kısa sürede yine doldu. Kristoff gülümsedi ve Elsa'ya teşekkür etti. Kraliçe Elsa, gemiyi karşılamak için Kristoff'u da yanına çağırdı. İkisi gemiye birlikte el salladı. Elsa bundan sonra limanda hiç koşmadı ve hep yavaş yürüdü.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa, gemiyi karşılamak"
   - Cümle 9: «Kraliçe Elsa, gemiyi karşılamak için Kristoff'u da yanına çağırdı.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, gemiyi karşılamak için"
   - Cümle 9: «Kraliçe Elsa, gemiyi karşılamak için Kristoff'u da yanına çağırdı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) sorunun çözümünde kullanılmıyor, yalnız unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0214` birebir aynı, `@degisim: zarif -> büyük` (tutuyorsan), ardından `@onarim: 7c8619a202a1f5886a87dd60c13a18dac41aefb9`, sonra gövde.

### Hikâye 2: tohum elsa-0215 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0215
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'koni', fiil 'tutunmak', sıfat 'havalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: geyik burnunu koniye soktu ve havuçlar döküldü | geyiğe oturmasını söyledi ve havuçları paylaştı
@tohum: elsa-0215
@degisim: havalı -> büyük
Limanda serin bir rüzgar esiyordu. Elsa'nın elinde kağıttan bir koni vardı ve koninin içi havuç doluydu. Sven burnunu hızla koniye soktu. Elsa düşmemek için Sven'in boynuna tutundu ve havuçlar yere döküldü. "Sven, otur ve bekle," dedi Elsa. Sven kraliçenin sözünü dinledi ve hemen yere oturdu. Elsa yere düşen havuçları topladı ve hepsini ikiye ayırdı. "Bunlar senin, bunlar da benim," dedi Elsa. Sven kendi havuçlarını yavaş yavaş yedi. Sonra büyük boynuzlarını salladı ve Elsa'nın elini kokladı. Elsa çok mutlu oldu, çünkü Sven ile güzelce paylaşmıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kağıttan bir koni"
   - Cümle 2: «Elsa'nın elinde kağıttan bir koni vardı ve koninin içi havuç doluydu.»
   - Açıklama: 'Koni' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime; 'külah' daha uygun.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa düşmemek için Sven'in boynuna tutundu"
   - Cümle 4: «Elsa düşmemek için Sven'in boynuna tutundu ve havuçlar yere döküldü.»
   - Açıklama: Elsa'nın neden düşecek olduğu hiç söylenmiyor; olay bir öncekinden çıkmıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sven kraliçenin sözünü dinledi"
   - Cümle 6: «Sven kraliçenin sözünü dinledi ve hemen yere oturdu.»
   - Açıklama: Elsa ilk kez 'kraliçe' diye anılıyor; çocuk için kimi gösterdiği belli değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven kraliçenin sözünü dinledi"
   - Cümle 6: «Sven kraliçenin sözünü dinledi ve hemen yere oturdu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız ad olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor; yalnız unvan olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0215` birebir aynı, `@degisim: havalı -> büyük` (tutuyorsan), ardından `@onarim: 1558a4a75d0d464bbc76c7eb4c6ab0e6c4bba76e`, sonra gövde.

### Hikâye 3: tohum elsa-0216 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0216
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kitap', fiil 'sarılmak', sıfat 'dağınık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: ıslak taşlara düşen kar taneleri hemen eriyordu | buzdan bir tabak yaptı ve taneleri üstüne topladı
@tohum: elsa-0216
Deniz kıyısında dağınık kar taneleri düşüyordu. Elsa kitapta yıldız şekilli kar taneleri görmüştü. Şimdi onları burada da görmek istedi. Ama ıslak taşlara düşen taneler hemen eriyordu. Elsa kitabını kapattı ve biraz düşündü. Sonra ellerini açtı ve buzdan ince, düz bir tabak yaptı. Kar taneleri soğuk tabağın üstüne düştü ve erimedi. Elsa onlara yakından baktı. Hepsi kitaptaki gibi yıldız şeklindeydi. Her birinin altı küçük ucu vardı. Elsa sevinçle kitabına sarıldı. Sonra Elsa tabakta yeni taneler toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Şimdi onları burada da görmek istedi.»
   - Açıklama: Sorun (tanelerin erimesi) ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0216` birebir aynı, ardından `@onarim: 2029857f105f5afe26b90ed1f9dc77d210f495af`, sonra gövde.

### Hikâye 4: tohum elsa-0217 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Anna
@tohum: elsa-0217
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: bir şey yapmak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yorgan', fiil 'kutlamak', sıfat 'mükemmel'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Anna
@plan: rüzgar yorganın köşelerini havaya kaldırdı | kardeşine bir köşeye oturmasını söyledi
@tohum: elsa-0217
Bir sabah Elsa ile Anna deniz kıyısında bir kutlama hazırlıyordu. Bugün Anna'nın doğum günüydü. Ama rüzgar esti ve yere koydukları yorganın köşeleri havaya kalktı. Anna yorganı tutmaya çalıştı ama bir köşe hep kalkıyordu. Kraliçe Elsa kardeşinin üzüldüğünü gördü ve ona hemen yardım etti. "Anna, şu köşeye otur, sepeti de öteki köşeye koy," dedi Elsa. Anna hemen onun dediğini yaptı. Elsa da kalan iki köşeye iki büyük taş koydu. Yorgan artık hiç kıpırdamadı. Elsa sepetten pastayı çıkardı ve yorganın üstüne koydu. "Bu doğum günü mükemmel oldu, Elsa!" dedi Anna. Elsa çok sevindi, çünkü kardeşinin doğum gününü birlikte kutlamışlardı.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kardeşine bir köşeye oturmasını söyledi"
   - Cümle 0 (plan satırı): «rüzgar yorganın köşelerini havaya kaldırdı | kardeşine bir köşeye oturmasını söyledi»
   - Açıklama: Plan çözümün yalnız bir parçasını söylüyor; sepet ve taşlarla köşeleri sabitleme planda yok.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sepeti de öteki köşeye koy"
   - Cümle 6: «"Anna, şu köşeye otur, sepeti de öteki köşeye koy," dedi Elsa.»
   - Açıklama: Çözüm oturmak, sepet koymak ve iki taş yerleştirmek gibi ikiden fazla adıma yayılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kalan iki köşeye iki büyük taş koydu"
   - Cümle 8: «Elsa da kalan iki köşeye iki büyük taş koydu.»
   - Açıklama: Taşlar daha önce hiç kurulmadan çözüm anında sebepsizce beliriyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kardeşinin doğum gününü birlikte kutlamışlardı"
   - Cümle 12: «Elsa çok sevindi, çünkü kardeşinin doğum gününü birlikte kutlamışlardı.»
   - Açıklama: Tekil özne Elsa ile çoğul 'kutlamışlardı' uyuşmuyor; 'kardeşiyle birlikte kutlamıştı' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0217` birebir aynı, ardından `@onarim: 77ac036f86f231011b6c98d19fee31fc4069aca7`, sonra gövde.

### Hikâye 5: tohum elsa-0218 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0218
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'çorba', fiil 'izlemek', sıfat 'tuzlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: arkadaşının çorbası çok sıcaktı ve içemiyordu | buzdan küçük bir kalp yapıp çorbaya bıraktı
@tohum: elsa-0218
@degisim: tuzlu -> sıcak
Elsa karlı ormanda Kristoff ile yürüyordu. Bir ağacın altında durdular ve Kristoff çantasından bir kap çıkardı. Kaptaki çorba çok sıcaktı ve Kristoff onu içemedi. "Çok acıktım ama beklemek zor," dedi Kristoff. Elsa kaba baktı ve biraz düşündü. Sonra elini salladı ve buzdan küçük bir kalp yaptı. Kalbi dikkatle çorbanın içine bıraktı. Kristoff buz kalbi merakla izledi. Kalp çorbada yavaş yavaş eridi. Kristoff kaşığını aldı ve çorbayı tattı. "Şimdi çok güzel oldu, teşekkürler, Elsa!" dedi Kristoff. Kristoff çorbasını mutlu mutlu içti. Elsa çok sevindi, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kristoff buz kalbi merakla"
   - Cümle 8: «Kristoff buz kalbi merakla izledi.»
   - Açıklama: Tamlama hatalı; 'buzdan kalbi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0218` birebir aynı, `@degisim: tuzlu -> sıcak` (tutuyorsan), ardından `@onarim: 08897874b495383eb794d81ab672f38dcb952f8c`, sonra gövde.

### Hikâye 6: tohum elsa-0219 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0219
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: paylaşmak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'davetiye', fiil 'gezdirmek', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: kısa ayakları derin karda battı ve yürüyemedi | kızağını paylaştı ve arkadaşını sarayda gezdirdi
@tohum: elsa-0219
@degisim: tekerlekli -> kısa
Karlı dağın tepesinde, buzdan sarayın önünde rüzgar esiyordu. Kraliçe Elsa, sarayını görmesi için Olaf'a bir davetiye vermişti. Ama sarayın önünde kar çok derindi ve Olaf'ın kısa ayakları karda battı. Olaf yürüyemedi ve üzgün üzgün durdu. Elsa bunu kapıdan gördü. Hemen kendi büyük kızağını getirdi ve Olaf'ın yanına koydu. Olaf kızağa oturdu ve sevinçle ellerini çırptı. Elsa kızağı çekti ve Olaf'ı içeri götürdü. Sonra onu bütün sarayda gezdirdi. Olaf parlak duvarlara, uzun merdivenlere ve geniş odalara baktı. Olaf çok sevindi, çünkü Elsa kızağını onunla paylaşmıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Olaf'a bir davetiye vermişti"
   - Cümle 2: «Kraliçe Elsa, sarayını görmesi için Olaf'a bir davetiye vermişti.»
   - Açıklama: 'Davetiye' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, sarayını görmesi"
   - Cümle 2: «Kraliçe Elsa, sarayını görmesi için Olaf'a bir davetiye vermişti.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; çözüm kızağı paylaşmak, özellik işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği sorunu çözmede işe yaramıyor, yalnız unvan olarak geçiyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Hemen kendi büyük kızağını"
   - Cümle 6: «Hemen kendi büyük kızağını getirdi ve Olaf'ın yanına koydu.»
   - Açıklama: Kartta Elsa'ya ait bir kızak yok; kızak kartın ilişkilerinde Kristoff ve Sven'e bağlı.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Hemen kendi büyük kızağını getirdi"
   - Cümle 6: «Hemen kendi büyük kızağını getirdi ve Olaf'ın yanına koydu.»
   - Açıklama: Kartta kızak Kristoff ile Sven'e ait; Elsa'nın kendi kızağı kartta yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0219` birebir aynı, `@degisim: tekerlekli -> kısa` (tutuyorsan), ardından `@onarim: 30066dd4faf2358f26c317c59fa64af9f7acfd1e`, sonra gövde.

### Hikâye 7: tohum elsa-0220 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0220
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'anahtar', fiil 'dökmek', sıfat 'güçlü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: aç geyik burnunu sepete soktu ve elmaları döktü | geyiği durdurdu, elmaları topladı ve onunla paylaştı
@tohum: elsa-0220
@degisim: anahtar -> elma
Rüzgar esiyordu ve Elsa limanda bir sepet elma tutuyordu. Güçlü Sven ağır kızağı limana çekmişti ve çok acıkmıştı. Burnunu hızla sepete soktu ve bütün elmaları yere döktü. Elmalar kıyıda her yere yuvarlandı. "Sven, dur ve bekle!" dedi Kraliçe Elsa. Sven hemen durdu ve başını eğdi. Elsa elmaları tek tek topladı ve sepete koydu. Sonra en büyük elmayı Sven'e verdi ve bir elma da kendisi aldı. Sven ile Elsa elmalarını birlikte yedi. Sven sevinçle yanına geldi ve başını Elsa'ya sürttü. "Afiyet olsun, Sven, bu sepet ikimizin!" dedi Elsa.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dedi Kraliçe Elsa"
   - Cümle 5: «"Sven, dur ve bekle!" dedi Kraliçe Elsa.»
   - Açıklama: Önce 'Elsa' olarak tanıtılan kişi burada 'Kraliçe Elsa' unvanıyla yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Kraliçe Elsa"
   - Cümle 5: «"Sven, dur ve bekle!" dedi Kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa elmaları tek tek topladı ve sepete koydu"
   - Cümle 7: «Elsa elmaları tek tek topladı ve sepete koydu.»
   - Açıklama: Sebep Sven'in açlığı iken çözüm durdurma, toplama ve paylaşma olarak üç adıma yayılıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sven sevinçle yanına geldi"
   - Cümle 10: «Sven sevinçle yanına geldi ve başını Elsa'ya sürttü.»
   - Açıklama: Sven ile Elsa elmaları zaten birlikte yemişken Sven'in sonradan yanına gelmesi olay sırasıyla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0220` birebir aynı, `@degisim: anahtar -> elma` (tutuyorsan), ardından `@onarim: 087254757025ac135b4524ed5471dda4a89e5ce0`, sonra gövde.

### Hikâye 8: tohum elsa-0222 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0222
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çamaşır', fiil 'belirmek', sıfat 'saklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: yağan kar beyaz yerde hiç görünmüyordu | koyu eldivenin üstünde karın yıldız şeklini gördü
@tohum: elsa-0222
@degisim: çamaşır -> eldiven
Kar yavaş yavaş yağıyordu ve Elsa ile Kristoff ormanda yürüyordu. Elsa karın şeklini yakından görmek istedi. Ama kar yere düşünce beyaz karın içinde kayboluyordu. Elsa, Kristoff'un koyu renkli eldivenine baktı. "Kristoff, elini aç ve bekle!" dedi Kraliçe Elsa. Kristoff elini hemen açtı ve bekledi. Küçük bir kar parçası eldivenin üstüne düştü. Birden koyu eldivenin üstünde küçük bir yıldız belirdi. Yıldızın altı ucu vardı ve hepsi parlıyordu. "Karın içinde saklı bir yıldız varmış!" dedi Kristoff. Sonra bir yıldız daha düştü. İkisi de yeni yıldıza dikkatle baktı. Elsa çok sevindi, çünkü karın gerçek şeklini sonunda görmüştü.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Kraliçe Elsa"
   - Cümle 5: «"Kristoff, elini aç ve bekle!" dedi Kraliçe Elsa.»
   - Açıklama: Tohum özelliği kraliçelik yalnız unvan olarak geçiyor, kartta tarif edildiği gibi işe yarar kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde hiç işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra bir yıldız daha düştü."
   - Cümle 11: «Sonra bir yıldız daha düştü.»
   - Açıklama: Kar tanesine anlatıcı 'yıldız' diyor; bu mecaz 3 yaşındaki çocuğa uygun değil ve yıldız düşmez.
   - Açıklama: Kar tanesine mecazla 'yıldız' deniyor; küçük çocuk gerçek bir yıldızın düştüğünü sanabilir.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "karın gerçek şeklini sonunda görmüştü"
   - Cümle 13: «Elsa çok sevindi, çünkü karın gerçek şeklini sonunda görmüştü.»
   - Açıklama: Karı ve buzu yöneten Elsa'nın kar tanesinin şeklini ilk kez görmesi kimlik cümlesine ve diziye aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0222` birebir aynı, `@degisim: çamaşır -> eldiven` (tutuyorsan), ardından `@onarim: a2080ff81c2e9af1e21e87bc9e8e24899be2e82d`, sonra gövde.

### Hikâye 9: tohum elsa-0224 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0224
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: kaybolan eşya
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'lamba', fiil 'konuşmak', sıfat 'bilgili'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: kar düşünce lamba karın altında kayboldu | ormanı iyi bildiği için lambayı koyduğu yeri buldu
@tohum: elsa-0224
@degisim: konuşmak -> hatırlamak
Ormanda karlı ağaçlar yan yana duruyordu. Elsa küçük lambasını bir taşın üstüne koymuştu. Ama bir daldan kar düştü ve lamba karın altında kayboldu. Elsa çevresine baktı ama her yer bembeyazdı. Bütün taşlar birbirine benziyordu. Elsa bu krallığın bilgili kraliçesiydi ve ormanı çok iyi biliyordu. En uzun çam ağacını hemen hatırladı. Lambayı o ağacın yanındaki taşa bırakmıştı. Elsa hemen o ağaca yürüdü. Taşın üstündeki karı elleriyle yavaşça itti. Karın altından sarı lamba çıktı. Lamba yine ışık veriyordu. Elsa lambasını bulduğu için çok mutlu oldu.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Elsa bu krallığın bilgili"
   - Cümle 6: «Elsa bu krallığın bilgili kraliçesiydi ve ormanı çok iyi biliyordu.»
   - Açıklama: 'Bu krallık' daha önce anılmadığı için 'bu' işaret sıfatının neyi gösterdiği belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu krallığın bilgili kraliçesiydi"
   - Cümle 6: «Elsa bu krallığın bilgili kraliçesiydi ve ormanı çok iyi biliyordu.»
   - Açıklama: Kraliçelik kartın 'kız kardeşini korur' özelliği yerine ormanı bilme gibi karta yeni bir bilgili olma özelliği olarak kullanılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu krallığın bilgili kraliçesiydi ve ormanı çok iyi biliyordu"
   - Cümle 6: «Elsa bu krallığın bilgili kraliçesiydi ve ormanı çok iyi biliyordu.»
   - Açıklama: Karttaki özellik kız kardeşini koruyan kraliçe; burada kraliçelik bilgililiğe ve ormanı bilmeye bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0224` birebir aynı, `@degisim: konuşmak -> hatırlamak` (tutuyorsan), ardından `@onarim: cc9e2a8e38d290c4d4036f7d885886981eb863f8`, sonra gövde.

### Hikâye 10: tohum elsa-0225 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Anna
@tohum: elsa-0225
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: paylaşmak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'bitki', fiil 'işaretlemek', sıfat 'tuhaf'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Anna
@plan: yalnız bir kızak vardı ve kardeşinin kızağı yoktu | kızağı kardeşiyle paylaştı ve güvenli bir yol seçti
@tohum: elsa-0225
@degisim: bitki -> kızak
Elsa ile Anna karlı dağda kaymak istiyordu. Ama Elsa'nın küçük bir kızağı vardı, Anna'nın kızağı yoktu. Anna üzüldü, çünkü kaymayı çok seviyordu. "Kızağı paylaşalım, Anna," dedi Elsa. Dağda tuhaf şekilli büyük bir kaya vardı. Elsa kardeşini korumak için kayadan uzak, düz bir yol seçti. Yolu bir dalla karda işaretledi. "Öne otur ve sıkı tutun, Anna," dedi kraliçe Elsa. Anna öne oturdu ve kızağı iki eliyle tuttu. Elsa da arkasına oturdu ve kardeşini sardı. Kızak işaretli yoldan yavaşça kaydı. Anna neşeyle güldü. İki kardeş de çok sevindi, çünkü ikisi de kızağa binmişti.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dağda tuhaf şekilli büyük bir kaya vardı"
   - Cümle 5: «Dağda tuhaf şekilli büyük bir kaya vardı.»
   - Açıklama: Kaya kızak sorunuyla ilgisiz biçimde sebepsiz beliriyor ve tehlikesi hiç kurulmuyor.
   - Açıklama: Kaya sebepsiz beliriyor ve güvenli yol seçimi kızağın paylaşılması sorunundan çıkmayan ek bir iş olarak kalıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yolu bir dalla karda işaretledi"
   - Cümle 7: «Yolu bir dalla karda işaretledi.»
   - Açıklama: Paylaşma çözümüne yol seçme ve işaretleme gibi sorunun sebebine yönelmeyen fazladan adımlar ekleniyor.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 8: «"Öne otur ve sıkı tutun, Anna," dedi kraliçe Elsa.»
   - Açıklama: Ada bağlı unvan büyük harfle yazılır: 'Kraliçe Elsa'.
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 8: «"Öne otur ve sıkı tutun, Anna," dedi kraliçe Elsa.»
   - Açıklama: Önceden tanıtılmış Elsa hikayenin ortasında unvanla yeniden tanıtılıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oturdu ve kardeşini sardı"
   - Cümle 10: «Elsa da arkasına oturdu ve kardeşini sardı.»
   - Açıklama: 'Sarmak' burada yanlış anlamda; 'kardeşine sarıldı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0225` birebir aynı, `@degisim: bitki -> kızak` (tutuyorsan), ardından `@onarim: 9f6c6b637c5470552beb20d130ca3c2f4d84e6a8`, sonra gövde.

### Hikâye 11: tohum elsa-0226 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0226
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yağmur ya da kar günü
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'duvar', fiil 'dokunmak', sıfat 'yapraklı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: kar yağdı ve geyiğin yapraklı dallarını kapattı | dalların yerini hatırladı ve geyiğe karı temizletti
@tohum: elsa-0226
Bir sabah dağa bol kar yağdı. Elsa ile Sven sarayın önündeydi. Sven yapraklı dallarını arıyordu ama kar dalların üstünü kapatmıştı. Sven karı kokladı ve üzgün bir ses çıkardı. Elsa dalları duvarın yanına koyduğunu hatırladı. Duvarın alt tarafına eliyle dokundu. "Sven, karı tam buradan temizle," dedi kraliçe Elsa. Sven hemen ayaklarıyla ve burnuyla karı itti. Karın altından yeşil dallar çıktı. Sven dalları sevinçle yedi ve başını salladı. Sonra Elsa ile Sven yağan karda mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 7: «"Sven, karı tam buradan temizle," dedi kraliçe Elsa.»
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 7: «"Sven, karı tam buradan temizle," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak anılıyor; kartın ozellikler alanına aykırı.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0226` birebir aynı, ardından `@onarim: 32b1519fc5360a2044ff626e4d21fee112c539c7`, sonra gövde.

### Hikâye 12: tohum elsa-0227 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0227
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'bot', fiil 'bağlamak', sıfat 'kaygan'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: yürürken tık tık diye bir ses geldi | arkadaşına durmasını söyledi ve sesi buldu
@tohum: elsa-0227
Dağdaki buz sarayının önü çok kaygandı. Elsa ile Olaf yavaş yavaş yürüyordu. Birden "tık tık" diye garip bir ses duydular. "Bu ses nereden geliyor?" diye sordu Olaf. Elsa çevresine baktı ama bir şey göremedi. "Olaf, sen dur, ben yalnız yürüyeceğim," dedi kraliçe Elsa. Olaf hemen durdu. Elsa bir adım attı ve ses yine geldi. Elsa aşağı baktı. Bir botunun bağcığı çözülmüştü ve ucu buza vuruyordu. Elsa bağcığı sıkıca bağladı. Ses hemen kesildi. "Sesi buldun, Elsa!" dedi Olaf. "Birlikte bulduk, Olaf, teşekkürler!" dedi Elsa.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sarayının önü çok kaygandı"
   - Cümle 1: «Dağdaki buz sarayının önü çok kaygandı.»
   - Açıklama: Kayganlık önemli bir ayrıntı gibi kuruluyor ama olayda hiç kullanılmıyor.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 6: «"Olaf, sen dur, ben yalnız yürüyeceğim," dedi kraliçe Elsa.»
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi kraliçe Elsa"
   - Cümle 6: «"Olaf, sen dur, ben yalnız yürüyeceğim," dedi kraliçe Elsa.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor; sesi bulmakta özellik işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak anılıyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0227` birebir aynı, ardından `@onarim: 942d83dd5defd105c9508a7367e8ff55c4940083`, sonra gövde.
