# Editör görevi (onarım): Örümcek Adam, onarım partisi 43

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar43.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar43.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0121 (deneme 4 -> 5)

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
Rüzgar sessiz kumsalda esiyordu. Örümcek Adam ilk uçurtmasını yeni bitirmişti. Ama örümcek hissi ona bir sorun olduğunu haber verdi. Uçurtmanın ipi iyi bağlı değildi. İp böyle kalırsa uçurtma uçup gidebilirdi. Örümcek Adam ipi çözdü. Sonra onu sıkı sıkı yeniden bağladı. Uçurtmayı başının üstüne kaldırdı ve koştu. Rüzgar uçurtmayı yavaş yavaş yukarı taşıdı. Uçurtma limanın üstüne çıktı. Düğüm sağlam kaldı. Kırmızı uçurtma uzun süre mavi gökyüzünde uçtu. Örümcek Adam çok sevindi, çünkü kendi yaptığı ilk uçurtma havalandı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissinin haber vermesi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede yalnız bir sorun olduğu söyleniyor, sorunun ne olduğu ancak dördüncü cümlede açıklanıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Uçurtmanın ipi iyi bağlı değildi"
   - Cümle 4: «Uçurtmanın ipi iyi bağlı değildi.»
   - Açıklama: İpin neden kötü bağlandığı söylenmiyor ve sorun yalnız olası bir tehlike olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0121` birebir aynı, ardından `@onarim: d49045bd7309dcd06014a047007bb1c21d0c7c6d`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0124 (deneme 4 -> 5)

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
Kumsalda hafif bir rüzgar esiyordu. Örümcek Adam gemi oyunu oynuyordu ve hazine olarak kabuk topluyordu. Ama eski sepetin altı delikti ve kabuklar tek tek kuma düşüyordu. Örümcek Adam bunu görmemişti ama örümcek hissi ona haber verdi. Arkasına baktı ve kumdaki kabukları gördü. Sonra kıyıya yaklaştı ve büyük, düz bir kabuk buldu. Düz kabuğu sepetin içine, deliğin üstüne koydu. Düşen kabukları da yeniden topladı. Bu kez hiçbir kabuk düşmedi. Sepet kısa sürede parlak kabuklarla doldu. Örümcek Adam bundan sonra sepetin altına hep baktı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona haber verdi"
   - Cümle 4: «Örümcek Adam bunu görmemişti ama örümcek hissi ona haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğa anlaşılır değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0124` birebir aynı, ardından `@onarim: 1b122a8da49555494572b8911a74aed8ed913b1c`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0125 (deneme 4 -> 5)

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
Bir sabah gizli evde hava çok soğuktu. Pencerede ince bir buz vardı ve Örümcek Adam tüylü bir battaniyenin altındaydı. Ghost-Spider evin çatısında şehre bakıyordu ve ısınmak istiyordu. Ama evde başka battaniye yoktu. Örümcek Adam battaniyeyi aldı ve süper gücüyle dış duvardan çatıya tırmandı. "Al, bu battaniye ikimiz için de büyük," dedi Örümcek Adam. Battaniyenin bir ucunu arkadaşına verdi. İkisi yan yana oturdu ve battaniyenin altına girdi. "Çok sıcak, teşekkür ederim!" dedi arkadaşı. Örümcek Adam çok mutlu oldu, çünkü battaniyeyi arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ghost-Spider evin çatısında şehre bakıyordu"
   - Cümle 3: «Ghost-Spider evin çatısında şehre bakıyordu ve ısınmak istiyordu.»
   - Açıklama: Çatıda oturmak çocuğun taklit edebileceği yüksek yer davranışıdır; sonunda ikisi de çatıda oturuyor.
   - Açıklama: Çatıda oturmak çocuğun taklit edebileceği yüksek yerde durma davranışı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "evin çatısında şehre bakıyordu ve ısınmak istiyordu"
   - Cümle 3: «Ghost-Spider evin çatısında şehre bakıyordu ve ısınmak istiyordu.»
   - Açıklama: Ghost-Spider'ın soğuk sabahta içeri girmek yerine çatıda üşümesinin sebebi söylenmiyor ve akla yatkın değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ghost-Spider evin çatısında şehre bakıyordu ve ısınmak istiyordu"
   - Cümle 3: «Ghost-Spider evin çatısında şehre bakıyordu ve ısınmak istiyordu.»
   - Açıklama: Ghost-Spider'ın soğukta sebepsizce çatıda oturması sorunu akla yatkın kılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "süper gücüyle dış duvardan çatıya tırmandı"
   - Cümle 5: «Örümcek Adam battaniyeyi aldı ve süper gücüyle dış duvardan çatıya tırmandı.»
   - Açıklama: Battaniyeyi götürmek için dış duvara tırmanmak sebepsiz ve olayın gerektirmediği bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0125` birebir aynı, ardından `@onarim: 870baa1d421815079b3da89732abb0e5ba1680b8`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0126 (deneme 4 -> 5)

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
Rüzgar parktaki ağaçların yapraklarını sallıyordu. Örümcek Adam ile Hulk çimenlerde vanilyalı bir keki süslemek istiyordu. Hulk ağacın tepesinde altın sarısı bir elma gördü ama ona uzanamadı. "Ağacı sallamak istemiyorum, dallar kırılır," dedi Hulk. Örümcek Adam elmaya bir ağ attı ve yavaşça çekti. Elma dalından koptu ve Örümcek Adam'ın eline düştü. Sonra elmayı kekin tam ortasına koydu. "Bu kek şimdi çok güzel oldu!" dedi Hulk ve güldü. Örümcek Adam çok sevindi, çünkü kek artık hazırdı.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra elmayı kekin tam ortasına koydu"
   - Cümle 7: «Sonra elmayı kekin tam ortasına koydu.»
   - Açıklama: Önceki cümlenin öznesi elma olduğu için elmayı kimin koyduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0126` birebir aynı, `@degisim: oturtmak -> koymak` (tutuyorsan), ardından `@onarim: 877da30e73c57e48bdf9850306853bd5f9dc8ecd`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0128 (deneme 4 -> 5)

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
@plan: rüzgar esti ve bayrak yüksek bir dala takıldı | ağ atıp bayrağı daldan çekti
@tohum: orumcek_adam-0128
@degisim: kurutmak -> sallamak
Örümcek Adam parkta bayrak oyunu oynuyordu. Ghost-Spider bayrağı kaptı ve koşarak kaçtı. Ama rüzgar esti ve bayrak yüksek bir ağacın dalına takıldı. Dal çok yüksekti ve bayrak aşağı düşmüyordu. Örümcek Adam ağacın altında bir an düşünceli durdu. Sonra ağ attı ve bayrağı daldan çekti. Arkadaşı bayrağı iki eliyle aldı ve sevinçle havada salladı. Sonra ikisi oyuna hemen yeniden başladı ve bayrağı sırayla kaptı. Örümcek Adam çok sevindi, çünkü bayraklarını daldan geri almıştı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama rüzgar esti ve bayrak yüksek bir ağacın dalına takıldı"
   - Cümle 3: «Ama rüzgar esti ve bayrak yüksek bir ağacın dalına takıldı.»
   - Açıklama: Ghost-Spider'ın elinde koşarak taşıdığı bayrağın rüzgarla yüksek bir dala takılması akla yatkın bir sebep değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve bayrak yüksek bir ağacın dalına takıldı"
   - Cümle 3: «Ama rüzgar esti ve bayrak yüksek bir ağacın dalına takıldı.»
   - Açıklama: Bayrak Ghost-Spider'ın elindeyken rüzgarın onu yüksek dala takması akla yatkın değil.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Dal çok yüksekti"
   - Cümle 4: «Dal çok yüksekti ve bayrak aşağı düşmüyordu.»
   - Açıklama: Dalın yüksek olduğu bir önceki cümlede zaten söylendi; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0128` birebir aynı, `@degisim: kurutmak -> sallamak` (tutuyorsan), ardından `@onarim: ec5ebdb0296c35428487c2acd8a5c7c13f6b658b`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0129 (deneme 4 -> 5)

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
@plan: saksının üstünden gelen ses çiçek için bir sorundu | sesi yapan ipi buldu ve saksıyı kenara çekti
@tohum: orumcek_adam-0129
Gizli evde Örümcek Adam en sevdiği çiçeği boyalı bir saksıda suluyordu. Birden saksının tam üstünden garip bir ses geldi. Örümcek hissi ona çiçek için bir sorun olduğunu haber verdi. Örümcek Adam başını kaldırdı ve yukarı baktı. Duvarda toplarla dolu bir file asılıydı. File eski bir ipe bağlıydı ve ses bu ipten geliyordu. Saksıyı hemen kenara çekti. Az sonra ip koptu ve file yere düştü. Toplar yuvarlandı ama çiçeğe hiçbir şey olmadı. Örümcek Adam topları tek tek fileye koydu. Sonra çiçeğini sulamaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "saksının üstünden gelen ses çiçek için bir sorundu"
   - Cümle 0 (plan satırı): «saksının üstünden gelen ses çiçek için bir sorundu | sesi yapan ipi buldu ve saksıyı kenara çekti»
   - Açıklama: Plan asıl sorunu (eski ipin kopup filenin çiçeğin üstüne düşecek olması) söylemiyor, yalnız belirsiz bir sesten söz ediyor.
   - Açıklama: Sorun ses değil, eski ipe asılı filenin çiçeğin üstüne düşecek olması.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi ona çiçek için"
   - Cümle 3: «Örümcek hissi ona çiçek için bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber vermesi 3 yaşındaki çocuk için anlaşılmaz.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi ona çiçek için bir sorun olduğunu haber verdi"
   - Cümle 3: «Örümcek hissi ona çiçek için bir sorun olduğunu haber verdi.»
   - Açıklama: Soyut 'örümcek hissi' kişileştirilerek haber veren özne yapılmış; 3 yaşındaki çocuk için soyut ve mecazlı.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "çiçek için bir sorun olduğunu"
   - Cümle 3: «Örümcek hissi ona çiçek için bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede sorun yalnız belirsiz bir 'sorun' olarak geçiyor; filenin düşeceği ancak 6. cümlede anlaşılıyor.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Örümcek hissi ona çiçek için bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede yalnız belirsiz bir sorun hissi var; asıl sorun (düşecek file) ancak 6. cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0129` birebir aynı, ardından `@onarim: 4dd37a6853244ba1c08c30efb30ceecf6771f20c`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0130 (deneme 4 -> 5)

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
Bir sabah Örümcek Adam ile Spin limanda kovayla oyuncak bir tekne yıkıyordu. Örümcek Adam kovayı taşımak için sabunlu süngeri yere bıraktı. Sünger çok kaygandı ve tekneyi taşıyan Spin geri geri yürüyordu. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. "Dur, Spin, yerde kaygan bir sünger var!" dedi Örümcek Adam. Spin hemen durdu. Örümcek Adam süngeri yerden aldı ve kovaya koydu. "Özür dilerim, Spin, süngeri yere ben bıraktım," dedi Örümcek Adam. "Sorun değil, teşekkürler," dedi Spin. Sonra ikisi tekneyi yıkamaya devam etti. Örümcek Adam bundan sonra süngeri hep kovanın içine koydu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber vermesi 3 yaşındaki çocuğa uygun olmayan bir mecaz.
   - Açıklama: 'Örümcek hissi haber verdi' soyut bir kavram ve kişileştirme; küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0130` birebir aynı, `@degisim: çalıştırmak -> yıkamak` (tutuyorsan), ardından `@onarim: 7460a3433b71142969e2e272bc16bb27661b675c`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0138 (deneme 4 -> 5)

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
Örümcek Adam ile Hulk kumsalda yumuşak bir topla oynuyordu. Kumun üstünde küçük bir pota vardı. Hulk topu potaya attı ama top içeri girmedi. "Top neden içeri girmedi?" diye sordu Hulk. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Potaya gitti ve çembere dikkatle baktı. "Çember aşağı eğilmiş, Hulk!" dedi Örümcek Adam. Hulk direği sıkıca tuttu. Örümcek Adam çemberi iki eliyle yukarı itti ve düzeltti. Hulk topu yine attı. Top bu kez içeri girdi. Sonra ikisi mutlu mutlu top oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi Örümcek Adam'a"
   - Cümle 5: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi Örümcek"
   - Cümle 5: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve bir hissin haber vermesi 3 yaşındaki çocuk için soyut ve mecazlı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Potaya gitti ve çembere"
   - Cümle 6: «Potaya gitti ve çembere dikkatle baktı.»
   - Açıklama: Önceki cümlenin öznesi 'örümcek hissi' olduğundan potaya kimin gittiği dilbilgisel olarak belirsiz.
   - Açıklama: Önceki cümlenin öznesi 'örümcek hissi' olduğu için potaya kimin gittiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0138` birebir aynı, ardından `@onarim: ad8b599cc05bee535902fe096398f061203d3775`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0140 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: bir dalga kağıt şapkaya doğru geliyordu | dalgayı gördü ve hızla sudan uzağa koştu
