# Editör görevi (onarım): Elsa, onarım partisi 53

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar53.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar53.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0120 (deneme 5 -> 6)

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
@degisim: şekillendirmek -> yapmak
Elsa karlı dağda küçük bir tepeden kızakla kayıyordu. Anna ise aşağıda kardan bir kale yapıyordu. Elsa önüne bakmadı ve kızak kaleye çarpıp onu dağıttı. "Kale yıkıldı!" dedi Anna üzgün bir sesle. Elsa hemen kızaktan indi ve Anna'nın yanına koştu. "Özür dilerim, Anna, dikkat etmedim," dedi Elsa. Elsa kraliçe olarak kardeşini kızaktan korumak istedi ve onun elini tuttu. Onu kızak yolundan uzak, düz bir yere götürdü. Orada yardımsever Anna askılı bir kovayla kar taşıdı. Elsa da yeni bir kale yaptı. "Teşekkürler, Elsa, kale burada güvende!" dedi Anna. Sonra Elsa ile Anna el ele kızağa bindi ve mutlu mutlu kaydı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Elsa önüne bakmadı ve kızak kaleye çarpıp"
   - Cümle 3: «Elsa önüne bakmadı ve kızak kaleye çarpıp onu dağıttı.»
   - Açıklama: Aşağıda oynayan birinin olduğu yere önüne bakmadan kızakla kaymak taklit edilince tehlikeli.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa kraliçe olarak kardeşini"
   - Cümle 7: «Elsa kraliçe olarak kardeşini kızaktan korumak istedi ve onun elini tuttu.»
   - Açıklama: 'Kraliçe olarak korumak' soyut bir görev anlatımı; küçük çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa kraliçe olarak kardeşini kızaktan korumak istedi"
   - Cümle 7: «Elsa kraliçe olarak kardeşini kızaktan korumak istedi ve onun elini tuttu.»
   - Açıklama: 'Kraliçe olarak' soyut bir rol ifadesi ve 'kızaktan korumak' çocuk için belirsiz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Anna askılı bir kovayla kar taşıdı"
   - Cümle 9: «Orada yardımsever Anna askılı bir kovayla kar taşıdı.»
   - Açıklama: Askılı kova hiçbir hazırlık olmadan sebepsizce beliriyor.
   - Açıklama: Askılı kova daha önce kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0120` birebir aynı, `@degisim: şekillendirmek -> yapmak` (tutuyorsan), ardından `@onarim: e96e8481db419dda899fb7277340dfc03032f61d`, sonra gövde.

### Hikâye 2: tohum elsa-0121 (deneme 4 -> 5)

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
@plan: salon karanlıktı ve karışık boyaların rengi görünmüyordu | en güneşli pencerenin perdelerini açtı
@tohum: elsa-0121
Elsa önlüğünü giymiş, kraliçe olduğu sarayın büyük salonunda resim yapıyordu. Resmine parlak renkler koymak istiyordu. Ama salon karanlıktı ve kutudaki karışık boyaların rengi görünmüyordu. Elsa salonun en güneşli penceresine gitti ve kalın perdeleri açtı. Güneş içeri girdi ve salonu aydınlattı. Elsa artık boyaları çok iyi görüyordu. Kırmızı, sarı ve mavi boyaları seçip resmine sürdü. Resmi rengarenk oldu. Elsa resmini uzaktan izledi ve gülümsedi. Elsa çok sevindi, çünkü resmini tam istediği gibi yapmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe olduğu sarayın"
   - Cümle 1: «Elsa önlüğünü giymiş, kraliçe olduğu sarayın büyük salonunda resim yapıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız yer tarifi içinde geçiyor, olayda işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kraliçe olduğu sarayın büyük salonunda"
   - Cümle 1: «Elsa önlüğünü giymiş, kraliçe olduğu sarayın büyük salonunda resim yapıyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız anılıyor, perde açma çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0121` birebir aynı, ardından `@onarim: b5c6f11ec5ed9ca0345ea93dddc3184400951d60`, sonra gövde.

