# Editör görevi (onarım): Elsa, onarım partisi 31

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar31.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar31.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0084 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0084
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'eşarp', fiil 'yaratmak', sıfat 'temiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: rüzgar kardan arkadaşın en üstteki topunu düşürdü | topu yerine koyup boynuna eşarp bağladı
@tohum: elsa-0084
@degisim: yaratmak -> yapmak
Rüzgar karlı ağaçların arasında çok sert esiyordu. Elsa ile Olaf ormanda kardan küçük bir arkadaş yapıyordu. Ama rüzgar arkadaşın en üstteki kar topunu yere düşürdü. "Kar topu düştü, Elsa!" dedi Olaf üzgün üzgün. Kraliçe Elsa yeni arkadaşı rüzgardan korumak istedi. Boynunda uzun, temiz bir eşarp vardı. Hemen Olaf'ın yanına eğildi. Topu yerine koydu ve karı iki eliyle bastırdı. Sonra eşarbını boynundan çıkardı. Eşarbı yeni arkadaşın boynuna sıkıca bağladı. Rüzgar yine esti ama top artık düşmedi. "Yaşasın, yeni arkadaşım hazır!" dedi Olaf. Elsa ile Olaf yeni arkadaşın yanında mutlu mutlu dans etti.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa yeni arkadaşı"
   - Cümle 5: «Kraliçe Elsa yeni arkadaşı rüzgardan korumak istedi.»
   - Açıklama: Zaten tanıtılmış Elsa unvanla yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa yeni arkadaşı rüzgardan korumak"
   - Cümle 5: «Kraliçe Elsa yeni arkadaşı rüzgardan korumak istedi.»
   - Açıklama: Kartta özellik kız kardeşini korumak iken Elsa kardan bir figürü koruyor; özellik karttaki gibi kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa yeni arkadaşı rüzgardan"
   - Cümle 5: «Kraliçe Elsa yeni arkadaşı rüzgardan korumak istedi.»
   - Açıklama: Tohumdaki özellik kız kardeşini korumak; burada unvan olarak geçip kardan figürü korumaya kaydırılıyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Boynunda uzun, temiz bir eşarp vardı"
   - Cümle 6: «Boynunda uzun, temiz bir eşarp vardı.»
   - Açıklama: Önceki cümlede yeni arkadaş da geçtiği için 'boynunda' kimin boynunu gösterdiği belli değil.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Eşarbı yeni arkadaşın boynuna sıkıca bağladı"
   - Cümle 10: «Eşarbı yeni arkadaşın boynuna sıkıca bağladı.»
   - Açıklama: Boyna bağlanan eşarbın başı rüzgardan nasıl koruduğu belirsiz ve çözüm topu koyma, bastırma ve eşarp bağlamayla ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0084` birebir aynı, `@degisim: yaratmak -> yapmak` (tutuyorsan), ardından `@onarim: 95397ea6103a974a1cf9a0caf69124e8d404a6d2`, sonra gövde.

### Hikâye 2: tohum elsa-0085 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0085
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'ekmek', fiil 'dilemek', sıfat 'siyah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: kurabiye torbası kaygan karda kayıp aşağıdaki kara düştü | geyikten yardım istedi ve geyik torbayı getirdi
@tohum: elsa-0085
@degisim: ekmek -> kurabiye
Karlı dağın tepesinde, buzdan sarayın önünde güneş parlıyordu. Kraliçe Elsa, Sven için siyah bir torbada kurabiye getirmişti. Ama torba kaygan karda kaydı ve biraz aşağıdaki karın içine düştü. Elsa oraya gidemedi, çünkü ayakları yumuşak karda batıyordu. Elsa torbanın geri gelmesini diledi. "Sven, torbayı getirir misin?" diye sordu Elsa. Sven uzun bacaklarıyla karda kolayca yürüdü. Siyah torbayı beyaz karda hemen gördü. Torbayı dişleriyle tuttu ve yukarı çıktı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Sven sevinçle başını salladı. Sonra ikisi sarayın önünde oturdu ve kurabiyeleri mutlu mutlu paylaştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa, Sven için"
   - Cümle 2: «Kraliçe Elsa, Sven için siyah bir torbada kurabiye getirmişti.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik kraliçelik (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0085` birebir aynı, `@degisim: ekmek -> kurabiye` (tutuyorsan), ardından `@onarim: a36f51531b5660ffe98e639d5cbfa7f3e2bdd49b`, sonra gövde.

