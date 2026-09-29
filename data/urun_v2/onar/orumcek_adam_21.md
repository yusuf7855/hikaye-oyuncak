# Editör görevi (onarım): Örümcek Adam, onarım partisi 21

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar21.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0032 (deneme 5 -> 6)

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
Örümcek Adam ile Spin parkta büyük bir resim yapıyordu. Spin bir çiçek fotoğrafına bakıyor ve çiçekler çiziyordu. Birden rüzgar esti ve fotoğrafı havaya uçurdu. Fotoğraf parktaki taş duvarın üstündeki yüksek dallara takıldı. "Onu nasıl alacağız?" diye sordu Spin. Örümcek Adam süper gücüyle duvara hızla tırmandı. Fotoğrafı dallardan yavaşça çıkardı ve yere indi. Spin fotoğrafa baktı ve son çiçeği de çizdi. Sonra resmin köşesine duvara tırmanan küçük bir Örümcek Adam çizdi. Bu komik çizim Örümcek Adam'ı çok güldürdü. "Teşekkürler, Spin, bu çok eğlenceli oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "duvara tırmanan küçük bir Örümcek Adam"
   - Cümle 9: «Sonra resmin köşesine duvara tırmanan küçük bir Örümcek Adam çizdi.»
   - Açıklama: Tohumdaki tırmanma özelliği işe yarar kullanımdan sonra çizim içinde ikinci kez anılıyor; kartın özellik alanındaki tek kullanım beklentisine aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0032` birebir aynı, `@degisim: karmakarışık -> yüksek` (tutuyorsan), ardından `@onarim: b382752803f1b599f5800b069d3210e0e86bac0e`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0042 (deneme 5 -> 6)

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
Parkın oyun alanında tek bir salıncak vardı. Örümcek Adam salıncakta uzun uzun sallanıyordu. Hulk da binmek istiyordu ama arkada sessizce bekliyordu. Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. Arkasına baktı ve arkadaşını gördü. Hulk başını eğmişti ve biraz üzgündü. Örümcek Adam hemen salıncaktan indi. "Sıra sende, Hulk! On kere sallan, sonra sıra bende," dedi Örümcek Adam. Hulk sevindi ve salıncağa oturdu. Örümcek Adam yüksek sesle saydı. Sonra yer değiştirdiler. "Hazır mısın, Örümcek Adam?" diye sordu Hulk. Bu kez Hulk saydı. İkisi sırayla sallandı ve çok güldü. "Sırayla oynamak çok eğlenceli, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0042` birebir aynı, `@degisim: tuz -> salıncak` (tutuyorsan), ardından `@onarim: 4cfd81bbb214d5bbed43abab5062ac33091d796f`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0044 (deneme 5 -> 6)

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
Kumsal güneşle aydınlanmıştı ve güçlü bir rüzgar esiyordu. Örümcek Adam kumdan bir gemi yapmıştı ve gemi oyunu oynuyordu. Birden örümcek hissi ona gemideki bayrakta bir sorun olduğunu haber verdi. Bayrağın çubuğu kumda sağa sola eğiliyordu. Örümcek Adam çubuğu hemen sıkı sıkı tuttu ve kuma daha derine itti. Çubuk artık kumda dik durdu. Rüzgar yine esti ama bayrak düşmedi. Örümcek Adam gemisinin önüne oturdu ve gülümsedi. Kırmızı bayrak rüzgarda sallanıyordu. Örümcek Adam çok mutluydu, çünkü gemisinin bayrağı yine yerinde duruyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona gemideki bayrakta bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona gemideki bayrakta bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım; küçük çocuk için anlaşılmaz.
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissi ona gemideki bayrakta bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede yalnız bayrakta bir sorun olduğu söyleniyor; sorunun ne olduğu ancak 4. cümlede açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0044` birebir aynı, `@degisim: gül -> bayrak` (tutuyorsan), ardından `@onarim: 4c39b7717cd84208341d2f10f5eb29c9b4c8deea`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0046 (deneme 5 -> 6)

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
Bir sabah parkta hafif bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider bir su birikintisinde kağıt tekne yarışı yapıyordu. Birden örümcek hissi Örümcek Adam'a tekneler için bir sorun olduğunu haber verdi. Rüzgar tekneleri çalıya doğru itiyordu. Örümcek Adam tekneleri çalıda kaybetmek istemedi. Hemen iki tekneyi de sudan aldı. Onları çalısı olmayan başka bir su birikintisine götürdü ve suya bıraktı. Bu kez rüzgar tekneleri suyun öbür kenarına itti. Yarışta arkadaşının teknesi daha hızlı gitti. Arkadaşı sevinçle güldü. Örümcek Adam yarışı kaybetti ama o da güldü. Örümcek Adam bundan sonra rüzgarlı günlerde tekneleri hep çalıdan uzak suya bıraktı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi Örümcek Adam'a"
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a tekneler için bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve onun haber vermesi 3 yaşındaki çocuk için soyut bir kavram.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a tekneler için bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a tekneler için bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi mecaz ve 'sorun' soyut bir kavram.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Rüzgar tekneleri çalıya doğru itiyordu"
   - Cümle 4: «Rüzgar tekneleri çalıya doğru itiyordu.»
   - Açıklama: Sorun ilk 3 cümlede yalnız ima ediliyor, açıkça ancak 4. cümlede söyleniyor.
   - Açıklama: İlk üç cümlede yalnız belirsiz bir sorundan söz ediliyor; asıl sorun ancak 4. cümlede açıkça söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0046` birebir aynı, `@degisim: zarif -> hafif` (tutuyorsan), ardından `@onarim: 90f10d2e24d9bc48ba3f750ccf9475ee41b4b463`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0047 (deneme 5 -> 6)

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
Örümcek Adam kumsalda kumdan bir kale yapıyordu. O sırada rüzgar siyah kovasını sürükledi ve uzağa götürdü. Örümcek Adam bunu görmedi. Ama örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam hemen yanına baktı ve kovasının yerinde olmadığını gördü. Sonra kumda uzun bir iz gördü. İzi yavaş yavaş takip etti. İz suyun kenarına kadar gidiyordu. Siyah kova orada duruyordu. Dalgalar kovayı doldurmuştu ve su kovadan taşmıştı. Örümcek Adam kovayı aldı ve kalesinin yanına geri döndü. Kovadaki suyu kuma döktü. Islak kumla kalesine yeni bir kule yaptı. Örümcek Adam çok sevindi, çünkü kaybolan kovasını kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar siyah kovasını sürükledi ve uzağa götürdü"
   - Cümle 2: «O sırada rüzgar siyah kovasını sürükledi ve uzağa götürdü.»
   - Açıklama: Rüzgarın kovayı hemen yanından suyun kenarına kadar sürüklemesi ve Örümcek Adam'ın bunu görmemesi akla yatkın değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama örümcek hissi ona"
   - Cümle 4: «Ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 4: «Ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' soyut, 3 yaşındaki çocuğa uygun olmayan anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0047` birebir aynı, `@degisim: salıncak -> kova` (tutuyorsan), ardından `@onarim: 1e4922621a15881f8656047fe55d60947e2cb24a`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0052 (deneme 4 -> 5)

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
@plan: ikisi aynı anda kapıyı açmak isteyince duvardan kum döküldü | sırayla oynamayı önerdi ve duvarı ağla sardı
@tohum: orumcek_adam-0052
@degisim: yerleştirmek -> sarmak
Rüzgar kumsalda serin serin esiyordu. Örümcek Adam ile Hulk kumdan büyük bir kale kuruyordu. İkisi de kapıyı aynı anda açmak isteyince duvardan biraz kum döküldü. Hulk üzgün üzgün kuma baktı. "Hulk, sırayla oynayalım mı?" diye sordu Örümcek Adam. "Olur, ilk sıra senin," dedi Hulk. Örümcek Adam duvarı ağıyla sıkıca sardı. Şimdi sıra Hulk'taydı. Hulk kocaman parmağıyla duvarda yuvarlak bir kapı açtı. Ağ kumu tuttu ve bu kez duvardan kum dökülmedi. Hulk kaleye baktı ve mutlu mutlu güldü. "Teşekkürler, Hulk, kalenin kapısı çok güzel oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Örümcek Adam duvarı ağıyla sıkıca sardı"
   - Cümle 7: «Örümcek Adam duvarı ağıyla sıkıca sardı.»
   - Açıklama: Sebep ikisinin aynı anda kapı açması iken çözüm hem sıraya hem ağla sarmaya dağılıyor; ağ sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0052` birebir aynı, `@degisim: yerleştirmek -> sarmak` (tutuyorsan), ardından `@onarim: 74ec0b4f17212f991c1a3f01273d4a62ff8d77c3`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0053 (deneme 4 -> 5)

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
@plan: sert bir rüzgar geliyordu ve fidan çok inceydi | fidanı iple sağlam bir sopaya bağladı
@tohum: orumcek_adam-0053
@degisim: uyanık -> sağlam
Örümcek Adam parkta bahçe oyunu oynuyordu ve ufak bir fidan dikti. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Sert bir rüzgar geliyordu ve fidan çok inceydi. Örümcek Adam fidana baktı ve somurttu. Sonra alet kutusundan bir ip ve sağlam bir sopa aldı. Sopayı fidanın yanında toprağa soktu. Fidanı iple sopaya yavaşça bağladı. Az sonra sert rüzgar esti ama fidan dik durdu. Örümcek Adam alet kutusunu kapattı ve küçük fidana gülümsedi. Örümcek Adam çok sevindi, çünkü fidanı rüzgardan korumuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi ... haber verdi' soyut ve mecazlı bir anlatım, küçük çocuk için anlaşılır değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi mecaz ve 'sorun' soyut bir kavram.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "alet kutusundan bir ip ve sağlam bir sopa"
   - Cümle 5: «Sonra alet kutusundan bir ip ve sağlam bir sopa aldı.»
   - Açıklama: Daha önce kurulmamış alet kutusu çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0053` birebir aynı, `@degisim: uyanık -> sağlam` (tutuyorsan), ardından `@onarim: 0a5f3b03dd5baed87f13b5928e487ee0db0d9c17`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0054 (deneme 4 -> 5)

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
Rüzgar sert sert esiyordu. Örümcek Adam kumsalda sulu bir şeftali yiyordu. Birden arkasından garip bir "pat pat" sesi duyuldu. Örümcek Adam şeftaliyi bıraktı ve bu sesi çok merak etti. Örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam sese doğru koştu. Ses, kumdaki büyük bir şemsiyeden geliyordu. Rüzgar şemsiyeyi sağa sola sallıyordu. Örümcek Adam şemsiyenin sapını iki eliyle tuttu. Sonra sapı kuma iyice bastırdı. Şemsiye artık hiç sallanmadı ve ses durdu. Örümcek Adam şeftalisini aldı ve şemsiyenin altında son lokmayı yedi. Örümcek Adam çok sevindi, çünkü garip sesin ne olduğunu bulmuştu.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Birden arkasından garip bir"
   - Cümle 3: «Birden arkasından garip bir "pat pat" sesi duyuldu.»
   - Açıklama: İlk üç cümlede yalnız bir ses duyuluyor; şemsiyenin sallanması sorunu ancak 7-8. cümlede anlaşılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi ona bir sorun"
   - Cümle 5: «Örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 5: «Örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve haber vermesi soyut ve mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0054` birebir aynı, `@degisim: yollamak -> tutmak` (tutuyorsan), ardından `@onarim: c350b68793f1e7bd99d9a25f9b6e4492ef057404`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0058 (deneme 4 -> 5)

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
@degisim: dalga -> davul
Dışarıda soğuk bir rüzgar esiyordu. Örümcek Adam gizli evde arkadaşı Ghost-Spider ile sırayla davul çalıyordu. Ama arkadaşı hızlı çalınca çubuk kaydı ve kanepenin altına sıkıştı. Kanepenin altı çok dardı ve eller oraya girmiyordu. Örümcek Adam ince bir ağ attı. Ağ çubuğa yapıştı ve Örümcek Adam çubuğu dışarı çekti. "Sıra sende," dedi Örümcek Adam ve çubuğu arkadaşına verdi. Arkadaşı bu kez davulu yavaşça çaldı. Davuldan değişik bir ses çıktı. Arkadaşı güldü ve çubuğu Örümcek Adam'a uzattı. "Sırayla oynamak çok eğlenceli!" dedi Örümcek Adam.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "eller oraya girmiyordu"
   - Cümle 4: «Kanepenin altı çok dardı ve eller oraya girmiyordu.»
   - Açıklama: Ellerin kime ait olduğu belirtilmemiş; iyelik eki eksik ('elleri' olmalı).
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Davuldan değişik bir ses çıktı"
   - Cümle 9: «Davuldan değişik bir ses çıktı.»
   - Açıklama: Değişik sesin sebebi yok ve olayda hiçbir işe yaramıyor.
   - Açıklama: Değişik ses işlevsiz bir ayrıntı olarak kalıyor, hiçbir yere bağlanmıyor.
   - Açıklama: Değişik ses kuruluyor ama olayda hiçbir işe yaramıyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sırayla oynamak çok eğlenceli!"
   - Cümle 11: «"Sırayla oynamak çok eğlenceli!" dedi Örümcek Adam.»
   - Açıklama: Kapanıştaki sırayla oynama dersi çubuğun sıkışması sorunundan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0058` birebir aynı, `@degisim: dalga -> davul` (tutuyorsan), ardından `@onarim: 714bca262d437b40dde92a9d406c243565a0ee7f`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0062 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0062
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'çömlek', fiil 'kalkmak', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: çiçek bahçesinden bilinmeyen bir ses geldi | duvara tırmandı ve sesin nereden geldiğini buldu
@tohum: orumcek_adam-0062
Örümcek Adam parkın oyun alanında yürüyordu. Birden çiçek bahçesinden "tam tam" diye bir ses geldi. Bahçenin duvarı çok yüksekti. Örümcek Adam bu sesi çok merak etti. Süper gücüyle duvara tırmandı ve aşağı baktı. Ghost-Spider çimlere oturmuş, kıpkırmızı bir çömleği davul gibi çalıyordu. "Ses senden geliyormuş!" dedi Örümcek Adam. Arkadaşı sevinçle yerden kalktı ve "Gel, birlikte çalalım!" dedi. Örümcek Adam duvardan indi ve onunla çömleği çaldı. Örümcek Adam çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Örümcek Adam bu sesi çok merak etti"
   - Cümle 4: «Örümcek Adam bu sesi çok merak etti.»
   - Açıklama: Sorun yalnız bilinmeyen bir sesi merak etmek; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Süper gücüyle duvara tırmandı"
   - Cümle 5: «Süper gücüyle duvara tırmandı ve aşağı baktı.»
   - Açıklama: 'Süper güç' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onunla çömleği çaldı"
   - Cümle 9: «Örümcek Adam duvardan indi ve onunla çömleği çaldı.»
   - Açıklama: 'Çömleği çaldı' hırsızlık anlamına da okunuyor; 'çömleği davul gibi çaldı' ya da 'vurdu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0062` birebir aynı, ardından `@onarim: 51b5cff7cf1afd33ba49270191e6a167b6670edf`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0064 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0064
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: paylaşmak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kumaş', fiil 'geçmek', sıfat 'bozuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: arkadaşının şemsiyesi bozuktu ve güneşte resim yapamadı | kendi şemsiyesini arkadaşıyla paylaştı
@tohum: orumcek_adam-0064
Bir sabah Örümcek Adam kumsalda şemsiyesinin altında oturuyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam etrafına baktı ve Spin'i gördü. Spin'in şemsiyesi bozuktu ve Spin güneşte resim yapamıyordu. Örümcek Adam şemsiyesini alıp Spin'in yanına götürdü. "Şemsiyemi seninle paylaşayım, Spin," dedi Örümcek Adam. Şemsiyeyi kuma sıkıca dikti. Şemsiyenin mavi kumaşı ikisini de güneşten korudu. Spin gölgeye geçti ve resmine devam etti. Denizi ve gemileri çok güzel çizdi. Sonra resmi Örümcek Adam'a gösterdi. "Teşekkürler, Örümcek Adam, bu resim senin!" dedi Spin.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi mecazlı ve soyut bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi mecaz ve 'sorun' soyut bir kavram.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Spin'in şemsiyesi bozuktu ve Spin güneşte resim yapamıyordu"
   - Cümle 4: «Spin'in şemsiyesi bozuktu ve Spin güneşte resim yapamıyordu.»
   - Açıklama: Sorun ilk 3 cümlede değil ancak 4. cümlede açıkça söyleniyor; 2. cümle yalnız belirsiz bir sorun olduğunu söylüyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede açıkça söyleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Spin'in şemsiyesi bozuktu"
   - Cümle 4: «Spin'in şemsiyesi bozuktu ve Spin güneşte resim yapamıyordu.»
   - Açıklama: Şemsiyenin neden bozuk olduğu hiç söylenmiyor, sorunun sebebi verilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0064` birebir aynı, ardından `@onarim: 5236b7f7b2f49252b6261ee5def8d5683c24bfcf`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0067 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0067
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'vanilya', fiil 'başlamak', sıfat 'hareketsiz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: rüzgar balonu dikenli bir çalıya uçurdu | balonu tutmadı ve ipinden yavaşça çekti
@tohum: orumcek_adam-0067
@degisim: vanilya -> balon
Parkın oyun alanında Örümcek Adam balon oyununa başladı. Uzun ipi olan kırmızı balonu eliyle havaya itiyordu. Birden rüzgar esti ve balon bir gül çalısının içine uçtu. Balon dalların arasında hareketsiz kaldı. Dallarda küçük dikenler vardı. Örümcek Adam hemen balonu tutmak istedi. Ama örümcek hissi ona bir sorun olduğunu haber verdi. Dikenler çok sivriydi. Örümcek Adam balonun ipini tuttu ve yavaşça çekti. Balon kolayca çalıdan çıktı. Örümcek Adam ipi bileğine bağladı ve oyuna devam etti. Örümcek Adam çok sevindi, çünkü balonunu geri almıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 7: «Ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0067` birebir aynı, `@degisim: vanilya -> balon` (tutuyorsan), ardından `@onarim: ef4714e5508af6e38eab541a617e5f176166ff5f`, sonra gövde.
