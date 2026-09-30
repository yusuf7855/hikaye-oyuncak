# Editör görevi (onarım): Elsa, onarım partisi 47

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar47.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar47.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0120 (deneme 4 -> 5)

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
Elsa karlı dağda küçük bir tepeden kızakla kayıyordu. Anna ise aşağıda kardan bir kale yapıyordu. Elsa önüne bakmadı ve kızak kaleye çarpıp onu dağıttı. "Kale yıkıldı!" dedi Anna üzgün bir sesle. Elsa hemen kızaktan indi ve Anna'nın yanına koştu. "Özür dilerim, Anna, dikkat etmedim," dedi Elsa. Kraliçe Elsa kardeşini kızaktan korumak istedi ve onun elini tuttu. Onu kızak yolundan uzak, düz bir yere götürdü. Orada yardımsever Anna kar taşıdı, Elsa da yeni kaleyi şekillendirdi. "Teşekkürler, Elsa, kale burada güvende!" dedi Anna. Sonra Elsa ile Anna el ele kızağa bindi ve mutlu mutlu kaydı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşini kızaktan"
   - Cümle 7: «Kraliçe Elsa kardeşini kızaktan korumak istedi ve onun elini tuttu.»
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Hikayede zaten tanıtılmış Elsa unvanıyla yeniden tanıtılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni kaleyi şekillendirdi"
   - Cümle 9: «Orada yardımsever Anna kar taşıdı, Elsa da yeni kaleyi şekillendirdi.»
   - Açıklama: 'şekillendirdi' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0120` birebir aynı, `@degisim: askı -> kızak` (tutuyorsan), ardından `@onarim: 35a76a59059be403af1e80cbaad931a170998832`, sonra gövde.

### Hikâye 2: tohum elsa-0121 (deneme 3 -> 4)

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
Elsa önlüğünü giymiş, sarayın büyük salonunda resim yapıyordu. Resmine parlak renkler koymak istiyordu. Ama salon karanlıktı ve kutudaki karışık boyaların rengi görünmüyordu. Elsa bu sarayın kraliçesiydi ve en güneşli pencereyi biliyordu. O pencereye gitti ve kalın perdeleri açtı. Güneş içeri girdi ve salonu aydınlattı. Elsa artık boyaları çok iyi görüyordu. Kırmızı, sarı ve mavi boyaları seçip resmine sürdü. Resmi rengarenk oldu. Elsa resmini uzaktan izledi ve gülümsedi. Elsa çok sevindi, çünkü resmini tam istediği gibi yapmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve en güneşli pencereyi biliyordu"
   - Cümle 4: «Elsa bu sarayın kraliçesiydi ve en güneşli pencereyi biliyordu.»
   - Açıklama: Kartın özellikler alanındaki kraliçelik (kız kardeşini korur) burada yalnız pencereyi bilmenin gerekçesi olarak kartta olmayan biçimde kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0121` birebir aynı, ardından `@onarim: a9123a46cf33ec1a1e661becbcb90b0e946df9d2`, sonra gövde.

