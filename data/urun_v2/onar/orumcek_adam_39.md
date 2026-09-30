# Editör görevi (onarım): Örümcek Adam, onarım partisi 39

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar39.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0143 (deneme 2 -> 3)

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
Rüzgar hafif esiyordu. Örümcek Adam ilk kez bir duvarın yanındaki kuma kocaman bir resim çiziyordu. Ama resim çok büyüktü ve Örümcek Adam yerden bütün çizgileri göremiyordu. Hulk da elinde küçük bir torbayla onu izliyordu. Örümcek Adam bu duvara tırmandı ve aşağı baktı. Kumdaki resim bir örümcekti ama bir bacağı eksikti. Hemen aşağı indi ve eksik bacağı da çizdi. Hulk torbasından iki deniz kabuğu çıkarıp ona verdi. Örümcek Adam kabukları örümceğin gözlerine koydu. Artık resim tamamdı. Hulk sevinçle alkışladı. Örümcek Adam çok sevindi, çünkü ilk kum resmini bitirmişti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam bu duvara tırmandı ve aşağı baktı"
   - Cümle 5: «Örümcek Adam bu duvara tırmandı ve aşağı baktı.»
   - Açıklama: Tırmanma süper güç olarak çerçevelenmeden, çocuğun taklit edebileceği biçimde resme bakmak için duvara çıkılıyor; güvenli özellik kullanımı satırına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0143` birebir aynı, ardından `@onarim: 163e88ea216730854b6d43e8cef22845c132aed4`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0144 (deneme 2 -> 3)

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
@plan: dalgalar gelince duvardaki resimler ıslanmaya başladı | duvara tırmanıp resimleri en yükseğe astı
@tohum: orumcek_adam-0144
@degisim: umutlu -> güzel
Dalgalar gürültüyle limanın duvarına çarpıyordu. Örümcek Adam, Spin için limanda bir sürpriz hazırlıyordu. Spin'in resimlerini duvarda suya yakın bir yere asmıştı. Ama dalgalar gelince resimler ıslanmaya başladı. Örümcek Adam onları hemen topladı. Sonra duvara tırmandı ve resimleri en yükseğe astı. Dalgalar artık onlara ulaşamıyordu. Örümcek Adam aşağı indi ve yanındaki sepetten yiyecekleri çıkardı. Sonra oturdu ve Spin'i bekledi. Az sonra Spin geldi ve duvardaki resimlerini gördü. "Bu sürpriz çok güzel, Örümcek Adam!" dedi Spin. "Hepsi senin için, Spin," dedi Örümcek Adam. İki arkadaş kumsalda yiyecekleri birlikte yedi. Örümcek Adam çok mutluydu, çünkü sürprizi Spin'i sevindirmişti.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "duvarda suya yakın bir yere asmıştı"
   - Cümle 3: «Spin'in resimlerini duvarda suya yakın bir yere asmıştı.»
   - Açıklama: Dalgaların çarptığı liman duvarında suya yakın yerde eşya asıp toplamak çocuğun taklit edebileceği su kenarı davranışı.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Spin'in resimlerini duvarda suya yakın bir yere asmıştı.»
   - Açıklama: İlk üç cümle yalnız hazırlık; sorun ancak 4. cümlede resimler ıslanınca söyleniyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra duvara tırmandı ve resimleri en yükseğe astı"
   - Cümle 6: «Sonra duvara tırmandı ve resimleri en yükseğe astı.»
   - Açıklama: Dalgaların çarptığı liman duvarına süper güç diye belirtilmeden tırmanılıyor; güvenli özellik kullanımı satırına göre tırmanma yalnız süper güç olarak geçmeli ve taklit edilebilir.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "İki arkadaş kumsalda yiyecekleri birlikte yedi"
   - Cümle 13: «İki arkadaş kumsalda yiyecekleri birlikte yedi.»
   - Açıklama: Hikaye limanın duvarında geçerken sonda sebepsizce kumsala geçiyor; tek sahne bozuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0144` birebir aynı, `@degisim: umutlu -> güzel` (tutuyorsan), ardından `@onarim: fcbd30aecc744eceea35424faf3542e53e268a98`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0145 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0145
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: paylaşmak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gevrek', fiil 'oturmak', sıfat 'açık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: arkadaşı yiyeceğini unutmuştu ve acıkmıştı | gevreği ikiye böldü ve onunla paylaştı
@tohum: orumcek_adam-0145
@degisim: açık -> sıcak
Örümcek Adam parkta bir bankta oturup gevrek yiyordu. Birden örümcek hissi ile bir sorun olduğunu anladı. Ağacın altında Ghost-Spider aç ve üzgündü, çünkü yiyeceğini gizli evde unutmuştu. Örümcek Adam elindeki gevreği ikiye böldü. Sonra arkadaşının yanına gitti. "Bunun yarısı senin," dedi Örümcek Adam. Arkadaşı gevreği aldı ve "Çok teşekkür ederim!" dedi. İkisi onu ağacın altında birlikte yedi. Gevrek sıcak ve çıtır çıtırdı. Arkadaşı artık aç değildi ve çok mutluydu. Örümcek Adam bundan sonra yiyeceğini arkadaşlarıyla hep paylaştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 2: «Birden örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ile sorunu anlamak soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anlamak' soyut ifadeler; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0145` birebir aynı, `@degisim: açık -> sıcak` (tutuyorsan), ardından `@onarim: 771bb03e3a424646bd60a6817b8c8a1cf794df9e`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0146 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0146
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'çember', fiil 'yumuşamak', sıfat 'biberli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: çember çamura derin battı ve çıkmadı | duvara tırmanıp güçlü arkadaşından yardım istedi
@tohum: orumcek_adam-0146
@degisim: biberli -> kırmızı
Bir sabah Örümcek Adam parkta kırmızı çemberiyle oynuyordu. Çember çiçek bahçesine yuvarlandı ve çamura derin battı. Bahçenin toprağı suyla çok yumuşamıştı. Örümcek Adam çemberi iki eliyle çekti ama çamur çok yapışkandı. Hulk da parktaydı ama ağaçların arasında görünmüyordu. Örümcek Adam süper gücüyle duvara tırmandı. Oradan Hulk'ı oyun alanında gördü. "Hulk, bana yardım eder misin?" diye seslendi Örümcek Adam. Hulk hemen koşup geldi. Kocaman eliyle çemberi tuttu ve kolayca çıkardı. Sonra çemberi Örümcek Adam'a verdi. Örümcek Adam çok sevindi, çünkü Hulk'tan yardım isteyerek çemberini geri almıştı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve çamura derin battı"
   - Cümle 2: «Çember çiçek bahçesine yuvarlandı ve çamura derin battı.»
   - Açıklama: Zarf olarak yönelme eki eksik; 'çamura derine battı' ya da 'çamura iyice battı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve çamura derin battı"
   - Cümle 2: «Çember çiçek bahçesine yuvarlandı ve çamura derin battı.»
   - Açıklama: 'Derin' sıfatı zarf yerine yanlış kullanılmış; 'derine/iyice battı' olmalı (plan satırında da aynı).
3. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Örümcek Adam süper gücüyle duvara tırmandı"
   - Cümle 6: «Örümcek Adam süper gücüyle duvara tırmandı.»
   - Açıklama: Kartın park tarifi oyun alanı, ağaçlar ve çiçek bahçesi sayıyor; tırmanılan duvar tarifte yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0146` birebir aynı, `@degisim: biberli -> kırmızı` (tutuyorsan), ardından `@onarim: d111e2e6485071fba23e8344af5bcc0c5518394d`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0147 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0147
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'kravat', fiil 'ovmak', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: yüksek duvarın tepesinden bilinmeyen bir ses geldi | duvara tırmanıp sesi yapan balonu buldu
@tohum: orumcek_adam-0147
@degisim: kravat -> balon
Parkta ince bir ses duyuluyordu. Örümcek Adam ile Ghost-Spider sesin nereden geldiğini merak etti. Ses yüksek bir duvarın tepesinden geliyordu ama yerden bir şey görünmüyordu. Arkadaşı sesi duyunca çok konuşkan oldu. "Orada ne var, Örümcek Adam?" diye sordu. "Ben bakarım," dedi Örümcek Adam. Süper gücüyle duvarın tepesine tırmandı. Tepede ipi takılmış mavi bir balon vardı. Rüzgar esince balon duvara değiyor ve ses çıkarıyordu. Örümcek Adam ipi dikkatle çözdü ve balonla aşağı indi. Balonu eliyle ovdu ve yine aynı ses geldi. "Demek ses balondan geliyormuş!" dedi arkadaşı ve güldü. Örümcek Adam ve arkadaşı çok sevindi, çünkü sesi yapan balonu bulmuşlardı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi duyunca çok konuşkan oldu"
   - Cümle 4: «Arkadaşı sesi duyunca çok konuşkan oldu.»
   - Açıklama: 'Konuşkan olmak' bir huy bildirir, bir anlık soru sorma durumuna uymuyor.
   - Açıklama: 'Konuşkan olmak' bir anlık merakı anlatmak için yanlış kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sesi duyunca çok konuşkan oldu"
   - Cümle 4: «Arkadaşı sesi duyunca çok konuşkan oldu.»
   - Açıklama: 'Konuşkan' soyut bir kişilik kelimesi, 3 yaşındaki çocuk için uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Arkadaşı sesi duyunca çok konuşkan oldu"
   - Cümle 4: «Arkadaşı sesi duyunca çok konuşkan oldu.»
   - Açıklama: Arkadaşın konuşkan olması işlevsiz ve sebepsiz bir ayrıntı.
   - Açıklama: Arkadaşın konuşkanlığı sebepsiz kuruluyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0147` birebir aynı, `@degisim: kravat -> balon` (tutuyorsan), ardından `@onarim: ee24e61fa45579fdca7b377aa3e026463507cfbe`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0148 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0148
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'flüt', fiil 'uçmak', sıfat 'kalın'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: rüzgar sürpriz uçurtmayı banktan uçurmaya başladı | kuyruğunu yakalayıp uçurtmaya kalın ip bağladı
@tohum: orumcek_adam-0148
@degisim: flüt -> uçurtma
Örümcek Adam, Spin'e sürpriz olsun diye uçurtma ve kalın ip getirdi. Birden örümcek hissiyle bir sorun olduğunu anladı. Sert bir rüzgar esti ve uçurtma banktan uçmaya başladı. Örümcek Adam hemen döndü ve uçurtmanın kuyruğunu yakaladı. Sonra uçurtmaya ipi sıkıca bağladı. Az sonra Spin parka geldi. "Bu uçurtma senin için, Spin," dedi Örümcek Adam. "Çok güzel, teşekkür ederim!" dedi Spin sevinçle. İki arkadaş ipi birlikte tuttu. Uçurtma rüzgarla gökyüzüne uçtu. Spin mutlu mutlu güldü. Örümcek Adam bundan sonra rüzgarlı havada uçurtmaya hep önce ip bağladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun olduğunu anladı"
   - Cümle 2: «Birden örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve bir sorunu sezmek soyut kavramlardır, 3 yaşındaki çocuk anlamaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle bir"
   - Cümle 2: «Birden örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0148` birebir aynı, `@degisim: flüt -> uçurtma` (tutuyorsan), ardından `@onarim: a083a9dd1bc27f2598d3cbc90e2d6f88a3e763b2`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0149 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0149
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'salata', fiil 'uzanmak', sıfat 'süslü'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: masa sallanıyordu ve salata kabı düşmek üzereydi | uzanıp kabı tuttu ve masanın ayağına taş koydu
@tohum: orumcek_adam-0149
Parkta, çiçek bahçesinin yanında, Örümcek Adam Hulk'a bir sürpriz hazırlıyordu. Eski bir masaya kocaman, süslü bir salata koydu ama masa sallanıyordu. Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı. Salata kabı masanın kenarına kaymıştı ve düşmek üzereydi. Örümcek Adam hemen uzandı ve kabı tuttu. Sonra masanın kısa ayağının altına düz bir taş koydu. Masa artık hiç sallanmıyordu. Az sonra Hulk geldi. "Bu salata senin için, Hulk!" dedi Örümcek Adam. "Ne güzel bir sürpriz!" dedi Hulk ve güldü. İkisi masaya oturup salatayı birlikte yedi. Örümcek Adam çok mutluydu, çünkü salata yere düşmedi ve Hulk çok sevindi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 3: «Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve soyut 'sorun olduğunu anladı' 3 yaşındaki çocuk için somut değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir sorun olduğunu anladı"
   - Cümle 3: «Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Sorun' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0149` birebir aynı, ardından `@onarim: 3feefa7acfacce93fa16bbf0dd6261aff81fc86e`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0150 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0150
