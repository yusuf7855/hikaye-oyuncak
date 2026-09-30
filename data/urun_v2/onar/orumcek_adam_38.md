# Editör görevi (onarım): Örümcek Adam, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0120 (deneme 3 -> 4)

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
@degisim: gizemli -> parlak
Kıyıda dalgaların sesi duyuluyordu. Örümcek Adam ile Spin, kuma çizdikleri ayçiçeğinin ortasına bir süs arıyordu. Suyun içinde parlak bir şey gördüler ama o şey kıyıdan uzaktaydı. "Bu ne olabilir, Örümcek Adam?" diye sordu Spin. Örümcek Adam kıyıda durdu ve ağ attı. Ağ parlak şeye yapıştı ve Örümcek Adam onu kıyıya çekti. Parlak şey, içi pembe büyük bir deniz kabuğu çıktı. "Ne güzel bir kabuk!" dedi Spin. Örümcek Adam kabuğu ayçiçeğinin ortasına koydu ve resim daha da güzelleşti. Örümcek Adam bundan sonra Spin'in resimlerine hep bir kabuk getirdi.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Örümcek Adam bundan sonra Spin'in resimlerine hep bir kabuk getirdi"
   - Cümle 10: «Örümcek Adam bundan sonra Spin'in resimlerine hep bir kabuk getirdi.»
   - Açıklama: Son cümle olaydan çıkan bir ders değil, sahnenin dışına taşan bir zaman atlaması.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Örümcek Adam bundan sonra Spin'in resimlerine hep bir kabuk getirdi"
   - Cümle 10: «Örümcek Adam bundan sonra Spin'in resimlerine hep bir kabuk getirdi.»
   - Açıklama: Son cümle olaydan çıkan bir ders ya da sıcak kapanış değil, sahne dışına taşan keyfi bir alışkanlık bildiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0120` birebir aynı, `@degisim: gizemli -> parlak` (tutuyorsan), ardından `@onarim: b83be04c9485dc474ab368e92ed381b651caddd5`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0121 (deneme 3 -> 4)

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
@plan: uçurtmanın ipi iyi bağlı değildi | ipi çözdü ve sıkıca yeniden bağladı
@tohum: orumcek_adam-0121
Rüzgar sessiz kumsalda esiyordu. Örümcek Adam ilk uçurtmasını yeni bitirmişti. Ama örümcek hissi başını gıdıkladı, çünkü ip iyi bağlı değildi. İp böyle kalırsa uçurtma uçup gidebilirdi. Örümcek Adam ipi çözdü. Sonra onu sıkı sıkı yeniden bağladı. Uçurtmayı başının üstüne kaldırdı ve koştu. Rüzgar uçurtmayı yavaş yavaş yukarı taşıdı. Uçurtma limanın üstüne çıktı. Düğüm sağlam kaldı. Kırmızı uçurtma uzun süre mavi gökyüzünde uçtu. Örümcek Adam çok sevindi, çünkü kendi yaptığı ilk uçurtma havalandı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi başını gıdıkladı"
   - Cümle 3: «Ama örümcek hissi başını gıdıkladı, çünkü ip iyi bağlı değildi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve başı gıdıklaması mecaz, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi başını gıdıkladı' mecazlı ve soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0121` birebir aynı, ardından `@onarim: 8ec3eee623ce80f27b35e3c32362b1cd0afa44d9`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0124 (deneme 3 -> 4)

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
Kumsalda hafif bir rüzgar esiyordu. Örümcek Adam gemi oyunu oynuyordu ve hazine olarak kabuk topluyordu. Ama eski sepetin altı delikti ve kabuklar tek tek kuma düşüyordu. Örümcek Adam bunu görmemişti ama örümcek hissi başını gıdıkladı. Arkasına baktı ve kumdaki kabukları gördü. Sonra kıyıya yaklaştı ve büyük, düz bir kabuk buldu. Düz kabuğu sepetin içine, deliğin üstüne koydu. Düşen kabukları da yeniden topladı. Bu kez hiçbir kabuk düşmedi. Sepet kısa sürede parlak kabuklarla doldu. Örümcek Adam bundan sonra sepetin altına hep baktı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi başını gıdıkladı"
   - Cümle 4: «Örümcek Adam bunu görmemişti ama örümcek hissi başını gıdıkladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve başı gıdıklaması mecaz.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve başını gıdıklaması mecaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0124` birebir aynı, ardından `@onarim: 3b9f849d103c0546623799d27304d44531155dfc`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0125 (deneme 3 -> 4)

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
@plan: gizli ev soğuktu ve evde tek battaniye vardı | duvara tırmanıp battaniyeyi arkadaşıyla paylaştı
@tohum: orumcek_adam-0125
Bir sabah gizli evde hava çok soğuktu. Pencerede ince bir buz vardı ve Örümcek Adam tüylü bir battaniyenin altındaydı. Ghost-Spider da ısınmak istiyordu ama evde başka battaniye yoktu. O sırada kostümüyle havada süzülerek oynuyordu. Örümcek Adam battaniyeyi aldı ve duvara tırmanarak arkadaşının yanına çıktı. "Gel, bu battaniye ikimiz için de büyük," dedi Örümcek Adam. Battaniyenin bir ucunu arkadaşına verdi. İkisi yavaşça aşağı indi ve yan yana oturdu. Sonra ikisi de battaniyenin altına girdi. "Çok sıcak, teşekkür ederim!" dedi arkadaşı. Örümcek Adam çok mutlu oldu, çünkü battaniyeyi arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O sırada kostümüyle havada"
   - Cümle 4: «O sırada kostümüyle havada süzülerek oynuyordu.»
   - Açıklama: 'O' zamirinin Örümcek Adam'ı mı Ghost-Spider'ı mı gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada kostümüyle havada süzülerek oynuyordu"
   - Cümle 4: «O sırada kostümüyle havada süzülerek oynuyordu.»
   - Açıklama: Üşüyen Ghost-Spider'ın havada süzülüp oynaması yalnız duvara tırmanmayı zorla getirmek için sebepsizce kuruluyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kostümüyle havada süzülerek oynuyordu"
   - Cümle 4: «O sırada kostümüyle havada süzülerek oynuyordu.»
   - Açıklama: Üşüyen arkadaşın havada süzülmesi sebepsiz beliriyor ve yalnız duvara tırmanmayı zorla getirmek için kurulmuş.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "duvara tırmanarak arkadaşının yanına çıktı"
   - Cümle 5: «Örümcek Adam battaniyeyi aldı ve duvara tırmanarak arkadaşının yanına çıktı.»
   - Açıklama: Güvenli özellik kullanımı satırı ev içi tırmanmayı dışlar; burada gizli evin içinde duvara tırmanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0125` birebir aynı, ardından `@onarim: 3aab8eab7763062a1e45aab7980576e6c94cdc82`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0126 (deneme 3 -> 4)

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
@degisim: oturtmak -> koymak
Rüzgar parktaki ağaçların yapraklarını sallıyordu. Örümcek Adam ile Hulk çimenlerde vanilyalı bir keki süslemek istiyordu. Hulk ağacın tepesinde altın sarısı bir elma gördü ama ona uzanamadı. "Ağacı sallamak istemiyorum, dallar kırılır," dedi Hulk. Örümcek Adam elmaya bir ağ attı. Ağ elmaya yapıştı ve Örümcek Adam ağı yavaşça çekti. Elma dalından koptu ve Örümcek Adam'ın eline düştü. Örümcek Adam elmayı kekin tam ortasına koydu. "Bu kek şimdi çok güzel oldu!" dedi Hulk ve güldü. Örümcek Adam çok sevindi, çünkü kek artık hazırdı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Örümcek Adam ağı yavaşça çekti"
   - Cümle 6: «Ağ elmaya yapıştı ve Örümcek Adam ağı yavaşça çekti.»
   - Açıklama: 5-8. cümlelerde 'Örümcek Adam' adı art arda gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0126` birebir aynı, `@degisim: oturtmak -> koymak` (tutuyorsan), ardından `@onarim: 46611b1d148aef29d1ef14bb8163a1bebd9aa080`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0128 (deneme 3 -> 4)

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
Örümcek Adam parkta bayrak oyunu oynuyordu. Ghost-Spider bayrağı kaptı ve havada süzülerek kaçtı. Ama rüzgar bayrağı elinden aldı ve fıskiyenin havuzuna düşürdü. Bayrak suyun tam ortasında yavaş yavaş yüzüyordu ve kenara gelmiyordu. Örümcek Adam havuzun kenarında bir an düşünceli durdu. Sonra ağ attı ve bayrağı sudan çekti. İkisi bayrağı güneşte biraz salladı ve kuruttu. Sonra ikisi oyuna hemen yeniden başladı ve bayrağı sırayla kaptı. Örümcek Adam çok sevindi, çünkü bayraklarını sudan geri almıştı.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "fıskiyenin havuzuna düşürdü"
   - Cümle 3: «Ama rüzgar bayrağı elinden aldı ve fıskiyenin havuzuna düşürdü.»
   - Açıklama: Kartın park tarifi oyun alanı, ağaçlar ve çiçek bahçesi sayıyor; fıskiye havuzu tarifte yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0128` birebir aynı, ardından `@onarim: 582be167a482d7523ed74f68f913d3d7f6bc756f`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0129 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: yukarıdan garip bir ses geldi | sesi buldu ve saksıyı hemen kenara çekti
