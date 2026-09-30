# Editör görevi (onarım): Elsa, onarım partisi 55

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar55.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar55.txt --ad urun_v2`
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

### Hikâye 1: tohum elsa-0169 (deneme 3 -> 4)

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
Bir sabah Elsa dağda sarayının önünde oynuyordu. Bugün yemek oyunu oynayıp kardan bir pasta yapacaktı. Ama pastayı koyacak bir tabağı yoktu. Elsa etrafına baktı ama yerde yalnız yumuşak kar vardı. Sonra ellerini açtı ve buzdan yuvarlak bir tabak yaptı. Bir yığın karı kucakladı ve tabağa koydu. Karı elleriyle bastırıp büyük bir pasta yaptı. Pastanın üstüne sos gibi ince, beyaz kar serpti. Pasta tabağın üstünde güzelce durdu. Elsa pastasına bakıp güldü. Elsa çok sevindi, çünkü oyununda ilk pastasını yapmıştı.
```

**Hakem bulguları (3):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Bugün yemek oyunu oynayıp"
   - Cümle 2: «Bugün yemek oyunu oynayıp kardan bir pasta yapacaktı.»
   - Açıklama: Geçmiş anlatımda 'bugün' zaman kaymasına yol açıyor; 'o gün' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bir yığın karı kucakladı"
   - Cümle 6: «Bir yığın karı kucakladı ve tabağa koydu.»
   - Açıklama: Kar kucaklanmaz; 'avuçladı' ya da 'topladı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sos gibi ince, beyaz"
   - Cümle 8: «Pastanın üstüne sos gibi ince, beyaz kar serpti.»
   - Açıklama: 'Sos gibi' benzetmesi küçük çocuk için mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0169` birebir aynı, `@degisim: ekşi -> beyaz` (tutuyorsan), ardından `@onarim: 6070038094376e3ce0bd7db0d0de7aaaa6ee103f`, sonra gövde.

### Hikâye 2: tohum elsa-0171 (deneme 3 -> 4)

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
@plan: rüzgar gümüş tacı karların içine uçurdu | parlak yeri görüp geyikle karı kazdı
@tohum: elsa-0171
@degisim: anlaşmak -> kazmak
Elsa ile Sven karlı dağda yürüyordu. Birden güçlü bir rüzgar esti ve Elsa'nın gümüş kraliçe tacı başından uçtu. Taç derin karların içine düştü ve kayboldu. Elsa karlara baktı ama tacı göremedi. Düşünceli bir yüzle rüzgarın estiği yöne baktı. Orada karın içinde küçük, parlak bir şey gördü. Elsa, Sven'e o yeri gösterdi. Sven koştu ve ayaklarıyla karı kazdı. Elsa da eliyle karı açtı. Taç karın altında parlıyordu. Elsa tacını taktı ve Sven'in başını okşadı. Sonra Elsa ile Sven dağda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa'nın gümüş kraliçe tacı"
   - Cümle 2: «Birden güçlü bir rüzgar esti ve Elsa'nın gümüş kraliçe tacı başından uçtu.»
   - Açıklama: Tohumdaki kraliçe özelliği (kraliçedir; kız kardeşini korur) yalnız taç sıfatı olarak geçiyor, çözümde işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Düşünceli bir yüzle rüzgarın"
   - Cümle 5: «Düşünceli bir yüzle rüzgarın estiği yöne baktı.»
   - Açıklama: 'Düşünceli bir yüzle' soyut bir anlatım ve küçük çocuğa ağır geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0171` birebir aynı, `@degisim: anlaşmak -> kazmak` (tutuyorsan), ardından `@onarim: b3fbbdad43f8155127eb29d358067f43bc25dbdc`, sonra gövde.

