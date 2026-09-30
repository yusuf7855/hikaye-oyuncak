# Editör görevi (onarım): Örümcek Adam, onarım partisi 47

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar47.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar47.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0188 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0188
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'börek', fiil 'yardımlaşmak', sıfat 'limonlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: güçlü bir rüzgar örtüye doğru geldi | sorunu önceden fark etti ve yardımlaştılar
@tohum: orumcek_adam-0188
Örümcek Adam ile Ghost-Spider parkta piknik yapıyordu. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Ağaçların yaprakları sallandı ve güçlü bir rüzgar örtüye doğru geldi. Örtünün üstünde peynirli börek ve limonlu su vardı. "Rüzgar geliyor, hemen toplayalım!" dedi Örümcek Adam. Hemen yardımlaştılar. Arkadaşı böreği ve suyu kucağına aldı. Örümcek Adam büyük taşları örtünün dört ucuna koydu. Rüzgar sert esti ama örtü yerinden kalkmadı. Biraz sonra ağaçlar yine sessiz oldu. Arkadaşı böreği ve suyu örtüye geri koydu. Örümcek Adam ve arkadaşı böreği mutlu mutlu yemeye devam etti.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sorunu önceden fark etti ve yardımlaştılar"
   - Cümle 0 (plan satırı): «güçlü bir rüzgar örtüye doğru geldi | sorunu önceden fark etti ve yardımlaştılar»
   - Açıklama: Plan çözümü söylemiyor; gövdedeki asıl çözüm örtünün uçlarına taş koymak.
   - Açıklama: Plan çözümü söylemiyor; gövdede çözüm örtünün uçlarına taş koymak.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: Bir hissin sorun olduğunu haber vermesi 3 yaşındaki çocuk için soyut bir kavram ve kişileştirme.
   - Açıklama: 'Örümcek hissi' ve onun haber vermesi soyut ve mecazlı, 3 yaşındaki çocuk anlamaz.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Örümcek Adam büyük taşları örtünün dört ucuna koydu"
   - Cümle 8: «Örümcek Adam büyük taşları örtünün dört ucuna koydu.»
   - Açıklama: Taşlar daha önce kurulmadan sebepsizce beliriyor ve çözümü getiriyor.
   - Açıklama: Büyük taşlar önceden kurulmadan çözümü getirmek için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0188` birebir aynı, ardından `@onarim: 25e357d3aa1fec6debf98f59bf7ccaaaa6f89840`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0189 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0189
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'bitki', fiil 'çizmek', sıfat 'pahalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: bir dalga arkadaşının resmine doğru geliyordu | sorunu hissetti ve resmi hızla kaldırdı
@tohum: orumcek_adam-0189
@degisim: pahalı -> renkli
Örümcek Adam kumsalda Hulk'ın bir bitki çizmesini izliyordu. Hulk'ın kağıdı ve renkli kalemleri suyun yanında, kumun üstündeydi. Birden örümcek hissi bir sorun olduğunu haber verdi: bir dalga geliyordu. Örümcek Adam kağıdı ve kalemleri hızla aldı ve geri koştu. Dalga kumu ıslattı ama resim kuru kaldı. "Neredeyse resmim ıslanıyordu!" dedi Hulk. İkisi sudan uzakta, kuru kuma oturdu. Hulk küçük bitkinin resmini orada bitirdi. Sonra kağıdı Örümcek Adam'a uzattı. "Teşekkürler, Örümcek Adam, bu resim senin!" dedi Hulk.
```

