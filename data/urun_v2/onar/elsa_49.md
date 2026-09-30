# Editör görevi (onarım): Elsa, onarım partisi 49

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar49.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar49.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0158 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0158
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'terazi', fiil 'düzenlemek', sıfat 'neşeli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: rüzgar masadaki örtüyü havaya kaldırdı | kardan adama örtüyü tutturdu ve üstüne terazi koydu
@tohum: elsa-0158
Elsa limanda Olaf ile ilk kar için neşeli bir şenlik hazırlıyordu. Olaf, limandaki büyük terazinin yanındaki masaya beyaz bir örtü serdi. Ama rüzgar esti ve örtü havaya kalktı. Kurabiye tabakları masada duramadı. "Olaf, sen örtüyü sıkıca tut," dedi Elsa. Olaf örtüyü iki eliyle tuttu. Elsa kraliçe olduğu için limandaki teraziyi kullanabilirdi. Ağır teraziyi getirdi ve örtünün ortasına koydu. Örtü artık rüzgarda kalkmadı. İkisi kurabiyeleri masada güzelce düzenledi. "Bu şenlik harika olacak!" dedi Olaf. Sonra Elsa ile Olaf şenliğe mutlu mutlu başladı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kardan adama örtüyü tutturdu"
   - Cümle 0 (plan satırı): «rüzgar masadaki örtüyü havaya kaldırdı | kardan adama örtüyü tutturdu ve üstüne terazi koydu»
   - Açıklama: Plandaki 'tutturdu' iliştirmek anlamına da gelir, gövdede ise Olaf örtüyü eliyle tutuyor; anlam belirsiz.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "limandaki teraziyi kullanabilirdi"
   - Cümle 7: «Elsa kraliçe olduğu için limandaki teraziyi kullanabilirdi.»
   - Açıklama: 'Limandaki' ve terazi tekrarı gereksiz; liman ve terazi önceki cümlelerde zaten söylendi.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçe olduğu için limandaki teraziyi"
   - Cümle 7: «Elsa kraliçe olduğu için limandaki teraziyi kullanabilirdi.»
   - Açıklama: Kartın kraliçe özelliği kız kardeşini korumaktır; teraziyi kullanma hakkı olarak zorlama kullanılmış.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçe olduğu için limandaki teraziyi kullanabilirdi"
   - Cümle 7: «Elsa kraliçe olduğu için limandaki teraziyi kullanabilirdi.»
   - Açıklama: Çözümü getiren terazi, kraliçelik gibi sebepsiz ve olayla ilgisiz bir gerekçeyle kullanılıyor.
   - Açıklama: Limandaki büyük terazi çözümü getirmek için sebepsizce kurulmuş, kraliçelik gerekçesi yapay kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0158` birebir aynı, ardından `@onarim: fc4968b550d50b58af08efe9b134bc9c31bfb9fc`, sonra gövde.

### Hikâye 2: tohum elsa-0159 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0159
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'süs', fiil 'güldürmek', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: rüzgar esti ve süs elinden uçup kayboldu | buz duvarına bakıp süsü saçında gördü
@tohum: elsa-0159
Bir sabah dağa sulu kar yağıyordu. Elsa buz sarayının kapısına yeni bir süs asmak istiyordu. Ama rüzgar esti, süs elinden uçtu ve kayboldu. Elsa kapının önündeki kara eğildi ve baktı. Sulu karın içinde yalnız küçük taşlar vardı. Elsa bu sarayın kraliçesiydi ve buz duvarların ayna gibi parladığını biliyordu. Kendi üstüne bakmak için duvara yaklaştı. Duvarda kendini gördü ve süs saçına takılmıştı. Süsün saçında olması Elsa'yı çok güldürdü. Süsü saçından çıkardı ve kapıya astı. Elsa çok sevindi, çünkü süsünü hiç uzağa gitmeden bulmuştu.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve buz duvarların ayna"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve buz duvarların ayna gibi parladığını biliyordu.»
   - Açıklama: Tamlama eki eksik; 'buz duvarlarının' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "buz duvarların ayna gibi"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve buz duvarların ayna gibi parladığını biliyordu.»
   - Açıklama: Tamlama eki eksik; 'buz duvarlarının' olmalı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve buz duvarların ayna gibi parladığını biliyordu.»
   - Açıklama: Kraliçe özelliği karttaki gibi (kız kardeşini korur) değil, ilgisiz bir bilgi gerekçesi olarak kullanılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bu sarayın kraliçesiydi ve buz duvarların"
   - Cümle 6: «Elsa bu sarayın kraliçesiydi ve buz duvarların ayna gibi parladığını biliyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kartın özellikler alanı) çözüme katkı vermeden yalnız anılıyor; çözümü duvarın parlaması sağlıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kendi üstüne bakmak için"
   - Cümle 7: «Kendi üstüne bakmak için duvara yaklaştı.»
   - Açıklama: Kendini görmek için 'kendi üstüne bakmak' yanlış anlamda; 'kendine bakmak' olmalı.
   - Açıklama: 'Kendi üstüne bakmak' yanlış anlamda; kastedilen 'kendine bakmak'.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kendi üstüne bakmak için duvara yaklaştı"
   - Cümle 7: «Kendi üstüne bakmak için duvara yaklaştı.»
   - Açıklama: Elsa'nın süsü kendi üstünde aramak için hiçbir sebebi yokken çözüm sebepsizce geliyor.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Duvarda kendini gördü ve süs saçına takılmıştı"
   - Cümle 8: «Duvarda kendini gördü ve süs saçına takılmıştı.»
   - Açıklama: Farklı özneli ve farklı zamanlı iki yan cümle 've' ile bozuk bağlanmış; 'süsün saçına takıldığını gördü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0159` birebir aynı, ardından `@onarim: 91ae2f73875479b7efe6d29443244280fce0fcbb`, sonra gövde.