### Hikâye 3: tohum elsa-0172 (deneme 3 -> 4)

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
Elsa karlı ormanda büyük bir ağacı buzdan yıldızlarla süslüyordu. Eldivenlerini çıkardı ve elleriyle yeni yıldızlar yaptı. Ama ağacın arkasında sık çalılar vardı ve Elsa oraya geçemiyordu. "Olaf, bana yardım eder misin?" diye sordu Elsa. "Tabii, Elsa!" dedi Olaf. Elsa, Olaf'a beş yıldız verdi. Olaf çalıların altından ağacın arkasına geçti. Yıldızları dallara tek tek astı ve saydı. "Bir, iki, üç, dört, beş!" dedi Olaf. Olaf çalıların altından geri geldi. Güneş çıktı ve yıldızlar renkli renkli parladı. Sonra Elsa ile Olaf ağacın önünde mutlu mutlu dans etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "elleriyle yeni yıldızlar yaptı"
   - Cümle 2: «Eldivenlerini çıkardı ve elleriyle yeni yıldızlar yaptı.»
   - Açıklama: Tohumdaki buz özelliği yalnız süs için iki kez kullanılıyor, sorunu (çalılar) çözmüyor; çözüm Olaf'tan geliyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Olaf çalıların altından ağacın arkasına geçti"
   - Cümle 7: «Olaf çalıların altından ağacın arkasına geçti.»
   - Açıklama: Tohumdaki buz özelliği sorunu çözmek için kullanılmıyor; çalı sorununu Olaf'ın yardımı çözüyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yıldızlar renkli renkli parladı"
   - Cümle 11: «Güneş çıktı ve yıldızlar renkli renkli parladı.»
   - Açıklama: 'Renkli renkli' gereksiz tekrar; 'rengarenk' ya da tek 'renkli' yeterli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0172` birebir aynı, ardından `@onarim: 5cd518e107cfba516ef17ebfd95f369cacb4de34`, sonra gövde.

### Hikâye 4: tohum elsa-0174 (deneme 3 -> 4)

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
Bir sabah Kristoff ormanda taburenin üstündeki buz parçalarını ölçüyordu. Kraliçe Elsa oraya çok hızlı koştu ve tabureye çarptı. Tabure devrildi ve buz parçaları karın içine düştü. Kristoff şaşırdı ve karda duran parçalara baktı. Elsa hemen durdu ve Kristoff'tan özür diledi. Sonra devrilen tabureyi kaldırdı ve yerine koydu. Buz parçalarını kardan tek tek ve yavaşça topladı. Elsa hepsini tabureye yeniden dizdi. Kristoff her parçayı bir daha ölçtü. Hiçbir parça kırılmamıştı. Sonra Elsa ile Kristoff işlerine mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa oraya çok hızlı koştu"
   - Cümle 2: «Kraliçe Elsa oraya çok hızlı koştu ve tabureye çarptı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız unvan olarak geçiyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "işlerine mutlu mutlu devam etti"
   - Cümle 11: «Sonra Elsa ile Kristoff işlerine mutlu mutlu devam etti.»
   - Açıklama: Elsa'nın hiçbir işi kurulmadığı için son cümle olaya bağlı olmayan, zayıf bir kapanış veriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0174` birebir aynı, ardından `@onarim: 1d91278c58c25b28a411d7dae7ff4f3e55c5d630`, sonra gövde.