**Hakem bulguları (2):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Hulk'ın bir bitki çizmesini izliyordu"
   - Cümle 1: «Örümcek Adam kumsalda Hulk'ın bir bitki çizmesini izliyordu.»
   - Açıklama: Kartın yanlar bölümünde resim yapma Spin'in ilişkisine ait; Hulk kocaman ve güçlü kahraman olarak tanımlanıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi bir sorun olduğunu haber verdi: bir dalga geliyordu.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatımdır.
   - Açıklama: 'Örümcek hissi haber verdi' soyut bir kavram ve kişileştirme; küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0189` birebir aynı, `@degisim: pahalı -> renkli` (tutuyorsan), ardından `@onarim: 32c52965035b36c9a632a59d9fb517bc2a665fc0`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0190 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0190
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: bir şey yapmak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'şort', fiil 'korunmak', sıfat 'kocaman'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: güneş çok sıcaktı ve havluyu takacak yer yoktu | duvara tırmanıp havlunun bir ucunu yukarı koydu
@tohum: orumcek_adam-0190
@degisim: şort -> havlu
Bir sabah Örümcek Adam ile Spin limanın yanındaki kumsala geldi. Güneş çok sıcaktı ve ikisi güneşten korunmak istedi. Kocaman bir havluyla gölge yapacaklardı ama havluyu takacak yer yoktu. "Kumsalda hiç ağaç yok," dedi Spin. Örümcek Adam limanın taş duvarına baktı. Havlunun bir ucunu aldı ve süper gücüyle duvara tırmandı. Ucu duvarın tepesine koydu ve üstüne ağır bir taş yerleştirdi. Spin öbür ucu kuma serdi ve iki taşla tuttu. Havlu kumun üstünde güzel bir gölge yaptı. "Burası çok serin oldu, Örümcek Adam!" dedi Spin. Örümcek Adam çok sevindi, çünkü artık ikisi de gölgede oturabiliyordu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "üstüne ağır bir taş yerleştirdi"
   - Cümle 7: «Ucu duvarın tepesine koydu ve üstüne ağır bir taş yerleştirdi.»
   - Açıklama: Altında oturulan gölgeliğin üstünde, duvarın tepesine ağır taş koymak taklit edilince tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0190` birebir aynı, `@degisim: şort -> havlu` (tutuyorsan), ardından `@onarim: bd71d24dc0254f3cfc5545f03a92a9d0c8131334`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0191 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0191
