# Editör görevi (onarım): Elsa, onarım partisi 30

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar30.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0078 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0078
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kristoff
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'sünger', fiil 'yakalanmak', sıfat 'sihirli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: karda her yerde ayak izi vardı ve saklanan bulunamadı | kar yağdırıp eski izleri kapattı ve yeni izleri buldu
@tohum: elsa-0078
@degisim: sünger -> kaya
Elsa ile Kristoff dağda saklambaç oynuyordu. Kristoff kayaların arkasına saklanmıştı. Ama karda her yerde eski ayak izleri vardı ve Elsa onu bulamadı. Elsa biraz düşündü ve ellerini gökyüzüne kaldırdı. Ellerinden buz taneleri ve sihirli bir kar yağdı. Yeni kar bütün eski izleri kapattı. Kar Kristoff'un başına da yağdı ve Kristoff başka bir kayanın arkasına kaçtı. Bu kez karda yalnız onun yeni ayak izleri vardı. Elsa izlerin peşinden gitti ve Kristoff'u buldu. "Tamam, yakalandım!" dedi Kristoff gülerek. Elsa çok sevindi, çünkü saklanan Kristoff'u sonunda bulmuştu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kar Kristoff'un başına da yağdı"
   - Cümle 7: «Kar Kristoff'un başına da yağdı ve Kristoff başka bir kayanın arkasına kaçtı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre güç canlıya yöneltilmemeli; yağdırılan kar Kristoff'un başına yağıyor ve o kaçıyor.
   - Açıklama: Güvenli özellik kullanımı satırına göre güç hiçbir canlıyı üşütmemeli; kar bir kişinin üstüne yağdırılıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kristoff başka bir kayanın arkasına kaçtı"
   - Cümle 7: «Kar Kristoff'un başına da yağdı ve Kristoff başka bir kayanın arkasına kaçtı.»
   - Açıklama: Elsa'nın çözümü ancak Kristoff'un tesadüfen yer değiştirmesiyle işe yarıyor; çözüm tek başına sebebe yönelip sonuç vermiyor.
   - Açıklama: Kar eski izleri kapatınca Kristoff'un izleri de kaybolur; Elsa'yı sonuca götüren kendi çözümü değil Kristoff'un rastlantısal kaçışı oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0078` birebir aynı, `@degisim: sünger -> kaya` (tutuyorsan), ardından `@onarim: 7dbfd7608001f7d12571663ce20655fe1c4010b2`, sonra gövde.