### Hikâye 3: tohum elsa-0123 (deneme 4 -> 5)

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
Ormanda sessizce kar yağıyordu. Elsa ile Anna kar topu oynarken çok ısındı. Sonra bir kütüğe oturdular ve serinlediler. Anna çantasından reçelli iki ekmek çıkardı, ama ekmeklerin üstüne hemen kar düştü. "Ekmekler ıslanıyor, Elsa!" dedi Anna. Elsa kraliçe olarak kardeşini kardan korumak istedi. Yakında büyük bir ağaç gördü. "Anna, ekmekleri al ve benimle o ağacın altına gel," dedi Elsa. Anna onları tuttu ve Elsa'nın peşinden koştu. Ağacın kalın dalları karı tutuyordu ve altı kuruydu. Elsa ile Anna dalların altında yan yana oturdu. Bu kez ekmeklere hiç kar düşmedi. "Teşekkürler, Elsa, burası kar günü için en güzel yer!" dedi Anna.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kar topu oynarken çok ısındı"
   - Cümle 2: «Elsa ile Anna kar topu oynarken çok ısındı.»
   - Açıklama: Isınıp serinleme ayrıntısı olayda hiçbir işe yaramıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Anna çantasından reçelli iki ekmek çıkardı, ama ekmeklerin üstüne hemen kar düştü.»
   - Açıklama: Sorun (ekmeklere kar düşmesi) ilk üç cümlede değil ancak 4. cümlede söyleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ekmeklerin üstüne hemen kar düştü"
   - Cümle 4: «Anna çantasından reçelli iki ekmek çıkardı, ama ekmeklerin üstüne hemen kar düştü.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yakında büyük bir ağaç"
   - Cümle 7: «Yakında büyük bir ağaç gördü.»
   - Açıklama: 'Yakında' zaman anlamı da taşıyor; yer için 'yakında bir yerde' ya da 'yakınında' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0123` birebir aynı, `@degisim: sadık -> kuru` (tutuyorsan), ardından `@onarim: 0ec779911311b6fb11e29344c2beadc3e572c0e0`, sonra gövde.

### Hikâye 4: tohum elsa-0124 (deneme 4 -> 5)

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
@plan: kızağın ipi bir çalıya takıldı ve karıştı | çalıyı kırmadan ipi dalların arasından çözdü
@tohum: elsa-0124
@degisim: gardırop -> ip
Rüzgar ormanda hafifçe esiyor ve Kraliçe Elsa'nın yüzünü serinletiyordu. Elsa küçük bir tepeden kızakla kayıyor, her seferinde gülüyordu. Ama kızağın ipi bir çalıya takıldı ve karmakarışık oldu. Elsa kızağı çekti, ama kızak yerinden oynamadı. Çalının ince dalları kırılacak gibi oldu. Elsa çalıyı kırmak istemedi. Çekmeyi bıraktı ve çalının yanına eğildi. İpi dalların arasından tek tek çözdü. Sonunda ip düzeldi ve kızak çalıdan kurtuldu. Elsa kızağını tepeye çekti ve bir kez daha kaydı. Bu kez ip hiçbir yere takılmadı. Elsa aşağıda yüksek sesle güldü. Sonra kızakla kaymaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa'nın yüzünü serinletiyordu"
   - Cümle 1: «Rüzgar ormanda hafifçe esiyor ve Kraliçe Elsa'nın yüzünü serinletiyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, hikayede işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0124` birebir aynı, `@degisim: gardırop -> ip` (tutuyorsan), ardından `@onarim: c51c21f87c5bbdc5952979126af4aae1e218bb27`, sonra gövde.

