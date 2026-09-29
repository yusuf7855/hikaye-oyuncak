# Editör görevi (onarım): Örümcek Adam, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Örümcek Adam | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar11.txt --ad urun_v2`
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

## Kart: Örümcek Adam (kaynaklı, kapalı dünya)

- Ad: Örümcek Adam (okunuş: örümcek adam; kesme eki okunuşa uyar)
- Kimlik: Örümcek Adam, arkadaşlarıyla birlikte şehre yardım eden, ağ atabilen genç bir süper kahramandır.
- Tür: kahraman
- Güvenli özellik kullanımı: Ağ ve tırmanma yalnız süper güç olarak kullanılır; çocuğun taklit edebileceği ev içi tırmanma (dolap, masa, pencere, perde) yoktur; 'tehlike' yerine 'bir sorun olduğunu haber verir' yazılır. Kavga ve vurma yoktur.
- Özellikler:
  - ağ: Bileğinden ağ atar. (örnek biçimler: ağ, ağını, ağla)
  - tırman: Duvarlara tırmanabilir. (örnek biçimler: tırmandı, tırmanarak)
  - örümcek hissi: Örümcek hissi bir sorun olduğunu ona haber verir. (örnek biçimler: örümcek hissi)
- Yerler:
  - deniz: Şehrin kumsalı ve limanı.
  - park: Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.
  - ev: Takımın gizli evi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Ghost-Spider: Örümcek Adam'ın ve Spin'in arkadaşı; iyi davul çalar, kostümüyle havada süzülebilir. Tür: kahraman; konuşur. Yüzey biçimleri: Ghost-Spider
  - Spin: Örümcek Adam'ın en iyi arkadaşı; görünmez olabilir, çok güzel resim yapar. Tür: kahraman; konuşur. Yüzey biçimleri: Spin
  - Hulk: Takıma bazen yardım eden kocaman, yeşil ve çok güçlü bir süper kahraman. Tür: kahraman; konuşur. Yüzey biçimleri: Hulk
- Dünya kuralları:
  - 'Tehlike' kelimesi kullanılmaz; örümcek hissi bir sorun olduğunu haber verir.
  - Ev içinde eşyalara tırmanılmaz.
  - 'Üs' kelimesi kullanılmaz (çocuk 'üst' ile karıştırır); takımın yeri 'gizli ev' diye anlatılır.
  - Kavga, yumruk ve dövüş yoktur; sorun yardımla ve ağla çözülür.
- Yasak adlar: Spidey, Peter, Miles, Gwen, Ghosty, May, Rhino, Doc Ock, Goblin, Electro, Black Cat, Sandman, Black Panther, Iron Man, Lizard
- Yasak: Kötü karakterler, robotlar ve dev bilgisayar hikayeye girmez.
- İzinli dünya kelimeleri: ağ, kahraman, tırman, örümcek

## Onarılacak hikâyeler