### Hikâye 2: tohum elsa-0080 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0080
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kutu', fiil 'sevmek', sıfat 'biberli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik çok acıkmıştı çünkü karın altında ot yoktu | kutudaki havuçları ona verdi
@tohum: elsa-0080
Elsa elinde bir yemek kutusuyla sarayından çıktı. Kapının önünde Sven burnuyla karı karıştırıyordu. Karın altında hiç ot yoktu ve Sven çok acıkmıştı. Elsa bir kraliçeydi ve Sven'i korumak istedi. Hemen kutusunu açtı. Kutunun içinde üstte biberli ekmekler, altta havuçlar vardı. Sven bir ekmeği kokladı ve başını çevirdi. "Biberli ekmeği sevmiyorsun, değil mi?" diye sordu Elsa. Sven başını iki yana salladı. Elsa ekmekleri kaldırdı ve iki havucu aldı. Havuçları Sven'e uzattı. Sven onları yedi ve sevinçle zıpladı. "Afiyet olsun, Sven, bunlar senin için!" dedi Elsa gülerek.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Elsa elinde bir yemek kutusuyla sarayından çıktı"
   - Cümle 1: «Elsa elinde bir yemek kutusuyla sarayından çıktı.»
   - Açıklama: Başlıktaki yer dağ olduğu halde hikaye sarayın kapısında geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sven'i korumak istedi"
   - Cümle 4: «Elsa bir kraliçeydi ve Sven'i korumak istedi.»
   - Açıklama: Sven bir tehlikede değil, aç; 'korumak' yerine 'doyurmak' ya da 'yardım etmek' gibi bir fiil gerekir.
   - Açıklama: Aç geyiğe yemek vermek korumak değildir; 'korumak' fiili bağlama uymuyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve Sven'i korumak istedi"
   - Cümle 4: «Elsa bir kraliçeydi ve Sven'i korumak istedi.»
   - Açıklama: Kartta kraliçe özelliği kız kardeşi korumaktır; özellik adı sayılıp Sven'e havuç vermeye yamanıyor.
   - Açıklama: Karttaki özellik kız kardeşini korumaktır; kraliçelik çözümde işe yarar biçimde kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa bir kraliçeydi ve Sven'i korumak istedi"
   - Cümle 4: «Elsa bir kraliçeydi ve Sven'i korumak istedi.»
   - Açıklama: Kraliçe olması olayda hiçbir işe yaramayan, sebepsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0080` birebir aynı, ardından `@onarim: a4ebf455bfc071c5b9150544d52f3e7540855654`, sonra gövde.

### Hikâye 3: tohum elsa-0084 (deneme 4 -> 5)

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
Rüzgar karlı ağaçların arasında çok sert esiyordu. Elsa ile Olaf ormanda kardan küçük bir arkadaş yapıyordu. Ama rüzgar arkadaşın en üstteki kar topunu yere düşürdü. "Kar topu düştü, Elsa!" dedi Olaf üzgün üzgün. Elsa bir kraliçeydi ve boynunda uzun, temiz bir eşarp vardı. Hemen Olaf'ın yanına eğildi. Topu yerine koydu ve karı iki eliyle bastırdı. Sonra eşarbını boynundan çıkardı. Eşarbı yeni arkadaşın boynuna sıkıca bağladı. Rüzgar yine esti ama top artık düşmedi. "Yaşasın, yeni arkadaşım hazır!" dedi Olaf. Elsa ile Olaf yeni arkadaşın yanında mutlu mutlu dans etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Elsa bir kraliçeydi ve"
   - Cümle 5: «Elsa bir kraliçeydi ve boynunda uzun, temiz bir eşarp vardı.»
   - Açıklama: Zaten tanıtılmış olan Elsa hikayenin ortasında yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve boynunda"
   - Cümle 5: «Elsa bir kraliçeydi ve boynunda uzun, temiz bir eşarp vardı.»
   - Açıklama: Kraliçe özelliği yalnız söylenip geçiliyor, kartın 'kız kardeşini korur' özelliği işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi ve boynunda uzun"
   - Cümle 5: «Elsa bir kraliçeydi ve boynunda uzun, temiz bir eşarp vardı.»
   - Açıklama: Tohumdaki kraliçe özelliği kartın özellik alanındaki gibi kız kardeşi korumak için değil, eşarp için anılıyor ve işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0084` birebir aynı, `@degisim: yaratmak -> yapmak` (tutuyorsan), ardından `@onarim: a31fb85fe1f96b46e1efaf700584d04cc03e400d`, sonra gövde.