### Hikâye 3: tohum elsa-0122 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: salonda tık tık diye bir ses vardı | kutudaki kozayı bulup pencereyi kapattı
@tohum: elsa-0122
@degisim: pahalı -> kuru
Büyük salonda ince bir tık tık sesi duyuluyordu. Elsa sesin nereden geldiğini çok merak etti. Önce perdeye, sonra halıya baktı, ama hiçbir şey bulamadı. Kraliçe Elsa sesi dinledi ve pencereye doğru yürüdü. Pencerenin yanında küçük bir kutu vardı. Elsa o kutuda kuru yapraklar biriktiriyordu. Kutunun yanına gitti ve içine eğilip baktı. Yaprakların arasında küçük, boş bir koza vardı. Açık pencereden gelen rüzgar kozayı sallıyordu. Koza kutuya vurunca tık tık ses çıkıyordu. Elsa pencereyi kapattı ve ses hemen durdu. Sonra kozayı yaprakların üstüne koydu ve mutlu mutlu gülümsedi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Büyük salonda ince bir tık tık sesi duyuluyordu"
   - Cümle 1: «Büyük salonda ince bir tık tık sesi duyuluyordu.»
   - Açıklama: Sorun yalnız zararsız bir ses; çocuğun önemseyeceği gerçek bir sorun yok.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa sesi dinledi"
   - Cümle 4: «Kraliçe Elsa sesi dinledi ve pencereye doğru yürüdü.»
   - Açıklama: Elsa önceki cümlelerde anlatılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Elsa zaten anlatılırken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sesi dinledi"
   - Cümle 4: «Kraliçe Elsa sesi dinledi ve pencereye doğru yürüdü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve sorunun çözümünde hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0122` birebir aynı, `@degisim: pahalı -> kuru` (tutuyorsan), ardından `@onarim: 90bdaee65db74fcec5faf17ee5f8eeca9018ffd9`, sonra gövde.

### Hikâye 4: tohum elsa-0123 (deneme 3 -> 4)

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
Ormanda sessizce kar yağıyordu. Elsa ile Anna kar topu oynayıp ısınmıştı ve bir kütükte serinliyordu. Anna çantasından reçelli iki ekmek çıkardı, ama ekmeklerin üstüne hemen kar düştü. "Ekmekler ıslanıyor, Elsa!" dedi Anna. Kraliçe Elsa kardeşini kardan korumak istedi ve yakında büyük bir ağaç gördü. "Anna, ekmekleri al ve benimle o ağacın altına gel," dedi Elsa. Anna onları tuttu ve Elsa'nın peşinden koştu. Ağacın kalın dalları karı tutuyordu ve altı kuruydu. Elsa ile Anna dalların altında yan yana oturdu. Çilek reçeli çok tatlıydı ve bu kez ekmeklere hiç kar düşmedi. "Teşekkürler, Elsa, burası kar günü için en güzel yer!" dedi Anna.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir kütükte serinliyordu"
   - Cümle 2: «Elsa ile Anna kar topu oynayıp ısınmıştı ve bir kütükte serinliyordu.»
   - Açıklama: Kar yağan ormanda 'kütükte serinlemek' fiil ve yer olarak uyumsuz; oturma eylemi eksik.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşini kardan"
   - Cümle 5: «Kraliçe Elsa kardeşini kardan korumak istedi ve yakında büyük bir ağaç gördü.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0123` birebir aynı, `@degisim: sadık -> kuru` (tutuyorsan), ardından `@onarim: d9989ad1014c4d8a09ae2d868d3a28aca175b55b`, sonra gövde.