### Hikâye 5: tohum elsa-0176 (deneme 3 -> 4)

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
@plan: geyiğin boynuzları iki dalın arasına takıldı | durmasını söyledi ve dalı kenara itti
@tohum: elsa-0176
@degisim: cetvel -> dal
Rüzgar hafifçe esiyordu. Kraliçe Elsa karlı ormanda Sven ile yürüyordu. Sven iki dalın arasındaki küçücük yerden geçmek istedi ama boynuzları takıldı. Sven başını çekti ama kurtulamadı. Dal her seferinde Sven'in başına değiyordu. Elsa hemen Sven'in yanına koştu. "Sven, dur ve başını yavaşça aşağı indir," dedi Elsa. Sven durdu ve başını indirdi. Elsa takılan dalı eliyle kenara itti. Sven'in boynuzları daldan kolayca çıktı. Sven sevinçle zıpladı ve Elsa'ya sokuldu. "Aferin, Sven, beni çok güzel dinledin!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa karlı ormanda"
   - Cümle 2: «Kraliçe Elsa karlı ormanda Sven ile yürüyordu.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartın özellik alanındaki gibi (kız kardeşini korur) işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0176` birebir aynı, `@degisim: cetvel -> dal` (tutuyorsan), ardından `@onarim: 6756cd27cb3b7aff0b4743b665151404edfd8427`, sonra gövde.

### Hikâye 6: tohum elsa-0178 (deneme 3 -> 4)

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
@plan: kavun yokuştan aşağı yuvarlandı | buzdan alçak bir duvar yapıp kavunu durdurdu
@tohum: elsa-0178
Ormanda aydınlık bir sabahtı. Elsa ile Olaf karda piknik oyunu oynuyordu ve Olaf bir kavun getirmişti. Ama Olaf kavunu yokuşa bıraktı ve kavun aşağı yuvarlandı. "Eyvah, kavun yuvarlanıyor!" diye bağırdı Olaf. Elsa hemen elini salladı. Yokuşun sonunda buzdan alçak bir duvar yaptı. Kavun duvara hafifçe çarptı ve durdu. Olaf koşup kavunu aldı ve güldü. "Teşekkürler, Elsa, kavun durdu!" dedi Olaf. Sonra ikisi piknik oyununa mutlu mutlu devam etti. Olaf bundan sonra kavunu hep düz bir yere yatırdı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kavunu hep düz bir yere yatırdı"
   - Cümle 11: «Olaf bundan sonra kavunu hep düz bir yere yatırdı.»
   - Açıklama: Kavun için 'yatırmak' uygun değil; 'koydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0178` birebir aynı, ardından `@onarim: 68dcc068e30558fb7b5dfa9c948b38c96fed1634`, sonra gövde.

### Hikâye 7: tohum elsa-0180 (deneme 3 -> 4)

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
Bir sabah Elsa karlı ormanda yürüyordu. Yolun başında sarayı gösteren eski bir tahta vardı. Ama tahta çok kirliydi ve üstündeki ok görünmüyordu. Okun ucundaki mavi mücevher de parlamıyordu. Tahta böyle kalırsa ormana gelenler yolunu kaybedecekti. Elsa bu krallığın kraliçesiydi ve tahtayı temizlemek istedi. Temiz karla tahtayı iyice sildi. Ok yeniden göründü ve mavi mücevher güneşte parladı. Elsa birkaç adım geri gitti ve baktı. Parlayan mücevher ağaçların arasından uzaktan görünüyordu. Elsa çok sevindi, çünkü artık herkes sarayın yolunu kolayca bulacaktı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama tahta çok kirliydi"
   - Cümle 3: «Ama tahta çok kirliydi ve üstündeki ok görünmüyordu.»
   - Açıklama: Tahtanın neden kirlendiği hiç söylenmiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tahta çok kirliydi"
   - Cümle 3: «Ama tahta çok kirliydi ve üstündeki ok görünmüyordu.»
   - Açıklama: Tahtanın neden kirlendiği söylenmiyor; sorunun sebebi verilmemiş.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ormana gelenler yolunu kaybedecekti"
   - Cümle 5: «Tahta böyle kalırsa ormana gelenler yolunu kaybedecekti.»
   - Açıklama: Çoğul özneyle iyelik uyumu eksik; 'yollarını' olmalı.
   - Açıklama: Çoğul özne 'gelenler' ile tekil iyelik uyuşmuyor; 'yollarını' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0180` birebir aynı, ardından `@onarim: e037c6be4757263d3f7a75fce679a5d908959c82`, sonra gövde.

### Hikâye 8: tohum elsa-0181 (deneme 3 -> 4)

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
Bir sabah Kraliçe Elsa ile Sven dağda, buz sarayının önündeydi. Sven'in çektiği küçük kızakta güzel kokan havuçlar vardı. Sven havuçlara ulaşmak isterken ağacın etrafında döndü ve ip ağaca sarıldı. Şimdi Sven ne öne ne de arkaya gidebiliyordu. Sven başını salladı ve komik bir ses çıkardı. Elsa gülümsedi ve Sven'in önüne geçti. "Sven, dur ve ağacın etrafında ters yöne bir kez dön," dedi Elsa. Sven hemen ters yöne döndü. İp ağaçtan çözüldü ve kızak yeniden serbest kaldı. Elsa kızaktan bir havuç aldı ve Sven'e verdi. "Aferin, Sven, şimdi afiyetle ye!" dedi Elsa.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bir sabah Kraliçe Elsa"
   - Cümle 1: «Bir sabah Kraliçe Elsa ile Sven dağda, buz sarayının önündeydi.»
   - Açıklama: Tohum özelliği kraliçelik yalnız unvan olarak geçiyor, kartta tarif edildiği gibi işe yarar kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak anılıyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0181` birebir aynı, `@degisim: iplik -> ip` (tutuyorsan), ardından `@onarim: f07700cdbc8081ab30711b9e4ff3400f75323e97`, sonra gövde.