### Hikâye 4: tohum elsa-0085 (deneme 4 -> 5)

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
@plan: kurabiye torbası kaygan karda kayıp aşağıdaki kara düştü | geyikten yardım diledi ve geyik torbayı getirdi
@tohum: elsa-0085
@degisim: ekmek -> kurabiye
Karlı dağın tepesinde, buzdan sarayın önünde güneş parlıyordu. Elsa, Sven için siyah bir torbada kurabiye getirmişti. Ama torba kaygan karda kaydı ve biraz aşağıdaki karın içine düştü. Elsa oraya gidemedi, çünkü ayakları yumuşak karda batıyordu. Elsa bir kraliçeydi, ama "Sven, torbayı getirir misin?" diye yardım diledi. Sven uzun bacaklarıyla karda kolayca yürüdü. Siyah torbayı beyaz karda hemen gördü. Torbayı dişleriyle tuttu ve yukarı çıktı. "Teşekkürler, Sven, sen çok iyi bir arkadaşsın," dedi Elsa. Sven sevinçle başını salladı. Sonra ikisi sarayın önünde oturdu ve kurabiyeleri mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Elsa bir kraliçeydi, ama"
   - Cümle 5: «Elsa bir kraliçeydi, ama "Sven, torbayı getirir misin?" diye yardım diledi.»
   - Açıklama: 'Kraliçeydi, ama' bağlacıyla kurulan cümle bozuk ve anlamsız bir karşıtlık kuruyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "diye yardım diledi"
   - Cümle 5: «Elsa bir kraliçeydi, ama "Sven, torbayı getirir misin?" diye yardım diledi.»
   - Açıklama: 'Yardım dilemek' bir arkadaştan istemek için uygun değil; 'yardım istedi' olmalı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi, ama"
   - Cümle 5: «Elsa bir kraliçeydi, ama "Sven, torbayı getirir misin?" diye yardım diledi.»
   - Açıklama: Kraliçe özelliği yalnız anılıyor; kartın 'kız kardeşini korur' özelliği işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği kartın özellik alanındaki gibi kullanılmıyor, yalnız söylenip geçiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0085` birebir aynı, `@degisim: ekmek -> kurabiye` (tutuyorsan), ardından `@onarim: 7bc1b3b3f53f6d162fbb6505d91b89815ef3a4da`, sonra gövde.

### Hikâye 5: tohum elsa-0087 (deneme 4 -> 5)

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
Elsa, Kristoff ile karlı dağda yürüyordu. Elsa kurabiye yemek için küçük bir keseyi açmak istedi. Ama keseyi bağlayan ipte çok sıkı bir düğüm vardı. Elsa bir kraliçeydi, ama düğümü tek başına açamadı. "Kristoff, bu düğümü açabilir misin?" diye sordu Elsa. Kristoff keseyi aldı ve güçlü parmaklarını kullandı. İpi yavaşça çekti ve düğüm açıldı. "İşte kurabiyeler, Elsa!" dedi Kristoff. Elsa kurabiyeleri ikiye böldü ve yarısını Kristoff'a verdi. İkisi mavi gökyüzünün altında kurabiyelerini yedi. Elsa çok mutlu oldu, çünkü yardım isteyince düğüm hemen açılmıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa bir kraliçeydi, ama düğümü"
   - Cümle 4: «Elsa bir kraliçeydi, ama düğümü tek başına açamadı.»
   - Açıklama: 'Ama' bağlacı kraliçelik ile düğüm açma arasında olmayan bir karşıtlık kuruyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa bir kraliçeydi, ama düğümü tek başına açamadı"
   - Cümle 4: «Elsa bir kraliçeydi, ama düğümü tek başına açamadı.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız anılıyor, kartın özellik satırındaki gibi kardeşini korumak için işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği işe yarar biçimde kullanılmıyor, yalnız anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0087` birebir aynı, `@degisim: berrak -> mavi` (tutuyorsan), ardından `@onarim: 7bdec79977a2b3f76dae5b0a1d8870a17188833b`, sonra gövde.

### Hikâye 6: tohum elsa-0093 (deneme 4 -> 5)

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
Bir sabah Kraliçe Elsa ile Sven rüzgarlı dağda uçurtma uçuruyordu. Elsa ipi tutuyordu ve Sven de yanında koşuyordu. Ama uçurtma sivri bir kayaya çarptı ve kağıdında bir delik açıldı. Uçurtma yere düştü ve Elsa çok üzüldü. Sven de başını önüne eğdi. Elsa uçurtmaya dikkatle baktı. "Üzülme, Sven, bunu düzeltebiliriz," dedi Elsa. Elsa uçurtmanın uzun kuyruğundan küçük bir parça kopardı. Parçayı deliğin üstüne koydu ve güzel bir yama yaptı. Rüzgar yine esti ve uçurtma havaya yükseldi. Sven sevinçle zıpladı. Sonra Elsa ile Sven uçurtmayı mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa ile Sven rüzgarlı dağda uçurtma uçuruyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın 'kız kardeşini korur' özelliği hiç kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Parçayı deliğin üstüne koydu ve güzel bir yama yaptı"
   - Cümle 9: «Parçayı deliğin üstüne koydu ve güzel bir yama yaptı.»
   - Açıklama: Parça deliğin üstüne yalnız konuyor, hiçbir şekilde tutturulmuyor; çözümün deliği nasıl kapattığı akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0093` birebir aynı, ardından `@onarim: 510a0de5375424911cd16a64411775e6eb115162`, sonra gövde.

### Hikâye 7: tohum elsa-0095 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: taşlar düz değildi ve turp yarı yolda duruyordu | elinden buz çıkarıp yere kaygan bir yol yaptı
@tohum: elsa-0095
@degisim: zeki -> kaygan
Şatoda tık tık diye bir ses duyuluyordu. Elsa orada yuvarlak bir turpu bir sepete doğru yuvarlıyordu. Ama yerdeki taşlar düz değildi. Turp taşlara tık tık çarpıyor ve hep yarı yolda duruyordu. Elsa bu oyunu çok seviyordu. Yeri süpürdü ve yine denedi, ama turp bir taşa takıldı. Elsa biraz düşündü. Sonra elinden buz çıkardı ve yere kaygan bir yol yaptı. Buz yolu turpun önünden sepete kadar uzandı. Elsa turpu hafifçe itti. Turp buzun üstünde hızla kaydı ve sepetin içine girdi. Elsa sevinçle ellerini çırptı. Sonra turpu geri aldı ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Turp taşlara tık tık çarpıyor ve hep yarı yolda duruyordu"
   - Cümle 4: «Turp taşlara tık tık çarpıyor ve hep yarı yolda duruyordu.»
   - Açıklama: Turpun sepete ulaşamaması sorunu ancak dördüncü cümlede açıkça söyleniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yere kaygan bir yol yaptı"
   - Cümle 8: «Sonra elinden buz çıkardı ve yere kaygan bir yol yaptı.»
   - Açıklama: Şatonun yerine kaygan buz döşemek kaymaya yol açabilecek, güvenli kullanım satırındaki 'kar yağdırır, buzdan şekil yapar' kapsamını aşan bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0095` birebir aynı, `@degisim: zeki -> kaygan` (tutuyorsan), ardından `@onarim: 495b42d7ac0867ccf0955b358ee29e166979fc69`, sonra gövde.

