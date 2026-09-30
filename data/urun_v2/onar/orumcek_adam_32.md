# Editör görevi (onarım): Örümcek Adam, onarım partisi 32

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar32.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0093 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0093
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: kaybolan eşya
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'bilye', fiil 'sunmak', sıfat 'yavaş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: mavi bilye yokuştan yuvarlandı ve kayboldu | bankın altına bakıp bilyeyi buldu
@tohum: orumcek_adam-0093
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin parkın oyun alanında bilye oynuyordu. Birden Spin'in mavi bilyesi yokuştan aşağı yuvarlandı ve kayboldu. "Bilyemi bulamıyorum, Örümcek Adam," dedi Spin üzgün bir sesle. Örümcek Adam yavaş yavaş aşağı yürüdü. Bir bankın yanına gelince örümcek hissi onu durdurdu. Örümcek Adam hemen eğildi ve bankın altına baktı. Mavi bilye kuru yaprakların arasında duruyordu. Örümcek Adam onu aldı ve iki eliyle Spin'e sundu. "İşte bilyen, Spin," dedi Örümcek Adam. Spin sevinçle bilyesini tuttu. İki arkadaş oyun alanına döndü ve bilye oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi onu durdurdu"
   - Cümle 6: «Bir bankın yanına gelince örümcek hissi onu durdurdu.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0093` birebir aynı, ardından `@onarim: 7ed618707b77d3707fe779dbf5a66af5895a91c0`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0096 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0096
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yeni bir şeyi denemek
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'cüzdan', fiil 'dinlemek', sıfat 'çiçekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: uzun çalılar bahçedeki çiçekleri kapatıyordu | duvara tırmanıp çiçeklere baktı ve resim çizdi
@tohum: orumcek_adam-0096
@degisim: cüzdan -> kalem
Parkın bahçesinde renkli çiçekler açmıştı. Örümcek Adam ilk kez onların resmini yapmayı denemek istiyordu. Ama önündeki uzun çalılar çiçeklerin çoğunu kapatıyordu. Spin ona kendi kağıdını ve kalemini verdi. "Önce iyice bak, sonra çiz," dedi Spin. Örümcek Adam onu dikkatle dinledi. Hemen süper gücüyle bahçenin yanındaki taş duvara tırmandı. Duvarın üstünden bütün bahçe görünüyordu. Kırmızı, sarı ve mor çiçeklere uzun uzun baktı. Sonra aşağı indi ve çiçekli bir resim çizdi. "Çok güzel olmuş, Örümcek Adam!" dedi Spin. Örümcek Adam çok sevindi, çünkü ilk resmini kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Spin ona kendi kağıdını ve kalemini verdi"
   - Cümle 4: «Spin ona kendi kağıdını ve kalemini verdi.»
   - Açıklama: Örümcek Adam'ın kağıdı olmadığı söylenmeden Spin'in kağıt vermesi sebepsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0096` birebir aynı, `@degisim: cüzdan -> kalem` (tutuyorsan), ardından `@onarim: 78af696201d9085bf17c6630a6431c7927566819`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0097 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0097
