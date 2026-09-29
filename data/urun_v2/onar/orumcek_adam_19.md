# Editör görevi (onarım): Örümcek Adam, onarım partisi 19

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar19.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar19.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0032 (deneme 4 -> 5)

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
@plan: rüzgar fotoğrafı uçurdu ve fotoğraf dallara takıldı | duvara tırmanıp fotoğrafı dallardan aldı
@tohum: orumcek_adam-0032
@degisim: karmakarışık -> yüksek
Örümcek Adam ile Spin parkta büyük bir resim yapıyordu. Spin bir çiçek fotoğrafına bakıyor ve çiçekler çiziyordu. Birden rüzgar esti ve fotoğrafı havaya uçurdu. Fotoğraf parktaki taş duvarın üstündeki yüksek dallara takıldı. "Onu nasıl alacağız?" diye sordu Spin. Örümcek Adam bir örümcek gibi duvara hızla tırmandı. Fotoğrafı dallardan yavaşça çıkardı ve yere indi. Spin fotoğrafa baktı ve son çiçeği de çizdi. Sonra resmin köşesine duvara tırmanan küçük bir Örümcek Adam çizdi. Bu komik çizim Örümcek Adam'ı çok güldürdü. "Teşekkürler, Spin, bu çok eğlenceli oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir örümcek gibi duvara"
   - Cümle 6: «Örümcek Adam bir örümcek gibi duvara hızla tırmandı.»
   - Açıklama: Benzetme küçük çocuk için mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0032` birebir aynı, `@degisim: karmakarışık -> yüksek` (tutuyorsan), ardından `@onarim: 7d761a462455efb2e4be21c6483dfed7c0d14086`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0036 (deneme 5 -> 6)

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
@plan: yüksek pencere açıldı ve içeri yağmur girdi | arkadaşından yardım istedi, arkadaşı pencereyi kapadı
@tohum: orumcek_adam-0036
Örümcek Adam gizli evde bir dilim karpuz yiyordu. Birden örümcek hissi ile bir sorun olduğunu anladı. Örümcek Adam döndü ve rüzgarla açılan pencereden yağmurun girdiğini gördü. Pencere çok yüksekteydi ve evin içinde tırmanmak yasaktı. "Ghost-Spider, bana yardım eder misin?" diye sordu Örümcek Adam. "Tabii, geliyorum," dedi arkadaşı. Arkadaşı havada süzüldü ve pencereyi kapadı. Sonra pencerenin minicik kolunu sıkıca çevirdi. Yağmur artık içeri girmiyordu. Örümcek Adam arkadaşına da bir dilim karpuz verdi. Örümcek Adam çok mutluydu, çünkü arkadaşı ona hemen yardım etmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 2: «Birden örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ile bir sorun"
   - Cümle 2: «Birden örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'bir sorun olduğunu anladı' soyut bir kavram; 3 yaşındaki çocuk bunu bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0036` birebir aynı, ardından `@onarim: 6e4c7f74cefdd89d049aed9c20bd3ddf4416fe2b`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0040 (deneme 5 -> 6)

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
Dışarıda yağmur şıp şıp yağıyordu. Örümcek Adam ile Hulk bu yüzden parka gidemedi. İkisi gizli evlerinde oturuyordu ve biraz sıkılmıştı. "Hulk, evi süsleyelim mi?" diye sordu Örümcek Adam. "Evet, çok güzel olur!" dedi Hulk. Örümcek Adam dolaptan ışıltılı süslerle dolu bir kutu çıkardı. Hulk süsleri kapıya ve pencereye astı. Örümcek Adam en büyük yıldız süsünü aldı. Süper gücüyle duvara tırmandı ve yıldızı tavana taktı. Sonunda bütün ev süslendi. Süsler pırıl pırıl parlıyordu. "Yağmurlu gün bile çok eğlenceli oldu, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Süper gücüyle duvara tırmandı ve yıldızı tavana taktı"
   - Cümle 9: «Süper gücüyle duvara tırmandı ve yıldızı tavana taktı.»
   - Açıklama: Kartın güvenli özellik kullanımı satırı ev içi tırmanmayı yasaklıyor; evin duvarına tırmanıp tavana süs asmak çocuğun taklit edebileceği bir davranış.
   - Açıklama: Ev içinde süs asmak için tavana tırmanmak, güvenli özellik kullanımı satırındaki ev içi tırmanma yasağına aykırıdır ve taklit edilebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0040` birebir aynı, ardından `@onarim: 1c32ec97e6695a990f1d81325093b465f6c1a80a`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0042 (deneme 4 -> 5)

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
Parkın oyun alanında tek bir salıncak vardı. Örümcek Adam salıncakta uzun uzun sallanıyordu. Hulk da binmek istiyordu ama arkada sessizce bekliyordu. Birden Örümcek Adam örümcek hissiyle arkada bir sorun olduğunu anladı. Örümcek Adam arkasına baktı ve arkadaşını gördü. Hulk başını eğmişti ve biraz üzgündü. Örümcek Adam hemen salıncaktan indi. "Sıra sende, Hulk! On kere sallan, sonra sıra bende," dedi Örümcek Adam. Hulk sevindi ve salıncağa oturdu. Örümcek Adam yüksek sesle saydı. Sonra yer değiştirdiler. "Hazır mısın, Örümcek Adam?" diye sordu Hulk. Bu kez Hulk saydı. İkisi sırayla sallandı ve çok güldü. "Sırayla oynamak çok eğlenceli, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle arkada bir sorun"
   - Cümle 4: «Birden Örümcek Adam örümcek hissiyle arkada bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' soyut ve çocuk için anlaşılmaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "arkada bir sorun olduğunu anladı"
   - Cümle 4: «Birden Örümcek Adam örümcek hissiyle arkada bir sorun olduğunu anladı.»
   - Açıklama: 'Sorun' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Örümcek Adam arkasına baktı"
   - Cümle 5: «Örümcek Adam arkasına baktı ve arkadaşını gördü.»
   - Açıklama: Art arda cümlelerde 'Örümcek Adam' adı gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0042` birebir aynı, `@degisim: tuz -> salıncak` (tutuyorsan), ardından `@onarim: c16173e783af3b1b4563f9ea31282d88290e5c64`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0044 (deneme 4 -> 5)

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
@plan: rüzgar kum gemisinin bayrağını düşürmek üzereydi | çubuğu tuttu ve kuma daha derine itti
@tohum: orumcek_adam-0044
@degisim: gül -> bayrak
Kumsal güneşle aydınlanmıştı ve güçlü bir rüzgar esiyordu. Örümcek Adam kumdan bir gemi yapmıştı ve gemi oyunu oynuyordu. Birden örümcek hissiyle rüzgarın gemideki bayrağı düşürmek üzere olduğunu anladı. Bayrağın çubuğu kumda sağa sola eğiliyordu. Örümcek Adam çubuğu hemen sıkı sıkı tuttu ve kuma daha derine itti. Çubuk artık kumda dik durdu. Rüzgar yine esti ama bayrak düşmedi. Örümcek Adam gemisinin önüne oturdu ve gülümsedi. Kırmızı bayrak rüzgarda sallanıyordu. Örümcek Adam çok mutluydu, çünkü gemisinin bayrağı yine yerinde duruyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle rüzgarın"
   - Cümle 3: «Birden örümcek hissiyle rüzgarın gemideki bayrağı düşürmek üzere olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0044` birebir aynı, `@degisim: gül -> bayrak` (tutuyorsan), ardından `@onarim: 3f701912632e6030ab6918c7b746c33692f495d0`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0046 (deneme 4 -> 5)

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
@plan: rüzgar hafif tekneleri çalıya doğru itiyordu | tekneleri çalısı olmayan başka bir suya götürdü
@tohum: orumcek_adam-0046
@degisim: zarif -> hafif
Bir sabah parkta hafif bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider bir su birikintisinde kağıt tekne yarışı yapıyordu. Birden örümcek hissi ile rüzgarın tekneleri çalıya götürdüğünü anladı. Örümcek Adam tekneleri çalıda kaybetmek istemedi. Hemen iki tekneyi de sudan aldı. Onları çalısı olmayan başka bir su birikintisine götürdü ve suya bıraktı. Bu kez rüzgar tekneleri suyun öbür kenarına itti. Yarışta arkadaşının teknesi daha hızlı gitti. Arkadaşı sevinçle güldü. Örümcek Adam yarışı kaybetti ama o da güldü. Örümcek Adam bundan sonra tekneleri çalıdan uzak suya bıraktı ve çok eğlendi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ile"
   - Cümle 3: «Birden örümcek hissi ile rüzgarın tekneleri çalıya götürdüğünü anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; küçük çocuk için anlaşılır değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Birden örümcek hissi ile rüzgarın"
   - Cümle 3: «Birden örümcek hissi ile rüzgarın tekneleri çalıya götürdüğünü anladı.»
   - Açıklama: İki kahraman varken anlayanın kim olduğu belli değil; özne eksik.
   - Açıklama: Önceki cümlede iki kahraman var; kimin anladığı belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissi ile rüzgarın tekneleri çalıya götürdüğünü anladı"
   - Cümle 3: «Birden örümcek hissi ile rüzgarın tekneleri çalıya götürdüğünü anladı.»
   - Açıklama: Kartın özellik alanında örümcek hissi yalnız bir sorun olduğunu haber verir, burada ise rüzgarın tekneleri nereye götürdüğünü ayrıntılı bilgi olarak veriyor.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Örümcek Adam bundan sonra tekneleri"
   - Cümle 11: «Örümcek Adam bundan sonra tekneleri çalıdan uzak suya bıraktı ve çok eğlendi.»
   - Açıklama: Son cümle bir ders cümlesi değil, sonraki zamana atlayan bir eylem ve eğlence anlatımı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0046` birebir aynı, `@degisim: zarif -> hafif` (tutuyorsan), ardından `@onarim: 9bf493d0f69ad37235424495aa933f5429fcda45`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0047 (deneme 4 -> 5)

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
@plan: rüzgar siyah kovayı sürükledi ve kova kayboldu | kumdaki izi takip etti ve kovayı buldu
@tohum: orumcek_adam-0047
@degisim: salıncak -> kova
Örümcek Adam kumsalda kumdan bir kale yapıyordu. O sırada rüzgar siyah kovasını sürükledi ve uzağa götürdü. Bunu görmedi ama örümcek hissi ile bir sorun olduğunu anladı. Hemen yanına baktı ve kovasının yerinde olmadığını gördü. Sonra kumda uzun bir iz gördü. Örümcek Adam izi yavaş yavaş takip etti. İz suyun kenarına kadar gidiyordu. Siyah kova orada duruyordu. Dalgalar kovayı doldurmuştu ve su kovadan taşmıştı. Örümcek Adam kovayı aldı ve kalesinin yanına geri döndü. Kovadaki suyu kuma döktü. Islak kumla kalesine yeni bir kule yaptı. Örümcek Adam çok sevindi, çünkü kaybolan kovasını kendisi bulmuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun"
   - Cümle 3: «Bunu görmedi ama örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' soyut ifadeler; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 3: «Bunu görmedi ama örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'bir sorun olduğunu anladı' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' soyut ifadeler, 3 yaşındaki çocuğa uygun değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bunu görmedi ama örümcek"
   - Cümle 3: «Bunu görmedi ama örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: Son özne rüzgar olduğu için 'görmedi' fiilinin öznesi belirsiz kalıyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bunu görmedi ama"
   - Cümle 3: «Bunu görmedi ama örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: Önceki cümlenin öznesi rüzgar olduğu için 'görmedi' fiilinin öznesi belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0047` birebir aynı, `@degisim: salıncak -> kova` (tutuyorsan), ardından `@onarim: 2d2c6b838c5b1a53b2e6642704cd7137f8834dcb`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0049 (deneme 4 -> 5)

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
@plan: rüzgar bir balonun ipini çözdü ve balon duvara takıldı | duvara tırmanıp balonu aldı ve banka bağladı
@tohum: orumcek_adam-0049
@degisim: küçültmek -> bağlamak
Bir sabah Örümcek Adam parkta Spin için bir sürpriz hazırlıyordu. Çimlere büyük bir havlu serdi ve üstüne kurabiyeler koydu. Ama tuhaf bir şey gördü. Rüzgar bankın yanındaki üç balondan birinin ipini çözmüştü. O balon uçmuş ve duvarın üstüne takılmıştı. Örümcek Adam hemen duvarın yanına koştu. Süper gücüyle duvara hızla tırmandı. Balonu dikkatle aldı ve aşağı indi. Sonra ipi banka sıkıca bağladı. Az sonra Spin parka geldi. "Sürpriz, Spin!" dedi Örümcek Adam. Spin havluyu, kurabiyeleri ve üç balonu gördü. "Teşekkürler, Örümcek Adam, bu çok güzel bir sürpriz!" dedi Spin.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Rüzgar bankın yanındaki üç balondan birinin ipini çözmüştü"
   - Cümle 4: «Rüzgar bankın yanındaki üç balondan birinin ipini çözmüştü.»
   - Açıklama: İlk üç cümlede yalnız 'tuhaf bir şey' deniyor; sorun ancak dördüncü cümlede söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rüzgar bankın yanındaki üç balondan birinin ipini"
   - Cümle 4: «Rüzgar bankın yanındaki üç balondan birinin ipini çözmüştü.»
   - Açıklama: Rüzgarın bir düğümü çözmesi akla yatkın bir sebep değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "O balon uçmuş ve duvarın üstüne takılmıştı"
   - Cümle 5: «O balon uçmuş ve duvarın üstüne takılmıştı.»
   - Açıklama: Sorun ilk üç cümlede değil, 4. ve 5. cümlelerde söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0049` birebir aynı, `@degisim: küçültmek -> bağlamak` (tutuyorsan), ardından `@onarim: 825c4579c37482cea8ee7d2d4e48d227872a0ae4`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0052 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0052
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'kapı', fiil 'yerleştirmek', sıfat 'mutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: ikisi aynı anda kapıyı açmak isteyince duvar yıkıldı | sırayla oynamayı önerdi ve duvarı ağla sardı
@tohum: orumcek_adam-0052
@degisim: yerleştirmek -> sarmak
Rüzgar kumsalda serin serin esiyordu. Örümcek Adam ile Hulk kumdan büyük bir kale kuruyordu. İkisi de kapıyı aynı anda açmak isteyince kalenin duvarı yıkıldı. Hulk üzgün üzgün kuma baktı. "Hulk, sırayla oynayalım mı?" diye sordu Örümcek Adam. "Olur, ilk sıra senin," dedi Hulk. Örümcek Adam duvarı yeniden yaptı ve ağıyla sıkıca sardı. Şimdi sıra Hulk'taydı. Hulk kocaman parmağıyla duvarda yuvarlak bir kapı açtı. Ağ kumu tuttu ve duvar bu kez yıkılmadı. Hulk kaleye baktı ve mutlu mutlu güldü. "Teşekkürler, Hulk, kalenin kapısı çok güzel oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Örümcek Adam duvarı yeniden yaptı ve ağıyla sıkıca sardı"
   - Cümle 7: «Örümcek Adam duvarı yeniden yaptı ve ağıyla sıkıca sardı.»
   - Açıklama: Duvar aynı anda kapıyı açmaya çalışmaktan yıkıldı; sıra önerisine ek olarak duvarı yeniden yapıp ağla sarmak sebebe yönelmeyen fazladan adımlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0052` birebir aynı, `@degisim: yerleştirmek -> sarmak` (tutuyorsan), ardından `@onarim: f2245a9b8ad2913c0407340d516ec87a7a74f5ff`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0053 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0053
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'alet', fiil 'somurtmak', sıfat 'uyanık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: rüzgar yüzünden küçük fidan yere eğildi | fidanı iple sağlam bir sopaya bağladı
@tohum: orumcek_adam-0053
@degisim: uyanık -> sağlam
Örümcek Adam parkta bahçe oyunu oynuyordu ve ufak bir fidan dikti. Yanındaki alet kutusunda bir ip ve sağlam bir sopa vardı. Birden örümcek hissiyle sert bir rüzgarın geleceğini anladı. Rüzgar esti ve ince fidan yere doğru eğildi. Örümcek Adam fidana baktı ve somurttu. Sonra kutudan ipi ve sopayı aldı. Sopayı fidanın yanında toprağa soktu. Fidanı iple sopaya yavaşça bağladı. Rüzgar yine esti ama fidan bu kez hiç eğilmedi. Örümcek Adam alet kutusunu kapattı ve küçük fidana gülümsedi. Örümcek Adam çok sevindi, çünkü fidanı rüzgardan korumuştu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle sert"
   - Cümle 3: «Birden örümcek hissiyle sert bir rüzgarın geleceğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; küçük çocuk için anlaşılır değil.
   - Açıklama: 'Örümcek hissi' soyut bir kavram, küçük çocuk anlamaz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissiyle sert bir rüzgarın geleceğini anladı"
   - Cümle 3: «Birden örümcek hissiyle sert bir rüzgarın geleceğini anladı.»
   - Açıklama: Örümcek hissi haber veriyor ama hiçbir işe yaramıyor; fidan yine eğiliyor ve sorun sonradan iple çözülüyor, bu da özelliğin işe yarar kullanımına aykırı.
   - Açıklama: Örümcek hissi haber verse de Örümcek Adam buna göre hiçbir şey yapmıyor ve fidan yine eğiliyor; özellik işe yarar biçimde kullanılmamış.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissiyle sert bir rüzgarın geleceğini anladı.»
   - Açıklama: Fidanın eğilmesi sorunu ancak 4. cümlede söyleniyor; ilk üç cümlede yalnız rüzgar sezgisi var.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "örümcek hissiyle sert bir rüzgarın geleceğini anladı"
   - Cümle 3: «Birden örümcek hissiyle sert bir rüzgarın geleceğini anladı.»
   - Açıklama: Rüzgarın geleceğini önceden anlaması işe yarayacakmış gibi kuruluyor ama Örümcek Adam buna göre hiçbir şey yapmıyor.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ince fidan yere doğru eğildi"
   - Cümle 4: «Rüzgar esti ve ince fidan yere doğru eğildi.»
   - Açıklama: Asıl sorun olan fidanın eğilmesi ilk üç cümlede değil dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0053` birebir aynı, `@degisim: uyanık -> sağlam` (tutuyorsan), ardından `@onarim: a1bc3826254b4fa851e2e787355967497236fb92`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0054 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0054
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'lokma', fiil 'yollamak', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgarda kumdaki şemsiye sallanıp garip bir ses çıkarıyordu | şemsiyenin sapını tuttu ve kuma iyice bastırdı
@tohum: orumcek_adam-0054
@degisim: yollamak -> tutmak
Rüzgar sert sert esiyordu. Örümcek Adam kumsalda sulu bir şeftali yiyordu. Birden arkasından garip bir "pat pat" sesi duyuldu. Örümcek Adam şeftaliyi bıraktı ve bu sesi çok merak etti. Örümcek hissiyle bu sesin iyi olmadığını anladı. Örümcek Adam sese doğru koştu. Ses, kumdaki büyük bir şemsiyeden geliyordu. Rüzgar şemsiyeyi sallıyordu ve şemsiye kumdan çıkmak üzereydi. Örümcek Adam şemsiyenin sapını iki eliyle tuttu. Sonra sapı kuma iyice bastırdı. Şemsiye artık hiç sallanmadı ve ses durdu. Örümcek Adam şeftalisini aldı ve şemsiyenin altında son lokmayı yedi. Örümcek Adam çok sevindi, çünkü garip sesin ne olduğunu bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissiyle bu sesin iyi olmadığını"
   - Cümle 5: «Örümcek hissiyle bu sesin iyi olmadığını anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Örümcek hissi' ve sesin 'iyi olmaması' soyut, 3 yaşındaki çocuğa uygun olmayan anlatımdır.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Rüzgar şemsiyeyi sallıyordu ve şemsiye kumdan çıkmak üzereydi"
   - Cümle 8: «Rüzgar şemsiyeyi sallıyordu ve şemsiye kumdan çıkmak üzereydi.»
   - Açıklama: İlk üç cümlede yalnız garip bir ses var; asıl sorun olan şemsiyenin kumdan çıkması sekizinci cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0054` birebir aynı, `@degisim: yollamak -> tutmak` (tutuyorsan), ardından `@onarim: 7f2758e101755e63af0fa90579753c776ea8138b`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0058 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0058
- yer: ev (Takımın gizli evi.)
- tema: sırayla oynamak
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'dalga', fiil 'sıkışmak', sıfat 'değişik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: davul çubuğu kaydı ve kanepenin altına sıkıştı | ağ atıp çubuğu dışarı çekti
@tohum: orumcek_adam-0058
Dışarıda soğuk bir rüzgar esiyordu. Örümcek Adam gizli evde arkadaşı Ghost-Spider ile sırayla davul çalıyordu. Ama arkadaşı hızlı çalınca çubuk kaydı ve kanepenin altına sıkıştı. Kanepenin altı çok dardı ve eller oraya girmiyordu. Örümcek Adam ince bir ağ attı. Ağ çubuğa yapıştı ve çubuk dışarı çıktı. "Sıra sende," dedi Örümcek Adam ve çubuğu arkadaşına verdi. Arkadaşı bu kez davulu yavaşça çaldı. Davuldan dalga sesine benzeyen değişik bir ses çıktı. Arkadaşı bu sese güldü ve çubuğu Örümcek Adam'a uzattı. "Sırayla oynamak çok eğlenceli!" dedi Örümcek Adam.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve çubuk dışarı çıktı"
   - Cümle 6: «Ağ çubuğa yapıştı ve çubuk dışarı çıktı.»
   - Açıklama: Çubuk kendi kendine çıkmaz; 'Örümcek Adam çubuğu dışarı çekti' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dalga sesine benzeyen değişik bir ses"
   - Cümle 9: «Davuldan dalga sesine benzeyen değişik bir ses çıktı.»
   - Açıklama: Benzetme içeren anlatım küçük çocuk için soyut ve mecazlı kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0058` birebir aynı, ardından `@onarim: 7ec6fe5ee0b7503b8f642e3a4b078ffa00764887`, sonra gövde.
