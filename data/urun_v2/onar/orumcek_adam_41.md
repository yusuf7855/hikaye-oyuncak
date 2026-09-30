# Editör görevi (onarım): Örümcek Adam, onarım partisi 41

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar41.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar41.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0169 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0169
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'süt', fiil 'inanmak', sıfat 'tertemiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: uçurtmanın ipi yüksek bir duvarın tepesine takıldı | duvara tırmandı ve arkadaşından ipi tutmasını istedi
@tohum: orumcek_adam-0169
@degisim: süt -> uçurtma
Bir sabah Örümcek Adam ile Spin parkta uçurtma uçuruyordu. Gökyüzü tertemizdi ama rüzgar birden sert esti. Uçurtmanın ipi, çiçek bahçesinin yüksek duvarına takıldı. Örümcek Adam duvara kolayca tırmandı. Ama uçurtma rüzgarda çekince ip yine takılıyordu. "Spin, ipin ucunu aşağıdan sıkıca tutar mısın?" diye sordu Örümcek Adam. Spin ipin ucunu iki eliyle tuttu. Örümcek Adam ipi duvardan yavaşça çözdü. Uçurtma yeniden yükseldi. Spin buna önce inanamadı, sonra sevinçle güldü. Örümcek Adam aşağı indi ve Spin'in yanına geldi. "Teşekkürler, Spin, uçurtmayı birlikte kurtardık!" dedi Örümcek Adam.
```

**Hakem bulguları (3):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Uçurtmanın ipi, çiçek bahçesinin"
   - Cümle 3: «Uçurtmanın ipi, çiçek bahçesinin yüksek duvarına takıldı.»
   - Açıklama: Özneden sonra gereksiz virgül konmuş.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvara kolayca tırmandı"
   - Cümle 4: «Örümcek Adam duvara kolayca tırmandı.»
   - Açıklama: Yüksek bahçe duvarına tırmanma süper güç olarak işaretlenmeden 'kolayca' anlatılıyor; güvenli özellik kullanımı satırına göre çocuğun taklit edebileceği bir yükseğe tırmanma örneği olabilir.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama uçurtma rüzgarda çekince ip yine takılıyordu"
   - Cümle 5: «Ama uçurtma rüzgarda çekince ip yine takılıyordu.»
   - Açıklama: 'Çekmek' nesnesiz ve belirsiz kullanılmış; uçurtmanın neyi çektiği anlaşılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0169` birebir aynı, `@degisim: süt -> uçurtma` (tutuyorsan), ardından `@onarim: fb3aea1a9b6539e180d956a126fd1c4a55270d67`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0170 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0170