### Hikâye 3: tohum elsa-0161 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | şato | Sven
@tohum: elsa-0161
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'uçurtma', fiil 'eğilmek', sıfat 'gürültülü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | şato | Sven
@plan: uçurtmanın ipi geyiğin ayaklarına dolandı | geyiğe durmasını söyledi, eğilip ipi çözdü
@tohum: elsa-0161
Bir sabah Elsa sarayın önünde mavi bir uçurtma uçuruyordu. Sven de onu izliyordu. Birden rüzgar durdu ve uçurtmanın ipi Sven'in ayaklarına dolandı. Sven ayaklarını salladı ama ipi çıkaramadı. Sonra döndü ve gürültülü sesler çıkardı. İp daha çok dolandı. "Sven, dur ve hiç kıpırdama!" dedi Elsa yüksek sesle. Sven kraliçenin sesini tanıdı ve hemen durdu. Elsa yanına eğildi ve ipi yavaşça çözdü. Sonra uçurtmayı dikkatle yere koydu. Sven sevinçle burnunu Elsa'nın eline sürttü. Elsa çok mutlu oldu, çünkü Sven'e yardım etmişti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sven kraliçenin sesini tanıdı"
   - Cümle 8: «Sven kraliçenin sesini tanıdı ve hemen durdu.»
   - Açıklama: Elsa'ya hiç tanıtılmamış 'kraliçe' adıyla değinilmesi, zamirin kimi gösterdiğini belirsizleştiriyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sven kraliçenin sesini tanıdı"
   - Cümle 8: «Sven kraliçenin sesini tanıdı ve hemen durdu.»
   - Açıklama: Tohumdaki kraliçe özelliği ('Kraliçedir; kız kardeşini korur') sorunu çözmede işe yaramıyor, yalnız etiket olarak geçiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Elsa yanına eğildi ve ipi yavaşça çözdü"
   - Cümle 9: «Elsa yanına eğildi ve ipi yavaşça çözdü.»
   - Açıklama: Az önce ayaklarını sallayıp gürültü yapan büyük bir hayvanın ayaklarına eğilmek çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0161` birebir aynı, ardından `@onarim: 56f211ca0009c7a3d255b5ff2c9f9fe56e3ec2f6`, sonra gövde.

### Hikâye 4: tohum elsa-0162 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0162
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'çember', fiil 'incelemek', sıfat 'dalgalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: dalgalar taşları ıslattı ve çember kaydı | limanın kuru tarafına geçti
@tohum: elsa-0162
Elsa limanda ilk kez çember çevirmeyi deniyordu. Ama deniz o sabah çok dalgalıydı. Dalgalar kıyıya vurdu ve taşları ıslattı. Çember ıslak taşların üstünde kaydı ve düştü. Elsa çemberi ve taşları dikkatle inceledi. Taşlar yalnız kıyıya yakın yerde ıslaktı. Elsa kraliçe olduğu için limanı çok iyi tanıyordu. Limanın arka tarafındaki taşların kuru olduğunu biliyordu. Hemen limanın o kuru tarafına geçti. Orada çemberi yeniden yuvarladı. Bu kez çember kaymadı ve uzun süre döndü. Sonra Elsa limanda çemberiyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçe olduğu için limanı"
   - Cümle 7: «Elsa kraliçe olduğu için limanı çok iyi tanıyordu.»
   - Açıklama: Kartın kraliçe özelliği kız kardeşini korumaktır; limanı tanımak olarak zorlama kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0162` birebir aynı, ardından `@onarim: 7e847cf3549b732765b7de1f2712492edac02783`, sonra gövde.

