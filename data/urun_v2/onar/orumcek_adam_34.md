# Editör görevi (onarım): Örümcek Adam, onarım partisi 34

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar34.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar34.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0125 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0125
- yer: ev (Takımın gizli evi.)
- tema: paylaşmak
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'buz', fiil 'vermek', sıfat 'tüylü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: gizli ev soğuktu ve evde tek battaniye vardı | duvara tırmanıp battaniyeyi aldı ve arkadaşıyla paylaştı
@tohum: orumcek_adam-0125
Bir sabah gizli evde hava çok soğuktu. Pencerede ince bir buz vardı ve Örümcek Adam ısınmak istiyordu. Ghost-Spider da ısınmak istiyordu ama evde tek bir tüylü battaniye vardı. Battaniye, duvarın en üstündeki bir askıda duruyordu. Örümcek Adam duvara tırmandı ve battaniyeyi aldı. Sonra yavaşça aşağı indi. "Gel, bu battaniye ikimiz için de büyük," dedi Örümcek Adam. Battaniyenin bir ucunu arkadaşına verdi. İkisi yan yana oturdu ve battaniyeye sarıldı. "Çok sıcak, teşekkür ederim!" dedi arkadaşı. Örümcek Adam çok mutlu oldu, çünkü battaniyeyi arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (4):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Battaniye, duvarın en üstündeki bir askıda duruyordu"
   - Cümle 4: «Battaniye, duvarın en üstündeki bir askıda duruyordu.»
   - Açıklama: Tek battaniye sorununun yanında battaniyenin ulaşılmaz yerde olması ikinci bir sorun olarak ekleniyor ve asıl çözülen bu oluyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Battaniye, duvarın en üstündeki bir askıda duruyordu"
   - Cümle 4: «Battaniye, duvarın en üstündeki bir askıda duruyordu.»
   - Açıklama: Battaniyenin duvarın tepesinde durması sebepsiz; yalnız tırmanma yeteneği kullanılsın diye kurulmuş.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvara tırmandı"
   - Cümle 5: «Örümcek Adam duvara tırmandı ve battaniyeyi aldı.»
   - Açıklama: Güvenli özellik kullanımı satırı ev içi tırmanmayı yasaklarken gizli evin içinde yüksekteki eşyaya ulaşmak için tırmanılıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oturdu ve battaniyeye sarıldı"
   - Cümle 9: «İkisi yan yana oturdu ve battaniyeye sarıldı.»
   - Açıklama: Battaniyeye sarılmak kucaklamak demektir; doğrusu 'battaniyeye sarındı'.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0125` birebir aynı, ardından `@onarim: cb5fef42455c130a5fbca2590e505400ccb7e604`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0126 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0126
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'altın', fiil 'oturtmak', sıfat 'vanilyalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: altın sarısı elma ağacın tepesindeydi | ağ atıp elmayı yavaşça çekti
@tohum: orumcek_adam-0126
Rüzgar parktaki ağaçların yapraklarını sallıyordu. Örümcek Adam ile Hulk çimenlerde vanilyalı bir keki süslemek istiyordu. Hulk ağacın tepesinde altın sarısı bir elma gördü ama ona uzanamadı. "Ağacı sallamak istemiyorum, dallar kırılır," dedi Hulk. Örümcek Adam elmaya bir ağ attı. Ağ elmaya yapıştı ve Örümcek Adam ağı yavaşça çekti. Elma dalından koptu ve Örümcek Adam'ın eline düştü. Örümcek Adam elmayı kekin tam ortasına oturttu. "Bu kek şimdi çok güzel oldu!" dedi Hulk ve güldü. Örümcek Adam çok sevindi, çünkü kek artık hazırdı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elmayı kekin tam ortasına oturttu"
   - Cümle 8: «Örümcek Adam elmayı kekin tam ortasına oturttu.»
   - Açıklama: 'Oturtmak' elma için alışılmadık ve mecazlı; 'koydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0126` birebir aynı, ardından `@onarim: 4c8caf110b8924295933d5b7b434aef1cee8c528`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0128 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0128
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'bayrak', fiil 'kurutmak', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar bayrağı fıskiyenin havuzuna düşürdü | ağ atıp bayrağı sudan çekti
@tohum: orumcek_adam-0128
Örümcek Adam parkta bayrak oyunu oynuyordu. Ghost-Spider bayrağı kaptı ve havada süzülerek kaçtı. Ama rüzgar bayrağı elinden aldı ve fıskiyenin havuzuna düşürdü. Bayrak suyun tam ortasında yüzüyordu. Örümcek Adam havuzun kenarında bir an düşünceli durdu. Sonra ağ attı ve bayrağı sudan çekti. İkisi bayrağı güneşte biraz salladı ve kuruttu. Sonra ikisi oyuna hemen yeniden başladı ve bayrağı sırayla kaptı. Örümcek Adam çok sevindi, çünkü en sevdikleri oyun hiç yarım kalmamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "oyun hiç yarım kalmamıştı"
   - Cümle 9: «Örümcek Adam çok sevindi, çünkü en sevdikleri oyun hiç yarım kalmamıştı.»
   - Açıklama: 'Yarım kalmak' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hiç yarım kalmamıştı"
   - Cümle 9: «Örümcek Adam çok sevindi, çünkü en sevdikleri oyun hiç yarım kalmamıştı.»
   - Açıklama: 'Yarım kalmak' soyut bir anlatım; küçük çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0128` birebir aynı, ardından `@onarim: cdb875c102e6929c83eb3c434ff86c11ba49d6a3`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0129 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | ev | -
@tohum: orumcek_adam-0129
- yer: ev (Takımın gizli evi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'file', fiil 'sulamak', sıfat 'boyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | ev | -
@plan: gizli evde garip bir tık tık sesi duyuldu | koridora gidip sesi buldu ve pencereyi kapattı
@tohum: orumcek_adam-0129
Gizli evde güneşli bir sabah başlamıştı. Örümcek Adam masadaki boyalı saksıyı suluyordu. Birden tık tık diye garip bir ses duydu. Örümcek Adam çok merak etti ama sesin nereden geldiğini bulamadı. O anda örümcek hissiyle koridorda bir sorun olduğunu anladı. Örümcek Adam hemen koridora yürüdü. Duvarda toplarla dolu bir file asılıydı. Açık pencereden giren rüzgar fileyi sallıyordu. Toplar da duvara çarpıyordu. Tık tık sesi buradan geliyordu. Örümcek Adam pencereyi kapattı. File durdu ve koridor sessiz oldu. Örümcek Adam gülümsedi ve çiçeğini sulamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden tık tık diye garip bir ses duydu"
   - Cümle 3: «Birden tık tık diye garip bir ses duydu.»
   - Açıklama: Sorun yalnız rüzgarın çıkardığı bir ses; çocuğun önemseyeceği bir sorun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle koridorda bir"
   - Cümle 5: «O anda örümcek hissiyle koridorda bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavramdır; 3 yaşındaki çocuk anlamaz.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "O anda örümcek hissiyle"
   - Cümle 5: «O anda örümcek hissiyle koridorda bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' 3 yaşındaki çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0129` birebir aynı, ardından `@onarim: 247a346b6c7e50f29b1c46e524d371e90cfb66a2`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0130 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0130
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'sünger', fiil 'çalıştırmak', sıfat 'kaygan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: yola konan sabunlu sünger çok kaygandı | arkadaşını durdurdu ve süngeri kovaya koydu
@tohum: orumcek_adam-0130
@degisim: çalıştırmak -> yıkamak
Bir sabah Örümcek Adam ile Spin limanda kovayla oyuncak bir tekne yıkıyordu. Örümcek Adam sabunlu süngeri yolun ortasına koydu. Sünger çok kaygandı ve tekneyi taşıyan Spin geri geri yürüyordu. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. "Dur, Spin, yerde kaygan bir sünger var!" dedi Örümcek Adam. Spin hemen durdu. Örümcek Adam süngeri yerden aldı ve kovaya koydu. "Özür dilerim, Spin, süngeri yola ben koydum," dedi Örümcek Adam. "Sorun değil, teşekkürler," dedi Spin. Sonra ikisi tekneyi yıkamaya devam etti. Örümcek Adam bundan sonra süngeri hep kovanın içine koydu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Örümcek Adam sabunlu süngeri yolun ortasına koydu"
   - Cümle 2: «Örümcek Adam sabunlu süngeri yolun ortasına koydu.»
   - Açıklama: Sorun, süngerin sebepsizce yolun ortasına konmasıyla yapay biçimde kuruluyor ve hiçbir şey olmadan çözülüyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun"
   - Cümle 4: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk için uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber vermesi mecaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0130` birebir aynı, `@degisim: çalıştırmak -> yıkamak` (tutuyorsan), ardından `@onarim: 930eb21399564e2dc94ccc35ce094f57ead5aea3`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0138 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0138
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'pota', fiil 'düzeltmek', sıfat 'yumuşak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: top potaya girmedi çünkü çember eğilmişti | sorunu bulup çemberi düzeltti
@tohum: orumcek_adam-0138
Örümcek Adam ile Hulk kumsalda yumuşak bir topla oynuyordu. Kumun üstünde küçük bir pota vardı. Hulk topu potaya attı ama top içeri girmedi. "Top neden içeri girmedi?" diye sordu Hulk. Örümcek Adam örümcek hissi sayesinde bir sorun olduğunu anladı. Oraya gitti ve dikkatle baktı. Çember aşağı doğru eğilmişti. "Çember eğilmiş, Hulk!" dedi Örümcek Adam. Hulk direği sıkıca tuttu. Örümcek Adam çemberi iki eliyle yukarı itti ve düzeltti. Hulk topu yine attı. Top bu kez içeri girdi. Sonra ikisi mutlu mutlu top oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi sayesinde bir sorun olduğunu anladı"
   - Cümle 5: «Örümcek Adam örümcek hissi sayesinde bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi sayesinde bir sorun olduğunu anlamak' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi', 'sayesinde' ve 'sorun' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissi sayesinde bir sorun olduğunu anladı"
   - Cümle 5: «Örümcek Adam örümcek hissi sayesinde bir sorun olduğunu anladı.»
   - Açıklama: Sorunu Hulk zaten fark etmişken örümcek hissi işe yarar bir iş görmüyor, kartın özellik alanındaki haber verme işlevi boşa kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0138` birebir aynı, ardından `@onarim: b4cccda6e0d06c9050e518405153e3cd57de97e8`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0139 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0139
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'damga', fiil 'planlamak', sıfat 'şapkalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: damgayı sormadan attı ve damga duvarda kaldı | özür dileyip duvara tırmandı ve damgayı getirdi
@tohum: orumcek_adam-0139
Bir sabah Örümcek Adam ile Spin limanda resim yapıyordu. Örümcek Adam, Spin'in çiçek damgasını alıp oyun için havaya attı. Damga yüksek bir duvarın tepesine düştü ve orada kaldı. Spin bugün şapkalı çiçekler yapmayı planlamıştı. Şimdi çok üzgündü. "Özür dilerim, Spin, sormadan aldım," dedi Örümcek Adam. Sonra duvara hızla tırmandı ve damgayı alıp indi. Damgayı Spin'e geri verdi. "Teşekkür ederim, Örümcek Adam," dedi Spin ve gülümsedi. Spin kağıda damgayı bastı ve çiçekler yaptı. Örümcek Adam da her çiçeğe küçük bir şapka çizdi. Örümcek Adam ile Spin resmi mutlu mutlu bitirdi.
```

**Hakem bulguları (3):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Spin bugün şapkalı çiçekler"
   - Cümle 4: «Spin bugün şapkalı çiçekler yapmayı planlamıştı.»
   - Açıklama: Geçmiş zaman anlatımında 'bugün' şimdiki zamana kayıyor; 'o gün' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şapkalı çiçekler yapmayı planlamıştı"
   - Cümle 4: «Spin bugün şapkalı çiçekler yapmayı planlamıştı.»
   - Açıklama: 'Planlamak' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Şimdi çok üzgündü."
   - Cümle 5: «Şimdi çok üzgündü.»
   - Açıklama: Geçmiş zaman anlatımında 'şimdi' zaman kayması yaratıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0139` birebir aynı, ardından `@onarim: 0ea0bf742673893a2df99d693c193e60e5058bd0`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0140 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0140
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kağıt', fiil 'seslenmek', sıfat 'temiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: kağıt şapkaya doğru büyük bir dalga geliyordu | sorunu fark etti ve sudan uzağa koştu
@tohum: orumcek_adam-0140
@degisim: seslenmek -> katlamak
Bir sabah Örümcek Adam su kenarında gemi oyunu oynuyordu. Temiz bir kağıttan bir şapka katladı ve başına taktı. Ama arkasından büyük bir dalga geliyordu ve Örümcek Adam onu görmüyordu. Birden örümcek hissi sayesinde bir sorun olduğunu anladı. Hemen arkasına döndü ve dalgayı gördü. Şapkasını eliyle tuttu ve sudan uzağa koştu. Dalga onun az önce durduğu yere kadar geldi. Kağıt şapka hiç ıslanmadı. Örümcek Adam kumsalın kuru bir yerine oturdu. Sonra kağıt şapkasıyla gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "arkasından büyük bir dalga geliyordu"
   - Cümle 3: «Ama arkasından büyük bir dalga geliyordu ve Örümcek Adam onu görmüyordu.»
   - Açıklama: Farkında olmadan arkadan yaklaşan büyük dalga küçük çocuk için korkutucu bir tehlike sahnesi oluşturuyor.
   - Açıklama: Fark edilmeden arkadan gelen büyük dalga küçük çocuk için korkutucu bir öğe.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi sayesinde bir sorun olduğunu anladı"
   - Cümle 4: «Birden örümcek hissi sayesinde bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi', 'sayesinde' ve 'sorun olduğunu anladı' küçük çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0140` birebir aynı, `@degisim: seslenmek -> katlamak` (tutuyorsan), ardından `@onarim: 9bd63241908adc284370f6d792097cb2a11eba36`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0141 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0141
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kozalak', fiil 'serpmek', sıfat 'sisli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: arkadaşı görünmez olup sürprize doğru geliyordu | kalbin üstüne yaprak serpti ve sürprizi sakladı
@tohum: orumcek_adam-0141
Örümcek Adam sisli bir sabah parkta Spin için kozalaklarla bir kalp diziyordu. Birden örümcek hissi bir sorun olduğunu haber verdi. Görünmez Spin ona doğru geliyordu ve kalp daha bitmemişti. Örümcek Adam ağacın altındaki kuru yaprakları hemen kalbin üstüne serpti. Spin, Örümcek Adam'ın yanına gelip görünür oldu ve etrafa baktı. Yerde yalnız yaprak gördü ve resim yapmak için çiçek bahçesine gitti. Örümcek Adam son kozalakları da dikkatle dizdi. Sonra yaprakları kaldırdı, Spin'in elini tuttu ve onu kalbin yanına getirdi. Spin kalbi görünce çok şaşırdı ve güldü. Örümcek Adam çok mutluydu, çünkü sürprizini Spin görmeden bitirmişti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
   - Açıklama: Hissin haber vermesi mecaz ve soyut bir anlatım.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Görünmez Spin ona doğru geliyordu"
   - Cümle 3: «Görünmez Spin ona doğru geliyordu ve kalp daha bitmemişti.»
   - Açıklama: Spin'in neden görünmez olduğu hiç söylenmiyor; görünmezlik sebepsiz beliriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "resim yapmak için çiçek bahçesine gitti"
   - Cümle 6: «Yerde yalnız yaprak gördü ve resim yapmak için çiçek bahçesine gitti.»
   - Açıklama: Spin'in sebepsizce uzaklaşması çözümü tesadüfle getiriyor ve Örümcek Adam'a kalbi bitirme zamanı veriyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Örümcek Adam son kozalakları da dikkatle dizdi"
   - Cümle 7: «Örümcek Adam son kozalakları da dikkatle dizdi.»
   - Açıklama: Kalp yaprakla örtülüyken kozalaklar diziliyor, yapraklar ancak sonra kaldırılıyor; sıra çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0141` birebir aynı, ardından `@onarim: b08d4f2332c910ad80feff4d2ae798056b6135bc`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0142 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0142
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'gömlek', fiil 'görmek', sıfat 'sadık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: top yüksek duvarın arkasına düştü ve görünmedi | duvara tırmanıp topu buldu ve arkadaşına verdi
@tohum: orumcek_adam-0142
@degisim: gömlek -> top
Parkın oyun alanında güneş parlıyordu. Örümcek Adam ile Ghost-Spider orada top oynuyordu. Arkadaşı topu çok yükseğe attı ve top bir duvarın arkasına düştü. Duvar çok yüksekti ve top hiç görünmüyordu. "Topum nereye gitti?" diye sordu arkadaşı üzgün üzgün. "Hemen bakarım," dedi Örümcek Adam. Duvara hızla tırmandı ve tepesine çıktı. Oradan kırmızı topu gördü. Top duvarın hemen yanındaki bir çalıya takılmıştı. Örümcek Adam duvarın üstünden eğildi ve topu aldı. Sonra aşağı indi ve topu arkadaşına verdi. O çok sevindi, çünkü sadık arkadaşı Örümcek Adam topunu bulmuştu.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşı topu çok yükseğe attı"
   - Cümle 3: «Arkadaşı topu çok yükseğe attı ve top bir duvarın arkasına düştü.»
   - Açıklama: 'Arkadaşı' kimin arkadaşı ve Ghost-Spider mı belli değil; ad yerine belirsiz gönderim kullanılmış.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşı topu çok yükseğe"
   - Cümle 3: «Arkadaşı topu çok yükseğe attı ve top bir duvarın arkasına düştü.»
   - Açıklama: İki kahraman da birbirinin arkadaşı olduğu için 'Arkadaşı' kimi gösterdiği belli değil; Ghost-Spider adıyla anılmıyor.
3. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "diye sordu arkadaşı üzgün üzgün"
   - Cümle 5: «"Topum nereye gitti?" diye sordu arkadaşı üzgün üzgün.»
   - Açıklama: Konuşan adıyla belirtilmemiş, yalnız belirsiz 'arkadaşı' deniyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvarın üstünden eğildi ve topu aldı"
   - Cümle 10: «Örümcek Adam duvarın üstünden eğildi ve topu aldı.»
   - Açıklama: Çok yüksek bir duvarın tepesinden aşağı eğilmek çocuğun taklit edebileceği tehlikeli bir davranış olarak gösteriliyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O çok sevindi, çünkü"
   - Cümle 12: «O çok sevindi, çünkü sadık arkadaşı Örümcek Adam topunu bulmuştu.»
   - Açıklama: 'O' zamirinin kimi gösterdiği belli değil; son özne Örümcek Adam.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0142` birebir aynı, `@degisim: gömlek -> top` (tutuyorsan), ardından `@onarim: 9bd32eb0b3233ac471ceeaf1e9a96f860064f2f2`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0143 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0143
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yeni bir şeyi denemek
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'torba', fiil 'izlemek', sıfat 'küçük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: resim çok büyüktü ve yerden bütün çizgiler görünmüyordu | duvara tırmanıp yukarıdan baktı ve eksik bacağı çizdi
@tohum: orumcek_adam-0143
Rüzgar hafif esiyordu. Örümcek Adam ilk kez kumsala kocaman bir resim çiziyordu. Ama resim çok büyüktü ve yerden bütün çizgileri göremiyordu. Hulk da elinde küçük bir torbayla onu izliyordu. Örümcek Adam limanın yüksek duvarına tırmandı ve aşağı baktı. Kumdaki resim bir örümcekti ama bir bacağı eksikti. Hemen aşağı indi ve eksik bacağı da çizdi. Hulk torbasından iki deniz kabuğu çıkarıp ona verdi. Örümcek Adam kabukları örümceğin gözlerine koydu. Artık resim tamamdı. Hulk sevinçle alkışladı. Örümcek Adam çok sevindi, çünkü ilk kum resmini bitirmişti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yerden bütün çizgileri göremiyordu"
   - Cümle 3: «Ama resim çok büyüktü ve yerden bütün çizgileri göremiyordu.»
   - Açıklama: Bağlaçla bağlanan ikinci yüklemin öznesi 'resim' gibi okunuyor; özne uyumu bozuk.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "limanın yüksek duvarına tırmandı"
   - Cümle 5: «Örümcek Adam limanın yüksek duvarına tırmandı ve aşağı baktı.»
   - Açıklama: Kumsalda önceden kurulmamış liman duvarı çözümü getirmek için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0143` birebir aynı, ardından `@onarim: 92995bfd8a6fe3fe6de20eb0a67b9f57d734c5dc`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0144 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0144
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'yiyecek', fiil 'ıslanmak', sıfat 'umutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: dalgalar yükselince duvardaki resimler ıslanmaya başladı | duvara tırmanıp resimleri en yükseğe astı
@tohum: orumcek_adam-0144
Dalgalar gürültüyle limanın duvarına çarpıyordu. Örümcek Adam, Spin için limanda bir sürpriz hazırlıyordu. Spin'in resimlerini duvarın altına asmıştı ama dalgalar yükselince resimler ıslanmaya başladı. Örümcek Adam onları hemen topladı. Sonra duvara tırmandı ve resimleri en yükseğe astı. Dalgalar artık onlara ulaşamıyordu. Örümcek Adam aşağı indi ve yanındaki sepetten yiyecekleri çıkardı. Sonra umutlu bir yüzle Spin'i bekledi. Az sonra Spin geldi ve duvardaki resimlerini gördü. "Bu sürpriz çok güzel, Örümcek Adam!" dedi Spin. "Hepsi senin için, Spin," dedi Örümcek Adam. İki arkadaş kumsalda yiyecekleri birlikte yedi. Örümcek Adam çok mutluydu, çünkü sürprizi Spin'i sevindirmişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "resimlerini duvarın altına asmıştı"
   - Cümle 3: «Spin'in resimlerini duvarın altına asmıştı ama dalgalar yükselince resimler ıslanmaya başladı.»
   - Açıklama: Resim duvarın altına asılmaz; 'duvarın alt kısmına' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra umutlu bir yüzle"
   - Cümle 8: «Sonra umutlu bir yüzle Spin'i bekledi.»
   - Açıklama: 'Umutlu' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "umutlu bir yüzle Spin'i"
   - Cümle 8: «Sonra umutlu bir yüzle Spin'i bekledi.»
   - Açıklama: 'Umutlu bir yüzle' soyut bir anlatım, küçük çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0144` birebir aynı, ardından `@onarim: a80f043bb6572425b52e50f7efe4384ba6809063`, sonra gövde.