- yer: ev (Takımın gizli evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'pizza', fiil 'kirletmek', sıfat 'çekingen'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: uçurtma gizli evin çamurlu çatısına düştü | duvara tırmanıp uçurtmayı getirdi
@tohum: orumcek_adam-0097
@degisim: pizza -> uçurtma
Gizli evin önünde Hulk ile Örümcek Adam uçurtma uçuruyordu. Birden rüzgar durdu ve Hulk'ın uçurtması evin çatısına düştü. Çatıda yağmurdan kalan çamur vardı. "Çamur uçurtmamı kirletecek," dedi Hulk ve başını çekingen çekingen eğdi. Hulk çatıya çıkamazdı, çünkü çok ağırdı. "Ben getiririm, Hulk," dedi Örümcek Adam. Örümcek Adam süper gücüyle evin duvarına tırmandı. Uçurtma çamurun hemen yanına düşmüştü. Örümcek Adam uçurtmayı aldı, yavaşça aşağı indi ve Hulk'a verdi. Hulk uçurtmasını kocaman elleriyle tuttu ve gülümsedi. "Teşekkürler, Örümcek Adam," dedi Hulk. Rüzgar yeniden esince ikisi uçurtmayı mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "başını çekingen çekingen eğdi"
   - Cümle 4: «"Çamur uçurtmamı kirletecek," dedi Hulk ve başını çekingen çekingen eğdi.»
   - Açıklama: 'Çekingen' soyut bir kelime ve ikilemeli zarf kullanımı küçük çocuk için uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Uçurtma çamurun hemen yanına düşmüştü"
   - Cümle 8: «Uçurtma çamurun hemen yanına düşmüştü.»
   - Açıklama: Çamur tehlike olarak kuruluyor ama uçurtma çamura hiç değmediği için işlevsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0097` birebir aynı, `@degisim: pizza -> uçurtma` (tutuyorsan), ardından `@onarim: 934c47fca0f2241b6d82c05fa1212f706587e36c`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0098 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0098
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: paylaşmak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kamyon', fiil 'giyinmek', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: kum dökülüyordu ve kale büyümüyordu | oyuncak kamyonunu arkadaşıyla paylaştı
@tohum: orumcek_adam-0098
@degisim: giyinmek -> taşımak
Bir sabah Örümcek Adam parkta çizgili oyuncak kamyonuyla oynuyordu. Yanında Spin kumdan bir kale yapıyordu. Ama Spin kumu elleriyle taşıyamıyordu, çünkü parmaklarından dökülüyordu. Örümcek Adam örümcek hissiyle başını kaldırdı ve Spin'in üzgün yüzünü gördü. "Bu kale hiç büyümüyor," dedi Spin. Örümcek Adam kamyonunu Spin'e uzattı. "Al, Spin, kamyonumu birlikte kullanalım," dedi Örümcek Adam. Spin kamyonu kumla doldurdu ve kaleye götürdü. Sonra sırayla taşıdılar ve duvarlar hızla yükseldi. İkisi de çok sevindi, çünkü paylaşınca kale çabucak büyümüştü.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam örümcek hissiyle"
   - Cümle 4: «Örümcek Adam örümcek hissiyle başını kaldırdı ve Spin'in üzgün yüzünü gördü.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissiyle başını kaldırdı"
   - Cümle 4: «Örümcek Adam örümcek hissiyle başını kaldırdı ve Spin'in üzgün yüzünü gördü.»
   - Açıklama: Spin hemen yanındayken örümcek hissi yalnız baş kaldırtıyor ve çözüme katkı vermiyor, kartın özellik alanındaki gibi işe yarar kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0098` birebir aynı, `@degisim: giyinmek -> taşımak` (tutuyorsan), ardından `@onarim: 51ee1b09867ff7189f204263b5079a65b203bf66`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0099 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0099
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'balon', fiil 'dizmek', sıfat 'uykulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar balonları uçurdu ve balonlar ağaca takıldı | ağ atıp balonları tek tek indirdi
@tohum: orumcek_adam-0099
@degisim: uykulu -> renkli
Parkta güçlü bir rüzgar esiyordu. Örümcek Adam'ın arkadaşı Ghost-Spider renkli balonlarını bir banka diziyordu. Birden rüzgar üç balonu uçurdu ve balonlar yüksek bir ağaca takıldı. O dallara baktı ve çok üzüldü. Örümcek Adam arkadaşına yardım etmek istedi. Ağacın altına koştu ve ağ attı. Ağ ilk balonun ipine yapıştı. Örümcek Adam ipi yavaşça çekti ve balon aşağı indi. Sonra öbür iki balonu da indirdi. Balonları arkadaşına verdi ve ikisi ipleri banka sıkıca bağladı. Arkadaşı sevinçle ellerini çırptı. Örümcek Adam çok mutlu oldu, çünkü arkadaşının balonlarını kurtarmıştı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O dallara baktı ve çok üzüldü"
   - Cümle 4: «O dallara baktı ve çok üzüldü.»
   - Açıklama: 'O' zamirinin Ghost-Spider'ı mı gösterdiği yoksa 'o dallar' mı olduğu belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O dallara baktı"
   - Cümle 4: «O dallara baktı ve çok üzüldü.»
   - Açıklama: 'O' zamirinin Ghost-Spider'ı mı gösterdiği yoksa 'o dallara' mı okunacağı belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0099` birebir aynı, `@degisim: uykulu -> renkli` (tutuyorsan), ardından `@onarim: be1323ff75cfd973694940483eb94f705bc40bb5`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0100 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0100
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'filiz', fiil 'incelemek', sıfat 'tekerlekli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: tekerlekli bir araba kayıyordu ve önünde bir filiz vardı | arabayı tuttu ve arkadaşından bir taş istedi
@tohum: orumcek_adam-0100
Parkta hafif bir rüzgar esiyordu. Örümcek Adam çiçek bahçesindeydi ve örümcek hissi bir sorun olduğunu haber verdi. Tekerlekli bir araba yokuştan kayıyordu ve önünde küçük bir filiz vardı. Örümcek Adam koştu ve arabayı iki eliyle tuttu. Sonra tekerleği inceledi. Tekerleğin önüne bir taş gerekiyordu. Ama arabayı bırakmadı. Ghost-Spider yakında oynuyordu. "Arkadaşım, bana bir taş getirir misin?" diye seslendi Örümcek Adam. Arkadaşı hemen bir taş getirdi ve tekerleğin önüne koydu. Araba durdu ve filiz kurtuldu. "Teşekkürler, arkadaşım, filizi birlikte kurtardık!" dedi Örümcek Adam.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 2: «Örümcek Adam çiçek bahçesindeydi ve örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' mecazlı ve soyut bir anlatım.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 'haber verdi' onunla mecazlı kullanılmış.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Tekerlekli bir araba yokuştan kayıyordu"
   - Cümle 3: «Tekerlekli bir araba yokuştan kayıyordu ve önünde küçük bir filiz vardı.»
   - Açıklama: Arabanın neden orada olduğu ve neden kaymaya başladığı söylenmiyor.
   - Açıklama: Arabanın neden kendi kendine kaymaya başladığı söylenmiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "koştu ve arabayı iki eliyle tuttu"
   - Cümle 4: «Örümcek Adam koştu ve arabayı iki eliyle tuttu.»
   - Açıklama: Yokuştan kayan tekerlekli arabayı elleriyle durdurmak çocuğun taklit edebileceği tehlikeli bir davranış.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam koştu ve arabayı iki eliyle tuttu"
   - Cümle 4: «Örümcek Adam koştu ve arabayı iki eliyle tuttu.»
   - Açıklama: Yokuştan kayan tekerlekli arabayı elle durdurmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0100` birebir aynı, ardından `@onarim: 0c2d313d3eafadd3152debec8e508472529ae6c9`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0101 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0101
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'harita', fiil 'beslemek', sıfat 'sağlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: harita suyun kenarında kaldı ve dalga geliyordu | haritayı hemen aldı ve özür diledi
@tohum: orumcek_adam-0101
@degisim: beslemek -> yemek
Kumsalda Örümcek Adam ile Hulk hazine oyunu oynuyordu. Örümcek Adam, Hulk'ın çizdiği haritayı suyun kenarına bıraktı. Birden örümcek hissiyle haritaya bir dalga geldiğini anladı. Örümcek Adam kağıdı kumdan hemen aldı. Ama bir köşesi ıslanmıştı. "Özür dilerim, Hulk, haritanı suya çok yakın bıraktım," dedi Örümcek Adam. "Sorun değil, yol yine görünüyor," dedi Hulk. İkisi haritadaki yolu izleyip büyük bir kayanın yanına yürüdü. Kayanın arkasında Hulk'ın sakladığı sağlıklı meyveler vardı. Örümcek Adam ile Hulk kumda oturdu ve meyveleri mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle haritaya bir"
   - Cümle 3: «Birden örümcek hissiyle haritaya bir dalga geldiğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle haritaya"
   - Cümle 3: «Birden örümcek hissiyle haritaya bir dalga geldiğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0101` birebir aynı, `@degisim: beslemek -> yemek` (tutuyorsan), ardından `@onarim: 88ad967da49f1098d45d828aad01433066a50cb9`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0102 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0102
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'dolma', fiil 'şaşırmak', sıfat 'geniş'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar uçurtmayı geniş duvarın üstünden uçurdu | duvara tırmanıp sesi yapan uçurtmayı buldu
@tohum: orumcek_adam-0102
@degisim: dolma -> uçurtma
Bir sabah Örümcek Adam limanda kırmızı uçurtmasını uçuruyordu. Birden rüzgar sert esti ve uçurtmanın ipi elinden kaydı. Uçurtma geniş taş duvarın üstünden uçtu ve kayboldu. Örümcek Adam çok üzüldü. Sonra duvarın üstünden garip bir ses geldi. Örümcek Adam bu sesi merak etti. Aşağıdan duvarın üstü görünmüyordu. Örümcek Adam süper gücüyle duvara tırmandı. Duvarın üstünde kendi uçurtmasını görünce şaşırdı. Uçurtmanın ipi eski bir demire takılmıştı. Rüzgar estikçe kağıdı sallanıyor ve ses çıkarıyordu. Örümcek Adam ipi dikkatle çözdü ve uçurtmayla aşağı indi. Örümcek Adam çok sevindi, çünkü hem sesi hem de uçurtmasını bulmuştu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi yapan uçurtmayı buldu"
   - Cümle 0 (plan satırı): «rüzgar uçurtmayı geniş duvarın üstünden uçurdu | duvara tırmanıp sesi yapan uçurtmayı buldu»
   - Açıklama: Ses 'yapılmaz', 'çıkarılır'; fiil nesnesine uymuyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "duvarın üstünden garip bir ses geldi"
   - Cümle 5: «Sonra duvarın üstünden garip bir ses geldi.»
   - Açıklama: Kaybolan uçurtmanın yanına ikinci bir sorun olarak gizemli ses ekleniyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Örümcek Adam bu sesi merak etti"
   - Cümle 6: «Örümcek Adam bu sesi merak etti.»
   - Açıklama: Figür uçurtmayı aramak için değil sesi merak ettiği için tırmanıyor; çözüm sebebe doğrudan yönelmiyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hem sesi hem de uçurtmasını bulmuştu"
   - Cümle 13: «Örümcek Adam çok sevindi, çünkü hem sesi hem de uçurtmasını bulmuştu.»
   - Açıklama: Ses bulunmaz; 'bulmak' fiili 'ses' nesnesine uymuyor.
   - Açıklama: Ses bulunmaz; 'sesin nereden geldiğini' olmalı.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "hem sesi hem de uçurtmasını bulmuştu"
   - Cümle 13: «Örümcek Adam çok sevindi, çünkü hem sesi hem de uçurtmasını bulmuştu.»
   - Açıklama: Garip ses kayıp uçurtmanın yanına ikinci bir gizem olarak ekleniyor ve son cümle onu ayrı bir hedef gibi kapatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0102` birebir aynı, `@degisim: dolma -> uçurtma` (tutuyorsan), ardından `@onarim: cae30b8ca962ae65a78a667fa3e06c411e1673e2`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0103 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0103
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'sakız', fiil 'dilemek', sıfat 'kapalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: büyük bir bina denize inen güneşi kapatıyordu | binanın duvarına tırmanıp güneşi gördü
@tohum: orumcek_adam-0103
@degisim: sakız -> güneş
Örümcek Adam limanda yürüyordu. Güneş denize doğru iniyordu ve gökyüzü kırmızı olmuştu. Ama büyük bir liman binası güneşi kapatıyordu. Örümcek Adam güneşin denize inişini görmek istiyordu. Binanın kapısı kapalıydı. Örümcek Adam binanın duvarına tırmandı ve çatıya çıktı. Oradan kırmızı güneşi ve parlayan denizi gördü. Güneşe baktı ve herkes mutlu olsun diye bir dilek diledi. Güneş yavaş yavaş denize indi. Örümcek Adam duvardan indi ve kumsala döndü. Örümcek Adam bundan sonra akşamları gökyüzüne daha çok baktı.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "binanın duvarına tırmandı ve çatıya çıktı"
   - Cümle 6: «Örümcek Adam binanın duvarına tırmandı ve çatıya çıktı.»
   - Açıklama: Kapısı kapalı bir binanın çatısına yalnız manzara için çıkılması çocuğun taklit edebileceği yükseğe çıkma davranışıdır.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "herkes mutlu olsun diye bir dilek diledi"
   - Cümle 8: «Güneşe baktı ve herkes mutlu olsun diye bir dilek diledi.»
   - Açıklama: Dilek sahnesi olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Dilek olaydan çıkmıyor ve hiçbir işe yaramıyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "duvardan indi ve kumsala döndü"
   - Cümle 10: «Örümcek Adam duvardan indi ve kumsala döndü.»
   - Açıklama: Hikaye limanda geçiyor ama figür hiç bulunmadığı kumsala dönüyor; sahne değişiyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Örümcek Adam bundan sonra akşamları gökyüzüne daha çok baktı"
   - Cümle 11: «Örümcek Adam bundan sonra akşamları gökyüzüne daha çok baktı.»
   - Açıklama: Son cümle olaydan çıkan bir ders ya da sıcak bir kapanış değil, çıplak bir alışkanlık bildiriyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "bundan sonra akşamları gökyüzüne daha çok baktı"
   - Cümle 11: «Örümcek Adam bundan sonra akşamları gökyüzüne daha çok baktı.»
   - Açıklama: Son cümle olaydan çıkan somut bir ders ya da sıcak bir kapanış değil, çıplak bir alışkanlık bildirimi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0103` birebir aynı, `@degisim: sakız -> güneş` (tutuyorsan), ardından `@onarim: 981a84a916183136370a190915877fc872f33ac6`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0108 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0108
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'zarf', fiil 'ovuşturmak', sıfat 'tuzlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: yüksek duvardan garip bir ses geldi | duvara tırmanıp sesi yapan uçurtmayı buldu
@tohum: orumcek_adam-0108
@degisim: zarf -> uçurtma
Rüzgar hafif hafif esiyordu. Örümcek Adam tuzlu suyun kenarında oynarken garip bir ses duydu. Ses yüksek bir taş duvarın tepesinden geliyordu. Örümcek Adam gözlerini ovuşturdu ve yukarı baktı. Ama aşağıdan hiçbir şey göremedi. Sesi çok merak etti. Örümcek Adam süper gücüyle duvara tırmandı ve tepeye çıktı. Orada kırmızı bir uçurtma takılı kalmıştı. Uçurtmanın kağıdı rüzgarda sallanıp ses çıkarıyordu. Örümcek Adam uçurtmayı dikkatle kurtardı ve aşağı indi. Kumsalda ipini tuttu ve uçurtma havaya yükseldi. Örümcek Adam çok sevindi, çünkü o garip sesi yapan uçurtmayı bulmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tuzlu suyun kenarında oynarken"
   - Cümle 2: «Örümcek Adam tuzlu suyun kenarında oynarken garip bir ses duydu.»
   - Açıklama: Deniz yerine 'tuzlu su' denmesi doğal değil; kelime yerinde kullanılmamış.
   - Açıklama: Deniz yerine 'tuzlu su' denmesi doğal değil ve kelime yerinde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0108` birebir aynı, `@degisim: zarf -> uçurtma` (tutuyorsan), ardından `@onarim: a518ccd5cedbe84829b5e5bd5c1a4b312119bb52`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0109 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0109
- yer: ev (Takımın gizli evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'çim', fiil 'bırakmak', sıfat 'kıvrımlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: koşarken yerdeki resme bastı ve resim buruştu | özür dileyip resmi duvarın en üstüne astı
@tohum: orumcek_adam-0109
@degisim: kıvrımlı -> yeşil
Örümcek Adam gizli evin önünde koşarak oynuyordu. Spin kağıda yeşil çimler çizmiş, resmi kurusun diye yere bırakmıştı. Örümcek Adam resmi görmedi ve üstüne bastı. Resim buruştu ve Spin çok üzüldü. Örümcek Adam hemen durdu ve Spin'den özür diledi. Resim düz kurusun diye onu yükseğe asmak istedi. Süper gücüyle evin duvarına tırmandı ve resmi en üstteki çiviye astı. Spin yukarıdaki resmine baktı ve gülümsedi. Örümcek Adam rahatladı, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Resim düz kurusun diye onu yükseğe asmak istedi"
   - Cümle 6: «Resim düz kurusun diye onu yükseğe asmak istedi.»
   - Açıklama: Resmi duvarın en üstüne asmak buruşukluğu gidermiyor; çözüm sorunun sebebine yönelmiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "evin duvarına tırmandı"
   - Cümle 7: «Süper gücüyle evin duvarına tırmandı ve resmi en üstteki çiviye astı.»
   - Açıklama: Güvenli kullanım satırı ev içi tırmanmayı yasaklıyor; evde resim asmak için duvara tırmanmak çocuğun taklit edebileceği bir ev içi tırmanma örneği.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "resmi en üstteki çiviye astı"
   - Cümle 7: «Süper gücüyle evin duvarına tırmandı ve resmi en üstteki çiviye astı.»
   - Açıklama: Sorun resmin buruşması ama çözüm resmi yükseğe asmak; bu buruşukluğu gidermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0109` birebir aynı, `@degisim: kıvrımlı -> yeşil` (tutuyorsan), ardından `@onarim: 5a59baac6c41898ba7f073e2cae84943895a44ed`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0110 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0110
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gökkuşağı', fiil 'eğlendirmek', sıfat 'yuvarlak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: dalgalar kum kalesine yaklaşıyordu | kalenin önüne çukur kazdı ve kumdan duvar yaptı
@tohum: orumcek_adam-0110
@degisim: gökkuşağı -> kum
Kumsalda güneşli ve sıcak bir gündü. Örümcek Adam suyun yakınında yuvarlak bir kum kalesi yapıyordu. Birden örümcek hissi bir sorun olduğunu haber verdi: dalgalar kaleye yaklaşıyordu. Örümcek Adam denize dikkatle baktı. Her dalga kuma biraz daha yukarı geliyordu. Kale yapmak onu çok eğlendiriyordu ve kalesini kaybetmek istemiyordu. Hemen kalenin önüne uzun bir çukur kazdı. Çıkan kumla çukurun arkasına alçak bir duvar yaptı. Sonra büyük bir dalga geldi. Su çukura doldu ve duvarda durdu. Yuvarlak kale hiç ıslanmadı. Örümcek Adam kalesinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi bir sorun olduğunu haber verdi: dalgalar kaleye yaklaşıyordu.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut bir kavram ve mecazdır.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber vermesi mecaz.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kale yapmak onu çok eğlendiriyordu ve kalesini kaybetmek istemiyordu"
   - Cümle 6: «Kale yapmak onu çok eğlendiriyordu ve kalesini kaybetmek istemiyordu.»
   - Açıklama: İki yan cümlenin öznesi farklı ama bağlaçla tek özneliymiş gibi bağlanmış; özne uyumu bozuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0110` birebir aynı, `@degisim: gökkuşağı -> kum` (tutuyorsan), ardından `@onarim: f8432a3cb2b515cd9caca70d884c8216cd218f60`, sonra gövde.
