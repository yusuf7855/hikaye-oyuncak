# Editör görevi (onarım): Örümcek Adam, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0093 (deneme 3 -> 4)

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
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin parkın oyun alanında bilye oynuyordu. Birden Spin'in mavi bilyesi yokuştan aşağı yuvarlandı ve kayboldu. "Bilyemi bulamıyorum, Örümcek Adam," dedi Spin üzgün bir sesle. Örümcek Adam yavaş yavaş aşağı yürüdü. Bir bankın yanına geldi. Süper gücü olan örümcek hissi ona burada durmasını söyledi. Örümcek Adam hemen eğildi ve bankın altına baktı. Mavi bilye kuru yaprakların arasında duruyordu. Örümcek Adam onu aldı ve iki eliyle Spin'e sundu. "İşte bilyen, Spin," dedi Örümcek Adam. Spin sevinçle bilyesini tuttu. İki arkadaş oyun alanına döndü ve bilye oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Süper gücü olan örümcek hissi ona burada durmasını söyledi"
   - Cümle 7: «Süper gücü olan örümcek hissi ona burada durmasını söyledi.»
   - Açıklama: His konuşmaz ve süper gücü olan şey his değil Örümcek Adam'dır; kelimeler öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona burada durmasını söyledi"
   - Cümle 7: «Süper gücü olan örümcek hissi ona burada durmasını söyledi.»
   - Açıklama: Konuşan 'örümcek hissi' soyut bir kavram ve mecazdır, küçük çocuk anlamaz.
   - Açıklama: Konuşan bir 'his' soyut ve mecazlı bir anlatım, küçük çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissi ona burada durmasını söyledi"
   - Cümle 7: «Süper gücü olan örümcek hissi ona burada durmasını söyledi.»
   - Açıklama: Kartta örümcek hissi bir sorun olduğunu haber verir; burada kayıp eşyanın yerini gösteren bir araç olarak kullanılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Süper gücü olan örümcek hissi ona burada durmasını söyledi"
   - Cümle 7: «Süper gücü olan örümcek hissi ona burada durmasını söyledi.»
   - Açıklama: Kartın özellikler alanında örümcek hissi yalnız bir sorun olduğunu haber verir; burada kayıp bilyenin yerini bulan bir iz sürme aracı gibi kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0093` birebir aynı, ardından `@onarim: c1903ff39e8ab4b9dab57ad9fa1899a48f31604b`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0096 (deneme 3 -> 4)

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
Parkın bahçesinde renkli çiçekler açmıştı. Örümcek Adam ilk kez onların resmini yapmayı denemek istiyordu. Ama önündeki uzun çalılar çiçeklerin çoğunu kapatıyordu. Örümcek Adam'ın kağıdı ve kalemi yoktu. Spin ona bir kağıtla bir kalem uzattı. "Önce iyice bak, sonra çiz," dedi Spin. Örümcek Adam onu dikkatle dinledi. Hemen süper gücüyle bahçenin yanındaki taş duvara tırmandı. Duvarın üstünden bütün bahçe görünüyordu. Kırmızı, sarı ve mor çiçeklere uzun uzun baktı. Sonra aşağı indi ve çiçekli bir resim çizdi. "Çok güzel olmuş, Örümcek Adam!" dedi Spin. Örümcek Adam çok sevindi, çünkü ilk resmini kendisi yapmıştı.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Örümcek Adam'ın kağıdı ve kalemi yoktu"
   - Cümle 4: «Örümcek Adam'ın kağıdı ve kalemi yoktu.»
   - Açıklama: Çalıların çiçekleri kapatması sorununa ek olarak kağıt ve kalem eksikliği ikinci bir sorun olarak ekleniyor.
   - Açıklama: Çalıların çiçekleri kapatması sorununun yanına kağıt ve kalem eksikliği diye ikinci bir sorun ekleniyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Spin ona bir kağıtla bir kalem uzattı"
   - Cümle 5: «Spin ona bir kağıtla bir kalem uzattı.»
   - Açıklama: Kağıt ve kalem eksikliğini figür değil yan karakter Spin gideriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0096` birebir aynı, `@degisim: cüzdan -> kalem` (tutuyorsan), ardından `@onarim: ef519d1b0b1e5b9e21b0c00a3c7c48fd4ff87927`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0098 (deneme 3 -> 4)

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
Bir sabah Örümcek Adam parkta çizgili oyuncak kamyonuyla oynuyordu. Biraz uzakta Spin kumdan bir kale yapıyordu. Ama Spin kumu elleriyle taşıyamıyordu, çünkü parmaklarından dökülüyordu. Örümcek Adam süper gücü olan örümcek hissiyle bir sorun olduğunu anladı. Hemen Spin'in yanına gitti ve onun üzgün yüzünü gördü. "Bu kale hiç büyümüyor," dedi Spin. Örümcek Adam kamyonunu Spin'e uzattı. "Al, Spin, kamyonumu birlikte kullanalım," dedi Örümcek Adam. Spin kamyonu kumla doldurdu ve kaleye götürdü. Sonra sırayla taşıdılar ve duvarlar hızla yükseldi. İkisi de çok sevindi, çünkü paylaşınca kale çabucak büyümüştü.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 4: «Örümcek Adam süper gücü olan örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: Tamlama bozuk; süper gücü olan Örümcek Adam iken cümlede his süper güce sahipmiş gibi duruyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun olduğunu anladı"
   - Cümle 4: «Örümcek Adam süper gücü olan örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'örümcek hissi' ve 'bir sorun olduğunu anladı' küçük çocuk için soyut.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 4: «Örümcek Adam süper gücü olan örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu anladı' soyut, 3 yaşındaki çocuk için anlaşılmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0098` birebir aynı, `@degisim: giyinmek -> taşımak` (tutuyorsan), ardından `@onarim: f32cf09d0d1b8835253d390fc6fd46ad4fc6152c`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0101 (deneme 3 -> 4)

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
Kumsalda Örümcek Adam ile Hulk hazine oyunu oynuyordu. Örümcek Adam, Hulk'ın çizdiği haritayı suyun kenarına bıraktı. Birden süper gücü olan örümcek hissiyle büyük bir dalganın geldiğini anladı. Örümcek Adam kağıdı kumdan hemen aldı. Ama bir köşesi ıslanmıştı. "Özür dilerim, Hulk, haritanı suya çok yakın bıraktım," dedi Örümcek Adam. "Sorun değil, yol yine görünüyor," dedi Hulk. İkisi haritadaki yolu izleyip büyük bir kayanın yanına yürüdü. Kayanın arkasında Hulk'ın sakladığı sağlıklı meyveler vardı. Örümcek Adam ile Hulk kumda oturdu ve meyveleri mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle büyük bir dalganın geldiğini anladı.»
   - Açıklama: Sıfat cümleciği yanlış kelimeye bağlanmış, tamlama bozuk.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Birden süper gücü olan örümcek hissiyle büyük bir dalganın geldiğini anladı"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle büyük bir dalganın geldiğini anladı.»
   - Açıklama: Tamlama bozuk ve cümlenin öznesi belirsiz; 'süper gücü olan örümcek hissi' dilbilgisel değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle büyük bir dalganın geldiğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Süper güç' ve 'örümcek hissi' soyut kavramlar; 3 yaşındaki çocuk bilmez.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam kağıdı kumdan hemen aldı"
   - Cümle 4: «Örümcek Adam kağıdı kumdan hemen aldı.»
   - Açıklama: Büyük bir dalga gelirken su kenarına gidip eşya almak çocuğun taklit edebileceği tehlikeli bir davranıştır.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ama bir köşesi ıslanmıştı"
   - Cümle 5: «Ama bir köşesi ıslanmıştı.»
   - Açıklama: Örümcek Adam dalga gelmeden haritayı hemen aldığı halde haritanın ıslanmış olması çözümle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0101` birebir aynı, `@degisim: beslemek -> yemek` (tutuyorsan), ardından `@onarim: 0ff45732088c1e8c3a95581df7c307aae09068f9`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0103 (deneme 3 -> 4)

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
Örümcek Adam limanda yürüyordu. Güneş denize doğru iniyordu ve gökyüzü kırmızı olmuştu. Ama büyük bir liman binası güneşi kapatıyordu. Örümcek Adam güneş denize inerken bir dilek dilemek istiyordu. Binanın kapısı kapalıydı. Örümcek Adam süper gücüyle binanın duvarına tırmandı. Duvarın üstünden kırmızı güneşi ve parlayan denizi gördü. Güneşe baktı ve yarın da güneşli bir gün olsun diye dilek diledi. Güneş yavaş yavaş denize indi. Örümcek Adam mutlu mutlu duvardan indi. Örümcek Adam bundan sonra güneşi bina olmayan kumsaldan izledi.
```