### Hikâye 5: tohum elsa-0128 (deneme 4 -> 5)

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
@plan: bağırarak seslenince geyik şaşırdı ve ağacın arkasına kaçtı | özür diledi ve onu yapraklarla yanına çağırdı
@tohum: elsa-0128
@degisim: yankılanmak -> seslenmek
Elsa ormanda Sven ile keyifli bir yürüyüş yapıyordu. Sven yaprak yerken Elsa ona neşeyle bağırarak seslendi. Sven şaşırdı ve bir ağacın arkasına kaçtı. Elsa sessizce ağaca doğru gitti. "Özür dilerim, Sven, çok yüksek bağırdım," dedi Elsa. Sven başını ağacın arkasından yavaşça çıkardı. Elsa bir avuç yaprak topladı ve ona uzattı. "Gel, Sven, yemeğine burada devam et," dedi Elsa. Sven kraliçenin sözünü dinledi ve yavaşça ona doğru yürüdü. Yaprakları yedi ve burnunu Elsa'nın eline sürttü. Elsa çok sevindi, çünkü Sven artık ondan kaçmıyordu.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sven kraliçenin sözünü dinledi"
   - Cümle 9: «Sven kraliçenin sözünü dinledi ve yavaşça ona doğru yürüdü.»
   - Açıklama: Elsa kraliçe olarak tanıtılmadan 'kraliçe' diye anılıyor, kimi gösterdiği belirsiz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven kraliçenin sözünü dinledi"
   - Cümle 9: «Sven kraliçenin sözünü dinledi ve yavaşça ona doğru yürüdü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir ad olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, karttaki koruma işleviyle kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0128` birebir aynı, `@degisim: yankılanmak -> seslenmek` (tutuyorsan), ardından `@onarim: b5ffee378c5d12ab5e267a82d7117ec34f7c42dd`, sonra gövde.

### Hikâye 6: tohum elsa-0131 (deneme 4 -> 5)

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
@plan: kraliçe kardeşini beklemeden önden gitti ve kardeşi yolda kaldı | özür diledi ve kardeşinin kolundan tuttu
@tohum: elsa-0131
Dağın tepesinde Elsa ile Anna buzdan saraya yürüyordu. Anna iki eliyle kurabiye dolu bir tabak taşıyordu. Elsa ise kardeşini beklemeden saraya doğru hızla gitti. Anna kaygan yolda ondan uzak ve yalnız kaldı. "Elsa, beni bekle, yol çok kaygan!" diye seslendi Anna. Elsa durdu ve yavaşça geri döndü. "Özür dilerim, Anna, seni beklemem gerekirdi," dedi Elsa. Elsa kraliçe olarak kardeşini korumak için onun kolundan tuttu. İki kardeş yolda yavaş yavaş yürüdü ve tabak hiç düşmedi. İkisi saraya girdi ve buzdan kapı arkalarından kapandı. Elsa çok sevindi, çünkü kardeşi artık yalnız değildi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa kraliçe olarak kardeşini korumak"
   - Cümle 8: «Elsa kraliçe olarak kardeşini korumak için onun kolundan tuttu.»
   - Açıklama: 'Kraliçe olarak korumak' soyut bir görev kavramı, küçük çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0131` birebir aynı, ardından `@onarim: 9214ec86b6b3fec72c346c9ed8c06c4bd938818d`, sonra gövde.

### Hikâye 7: tohum elsa-0133 (deneme 4 -> 5)

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
Elsa karlı ormanda kızağıyla kayıyordu. Olaf'ın ise hiç kızağı yoktu. Olaf yerde bir kutu kapağı buldu ve üstüne oturdu. Ama kapak çok hafifti ve kayarken döndü. Olaf karın içine yuvarlandı. Olaf güldü ama Elsa'nın kızağına üzgün üzgün baktı. Elsa kızağını Olaf'ın yanında durdurdu. "Olaf, öne otur ve iki elinle sıkı tutun," dedi Elsa. Olaf kraliçesinin sözünü dinledi ve hemen öne oturdu. Elsa da arkasına oturdu ve Olaf'a sarıldı. Kızak ağaçların arasından yavaşça ilerledi. "Bu çok eğlenceli, Elsa!" dedi Olaf. Elsa ile Olaf aynı kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Olaf kraliçesinin sözünü dinledi"
   - Cümle 9: «Olaf kraliçesinin sözünü dinledi ve hemen öne oturdu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor; yalnız unvan olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0133` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 5ae67e157e8c6e1a99265eafc4dae0176f70b3cd`, sonra gövde.