- yer: ev (Takımın gizli evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'üzüm', fiil 'gülümsemek', sıfat 'reçelli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: ekmeğe göz olacak üzüm kutuların arasına kaçtı | ağ atıp üzümü dar yerden çekti
@tohum: orumcek_adam-0191
Dışarıda yağmur yağıyordu. Örümcek Adam gizli evde yemek oyunu oynuyordu ve Hulk'a reçelli ekmek hazırladı. Ekmeğe üzümlerle göz yapacaktı ama bir üzüm kutuların arasına yuvarlandı. Hulk kocaman elini uzattı ama eli o dar yere sığmadı. Örümcek Adam ince bir ağ attı. Ağ üzüme yapıştı. Örümcek Adam ağı yavaşça çekti ve üzümü aldı. Üzümü suyla yıkadı ve diğer üzümün yanına koydu. Artık ekmeğin üstünde iki göz vardı. Örümcek Adam reçelle gülen bir ağız da çizdi. Hulk tabağa baktı ve gülümsedi. Örümcek Adam çok sevindi, çünkü Hulk onun yemeğini beğenmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "üzüm kutuların arasına kaçtı"
   - Cümle 0 (plan satırı): «ekmeğe göz olacak üzüm kutuların arasına kaçtı | ağ atıp üzümü dar yerden çekti»
   - Açıklama: Üzüm kaçmaz; plan satırında fiil öznesine uymuyor, 'yuvarlandı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0191` birebir aynı, ardından `@onarim: d9725280f4b6acd6440c757e60d0de07ef2db454`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0192 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0192
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yağmur ya da kar günü
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'top', fiil 'ulaşmak', sıfat 'hevesli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: yağmurda rüzgar topu limanın duvarına taşıdı | duvara tırmanıp topu aldı ve arkadaşına verdi
@tohum: orumcek_adam-0192
Örümcek Adam ile Spin kumsalda top oynuyordu. Birden yağmur başladı ve güçlü bir rüzgar esti. Rüzgar topu uçurdu ve limandaki taş duvarın üstüne taşıdı. Spin elini uzattı ama topa ulaşamadı. Spin yağmurda oynamak için çok hevesliydi. "Topu bana getirebilir misin, Örümcek Adam?" diye sordu Spin. "Tabii, hemen getiriyorum," dedi Örümcek Adam. Örümcek Adam ellerini ıslak duvara yapıştırdı ve yukarı tırmandı. Topu aldı ve yavaşça aşağı indi. Sonra topu Spin'e verdi. İkisi yağmurun altında koştu ve bol bol güldü. Örümcek Adam bundan sonra rüzgarlı günlerde duvardan uzakta top oynadı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yağmurda oynamak için çok hevesliydi"
   - Cümle 5: «Spin yağmurda oynamak için çok hevesliydi.»
   - Açıklama: 'Hevesli' soyut bir duygu kelimesi, 3 yaşındaki çocuk için zor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Spin yağmurda oynamak için çok hevesliydi"
   - Cümle 5: «Spin yağmurda oynamak için çok hevesliydi.»
   - Açıklama: Top duvarda kalmışken araya giren bu ayrıntı sorunla ilgisiz ve akışı bozuyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ellerini ıslak duvara yapıştırdı ve yukarı tırmandı"
   - Cümle 8: «Örümcek Adam ellerini ıslak duvara yapıştırdı ve yukarı tırmandı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre tırmanma yalnız süper güç olarak geçmeli; burada yağmurda ve rüzgarda ıslak liman duvarına tırmanma süper güç diye belirtilmeden, taklit edilebilir biçimde anlatılıyor.
   - Açıklama: Güvenli özellik kullanımı satırına göre tırmanma süper güç olarak verilmeli; yağmurda ıslak duvara tırmanma taklit edilebilir biçimde anlatılıyor.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "bundan sonra rüzgarlı günlerde duvardan uzakta top oynadı"
   - Cümle 12: «Örümcek Adam bundan sonra rüzgarlı günlerde duvardan uzakta top oynadı.»
   - Açıklama: Zaten kumsalda oynuyorlardı; duvardan uzak durma dersi olaydan çıkmıyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "rüzgarlı günlerde duvardan uzakta top oynadı"
   - Cümle 12: «Örümcek Adam bundan sonra rüzgarlı günlerde duvardan uzakta top oynadı.»
   - Açıklama: Kumsalda oynarken top rüzgarla duvara uçtuğu için duvardan uzak oynamak dersi yaşanan olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0192` birebir aynı, ardından `@onarim: 8f4a843fc25364068ab1625206c687a7f4126391`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0193 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0193
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yeni bir şeyi denemek
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'küpe', fiil 'aramak', sıfat 'nefis'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: saklambaçta arkadaşını büyük parkta bulamadı | duvara tırmanıp yukarıdan baktı ve parlak bir küpe gördü
@tohum: orumcek_adam-0193
@degisim: nefis -> parlak
Örümcek Adam parkta Ghost-Spider ile ilk kez saklambaç oynuyordu. Arkadaşı saklandı ve Örümcek Adam onu aramaya başladı. Ama park çok büyüktü ve onu hiçbir yerde bulamadı. "Hadi, beni bul!" diye seslendi arkadaşı. Ses ağaçlardan geliyordu ama orada kimse görünmüyordu. Örümcek Adam çiçek bahçesinin taş duvarına tırmandı. Yukarıdan parka baktı ve bir ağaçta parlak bir küpe gördü. Arkadaşı o ağacın yaprakları arasında havada süzülüyordu. Örümcek Adam duvardan indi ve ağaca koştu. "Buldum seni!" dedi Örümcek Adam. "Bu yeni oyunu çok iyi oynadın," dedi arkadaşı ve güldü. Sonra saklanma sırası Örümcek Adam'a geçti. İkisi oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "çiçek bahçesinin taş duvarına tırmandı"
   - Cümle 6: «Örümcek Adam çiçek bahçesinin taş duvarına tırmandı.»
   - Açıklama: Güvenli kullanım satırı tırmanmanın yalnız süper güç olarak anlatılmasını ister; burada çocuğun taklit edebileceği sıradan bir duvara tırmanma var.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "bir ağaçta parlak bir küpe gördü"
   - Cümle 7: «Yukarıdan parka baktı ve bir ağaçta parlak bir küpe gördü.»
   - Açıklama: Kartta Ghost-Spider için küpe gibi bir eşya yok; kapalı dünyaya kartta olmayan eşya ekleniyor.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "bir ağaçta parlak bir küpe gördü"
   - Cümle 7: «Yukarıdan parka baktı ve bir ağaçta parlak bir küpe gördü.»
   - Açıklama: Kartın Ghost-Spider ilişki/görünüş bilgisinde küpe yok; diziyi izleyen çocuk onu bu işaretle tanımaz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir ağaçta parlak bir küpe gördü"
   - Cümle 7: «Yukarıdan parka baktı ve bir ağaçta parlak bir küpe gördü.»
   - Açıklama: Küpe daha önce hiç kurulmadan beliriyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0193` birebir aynı, `@degisim: nefis -> parlak` (tutuyorsan), ardından `@onarim: 311db3f9cf2ee44b48c0044b313378621cc96f5c`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0197 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0197
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: paylaşmak
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'örgü', fiil 'paylaşmak', sıfat 'eğlenceli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: uçurtma rüzgarla yüksek bir duvarın üstüne takıldı | duvara tırmanıp uçurtmayı aldı ve paylaştı
@tohum: orumcek_adam-0197
@degisim: örgü -> uçurtma
Örümcek Adam parkta eğlenceli bir uçurtma uçuruyordu. Hulk da yanına geldi ve uçurtmaya hevesle baktı. Ama birden rüzgar esti ve uçurtma yüksek bir duvarın üstüne takıldı. "Duvar çok yüksek, ben uzanamıyorum," dedi Hulk. "Ben alırım, Hulk," dedi Örümcek Adam. Örümcek Adam ellerini duvara yapıştırdı ve yukarı tırmandı. Uçurtmayı dikkatle çıkardı ve aşağı indi. Sonra ipi Hulk'a uzattı. "Bu uçurtmayı seninle paylaşmak istiyorum," dedi Örümcek Adam. Hulk ipi kocaman eliyle tuttu ve koştu. Uçurtma yeniden gökyüzüne yükseldi. Hulk kahkahalarla güldü. Örümcek Adam çok sevindi, çünkü uçurtmasını arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "uçurtmaya hevesle baktı"
   - Cümle 2: «Hulk da yanına geldi ve uçurtmaya hevesle baktı.»
   - Açıklama: 'Hevesle' soyut bir kelime ve 3 yaşındaki çocuk için zor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Duvar çok yüksek, ben uzanamıyorum"
   - Cümle 4: «"Duvar çok yüksek, ben uzanamıyorum," dedi Hulk.»
   - Açıklama: Yanlar kartında kocaman ve çok güçlü olan Hulk'un duvara uzanamaması diziyi bilen çocuğa yanlış bilgi verir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0197` birebir aynı, `@degisim: örgü -> uçurtma` (tutuyorsan), ardından `@onarim: ebb5393e30b9bb35057bec524e0f0084ae849f98`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0198 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0198
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'havuç', fiil 'süslemek', sıfat 'somurtkan'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: limanın taş duvarı denizi kapatıyordu ve gemi görünmüyordu | duvara tırmanıp üstünde gemiyi bekledi
@tohum: orumcek_adam-0198
@degisim: havuç -> bayrak
Limanda hava güneşliydi. Örümcek Adam limana gelecek büyük bir gemiyi bekliyordu. Ama limanın taş duvarı denizi kapatıyordu ve Örümcek Adam gemiyi göremiyordu. Bu yüzden biraz somurtkandı. Sonra ellerini duvara yapıştırdı ve yukarı tırmandı. Duvarın üstüne oturdu ve denize baktı. Deniz sakindi ve gemi daha görünmüyordu. Örümcek Adam sessizce bekledi. Sonunda uzakta büyük bir gemi göründü. Gemi rengarenk bayraklarla süslenmişti. Gemi limana yaklaştı ve düdüğünü çaldı. Örümcek Adam gemiye el salladı ve güldü. Örümcek Adam bundan sonra gemileri görmek için hep bu duvara geldi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu yüzden biraz somurtkandı"
   - Cümle 4: «Bu yüzden biraz somurtkandı.»
   - Açıklama: 'Somurtkan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Duvarın üstüne oturdu ve denize baktı"
   - Cümle 6: «Duvarın üstüne oturdu ve denize baktı.»
   - Açıklama: Deniz kenarındaki yüksek liman duvarının üstünde oturmak ve bunu alışkanlık yapmak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Limanda denizin üstündeki yüksek taş duvarın tepesine oturmak çocuğun taklit edebileceği bir yükseğe çıkma davranışı.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bundan sonra gemileri görmek için hep bu duvara geldi"
   - Cümle 13: «Örümcek Adam bundan sonra gemileri görmek için hep bu duvara geldi.»
   - Açıklama: Son cümle olaydan çıkan bir ders değil, hikayeyi sonraki günlere taşıyan bir zaman atlaması.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0198` birebir aynı, `@degisim: havuç -> bayrak` (tutuyorsan), ardından `@onarim: f1e0405f40e0e0c25da616a4121911cef8ce74a9`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0199 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0199
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'külah', fiil 'toplamak', sıfat 'pembe'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: rüzgar kabuk dolu külahı yüksek duvara uçurdu | duvara tırmanıp külahı aldı ve arkadaşına verdi
@tohum: orumcek_adam-0199
Limanın yanındaki kumsalda hafif bir rüzgar esiyordu. Hulk, Örümcek Adam ile kağıttan bir külaha pembe kabuklar topluyordu. Birden rüzgar külahı uçurdu ve külah yüksek bir duvarın üstüne düştü. "Külahım orada kaldı, Örümcek Adam!" dedi Hulk. Hulk zıpladı ama duvar ondan bile daha yüksekti. "Üzülme, Hulk, ben getiririm," dedi Örümcek Adam. Örümcek Adam taş duvara yapıştı ve hızlıca tırmandı. Külahı aldı ve içine baktı. Kabukların hepsi içindeydi. Sonra yavaşça aşağı indi ve külahı Hulk'a verdi. "Teşekkürler, sen çok iyi bir arkadaşsın!" dedi Hulk. Örümcek Adam bundan sonra yardım isteyen arkadaşına hemen koştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgar külahı uçurdu ve külah yüksek bir duvarın üstüne düştü"
   - Cümle 3: «Birden rüzgar külahı uçurdu ve külah yüksek bir duvarın üstüne düştü.»
   - Açıklama: Hafif bir rüzgarın kabuk dolu bir külahı yüksek bir duvarın üstüne uçurması akla yatkın değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgar külahı uçurdu"
   - Cümle 3: «Birden rüzgar külahı uçurdu ve külah yüksek bir duvarın üstüne düştü.»
   - Açıklama: Hafif bir rüzgarın kabuk dolu külahı yüksek bir duvarın üstüne uçurması akla yatkın değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kabukların hepsi içindeydi"
   - Cümle 9: «Kabukların hepsi içindeydi.»
   - Açıklama: Külah rüzgarla uçup duvara düştüğü halde kabukların hiçbiri dökülmemiş olması uçma olayıyla çelişiyor.
   - Açıklama: Uçup duvara düşen külahtaki kabukların hiçbirinin dökülmemesi olayla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0199` birebir aynı, ardından `@onarim: 5bfda4817b2337db5b419bdd4731a38bfbbafffe`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0200 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0200
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: kaybolan eşya
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'tüy', fiil 'giymek', sıfat 'keyifli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar arkadaşının şapkasını uçurdu ve şapka kayboldu | duvara tırmanıp öbür tarafta şapkayı buldu
@tohum: orumcek_adam-0200
@degisim: giymek -> takmak
Parkta güçlü bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider çiçek bahçesinde yürüyordu. Birden rüzgar arkadaşının şapkasını uçurdu ve şapka kayboldu. İkisi çiçeklerin arasına baktı ama şapkayı bulamadı. Sonra Örümcek Adam bahçenin duvarında beyaz bir tüy gördü. "Bak, bu senin şapkanın tüyü!" dedi Örümcek Adam. Örümcek Adam duvara tırmandı ve duvarın öbür tarafına baktı. Şapka orada, bir çalının üstünde duruyordu. Örümcek Adam şapkayı aldı ve arkadaşına getirdi. Arkadaşı şapkasını taktı ve güldü. "Teşekkürler, Örümcek Adam!" dedi arkadaşı. Sonra ikisi keyifli yürüyüşlerine mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "rüzgar arkadaşının şapkasını uçurdu"
   - Cümle 3: «Birden rüzgar arkadaşının şapkasını uçurdu ve şapka kayboldu.»
   - Açıklama: 'arkadaşının' kimin arkadaşını gösterdiği belli değil ve Ghost-Spider bir daha adıyla anılmıyor.
   - Açıklama: İki kişi varken 'arkadaşının' kimin şapkası olduğunu, Ghost-Spider'ın mı başka birinin mi, belli etmiyor.
   - Açıklama: Plan satırında da 'arkadaşının' kimi gösterdiği belli değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvara tırmandı"
   - Cümle 7: «Örümcek Adam duvara tırmandı ve duvarın öbür tarafına baktı.»
   - Açıklama: Park duvarına tırmanma süper güç olarak belirtilmeden, çocuğun taklit edebileceği biçimde anlatılıyor; güvenli özellik kullanımı satırına aykırı.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "keyifli yürüyüşlerine mutlu mutlu devam"
   - Cümle 12: «Sonra ikisi keyifli yürüyüşlerine mutlu mutlu devam etti.»
   - Açıklama: 'keyifli' ve 'mutlu mutlu' aynı anlamı gereksizce tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0200` birebir aynı, `@degisim: giymek -> takmak` (tutuyorsan), ardından `@onarim: d777950a267df22945be495db0e4c10851cbdb1c`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0201 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0201
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yeni bir şeyi denemek
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'yorgan', fiil 'doyurmak', sıfat 'lezzetli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: rüzgar piknik örtüsünü duvarın üstüne uçurdu | duvara tırmanıp örtüyü aldı ve çimlere serdi
@tohum: orumcek_adam-0201
@degisim: yorgan -> örtü
Bir sabah Örümcek Adam ile Spin parka piknik yapmaya geldi. Spin ilk kez muzlu bir sandviç yapmıştı. Ama rüzgar esti ve piknik örtüsünü parktaki taş duvarın üstüne uçurdu. "Çimler ıslak, örtü olmadan oturmak zor," dedi Spin. "Ben onu hemen getiririm, Spin," dedi Örümcek Adam. Örümcek Adam duvara tırmandı ve örtüyü aldı. Sonra aşağı indi ve örtüyü çimlere serdi. İkisi örtünün üstüne oturdu. Örümcek Adam yeni sandviçten bir ısırık aldı. "Çok lezzetli, bu sandviçi sevdim!" dedi Örümcek Adam. Spin sevinçle güldü. İkisi karınlarını doyurdu ve sonra mutlu mutlu oyun alanına koştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve piknik örtüsünü parktaki taş duvarın üstüne uçurdu"
   - Cümle 3: «Ama rüzgar esti ve piknik örtüsünü parktaki taş duvarın üstüne uçurdu.»
   - Açıklama: Sorun önemsiz bir olay; örtü tek tırmanışla alınıyor ve hikaye 'uçtu, aldı, bitti' kalıbına düşüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0201` birebir aynı, `@degisim: yorgan -> örtü` (tutuyorsan), ardından `@onarim: bf2f9de9c7f29aebd22151223760d1167171342f`, sonra gövde.
