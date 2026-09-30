# Editör görevi (onarım): Örümcek Adam, onarım partisi 46

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar46.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar46.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0171 (deneme 2 -> 3)

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
Örümcek Adam parkta Ghost-Spider ile çiçek dikiyordu. Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı. Rüzgar büyük bir topu yeni çiçeklere doğru yuvarlıyordu. Arkadaşı topu görmemişti. Örümcek Adam hemen koştu ve topu çiçeklerin önünde tuttu. "Çok sevdiğim çiçeklerim kurtuldu!" dedi arkadaşı. Sonra meraklı bir sesle topun nereden geldiğini sordu. Örümcek Adam ona oyun alanını gösterdi. Sonra topu oyun alanına geri götürdü. Örümcek Adam ile arkadaşı kalan çiçekleri birlikte mutlu mutlu dikti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun"
   - Cümle 2: «Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve soyut 'sorun olduğunu anladı' 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 2: «Birden Örümcek Adam örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' 3 yaşındaki çocuğun bilmediği soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0171` birebir aynı, `@degisim: sebze -> çiçek` (tutuyorsan), ardından `@onarim: b5d0727fb1c4fa36dc226c4365b641ed9f22eb1a`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0172 (deneme 2 -> 3)

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
Kumsalda serin bir rüzgar esiyordu. Örümcek Adam ile Hulk kovayla kumdan kule yapma oyunu oynuyordu. Ama bir dalga geldi ve kovayı simsiyah kayaların arasına sürükledi. Örümcek Adam kayalara doğru bir adım attı. Birden örümcek hissiyle ıslak kayaların çok kaygan olduğunu anladı. Örümcek Adam kuma geri döndü. "Hulk, kumda durup kovaya uzanır mısın?" diye sordu Örümcek Adam. Hulk kumda durdu ve kocaman koluyla kovayı kolayca aldı. Hulk kovayı arkadaşına verdi ve onu rahatlattı. Örümcek Adam çok sevindi, çünkü kovayı kayalara basmadan kurtarmışlardı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle ıslak"
   - Cümle 5: «Birden örümcek hissiyle ıslak kayaların çok kaygan olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle ıslak kayaların"
   - Cümle 5: «Birden örümcek hissiyle ıslak kayaların çok kaygan olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "verdi ve onu rahatlattı"
   - Cümle 9: «Hulk kovayı arkadaşına verdi ve onu rahatlattı.»
   - Açıklama: 'Rahatlatmak' soyut bir duygu fiili, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0172` birebir aynı, `@degisim: armut -> kova` (tutuyorsan), ardından `@onarim: 3176d60e7e8aa658b09ced6f8fab3e3d5bdf6e63`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0173 (deneme 2 -> 3)

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
Rüzgar esiyordu ve Örümcek Adam ile Spin kumsalda yürüyordu. Spin ağır çantasını bir kayanın üstüne koydu. Ama çanta kaydı ve iki kayanın arasına düştü. Kayaların arası çok dardı. Spin elini uzattı ama çantaya yetişemedi. "Kitabım orada, onu sana okumak istiyordum," dedi Spin. "Üzülme, Spin, ben onu çıkarırım," dedi Örümcek Adam. Örümcek Adam ince bir ağ attı. Ağ çantaya yapıştı. Örümcek Adam ağı yavaşça çekti ve çantayı dışarı çıkardı. Spin çantayı aldı ve sevinçle güldü. Sonra ikisi kumun üstüne oturdu ve kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama çantaya yetişemedi"
   - Cümle 5: «Spin elini uzattı ama çantaya yetişemedi.»
   - Açıklama: 'Yetişmek' burada yanlış anlamda; 'eli çantaya yetişmedi' ya da 'çantaya uzanamadı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0173` birebir aynı, ardından `@onarim: 5a5d269223412c1d5a6c0d7bfd9ee064ce9c5b93`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0176 (deneme 2 -> 3)

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
@plan: bisikletin tekerleğine küçük bir kabuk sıkıştı | durup kabuğu tekerlekten çıkardı
@tohum: orumcek_adam-0176
@degisim: ilginç -> garip
Kumsalda Örümcek Adam bisikletiyle büyük daireler çiziyordu. Birden kumdaki küçük bir kabuk ön tekerleğe sıkıştı. Tekerlek zor dönmeye başladı ve garip bir ses çıkardı. Örümcek Adam hızlanmak istedi. Ama örümcek hissi ile bir sorun olduğunu anladı. Hemen yavaşladı ve bisikletten indi. Tekerleğe eğildi ve kabuğu gördü. Kabuğu parmaklarıyla dikkatle çekip çıkardı. Tekerleği elle çevirdi ve tekerlek rahat döndü. Örümcek Adam bisikletine yeniden bindi ve yeni daireler çizdi. Örümcek Adam çok sevindi, çünkü bisikleti yine kolayca gidiyordu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun olduğunu anladı"
   - Cümle 5: «Ama örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0176` birebir aynı, `@degisim: ilginç -> garip` (tutuyorsan), ardından `@onarim: bfe5c934eba56a185be2077bd832038f26742477`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0177 (deneme 2 -> 3)

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
Kumsalda Örümcek Adam ile Hulk piknik yapıyordu. Hulk büyük bir çilekli pasta getirmişti. Birden yakındaki kayalardan garip bir tak tak sesi geldi. "Belki bu dalgaların sesi," dedi Hulk. Ama Örümcek Adam örümcek hissiyle bunun dalga sesi olmadığını anladı. İkisi hemen kayaların arkasına baktı. Küçük bir kayığın ipi direkten çözülmüştü. Dalgalar kayığı kayalara çarpıyordu. Örümcek Adam kayığı ipinden çekip kıyıya getirdi. Sonra ipi direğe iki kez sıkıca bağladı. Kayık durdu ve tak tak sesi kesildi. "Hadi, şimdi pasta yiyelim," dedi Örümcek Adam. Örümcek Adam çok mutluydu, çünkü sesin nereden geldiğini bulmuş ve kayığı kurtarmıştı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam kayığı ipinden çekip kıyıya getirdi"
   - Cümle 9: «Örümcek Adam kayığı ipinden çekip kıyıya getirdi.»
   - Açıklama: Dalgaların kayalara çarptığı yerde kayığı iple çekmek çocuğun taklit edebileceği riskli bir davranış.
   - Açıklama: Dalgaların kayalara çarptığı başıboş kayığı çekmek çocuğun taklit edebileceği su kenarı tehlikesi taşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0177` birebir aynı, `@degisim: yazmak -> bağlamak` (tutuyorsan), ardından `@onarim: a93dd7456c1af194a3d5a10d80d9fc225e339163`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0179 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar boş fıçıyı çiçeklere doğru yuvarladı | koşup fıçıyı çiçeklerin önünde tuttu