### Hikâye 1: tohum orumcek_adam-0032 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0032
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: bir şey yapmak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'fotoğraf', fiil 'güldürmek', sıfat 'karmakarışık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: rüzgar resmi uçurdu ve kağıt dallara takıldı | duvara tırmanıp kağıdı dallardan aldı
@tohum: orumcek_adam-0032
@degisim: fotoğraf -> resim
Örümcek Adam ile Spin parkta büyük bir resim yapıyordu. Resimde çiçek bahçesi ve uçan kelebekler vardı. Birden rüzgar esti ve kağıdı havaya uçurdu. Kağıt bahçedeki taş duvarın üstündeki karmakarışık dallara takıldı. "Resim orada kaldı, onu nasıl alacağız?" diye sordu Spin. Örümcek Adam bir örümcek gibi duvara hızla tırmandı. Kağıdı dallardan yavaşça çıkardı ve yere indi. Resim hiç yırtılmamıştı. Spin resmin köşesine duvara tırmanan küçük bir Örümcek Adam çizdi. Bu komik resim Örümcek Adam'ı çok güldürdü. "Teşekkürler, Spin, bu çok eğlenceli oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "taş duvarın üstündeki karmakarışık dallara"
   - Cümle 4: «Kağıt bahçedeki taş duvarın üstündeki karmakarışık dallara takıldı.»
   - Açıklama: 'Karmakarışık' kelimesi 3 yaşındaki bir çocuk için zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0032` birebir aynı, `@degisim: fotoğraf -> resim` (tutuyorsan), ardından `@onarim: 215fa8ae99f56aaf1e0648971999ad59cd439c83`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0034 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0034
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'kitap', fiil 'kullanmak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: kitaptaki mor çiçek yüksek duvarın tepesindeydi | duvarın sağlam olduğuna baktı ve duvara tırmandı
@tohum: orumcek_adam-0034
Parkın çiçek bahçesinde Örümcek Adam bir çiçek kitabına bakıyordu. Kitapta küçük, mor bir çiçeğin resmi vardı. Birden yüksek bir duvarın tepesinde mor bir şey gördü. Ama duvar çok yüksekti ve Örümcek Adam onu iyi göremedi. Önce duvara eliyle dokundu. Duvar taştandı ve çok sağlamdı. Sonra Örümcek Adam gücünü kullandı ve duvara hızla tırmandı. Duvarın tepesinde küçük mor çiçekler açmıştı. Örümcek Adam kitabı açtı ve resme baktı. Çiçekler tıpkı resimdeki gibiydi. Örümcek Adam çiçeklere dokunmadı, onlara uzun uzun baktı. Sonra yavaşça aşağı indi. Örümcek Adam çok sevindi, çünkü kitaptaki çiçeği sonunda bulmuştu.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden yüksek bir duvarın tepesinde mor bir şey gördü.»
   - Açıklama: İlk üç cümlede sorun söylenmiyor; duvarın yüksekliği ancak 4. cümlede sorun oluyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yüksek bir duvarın tepesinde mor bir şey gördü"
   - Cümle 3: «Birden yüksek bir duvarın tepesinde mor bir şey gördü.»
   - Açıklama: Duvara tırmanabilen figür için yüksek duvar gerçek bir sorun değil ve çiçeği arama hedefi hiç kurulmuyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Örümcek Adam onu iyi göremedi"
   - Cümle 4: «Ama duvar çok yüksekti ve Örümcek Adam onu iyi göremedi.»
   - Açıklama: 'onu' zamirinin duvarı mı mor şeyi mi gösterdiği belli değil.
   - Açıklama: 'Onu' zamirinin duvarı mı mor şeyi mi gösterdiği belli değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Duvar taştandı ve çok sağlamdı"
   - Cümle 6: «Duvar taştandı ve çok sağlamdı.»
   - Açıklama: Duvarın sağlamlığını yoklayıp tırmanmak, güvenli kullanım satırının süper güç dışı tırmanma yasağına aykırı olarak çocuğun taklit edebileceği bir tırmanma örneği veriyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "gücünü kullandı ve duvara hızla tırmandı"
   - Cümle 7: «Sonra Örümcek Adam gücünü kullandı ve duvara hızla tırmandı.»
   - Açıklama: Duvarın sağlamlığını elle yoklayıp yüksek duvara tırmanmak, çocuğun taklit edebileceği bir yükseğe tırmanma örneği olarak sunuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0034` birebir aynı, ardından `@onarim: 7cb1b3609857d1b26ba35225d220e318cf085044`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0036 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0036