### Hikâye 5: tohum elsa-0163 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Olaf
@tohum: elsa-0163
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'vanilya', fiil 'sabırsızlanmak', sıfat 'kapalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Olaf
@plan: kapıyı kapadı ve kardan adamı dışarıda unuttu | sesi duyup kapıyı açtı ve özür diledi
@tohum: elsa-0163
@degisim: sabırsızlanmak -> beklemek
Rüzgar dağın tepesinde hafifçe esiyordu. Elsa buz sarayında vanilyalı kurabiyeleri bir tabağa diziyordu. Rüzgar girmesin diye kapıyı kapadı. Ama Olaf dışarıda karla oynuyordu ve Elsa bunu unutmuştu. Olaf kapalı kapıya vurdu ve bekledi. Salon çok büyüktü ve Elsa sesi zor duydu. Elsa hemen kapıya koştu ve onu açtı. "Özür dilerim, Olaf, seni dışarıda unuttum," dedi Elsa. "Tamam, ama bana sıkıca sarıl!" dedi Olaf. Elsa ona sarıldı ve bir kurabiye verdi. Sonra Elsa kapının yanına buzdan küçük bir çan yaptı. Olaf çanı çaldı ve güzel bir ses çıktı. Elsa ile Olaf çok sevindi, çünkü Olaf artık gelince çanı çalabilecekti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Rüzgar girmesin diye kapıyı kapadı.»
   - Açıklama: Olaf'ın dışarıda unutulması sorunu ancak dördüncü cümlede söyleniyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra Elsa kapının yanına buzdan küçük bir çan yaptı"
   - Cümle 11: «Sonra Elsa kapının yanına buzdan küçük bir çan yaptı.»
   - Açıklama: Sorun kapıyı açıp özür dileyince çözülmüşken çözüm sarılma, kurabiye ve çan yapma adımlarıyla ikiden fazla adıma uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0163` birebir aynı, `@degisim: sabırsızlanmak -> beklemek` (tutuyorsan), ardından `@onarim: 9cba8433127d8eb2339f52b1b53a4be17fedfc8d`, sonra gövde.

### Hikâye 6: tohum elsa-0165 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0165
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'teker', fiil 'ısınmak', sıfat 'yetenekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: arabanın tekeri bir taşa çarpıp çatladı | sarayın boş arabasını paylaştı ve buzları taşıdılar
@tohum: elsa-0165
Bir sabah Kristoff limanda buz dolu arabasını çekiyordu. Elsa da sarayın büyük ve boş arabasıyla oradaydı. Ama Kristoff'un arabasının tekeri bir taşa çarptı ve çatladı. Araba yana yattı ve bir buz parçası yere düştü. Hava ısınıyordu ve buzlar güneşte eriyebilirdi. Elsa kraliçeydi ve sarayın arabası onundu. Arabasını hemen Kristoff ile paylaştı. Kristoff çok yetenekliydi ve buzları hızlıca sarayın arabasına dizdi. Elsa da düşen buz parçasını yerden aldı ve onların yanına koydu. Kristoff teşekkür etmek için Elsa'ya en parlak buz parçasını verdi. Elsa buzu havaya kaldırdı ve güldü. Sonra Elsa ile Kristoff sarayın arabasını mutlu mutlu birlikte çekti.
```