- yer: ev (Takımın gizli evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'silgi', fiil 'kapanmak', sıfat 'yeni'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: kutu küçüktü ve kapağı kapanmıyordu | kutuyu ağla sardı ve kapağı kapattı
@tohum: orumcek_adam-0170
@degisim: silgi -> kutu
Örümcek Adam gizli evde arkadaşı için yeni davul çubukları paketliyordu. Ama kutu küçüktü ve kapağı kapanmıyordu. Örümcek Adam kapağı bastırdı ama kapak yine açıldı. Sonra ağını attı ve kutuyu ağla sardı. Ağ kapağı sıkıca tuttu ve kutu kapandı. Beyaz ağ, kutunun üstünde bir kurdele gibi duruyordu. Az sonra Ghost-Spider gizli eve geldi. Örümcek Adam kutuyu ona uzattı. O da ağı çözdü ve yeni çubukları gördü. Hemen davulunu çalmaya başladı. Örümcek Adam ellerini çırparak onu dinledi. Örümcek Adam bundan sonra bütün hediyeleri ağla paketledi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kurdele gibi duruyordu"
   - Cümle 6: «Beyaz ağ, kutunun üstünde bir kurdele gibi duruyordu.»
   - Açıklama: Benzetme ve 'kurdele' kelimesi 3 yaşındaki çocuk için soyut ve zor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O da ağı çözdü"
   - Cümle 9: «O da ağı çözdü ve yeni çubukları gördü.»
   - Açıklama: 'O' zamirinin Örümcek Adam'ı mı Ghost-Spider'ı mı gösterdiği belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bütün hediyeleri ağla paketledi"
   - Cümle 12: «Örümcek Adam bundan sonra bütün hediyeleri ağla paketledi.»
   - Açıklama: Tohumdaki ağ özelliği bir kez yerine sürekli bir alışkanlık olarak yeniden kullanılıyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Örümcek Adam bundan sonra bütün hediyeleri ağla paketledi"
   - Cümle 12: «Örümcek Adam bundan sonra bütün hediyeleri ağla paketledi.»
   - Açıklama: Son cümle olaydan çıkan sıcak bir kapanış ya da ders değil, çıplak bir alışkanlık bildirimi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0170` birebir aynı, `@degisim: silgi -> kutu` (tutuyorsan), ardından `@onarim: 8352105fc71ed4df4f443e93ae42912a5bc4be75`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0171 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0171
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'sebze', fiil 'sevmek', sıfat 'meraklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar büyük bir topu yeni çiçeklere doğru yuvarladı | koşup topu çiçeklerin önünde tuttu
@tohum: orumcek_adam-0171
@degisim: sebze -> çiçek
Örümcek Adam parkta Ghost-Spider ile çiçek dikiyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Rüzgar büyük bir topu yeni çiçeklere doğru yuvarlıyordu. Arkadaşı topu görmemişti. Örümcek Adam hemen koştu ve topu çiçeklerin önünde tuttu. "Çok sevdiğim çiçeklerim kurtuldu!" dedi arkadaşı. Sonra meraklı meraklı topun nereden geldiğini sordu. Örümcek Adam ona oyun alanını gösterdi. Sonra topu oyun alanına geri götürdü. Örümcek Adam ile arkadaşı kalan çiçekleri birlikte mutlu mutlu dikti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Bir hissin haber vermesi mecazdır ve 'his', 'sorun' 3 yaşındaki çocuk için soyut kelimelerdir.
   - Açıklama: Soyut 'örümcek hissi' kişileştirilip haber veren özne yapılmış.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Sonra meraklı meraklı topun"
   - Cümle 7: «Sonra meraklı meraklı topun nereden geldiğini sordu.»
   - Açıklama: 'Meraklı meraklı' Türkçede yerleşik bir ikileme değildir; 'merakla' olmalı.
   - Açıklama: 'Meraklı meraklı' doğru bir ikileme değil; 'merakla' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0171` birebir aynı, `@degisim: sebze -> çiçek` (tutuyorsan), ardından `@onarim: 313af1b68a94c3dc8767cfd626bee8190ed8d4e8`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0172 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0172
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'armut', fiil 'rahatlatmak', sıfat 'simsiyah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: dalga kovayı simsiyah kayaların arasına sürükledi | kaygan kayalara basmadı ve arkadaşından yardım istedi
@tohum: orumcek_adam-0172
@degisim: armut -> kova
Kumsalda serin bir rüzgar esiyordu. Örümcek Adam ile Hulk kovayla kumdan kule yapma oyunu oynuyordu. Ama bir dalga geldi ve kovayı simsiyah kayaların arasına sürükledi. Örümcek Adam kayalara doğru bir adım attı. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Islak kayalar çok kaygandı. Örümcek Adam kuma geri döndü. "Hulk, kumda durup kovaya uzanır mısın?" diye sordu Örümcek Adam. Hulk kumda durdu ve kocaman koluyla kovayı kolayca aldı. Kovayı yeniden görmek ikisini de çok rahatlattı. Örümcek Adam çok sevindi, çünkü kovayı kayalara basmadan kurtarmışlardı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 5: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'haber verdi' soyut ve mecazlı bir anlatım; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi haber verdi' mecaz ve soyut bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kovayı yeniden görmek ikisini de çok rahatlattı"
   - Cümle 10: «Kovayı yeniden görmek ikisini de çok rahatlattı.»
   - Açıklama: Eylemi özne yapan soyut yapı küçük çocuk için ağır; 'İkisi de rahatladı' daha somut olurdu.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ikisini de çok rahatlattı"
   - Cümle 10: «Kovayı yeniden görmek ikisini de çok rahatlattı.»
   - Açıklama: 'Rahatlattı' soyut bir duygu kavramı; somut anlatım yerine soyut özne kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0172` birebir aynı, `@degisim: armut -> kova` (tutuyorsan), ardından `@onarim: 6974458b39ab181902b45db7ada620cd16eec4c2`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0173 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0173
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'çanta', fiil 'okumak', sıfat 'ağır'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: ağır çanta iki kayanın arasına düştü | ağ atıp çantayı dışarı çekti
@tohum: orumcek_adam-0173
Rüzgar esiyordu ve Örümcek Adam ile Spin kumsalda yürüyordu. Spin'in çantası ağırdı, Spin onu bir kayanın üstüne koydu. Ama çanta kaydı ve iki kayanın arasına düştü. Kayaların arası çok dardı. Spin elini uzattı ama çantaya yetişemedi. "Kitabım orada, onu sana okumak istiyordum," dedi Spin. "Üzülme, Spin, ben onu çıkarırım," dedi Örümcek Adam. Örümcek Adam ince bir ağ attı. Ağ çantaya yapıştı. Örümcek Adam ağı yavaşça çekti ve çantayı dışarı çıkardı. Spin çantayı aldı ve sevinçle güldü. Sonra ikisi kumun üstüne oturdu ve kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Spin'in çantası ağırdı, Spin onu"
   - Cümle 2: «Spin'in çantası ağırdı, Spin onu bir kayanın üstüne koydu.»
   - Açıklama: Aynı cümlede Spin adı gereksiz yere iki kez tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0173` birebir aynı, ardından `@onarim: 45df543f1835ac9b02d425bacca7955df141960c`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0174 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0174
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'pul', fiil 'doğmak', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar ipi kopardı ve uçurtma uçup gitti | parlayan pulları görüp uçurtmayı ağla indirdi
@tohum: orumcek_adam-0174
Örümcek Adam, güneş doğarken kumsalda uçurtma uçuruyordu. Uçurtmanın uzun kuyruğunda parlak pullar vardı. Birden sert bir rüzgar esti ve uçurtmanın ipi koptu. Uçurtma limana doğru uçup gitti. Örümcek Adam hemen limana koştu ve etrafına baktı. Yüksek bir direğin tepesinde parlak pullar gördü. Uçurtma o direğe takılmıştı. Örümcek Adam direğin tepesine bir ağ attı. Ağ uçurtmaya yapıştı ve Örümcek Adam onu yavaşça aşağı çekti. Sonra kopan ipin iki ucunu sıkıca bağladı. Kumsala döndü ve uçurtmayı yeniden havaya bıraktı. Uçurtma yine yükseldi ve Örümcek Adam oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Örümcek Adam hemen limana koştu"
   - Cümle 5: «Örümcek Adam hemen limana koştu ve etrafına baktı.»
   - Açıklama: Hikaye kumsaldan limana geçip yeniden kumsala dönüyor; tek sahne kuralı çiğneniyor.
   - Açıklama: Hikaye kumsaldan limana geçip kumsala dönüyor; tek sahne kuralı çiğneniyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kopan ipin iki ucunu sıkıca bağladı"
   - Cümle 10: «Sonra kopan ipin iki ucunu sıkıca bağladı.»
   - Açıklama: Çözüm limana koşma, ağla indirme, ipi bağlama ve kumsala dönme gibi ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0174` birebir aynı, ardından `@onarim: 31cc1c2530c30d73b01a55e3ccef6b4bfb1b51a1`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0176 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0176
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'bisiklet', fiil 'hızlanmak', sıfat 'ilginç'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: bisikletin tekerleğine küçük bir kabuk sıkıştı | sesi duyup durdu ve kabuğu çıkardı
@tohum: orumcek_adam-0176
Kumsalın yanındaki yolda Örümcek Adam bisiklet sürüyordu. Dalgalarla yarışıyordu ve her dalga gelince hızlanıyordu. Birden ön tekerleğin tellerine küçük bir kabuk sıkıştı. Tekerlekten ilginç bir tık tık sesi gelmeye başladı. Örümcek hissi de ona bir sorun olduğunu haber verdi. Örümcek Adam hemen yavaşladı ve bisikletten indi. Tekerleğe eğildi ve kabuğu gördü. Kabuğu parmaklarıyla dikkatle çekip çıkardı. Tekerleği elle çevirdi ve ses kesildi. Örümcek Adam bisikletine yeniden bindi ve yarışa devam etti. Yeni bir dalga geldi ve Örümcek Adam onu yine geçti. Örümcek Adam çok sevindi, çünkü bisikleti artık sessizce gidiyordu.
```

**Hakem bulguları (5):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "Kumsalın yanındaki yolda Örümcek Adam"
   - Cümle 1: «Kumsalın yanındaki yolda Örümcek Adam bisiklet sürüyordu.»
   - Açıklama: Deniz yerinin tarifi şehrin kumsalı ve limanı iken olay kumsalın yanındaki bir yolda geçiyor.
   - Açıklama: Kartın deniz tarifi şehrin kumsalı ve limanı; kumsalın yanındaki yol tarifin dışında.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "her dalga gelince hızlanıyordu"
   - Cümle 2: «Dalgalarla yarışıyordu ve her dalga gelince hızlanıyordu.»
   - Açıklama: Su kenarındaki yolda dalgalarla yarışıp bisikletle hızlanmak çocuğun taklit edebileceği riskli bir davranış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ilginç bir tık tık sesi"
   - Cümle 4: «Tekerlekten ilginç bir tık tık sesi gelmeye başladı.»
   - Açıklama: 'İlginç' soyut bir sıfat; 3 yaşındaki çocuk için 'garip' ya da 'yeni' daha somut olur.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Tekerlekten ilginç bir tık tık sesi"
   - Cümle 4: «Tekerlekten ilginç bir tık tık sesi gelmeye başladı.»
   - Açıklama: Sorun yalnız ilginç bir ses; çocuğun önemseyeceği bir sorun kurulmuyor ve kabuğun yola nasıl geldiği söylenmiyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi de ona bir sorun olduğunu haber verdi"
   - Cümle 5: «Örümcek hissi de ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber veren bir kişi gibi anlatılıyor; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber vermesi mecaz; 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0176` birebir aynı, ardından `@onarim: e4a2ac0aa122e3384397ee045ec91e1abd8cbbe3`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0177 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0177
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'pasta', fiil 'yazmak', sıfat 'yakın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: yakındaki kayalardan garip bir ses geldi | sesi arayıp kayığı buldu ve ipini bağladı
@tohum: orumcek_adam-0177
@degisim: yazmak -> bağlamak
Kumsalda Örümcek Adam ile Hulk piknik yapıyordu. Hulk büyük bir çilekli pasta getirmişti. Birden yakındaki kayalardan garip bir tak tak sesi geldi. "Belki bu dalgaların sesi," dedi Hulk. Ama Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. İkisi hemen kayaların arkasına baktı. Küçük bir kayığın ipi direkten çözülmüştü. Dalgalar kayığı kayalara çarpıyordu. Hulk kayığı ipinden çekip kıyıya getirdi. Örümcek Adam ipi direğe iki kez sıkıca bağladı. Kayık durdu ve tak tak sesi kesildi. "Hadi, şimdi pasta yiyelim," dedi Örümcek Adam. Örümcek Adam çok mutluydu, çünkü sesin nereden geldiğini bulmuş ve kayığı kurtarmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 5: «Ama Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve hissin haber vermesi mecaz; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' ve 'haber vermek' soyut ve mecazlı; 3 yaşındaki çocuk anlamaz.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Hulk kayığı ipinden çekip kıyıya getirdi"
   - Cümle 9: «Hulk kayığı ipinden çekip kıyıya getirdi.»
   - Açıklama: Kayığı kurtaran asıl adımı yan karakter Hulk atıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0177` birebir aynı, `@degisim: yazmak -> bağlamak` (tutuyorsan), ardından `@onarim: 7e287ebb262341b36e1edbe18cec898be01e4ecc`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0178 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0178
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'buket', fiil 'sürmek', sıfat 'patlak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: bisiklet ipe takıldı ve balonlar ağaca uçtu | özür diledi ve ağla balonları indirdi
@tohum: orumcek_adam-0178
@degisim: patlak -> yavaş
Örümcek Adam parkta bisikletini çok hızlı sürüyordu. Spin'in renkli balon buketi bir banka bağlıydı. Örümcek Adam önüne bakmadı ve bisikleti balonların ipine takıldı. İp çözüldü ve balonlar yüksek bir ağacın dallarına uçtu. Spin ağaca baktı ve çok üzüldü. Örümcek Adam bisikletten indi ve Spin'den özür diledi. Sonra ağaca doğru bir ağ attı. Ağ balonların iplerine yapıştı. Örümcek Adam balonları yavaşça aşağı çekti ve Spin'e verdi. Spin gülümsedi ve ona teşekkür etti. Örümcek Adam bisikletini bu kez yavaş yavaş sürdü. İkisi balonlarla parkta mutlu mutlu dolaştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "renkli balon buketi"
   - Cümle 2: «Spin'in renkli balon buketi bir banka bağlıydı.»
   - Açıklama: 'Buket' kelimesini 3 yaşındaki bir çocuk bilmeyebilir; 'balonlar' yeterliydi.
   - Açıklama: 'Buket' kelimesini 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0178` birebir aynı, `@degisim: patlak -> yavaş` (tutuyorsan), ardından `@onarim: 1bc07f3264f586fb6245fb0864aa02efd2ee56b3`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0179 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0179
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'fıçı', fiil 'yıkanmak', sıfat 'sevecen'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: yağmur suyu fıçıyı doldurmuştu | suyu döktü ve topu içine attı
@tohum: orumcek_adam-0179
@degisim: sevecen -> boş
Yağmur yağdı ve parktaki çiçekler güzelce yıkandı. Örümcek Adam parkta topu tahta bir fıçının içine atma oyunu oynuyordu. Tam topu atarken örümcek hissi bir sorun olduğunu haber verdi. Örümcek Adam fıçının içine baktı. Fıçı yağmur suyuyla dolmuştu. Top suya düşerse ıslanırdı. Örümcek Adam fıçıyı yavaşça yana yatırdı. Su çiçek bahçesine doğru aktı. Örümcek Adam boş fıçıyı yeniden yerine koydu. Sonra topu attı ve top tam fıçının içine düştü. Örümcek Adam çok sevindi, çünkü topu kuru kalmıştı ve oyunu devam ediyordu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 3: «Tam topu atarken örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Fıçı yağmur suyuyla dolmuştu"
   - Cümle 5: «Fıçı yağmur suyuyla dolmuştu.»
   - Açıklama: İlk üç cümlede yalnız bir sorun olduğu söyleniyor; sorunun ne olduğu ancak 5. cümlede açıklanıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Top suya düşerse ıslanırdı"
   - Cümle 6: «Top suya düşerse ıslanırdı.»
   - Açıklama: Sorun yalnız varsayımsal ve topun ıslanması çocuk için önemsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0179` birebir aynı, `@degisim: sevecen -> boş` (tutuyorsan), ardından `@onarim: 4fc37e2c37f42ced53f80f1ac2943d578700d6b5`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0181 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | -
@tohum: orumcek_adam-0181
- yer: ev (Takımın gizli evi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'çikolata', fiil 'seyretmek', sıfat 'sabırsız'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | -
@plan: mutfaktan ilginç bir tıp tıp sesi geldi | sesi dinleyip açık pencereyi kapattı
@tohum: orumcek_adam-0181
Dışarıda yağmur yağıyordu ve rüzgar esiyordu. Örümcek Adam gizli evde oturmuş, yağmuru seyrediyordu. Birden mutfaktan ilginç bir tıp tıp sesi geldi. Örümcek hissi de bir sorun olduğunu haber verdi. Örümcek Adam sabırsızdı ve hemen mutfağa koştu. Ama acele edince sesin nereden geldiğini bulamadı. Sonra sessizce durdu ve dinledi. Ses küçük pencereden geliyordu. Rüzgar pencereyi açmıştı ve yağmur damlaları içeri giriyordu. Damlalar, pencerenin önündeki çikolata kutusunun üstüne düşüyordu. Örümcek Adam kutuyu kuru bir yere koydu ve pencereyi kapattı. Örümcek Adam bundan sonra bir ses duyunca önce durup dinledi.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Adam gizli evde oturmuş"
   - Cümle 2: «Örümcek Adam gizli evde oturmuş, yağmuru seyrediyordu.»
   - Açıklama: İyelik eki eksik; 'gizli evinde' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ilginç bir tıp tıp sesi"
   - Cümle 3: «Birden mutfaktan ilginç bir tıp tıp sesi geldi.»
   - Açıklama: 'İlginç' küçük bir çocuk için soyut bir sıfat.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi de bir sorun olduğunu haber verdi"
   - Cümle 4: «Örümcek hissi de bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve bir hissin 'haber vermesi' soyut ve mecazlı bir anlatım, 3 yaşındaki bir çocuk bunu anlamaz.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Örümcek hissi de bir sorun olduğunu haber verdi"
   - Cümle 4: «Örümcek hissi de bir sorun olduğunu haber verdi.»
   - Açıklama: Ses zaten duyulmuşken örümcek hissi işe yaramayan bir tekrar olarak geçiyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Örümcek Adam sabırsızdı ve hemen mutfağa koştu"
   - Cümle 5: «Örümcek Adam sabırsızdı ve hemen mutfağa koştu.»
   - Açıklama: Tohumdaki özellik örümcek hissi iken sabırsızlık ikinci bir özellik olarak ekleniyor ve sorunu örümcek hissi değil dinlemek çözüyor.
   - Açıklama: Tohumdaki özellik örümcek hissi; sabırsızlık ve dinleme ikinci bir özellik olarak eklenip sorunu o çözüyor.
6. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Damlalar, pencerenin önündeki"
   - Cümle 10: «Damlalar, pencerenin önündeki çikolata kutusunun üstüne düşüyordu.»
   - Açıklama: Özneden sonra gereksiz virgül konmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0181` birebir aynı, ardından `@onarim: fa1977efc6634d6c5527203452a0c890a392b4e6`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0183 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0183
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: paylaşmak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kabuk', fiil 'koşturmak', sıfat 'şanslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: arkadaşının kovası delikti ve kabuklar düşüyordu | düşen kabukları görüp kendi kovasını paylaştı
@tohum: orumcek_adam-0183
Kumsalda Örümcek Adam ile Spin kabuk topluyordu. İkisi oradan oraya koşturuyordu. Ama Spin'in kovasının dibinde küçük bir delik vardı ve kabuklar düşüyordu. Spin bunu görmedi. Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. Örümcek Adam arkasına döndü ve kumdaki kabukları gördü. "Spin, kovanda delik var, kabukların düşüyor!" dedi Örümcek Adam. Spin kovasına baktı ve üzüldü. "Benim kovam sağlam, birlikte kullanalım," dedi Örümcek Adam. İkisi düşen kabukları topladı ve hepsini aynı kovaya koydu. "Ne şanslıyım, sen benim arkadaşımsın," dedi Spin. Örümcek Adam çok sevindi, çünkü kovasını paylaşınca bütün kabuklar bir arada kaldı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 5: «Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: Bir hissin haber vermesi mecazdır ve 'his', 'sorun' 3 yaşındaki çocuk için soyut kelimelerdir.
   - Açıklama: 'Örümcek hissi' ve 'haber vermek' soyut ve mecazlı, küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ne şanslıyım, sen"
   - Cümle 11: «"Ne şanslıyım, sen benim arkadaşımsın," dedi Spin.»
   - Açıklama: 'Şanslı' soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0183` birebir aynı, ardından `@onarim: 3a3ef78920839d1108ffd9815247c17fa8ea7580`, sonra gövde.