### Hikâye 9: tohum elsa-0183 (deneme 3 -> 4)

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
@degisim: savrulmak -> dökülmek
Elsa, kardeşi Anna ile karlı ormanda yürüyordu. Birden yakından garip bir tık tık sesi geldi. Karda da yıldız gibi küçük delikler vardı. "Elsa, bu ses nereden geliyor?" diye sordu Anna. Anna sese doğru koşmak istedi. Elsa kraliçeydi ve kardeşini korumak için Anna'nın elini tuttu. Deliklerin hep bir ağacın altında olduğunu gördü. "Anna, koşma, dur ve ağacın dallarına bak," dedi Elsa. Anna durdu ve başını kaldırdı. Rüzgar esince dallardan mor yemişler döküldü. Yemişler dallara çarptı ve aynı sesi çıkardı. Her yemiş karda bir delik açtı. "Sesi bu yemişler yapıyormuş!" dedi Anna. Elsa çok sevindi, çünkü sesin nereden geldiğini kardeşiyle bulmuştu.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kardeşini korumak için Anna'nın elini tuttu"
   - Cümle 6: «Elsa kraliçeydi ve kardeşini korumak için Anna'nın elini tuttu.»
   - Açıklama: Aynı kişi cümlede hem 'kardeşini' hem 'Anna'nın' diye gereksiz yere iki kez anılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kardeşini korumak için Anna'nın elini tuttu"
   - Cümle 6: «Elsa kraliçeydi ve kardeşini korumak için Anna'nın elini tuttu.»
   - Açıklama: Ortada bir tehlike yokken koruma ayrıntısı sebepsiz ekleniyor ve olayda işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0183` birebir aynı, `@degisim: savrulmak -> dökülmek` (tutuyorsan), ardından `@onarim: 339cda66de112f45441c8531bb828d8fadf21a29`, sonra gövde.

### Hikâye 10: tohum elsa-0185 (deneme 3 -> 4)

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
Limanda Elsa ile Kristoff yan yana oturuyordu. Önlerindeki taşta iki bardak içecek ve reçelli ekmek vardı. Elsa suyun üstünde süzülen kuşları gösterirken Kristoff'un bardağını devirdi. İçecek döküldü ve bardak boş kaldı. Elsa kraliçeydi ama hatasını hemen söyledi. "Özür dilerim, Kristoff, dikkat etmedim," dedi Elsa. Elsa kendi bardağını aldı ve içeceğin yarısını Kristoff'a verdi. "Kristoff, al, yarısı senin," dedi Elsa. "Teşekkür ederim, Elsa," dedi Kristoff ve gülümsedi. Elsa ile Kristoff reçelli ekmeklerini yiyip kuşları mutlu mutlu izlediler.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa kraliçeydi ama hatasını hemen söyledi"
   - Cümle 5: «Elsa kraliçeydi ama hatasını hemen söyledi.»
   - Açıklama: Kraliçelik ile hatayı kabul etmek arasındaki karşıtlık 3 yaşındaki çocuk için soyut bir kavramdır.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Elsa kraliçeydi ama hatasını"
   - Cümle 5: «Elsa kraliçeydi ama hatasını hemen söyledi.»
   - Açıklama: Tohumdaki kraliçe özelliği yalnız bir niteleme olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0185` birebir aynı, ardından `@onarim: bd096d757988b2f51aadff437828e6002070cf20`, sonra gövde.