@tohum: orumcek_adam-0179
@degisim: sevecen -> boş
Rüzgar esiyordu ve parktaki çiçekler yağmurla yeni yıkanmıştı. Örümcek Adam boş bir fıçıya top atma oyunu oynuyordu. Ama sert bir rüzgar fıçıyı devirdi ve fıçı çiçeklere doğru yuvarlandı. Örümcek Adam o sırada fıçıyı görmüyordu. Ama örümcek hissi ile bir sorun olduğunu anladı. Hemen arkasına döndü ve yuvarlanan fıçıyı gördü. Koştu ve fıçıyı çiçeklerin önünde iki eliyle tuttu. Örümcek Adam fıçıyı yeniden yerine koydu. Sonra topu attı ve top tam fıçının içine düştü. Örümcek Adam çok sevindi, çünkü çiçekler kurtulmuştu ve oyunu devam ediyordu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çiçekler yağmurla yeni yıkanmıştı"
   - Cümle 1: «Rüzgar esiyordu ve parktaki çiçekler yağmurla yeni yıkanmıştı.»
   - Açıklama: Çiçeklerin yağmurla yıkanması mecazlı bir anlatım.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Örümcek Adam o sırada fıçıyı görmüyordu"
   - Cümle 4: «Örümcek Adam o sırada fıçıyı görmüyordu.»
   - Açıklama: Örümcek Adam fıçıya top atarken fıçıyı görmüyor ve arkasına dönmek zorunda kalıyor, bu çelişkili.
   - Açıklama: Fıçıya top atma oyunu oynayan Örümcek Adam'ın fıçıyı görmüyor olması oyunla çelişiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ile bir sorun"
   - Cümle 5: «Ama örümcek hissi ile bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve bir sorun olduğunu anlamak küçük çocuk için soyut kavramlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0179` birebir aynı, `@degisim: sevecen -> boş` (tutuyorsan), ardından `@onarim: 8c6c614725b70215036f7d4f9e79ad31db71e4dc`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0180 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0180
- yer: ev (Takımın gizli evi.)
- tema: paylaşmak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'toz', fiil 'kurulanmak', sıfat 'güneşli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: arkadaşının kurabiyesi yere düştü ve tozlandı | sorunu hemen fark etti ve kurabiyesini paylaştı
@tohum: orumcek_adam-0180
Dışarıda güneşli bir hava vardı. Örümcek Adam gizli evde yüzünü yıkadı ve havluyla kurulandı. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam hemen masanın yanına koştu. Ghost-Spider'ın kurabiyesi yere düşmüştü ve üstüne toz bulaşmıştı. Arkadaşı üzgün üzgün yere bakıyordu. "Bunu artık yiyemem," dedi arkadaşı. Örümcek Adam kendi kurabiyesini aldı ve ikiye böldü. "Al, yarısı senin," dedi Örümcek Adam. O gülümsedi ve kurabiyenin yarısını aldı. İkisi masaya oturdu ve kurabiyelerini birlikte yedi. "Teşekkürler, Örümcek Adam, sen çok iyi bir arkadaşsın!" dedi arkadaşı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yüzünü yıkadı ve havluyla kurulandı"
   - Cümle 2: «Örümcek Adam gizli evde yüzünü yıkadı ve havluyla kurulandı.»
   - Açıklama: Yüz yıkama ayrıntısı olayla bağlantısız ve işlevsiz.
   - Açıklama: Yüz yıkama ve kurulanma olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede yalnız bir sorun olduğu söyleniyor; kurabiyenin düşmesi ancak 5. cümlede açıklanıyor.
   - Açıklama: Sorun ilk üç cümlede açıkça söylenmiyor, ancak beşinci cümlede ortaya çıkıyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O gülümsedi ve kurabiyenin"
   - Cümle 10: «O gülümsedi ve kurabiyenin yarısını aldı.»
   - Açıklama: Son konuşan Örümcek Adam olduğu için 'O' zamirinin Ghost-Spider'ı gösterdiği belli değil.
   - Açıklama: Son konuşan Örümcek Adam olduğundan 'O' zamirinin arkadaşı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0180` birebir aynı, ardından `@onarim: 8cf73187f3af530b261faa1d6ee47855ea7fc325`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0181 (deneme 2 -> 3)

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
@plan: garip bir tıp tıp sesi geldi | sesi bulup açık pencereyi kapattı
@tohum: orumcek_adam-0181
@degisim: sabırsız -> kuru
Dışarıda yağmur yağıyordu ve rüzgar esiyordu. Örümcek Adam gizli evde oturuyor ve yağmuru seyrediyordu. Birden garip bir tıp tıp sesi duydu. Ama sesin nereden geldiğini bilmiyordu. Örümcek Adam örümcek hissiyle mutfakta bir sorun olduğunu anladı. Hemen mutfağa gitti. Rüzgar mutfağın küçük penceresini açmıştı. Yağmur damlaları içeri giriyordu. Damlalar pencerenin önündeki çikolata kutusunun üstüne düşüyordu. Tıp tıp sesi buradan geliyordu. Örümcek Adam kutuyu kuru bir yere koydu ve pencereyi kapattı. Örümcek Adam bundan sonra rüzgar esince önce mutfak penceresine baktı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle mutfakta bir sorun"
   - Cümle 5: «Örümcek Adam örümcek hissiyle mutfakta bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'sorun' 3 yaşındaki çocuğa soyut kalan kavramlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0181` birebir aynı, `@degisim: sabırsız -> kuru` (tutuyorsan), ardından `@onarim: 6c1b30b30a8775d2464a1b81d44260b64e8b9134`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0182 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0182
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yeni bir şeyi denemek
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'ay', fiil 'yankılanmak', sıfat 'güçlü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: arkadaşı ilk kez voleybol oynayacaktı ama kumsalda file yoktu | iki kayanın arasına ağ atıp file yaptı
@tohum: orumcek_adam-0182
Denizden serin bir rüzgar esiyordu. Örümcek Adam ile Hulk ay ışığında kumsala geldi. Hulk elindeki topla ilk kez voleybol oynamak istiyordu ama kumsalda file yoktu. "File olmadan bu oyun olmaz," dedi Hulk. Örümcek Adam kumdaki iki büyük kayaya baktı. Sonra kayaların arasına ağ attı ve uzun bir file ördü. Hulk topa güçlü bir vuruş yaptı. Top yukarı uçtu ve Örümcek Adam onu yakaladı. Hulk'ın kahkahası limanda yankılandı. "Bu oyunu çok sevdim!" dedi Hulk. Örümcek Adam ve Hulk kumsalda mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hulk'ın kahkahası limanda yankılandı"
   - Cümle 9: «Hulk'ın kahkahası limanda yankılandı.»
   - Açıklama: 'Kahkahası yankılandı' 3 yaşındaki çocuğa uygun olmayan soyut ve zor bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kahkahası limanda yankılandı"
   - Cümle 9: «Hulk'ın kahkahası limanda yankılandı.»
   - Açıklama: 'Yankılanmak' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hulk'ın kahkahası limanda yankılandı"
   - Cümle 9: «Hulk'ın kahkahası limanda yankılandı.»
   - Açıklama: Hikaye kumsalda geçerken liman sebepsizce beliriyor ve sahneyle uyuşmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0182` birebir aynı, ardından `@onarim: f6e956067566a2444044689311d04c2754da2da4`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0183 (deneme 2 -> 3)

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
@degisim: şanslı -> iyi
Kumsalda Örümcek Adam ile Spin kabuk topluyordu. İkisi oradan oraya koşturuyordu. Ama Spin'in kovasının dibinde küçük bir delik vardı ve kabuklar düşüyordu. Spin bunu görmedi. Birden Örümcek Adam örümcek hissiyle bir sorun olduğunu anladı. Hemen arkasına döndü ve kumdaki kabukları gördü. "Spin, kovanda delik var, kabukların düşüyor!" dedi Örümcek Adam. Spin kovasına baktı ve üzüldü. "Benim kovam sağlam, birlikte kullanalım," dedi Örümcek Adam. İkisi düşen kabukları topladı ve hepsini aynı kovaya koydu. "Teşekkürler, sen çok iyi bir arkadaşsın," dedi Spin. Örümcek Adam çok sevindi, çünkü kovasını paylaşınca bütün kabuklar bir arada kaldı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun olduğunu anladı"
   - Cümle 5: «Birden Örümcek Adam örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' ve 'bir sorun olduğunu anladı' 3 yaşındaki çocuk için soyut bir anlatım.
   - Açıklama: 'Örümcek hissi' ve 'bir sorun olduğunu anlamak' soyut ifadeler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0183` birebir aynı, `@degisim: şanslı -> iyi` (tutuyorsan), ardından `@onarim: 14264a0adca9cc5c9e939ac58fef5a4baf8078e3`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0184 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0184
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'elbise', fiil 'küçülmek', sıfat 'değerli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar uçurtmayı uzun duvarın üstüne düşürdü | duvara tırmandı ve uçurtmayı geri getirdi
@tohum: orumcek_adam-0184
@degisim: elbise -> uçurtma
Denizden güçlü bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider kumsalda uçurtma uçuruyordu. Birden rüzgar çok sert esti ve ip arkadaşının elinden kaydı. Uçurtma havada küçüldü ve limanın yanındaki uzun duvarın üstüne düştü. "O uçurtma çok değerli, onu birlikte yaptık!" dedi arkadaşı. "Üzülme, ben getiririm," dedi Örümcek Adam. Örümcek Adam süper gücüyle duvara hızla tırmandı. Uçurtmayı dikkatle aldı ve aşağı indi. Sonra onu arkadaşına verdi. O ipi bu kez iki eliyle sıkıca tuttu. Uçurtma yeniden göğe yükseldi. "Teşekkürler, Örümcek Adam, bu oyun yine çok eğlenceli!" dedi arkadaşı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Uçurtma havada küçüldü"
   - Cümle 4: «Uçurtma havada küçüldü ve limanın yanındaki uzun duvarın üstüne düştü.»
   - Açıklama: Uçurtma küçülmez; uzaklaşıp küçük göründüğü anlatılmalı.
   - Açıklama: Uçurtma gerçekte küçülmez; fiil öznesine uymuyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "uzun duvarın üstüne düştü"
   - Cümle 4: «Uçurtma havada küçüldü ve limanın yanındaki uzun duvarın üstüne düştü.»
   - Açıklama: Asıl sorun olan uçurtmanın duvara düşmesi ilk 3 cümlede değil 4. cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "uçurtma çok değerli"
   - Cümle 5: «"O uçurtma çok değerli, onu birlikte yaptık!" dedi arkadaşı.»
   - Açıklama: 'Değerli' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O ipi bu kez"
   - Cümle 10: «O ipi bu kez iki eliyle sıkıca tuttu.»
   - Açıklama: 'O' zamirinin Örümcek Adam'ı mı arkadaşını mı gösterdiği belli değil.
   - Açıklama: 'O' zamiri kişiyi mi ipi mi gösteriyor belli değil; ipi kimin tuttuğu belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0184` birebir aynı, `@degisim: elbise -> uçurtma` (tutuyorsan), ardından `@onarim: 3b8f6a2b380b3b8401f40f6331913ab6a82577b3`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0187 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0187
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'brokoli', fiil 'götürmek', sıfat 'hareketli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: torba yırtıldı ve brokoliler suya doğru yuvarlandı | ağ atıp brokolileri sudan önce yakaladı
@tohum: orumcek_adam-0187
Limanda hareketli bir sabah vardı ve Örümcek Adam kumsalda bekliyordu. Ghost-Spider piknik için bir torba brokoli getiriyordu. Ama torba birden yırtıldı ve brokoliler suya doğru yuvarlandı. "Brokoliler denize gidiyor!" dedi arkadaşı. Örümcek Adam hızla ağ attı ve hepsini sudan önce yakaladı. Sonra onları kollarına aldı ve piknik yerine götürdü. "Teşekkürler, Örümcek Adam, hepsi kurtuldu!" dedi arkadaşı. İkisi kumun üstüne büyük bir örtü serdi. Brokolileri, ekmeği ve suyu örtünün üstüne koydular. Örümcek Adam ile arkadaşı kumsalda mutlu mutlu piknik yaptı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama torba birden yırtıldı"
   - Cümle 3: «Ama torba birden yırtıldı ve brokoliler suya doğru yuvarlandı.»
   - Açıklama: Torbanın neden yırtıldığı söylenmiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "denize gidiyor!" dedi arkadaşı"
   - Cümle 4: «"Brokoliler denize gidiyor!" dedi arkadaşı.»
   - Açıklama: Ghost-Spider adıyla tanıtıldıktan sonra 'arkadaşı' diye anılıyor; konuşanın kim olduğu belirsizleşiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "hepsini sudan önce yakaladı"
   - Cümle 5: «Örümcek Adam hızla ağ attı ve hepsini sudan önce yakaladı.»
   - Açıklama: 'Sudan önce' eksik bir yapı; 'suya düşmeden önce' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0187` birebir aynı, ardından `@onarim: dceb67a335df03535a48b376d1dd6cae2af58795`, sonra gövde.