@tohum: orumcek_adam-0129
Gizli evde her yer sessizdi. Örümcek Adam en sevdiği çiçeği boyalı bir saksıda suluyordu. Birden yukarıdan garip bir ses geldi. Örümcek Adam bu sesi çok merak etti ve başını kaldırdı. Duvarda, saksının tam üstünde toplarla dolu bir file asılıydı. File eski bir ipe bağlıydı ve ses bu ipten geliyordu. Örümcek Adam örümcek hissiyle file ile topların çiçeğe düşeceğini anladı. Saksıyı hemen kenara çekti. Az sonra ip koptu ve file yere düştü. Toplar yuvarlandı ama çiçeğe hiçbir şey olmadı. Örümcek Adam topları tek tek fileye koydu. Sonra çiçeğini sulamaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Birden yukarıdan garip bir ses geldi"
   - Cümle 3: «Birden yukarıdan garip bir ses geldi.»
   - Açıklama: İlk üç cümlede yalnız bir ses var; asıl sorun olan filenin çiçeğe düşme tehlikesi ancak 7. cümlede ortaya çıkıyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yukarıdan garip bir ses geldi"
   - Cümle 3: «Birden yukarıdan garip bir ses geldi.»
   - Açıklama: Plan sorunu yalnız garip bir ses olarak söylüyor; gövdedeki asıl sorun filenin çiçeğin üstüne düşecek olması.
   - Açıklama: Plan sorunu yalnız bir ses olarak veriyor; gövdedeki asıl sorun filenin saksının üstüne düşecek olması.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam örümcek hissiyle"
   - Cümle 7: «Örümcek Adam örümcek hissiyle file ile topların çiçeğe düşeceğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "file ile topların çiçeğe düşeceğini anladı"
   - Cümle 7: «Örümcek Adam örümcek hissiyle file ile topların çiçeğe düşeceğini anladı.»
   - Açıklama: Asıl sorun olan filenin çiçeğe düşme tehlikesi ilk üç cümlede değil ancak yedinci cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0129` birebir aynı, ardından `@onarim: ab5f9ac0c83077748ae5137c2465a449247ff0c6`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0130 (deneme 3 -> 4)

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
@plan: yerdeki sabunlu sünger çok kaygandı | arkadaşını durdurdu ve süngeri kovaya koydu
@tohum: orumcek_adam-0130
@degisim: çalıştırmak -> yıkamak
Bir sabah Örümcek Adam ile Spin limanda kovayla oyuncak bir tekne yıkıyordu. Örümcek Adam kovayı taşımak için sabunlu süngeri yere bıraktı. Sünger çok kaygandı ve tekneyi taşıyan Spin geri geri yürüyordu. Birden Örümcek Adam örümcek hissiyle Spin'in yerdeki süngeri görmediğini anladı. "Dur, Spin, yerde kaygan bir sünger var!" dedi Örümcek Adam. Spin hemen durdu. Örümcek Adam süngeri yerden aldı ve kovaya koydu. "Özür dilerim, Spin, süngeri yere ben bıraktım," dedi Örümcek Adam. "Sorun değil, teşekkürler," dedi Spin. Sonra ikisi tekneyi yıkamaya devam etti. Örümcek Adam bundan sonra süngeri hep kovanın içine koydu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle Spin'in yerdeki"
   - Cümle 4: «Birden Örümcek Adam örümcek hissiyle Spin'in yerdeki süngeri görmediğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0130` birebir aynı, `@degisim: çalıştırmak -> yıkamak` (tutuyorsan), ardından `@onarim: 56fa6f243a7335173d6f6f163da423c7a3227c0f`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0138 (deneme 3 -> 4)

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
Örümcek Adam ile Hulk kumsalda yumuşak bir topla oynuyordu. Kumun üstünde küçük bir pota vardı. Hulk topu potaya attı ama top içeri girmedi. "Top neden içeri girmedi?" diye sordu Hulk. Örümcek Adam örümcek hissiyle çemberin eğri olduğunu anladı. Potaya gitti ve çembere dikkatle baktı. "Çember aşağı eğilmiş, Hulk!" dedi Örümcek Adam. Hulk direği sıkıca tuttu. Örümcek Adam çemberi iki eliyle yukarı itti ve düzeltti. Hulk topu yine attı. Top bu kez içeri girdi. Sonra ikisi mutlu mutlu top oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissiyle çemberin eğri olduğunu anladı"
   - Cümle 5: «Örümcek Adam örümcek hissiyle çemberin eğri olduğunu anladı.»
   - Açıklama: Kartın özellikler alanında örümcek hissi yalnız bir sorun olduğunu haber verir; burada zaten bilinen sorunun nedenini teşhis eden bir araç olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0138` birebir aynı, ardından `@onarim: 97745f250f4a7b981159ab5adcfc013c95a0f88d`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0140 (deneme 3 -> 4)

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
@plan: bir dalga kağıt şapkaya doğru geliyordu | dalgayı önceden fark etti ve sudan uzağa koştu
@tohum: orumcek_adam-0140
@degisim: seslenmek -> katlamak
Bir sabah Örümcek Adam su kenarında gemi oyunu oynuyordu. Temiz bir kağıttan bir şapka katladı ve başına taktı. Ama dalgalar kuma kadar geliyordu ve kağıt şapka suda bozulurdu. Birden örümcek hissiyle küçük bir dalganın arkasından geldiğini anladı. Hemen arkasına döndü ve dalgayı gördü. Şapkasını eliyle tuttu ve sudan uzağa koştu. Dalga onun az önce durduğu yere kadar geldi. Kağıt şapka hiç ıslanmadı. Örümcek Adam kumsalın kuru bir yerine oturdu. Sonra kağıt şapkasıyla gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "küçük bir dalganın arkasından geldiğini"
   - Cümle 4: «Birden örümcek hissiyle küçük bir dalganın arkasından geldiğini anladı.»
   - Açıklama: Cümlede gelen şeyin öznesi eksik; 'küçük bir dalganın arkadan geldiğini' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle"
   - Cümle 4: «Birden örümcek hissiyle küçük bir dalganın arkasından geldiğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir söz değil.
   - Açıklama: 'Örümcek hissi' soyut ve çocuğun bilmediği bir kavramdır.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "küçük bir dalganın arkasından geldiğini"
   - Cümle 4: «Birden örümcek hissiyle küçük bir dalganın arkasından geldiğini anladı.»
   - Açıklama: 'Arkasından' kimin arkasını gösterdiği belirsiz; dalganın arkasından bir şey geliyormuş gibi okunuyor.
4. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sudan uzağa koştu"
   - Cümle 6: «Şapkasını eliyle tuttu ve sudan uzağa koştu.»
   - Açıklama: Planda sudan uzağa koştuğu yazıyor ama gövdede koşma eylemi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0140` birebir aynı, `@degisim: seslenmek -> katlamak` (tutuyorsan), ardından `@onarim: e8008a6fd20447ab5ba19d2c3cadd1e7f1028881`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0141 (deneme 2 -> 3)

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
@plan: arkadaşı bitmemiş sürprizin yanından geçecekti | kalbin üstüne yaprak serpti ve sürprizi sakladı
@tohum: orumcek_adam-0141
Örümcek Adam sisli bir sabah parkta Spin için kozalaklarla bir kalp diziyordu. Birden örümcek hissiyle Spin'in bu yoldan geçeceğini anladı. Ama kalp daha bitmemişti. Örümcek Adam, Spin'in onu görmesini istemiyordu. Örümcek Adam ağacın altındaki kuru yaprakları hemen kalbin üstüne serpti. Spin yoldan geçti, yerde yalnız yaprak gördü ve yürümeye devam etti. Örümcek Adam yaprakları kaldırdı ve son kozalakları da dikkatle dizdi. Sonra Spin'in yanına koştu, elini tuttu ve onu kalbin yanına getirdi. Spin kalbi görünce çok şaşırdı ve güldü. Örümcek Adam çok mutluydu, çünkü sürprizini Spin görmeden bitirmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle Spin'in"
   - Cümle 2: «Birden örümcek hissiyle Spin'in bu yoldan geçeceğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Örümcek hissi' 3 yaşındaki çocuğun anlamayacağı soyut bir kavram.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissiyle Spin'in bu yoldan geçeceğini anladı"
   - Cümle 2: «Birden örümcek hissiyle Spin'in bu yoldan geçeceğini anladı.»
   - Açıklama: Karttaki özellik örümcek hissinin bir sorunu haber vermesidir; burada bir arkadaşın nereden geçeceğini önceden bildiren bir sezgi gibi kullanılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Spin'in onu görmesini istemiyordu"
   - Cümle 4: «Örümcek Adam, Spin'in onu görmesini istemiyordu.»
   - Açıklama: 'Onu' zamirinin kalbi mi Örümcek Adam'ı mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0141` birebir aynı, ardından `@onarim: a41be8a161cc27097ee825cc11805c0d50544729`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0142 (deneme 2 -> 3)

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
Parkın oyun alanında güneş parlıyordu. Örümcek Adam orada top oynuyordu. Ghost-Spider topu çok yükseğe attı ve top bir duvarın arkasına düştü. Duvar çok yüksekti ve top hiç görünmüyordu. Örümcek Adam'ın arkadaşı çok üzüldü. "Üzülme, hemen bakarım," dedi Örümcek Adam. Duvara hızla tırmandı ve tepesine çıktı. Oradan kırmızı topu gördü. Top duvarın hemen yanındaki bir çalıya takılmıştı. Örümcek Adam duvarın öbür yanına indi ve topu çalıdan aldı. Sonra duvarın yanından dolaşıp geri geldi ve topu arkadaşına verdi. İki sadık arkadaş çok sevindi, çünkü kırmızı topu geri almışlardı.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Örümcek Adam'ın arkadaşı çok üzüldü"
   - Cümle 5: «Örümcek Adam'ın arkadaşı çok üzüldü.»
   - Açıklama: Adıyla geçen Ghost-Spider'a sonra 'arkadaşı' deniyor; kimin kastedildiği açıkça bağlanmıyor.
   - Açıklama: Ghost-Spider adıyla girdikten sonra 'arkadaşı' diye yeniden tanıtılıyor; aynı kişi mi yoksa üçüncü biri mi olduğu belli değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Duvara hızla tırmandı ve tepesine çıktı"
   - Cümle 7: «Duvara hızla tırmandı ve tepesine çıktı.»
   - Açıklama: Çok yüksek duvara tırmanıp öbür yanına inme süper güç olarak çerçevelenmeden, çocuğun taklit edebileceği biçimde anlatılıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Örümcek Adam duvarın öbür yanına indi ve topu çalıdan aldı"
   - Cümle 10: «Örümcek Adam duvarın öbür yanına indi ve topu çalıdan aldı.»
   - Açıklama: Çözüm tırmanma, bakma, inme, topu alma ve dolaşıp dönme gibi ikiden çok adım sürüyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra duvarın yanından dolaşıp geri geldi"
   - Cümle 11: «Sonra duvarın yanından dolaşıp geri geldi ve topu arkadaşına verdi.»
   - Açıklama: Duvarın yanından dolaşılabiliyorsa yüksek duvara tırmanma gereği ortadan kalkıyor ve kurulan engelle çelişiyor.
   - Açıklama: Duvarın yanından dolaşılabiliyorsa topa ulaşmak için tırmanmaya gerek yoktu; yüksek duvar engeli kendisiyle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0142` birebir aynı, `@degisim: gömlek -> top` (tutuyorsan), ardından `@onarim: 56fb12abe3c87c0f83e97946f939013ba2273aa1`, sonra gövde.