### Hikâye 5: tohum elsa-0124 (deneme 3 -> 4)

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
Rüzgar ormanda hafifçe esiyor ve Elsa'nın yüzünü serinletiyordu. Elsa küçük bir tepeden kızakla kayıyor, her seferinde gülüyordu. Ama kızağın ipi bir çalıya takıldı ve karmakarışık oldu. Elsa kızağı çekti, ama kızak yerinden oynamadı. Çalının ince dalları kırılacak gibi oldu. Kraliçe Elsa çalıyı kırmak istemedi. Çekmeyi bıraktı ve çalının yanına eğildi. İpi dalların arasından tek tek çözdü. Sonunda ip düzeldi ve kızak çalıdan kurtuldu. Elsa kızağını tepeye çekti ve bir kez daha kaydı. Bu kez ip hiçbir yere takılmadı. Elsa aşağıda yüksek sesle güldü. Sonra kızakla kaymaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa çalıyı kırmak"
   - Cümle 6: «Kraliçe Elsa çalıyı kırmak istemedi.»
   - Açıklama: Elsa hikayenin ortasında 'Kraliçe Elsa' diye ikinci kez tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa çalıyı kırmak istemedi"
   - Cümle 6: «Kraliçe Elsa çalıyı kırmak istemedi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, çözümde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0124` birebir aynı, `@degisim: gardırop -> ip` (tutuyorsan), ardından `@onarim: 992bcc2e8906e38fb93b3c9741fa54500dbe2575`, sonra gövde.

### Hikâye 6: tohum elsa-0125 (deneme 3 -> 4)

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
@plan: kardan adamın eli bal kasesine yapıştı | arkadaşına elini yavaşça çevirmesini söyledi ve balı sildi
@tohum: elsa-0125
Bir sabah Kraliçe Elsa sarayda kahvaltı yapıyordu, Olaf da masada oturuyordu. Olaf Elsa'nın taze ekmeğine bal sürmek istedi. Ama ince eli bal kasesinin kenarına yapıştı. "Elsa, elim kaseye yapıştı!" dedi Olaf. Olaf elini hızlı hızlı salladı ve kase de onunla sallandı. "Olaf, dur ve elini yavaşça çevir," dedi Elsa. Olaf Elsa'nın sözünü dinledi ve elini yavaşça çevirdi. Eli kolayca kurtuldu. Elsa bir bezle Olaf'ın elindeki balı sildi. Sonra kendi ekmeğine biraz bal sürdü. Olaf Elsa'ya sıkıca sarıldı. Olaf çok sevindi, çünkü Elsa ona yardım etmişti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa sarayda"
   - Cümle 1: «Bir sabah Kraliçe Elsa sarayda kahvaltı yapıyordu, Olaf da masada oturuyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa sarayda kahvaltı yapıyordu"
   - Cümle 1: «Bir sabah Kraliçe Elsa sarayda kahvaltı yapıyordu, Olaf da masada oturuyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kartın özellikler alanı) yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0125` birebir aynı, ardından `@onarim: 83698f4d17a183b6588c8d1c1c2cd55118e2e256`, sonra gövde.

### Hikâye 7: tohum elsa-0126 (deneme 3 -> 4)

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
Bir sabah Kraliçe Elsa karlı dağda ren geyiği Sven ile yürüyordu. Çantasında Sven için beş kırmızı elma vardı. Elsa ona bir sürpriz yapmak istedi, ama geyik hep burnunu çantaya sokuyordu. "Sven, şu kayanın arkasına git ve orada bekle," dedi Elsa. Sven Elsa'nın sözünü dinledi ve kayanın arkasına geçti. Elsa düz bir taşın üstündeki karı temizledi. Elmaları taşın üstüne yan yana düzgün dizdi. Sonra Sven'i yanına çağırdı. Sven koşarak geldi ve elmaları görünce sevinçle zıpladı. Bütün elmaları yedi ve karda yalnız küçük kırıntılar kaldı. Sven başını Elsa'nın koluna sürttü. "Bu sürpriz senin için, sevgili Sven!" dedi Elsa.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa karlı dağda"
   - Cümle 1: «Bir sabah Kraliçe Elsa karlı dağda ren geyiği Sven ile yürüyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, sorunun çözümünde hiçbir işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa karlı dağda ren geyiği Sven ile yürüyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0126` birebir aynı, `@degisim: yeşillenmek -> dizmek` (tutuyorsan), ardından `@onarim: b778b25acafb57121f5491093da74a9c65937504`, sonra gövde.

### Hikâye 8: tohum elsa-0128 (deneme 3 -> 4)

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
Elsa ormanda Sven ile keyifli bir yürüyüş yapıyordu. Sven yaprak yerken Elsa ona neşeyle bağırarak seslendi. Sven şaşırdı ve bir ağacın arkasına kaçtı. Kraliçe Elsa sessizce ağaca doğru yürüdü. "Özür dilerim, Sven, çok yüksek bağırdım," dedi Elsa. Sven başını ağacın arkasından yavaşça çıkardı. Elsa bir avuç yaprak topladı ve ona uzattı. "Gel, Sven, yemeğine burada devam et," dedi Elsa. Sven yavaşça Elsa'ya doğru yürüdü. Yaprakları yedi ve burnunu Elsa'nın eline sürttü. Elsa çok sevindi, çünkü Sven artık ondan kaçmıyordu.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa sessizce ağaca"
   - Cümle 4: «Kraliçe Elsa sessizce ağaca doğru yürüdü.»
   - Açıklama: Zaten tanıtılmış Elsa 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sessizce ağaca doğru yürüdü"
   - Cümle 4: «Kraliçe Elsa sessizce ağaca doğru yürüdü.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa sessizce ağaca"
   - Cümle 4: «Kraliçe Elsa sessizce ağaca doğru yürüdü.»
   - Açıklama: Tohum özelliği 'Kraliçedir; kız kardeşini korur' yalnız unvan olarak geçiyor, kardeş yok ve özellik işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0128` birebir aynı, `@degisim: yankılanmak -> seslenmek` (tutuyorsan), ardından `@onarim: 3ae70ff00c7d4a918ddef2a7fe6d349664906201`, sonra gövde.

