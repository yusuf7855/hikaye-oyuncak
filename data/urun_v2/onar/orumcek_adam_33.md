# Editör görevi (onarım): Örümcek Adam, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar33.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0111 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0111
- yer: ev (Takımın gizli evi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'bez', fiil 'savrulmak', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: rüzgar bezi uçurdu ve bez bir resmin arkasına girdi | duvara tırmanıp arkadaşından yardım istedi
@tohum: orumcek_adam-0111
Bir sabah Örümcek Adam ile Spin gizli evde resim yapıyordu. Açık pencereden sert bir rüzgar esti ve Spin'in boya bezi havaya savruldu. Bez duvarın en üstündeki resimlerin arkasında saklı kaldı. Spin'in fırçaları boyalı kaldı ve Spin üzüldü. Örümcek Adam süper gücüyle duvara tırmandı. Ama yukarıda üç resim vardı ve bez görünmüyordu. Örümcek Adam aşağıdaki Spin'den yardım istedi. Spin aşağıdan bakınca bezin ucunu gördü ve sarı resmi gösterdi. Örümcek Adam sarı resmin arkasına baktı ve bezi buldu. Aşağı indi ve bezi Spin'e verdi. Spin fırçalarını sildi ve yeniden resim yapmaya başladı. Örümcek Adam çok sevindi, çünkü Spin'e sorunca bezi hemen bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bez duvarın en üstündeki resimlerin arkasında saklı kaldı"
   - Cümle 3: «Bez duvarın en üstündeki resimlerin arkasında saklı kaldı.»
   - Açıklama: Rüzgarın bir boya bezini duvarın en üstündeki resimlerin arkasına sokması akla yatkın değil ve kaybolan bir bez çocuk için önemsiz bir sorun.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam süper gücüyle duvara tırmandı"
   - Cümle 5: «Örümcek Adam süper gücüyle duvara tırmandı.»
   - Açıklama: Güvenli özellik kullanımı ev içi tırmanmayı dışlıyor; gizli evin içinde yüksekteki bir eşyaya ulaşmak için tırmanma çocuğa taklit edilebilir örnek oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0111` birebir aynı, ardından `@onarim: 3df2fe799da28d4049ebeab9c17deb89a7fe3006`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0112 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0112
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'tabela', fiil 'yağmak', sıfat 'yapraklı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar topu uçurdu ve top tabelanın arkasına sıkıştı | ağ atıp topu tabelanın arkasından çekti
@tohum: orumcek_adam-0112
@degisim: yağmak -> zıplamak
Bir sabah Örümcek Adam ile Ghost-Spider kumsalda top oynuyordu. Top, tabeladaki yapraklı ağaç resmine değince sevinçle zıplıyorlardı. Ama rüzgar topu uçurdu ve top yüksek tabelanın arkasına sıkıştı. "Topumuz orada kaldı!" dedi arkadaşı. Örümcek Adam tabelaya baktı ve gülümsedi. "Üzülme, ben onu alırım," dedi Örümcek Adam. Hemen ağ attı ve ağ topa yapıştı. Ağı çekince top tabelanın arkasından çıktı ve kuma düştü. Arkadaşı topu aldı ve yeniden attı. Top ağaç resmine değdi ve ikisi sevinçle zıpladı. Örümcek Adam çok sevindi, çünkü oyunları yeniden başlamıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Top, tabeladaki yapraklı ağaç resmine değince sevinçle zıplıyorlardı"
   - Cümle 2: «Top, tabeladaki yapraklı ağaç resmine değince sevinçle zıplıyorlardı.»
   - Açıklama: Yan cümlenin öznesi 'top', ana fiil 'zıplıyorlardı' ile özne uyumu bozuk ve cümle karışık.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Top, tabeladaki yapraklı"
   - Cümle 2: «Top, tabeladaki yapraklı ağaç resmine değince sevinçle zıplıyorlardı.»
   - Açıklama: Zarf-fiil cümlesinin öznesinden sonra gereksiz virgül konmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0112` birebir aynı, `@degisim: yağmak -> zıplamak` (tutuyorsan), ardından `@onarim: f67fa544300b3e90ac34797329f2e0c9d2c4333f`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0113 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0113
- yer: ev (Takımın gizli evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'menekşe', fiil 'yoğurmak', sıfat 'masmavi'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: oyun hamuru yüksek tavana yapıştı | duvara tırmanıp hamuru tavandan aldı
@tohum: orumcek_adam-0113
Dışarıda yağmur yağıyordu. Örümcek Adam, gizli evlerinde masmavi oyun hamuru yoğuran Hulk'ı izliyordu. Hulk hamuru çok hızlı yukarı attı ve hamur tavana yapıştı. "Hamurdan menekşe yapacaktım ama tavan çok yüksek!" dedi Hulk. "Ben sana yardım ederim, Hulk," dedi Örümcek Adam. Örümcek Adam süper gücüyle duvara tırmandı ve tavana kadar çıktı. Yapışkan hamuru tavandan yavaşça çekip aldı. Sonra aşağı indi ve hamuru Hulk'a verdi. Hulk bu kez hamura yavaşça şekil verdi ve güzel bir menekşe yaptı. "Teşekkürler, bu menekşe senin!" dedi Hulk. Örümcek Adam çok sevindi, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "süper gücüyle duvara tırmandı ve tavana kadar çıktı"
   - Cümle 6: «Örümcek Adam süper gücüyle duvara tırmandı ve tavana kadar çıktı.»
   - Açıklama: Güvenli özellik kullanımı satırı ev içi tırmanmayı dışlar; burada evin içinde tavana kadar tırmanılıyor ve çocuk yüksekteki bir şeyi almak için tırmanmayı taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0113` birebir aynı, ardından `@onarim: d02bb12b743da9ebed13915285cafad3b7875053`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0114 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0114
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'şemsiye', fiil 'ekmek', sıfat 'kirli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar sürpriz şemsiyeyi uçurdu ve şemsiye duvara takıldı | duvara tırmanıp şemsiyeyi aldı ve kuma dikti
@tohum: orumcek_adam-0114
@degisim: ekmek -> süslemek
Örümcek Adam kumsalda Ghost-Spider için bir sürpriz hazırlıyordu. Ona büyük bir şemsiye ve renkli kağıtlar getirmişti. Ama rüzgar şemsiyeyi uçurdu ve şemsiye yüksek bir duvara takıldı. Arkadaşı güneşte davul çalıyordu ve bunu görmedi. Duvar kirliydi ama Örümcek Adam ona kolayca tırmandı. Şemsiyeyi aldı ve yavaşça aşağı indi. Sonra şemsiyeyi kuma dikti ve kağıtlarla süsledi. "Gel, sana bir sürprizim var!" diye seslendi Örümcek Adam. Arkadaşı geldi ve süslü şemsiyeyi gördü. "Ne güzel bir şemsiye, çok teşekkürler!" dedi arkadaşı. İkisi şemsiyenin gölgesinde yan yana oturdu. Örümcek Adam çok mutluydu, çünkü sürprizi arkadaşını sevindirmişti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ona büyük bir şemsiye"
   - Cümle 2: «Ona büyük bir şemsiye ve renkli kağıtlar getirmişti.»
   - Açıklama: 'Ona' zamiri belirsiz; şemsiye getirilen kişi arkadaş mı belli değil ve arkadaş sonra hiçbir şey görmüyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Duvar kirliydi ama Örümcek"
   - Cümle 5: «Duvar kirliydi ama Örümcek Adam ona kolayca tırmandı.»
   - Açıklama: 'Kirli' tırmanmayı zorlaştıran bir özellik değil; 'ama' ile kurulan karşıtlık anlamsız.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Duvar kirliydi ama Örümcek Adam"
   - Cümle 5: «Duvar kirliydi ama Örümcek Adam ona kolayca tırmandı.»
   - Açıklama: Duvarın kirli olması engel gibi kuruluyor ama hiçbir işe yaramıyor.
   - Açıklama: Duvarın kirli olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0114` birebir aynı, `@degisim: ekmek -> süslemek` (tutuyorsan), ardından `@onarim: 19860e48ba0a30dd32f3a4f82efafbb76630d388`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0116 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0116
- yer: ev (Takımın gizli evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'tablo', fiil 'ayırmak', sıfat 'yaratıcı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: açık pencereden gelen rüzgar resmi duvara yapıştırdı | özür dileyip tırmandı ve resmi duvardan ayırdı
@tohum: orumcek_adam-0116
@degisim: tablo -> resim
Rüzgar gizli evin açık penceresinden içeri esiyordu. Örümcek Adam pencereyi açık bırakmıştı ve yaratıcı Hulk kağıda bir resim yapıyordu. Birden rüzgar ıslak resmi uçurdu ve resim yüksek duvara yapıştı. "Resim çok yukarıda kaldı!" dedi Hulk. "Özür dilerim, Hulk, pencereyi ben açık bıraktım," dedi Örümcek Adam. Örümcek Adam önce pencereyi kapattı. Sonra duvara tırmandı ve resmi duvardan yavaşça ayırdı. Aşağı indi ve resmi Hulk'a verdi. "Sorun yok, dostum," dedi Hulk ve gülümsedi. Sonra Örümcek Adam ile Hulk resmi birlikte mutlu mutlu boyamaya devam etti.
```

**Hakem bulguları (3):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "yaratıcı Hulk kağıda bir resim"
   - Cümle 2: «Örümcek Adam pencereyi açık bırakmıştı ve yaratıcı Hulk kağıda bir resim yapıyordu.»
   - Açıklama: Kartın yanlar bölümünde resim yapmak Spin'in özelliği; Hulk kocaman ve güçlü bir yardımcı olarak tanımlanıyor, yaratıcı ressam olarak değil.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "yaratıcı Hulk kağıda bir resim yapıyordu"
   - Cümle 2: «Örümcek Adam pencereyi açık bırakmıştı ve yaratıcı Hulk kağıda bir resim yapıyordu.»
   - Açıklama: Resim yapma kartın yanlar bölümünde Spin'in özelliğidir; Hulk'ın ilişki tarifinde yok.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra duvara tırmandı ve"
   - Cümle 7: «Sonra duvara tırmandı ve resmi duvardan yavaşça ayırdı.»
   - Açıklama: Ev içinde süper güç vurgusu olmadan duvara tırmanılıyor; güvenli kullanım satırı ev içi taklit edilebilir tırmanmayı yasaklıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0116` birebir aynı, `@degisim: tablo -> resim` (tutuyorsan), ardından `@onarim: 3661f95015a67596c13a9a045d89c6f2e512a33c`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0117 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0117
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'çamur', fiil 'güneşlenmek', sıfat 'kırılgan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: top hızla uçtu ve çamura düşecekti | ağ atıp topu havada yakaladı
@tohum: orumcek_adam-0117
@degisim: kırılgan -> renkli
Bir sabah Örümcek Adam ile Ghost-Spider parkta çimenlere uzanıp güneşleniyordu. Sonra kalkıp renkli bir topla oynamaya başladılar. Bir ara top rüzgarla çok hızlı uçtu ve çamura doğru gitti. "Topumuz çamura düşecek!" diye bağırdı Örümcek Adam. Örümcek Adam hemen elini kaldırdı ve bir ağ attı. Ağ, topu havada yakaladı. Örümcek Adam onu yavaşça kendine çekti. Top tertemiz kalmıştı. İkisi de sevinçle güldü. "Şimdi sıra sende," dedi Örümcek Adam ve topu ona verdi. İkisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "top rüzgarla çok hızlı uçtu ve çamura doğru gitti"
   - Cümle 3: «Bir ara top rüzgarla çok hızlı uçtu ve çamura doğru gitti.»
   - Açıklama: Topun çamura düşecek olması önemsiz bir olay ve tek hamlede hemen çözülüp bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0117` birebir aynı, `@degisim: kırılgan -> renkli` (tutuyorsan), ardından `@onarim: 3c9f1f51ff34e3d6b791f082f86562464f738c54`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0118 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0118
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'turşu', fiil 'sabırsızlanmak', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: büyük bir dalga turşu kavanozuna doğru geldi | kavanozu hemen kapıp sudan uzağa taşıdı
@tohum: orumcek_adam-0118
@degisim: sabırlı -> ekşi
Örümcek Adam kumsalda ilk kez ekşi bir turşu deneyecekti. Turşu kavanozunu kumun üstüne koydu ve tadına bakmak için sabırsızlandı. Birden örümcek hissiyle büyük bir dalganın kavanoza doğru geldiğini anladı. Örümcek Adam kavanozu hemen kaptı ve geriye doğru koştu. Dalga, kavanozun durduğu yeri ıslattı ve denize geri çekildi. Kavanozun üstüne tek bir damla bile gelmemişti. Örümcek Adam kapağı açtı ve bir turşu aldı. Onu yavaşça çiğnedi. Tadını çok beğendi ve bir tane daha yedi. Örümcek Adam bundan sonra yiyeceklerini hep sudan uzak bir yere koydu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tadına bakmak için sabırsızlandı"
   - Cümle 2: «Turşu kavanozunu kumun üstüne koydu ve tadına bakmak için sabırsızlandı.»
   - Açıklama: 'Sabırsızlandı' 3 yaşındaki bir çocuk için soyut bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle büyük"
   - Cümle 3: «Birden örümcek hissiyle büyük bir dalganın kavanoza doğru geldiğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Örümcek hissi' küçük çocuğun bilmeyeceği soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0118` birebir aynı, `@degisim: sabırlı -> ekşi` (tutuyorsan), ardından `@onarim: 8c62fe7ad9ab94dc26e66b18d3c6c5ad9b528d34`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0119 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | -
@tohum: orumcek_adam-0119
- yer: ev (Takımın gizli evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'bluz', fiil 'dağıtmak', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | -
@plan: çantada bir delik vardı ve paket kayıyordu | düşen paketi yakaladı ve deliği sıkıca bağladı
@tohum: orumcek_adam-0119
Yağmur gizli evin çatısına tıp tıp vuruyordu. Örümcek Adam içeride paket oyunu oynuyor ve paketleri odalara dağıtıyordu. Ama çantasının altında küçük bir delik vardı ve bir paket oradan kayıyordu. Çanta onun arkasındaydı ve Örümcek Adam deliği göremedi. Birden örümcek hissiyle bir sorun olduğunu anladı. Hemen çantasına baktı. İçinde yepyeni bir bluz olan paket delikten düşmek üzereydi. Örümcek Adam paketi elleriyle yakaladı. Sonra deliğin olduğu yeri sıkıca bağladı. Kalan paketleri de odalara tek tek bıraktı. Örümcek Adam çok sevindi, çünkü hiçbir paket yere düşmedi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "deliği sıkıca bağladı"
   - Cümle 0 (plan satırı): «çantada bir delik vardı ve paket kayıyordu | düşen paketi yakaladı ve deliği sıkıca bağladı»
   - Açıklama: Delik bağlanmaz; fiil nesnesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun olduğunu anladı"
   - Cümle 5: «Birden örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İçinde yepyeni bir bluz olan paket"
   - Cümle 7: «İçinde yepyeni bir bluz olan paket delikten düşmek üzereydi.»
   - Açıklama: Bluz ayrıntısı olayda hiçbir işe yaramıyor.
   - Açıklama: Paketin içindeki bluz sebepsiz beliren ve olayda işlevi olmayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0119` birebir aynı, ardından `@onarim: 7f53b55cd560fd2200eb8bac49075edc84e496e7`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0120 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0120
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'ayçiçeği', fiil 'güzelleşmek', sıfat 'gizemli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: suyun içindeki parlak şey kıyıdan uzaktaydı | ağ atıp parlak şeyi kıyıya çekti
@tohum: orumcek_adam-0120
Kıyıda dalgalar şırıl şırıl ses çıkarıyordu. Örümcek Adam ile Spin suyun içinde gizemli, parlak bir şey gördü. Onu yakından görmek istediler ama o şey kıyıdan uzaktaydı. "Bu ne olabilir, Örümcek Adam?" diye sordu Spin. Örümcek Adam kıyıda durdu ve ağ attı. Ağ parlak şeye yapıştı ve Örümcek Adam onu kıyıya çekti. Parlak şey, içi pembe büyük bir deniz kabuğu çıktı. "Ne güzel bir kabuk!" dedi Spin. Spin kuma parmağıyla büyük bir ayçiçeği çizdi. Örümcek Adam kabuğu ayçiçeğinin ortasına koydu ve resim daha da güzelleşti. Örümcek Adam bundan sonra kumsalda parlak şeylere hep dikkatle baktı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dalgalar şırıl şırıl ses"
   - Cümle 1: «Kıyıda dalgalar şırıl şırıl ses çıkarıyordu.»
   - Açıklama: 'şırıl şırıl' akan su içindir, dalgalara uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "suyun içinde gizemli, parlak"
   - Cümle 2: «Örümcek Adam ile Spin suyun içinde gizemli, parlak bir şey gördü.»
   - Açıklama: 'gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Spin kuma parmağıyla büyük bir ayçiçeği çizdi"
   - Cümle 9: «Spin kuma parmağıyla büyük bir ayçiçeği çizdi.»
   - Açıklama: Ayçiçeği çizimi sorundan ya da çözümden çıkmıyor, sebepsiz eklenmiş bir olay.
   - Açıklama: Ayçiçeği resmi sorunla ilgisiz, sebepsiz beliren yeni bir olay.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "parlak şeylere hep dikkatle baktı"
   - Cümle 11: «Örümcek Adam bundan sonra kumsalda parlak şeylere hep dikkatle baktı.»
   - Açıklama: Son ders cümlesi yaşanan olaydan çıkmıyor; hikayede dikkatsizlikten doğan bir sorun yok.
   - Açıklama: Son cümle olaydan çıkmayan belirsiz bir ders; sıcak bir kapanış vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0120` birebir aynı, ardından `@onarim: e0cb6f758c657fe59a8bd1aac71f4c7a6512505c`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0121 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0121
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'rüzgar', fiil 'bitirmek', sıfat 'sessiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: uçurtmanın ipi iyi bağlı değildi | ipi açıp sıkıca yeniden bağladı
@tohum: orumcek_adam-0121
Rüzgar sessiz kumsalda esiyordu. Örümcek Adam ilk uçurtmasını yeni bitirmişti. Ama örümcek hissiyle ipin iyi bağlı olmadığını anladı. İp böyle kalırsa uçurtma uçup gidebilirdi. Örümcek Adam ipi çözdü. Sonra onu sıkı sıkı yeniden bağladı. Uçurtmayı başının üstüne kaldırdı ve koştu. Rüzgar uçurtmayı yavaş yavaş yukarı taşıdı. Uçurtma limanın üstüne çıktı. Düğüm sağlam kaldı. Kırmızı uçurtma uzun süre mavi gökyüzünde uçtu. Örümcek Adam çok sevindi, çünkü kendi yaptığı ilk uçurtma havalandı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ipi açıp sıkıca yeniden"
   - Cümle 0 (plan satırı): «uçurtmanın ipi iyi bağlı değildi | ipi açıp sıkıca yeniden bağladı»
   - Açıklama: İp açılmaz, düğüm açılır ya da ip çözülür; fiil nesnesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama örümcek hissiyle ipin"
   - Cümle 3: «Ama örümcek hissiyle ipin iyi bağlı olmadığını anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0121` birebir aynı, ardından `@onarim: df069861f81a802859733302aad0ae77f4c40f6a`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0123 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0123
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'fıskiye', fiil 'sürtmek', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: top çok güçlü atıldı ve duvarın üstünde kaldı | süper gücüyle duvara tırmanıp topu indirdi
@tohum: orumcek_adam-0123
@degisim: dolu -> sarı
Fıskiyenin sesi bütün parkta duyuluyordu. Örümcek Adam ile Hulk fıskiyenin yanında sırayla sarı bir top atıyordu. Hulk çok güçlü attı ve top bahçedeki duvarın üstünde kaldı. Hulk üzgün üzgün duvara baktı. Örümcek Adam süper gücüyle duvara hızla tırmandı. Topu aldı ve aşağı indi. Sıra Örümcek Adam'daydı ve topu yavaşça Hulk'a attı. Hulk topu kocaman elleriyle yakaladı. Sonra tozlu topu çimene sürtüp temizledi. Bu kez Hulk da topu hafifçe attı. Örümcek Adam ile Hulk sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "top çok güçlü atıldı"
   - Cümle 0 (plan satırı): «top çok güçlü atıldı ve duvarın üstünde kaldı | süper gücüyle duvara tırmanıp topu indirdi»
   - Açıklama: Plan satırında 'güçlü' zarf yerinde yanlış kullanılmış; 'çok sert atıldı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hulk çok güçlü attı"
   - Cümle 3: «Hulk çok güçlü attı ve top bahçedeki duvarın üstünde kaldı.»
   - Açıklama: 'Güçlü' sıfat olarak zarf yerinde kullanılmış; 'çok sert attı' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra tozlu topu çimene sürtüp temizledi"
   - Cümle 9: «Sonra tozlu topu çimene sürtüp temizledi.»
   - Açıklama: Topun tozlanması hiçbir sebeple kurulmadan beliriyor ve olaya bir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0123` birebir aynı, `@degisim: dolu -> sarı` (tutuyorsan), ardından `@onarim: 52c939906f7fc27db7891f4148ee62b8cd8f50cb`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0124 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0124
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'sepet', fiil 'yaklaşmak', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: eski sepetin altındaki delikten kabuklar düşüyordu | deliğin üstüne büyük ve düz bir kabuk koydu
@tohum: orumcek_adam-0124
Kumsalda hafif bir rüzgar esiyordu. Örümcek Adam gemi oyunu oynuyordu ve hazine olarak kabuk topluyordu. Birden örümcek hissi bir sorun olduğunu haber verdi: eski sepetin altı delikti. Örümcek Adam arkasına baktı. Topladığı kabuklar tek tek kuma düşmüştü. Hemen bütün kabukları yeniden topladı. Sonra kıyıya yaklaştı ve büyük, düz bir kabuk buldu. Düz kabuğu sepetin içine, deliğin üstüne koydu. Bu kez hiçbir kabuk düşmedi. Sepet kısa sürede parlak kabuklarla doldu. Örümcek Adam bundan sonra sepetin altına hep baktı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu"
   - Cümle 3: «Birden örümcek hissi bir sorun olduğunu haber verdi: eski sepetin altı delikti.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' soyut ve mecazlı; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi bir sorun olduğunu haber verdi: eski sepetin altı delikti.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuğa uygun değil.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hemen bütün kabukları yeniden topladı"
   - Cümle 6: «Hemen bütün kabukları yeniden topladı.»
   - Açıklama: Delik kapatılmadan kabuklar yeniden toplanıyor; çözüm sebebe doğrudan yönelmeden fazladan bir adımla başlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0124` birebir aynı, ardından `@onarim: d1bff050aeddddc6e6506ba714be7d421f7d3f02`, sonra gövde.