### Hikâye 8: tohum elsa-0139 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0139
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'etiket', fiil 'düzeltmek', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: yükselen dalgalar kumdaki kabuk resmini bozdu | kabukları kuru kuma taşıyıp yeniden dizdiler
@tohum: elsa-0139
@degisim: etiket -> kova
Rüzgar hafif hafif esiyordu. Elsa ile Olaf kovadaki renkli kabuklarla kumda bir güneş yaptı. Ama deniz yükseldi ve dalgalar güneşin bir kenarını bozdu. Olaf kabukları hemen aynı yere dizmek istedi. Orası suya çok yakındı ve dalgalar yine gelecekti. Elsa bütün kabukları kovaya geri koydu. Sonra dolu kovayı sudan uzak, kuru kuma taşıdı. Olaf kraliçesinin peşinden koştu. İkisi güneşi orada yeniden yaptı. Olaf eğri duran bir kabuğu düzeltti. Dalgalar kabuklara hiç ulaşamadı. Elsa ile Olaf çok sevindi, çünkü kumdaki güneş artık dalgalardan uzaktaydı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Olaf kraliçesinin peşinden koştu"
   - Cümle 8: «Olaf kraliçesinin peşinden koştu.»
   - Açıklama: Elsa'ya 'kraliçesi' diye ikinci bir adla gönderme yapılıyor; kimi gösterdiği çocuk için belli değil.
   - Açıklama: Elsa önce adıyla tanıtılmışken birden 'kraliçesi' diye anılıyor; kimi gösterdiği küçük çocuk için belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Olaf kraliçesinin peşinden koştu"
   - Cümle 8: «Olaf kraliçesinin peşinden koştu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir kelime olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0139` birebir aynı, `@degisim: etiket -> kova` (tutuyorsan), ardından `@onarim: fd8306a0e483eaadd0248a3a8985f560c70a5a76`, sonra gövde.

### Hikâye 9: tohum elsa-0144 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: tepeden kayan taşlar küçük bir fidana çarpıyordu | büyük taşları fidanın önüne sıraladı
@tohum: elsa-0144
@degisim: hareketli -> ufak
Elsa karlı ormanda yürürken tık tık diye bir ses duydu. Durdu ve küçük bir tepeye baktı. Tepede kar eriyordu ve ufak taşlar aşağı kayıp bir fidana çarpıyordu. Ses bu taşlardan geliyordu. Taşlar çarpınca fidanın ince dalları sallanıyordu. Elsa bir kraliçeydi ve küçük fidanı korumak istedi. Yerdeki büyük taşları tek tek topladı. Sonra onları fidanın önüne yan yana sıraladı. Tepeden yeni bir taş kaydı ve büyük taşlara çarpıp durdu. Fidana artık hiç taş çarpmadı. Elsa fidana baktı ve çok sevindi. Elsa bundan sonra ormanda her küçük fidanı böyle korurdu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve küçük fidanı korumak istedi"
   - Cümle 6: «Elsa bir kraliçeydi ve küçük fidanı korumak istedi.»
   - Açıklama: Karttaki kraliçe özelliği kız kardeşi korumaktır; burada fidana uygulanıyor ve çözüme katkısı yok.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız anılıyor, çözümde (taş dizme) hiçbir işe yaramıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Yerdeki büyük taşları tek tek topladı"
   - Cümle 7: «Yerdeki büyük taşları tek tek topladı.»
   - Açıklama: Taş kayan bir tepenin altında büyük taş taşımak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Taşların kayıp düştüğü tepenin altında taş toplamak çocuğun taklit edebileceği tehlikeli bir davranış.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "her küçük fidanı böyle korurdu"
   - Cümle 12: «Elsa bundan sonra ormanda her küçük fidanı böyle korurdu.»
   - Açıklama: Anlatım -dı'lı geçmişten -rdı'lı geniş zamanın hikayesine kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0144` birebir aynı, `@degisim: hareketli -> ufak` (tutuyorsan), ardından `@onarim: 1067c614a651133067df2de61a9a3063efa85ce7`, sonra gövde.