### Hikâye 9: tohum elsa-0129 (deneme 3 -> 4)

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
@plan: yıldızı ağacın tepesine koymak istedi ama boyu yetmedi | arkadaşından yıldızı tepeye koymasını istedi
@tohum: elsa-0129
@degisim: tablo -> yıldız
Ormanda Elsa bir ağacı süslüyordu, Kristoff da yakında kızakla kayıyordu. Elsa elini salladı ve ağacın tepesi için buzdan parlak bir yıldız yaptı. Ama ağacın tepesi Elsa'dan biraz yüksekti ve Elsa'nın boyu yetmedi. "Kristoff, bu yıldızı tepeye koyar mısın?" diye seslendi Elsa. Kristoff kızaktan indi ve yanına geldi. "Tabii, Elsa!" dedi Kristoff. Kristoff Elsa'dan uzundu ve yıldızı kolayca en üstteki dala taktı. Güneş yıldıza vurdu ve bütün ağaç parladı. Artık ağaçta hiçbir süs eksik değildi. Elsa ile Kristoff süslü ağacın önünde mutlu mutlu el çırptı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Güneş yıldıza vurdu"
   - Cümle 8: «Güneş yıldıza vurdu ve bütün ağaç parladı.»
   - Açıklama: 'Güneş vurmak' deyimsel bir anlatım; küçük çocuk için mecazlı.
   - Açıklama: 'Güneş vurmak' mecazlı bir kalıp; küçük çocuk güneşin yıldıza çarptığını sanabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0129` birebir aynı, `@degisim: tablo -> yıldız` (tutuyorsan), ardından `@onarim: a73c8d071d84b7675310bcdfc3369f595a5348df`, sonra gövde.

### Hikâye 10: tohum elsa-0131 (deneme 3 -> 4)

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
@plan: kraliçe kardeşini beklemeden koştu ve kardeşi yolda kaldı | özür diledi ve kardeşinin kolundan tuttu
@tohum: elsa-0131
Dağın tepesinde Elsa ile Anna buzdan saraya yürüyordu. Anna iki eliyle kurabiye dolu bir tabak taşıyordu. Elsa ise kardeşini beklemeden saraya doğru koştu. Anna kaygan yolda ondan uzak ve yalnız kaldı. "Elsa, beni bekle, yol çok kaygan!" diye seslendi Anna. Elsa durdu ve hemen geri koştu. "Özür dilerim, Anna, seni beklemem gerekirdi," dedi Elsa. Kraliçe Elsa kardeşini korumak için onun kolundan tuttu. İki kardeş yolda yavaş yavaş yürüdü ve tabak hiç düşmedi. İkisi saraya girdi ve buzdan kapı arkalarından kapandı. Elsa çok sevindi, çünkü kardeşi artık yalnız değildi.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Elsa durdu ve hemen geri koştu"
   - Cümle 6: «Elsa durdu ve hemen geri koştu.»
   - Açıklama: Kaygan olduğu söylenen dağ yolunda koşmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0131` birebir aynı, ardından `@onarim: 93061361a1d8dd0a9c926c2175a9c39a8d87e6fc`, sonra gövde.