- yer: ev (Takımın gizli evi.)
- tema: sırayla oynamak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'yaprak', fiil 'eklemek', sıfat 'rahat'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: ikisi aynı anda küp koyunca kule sallandı | kuleyi tuttu ve sırayla oynamayı önerdi
@tohum: orumcek_adam-0150
@degisim: yaprak -> küp
Örümcek Adam ile Spin gizli evde tahta küplerle kule yapıyordu. İkisi de aynı anda bir küp eklemek istedi. Elleri çarpıştı ve kule sallanmaya başladı. Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı. Elini hemen çekti ve kuleyi iki yandan tuttu. Kule yıkılmadı. "Sırayla koyalım, Spin," dedi Örümcek Adam. "Olur, önce sen koy," dedi Spin. Örümcek Adam kırmızı bir küpü yavaşça kulenin üstüne koydu. Sonra Spin mavi bir küp ekledi. Kule yavaş yavaş yükseldi ve ikisi de artık çok rahattı. Örümcek Adam çok sevindi, çünkü sırayla oynayınca kuleleri yıkılmamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 4: «Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'örümcek hissi' ve 'sorun olduğunu anladı' küçük çocuk için soyut ifade.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 4: «Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: Kule zaten gözle görülür biçimde sallanırken örümcek hissinin sorunu haber vermesi işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0150` birebir aynı, `@degisim: yaprak -> küp` (tutuyorsan), ardından `@onarim: 6d46c7b5713ca6bab71a5da85d84b4a2a8202942`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0151 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0151
- yer: ev (Takımın gizli evi.)
- tema: yağmur ya da kar günü
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'yosun', fiil 'görüşmek', sıfat 'farklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: rüzgar yüksek pencereyi açtı ve yağmur yastıkları ıslattı | pencereye ağ atıp çekti ve pencereyi kapattı
@tohum: orumcek_adam-0151
@degisim: yosun -> yastık
Gizli evde yağmurlu bir sabahtı. Hulk, Örümcek Adam'a "Görüşürüz!" deyip gidecekti ama dışarıda çok yağmur vardı. Bu yüzden iki arkadaş farklı renkli yastıklarla yerde bir kale yaptı. Ama rüzgar yukarıdaki küçük pencereyi açtı ve yağmur içeri girip kaleyi ıslattı. "Kalemiz ıslanıyor!" dedi Hulk. Pencere tavanın yanındaydı ve Hulk'tan bile yüksekti. Örümcek Adam pencereye hemen bir ağ attı ve sıkıca çekti. Pencere kapandı. Hulk ıslak yastıkları kenara koydu. İki arkadaş kaleyi kuru yastıklarla yeniden kurdu. Sonra kalenin içine oturup yağmurun sesini dinlediler. Örümcek Adam ile Hulk çok sevindi, çünkü yağmur artık kalelerine giremiyordu.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "rüzgar yukarıdaki küçük pencereyi açtı"
   - Cümle 4: «Ama rüzgar yukarıdaki küçük pencereyi açtı ve yağmur içeri girip kaleyi ıslattı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede ortaya çıkıyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0151` birebir aynı, `@degisim: yosun -> yastık` (tutuyorsan), ardından `@onarim: 5c84065a1976ece7bbb996f967c5bd1f02e9be9e`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0152 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0152
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'pantolon', fiil 'erimek', sıfat 'düz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar heykelin pantolonunu geminin direğine uçurdu | ağını atıp pantolonu çekti ve kuma gömdü
@tohum: orumcek_adam-0152
@degisim: erimek -> giydirmek
Rüzgar kumsalda hızlı hızlı esiyordu. Örümcek Adam ile Ghost-Spider düz kumda komik bir heykel yapmıştı. Arkadaşı heykele eski bir pantolon giydirdi ama rüzgar pantolonu uçurdu. Pantolon limanda bir geminin direğine takıldı. "Pantolonu geri alalım!" dedi arkadaşı gülerek. Örümcek Adam ağını direğe doğru attı. Ağ pantolonu yakaladı. Örümcek Adam ağı yavaşça çekti ve pantolon eline geldi. Sonra pantolonu yeniden heykele giydirdi. Bu kez ucunu kuma iyice gömdü. "Artık rüzgar onu alamaz," dedi Örümcek Adam. "Teşekkürler, Örümcek Adam, heykel yine çok komik oldu!" dedi arkadaşı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşı heykele eski bir pantolon"
   - Cümle 3: «Arkadaşı heykele eski bir pantolon giydirdi ama rüzgar pantolonu uçurdu.»
   - Açıklama: 'Arkadaşı' sözünün Ghost-Spider'ı mı başka birini mi gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pantolon limanda bir geminin direğine takıldı"
   - Cümle 4: «Pantolon limanda bir geminin direğine takıldı.»
   - Açıklama: Kumsaldaki sahnede limandaki gemi ve direği sebepsizce beliriyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bu kez ucunu kuma iyice gömdü"
   - Cümle 10: «Bu kez ucunu kuma iyice gömdü.»
   - Açıklama: Çözüm ağ atma, çekme, yeniden giydirme ve kuma gömme olarak ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0152` birebir aynı, `@degisim: erimek -> giydirmek` (tutuyorsan), ardından `@onarim: 98d1cb00d01bbb2a3531ee0ca099918e10d84443`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0153 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0153
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'şişe', fiil 'dayamak', sıfat 'eksik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: büyük bir dalga sürpriz sofraya doğru geliyordu | sofrayı hemen kuru kuma taşıdı
@tohum: orumcek_adam-0153
Dalgalar kumsala gürültüyle vuruyordu. Örümcek Adam, Spin gelmeden kumsalda sürpriz bir sofra kuruyordu. Birden örümcek hissi, büyük bir dalganın sofraya geldiğini haber verdi. Örümcek Adam hemen örtünün dört ucunu topladı. Keki, sepeti ve meyve suyu şişesini örtüyle birlikte kaldırdı. Hepsini sudan uzak, kuru kuma taşıdı. Dalga geldi ama yalnız boş kumu ıslattı. Örümcek Adam örtüyü yeniden serdi. Şişeyi düşmesin diye sepete dayadı. Sofraya baktı, hiçbir şey eksik değildi. Sonra Spin geldi. "Bu sürpriz benim için mi?" diye sordu Spin. "Evet, iyi ki doğdun, Spin!" dedi Örümcek Adam. Örümcek Adam ile Spin kuru kumda oturup keki mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi, büyük bir dalganın sofraya geldiğini haber verdi"
   - Cümle 3: «Birden örümcek hissi, büyük bir dalganın sofraya geldiğini haber verdi.»
   - Açıklama: Bir hissin haber vermesi soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi, büyük"
   - Cümle 3: «Birden örümcek hissi, büyük bir dalganın sofraya geldiğini haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0153` birebir aynı, ardından `@onarim: 8607b584193cbb662038f52d22019804b221acc4`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0154 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0154
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'terazi', fiil 'şakalaşmak', sıfat 'rüzgarlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: arkadaşının kovası kayboldu ve taşlardan garip bir ses geldi | sesin geldiği yere gidip kovayı buldu
@tohum: orumcek_adam-0154
@degisim: terazi -> kova
Rüzgarlı bir sabah Örümcek Adam ile Hulk kumsalda şakalaşıyordu. Birden Hulk kırmızı kovasını bulamadı. Tam o sırada taşların arasından garip bir tık tık sesi geldi. Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı. Sesin geldiği yere hemen yürüdü. Hulk da peşinden gitti. Taşların arasında kırmızı kova vardı. Rüzgar kovayı taşlara çarpıyordu ve tık tık sesi buradan geliyordu. Örümcek Adam kovayı aldı ve Hulk'a verdi. Hulk kovasını tuttu ve kocaman gülümsedi. "Teşekkürler, Örümcek Adam, sesi de kovamı da buldun!" dedi Hulk.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "arkadaşının kovası kayboldu ve taşlardan garip bir ses geldi"
   - Cümle 0 (plan satırı): «arkadaşının kovası kayboldu ve taşlardan garip bir ses geldi | sesin geldiği yere gidip kovayı buldu»
   - Açıklama: Plan ve kapanış kaybolan kova ile garip sesi iki ayrı sorun gibi sunuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 4: «Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'bir sorun olduğunu anladı' soyut anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0154` birebir aynı, `@degisim: terazi -> kova` (tutuyorsan), ardından `@onarim: 2ad0aa4b0b3c29719dba58a7c3316175a4efce0e`, sonra gövde.