**Hakem bulguları (2):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "güneşi bina olmayan kumsaldan izledi"
   - Cümle 11: «Örümcek Adam bundan sonra güneşi bina olmayan kumsaldan izledi.»
   - Açıklama: Son ders cümlesi yaşanan olaydan çıkmıyor; sorun duvara tırmanarak çözülmüşken kumsala gitmek ders olarak sebepsizce ekleniyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "bundan sonra güneşi bina olmayan kumsaldan izledi"
   - Cümle 11: «Örümcek Adam bundan sonra güneşi bina olmayan kumsaldan izledi.»
   - Açıklama: Son cümle olaydan çıkan sıcak bir kapanış değil, az önceki çözümü geçersiz kılan kuru bir eylem.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0103` birebir aynı, `@degisim: sakız -> güneş` (tutuyorsan), ardından `@onarim: 905dddf8aef0735048cde0bc5ab12f0f02696d29`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0108 (deneme 3 -> 4)

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
@plan: yüksek duvardan garip bir ses geldi | duvara tırmanıp sesi çıkaran uçurtmayı buldu
@tohum: orumcek_adam-0108
@degisim: zarf -> uçurtma
Rüzgar hafif hafif esiyordu. Örümcek Adam kıyıda, denizin tuzlu suyuyla oynarken garip bir ses duydu. Ses yüksek bir taş duvarın tepesinden geliyordu. Örümcek Adam gözlerini ovuşturdu ve yukarı baktı. Ama aşağıdan hiçbir şey göremedi. Sesi çok merak etti. Örümcek Adam süper gücüyle duvara tırmandı ve tepeye çıktı. Orada kırmızı bir uçurtma takılı kalmıştı. Uçurtmanın kağıdı rüzgarda sallanıp ses çıkarıyordu. Örümcek Adam uçurtmayı dikkatle kurtardı ve aşağı indi. Kumsalda ipini tuttu ve uçurtma havaya yükseldi. Örümcek Adam çok sevindi, çünkü o garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kumsalda ipini tuttu ve uçurtma havaya yükseldi"
   - Cümle 11: «Kumsalda ipini tuttu ve uçurtma havaya yükseldi.»
   - Açıklama: Sesin kaynağı bulunduktan sonra kimin olduğu belirsiz uçurtmanın uçurulması sebepsiz ve işlevsiz ek bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0108` birebir aynı, `@degisim: zarf -> uçurtma` (tutuyorsan), ardından `@onarim: 3401f376f7a8b470d1585bdc5cfa597da2bd672f`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0109 (deneme 3 -> 4)

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
@plan: koşarken yerdeki resme bastı ve resim buruştu | özür dileyip resmi düzeltti ve duvara astı
@tohum: orumcek_adam-0109
@degisim: kıvrımlı -> yeşil
Örümcek Adam gizli evin önünde koşarak oynuyordu. Spin kağıda yeşil çimler çizmiş, resmi kurusun diye yere bırakmıştı. Örümcek Adam resmi görmedi ve üstüne bastı. Resim buruştu ve Spin çok üzüldü. Örümcek Adam hemen durdu ve Spin'den özür diledi. Sonra buruşuk resmi elleriyle yavaş yavaş düzeltti. Resmi yerde bırakmak istemedi, çünkü koşarken yine basabilirdi. Süper gücüyle evin dış duvarına tırmandı ve resmi bir çiviye astı. Resim orada düz kaldı ve güneşte kurudu. Spin yukarıdaki resmine baktı ve gülümsedi. Örümcek Adam rahatladı, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Süper gücüyle evin dış duvarına tırmandı"
   - Cümle 8: «Süper gücüyle evin dış duvarına tırmandı ve resmi bir çiviye astı.»
   - Açıklama: Evde resim asmak için evin duvarına tırmanmak, güvenli özellik kullanımı satırının kaçındığı ev ortamında taklit edilebilir bir tırmanma örneği veriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Süper gücüyle evin dış duvarına"
   - Cümle 8: «Süper gücüyle evin dış duvarına tırmandı ve resmi bir çiviye astı.»
   - Açıklama: 'Süper güç' 3 yaşındaki bir çocuk için soyut bir kavram.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Süper gücüyle evin dış duvarına tırmandı"
   - Cümle 8: «Süper gücüyle evin dış duvarına tırmandı ve resmi bir çiviye astı.»
   - Açıklama: Özür ve düzeltmeden sonra duvara tırmanıp asmak üçüncü bir adım ekliyor ve çözüm ikiyi aşıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "resmi bir çiviye astı"
   - Cümle 8: «Süper gücüyle evin dış duvarına tırmandı ve resmi bir çiviye astı.»
   - Açıklama: Çözüm özür dileme, düzeltme ve duvara tırmanıp asma olarak üç adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0109` birebir aynı, `@degisim: kıvrımlı -> yeşil` (tutuyorsan), ardından `@onarim: 61520abefce31798e53ca1edc405ff7408f1a197`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0110 (deneme 3 -> 4)

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
Kumsalda güneşli ve sıcak bir gündü. Örümcek Adam suyun yakınında yuvarlak bir kum kalesi yapıyordu. Birden süper gücü olan örümcek hissiyle dalgaların kaleye yaklaştığını anladı. Örümcek Adam denize dikkatle baktı. Her dalga kuma biraz daha yukarı geliyordu. Kale yapmak Örümcek Adam'ı çok eğlendiriyordu. Kalesini kaybetmek istemiyordu. Hemen kalenin önüne uzun bir çukur kazdı. Çıkan kumla çukurun arkasına alçak bir duvar yaptı. Sonra büyük bir dalga geldi. Su çukura doldu ve duvarda durdu. Yuvarlak kale hiç ıslanmadı. Örümcek Adam kalesinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle dalgaların kaleye yaklaştığını anladı.»
   - Açıklama: Sıfat cümleciği yanlış öğeye bağlanmış; 'süper gücü olan' örümceği niteliyor gibi okunuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle dalgaların kaleye yaklaştığını anladı.»
   - Açıklama: 'Örümcek hissi' ve 'süper güç' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' ve 'süper güç' 3 yaşındaki çocuk için soyut kavramlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0110` birebir aynı, `@degisim: gökkuşağı -> kum` (tutuyorsan), ardından `@onarim: da13c35c49342748e85832d40cca1041945c7027`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0115
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'baston', fiil 'buruşturmak', sıfat 'yalnız'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: tek salıncak boştu ve ikisi de binmek istedi | sırayla bindiler ve arkadaşını ağla salladı
@tohum: orumcek_adam-0115
@degisim: baston -> salıncak
Parkta serin bir rüzgar esiyordu. Örümcek Adam ile Spin oyun alanına koştu. Ama orada yalnız bir salıncak boştu ve ikisi de binmek istedi. Spin yüzünü buruşturdu. "Önce sen bin, Spin, sonra sıra bende," dedi Örümcek Adam. Spin sevinçle salıncağa oturdu. Örümcek Adam bileğinden salıncağa ağ attı. Ağı yavaşça çekip bıraktı ve salıncak ileri geri sallandı. Spin çok güldü. Sonra salıncaktan indi. "Şimdi sıra sende, Örümcek Adam!" dedi Spin. Örümcek Adam salıncağa bindi ve Spin onu arkadan itti. Örümcek Adam bundan sonra parkta hep sırayla oynadı.
```

**Hakem bulguları (1):**

1. **C5** (K merceği) — Son güvenli ve sorun çözülmüş ('sıcaklık' aranmaz).
   - Alıntı: "Örümcek Adam bundan sonra parkta hep sırayla oynadı"
   - Cümle 13: «Örümcek Adam bundan sonra parkta hep sırayla oynadı.»
   - Açıklama: Korkunç sesin ne olduğu hiç açıklanmadan hikaye bitiyor; bu gerilim çözülmemiş kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0115` birebir aynı, `@degisim: baston -> salıncak` (tutuyorsan), ardından `@onarim: 4a0eee8a98c80580ece8f35746a2e65dba30404b`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0116 (deneme 3 -> 4)

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
@plan: açık pencereden esen rüzgar kağıt uçağı çatıya uçurdu | özür dileyip tırmandı ve uçağı çatıdan ayırdı
@tohum: orumcek_adam-0116
@degisim: tablo -> uçak
Rüzgar gizli evin açık penceresinden esiyordu. Örümcek Adam pencereyi açık bırakmıştı ve yaratıcı Hulk kağıttan bir uçak yapıyordu. Birden rüzgar uçağı pencereden dışarı uçurdu ve uçak çatının kenarına takıldı. "Uçağım çok yukarıda kaldı!" dedi Hulk. "Özür dilerim, Hulk, pencereyi ben açık bıraktım," dedi Örümcek Adam. Örümcek Adam önce pencereyi kapattı. Sonra dışarı çıktı ve süper gücüyle evin duvarına tırmandı. Uçağı çatının kenarından yavaşça ayırdı. Aşağı indi ve uçağı Hulk'a verdi. "Sorun yok, dostum," dedi Hulk ve gülümsedi. Sonra Örümcek Adam ile Hulk uçağı birlikte mutlu mutlu uçurdu.
```

**Hakem bulguları (2):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "yaratıcı Hulk kağıttan bir uçak yapıyordu"
   - Cümle 2: «Örümcek Adam pencereyi açık bırakmıştı ve yaratıcı Hulk kağıttan bir uçak yapıyordu.»
   - Açıklama: Kartın yanlar bölümünde Hulk kocaman, yeşil ve çok güçlü diye tanımlanır; yaratıcılık karttaki tarifinde yok.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Örümcek Adam önce pencereyi kapattı"
   - Cümle 6: «Örümcek Adam önce pencereyi kapattı.»
   - Açıklama: Çözüm pencereyi kapatma, dışarı çıkma, tırmanma, ayırma ve inme gibi ikiden çok adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0116` birebir aynı, `@degisim: tablo -> uçak` (tutuyorsan), ardından `@onarim: a5b4050b468eb846312de18e0c35f726ec8d2f7f`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0118 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@degisim: sabırsızlanmak -> denemek