### Hikâye 10: tohum elsa-0149 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar maskeyi uçurdu ve maske uçuşan kara karıştı | kardaki uzun çizginin yanından yürüyüp maskeyi buldu
@tohum: elsa-0149
@degisim: sakar -> kocaman
Elsa karlı ormanda saraya doğru yürüyordu. Elinde şenlik için kocaman, beyaz bir maske vardı. Ama birden rüzgar esti ve maske elinden uçtu. Rüzgar yerdeki karı da havaya kaldırdı. Beyaz maske uçuşan karın içine karıştı. Elsa maskeyi beyaz karda göremedi. O bir kraliçeydi ve şenlikte bu maskeyi takacaktı. Elsa durdu ve yerdeki kara dikkatle baktı. Karda uzun ince bir çizgi fark etti. Maske kayarken karda bu çizgiyi bırakmıştı. Elsa çizginin yanından yavaşça yürüdü. Çizgi büyük bir ağacın dibinde bitti. Maske de oradaydı. Elsa maskeyi aldı ve şenliğe mutlu mutlu koştu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "O bir kraliçeydi ve şenlikte bu maskeyi takacaktı"
   - Cümle 7: «O bir kraliçeydi ve şenlikte bu maskeyi takacaktı.»
   - Açıklama: Tohumdaki kraliçe özelliği çözümde işe yaramıyor, kartın özellik alanındaki gibi kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "O bir kraliçeydi ve şenlikte"
   - Cümle 7: «O bir kraliçeydi ve şenlikte bu maskeyi takacaktı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız anılıyor, maskeyi bulmada hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0149` birebir aynı, `@degisim: sakar -> kocaman` (tutuyorsan), ardından `@onarim: b3194a8ff4ee2be3ba049bf44ac1f80a0f246323`, sonra gövde.

### Hikâye 11: tohum elsa-0150 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0150
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'bisküvi', fiil 'silmek', sıfat 'uzun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: kaydırak kısaydı ve bisküvi tabağa gelmeden düştü | elinden çıkan buzla kaydırağı tabağa kadar uzattı
@tohum: elsa-0150
Limanda Elsa tahtadan kısa bir kaydırak ve bir tabak hazırlamıştı. Bisküviler kaydıraktan kayıp tabağa düşecekti. Ama kaydırak kısaydı ve ilk bisküvi tabağa gelmeden yere düştü. Bisküvi karlı yerde ıslandı. Elsa ıslak bisküviyi kenara koydu ve biraz düşündü. Sonra elini kaydırağın ucuna doğru tuttu. Elinden buz çıktı ve kaydırak tabağa kadar uzadı. İlk bisküvi kaydırakta kırıntılar bırakmıştı. Elsa uzun kaydırağı eliyle sildi. Sonra cebinden yeni bir bisküvi çıkardı ve yukarıdan bıraktı. Bisküvi hızla kaydı ve tam tabağa düştü. Elsa sevinçle güldü ve bisküviyi yedi. Sonra limanda oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İlk bisküvi kaydırakta kırıntılar bırakmıştı"
   - Cümle 8: «İlk bisküvi kaydırakta kırıntılar bırakmıştı.»
   - Açıklama: İlk bisküvi kaydırağın ucuna gelmeden düşmüştü; kırıntı ve silme ayrıntısı olaydan çıkmıyor ve işlevsiz.
   - Açıklama: Kırıntılar ve kaydırağın silinmesi olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0150` birebir aynı, ardından `@onarim: 1131df30705b972b0acb40eb0d61c56174282853`, sonra gövde.

### Hikâye 12: tohum elsa-0151 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Sven
@tohum: elsa-0151
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: yeni bir şeyi denemek
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tutkal', fiil 'yarışmak', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Sven
@plan: geyik dalgaların sesini işaret sandı ve erken koştu | kağıttan bir bayrak yaptı ve onu yukarı kaldırdı
@tohum: elsa-0151
Bir sabah kraliçe Elsa ile Sven limanda ilk kez yarışacaktı. Elsa'nın cebinde mektup için kırmızı bir kağıt ve tutkal vardı. Ama çevik Sven gürültülü dalgaların sesini işaret sandı ve erken koştu. Elsa, Sven'i yeniden yanına çağırdı. Elsa kağıdı tutkalla bir dala yapıştırdı ve küçük bir bayrak yaptı. "Sven, bu bayrak kalkınca koşacağız," dedi Elsa. Sven bu kez yerinden kıpırdamadan bekledi. Elsa bayrağı yukarı kaldırdı ve ikisi birlikte koştu. Sven yolun sonuna ilk vardı ve sevinçle zıpladı. Elsa gülerek arkasından geldi. Elsa çok sevindi, çünkü ilk yarışları çok güzel olmuştu.
```

**Hakem bulguları (5):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Bir sabah kraliçe Elsa"
   - Cümle 1: «Bir sabah kraliçe Elsa ile Sven limanda ilk kez yarışacaktı.»
   - Açıklama: Addan önce gelen unvan büyük harfle yazılır: 'Kraliçe Elsa'.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah kraliçe Elsa"
   - Cümle 1: «Bir sabah kraliçe Elsa ile Sven limanda ilk kez yarışacaktı.»
   - Açıklama: Tohum özelliği kraliçelik yalnız unvan olarak geçiyor, kartta tarif edildiği gibi işe yarar kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah kraliçe Elsa ile Sven"
   - Cümle 1: «Bir sabah kraliçe Elsa ile Sven limanda ilk kez yarışacaktı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dalgaların sesini işaret sandı"
   - Cümle 3: «Ama çevik Sven gürültülü dalgaların sesini işaret sandı ve erken koştu.»
   - Açıklama: Başlama işareti anlamındaki 'işaret' 3 yaşındaki çocuk için soyut.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama çevik Sven gürültülü"
   - Cümle 3: «Ama çevik Sven gürültülü dalgaların sesini işaret sandı ve erken koştu.»
   - Açıklama: 'Çevik' kelimesini 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0151` birebir aynı, ardından `@onarim: 2bc5e304dd47dd549c48a67117b4711178efa09b`, sonra gövde.