**Hakem bulguları (6):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Kristoff limanda buz dolu arabasını çekiyordu"
   - Cümle 1: «Bir sabah Kristoff limanda buz dolu arabasını çekiyordu.»
   - Açıklama: Kartın Sven ilişkisine göre Kristoff'un aracı Sven'in çektiği kızaktır; elle çekilen tekerlekli araba diziyi bilen çocuğa yanlış bilgi verir.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sarayın büyük ve boş arabasıyla oradaydı"
   - Cümle 2: «Elsa da sarayın büyük ve boş arabasıyla oradaydı.»
   - Açıklama: Elsa'nın limanda boş bir arabayla bulunması sebepsiz ve yalnız çözümü getirmek için kuruluyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve sarayın arabası onundu"
   - Cümle 6: «Elsa kraliçeydi ve sarayın arabası onundu.»
   - Açıklama: Kartın özellikler alanındaki kraliçelik (kız kardeşini korur) burada araba sahipliği olarak kartta olmayan biçimde kullanılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve sarayın arabası onundu"
   - Cümle 6: «Elsa kraliçeydi ve sarayın arabası onundu.»
   - Açıklama: Sarayın boş arabası sebepsizce limanda hazır bulunuyor ve çözümü kendiliğinden getiriyor; kraliçelik cümlesi de yalnız bunu açıklamak için ekleniyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kristoff çok yetenekliydi ve"
   - Cümle 8: «Kristoff çok yetenekliydi ve buzları hızlıca sarayın arabasına dizdi.»
   - Açıklama: 'Yetenekli' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "aldı ve onların yanına koydu"
   - Cümle 9: «Elsa da düşen buz parçasını yerden aldı ve onların yanına koydu.»
   - Açıklama: 'Onların' zamirinin buzları mı kişileri mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0165` birebir aynı, ardından `@onarim: fe6bd94e837ecfc5dc636ec38a65eb0b2c2a55b7`, sonra gövde.

### Hikâye 7: tohum elsa-0167 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0167
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tepsi', fiil 'çıkmak', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: tepsi karlı tepede bir şeye çarpıp durdu | karı itip gizli taşı buldu ve yanından kaydı
@tohum: elsa-0167
Ormanda küçük ve karlı bir tepe vardı. Elsa bir tepsiye oturdu ve tepeden aşağı kaydı. Ama tepsi tepenin ortasında "tak" diye bir şeye çarptı ve durdu. Elsa bu sesi çok merak etti. Tepsiden kalktı ve karı eliyle yavaşça kenara itti. Karın altından gizli, büyük bir taş çıktı. Elsa kraliçeydi ve kimsenin bu taşa çarpmasını istemedi. Taşın üstünü karla yeniden kapatmadı. Artık büyük taş uzaktan görünüyordu. Sonra Elsa tepeye geri yürüdü. Bu kez taşın öbür yanından aşağı kaydı. Tepsi hiç durmadan en alta kadar gitti. Elsa gülerek tepeye koştu ve mutlu mutlu bir daha kaydı.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bir şeye çarptı ve durdu"
   - Cümle 3: «Ama tepsi tepenin ortasında "tak" diye bir şeye çarptı ve durdu.»
   - Açıklama: Tepsiyle tepeden kayıp gizli bir taşa çarpmak çocuğun taklit edebileceği tehlikeli bir davranış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve kimsenin bu taşa çarpmasını istemedi"
   - Cümle 7: «Elsa kraliçeydi ve kimsenin bu taşa çarpmasını istemedi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız etiket olarak anılıyor, sorunu çözmekte işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0167` birebir aynı, ardından `@onarim: 46b20a57a55814a0daf6341b38ed6afcb94c07df`, sonra gövde.