@tohum: orumcek_adam-0140
@degisim: seslenmek -> katlamak
Bir sabah Örümcek Adam su kenarında gemi oyunu oynuyordu. Temiz bir kağıttan bir şapka katladı ve başına taktı. Ama dalgalar kuma kadar geliyordu ve kağıt şapka suda bozulurdu. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Hemen arkasına döndü ve arkadan gelen küçük bir dalgayı gördü. Şapkasını eliyle tuttu ve hızla sudan uzağa koştu. Dalga onun az önce durduğu yere kadar geldi. Kağıt şapka hiç ıslanmadı. Örümcek Adam kumsalın kuru bir yerine oturdu. Sonra kağıt şapkasıyla gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kağıt şapka suda bozulurdu"
   - Cümle 3: «Ama dalgalar kuma kadar geliyordu ve kağıt şapka suda bozulurdu.»
   - Açıklama: Sorun gerçekleşmeyen önemsiz bir tehlike; dalga geliyor, figür kaçıyor ve hikaye bitiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve hissin haber vermesi 3 yaşındaki çocuğa uygun olmayan bir mecaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0140` birebir aynı, `@degisim: seslenmek -> katlamak` (tutuyorsan), ardından `@onarim: 0c66de65c34e945bd96d316ea0959961da611938`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0141 (deneme 3 -> 4)

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
Örümcek Adam sisli bir sabah parkta Spin için kozalaklarla bir kalp diziyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Başını kaldırdı ve yoldan gelen Spin'i gördü. Ama kalp daha bitmemişti. Örümcek Adam, Spin'in kalbi görmesini istemiyordu. Ağacın altındaki kuru yaprakları hemen kalbin üstüne serpti. Spin yoldan geçti, yerde yalnız yaprak gördü ve yürümeye devam etti. Örümcek Adam yaprakları kaldırdı ve son kozalakları da dikkatle dizdi. Sonra Spin'in yanına koştu, elini tuttu ve onu kalbin yanına getirdi. Spin kalbi görünce çok şaşırdı ve güldü. Örümcek Adam çok mutluydu, çünkü sürprizini Spin görmeden bitirmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Bir hissin sorun olduğunu haber vermesi 3 yaşındaki çocuk için soyut bir kavram ve kişileştirme.
   - Açıklama: 'Örümcek hissinin haber vermesi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0141` birebir aynı, ardından `@onarim: 954b3ed33476ed206add80e89e6eefff706dd645`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0142 (deneme 3 -> 4)

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
@plan: top yüksek duvarın tepesine düştü ve görünmedi | duvara tırmanıp topu aldı ve arkadaşına verdi
@tohum: orumcek_adam-0142
@degisim: gömlek -> top
Parkın oyun alanında güneş parlıyordu. Örümcek Adam orada arkadaşıyla top oynuyordu. Ghost-Spider topu yükseğe attı ve top bir duvarın tepesine düştü. Duvar çok yüksekti ve top aşağıdan hiç görünmüyordu. Arkadaşı buna çok üzüldü. "Üzülme, hemen bakarım," dedi Örümcek Adam. Süper gücüyle duvara tırmandı ve tepesine çıktı. Oradan kırmızı topu gördü ve aldı. Sonra Örümcek Adam yavaşça aşağı indi ve topu arkadaşına verdi. İki sadık arkadaş çok sevindi, çünkü kırmızı topu geri almışlardı.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ghost-Spider topu yükseğe attı"
   - Cümle 3: «Ghost-Spider topu yükseğe attı ve top bir duvarın tepesine düştü.»
   - Açıklama: Ghost-Spider'ın az önce anılan arkadaş olduğu söylenmeden adı birden geçiyor, kim olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0142` birebir aynı, `@degisim: gömlek -> top` (tutuyorsan), ardından `@onarim: b14179574c58a3b46d9d83c0c531d2a8de3199e2`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0143 (deneme 3 -> 4)

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
Rüzgar hafif esiyordu. Örümcek Adam ilk kez bir duvarın yanındaki kuma kocaman bir resim çiziyordu. Ama resim çok büyüktü ve Örümcek Adam yerden bütün çizgileri göremiyordu. Hulk da elinde küçük bir torbayla onu izliyordu. Örümcek Adam süper gücüyle duvara tırmandı ve yukarıdan baktı. Kumdaki resim bir örümcekti ama bir bacağı eksikti. Hemen aşağı indi ve eksik bacağı da çizdi. Hulk torbasından iki deniz kabuğu çıkarıp ona verdi. Örümcek Adam kabukları örümceğin gözlerine koydu. Artık resim tamamdı. Hulk sevinçle alkışladı. Örümcek Adam çok sevindi, çünkü ilk kum resmini bitirmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hulk torbasından iki deniz kabuğu çıkarıp ona verdi"
   - Cümle 8: «Hulk torbasından iki deniz kabuğu çıkarıp ona verdi.»
   - Açıklama: Sorun eksik bacak çizilince çözülmüşken kabuklar sorundan çıkmayan ek bir adım olarak geliyor ve resmi ancak onlar tamamlıyor gibi gösteriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0143` birebir aynı, ardından `@onarim: acc0026cd1fcb98051f1bdff02348dbdd5162c86`, sonra gövde.