### Hikâye 8: tohum elsa-0097 (deneme 3 -> 4)

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
Limanın kıyısında serin bir rüzgar esiyordu. Kraliçe Elsa ile Olaf orada gemi oyunu oynuyordu. Ama rüzgar, Olaf'ın kırmızı balonunu denize doğru çekiyordu. Olaf'ın ince dal kolları ipi zor tutuyordu. Elsa, Olaf'ın balonunu korumak için hemen yanına koştu. Elsa ipi Olaf'ın koluna iki kez sardı ve sıkıca bağladı. Rüzgar yine esti, ama balon artık kaçmadı. Bu kolay düğüm Olaf'ı çok şaşırttı. Sonra Olaf balonunu sallayarak kıyıda yürüdü. Elsa çok sevindi, çünkü Olaf oyuna balonuyla devam edebiliyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Olaf'ın balonunu korumak için"
   - Cümle 5: «Elsa, Olaf'ın balonunu korumak için hemen yanına koştu.»
   - Açıklama: Kartta kraliçe özelliği kız kardeşi korumaktır; burada balonu korumaya kaydırılmış ve kraliçelik işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Olaf'ın balonunu korumak için hemen"
   - Cümle 5: «Elsa, Olaf'ın balonunu korumak için hemen yanına koştu.»
   - Açıklama: Karttaki özellik kız kardeşini korumaktır; kraliçelik çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0097` birebir aynı, ardından `@onarim: 21405d2f5d08c6cc7e53a6bde8911dcfc0f01769`, sonra gövde.

### Hikâye 9: tohum elsa-0098 (deneme 3 -> 4)

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
Karlı ormanda güzel bir gündü. Anna, Kraliçe Elsa ile piknik yapmak için bir tabak köfte getirmişti. Ama tabak bir ağacın altındaydı ve dallardan köftelerin üstüne kar düşüyordu. Anna karı eliyle sildi, ama dallardan onun başına da kar düştü. Elsa kardeşini korumak için hemen yanına geldi. "Anna, tabağı al ve benimle o açık yere gel," dedi Elsa. Anna, Elsa'yı dinledi ve tabağı açık yere taşıdı. Orada hiç ağaç yoktu ve tabağa kar düşmedi. Elsa köftelerin üstündeki karı temizledi ve onları tabakta güzelce dizdi. Sonra iki kardeş yan yana oturdu. "Teşekkürler, Elsa, piknik sonunda hazır!" dedi Anna.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onun başına da kar"
   - Cümle 4: «Anna karı eliyle sildi, ama dallardan onun başına da kar düştü.»
   - Açıklama: Özne Anna iken 'onun' zamiri başka birini gösteriyor gibi belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0098` birebir aynı, ardından `@onarim: 1ed02d18e4cc373d1e047d1582bf9def368f4ae7`, sonra gövde.