### Hikâye 8: tohum elsa-0168 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0168
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: paylaşmak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yağ', fiil 'kurtulmak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: kızaktaki oynak bir tahta yerinden kurtuldu | kendi kızağını kardeşiyle paylaştı
@tohum: elsa-0168
@degisim: yağ -> kızak
Ormanda karlı ağaçların arasında küçük bir tepe vardı. Elsa ile Anna kızaklarını çekerek tepeye yürüdü. Ama Anna'nın kızağındaki oynak bir tahta yerinden kurtuldu ve kara düştü. Anna kırık kızağa baktı ve çok üzüldü. Kraliçe Elsa kardeşine kendi kızağında öne oturmasını söyledi. Anna hemen öne oturdu. Elsa da arkasına oturdu ve kardeşine sıkıca sarıldı. İki kardeş tepeden yavaş yavaş kaydı. Anna kahkahalarla güldü. Aşağıda kalkıp bir kez daha yukarı yürüdüler. Elsa çok mutlu oldu, çünkü kızağını kardeşiyle paylaşmıştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oynak bir tahta yerinden kurtuldu"
   - Cümle 3: «Ama Anna'nın kızağındaki oynak bir tahta yerinden kurtuldu ve kara düştü.»
   - Açıklama: Tahta 'kurtulmaz'; burada 'yerinden çıktı' denmeliydi, aynı yanlış kullanım plan satırında da var.
   - Açıklama: Tahta kurtulmaz; 'yerinden çıktı' ya da 'koptu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tahta yerinden kurtuldu ve kara düştü"
   - Cümle 3: «Ama Anna'nın kızağındaki oynak bir tahta yerinden kurtuldu ve kara düştü.»
   - Açıklama: Tahta için 'kurtuldu' fiili öznesine uymuyor; 'çıktı' olmalı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kardeşine kendi kızağında öne oturmasını"
   - Cümle 5: «Kraliçe Elsa kardeşine kendi kızağında öne oturmasını söyledi.»
   - Açıklama: 'Kendi kızağı' Elsa'nın mı yoksa Anna'nın mı olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0168` birebir aynı, `@degisim: yağ -> kızak` (tutuyorsan), ardından `@onarim: c24320e8277535d28f693c1b864f703bae3e0378`, sonra gövde.

### Hikâye 9: tohum elsa-0169 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0169
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'sos', fiil 'kucaklamak', sıfat 'ekşi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: yemek oyununda pastayı koyacak tabak yoktu | ellerini açıp buzdan bir tabak yaptı
@tohum: elsa-0169
@degisim: ekşi -> beyaz
Bir sabah Elsa dağda sarayının önünde oynuyordu. Bugün yemek oyunu oynayıp kardan bir pasta yapacaktı. Ama pastayı koyacak bir tabağı yoktu. Elsa etrafına baktı ama yerde yalnız yumuşak kar vardı. Sonra ellerini açtı ve buzdan yuvarlak bir tabak yaptı. Bir yığın karı kucakladı ve tabağa koydu. Karı elleriyle bastırıp büyük bir pasta yaptı. Tepedeki yumuşak kardan beyaz bir sos hazırladı ve pastaya döktü. Pasta tabağın üstünde güzelce durdu. Elsa pastasına bakıp güldü. Elsa çok sevindi, çünkü oyununda ilk pastasını yapmıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "beyaz bir sos hazırladı ve pastaya döktü"
   - Cümle 8: «Tepedeki yumuşak kardan beyaz bir sos hazırladı ve pastaya döktü.»
   - Açıklama: Kardan sos yapılıp dökülmez; fiil nesnesine uymuyor.
   - Açıklama: Yumuşak kardan sos yapılıp dökülemez; fiil nesnesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0169` birebir aynı, `@degisim: ekşi -> beyaz` (tutuyorsan), ardından `@onarim: ed714062634feaa4b442b27be90c8741619bc54a`, sonra gövde.