Örümcek Adam kumsalda ilk kez ekşi bir turşu deneyecekti. Kavanozu kumun üstüne koyunca örümcek hissi başını gıdıkladı. Hemen arkasına baktı ve kavanoza doğru gelen büyük bir dalga gördü. Örümcek Adam kavanozu kaptı ve geriye doğru koştu. Dalga, kavanozun durduğu yeri ıslattı. Örümcek Adam sabırlıydı ve dalga denize geri çekilene kadar bekledi. Kavanozun üstüne tek bir damla bile gelmemişti. Sonra kuru kumun üstüne oturdu ve kapağı açtı. Bir turşu aldı ve onu yavaşça çiğnedi. Tadını çok beğendi ve bir tane daha yedi. Örümcek Adam bundan sonra yiyeceklerini hep sudan uzak bir yere koydu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi başını gıdıkladı"
   - Cümle 2: «Kavanozu kumun üstüne koyunca örümcek hissi başını gıdıkladı.»
   - Açıklama: His baş gıdıklamaz; mecaz ve soyut kavram 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi başını gıdıkladı' mecazlı ve soyut bir anlatımdır.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kavanozu kumun üstüne koyunca"
   - Cümle 2: «Kavanozu kumun üstüne koyunca örümcek hissi başını gıdıkladı.»
   - Açıklama: Kavanozun neden suya yakın konduğu söylenmiyor ve kapalı bir kavanozun ıslanması çocuk için zayıf bir sorun.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Örümcek Adam sabırlıydı ve dalga"
   - Cümle 6: «Örümcek Adam sabırlıydı ve dalga denize geri çekilene kadar bekledi.»
   - Açıklama: Tohumdaki özellik örümcek hissi; sabır ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0118` birebir aynı, `@degisim: sabırsızlanmak -> denemek` (tutuyorsan), ardından `@onarim: f9c264ce77f4f65ae6380f8ec1f18252cee9cc43`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0119 (deneme 3 -> 4)

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
@plan: çantada bir delik vardı ve paket kayıyordu | düşen paketi yakaladı ve çantanın delikli köşesini bağladı
@tohum: orumcek_adam-0119
Yağmur gizli evin çatısına tıp tıp vuruyordu. Örümcek Adam içeride paket oyunu oynuyor ve yepyeni bluz paketlerini odalara dağıtıyordu. Ama çantasının köşesinde küçük bir delik vardı ve bir paket kayıyordu. Çanta onun arkasındaydı ve Örümcek Adam deliği göremedi. Birden örümcek hissi başını gıdıkladı. Hemen çantasına baktı. Bir paket delikten düşmek üzereydi. Örümcek Adam paketi elleriyle yakaladı. Sonra çantanın delikli köşesini sıkıca bağladı. Kalan paketleri de odalara tek tek bıraktı. Örümcek Adam çok sevindi, çünkü hiçbir paket yere düşmedi.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "düşen paketi yakaladı"
   - Cümle 0 (plan satırı): «çantada bir delik vardı ve paket kayıyordu | düşen paketi yakaladı ve çantanın delikli köşesini bağladı»
   - Açıklama: Gövdede paket düşmüyor, yalnız düşmek üzereyken yakalanıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi başını gıdıkladı"
   - Cümle 5: «Birden örümcek hissi başını gıdıkladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve hissin baş gıdıklaması mecaz; 3 yaşındaki çocuk anlamaz.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi başını gıdıkladı"
   - Cümle 5: «Birden örümcek hissi başını gıdıkladı.»
   - Açıklama: 'Örümcek hissi başını gıdıkladı' soyut ve mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0119` birebir aynı, ardından `@onarim: aee328e5f7c580668ea9290ce547554ce4fc01ff`, sonra gövde.
