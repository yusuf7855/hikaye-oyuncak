# Editör görevi (onarım): Örümcek Adam, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar9.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0029 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0029
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'kostüm', fiil 'homurdanmak', sıfat 'faydalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: topa hızlı vurdu ve davul çubuğu suya düştü | özür diledi ve çubuğu ağla kıyıya çekti
@tohum: orumcek_adam-0029
@degisim: faydalı -> neşeli
Örümcek Adam kumsalda topla oynuyordu ve Ghost-Spider onun yanında davul çalıyordu. Örümcek Adam topa çok hızlı vurdu ve top arkadaşının çubuğuna çarptı. Davul çubuğu suya düştü ve dalgalarla uzaklaşmaya başladı. Arkadaşı üzgün üzgün homurdandı. "Özür dilerim, dikkat etmedim," dedi Örümcek Adam. Sonra suya doğru ağ attı. Ağ çubuğa yapıştı ve Örümcek Adam onu yavaşça kıyıya çekti. Islak çubuğu arkadaşına geri verdi. Arkadaşı çubuğu kostümüyle kuruladı. "Teşekkürler, Örümcek Adam, çubuğum yine elimde!" dedi arkadaşı ve gülümsedi. Arkadaşı yeniden davul çaldı ve Örümcek Adam neşeli sesi mutlu mutlu dinledi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Arkadaşı üzgün üzgün homurdandı"
   - Cümle 4: «Arkadaşı üzgün üzgün homurdandı.»
   - Açıklama: 'Homurdanmak' kızgınlık bildirir, üzüntüyle uyuşmuyor ve küçük çocuk için uygun kelime değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "neşeli sesi mutlu mutlu dinledi"
   - Cümle 11: «Arkadaşı yeniden davul çaldı ve Örümcek Adam neşeli sesi mutlu mutlu dinledi.»
   - Açıklama: Hangi sesin kastedildiği belirsiz ve 'neşeli ses' davul için uygun kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0029` birebir aynı, `@degisim: faydalı -> neşeli` (tutuyorsan), ardından `@onarim: 65ab459ff4b46fb91423105a1be6e98cf310f811`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0030 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0030
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'bileklik', fiil 'dağılmak', sıfat 'soslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: suda parlayan bilinmeyen bir şey vardı | ağ atıp onu çekti ve bilekliği buldu
@tohum: orumcek_adam-0030
@degisim: soslu -> renkli
Kumsalda serin bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider limanın kenarında dalgalara bakıyordu. Köpükler dağıldı ve suda küçük bir ışık göründü. "Bu nedir, Örümcek Adam?" diye sordu arkadaşı. O şey kıyıdan biraz uzaktaydı. Örümcek Adam ağ attı ve onu yakaladı. Sonra ağı yavaşça kendine çekti. Ağın içinde renkli bir bileklik vardı. "Bu benim kayıp bilekliğim!" dedi arkadaşı. Arkadaşı bilekliği hemen koluna taktı ve "Teşekkürler, Örümcek Adam," dedi. Örümcek Adam çok sevindi, çünkü suda parlayan şeyin ne olduğunu bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "suda parlayan bilinmeyen bir şey vardı"
   - Cümle 0 (plan satırı): «suda parlayan bilinmeyen bir şey vardı | ağ atıp onu çekti ve bilekliği buldu»
   - Açıklama: Sorun yalnız bir merak; bilekliğin nasıl suya düştüğü, yani sebep hiç söylenmiyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "limanın kenarında dalgalara bakıyordu"
   - Cümle 2: «Örümcek Adam ile Ghost-Spider limanın kenarında dalgalara bakıyordu.»
   - Açıklama: Hikaye kumsalda başlıyor ama figürler bir anda limanın kenarında.
   - Açıklama: Hikaye kumsalda başlıyor ama karakterler aynı anda limanın kenarında duruyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "suda küçük bir ışık göründü"
   - Cümle 3: «Köpükler dağıldı ve suda küçük bir ışık göründü.»
   - Açıklama: Sorun belirsiz bir merak; bilekliğin nasıl kaybolduğu söylenmiyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "dedi arkadaşı. Arkadaşı bilekliği"
   - Cümle 10: «Arkadaşı bilekliği hemen koluna taktı ve "Teşekkürler, Örümcek Adam," dedi.»
   - Açıklama: 'Arkadaşı' art arda gereksiz tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0030` birebir aynı, `@degisim: soslu -> renkli` (tutuyorsan), ardından `@onarim: 5c23d040709f75d1f6fb0d4ee504b19abe5db937`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0031 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0031
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: kaybolan eşya
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'köfte', fiil 'dolanmak', sıfat 'temkinli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: rüzgar esti ve balon ağaçların arasında kayboldu | balonu dalda buldu ve ipini ağla çekti
@tohum: orumcek_adam-0031
Örümcek Adam ile Hulk parkta yürüyordu. Hulk bir eliyle köfte yiyor, öbür eliyle kırmızı balonunu tutuyordu. Birden güçlü bir rüzgar esti ve balonun ipi Hulk'ın elinden kaydı. Balon uçtu ve ağaçların arasında kayboldu. "Balonum nereye gitti?" diye sordu Hulk. Örümcek Adam temkinli adımlarla ağaçlara doğru yürüdü. Sonunda balonu yüksek bir dalda buldu. Balonun ipi dala dolanmıştı. Örümcek Adam bileğinden ağ attı ve ipi yakaladı. Sonra ipi yavaşça çekip daldan kurtardı. Balonu Hulk'a geri verdi. "Teşekkürler, Örümcek Adam!" dedi Hulk ve kocaman güldü. Örümcek Adam çok sevindi, çünkü arkadaşının balonunu bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "temkinli adımlarla ağaçlara"
   - Cümle 6: «Örümcek Adam temkinli adımlarla ağaçlara doğru yürüdü.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0031` birebir aynı, ardından `@onarim: a0edc63c0f7d0d8f7d09bd520a19b02f5d302422`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0032 (deneme 1 -> 2)

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
Örümcek Adam ile Spin parkta büyük bir resim yapıyordu. Resimde çiçek bahçesi ve uçan kelebekler vardı. Birden rüzgar esti ve kağıdı havaya uçurdu. Kağıt bahçedeki taş duvarın üstünde karmakarışık dallara takıldı. "Resim orada kaldı, onu nasıl alacağız?" diye sordu Spin. Örümcek Adam duvara hızla tırmandı. Kağıdı dallardan yavaşça çıkardı ve yere indi. Resim hiç yırtılmamıştı. Spin resmin köşesine duvara tırmanan küçük bir Örümcek Adam çizdi. Bu komik resim Örümcek Adam'ı çok güldürdü. "Teşekkürler, Spin, bu çok eğlenceli oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "taş duvarın üstünde karmakarışık dallara"
   - Cümle 4: «Kağıt bahçedeki taş duvarın üstünde karmakarışık dallara takıldı.»
   - Açıklama: Sıfat-fiil eki eksik; 'duvarın üstündeki dallara' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "duvarın üstünde karmakarışık dallara takıldı"
   - Cümle 4: «Kağıt bahçedeki taş duvarın üstünde karmakarışık dallara takıldı.»
   - Açıklama: Sıfat tamlaması için 'duvarın üstündeki dallara' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0032` birebir aynı, `@degisim: fotoğraf -> resim` (tutuyorsan), ardından `@onarim: 9faa5f024f0a603514b3fdc9d0086d92d67f407f`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0033 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0033
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: paylaşmak
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'ipek', fiil 'sallanmak', sıfat 'gizli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: arkadaşının uçurtması yırtılmıştı ve o üzgündü | duvara tırmanıp uçurtmasını onunla paylaştı
@tohum: orumcek_adam-0033
Örümcek Adam parkta ipek kuyruklu bir uçurtma uçuruyordu. Parktaki taş duvarın arkasından Hulk gizli gizli uçurtmaya bakıyordu. Hulk'ın kendi uçurtması rüzgarda yırtılmıştı ve o biraz üzgündü. Örümcek Adam onun üzgün yüzünü gördü. Uçurtmanın ipini sıkıca tuttu ve duvara tırmandı. Duvarın öbür yanına indi ve Hulk'ın yanına oturdu. Sonra ipi Hulk'a uzattı. Hulk ipi iki eliyle tuttu ve uçurtma yükseldi. İpek kuyruk rüzgarda sağa sola sallandı. Hulk kocaman gülümsedi. İkisi uçurtmayı sırayla uçurdu. Örümcek Adam çok mutluydu, çünkü uçurtmasını arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "sıkıca tuttu ve duvara tırmandı"
   - Cümle 5: «Uçurtmanın ipini sıkıca tuttu ve duvara tırmandı.»
   - Açıklama: Tırmanma süper güç olarak çerçevelenmeden, çocuğun taklit edebileceği biçimde parktaki taş duvara tırmanma olarak anlatılıyor; güvenli özellik kullanımı satırına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0033` birebir aynı, ardından `@onarim: eff07ce37a28df06c26af24e5a4fbe162dc63e5a`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0036 (deneme 1 -> 2)

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
Örümcek Adam gizli evde bir dilim karpuz yiyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Evin yüksek penceresi rüzgarla açılmıştı ve içeri yağmur giriyordu. Pencere çok yüksekteydi ve Örümcek Adam ona yetişemiyordu. "Ghost-Spider, bana yardım eder misin?" diye sordu Örümcek Adam. "Tabii, hemen geliyorum," dedi arkadaşı. Sonra kostümüyle havada süzüldü ve pencereye yükseldi. Pencerenin minicik kolunu çevirdi ve onu sıkıca kapadı. Yağmur artık içeri girmiyordu. Örümcek Adam ona da bir dilim karpuz verdi. Örümcek Adam çok mutluydu, çünkü arkadaşı ona hemen yardım etmişti.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı, 3 yaşındaki çocuk için uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber vermesi mecaz; 3 yaşındaki çocuk anlamaz.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Örümcek Adam ona yetişemiyordu"
   - Cümle 4: «Pencere çok yüksekteydi ve Örümcek Adam ona yetişemiyordu.»
   - Açıklama: Kartın özelliklerine göre ağ atabilen Örümcek Adam'ın yüksek pencereye hiç yetişemediği söyleniyor, bu diziyi bilen çocuğa yanlış bilgi verir.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Pencere çok yüksekteydi ve Örümcek Adam ona yetişemiyordu"
   - Cümle 4: «Pencere çok yüksekteydi ve Örümcek Adam ona yetişemiyordu.»
   - Açıklama: Duvarlara tırmanabilen Örümcek Adam'ın yüksek pencereye yetişememesi akla yatkın bir sebep değil.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra kostümüyle havada süzüldü"
   - Cümle 7: «Sonra kostümüyle havada süzüldü ve pencereye yükseldi.»
   - Açıklama: Öznesiz cümlede süzülenin Ghost-Spider mı Örümcek Adam mı olduğu belli değil.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Örümcek Adam ona da"
   - Cümle 10: «Örümcek Adam ona da bir dilim karpuz verdi.»
   - Açıklama: Önceki cümlede arkadaş geçmediği için 'ona' zamirinin kimi gösterdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0036` birebir aynı, ardından `@onarim: be51f18658719fb8fc8fbd12203ae215753db31c`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0038 (deneme 1 -> 2)

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
Örümcek Adam ile Ghost-Spider limanda denize bakıyordu. Birden arkalarından tık tık diye bir ses geldi. Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. İkisi sesin geldiği yere yavaşça yürüdü. Arkadaşının fındık torbası rüzgarda devrilmişti. Fındıklar yerde tık tık yuvarlanıyordu. Örümcek Adam torbayı hemen kaldırdı ve sıkıca kapadı. Arkadaşı da yerdeki fındıkları tek tek topladı. Hiçbir fındık denize düşmedi. "Teşekkürler, Örümcek Adam!" dedi arkadaşı. "Bu sesi birlikte bulduk, ben de çok memnun oldum!" dedi Örümcek Adam.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "tık tık diye bir ses geldi"
   - Cümle 2: «Birden arkalarından tık tık diye bir ses geldi.»
   - Açıklama: Sorun yalnızca bir ses; rüzgarın devirdiği fındıklar toplanıp bitiyor, çocuğun önemseyeceği bir sorun kurulmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 3: «Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuk anlamaz.
   - Açıklama: Hissin haber vermesi mecazdır ve 3 yaşındaki çocuğa soyut gelir.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşının fındık torbası rüzgarda"
   - Cümle 5: «Arkadaşının fındık torbası rüzgarda devrilmişti.»
   - Açıklama: 'Arkadaşı' kimi gösteriyor belli değil; Ghost-Spider mı yoksa yeni biri mi anlaşılmıyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşının fındık torbası rüzgarda devrilmişti"
   - Cümle 5: «Arkadaşının fındık torbası rüzgarda devrilmişti.»
   - Açıklama: 'Arkadaşı' kimi gösteriyor belli değil; Ghost-Spider adıyla tanıtılmışken adsız bir arkadaş gibi anılıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Arkadaşının fındık torbası rüzgarda devrilmişti"
   - Cümle 5: «Arkadaşının fındık torbası rüzgarda devrilmişti.»
   - Açıklama: Fındık torbası ve adı verilmeyen arkadaş önceden kurulmadan sebepsiz beliriyor.
   - Açıklama: Fındık torbası ve sahibi olan arkadaş daha önce hiç kurulmadan sebepsizce beliriyor.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben de çok memnun oldum"
   - Cümle 11: «"Bu sesi birlikte bulduk, ben de çok memnun oldum!" dedi Örümcek Adam.»
   - Açıklama: 'Memnun' küçük çocuk için soyut bir kelimedir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0038` birebir aynı, ardından `@onarim: 7b3d8607313ec204bacbcb58fa2e6ee85f1e1234`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0039 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0039
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: kaybolan eşya
- yan: -
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'böğürtlen', fiil 'mırıldanmak', sıfat 'neşeli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar böğürtlen kutusunu kayaların arasına düşürdü | kutuyu iki kaya arasında buldu ve ağla çekti
@tohum: orumcek_adam-0039
Martılar limanın üstünde ötüyordu. Örümcek Adam kumsalda neşeli bir şarkı mırıldanıyordu. Birden rüzgar esti ve kayanın üstündeki böğürtlen kutusunu düşürdü. Kutu kayaların arasına yuvarlandı ve kayboldu. Örümcek Adam her yere dikkatle baktı. Sonunda kutuyu iki kayanın arasında gördü. Orası çok dardı ve eli içeri girmiyordu. Örümcek Adam hemen ağ attı ve kutuyu yakaladı. Kutuyu yavaşça yukarı çekti. Kapağı sıkıca kapalıydı ve böğürtlenler hiç dökülmedi. Örümcek Adam kutuyu açtı ve bir böğürtlen yedi. Örümcek Adam çok mutluydu, çünkü kaybolan kutusunu bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kayanın üstündeki böğürtlen kutusunu"
   - Cümle 3: «Birden rüzgar esti ve kayanın üstündeki böğürtlen kutusunu düşürdü.»
   - Açıklama: Böğürtlen kutusu daha önce kurulmadan kayanın üstünde sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0039` birebir aynı, ardından `@onarim: dcd457d427f4f3a1656b510d16c40c09d961e93c`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0040 (deneme 1 -> 2)

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
Dışarıda yağmur şıp şıp yağıyordu. Örümcek Adam ile Hulk bu yüzden parka gidemedi. İkisi gizli evde oturuyordu ve biraz sıkılmıştı. Örümcek Adam dolapta ışıltılı süslerle dolu bir kutu buldu. "Hulk, bu süsleri odaya asalım mı?" diye sordu Örümcek Adam. "Evet, hadi asalım!" dedi Hulk. Hulk süsleri kapıya ve pencereye astı. Örümcek Adam da duvara tırmandı ve en büyük yıldız süsünü tavana taktı. Sonunda bütün oda süslendi. Süsler odada pırıl pırıl parlıyordu. "Yağmurlu gün bile çok eğlenceli oldu, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Örümcek Adam dolapta ışıltılı süslerle dolu bir kutu buldu"
   - Cümle 4: «Örümcek Adam dolapta ışıltılı süslerle dolu bir kutu buldu.»
   - Açıklama: Süs kutusu sebepsizce beliriyor ve çözümü tesadüfen getiriyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam da duvara tırmandı ve en büyük yıldız süsünü tavana taktı"
   - Cümle 8: «Örümcek Adam da duvara tırmandı ve en büyük yıldız süsünü tavana taktı.»
   - Açıklama: Güvenli kullanım satırı ev içi taklit edilebilir tırmanmayı yasaklar; evde süs asmak için tırmanma çocukça taklit edilebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0040` birebir aynı, ardından `@onarim: 1c9df060c9457763c5d80a3defe61a35fc4d3db6`, sonra gövde.