### Hikâye 10: tohum elsa-0171 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0171
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: kaybolan eşya
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'gümüş', fiil 'anlaşmak', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: rüzgar gümüş tacı karların içine uçurdu | geyiğe kayayı gösterdi ve tacı karın altında buldu
@tohum: elsa-0171
Elsa ile Sven karlı dağda yürüyordu. Birden güçlü bir rüzgar esti ve Elsa'nın gümüş tacı başından uçtu. Taç derin karların içine düştü ve kayboldu. Elsa karlara baktı ama tacı göremedi. Düşünceli bir yüzle rüzgarın estiği yöne baktı. Orada büyük bir kaya vardı. Kraliçe Elsa eliyle kayayı gösterdi ve Sven'e oraya gitmesini işaret etti. Sven hemen koştu ve burnunu karlara soktu. Bir yerde durdu ve ayağıyla kara vurdu. Elsa oraya eğildi ve karı eliyle açtı. Taç karın altında parlıyordu. Elsa ile Sven hiç konuşmadan çok iyi anlaştı. Elsa tacını taktı ve Sven ile dağda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Orada büyük bir kaya vardı"
   - Cümle 6: «Orada büyük bir kaya vardı.»
   - Açıklama: Kaya çözümü getirecekmiş gibi kuruluyor ama tacın neden kayanın yanında olduğu söylenmiyor ve kaya sonra işlevsiz kalıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa eliyle kayayı"
   - Cümle 7: «Kraliçe Elsa eliyle kayayı gösterdi ve Sven'e oraya gitmesini işaret etti.»
   - Açıklama: Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa eliyle kayayı gösterdi"
   - Cümle 7: «Kraliçe Elsa eliyle kayayı gösterdi ve Sven'e oraya gitmesini işaret etti.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor ve çözümde işe yaramıyor.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bir yerde durdu ve ayağıyla kara vurdu"
   - Cümle 9: «Bir yerde durdu ve ayağıyla kara vurdu.»
   - Açıklama: Tacın yerini Elsa değil Sven buluyor; yan karakter yardımdan öte sorunu çözüyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hiç konuşmadan çok iyi anlaştı"
   - Cümle 12: «Elsa ile Sven hiç konuşmadan çok iyi anlaştı.»
   - Açıklama: 'Konuşmadan anlaşmak' soyut bir kavram; küçük çocuk için somut değil.
   - Açıklama: 'Konuşmadan anlaşmak' soyut bir anlatım; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0171` birebir aynı, ardından `@onarim: fe05c01ea73f54f14514cf56c1c0b0f512b49dda`, sonra gövde.

### Hikâye 11: tohum elsa-0172 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0172
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'eldiven', fiil 'saymak', sıfat 'renkli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: sık çalılar yüzünden ağacın arkasına geçemedi | kardan adamdan yardım istedi ve yıldızları ona astırdı
@tohum: elsa-0172
Elsa karlı ormanda büyük bir ağacı buzdan yıldızlarla süslüyordu. Eldivenlerini çıkardı ve elinden yıldızlar yaptı. Ama ağacın arkasında sık çalılar vardı ve Elsa oraya geçemiyordu. "Olaf, bana yardım eder misin?" diye sordu Elsa. "Tabii, Elsa!" dedi Olaf. Elsa, Olaf'a beş yıldız verdi. Olaf çalıların altından ağacın arkasına geçti. Yıldızları dallara tek tek astı ve saydı. "Bir, iki, üç, dört, beş!" dedi Olaf. Olaf çalıların altından geri geldi. Güneş çıktı ve yıldızlar renkli renkli parladı. Sonra Elsa ile Olaf ağacın önünde mutlu mutlu dans etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve elinden yıldızlar yaptı"
   - Cümle 2: «Eldivenlerini çıkardı ve elinden yıldızlar yaptı.»
   - Açıklama: 'Elinden yıldız yaptı' eliyle yıldız yapmak yerine elini malzeme gibi gösteriyor; 'buzdan' ya da 'elleriyle' olmalı.
   - Açıklama: Yıldızlar elden yapılmaz; 'elleriyle yıldızlar yaptı' anlamı yanlış kuruluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0172` birebir aynı, ardından `@onarim: 13254d507b9df5eb1a6cc4cb0501c87d0380016b`, sonra gövde.