### Hikâye 11: tohum elsa-0189 (deneme 3 -> 4)

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
@plan: çamur kız kardeşinin boncuklarını kirletti | kendi boncuklarını kardeşiyle paylaştı
@tohum: elsa-0189
@degisim: devasa -> büyük
Deniz kıyısında Elsa ile Anna boncuklarla kolye yapıyordu. Birden Anna'nın kutusu yere düştü. Yerdeki çamur bütün boncukları kirletti ve Anna'nın kolyesi yarım kaldı. Anna çok üzüldü ve kirli boncuklara baktı. Elsa kraliçeydi ve kardeşini üzgün görmek istemedi. Hemen kendi kutusunu açtı. Boncuklarını ikiye ayırdı ve yarısını Anna'ya verdi. Kutuda büyük, mavi bir boncuk da vardı. Elsa onu da kardeşine verdi. Anna mavi boncuğu kolyesinin ortasına taktı ve güldü. Sonra Elsa ile Anna kolyelerini mutlu mutlu bitirdi.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Elsa onu da kardeşine verdi"
   - Cümle 9: «Elsa onu da kardeşine verdi.»
   - Açıklama: Paylaşımla sorun çözülmüşken mavi boncuk ek bir adım olarak ekleniyor ve çözüm iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0189` birebir aynı, `@degisim: devasa -> büyük` (tutuyorsan), ardından `@onarim: b63c66dd815301cecff765451855fccc3249505c`, sonra gövde.

### Hikâye 12: tohum elsa-0190 (deneme 3 -> 4)

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
@plan: dağda soğuk olduğu için hiç çiçek açmıyordu | buzdan çiçekler yapıp karın içine dikti
@tohum: elsa-0190
@degisim: hevesli -> güzel
Karlı dağın tepesinde Elsa bir oyun oynuyordu. Oyunda sarayın önüne güzel bir bahçe yapmak istiyordu. Ama dağ çok soğuktu ve orada hiç çiçek açmıyordu. Elsa karlı yere bakıp biraz düşündü. Sonra elinden çıkan buzla parlak çiçekler ve küçük bir kürek yaptı. Ayağıyla küreğe bastı ve karda küçük çukurlar açtı. Çiçekleri tek tek çukurlara dikti. Güneşte buz çiçekleri ışıl ışıl parladı. Sarayın önünde bir çiçek bahçesi oldu. Elsa, soğuk dağda da kendi çiçeklerini yapabileceğini öğrendi.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "küçük bir kürek yaptı"
   - Cümle 5: «Sonra elinden çıkan buzla parlak çiçekler ve küçük bir kürek yaptı.»
   - Açıklama: Çözüm buz çiçekleri yapmak, kürekle çukur açmak ve çiçekleri dikmek olarak iki adımı aşıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "buzla parlak çiçekler ve küçük bir kürek yaptı"
   - Cümle 5: «Sonra elinden çıkan buzla parlak çiçekler ve küçük bir kürek yaptı.»
   - Açıklama: Çözüm çiçek ve kürek yapma, çukur açma ve dikme olarak ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0190` birebir aynı, `@degisim: hevesli -> güzel` (tutuyorsan), ardından `@onarim: a369fa0f092a1878319ebcd67aeff3a21970fa04`, sonra gövde.
