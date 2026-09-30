# Editör görevi (onarım): Örümcek Adam, onarım partisi 35

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar35.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar35.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0145 (deneme 1 -> 2)

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
@plan: arkadaşı yiyeceğini unutmuştu ve açtı | gevreği ikiye böldü ve onunla paylaştı
@tohum: orumcek_adam-0145
Örümcek Adam parkta bir bankta oturup gevrek yiyordu. Birden örümcek hissi bir sorun olduğunu ona haber verdi. Ağacın altında Ghost-Spider aç ve üzgündü, çünkü yiyeceğini gizli evde unutmuştu. Önündeki kutu açıktı ve içi boştu. Örümcek Adam elindeki gevreği ikiye böldü. Sonra arkadaşının yanına gitti. "Bunun yarısı senin," dedi Örümcek Adam. Arkadaşı gevreği aldı ve "Çok teşekkür ederim!" dedi. İkisi onu ağacın altında birlikte yedi. Gevrek sıcak ve çıtır çıtırdı. Arkadaşı artık aç değildi ve çok mutluydu. Örümcek Adam bundan sonra yiyeceğini arkadaşlarıyla hep paylaştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "unutmuştu ve açtı"
   - Cümle 0 (plan satırı): «arkadaşı yiyeceğini unutmuştu ve açtı | gevreği ikiye böldü ve onunla paylaştı»
   - Açıklama: Plandaki 'açtı' hem 'aç idi' hem 'bir şeyi açtı' diye okunabiliyor, anlam belirsiz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu ona haber verdi"
   - Cümle 2: «Birden örümcek hissi bir sorun olduğunu ona haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatımdır.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Önündeki kutu açıktı ve içi boştu"
   - Cümle 4: «Önündeki kutu açıktı ve içi boştu.»
   - Açıklama: Yiyeceği evde unutulmuşken önünde açık ve boş bir kutu sebepsiz beliriyor ve hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0145` birebir aynı, ardından `@onarim: e75e97e4dc4301bbfccb499e54e45e892831e392`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0146 (deneme 1 -> 2)

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
@plan: çember yumuşak toprağa battı ve çıkmadı | duvara tırmanıp güçlü arkadaşından yardım istedi
@tohum: orumcek_adam-0146
@degisim: biberli -> kırmızı
Bir sabah Örümcek Adam parkta kırmızı çemberiyle oynuyordu. Çember çiçek bahçesine yuvarlandı ve toprağa battı. Toprak sulandığı için çok yumuşamıştı. Örümcek Adam çemberi iki eliyle çekti ama çıkaramadı. Hulk'ı bulmak için bahçenin duvarına hızla tırmandı. Oradan Hulk'ı oyun alanında gördü. "Hulk, bana yardım eder misin?" diye seslendi Örümcek Adam. Hulk hemen koşup geldi. Kocaman eliyle çemberi tuttu ve kolayca çıkardı. Sonra çemberi Örümcek Adam'a verdi. Örümcek Adam çok sevindi, çünkü Hulk'tan yardım isteyerek çemberini kurtarmıştı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Toprak sulandığı için çok yumuşamıştı"
   - Cümle 3: «Toprak sulandığı için çok yumuşamıştı.»
   - Açıklama: Yuvarlanan bir çemberin yumuşak toprağa batıp çıkmaması akla yatkın değil; yumuşak toprak çekmeyi zorlaştırmaz, kolaylaştırır.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bahçenin duvarına hızla tırmandı"
   - Cümle 5: «Hulk'ı bulmak için bahçenin duvarına hızla tırmandı.»
   - Açıklama: Güvenli kullanım satırına göre tırmanma yalnız süper güç olarak anlatılmalı; burada bahçe duvarına hızla tırmanmak çocuğun taklit edebileceği biçimde veriliyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bahçenin duvarına hızla tırmandı"
   - Cümle 5: «Hulk'ı bulmak için bahçenin duvarına hızla tırmandı.»
   - Açıklama: Tohumdaki tırmanma özelliği sorunu çözmüyor; çemberi Hulk çıkarıyor, tırmanma yalnız arkadaşı görmek için süs olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0146` birebir aynı, `@degisim: biberli -> kırmızı` (tutuyorsan), ardından `@onarim: 0c41df924192991c9837a503f7bc59358eeda954`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0147 (deneme 1 -> 2)

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
Parkta ince bir ses duyuluyordu. Örümcek Adam ile Ghost-Spider sesin nereden geldiğini merak etti. Ses yüksek bir duvarın tepesinden geliyordu ama yerden bir şey görünmüyordu. "Orada ne var, Örümcek Adam?" diye sordu konuşkan arkadaşı. "Ben bakarım," dedi Örümcek Adam. Duvara hızla tırmandı ve tepeye çıktı. Tepede ipi takılmış mavi bir balon vardı. Rüzgar esince balon duvara değiyor ve ses çıkarıyordu. Örümcek Adam ipi dikkatle çözdü ve balonla aşağı indi. Balon tozluydu ve Örümcek Adam onu eliyle ovdu. "Demek ses balondan geliyormuş!" dedi arkadaşı ve güldü. Örümcek Adam ve arkadaşı çok sevindi, çünkü sesi yapan balonu bulmuşlardı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "diye sordu konuşkan arkadaşı"
   - Cümle 4: «"Orada ne var, Örümcek Adam?" diye sordu konuşkan arkadaşı.»
   - Açıklama: Ghost-Spider adıyla tanıtıldıktan sonra 'konuşkan arkadaşı' diye yeniden tanıtılıyor ve kim olduğu belirsizleşiyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "diye sordu konuşkan arkadaşı"
   - Cümle 4: «"Orada ne var, Örümcek Adam?" diye sordu konuşkan arkadaşı.»
   - Açıklama: Ghost-Spider'a kartın ilişki alanında olmayan 'konuşkan' huyu yakıştırılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Balon tozluydu ve Örümcek Adam onu eliyle ovdu"
   - Cümle 10: «Balon tozluydu ve Örümcek Adam onu eliyle ovdu.»
   - Açıklama: Balonun tozlu olması ve ovulması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Balonun tozlu olması ve ovulması olayda hiçbir işe yaramayan ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0147` birebir aynı, `@degisim: kravat -> balon` (tutuyorsan), ardından `@onarim: 078f3ad961c8fd20825d3893a7eefb962081534c`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0148 (deneme 1 -> 2)

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
Örümcek Adam, Spin'e sürpriz olsun diye parka yeni bir uçurtma getirdi. Birden örümcek hissi bir sorun olduğunu ona haber verdi. Sert bir rüzgar esti ve uçurtma banktan uçmaya başladı. Örümcek Adam hemen döndü ve uçurtmanın kuyruğunu yakaladı. Sonra uçurtmaya yanındaki kalın ipi sıkıca bağladı. Az sonra Spin parka geldi. "Bu uçurtma senin için, Spin," dedi Örümcek Adam. "Çok güzel, teşekkür ederim!" dedi Spin sevinçle. İki arkadaş ipi birlikte tuttu. Uçurtma rüzgarla gökyüzüne uçtu. Spin mutlu mutlu güldü. Örümcek Adam bundan sonra rüzgarlı havada uçurtmaya hep önce ip bağladı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu ona haber verdi"
   - Cümle 2: «Birden örümcek hissi bir sorun olduğunu ona haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber veren bir özne gibi mecazlı kullanılmış.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuk için anlaşılmaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi bir sorun"
   - Cümle 2: «Birden örümcek hissi bir sorun olduğunu ona haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "uçurtmaya yanındaki kalın ipi"
   - Cümle 5: «Sonra uçurtmaya yanındaki kalın ipi sıkıca bağladı.»
   - Açıklama: Çözümü getiren kalın ip önceden kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0148` birebir aynı, `@degisim: flüt -> uçurtma` (tutuyorsan), ardından `@onarim: cff2cf71486bc08b5ef515ea6f31d8318735899a`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0149 (deneme 1 -> 2)

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
Parkta, çiçek bahçesinin yanında, Örümcek Adam Hulk'a bir sürpriz hazırlıyordu. Eski bir masaya kocaman, süslü bir salata koydu ama masa sallanıyordu. Birden örümcek hissi bir sorun olduğunu ona haber verdi. Salata kabı masanın kenarına kaymıştı ve düşmek üzereydi. Örümcek Adam hemen uzandı ve kabı tuttu. Sonra masanın kısa ayağının altına düz bir taş koydu. Masa artık hiç sallanmıyordu. Az sonra Hulk geldi. "Bu salata senin için, Hulk!" dedi Örümcek Adam. "Ne güzel bir sürpriz!" dedi Hulk ve güldü. İkisi masaya oturup salatayı birlikte yedi. Örümcek Adam çok mutluydu, çünkü sürprizini kurtarmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu ona haber verdi"
   - Cümle 3: «Birden örümcek hissi bir sorun olduğunu ona haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber veren özne gibi mecazlı kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çünkü sürprizini kurtarmıştı"
   - Cümle 12: «Örümcek Adam çok mutluydu, çünkü sürprizini kurtarmıştı.»
   - Açıklama: 'Sürprizini kurtarmak' mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Sürprizini kurtarmak' mecazlı ve soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0149` birebir aynı, ardından `@onarim: b84f471160d27a156ab040748450bb27d489498d`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0150 (deneme 1 -> 2)

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
Örümcek Adam ile Spin gizli evde tahta küplerle kule yapıyordu. İkisi de aynı anda bir küp eklemek istedi. Elleri çarpıştı ve kule sallanmaya başladı. Birden örümcek hissi bir sorun olduğunu Örümcek Adam'a haber verdi. Örümcek Adam elini hemen çekti ve kuleyi iki yandan tuttu. Kule yıkılmadı. "Sırayla koyalım, Spin," dedi Örümcek Adam. "Olur, önce sen koy," dedi Spin. Örümcek Adam kırmızı bir küpü yavaşça kulenin üstüne koydu. Sonra Spin mavi bir küp ekledi. Kule yavaş yavaş yükseldi ve ikisi de artık çok rahattı. Örümcek Adam çok sevindi, çünkü sırayla oynayınca kuleleri yıkılmamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu"
   - Cümle 4: «Birden örümcek hissi bir sorun olduğunu Örümcek Adam'a haber verdi.»
   - Açıklama: 'Örümcek hissinin haber vermesi' soyut ve mecazlı bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi bir sorun olduğunu"
   - Cümle 4: «Birden örümcek hissi bir sorun olduğunu Örümcek Adam'a haber verdi.»
   - Açıklama: Bir hissin haber vermesi soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0150` birebir aynı, `@degisim: yaprak -> küp` (tutuyorsan), ardından `@onarim: d26700acaa48e3cec73425f644f6961fe9331897`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0151 (deneme 1 -> 2)

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
Gizli evde yağmurlu bir sabah Hulk, Örümcek Adam ile görüşmeye gelmişti. İki arkadaş yastıklarla yerde farklı bir kale yaptı. Ama rüzgar yukarıdaki küçük pencereyi açtı ve yağmur içeri girip kaleyi ıslattı. "Kalemiz ıslanıyor!" dedi Hulk. Pencere tavanın yanındaydı ve Hulk'tan bile yüksekti. Örümcek Adam pencereye hemen bir ağ attı ve sıkıca çekti. Pencere hemen kapandı. Hulk ıslak yastıkları kenara koydu. İki arkadaş kaleyi kuru yastıklarla yeniden kurdu. Sonra kalenin içine oturup yağmurun sesini dinlediler. Örümcek Adam ile Hulk çok sevindi, çünkü yağmur artık kalelerine giremiyordu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam ile görüşmeye gelmişti"
   - Cümle 1: «Gizli evde yağmurlu bir sabah Hulk, Örümcek Adam ile görüşmeye gelmişti.»
   - Açıklama: 'Görüşmek' 3 yaşındaki çocuğun bilmeyeceği yetişkin kelimesi.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yerde farklı bir kale yaptı"
   - Cümle 2: «İki arkadaş yastıklarla yerde farklı bir kale yaptı.»
   - Açıklama: 'Farklı' neyden farklı olduğu belli olmadan yanlış anlamda kullanılmış.
   - Açıklama: Neyden farklı olduğu belli değil; 'farklı' kelimesi yerinde kullanılmamış.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Pencere hemen kapandı."
   - Cümle 7: «Pencere hemen kapandı.»
   - Açıklama: 'Hemen' art arda iki cümlede gereksiz tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0151` birebir aynı, `@degisim: yosun -> yastık` (tutuyorsan), ardından `@onarim: 94f4f362676eadcf3fa8cfed82c17a92b4d3b3c1`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0154 (deneme 1 -> 2)

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
@plan: taşların arasından garip bir tık tık sesi geldi | sesin yerini bulup suya giden kovayı yakaladı
@tohum: orumcek_adam-0154
@degisim: terazi -> kova
Rüzgarlı bir sabah Örümcek Adam ile Hulk kumsalda şakalaşıyordu. Birden taşların arasından garip bir tık tık sesi geldi. Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. Örümcek Adam sesin geldiği yere hemen yürüdü. Hulk da peşinden gitti. Taşların arasında kırmızı bir kova vardı. Rüzgar kovayı taşlara çarpıyordu ve tık tık sesi buradan geliyordu. Kova yavaş yavaş suya doğru gidiyordu. Örümcek Adam kovayı hemen yakaladı. "Bu benim kovam!" dedi Hulk. Hulk kovasını aldı ve kocaman gülümsedi. "Teşekkürler, Örümcek Adam, sesi de kovamı da buldun!" dedi Hulk.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "garip bir tık tık sesi geldi"
   - Cümle 2: «Birden taşların arasından garip bir tık tık sesi geldi.»
   - Açıklama: Bir tık tık sesi çocuğun önemseyeceği bir sorun olarak kurulmuyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "taşların arasından garip bir tık tık sesi geldi"
   - Cümle 2: «Birden taşların arasından garip bir tık tık sesi geldi.»
   - Açıklama: Sorun yalnız bir sesten ibaret; çocuğun önemseyeceği bir kayıp ya da istek yok.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 3: «Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Hissin haber vermesi mecazlı ve soyut bir anlatım.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Kova yavaş yavaş suya doğru gidiyordu"
   - Cümle 8: «Kova yavaş yavaş suya doğru gidiyordu.»
   - Açıklama: Garip ses sorununa kovanın suya kayması diye ikinci bir sorun ekleniyor.
   - Açıklama: Garip ses sorununun yanına kovanın suya kayması diye ikinci bir sorun ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0154` birebir aynı, `@degisim: terazi -> kova` (tutuyorsan), ardından `@onarim: 9d3febcaceac1aeae51ec1dc23f69fc0236c9711`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0155 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0155
- yer: ev (Takımın gizli evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'patlıcan', fiil 'boyamak', sıfat 'mükemmel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: boş çivi duvarın en üstündeydi | duvara tırmanıp resmi çiviye astı
@tohum: orumcek_adam-0155
Örümcek Adam gizli evde Ghost-Spider ile sergi oyunu oynuyordu. İkisi büyük bir kağıda mor bir patlıcan boyadı. Ama resmi asmak için boş çivi duvarın en üstündeydi. "Bu patlıcan mükemmel, onu en üste asalım!" dedi Örümcek Adam. Resmi aldı ve süper gücüyle duvara tırmandı. Resmi en üstteki çiviye dikkatle astı. "Biraz sağa çek!" dedi arkadaşı aşağıdan. Örümcek Adam resmi biraz sağa çekti ve resim düz durdu. Sonra aşağı indi ve ikisi resme baktı. Mor patlıcan duvarda çok güzel görünüyordu. Örümcek Adam ile arkadaşı çok sevindi, çünkü resimleri artık en güzel yerdeydi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ghost-Spider ile sergi oyunu oynuyordu"
   - Cümle 1: «Örümcek Adam gizli evde Ghost-Spider ile sergi oyunu oynuyordu.»
   - Açıklama: 'Sergi' kelimesi 3 yaşındaki bir çocuğun bileceği bir kelime değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "mor bir patlıcan boyadı"
   - Cümle 2: «İkisi büyük bir kağıda mor bir patlıcan boyadı.»
   - Açıklama: Kağıda patlıcan resmi çizilir; 'patlıcan boyadı' patlıcanın kendisini boyamak anlamına gelir.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "boş çivi duvarın en üstündeydi"
   - Cümle 3: «Ama resmi asmak için boş çivi duvarın en üstündeydi.»
   - Açıklama: Çivinin yüksekte olması gerçek bir sorun gibi kurulmuyor; figür zaten resmi en üste asmak istiyor, sorun zayıf ve önemsiz kalıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "süper gücüyle duvara tırmandı"
   - Cümle 5: «Resmi aldı ve süper gücüyle duvara tırmandı.»
   - Açıklama: Gizli evin içinde resim asmak için yükseğe tırmanılıyor; güvenli kullanım satırı ev içi taklit edilebilir tırmanmayı yasaklıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0155` birebir aynı, ardından `@onarim: e6083ca35ed95eb795a7a8ed0fc3d8504d8f24cb`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0156 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0156
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'ağaç', fiil 'karşılaşmak', sıfat 'güzel'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar ağaçtaki sürpriz süsleri uçurmak üzereydi | sorunu erken fark edip süsleri sıkıca bağladı
@tohum: orumcek_adam-0156
Bir sabah Örümcek Adam, Ghost-Spider için kumsalda bir ağaca renkli süsler astı. Birden örümcek hissi bir sorun olduğunu haber verdi. Rüzgar esmeye başlamıştı ve süsler dallardan kayıyordu. Örümcek Adam hemen her süsü dallara sıkıca bağladı. Rüzgar yine esti ama hiçbir süs uçmadı. Az sonra arkadaşı havada süzülerek kumsala geldi. İki arkadaş ağacın altında karşılaştı. "Sürpriz!" dedi Örümcek Adam. "Bu ağaç çok güzel olmuş!" dedi arkadaşı sevinçle. İkisi ağacın altına oturup renkli süsleri izledi. Örümcek Adam bundan sonra rüzgarlı günlerde süsleri hep sıkıca bağladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0156` birebir aynı, ardından `@onarim: 0d36771abb4aea8f4679a0bd2655677453755b0a`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0157 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0157
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'küp', fiil 'kucaklamak', sıfat 'ferah'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: sarı küp çiçek bahçesinin duvarında kaldı | duvara tırmanıp küpü aldı
@tohum: orumcek_adam-0157
Örümcek Adam ferah parkın oyun alanında yumuşak renkli küplerle oynuyordu. Küpleri havaya atıp tek tek tutuyordu. Ama sarı küp fazla yükseğe gitti ve çiçek bahçesinin duvarında kaldı. Küp duvarın tepesinde komik bir şapka gibi duruyordu. Örümcek Adam buna çok güldü. Sonra süper gücüyle duvara hızla tırmandı. Sarı küpü aldı ve yavaşça aşağı indi. Küpü iki koluyla sıkıca kucakladı. Bu kez küpleri daha alçaktan atmaya başladı. Kırmızı, mavi ve sarı küpler havada dönüyordu. Hepsi onun ellerine düşüyordu. Örümcek Adam çok mutluydu, çünkü sarı küpünü geri almıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ferah parkın oyun alanında"
   - Cümle 1: «Örümcek Adam ferah parkın oyun alanında yumuşak renkli küplerle oynuyordu.»
   - Açıklama: 'Ferah' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
   - Açıklama: 'Ferah' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "komik bir şapka gibi"
   - Cümle 4: «Küp duvarın tepesinde komik bir şapka gibi duruyordu.»
   - Açıklama: Benzetme mecazdır; küçük çocuk için gereksiz.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "süper gücüyle duvara hızla tırmandı"
   - Cümle 6: «Sonra süper gücüyle duvara hızla tırmandı.»
   - Açıklama: Oyuncağı almak için bahçe duvarına tırmanmak çocuğun taklit edebileceği yükseğe tırmanma davranışıdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0157` birebir aynı, ardından `@onarim: 6c5c1f37c75cd9df9c9427c25f2b8195c67c81a3`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0158 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0158
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'tabure', fiil 'hazırlanmak', sıfat 'turuncu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: tabure ıslak kuma batıp yana eğiliyordu | sorunu fark edip tabureyi kuru kuma taşıdı
@tohum: orumcek_adam-0158
Örümcek Adam kumsalda gemi oyununa hazırlanıyordu. Suyun kenarına bir tabure koydu ve üstüne turuncu bir havlu astı. Ama tabure yumuşak, ıslak kuma batıyordu ve yana eğiliyordu. Oturmadan önce örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam tabureyi kaldırdı ve kuru, sert kuma taşıdı. Tabure artık dimdik duruyordu. Örümcek Adam tabureye oturdu. Turuncu havluyu yelken gibi iki eliyle tuttu. Rüzgar esti ve havlu şişti. Örümcek Adam denizdeki gemilere el salladı. Örümcek Adam çok sevindi, çünkü gemi oyununu kuru kumda rahatça oynuyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 4: «Oturmadan önce örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0158` birebir aynı, ardından `@onarim: 68f3ef518d8acaa45c3f58d1fb6d7aaa47cabcdf`, sonra gövde.