### Hikâye 12: tohum elsa-0174 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Kristoff
@tohum: elsa-0174
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'tabure', fiil 'ölçmek', sıfat 'hızlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Kristoff
@plan: hızlı koşarken tabureye çarptı ve buzlar düştü | özür diledi ve buzları toplayıp yeniden dizdi
@tohum: elsa-0174
Bir sabah Kristoff ormanda taburenin üstündeki buz parçalarını ölçüyordu. Elsa onun yanına çok hızlı koştu ve tabureye çarptı. Tabure devrildi ve buz parçaları karın içine düştü. Kristoff şaşırdı ve karda duran parçalara baktı. Elsa hemen onun yanına eğildi ve özür diledi. Sonra devrilen tabureyi kaldırdı ve yerine koydu. Elsa kraliçeydi ve Kristoff'un buzlarını korumak istedi. Buz parçalarını kardan tek tek ve yavaşça topladı. Elsa hepsini tabureye yeniden dizdi. Kristoff her parçayı bir daha ölçtü ve hiçbiri kırılmamıştı. Sonra Elsa ile Kristoff işlerine mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "onun yanına çok hızlı"
   - Cümle 2: «Elsa onun yanına çok hızlı koştu ve tabureye çarptı.»
   - Açıklama: 'onun yanına' kalıbı 2. ve 5. cümlede gereksizce tekrarlanıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa hemen onun yanına eğildi"
   - Cümle 5: «Elsa hemen onun yanına eğildi ve özür diledi.»
   - Açıklama: Birinin yanına eğilinmez; 'yanına çömeldi' ya da 'parçalara eğildi' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hemen onun yanına eğildi"
   - Cümle 5: «Elsa hemen onun yanına eğildi ve özür diledi.»
   - Açıklama: 'yanına eğilmek' yanlış; Elsa buzlara ya da yere eğilir.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ve Kristoff'un buzlarını korumak istedi"
   - Cümle 7: «Elsa kraliçeydi ve Kristoff'un buzlarını korumak istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız gerekçe olarak anılıyor, çözümde işe yaramıyor.
   - Açıklama: Kartın özellikler alanında kraliçelik kız kardeşini korumakla tanımlı; burada yalnız Kristoff'un buzlarını korumak için etiket gibi söyleniyor ve çözüme katkısı yok.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa kraliçeydi ve Kristoff'un buzlarını korumak istedi"
   - Cümle 7: «Elsa kraliçeydi ve Kristoff'un buzlarını korumak istedi.»
   - Açıklama: Kraliçe olması olaya hiçbir şey katmayan, akışı bölen işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0174` birebir aynı, ardından `@onarim: 75e735b6599c009fd67c7a64f3da8be51f446ba4`, sonra gövde.