### Hikâye 11: tohum elsa-0133 (deneme 3 -> 4)

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
Elsa karlı ormanda kızağıyla kayıyordu. Olaf'ın ise hiç kızağı yoktu. Olaf yerde bir kutu kapağı buldu ve üstüne oturdu. Ama kapak çok hafifti ve kayarken döndü. Olaf karın içine yuvarlandı. Olaf güldü ama kızağa üzgün üzgün baktı. Kraliçe Elsa kızağını Olaf'ın yanında durdurdu. "Olaf, öne otur ve iki elinle sıkı tutun," dedi Elsa. Olaf hemen öne oturdu. Elsa da arkasına oturdu ve Olaf'a sarıldı. Kızak ağaçların arasından yavaşça ilerledi. "Bu çok eğlenceli, Elsa!" dedi Olaf. Elsa ile Olaf aynı kızakla mutlu mutlu kaymaya devam etti.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kızağa üzgün üzgün baktı"
   - Cümle 6: «Olaf güldü ama kızağa üzgün üzgün baktı.»
   - Açıklama: Olaf'ın kızağı yok; 'kızağa' sözcüğünün hangi kızağı gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kızağını Olaf'ın"
   - Cümle 7: «Kraliçe Elsa kızağını Olaf'ın yanında durdurdu.»
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa ikinci kez 'Kraliçe Elsa' diye tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kızağını Olaf'ın"
   - Cümle 7: «Kraliçe Elsa kızağını Olaf'ın yanında durdurdu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kızağını Olaf'ın yanında durdurdu"
   - Cümle 7: «Kraliçe Elsa kızağını Olaf'ın yanında durdurdu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kızak paylaşmada işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0133` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: dc182a33e4ea669e4e04fd48f9ec6e77dd6d9a25`, sonra gövde.

### Hikâye 12: tohum elsa-0139 (deneme 3 -> 4)

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
Rüzgar hafif hafif esiyordu. Elsa ile Olaf renkli kabuklarla kumda bir güneş yaptı. Ama deniz yükseldi ve dalgalar güneşin bir ucunu bozdu. Olaf kabukları hemen aynı yere dizmek istedi. Orası suya çok yakındı. Elsa bir kraliçeydi ve Olaf'ı dalgalardan korumak istedi. Elsa bütün kabukları bir kovaya koydu. Sonra dolu kovayı limanın yanındaki kuru kuma taşıdı. İkisi güneşi orada yeniden yaptı. Olaf eğri duran bir kabuğu düzeltti. Dalgalar kabuklara hiç ulaşamadı. Elsa ile Olaf çok sevindi, çünkü kumdaki güneş artık dalgalardan uzaktaydı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dalgalar güneşin bir ucunu bozdu"
   - Cümle 3: «Ama deniz yükseldi ve dalgalar güneşin bir ucunu bozdu.»
   - Açıklama: Yuvarlak bir güneş resminin ucu olmaz; 'bir kenarını' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve Olaf'ı dalgalardan korumak istedi"
   - Cümle 6: «Elsa bir kraliçeydi ve Olaf'ı dalgalardan korumak istedi.»
   - Açıklama: Kartın özellik alanı kraliçeliği kız kardeşini korumak olarak veriyor; burada Olaf'a uygulanıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Olaf'ı dalgalardan korumak istedi"
   - Cümle 6: «Elsa bir kraliçeydi ve Olaf'ı dalgalardan korumak istedi.»
   - Açıklama: Sorun kabuk resminin bozulması iken Elsa'nın gerekçesi Olaf'ı korumak olarak sebepsizce değişiyor.
   - Açıklama: Sorun kabuk resminin bozulması iken Elsa'nın amacı sebepsizce Olaf'ı korumaya kayıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "limanın yanındaki kuru kuma taşıdı"
   - Cümle 8: «Sonra dolu kovayı limanın yanındaki kuru kuma taşıdı.»
   - Açıklama: Liman ve kova sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0139` birebir aynı, `@degisim: etiket -> kova` (tutuyorsan), ardından `@onarim: a99e7b0c323c7ed87df10d1eef1c3ac174fd0a60`, sonra gövde.
