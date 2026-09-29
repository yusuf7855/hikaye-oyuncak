# Editör görevi (onarım): Örümcek Adam, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0002 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0002
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'mercan', fiil 'dökmek', sıfat 'peynirli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar balonu kaçırdı ve balon yüksek bir dala takıldı | dala ağ atıp balonu yavaşça indirdi
@tohum: orumcek_adam-0002
@degisim: mercan -> balon
Örümcek Adam parkta Ghost-Spider için sürpriz bir piknik hazırlıyordu. Ağacın altına büyük bir örtü serdi ve peynirli sandviçleri dizdi. Ama birden rüzgar esti ve kırmızı balon elinden kaçtı. Balon uçtu ve ağacın yüksek bir dalına takıldı. Örümcek Adam dala doğru bir ağ attı. Ağ balonun ipine yapıştı. Örümcek Adam ipi yavaşça çekti ve balon aşağı indi. Sonra ipi örtünün köşesine sıkıca bağladı. Kutudaki kurabiyeleri de bir tabağa döktü. Az sonra arkadaşı havada süzülerek geldi. Örtüyü ve sandviçleri görünce çok şaşırdı. Sonra sevinçle Örümcek Adam'a sarıldı. İki arkadaş kırmızı balonun yanında oturdu ve sandviçlerini mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutudaki kurabiyeleri de bir tabağa döktü"
   - Cümle 9: «Kutudaki kurabiyeleri de bir tabağa döktü.»
   - Açıklama: Kurabiye kutusu sebepsiz beliriyor ve kurabiyeler hikayede hiçbir işe yaramıyor.
   - Açıklama: Kurabiyeler sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0002` birebir aynı, `@degisim: mercan -> balon` (tutuyorsan), ardından `@onarim: f9b0c6979e00b30084decb27a522ad5744d67a5f`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0003 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0003
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'fiyonk', fiil 'yemek', sıfat 'heyecanlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: rüzgar büyük bir dalı piknik masasına düşürdü | dalı kaldıramadı ve güçlü arkadaşından yardım istedi
@tohum: orumcek_adam-0003
Parkta rüzgar sert esiyordu. Örümcek Adam'ın örümcek hissi, piknik masasında bir sorun olduğunu haber verdi. Rüzgar büyük bir dalı kırmış ve dal masanın üstüne düşmüştü. Örümcek Adam, Hulk ile orada piknik yapacaktı ve çok heyecanlıydı. Elindeki fiyonklu kek kutusunu çimenlere bıraktı ve dalı itti. Ama dal çok ağırdı ve hiç kıpırdamadı. Biraz sonra Hulk da masaya geldi. "Hulk, bu dalı kaldırabilir misin?" diye sordu Örümcek Adam. Hulk dalı kolayca kaldırdı ve ağaçların yanına taşıdı. Örümcek Adam kutuyu masaya koydu ve açtı. İki arkadaş keki birlikte yedi. Örümcek Adam çok sevindi, çünkü Hulk'tan yardım istemiş ve pikniği kurtarmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam'ın örümcek hissi"
   - Cümle 2: «Örümcek Adam'ın örümcek hissi, piknik masasında bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve bir hissin haber vermesi soyut ve mecazlı bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi, piknik masasında bir sorun olduğunu haber verdi"
   - Cümle 2: «Örümcek Adam'ın örümcek hissi, piknik masasında bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun' soyut kavram; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0003` birebir aynı, ardından `@onarim: a78f87fea1d1145d7d338f23c2c320fccffc4bf1`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0006 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0006
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'kabak', fiil 'bindirmek', sıfat 'enerjik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: rüzgar kabak resmini uzağa taşıdı ve resim kayboldu | arkadaşından yardım isteyip duvara tırmanarak resmi aldı
@tohum: orumcek_adam-0006
@degisim: bindirmek -> taşımak
Örümcek Adam kumsalda kağıda büyük bir kabak resmi yapmıştı. Birden güçlü bir rüzgar esti ve resmi uzağa taşıdı. Örümcek Adam resmin nereye gittiğini göremedi. Spin de kumsalda oynuyordu. "Spin, resmimi bulmama yardım eder misin?" diye sordu Örümcek Adam. Spin çok enerjikti ve hemen Örümcek Adam'ın yanına koştu. "Resmin kumsaldaki duvarın üstüne düştü, ben gördüm," dedi Spin. Örümcek Adam duvara hızla tırmandı. Kağıdı duvarın üstünden aldı. Sonra kağıdı dikkatle tutarak aşağı indi. Kabak resmi hiç yırtılmamıştı. "Teşekkürler, Spin, kabak resmim yine elimde!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Resmin kumsaldaki duvarın üstüne düştü"
   - Cümle 7: «"Resmin kumsaldaki duvarın üstüne düştü, ben gördüm," dedi Spin.»
   - Açıklama: Kumsaldaki duvar önceden kurulmadan yalnız figürün tırmanma özelliğini kullandırmak için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0006` birebir aynı, `@degisim: bindirmek -> taşımak` (tutuyorsan), ardından `@onarim: 3d424c5b0b65052c49e1a138f4ae690dc202f0b3`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0011 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0011
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'yağ', fiil 'sakinleşmek', sıfat 'yeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: rüzgar topu çiçeklerin arasına yuvarladı ve top kayboldu | eğilen çiçeklerin yanına gidip taşların arasındaki topu buldu
@tohum: orumcek_adam-0011
@degisim: yağ -> top
Rüzgar hafif hafif esiyordu. Örümcek Adam parkta yeşil topuyla oynuyordu. Birden rüzgar topu çiçek bahçesine yuvarladı ve top çiçeklerin arasında kayboldu. Örümcek Adam önce üzüldü, sonra sakinleşti ve çiçeklere baktı. Bir yerde çiçekler yana doğru eğilmişti. Örümcek Adam bunu merak etti ve oraya yavaşça yürüdü. O anda örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam hemen durdu ve ayağının önüne baktı. Yeşil top iki taşın arasına sıkışmıştı. Top yuvarlanırken çiçekleri eğmişti. Örümcek Adam topu taşların arasından dikkatle çıkardı. Örümcek Adam çok sevindi, çünkü kayıp topunu bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 7: «O anda örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatımdır.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuk bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 7: «O anda örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Ortada bir tehlike yokken örümcek hissi sebepsizce devreye girip çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0011` birebir aynı, `@degisim: yağ -> top` (tutuyorsan), ardından `@onarim: b5a354c343e443c062ade8a29eb1a0ef84f63bde`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0012 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | -
@tohum: orumcek_adam-0012
- yer: ev (Takımın gizli evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'bezelye', fiil 'tekrarlamak', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | ev | -
@plan: masanın kenarındaki yamuk saksı kayıp düşecekti | saksıyı yakalayıp masanın ortasına düz koydu
@tohum: orumcek_adam-0012
@degisim: tekrarlamak -> sulamak
Örümcek Adam gizli evde bahçe oyunu oynuyordu. Masanın kenarında yamuk duran bir saksıya bezelye taneleri ekiyordu. Birden örümcek hissi bir sorun olduğunu haber verdi: saksı kayıyordu. Örümcek Adam saksıyı hemen iki eliyle yakaladı. Sonra onu masanın ortasına düz bir şekilde koydu. Artık saksı hiç kaymıyordu. Örümcek Adam toprağa parmağıyla küçük çukurlar açtı. Kalan bezelye tanelerini bu çukurlara tek tek gömdü. Sonra bir bardak suyla toprağı suladı. Toprak güzelce ıslandı. Örümcek Adam bahçe oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi bir sorun olduğunu haber verdi: saksı kayıyordu.»
   - Açıklama: Hissin haber vermesi mecaz ve 'sorun' soyut bir kavram.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve kişileştirilmiş bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0012` birebir aynı, `@degisim: tekrarlamak -> sulamak` (tutuyorsan), ardından `@onarim: 37d0a7285fa192eac5ce38cb330a052ba42a1d1f`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0013 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0013
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gemi', fiil 'tanışmak', sıfat 'yağmurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: büyük bir dalga kumdan gemiye doğru geliyordu | geminin önüne hemen kumdan bir duvar yaptı
@tohum: orumcek_adam-0013
@degisim: tanışmak -> denemek
Örümcek Adam yağmurlu bir sabah kumsala geldi. Suya yakın ıslak kumdan ilk kez büyük bir gemi yapmayı denedi. Birden örümcek hissi, bir dalganın gemiyi yıkacağını haber verdi. Örümcek Adam hemen geminin önüne kumdan uzun bir duvar yaptı. Az sonra dalga kumsala geldi. Su duvara çarptı ve iki yana aktı. Kumdan gemi hiç bozulmadı. Sonra kumdaki küçük bir dalı ona dikti ve direk yaptı. Kenarlarına deniz kabuklarından pencereler koydu. Gemi artık çok güzel görünüyordu. Örümcek Adam çok sevindi, çünkü ilk kumdan gemisini dalgadan korumuştu.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "büyük bir dalga kumdan gemiye doğru geliyordu"
   - Cümle 0 (plan satırı): «büyük bir dalga kumdan gemiye doğru geliyordu | geminin önüne hemen kumdan bir duvar yaptı»
   - Açıklama: Figür büyük bir dalga gelirken suya yakın ıslak kumda kalıp duvar yapıyor; çocuğun taklit edebileceği su kenarı davranışı.
   - Açıklama: Figür büyük bir dalga gelirken su kenarında kalıp önüne duvar yapıyor; çocuk bunu taklit ederek dalganın önünde kalabilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir dalganın gemiyi yıkacağını haber verdi"
   - Cümle 3: «Birden örümcek hissi, bir dalganın gemiyi yıkacağını haber verdi.»
   - Açıklama: Hissin haber vermesi mecazlı bir anlatım.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi, bir dalganın gemiyi yıkacağını haber verdi"
   - Cümle 3: «Birden örümcek hissi, bir dalganın gemiyi yıkacağını haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım, küçük çocuk için uygun değil.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Birden örümcek hissi, bir dalganın"
   - Cümle 3: «Birden örümcek hissi, bir dalganın gemiyi yıkacağını haber verdi.»
   - Açıklama: Özne ile yüklem arasına gereksiz virgül konmuş.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dalı ona dikti"
   - Cümle 8: «Sonra kumdaki küçük bir dalı ona dikti ve direk yaptı.»
   - Açıklama: 'ona' zamirinin gemiyi mi duvarı mı gösterdiği belli değil ve nesneye 'ona dikti' demek yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0013` birebir aynı, `@degisim: tanışmak -> denemek` (tutuyorsan), ardından `@onarim: b4ed71b31689388d0ab23e80f41c73cc1d63a092`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0015 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0015
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'çeşme', fiil 'guruldamak', sıfat 'özel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: bir dalga kumdaki sandviç çantasına doğru geliyordu | koşup çantayı dalga gelmeden kumdan kaldırdı
@tohum: orumcek_adam-0015
Kumsalda Spin'in karnı yüksek sesle guruldadı. Spin sandviç çantasını suya yakın bıraktı ve Örümcek Adam ile çeşmeye yürüdü. Birden Örümcek Adam'ın örümcek hissi, bir dalganın çantayı ıslatacağını haber verdi. Çantada Spin'in yaptığı özel sandviçler vardı. Örümcek Adam hemen koştu ve çantayı kumdan kaldırdı. Tam o sırada dalga geldi ve o yeri ıslattı. Ama sandviçler kuru kaldı. Örümcek Adam çantayı Spin'e verdi. İki arkadaş ellerini çeşmede yıkadı ve kuma oturdu. Spin sandviçlerden birini Örümcek Adam'a uzattı. "Teşekkürler, Örümcek Adam, sandviçler ıslanmadı!" dedi Spin.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi, bir dalganın çantayı ıslatacağını haber verdi"
   - Cümle 3: «Birden Örümcek Adam'ın örümcek hissi, bir dalganın çantayı ıslatacağını haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam hemen koştu ve çantayı kumdan kaldırdı"
   - Cümle 5: «Örümcek Adam hemen koştu ve çantayı kumdan kaldırdı.»
   - Açıklama: Dalga gelirken su kenarına koşup eşya kurtarmak çocuğun taklit edebileceği tehlikeli bir davranıştır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0015` birebir aynı, ardından `@onarim: 1a32c108d231767140b28c115b0f96176169a0d8`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0017 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0017
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: kaybolan eşya
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'saksı', fiil 'binmek', sıfat 'dikkatli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar topu yuvarladı ve top kayboldu | topu dikenli güllerin arasında bulup ağla dikkatlice çekti
@tohum: orumcek_adam-0017
@degisim: binmek -> yuvarlanmak
Örümcek Adam ile Ghost-Spider parkta kırmızı bir topla oynuyordu. Birden rüzgar esti ve top çimenlerin üstünde hızla yuvarlandı. İkisi topun peşinden koştu ama onu hiçbir yerde bulamadı. "Topumuz nereye gitti?" diye sordu arkadaşı. Örümcek Adam çiçek bahçesine baktı. Top, büyük bir saksının içindeki dikenli güllerin arasına girmişti. "Dikenlere dokunmayalım," dedi Örümcek Adam. Sonra topa bir ağ attı. Ağ topa yapıştı ve Örümcek Adam ağı dikkatli bir şekilde çekti. Top güllerin arasından çıktı ve hiçbir dal kırılmadı. Arkadaşı sevinçle ellerini çırptı. İki arkadaş top oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "diye sordu arkadaşı"
   - Cümle 4: «"Topumuz nereye gitti?" diye sordu arkadaşı.»
   - Açıklama: Konuşan 'arkadaşı' diye anılıyor; iki kişi de birbirinin arkadaşı olduğundan kimin sorduğu belli değil.
   - Açıklama: Soruyu soran adıyla belirtilmemiş; 'arkadaşı' ile kimin kastedildiği belirsiz.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "büyük bir saksının içindeki dikenli güllerin arasına girmişti"
   - Cümle 6: «Top, büyük bir saksının içindeki dikenli güllerin arasına girmişti.»
   - Açıklama: Çimende yuvarlanan topun büyük bir saksının içine girmesi akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0017` birebir aynı, `@degisim: binmek -> yuvarlanmak` (tutuyorsan), ardından `@onarim: af7bd1f799dc43d23530d9b8c46a6cb87f80f0cb`, sonra gövde.