- yer: ev (Takımın gizli evi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'dilim', fiil 'açılmak', sıfat 'minicik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: yüksek pencere açıldı ve içeri yağmur girdi | arkadaşından yardım istedi ve o pencereyi kapadı
@tohum: orumcek_adam-0036
Örümcek Adam gizli evde bir dilim karpuz yiyordu. Birden örümcek hissi ile bir sorun olduğunu anladı. Evin yüksek penceresi rüzgarla açılmıştı ve içeri yağmur giriyordu. Pencere çok yüksekteydi ve Örümcek Adam evin içinde tırmanmak istemedi. "Ghost-Spider, bana yardım eder misin?" diye sordu Örümcek Adam. "Tabii, hemen geliyorum," dedi arkadaşı ve kostümüyle havada süzüldü. Pencerenin minicik kolunu çevirdi ve onu sıkıca kapadı. Yağmur artık içeri girmiyordu. Örümcek Adam arkadaşına da bir dilim karpuz verdi. Örümcek Adam çok mutluydu, çünkü arkadaşı ona hemen yardım etmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun"
   - Cümle 2: «Birden örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Örümcek Adam evin içinde tırmanmak istemedi"
   - Cümle 4: «Pencere çok yüksekteydi ve Örümcek Adam evin içinde tırmanmak istemedi.»
   - Açıklama: Tırmanabilen figürün tırmanmak istememesi sebepsiz; yardım istemeye giden adım olaydan çıkmıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onu sıkıca kapadı"
   - Cümle 7: «Pencerenin minicik kolunu çevirdi ve onu sıkıca kapadı.»
   - Açıklama: 'onu' zamirinin pencereyi mi kolu mu gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0036` birebir aynı, ardından `@onarim: 04c200da2c76b74d49520e970ca220d3c6e88fda`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0038 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0038
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'fındık', fiil 'kapamak', sıfat 'memnun'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: arkadan bilinmeyen bir tık tık sesi geldi | sesi izleyip devrilen torbayı buldu ve kapadı
@tohum: orumcek_adam-0038
@degisim: memnun -> mutlu
Örümcek Adam ile Ghost-Spider limanda denize bakıyordu. Arkadaşı fındık torbasını biraz geride bırakmıştı. Birden arkalarından tık tık diye bir ses geldi. Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı. İkisi hemen sesin geldiği yere yürüdü. Fındık torbası rüzgarda devrilmişti. Fındıklar tık tık yuvarlanıyor ve denize doğru gidiyordu. Örümcek Adam torbayı hemen kaldırdı ve sıkıca kapadı. İkisi yerdeki fındıkları tek tek topladı. Hiçbir fındık denize düşmedi. "Teşekkürler, Örümcek Adam!" dedi arkadaşı. "Sesi birlikte bulduk, ben de çok mutlu oldum!" dedi Örümcek Adam.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşı fındık torbasını biraz"
   - Cümle 2: «Arkadaşı fındık torbasını biraz geride bırakmıştı.»
   - Açıklama: İki kişi yeni tanıtılmışken 'Arkadaşı' kimi gösterdiği belirsiz, Ghost-Spider adıyla anılmıyor.
   - Açıklama: 'Arkadaşı' ile kimin kastedildiği belli değil; ad kullanılmamış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 4: «Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' 3 yaşındaki çocuğa soyut.
   - Açıklama: 'Örümcek hissi' soyut bir kavram; küçük çocuk anlamaz.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 6: «Fındık torbası rüzgarda devrilmişti.»
   - Açıklama: Asıl sorun olan devrilen torba ve denize yuvarlanan fındıklar ilk 3 cümlede değil ancak 6-7. cümlede söyleniyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "İkisi yerdeki fındıkları tek tek topladı"
   - Cümle 9: «İkisi yerdeki fındıkları tek tek topladı.»
   - Açıklama: Çözüm sese yürümek, torbayı kapamak ve fındıkları toplamak olarak ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0038` birebir aynı, `@degisim: memnun -> mutlu` (tutuyorsan), ardından `@onarim: b5192968cff7d101e25840ce9371b945c85943e0`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0040 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0040
- yer: ev (Takımın gizli evi.)
- tema: yağmur ya da kar günü
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'süs', fiil 'süslenmek', sıfat 'ışıltılı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: yağmur yüzünden parka gidemediler ve sıkıldılar | duvara tırmanıp süsleri arkadaşıyla birlikte astı
@tohum: orumcek_adam-0040
Dışarıda yağmur şıp şıp yağıyordu. Örümcek Adam ile Hulk bu yüzden parka gidemedi. İkisi gizli evde oturuyordu ve biraz sıkılmıştı. "Hulk, odayı süsleyelim mi?" diye sordu Örümcek Adam. "Evet, çok güzel olur!" dedi Hulk. Örümcek Adam dolaptan ışıltılı süslerle dolu bir kutu çıkardı. Hulk süsleri kapıya ve pencereye astı. Örümcek Adam da bir örümcek gibi duvara tırmandı. En büyük yıldız süsünü tavana taktı. Sonunda bütün oda süslendi. Süsler odada pırıl pırıl parlıyordu. "Yağmurlu gün bile çok eğlenceli oldu, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bir örümcek gibi duvara tırmandı"
   - Cümle 8: «Örümcek Adam da bir örümcek gibi duvara tırmandı.»
   - Açıklama: Güvenli özellik kullanımı satırı çocuğun taklit edebileceği ev içi tırmanmayı yasaklıyor; burada ev içinde tavana süs asmak için duvara tırmanılıyor.
   - Açıklama: Güvenli özellik kullanımı satırı çocuğun taklit edebileceği ev içi tırmanmayı yasaklar; gizli evin odasında duvara tırmanıp tavana süs takılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0040` birebir aynı, ardından `@onarim: 28dab55f1f7d7680f4e179e74cffd92506a04de8`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0042 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0042
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'tuz', fiil 'eğmek', sıfat 'hazır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: arkadaşı salıncağa binmek için arkada sessizce bekliyordu | arkasına baktı ve sırayı arkadaşına verdi
@tohum: orumcek_adam-0042
@degisim: tuz -> salıncak
Parkın oyun alanında tek bir salıncak vardı. Örümcek Adam salıncakta uzun uzun sallanıyordu. Hulk da binmek istiyordu ama arkada sessizce bekliyordu. Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. Örümcek Adam arkasına baktı ve arkadaşını gördü. Hulk başını eğmişti ve biraz üzgündü. Örümcek Adam hemen salıncaktan indi. "Sıra sende, Hulk! On kere sallan, sonra sıra bende," dedi Örümcek Adam. Hulk sevindi ve salıncağa oturdu. Örümcek Adam yüksek sesle saydı. Sonra yer değiştirdiler. "Hazır mısın, Örümcek Adam?" diye sordu Hulk ve o da saydı. İkisi sırayla sallandı ve çok güldü. "Sırayla oynamak çok eğlenceli, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: Örümcek hissinin haber vermesi soyut bir kavram ve mecaz; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: Soyut 'örümcek hissi' kavramı ve hissin haber vermesi mecazı 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0042` birebir aynı, `@degisim: tuz -> salıncak` (tutuyorsan), ardından `@onarim: ca6e1295e7016ca21747a1f43765e61e8c36e8d0`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0043 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0043
- yer: ev (Takımın gizli evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'boncuk', fiil 'solmak', sıfat 'cesur'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: boncuk kutusu dolabın arkasındaki dar boşluğa kaydı | ağ attı ve kutuyu dışarı çekti
@tohum: orumcek_adam-0043
@degisim: solmak -> kaymak
Gizli evde Örümcek Adam ile Spin cesur denizciler oyunu oynuyordu. Hazineleri boncuklarla dolu küçük bir kutuydu. Ama Spin koşarken masaya çarptı ve kutu dolabın arkasına kaydı. Dolabın arkasındaki boşluk çok dardı. Spin elini uzattı ama eli sığmadı. "Hazinemiz orada kaldı!" dedi Spin. "Merak etme, Spin," dedi Örümcek Adam. Örümcek Adam boşluğa doğru eğildi ve ağ attı. Ağ kutuya yapıştı. Örümcek Adam ağı yavaşça çekti ve kutu dışarı çıktı. Bütün boncuklar kutunun içindeydi. Spin sevinçle zıpladı ve kutuyu gemilerine koydu. "Hazineyi kurtardın, Örümcek Adam, teşekkürler!" dedi Spin.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Merak etme, Spin"
   - Cümle 7: «"Merak etme, Spin," dedi Örümcek Adam.»
   - Açıklama: 'Merak etme' kalıp ifadesi 'endişelenme' anlamında deyimsel.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kutuyu gemilerine koydu"
   - Cümle 12: «Spin sevinçle zıpladı ve kutuyu gemilerine koydu.»
   - Açıklama: Hikayede gemi yok; 'gemilerine' kelimesi yanlış ve belirsiz.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kutuyu gemilerine koydu"
   - Cümle 12: «Spin sevinçle zıpladı ve kutuyu gemilerine koydu.»
   - Açıklama: Gemi daha önce kurulmadan sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0043` birebir aynı, `@degisim: solmak -> kaymak` (tutuyorsan), ardından `@onarim: b242bc5256d5f86ef78f787ebc1f429c6feb8457`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0044 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0044
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gül', fiil 'aydınlanmak', sıfat 'sıkı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar kum gemisinin bayrağını yıkmak üzereydi | çubuğu kuma soktu ve bayrağı sıkı bağladı
@tohum: orumcek_adam-0044
@degisim: gül -> bayrak
Kumsalda güçlü bir rüzgar esiyordu. Örümcek Adam kumdan bir gemi yapmıştı ve gemi oyunu oynuyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Rüzgar gemideki bayrağın çubuğunu sallıyordu ve çubuk düşmek üzereydi. Örümcek Adam çubuğu hemen tuttu. Onu kuma daha derin soktu. Sonra bayrağın ipini çubuğa sıkı bir düğümle bağladı. Rüzgar yine esti ama bayrak düşmedi. Bir süre sonra bulutlar gitti ve kumsal aydınlandı. Örümcek Adam gemisinin önüne oturdu ve gülümsedi. Kırmızı bayrak rüzgarda sallanıyordu. Örümcek Adam çok mutluydu, çünkü gemisinin bayrağı yine yerinde duruyordu.
```

**Hakem bulguları (9):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yıkmak üzereydi"
   - Cümle 0 (plan satırı): «rüzgar kum gemisinin bayrağını yıkmak üzereydi | çubuğu kuma soktu ve bayrağı sıkı bağladı»
   - Açıklama: Bayrak yıkılmaz; 'devirmek' ya da 'düşürmek' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kum gemisinin bayrağını yıkmak üzereydi"
   - Cümle 0 (plan satırı): «rüzgar kum gemisinin bayrağını yıkmak üzereydi | çubuğu kuma soktu ve bayrağı sıkı bağladı»
   - Açıklama: Bayrak yıkılmaz; 'devirmek' ya da 'düşürmek' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım.
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatımdır.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede yalnız bir sorun olduğu söyleniyor; bayrak çubuğunun düşmek üzere olduğu ancak 4. cümlede açıklanıyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kuma daha derin soktu"
   - Cümle 6: «Onu kuma daha derin soktu.»
   - Açıklama: Yönelme eki eksik; 'daha derine' olmalı.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Onu kuma daha derin soktu"
   - Cümle 6: «Onu kuma daha derin soktu.»
   - Açıklama: Yön eki eksik; 'daha derine' olmalı.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra bayrağın ipini çubuğa sıkı bir düğümle bağladı"
   - Cümle 7: «Sonra bayrağın ipini çubuğa sıkı bir düğümle bağladı.»
   - Açıklama: Çözüm tutma, derine sokma ve ipi bağlama olarak üç adım sürüyor ve ipi bağlamak çubuğun düşmesine yönelmiyor.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir süre sonra bulutlar gitti"
   - Cümle 9: «Bir süre sonra bulutlar gitti ve kumsal aydınlandı.»
   - Açıklama: Daha önce hiç anılmayan bulutlar sebepsiz beliriyor ve olaya hiçbir katkısı yok.
9. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir süre sonra bulutlar gitti ve kumsal aydınlandı"
   - Cümle 9: «Bir süre sonra bulutlar gitti ve kumsal aydınlandı.»
   - Açıklama: Daha önce hiç bulut söz konusu değilken bulutlar sebepsiz beliriyor ve olayda işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0044` birebir aynı, `@degisim: gül -> bayrak` (tutuyorsan), ardından `@onarim: 02f2efd48c4992ff27f2f4842a733a7bb0cf2435`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0045 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0045
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'ayna', fiil 'köpürmek', sıfat 'şirin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: ikisi de tek çubuğu aynı anda çekti | şişeyi tuttu ve sırayla oynamayı önerdi
@tohum: orumcek_adam-0045
@degisim: ayna -> baloncuk
Parkta hafif bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider baloncuk yapmak istiyordu ama tek bir çubukları vardı. İkisi de çubuğu aynı anda tuttu ve çekti. Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. Bankın üstündeki sabunlu su şişesi sallanıyordu ve düşmek üzereydi. Örümcek Adam çubuğu bıraktı ve şişeyi tuttu. "Sırayla yapalım, önce sen," dedi Örümcek Adam. Arkadaşı çubuğu şişeye soktu ve sabunlu su köpürdü. Sonra çubuğa üfledi ve şirin, küçük baloncuklar havaya uçtu. Sıra Örümcek Adam'a geldi ve o da kocaman bir baloncuk yaptı. İkisi parkta sırayla baloncuk yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' soyut, çocuğa uygun olmayan bir anlatım.
   - Açıklama: Hissin haber vermesi mecazdır ve 'örümcek hissi' 3 yaşındaki çocuğun bilmeyeceği soyut bir kavramdır.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: Şişe olayı sebepsiz beliriyor ve çubuk sorununun çözümüyle bağı yok.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "sabunlu su şişesi sallanıyordu ve düşmek üzereydi"
   - Cümle 5: «Bankın üstündeki sabunlu su şişesi sallanıyordu ve düşmek üzereydi.»
   - Açıklama: Çubuk kavgasının yanında düşmek üzere olan şişe ikinci bir sorun olarak ekleniyor.
   - Açıklama: Çubuk kavgasının yanına düşmek üzere olan şişe ikinci bir sorun olarak ekleniyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "şişesi sallanıyordu ve düşmek üzereydi"
   - Cümle 5: «Bankın üstündeki sabunlu su şişesi sallanıyordu ve düşmek üzereydi.»
   - Açıklama: Çubuk kavgasının yanına düşmek üzere olan şişe ikinci bir sorun olarak ekleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Örümcek Adam çubuğu bıraktı ve şişeyi tuttu"
   - Cümle 6: «Örümcek Adam çubuğu bıraktı ve şişeyi tuttu.»
   - Açıklama: Paylaşma sorunu, sebepsizce beliren şişe olayı yüzünden tesadüfen çözülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0045` birebir aynı, `@degisim: ayna -> baloncuk` (tutuyorsan), ardından `@onarim: 398f7e6c8f9fa371c6be7a2bb8b2812214e73442`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0046 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0046
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'tekne', fiil 'kaybetmek', sıfat 'zarif'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar hafif tekneleri çalıya doğru itiyordu | tekneleri rüzgarın geldiği yerden suya bıraktı
@tohum: orumcek_adam-0046
@degisim: zarif -> hafif
Bir sabah parkta hafif bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider bir su birikintisinde kağıt tekne yarışı yapıyordu. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Rüzgar hafif tekneleri suyun kenarındaki çalıya doğru itiyordu. Örümcek Adam tekneleri çalıda kaybetmek istemedi. Hemen iki tekneyi de sudan aldı. Onları suyun öbür kenarına götürdü ve suya bıraktı. Şimdi rüzgar tekneleri çalıdan uzağa itti. Yarışta Örümcek Adam'ın teknesi kendi etrafında döndü. Arkadaşı buna çok güldü. Örümcek Adam yarışı kaybetti ama o da güldü. Örümcek Adam bundan sonra tekneleri hep rüzgarın geldiği yerden suya bıraktı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi Örümcek Adam'a"
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuk için anlaşılır değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yarışta Örümcek Adam'ın teknesi kendi etrafında döndü"
   - Cümle 9: «Yarışta Örümcek Adam'ın teknesi kendi etrafında döndü.»
   - Açıklama: Teknenin kendi etrafında dönmesi sebepsiz beliren, çözülen sorunla bağı olmayan yeni bir olay.
   - Açıklama: Çözümden sonra teknenin sebepsizce kendi etrafında dönmesi olaydan çıkmayan yeni bir olay ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0046` birebir aynı, `@degisim: zarif -> hafif` (tutuyorsan), ardından `@onarim: d51e5a73eddb1d52d5338861df4542b919729d4b`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0047 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0047
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: kaybolan eşya
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'salıncak', fiil 'taşmak', sıfat 'siyah'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar siyah kovayı yuvarladı ve kova kayboldu | kumdaki izi takip etti ve kovayı buldu
@tohum: orumcek_adam-0047
@degisim: salıncak -> kova
Örümcek Adam kumsalda kumdan bir kale yapıyordu. O sırada rüzgar siyah kovasını yuvarladı ve uzağa götürdü. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam yanına baktı ama kovası yoktu. Sonra kumda uzun bir iz gördü. Örümcek Adam izi yavaş yavaş takip etti. İz onu suyun kenarına götürdü. Siyah kova orada, kumun üstünde yatıyordu. Dalgalar kovayı suyla doldurmuştu ve su kovadan taşmıştı. Örümcek Adam kovayı aldı ve suyunu boşalttı. Sonra kalesinin yanına geri döndü. Kovayla kalesine yeni bir kule yaptı. Örümcek Adam çok sevindi, çünkü kaybolan kovasını kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi mecaz ve 'örümcek hissi' ile 'sorun' 3 yaşındaki çocuğa soyut.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dalgalar kovayı suyla doldurmuştu ve su kovadan taşmıştı"
   - Cümle 9: «Dalgalar kovayı suyla doldurmuştu ve su kovadan taşmıştı.»
   - Açıklama: Dalgaların kovayı doldurması sorunla ilgisiz, sonradan eklenmiş işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0047` birebir aynı, `@degisim: salıncak -> kova` (tutuyorsan), ardından `@onarim: afa21c2e09d6823ae988fa7647e8c735162df11a`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0049 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0049
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'havlu', fiil 'küçültmek', sıfat 'tuhaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: sürpriz balonlardan birinin ipi duvara takıldı | duvara tırmanıp balonu aldı ve banka bağladı
@tohum: orumcek_adam-0049
@degisim: küçültmek -> bağlamak
Bir sabah Örümcek Adam parkta Spin için bir sürpriz hazırlıyordu. Çimlere büyük bir havlu serdi ve üstüne kurabiyeler koydu. Ama sonra tuhaf bir şey gördü, bankın yanındaki üç balondan biri yoktu. Balonun ipi çözülmüştü ve balon duvarın üstüne takılmıştı. Örümcek Adam hemen duvarın yanına koştu. Gücüyle duvara hızla tırmandı. Balonun ipini dikkatle çözdü ve aşağı indi. Sonra ipi banka sıkıca bağladı. Az sonra Spin parka geldi. "Sürpriz, Spin!" dedi Örümcek Adam. Spin havluyu, kurabiyeleri ve üç balonu gördü. "Teşekkürler, Örümcek Adam, bu çok güzel bir sürpriz!" dedi Spin.
```

**Hakem bulguları (3):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "tuhaf bir şey gördü, bankın yanındaki"
   - Cümle 3: «Ama sonra tuhaf bir şey gördü, bankın yanındaki üç balondan biri yoktu.»
   - Açıklama: Açıklama bildiren ikinci cümleden önce virgül yerine iki nokta gerekir.
   - Açıklama: Açıklama yapan ikinci cümle virgülle değil iki noktayla ayrılmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Gücüyle duvara hızla tırmandı"
   - Cümle 6: «Gücüyle duvara hızla tırmandı.»
   - Açıklama: 'Gücüyle' neyi anlattığı belirsiz ve bu bağlamda yerinde kullanılmamış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Gücüyle duvara hızla tırmandı"
   - Cümle 6: «Gücüyle duvara hızla tırmandı.»
   - Açıklama: 'Gücüyle' soyut bir kavram ve 3 yaşındaki çocuğa somut bir şey anlatmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0049` birebir aynı, `@degisim: küçültmek -> bağlamak` (tutuyorsan), ardından `@onarim: d7df889e1e6fe917ae6aadaada0580852996d674`, sonra gövde.