### Hikâye 3: tohum elsa-0087 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0087
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kese', fiil 'kullanmak', sıfat 'berrak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: keseyi bağlayan ipte çok sıkı bir düğüm vardı | düğümü açmak için arkadaşından yardım istedi
@tohum: elsa-0087
@degisim: berrak -> mavi
Elsa, Kristoff ile karlı dağda yürüyordu. Elsa kurabiye yemek için küçük bir keseyi açmak istedi. Ama keseyi bağlayan ipte çok sıkı bir düğüm vardı. Elsa düğümü tek başına açamadı. "Kristoff, bu düğümü açabilir misin?" diye sordu Elsa. Kristoff keseyi aldı ve güçlü parmaklarını kullandı. İpi yavaşça çekti ve düğüm açıldı. "İşte kurabiyeler, Kraliçe Elsa!" dedi Kristoff. Elsa kurabiyeleri ikiye böldü ve yarısını Kristoff'a verdi. İkisi mavi gökyüzünün altında kurabiyelerini yedi. Elsa çok mutlu oldu, çünkü yardım isteyince düğüm hemen açılmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "İşte kurabiyeler, Kraliçe Elsa!"
   - Cümle 8: «"İşte kurabiyeler, Kraliçe Elsa!" dedi Kristoff.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız hitap olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik kraliçelik (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0087` birebir aynı, `@degisim: berrak -> mavi` (tutuyorsan), ardından `@onarim: a2ee87b11cc49d41c37501902b4aeb143504d6b9`, sonra gövde.

### Hikâye 4: tohum elsa-0093 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0093
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yama', fiil 'üzülmek', sıfat 'rüzgarlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: uçurtma sivri bir kayaya çarpıp delindi | kuyruğundan bir parça koparıp deliğe yama yaptı
@tohum: elsa-0093
Bir sabah Elsa ile Sven rüzgarlı dağda uçurtma uçuruyordu. Elsa ipi tutuyordu ve Sven de yanında koşuyordu. Ama uçurtma sivri bir kayaya çarptı ve kağıdında bir delik açıldı. Uçurtma yere düştü ve Elsa çok üzüldü. Sven de başını önüne eğdi. Kraliçe Elsa arkadaşını hemen sevindirmek istedi. "Üzülme, Sven, bunu düzeltebiliriz," dedi Elsa. Elsa uçurtmanın uzun kuyruğundan küçük bir parça kopardı. Parçayı deliğin üstüne koydu ve iki ucunu çubuğa sıkıca bağladı. Böylece delik kapandı ve güzel bir yama oldu. Rüzgar yine esti ve uçurtma havaya yükseldi. Sven sevinçle zıpladı. Sonra Elsa ile Sven uçurtmayı mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa arkadaşını hemen"
   - Cümle 6: «Kraliçe Elsa arkadaşını hemen sevindirmek istedi.»
   - Açıklama: Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa arkadaşını hemen sevindirmek"
   - Cümle 6: «Kraliçe Elsa arkadaşını hemen sevindirmek istedi.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik kraliçelik (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0093` birebir aynı, ardından `@onarim: 91f5858e802f5196b65d470bb6910e58c551727b`, sonra gövde.

### Hikâye 5: tohum elsa-0095 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Elsa | şato | -
@tohum: elsa-0095
- yer: şato (Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'turp', fiil 'süpürmek', sıfat 'zeki'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | şato | -
@plan: taşlar düz değildi ve turp yarı yolda duruyordu | elinden buz çıkarıp kaygan bir kaydırak yaptı
@tohum: elsa-0095
@degisim: zeki -> kaygan
Şatoda tık tık diye bir ses duyuluyordu. Elsa orada yuvarlak bir turpu bir sepete doğru yuvarlıyordu. Ama yerdeki taşlar düz değildi ve turp hep yarı yolda duruyordu. Turp taşlara tık tık çarpıyordu. Elsa bu oyunu çok seviyordu. Yeri süpürdü ve yine denedi, ama turp bir taşa takıldı. Elsa biraz düşündü. Sonra elinden buz çıkardı ve küçük, kaygan bir kaydırak yaptı. Kaydırağın ucu sepetin içine iniyordu. Elsa turpu kaydırağın üstüne koydu. Turp buzun üstünde hızla kaydı ve sepetin içine girdi. Elsa sevinçle ellerini çırptı. Sonra turpu geri aldı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yuvarlak bir turpu bir sepete doğru yuvarlıyordu"
   - Cümle 2: «Elsa orada yuvarlak bir turpu bir sepete doğru yuvarlıyordu.»
   - Açıklama: Şatoda bir turpu sepete yuvarlama oyunu saçma bir olay, sorun çocuğun önemseyeceği akla yatkın bir şeye dayanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0095` birebir aynı, `@degisim: zeki -> kaygan` (tutuyorsan), ardından `@onarim: d4bff0b7ab3de844dc9aab02b14f850f53e460f1`, sonra gövde.

### Hikâye 6: tohum elsa-0097 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Olaf
@tohum: elsa-0097
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Olaf
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'balon', fiil 'şaşırtmak', sıfat 'kolay'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | Olaf
@plan: rüzgar kırmızı balonu denize doğru çekiyordu | ipi kardan adamın koluna sarıp düğüm yaptı
@tohum: elsa-0097
Limanın kıyısında serin bir rüzgar esiyordu. Kraliçe Elsa ile Olaf orada gemi oyunu oynuyordu. Ama rüzgar, Olaf'ın kırmızı balonunu denize doğru çekiyordu. Olaf'ın ince dal kolları ipi zor tutuyordu. Elsa hemen Olaf'ın yanına koştu. Elsa ipi Olaf'ın koluna iki kez sardı ve sıkıca bağladı. Rüzgar yine esti, ama balon artık kaçmadı. Bu kolay düğüm Olaf'ı çok şaşırttı. Sonra Olaf balonunu sallayarak kıyıda yürüdü. Elsa çok sevindi, çünkü Olaf oyuna balonuyla devam edebiliyordu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa ile Olaf"
   - Cümle 2: «Kraliçe Elsa ile Olaf orada gemi oyunu oynuyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki özellik kraliçelik (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0097` birebir aynı, ardından `@onarim: ec343504c1c65d74c5d8d89f043a75eda48f3c3a`, sonra gövde.

### Hikâye 7: tohum elsa-0098 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0098
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'köfte', fiil 'dizmek', sıfat 'hazır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: ağaç dallarından köftelerin üstüne kar düşüyordu | kardeşine tabağı açık bir yere götürmesini söyledi
@tohum: elsa-0098
Karlı ormanda güzel bir gündü. Anna, Kraliçe Elsa ile piknik yapmak için bir tabak köfte getirmişti. Ama tabak bir ağacın altındaydı ve dallardan köftelerin üstüne kar düşüyordu. Anna karı eliyle sildi, ama bu sırada başına da kar düştü. Elsa kardeşini korumak için hemen yanına geldi. "Anna, tabağı al ve benimle o açık yere gel," dedi Elsa. Anna, Elsa'yı dinledi ve tabağı açık yere taşıdı. Orada hiç ağaç yoktu ve tabağa kar düşmedi. Elsa köftelerin üstündeki karı temizledi ve onları tabakta güzelce dizdi. Sonra iki kardeş yan yana oturdu. "Teşekkürler, Elsa, piknik sonunda hazır!" dedi Anna.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "onları tabakta güzelce dizdi"
   - Cümle 9: «Elsa köftelerin üstündeki karı temizledi ve onları tabakta güzelce dizdi.»
   - Açıklama: Dizmek fiili yönelme ister; 'tabağa dizdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0098` birebir aynı, ardından `@onarim: 101f7cf23058fdfe13d1bf6d774c63b9e5514608`, sonra gövde.
