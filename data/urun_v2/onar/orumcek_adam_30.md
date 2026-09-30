# Editör görevi (onarım): Örümcek Adam, onarım partisi 30

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar30.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0116 (deneme 1 -> 2)

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
@plan: açık pencereden gelen rüzgar resmi duvara yapıştırdı | özür dileyip tırmandı ve resmi duvardan ayırdı
@tohum: orumcek_adam-0116
@degisim: yaratıcı -> renkli
Rüzgar gizli evin açık penceresinden içeri esiyordu. Örümcek Adam pencereyi açık bırakmıştı ve Hulk kağıda renkli bir tablo yapıyordu. Birden rüzgar ıslak resmi uçurdu ve resim yüksek duvara yapıştı. "Resim çok yukarıda kaldı!" dedi Hulk. "Özür dilerim, Hulk, pencereyi ben açık bıraktım," dedi Örümcek Adam. Örümcek Adam önce pencereyi kapattı. Sonra duvara tırmandı ve resmi duvardan yavaşça ayırdı. Aşağı indi ve resmi Hulk'a verdi. "Sorun yok, dostum," dedi Hulk ve gülümsedi. Sonra Örümcek Adam ile Hulk resmi birlikte mutlu mutlu boyamaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kağıda renkli bir tablo yapıyordu"
   - Cümle 2: «Örümcek Adam pencereyi açık bırakmıştı ve Hulk kağıda renkli bir tablo yapıyordu.»
   - Açıklama: 'Tablo' küçük çocuğun bilmeyeceği ve çok anlamlı bir kelime; 'resim' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kağıda renkli bir tablo"
   - Cümle 2: «Örümcek Adam pencereyi açık bırakmıştı ve Hulk kağıda renkli bir tablo yapıyordu.»
   - Açıklama: 'Tablo' 3 yaşındaki çocuk için belirsiz; 'resim' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0116` birebir aynı, `@degisim: yaratıcı -> renkli` (tutuyorsan), ardından `@onarim: 50fa264588115c101539e59c220693d9394be119`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0117 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0117
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'çamur', fiil 'güneşlenmek', sıfat 'kırılgan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: top hızla uçtu ve çamura düşecekti | ağ atıp topu havada yakaladı
@tohum: orumcek_adam-0117
@degisim: kırılgan -> renkli
Bir sabah Örümcek Adam ile Ghost-Spider parkta çimenlere uzanıp güneşleniyordu. Sonra kalkıp renkli bir topla oynamaya başladılar. Bir ara top rüzgarla çok hızlı uçtu ve çamura doğru gitti. "Topumuz çamura düşecek!" diye bağırdı arkadaşı. Örümcek Adam hemen elini kaldırdı ve bir ağ attı. Ağ, topu havada yakaladı. Örümcek Adam onu yavaşça kendine çekti. Top tertemiz kalmıştı. "Harika yakaladın!" dedi arkadaşı ve güldü. "Şimdi sıra sende," dedi Örümcek Adam ve topu ona verdi. İkisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "diye bağırdı arkadaşı"
   - Cümle 4: «"Topumuz çamura düşecek!" diye bağırdı arkadaşı.»
   - Açıklama: Ghost-Spider adıyla değil 'arkadaşı' diye anılıyor; kimin arkadaşı olduğu ve kimi gösterdiği açık değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0117` birebir aynı, `@degisim: kırılgan -> renkli` (tutuyorsan), ardından `@onarim: b9f0e2d2dbd869f0d2b73c06fff9cdc028196363`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0118 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@degisim: sabırlı -> ekşi
Örümcek Adam kumsalda ilk kez ekşi bir turşu deneyecekti. Turşu kavanozunu kumun üstüne koydu ve tadına bakmak için sabırsızlandı. Birden örümcek hissi, büyük bir dalganın kavanoza doğru geldiğini haber verdi. Örümcek Adam kavanozu hemen kaptı ve geriye doğru koştu. Dalga, kavanozun durduğu yeri ıslattı ve denize geri çekildi. Kavanozun üstüne tek bir damla bile gelmemişti. Örümcek Adam kapağı açtı ve bir turşu aldı. Onu yavaşça çiğnedi. Tadı çok güzeldi ve bir tane daha yedi. Örümcek Adam bundan sonra yiyeceklerini hep sudan uzak bir yere koydu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi, büyük bir dalganın"
   - Cümle 3: «Birden örümcek hissi, büyük bir dalganın kavanoza doğru geldiğini haber verdi.»
   - Açıklama: Örümcek hissinin haber vermesi soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuk anlamaz.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Tadı çok güzeldi ve bir tane daha yedi"
   - Cümle 9: «Tadı çok güzeldi ve bir tane daha yedi.»
   - Açıklama: Bağlanan iki cümlenin öznesi farklı; 'tadı' özneyken 'yedi' fiili uyumsuz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0118` birebir aynı, `@degisim: sabırlı -> ekşi` (tutuyorsan), ardından `@onarim: 947dfa5cb911bb05c1139ff41617e2408f2bdce9`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0119 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar kağıt paraları dağıtmak üzereydi | hemen koşup açık pencereyi kapattı
@tohum: orumcek_adam-0119
Rüzgar açık pencereden içeri esiyordu. Örümcek Adam gizli evde mağaza oyunu oynuyordu ve masada kağıt paralar vardı. Birden örümcek hissi, rüzgarın paraları dağıtmak üzere olduğunu haber verdi. Örümcek Adam hemen koştu ve pencereyi kapattı. Paraların hepsi masada kaldı. Sonra satmak için tek bir şeyi masanın ortasına koydu. Bu, yepyeni ve mavi bir bluzdu. Örümcek Adam bluzu güzelce katladı. Yanına fiyatını yazdığı küçük bir kağıt koydu. Artık oyun için her şey hazırdı. Örümcek Adam çok sevindi, çünkü oyunu hiç bozulmadı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi, rüzgarın paraları dağıtmak üzere olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi, rüzgarın paraları dağıtmak üzere olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuk için anlaşılmaz.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgarın paraları dağıtmak üzere olduğunu"
   - Cümle 3: «Birden örümcek hissi, rüzgarın paraları dağıtmak üzere olduğunu haber verdi.»
   - Açıklama: Sorun gerçekleşmeden tek hamlede bitiyor; önemsiz, çocuğun önemseyeceği bir sorun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu, yepyeni ve mavi bir bluzdu"
   - Cümle 7: «Bu, yepyeni ve mavi bir bluzdu.»
   - Açıklama: Bluz ve fiyat hazırlığı sorunla ilgisi olmayan işlevsiz ayrıntılar.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yepyeni ve mavi bir bluzdu"
   - Cümle 7: «Bu, yepyeni ve mavi bir bluzdu.»
   - Açıklama: Sorun çözüldükten sonra bluz, katlama ve fiyat kağıdı gibi sorunla ilgisiz ayrıntılar uzayıp gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0119` birebir aynı, ardından `@onarim: 0d6afa264bd8f5eebfe0f6ae78ff517ef124b239`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0121 (deneme 1 -> 2)

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
@plan: uçurtmanın ipi iyi bağlı değildi | ipi açıp sıkıca yeniden bağladı
@tohum: orumcek_adam-0121
Rüzgar sessiz kumsalda esiyordu. Örümcek Adam ilk uçurtmasını yeni bitirmişti. Ama örümcek hissi, ipin iyi bağlı olmadığını haber verdi. İp böyle kalırsa uçurtma uçup gidebilirdi. Örümcek Adam ipi çözdü. Sonra onu sıkı sıkı yeniden bağladı. Uçurtmayı başının üstüne kaldırdı ve koştu. Rüzgar onu yavaş yavaş yukarı taşıdı. Uçurtma limanın üstüne çıktı. Düğüm sağlam kaldı. Kırmızı uçurtma uzun süre mavi gökyüzünde uçtu. Örümcek Adam çok sevindi, çünkü kendi yaptığı ilk uçurtma havalandı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi, ipin iyi bağlı olmadığını haber verdi"
   - Cümle 3: «Ama örümcek hissi, ipin iyi bağlı olmadığını haber verdi.»
   - Açıklama: 'Örümcek hissinin haber vermesi' soyut ve mecazlı bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama örümcek hissi, ipin"
   - Cümle 3: «Ama örümcek hissi, ipin iyi bağlı olmadığını haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Rüzgar onu yavaş yavaş"
   - Cümle 8: «Rüzgar onu yavaş yavaş yukarı taşıdı.»
   - Açıklama: 'Onu' zamirinin uçurtmayı mı Örümcek Adam'ı mı gösterdiği belli değil.
   - Açıklama: 'Onu' zamiri son özne Örümcek Adam'ı da uçurtmayı da gösterebiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0121` birebir aynı, ardından `@onarim: 4f41492bc7fbafffe2d741095c467fab52cd826e`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0122
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'köpük', fiil 'yaslanmak', sıfat 'çamurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: top zıpladı ve yüksek duvarın üstünde kaldı | süper gücüyle duvara tırmanıp topu aldı
@tohum: orumcek_adam-0122
@degisim: çamurlu -> kırmızı
Kumsalda dalgalar beyaz köpükler yapıyordu. Örümcek Adam kırmızı topunu limanın taş duvarına atıyor ve geri gelince tutuyordu. Bir kez top çok yükseğe zıpladı ve duvarın üstünde kaldı. Örümcek Adam duvara yaslandı ve yukarı baktı. Top çok yüksekteydi ve eli ona uzanamadı. Örümcek Adam süper gücüyle duvara kolayca tırmandı. Topu aldı ve yavaşça aşağı indi. Sonra topu havaya atıp yeniden oynamaya başladı. Top bu kez hep eline geri döndü ve Örümcek Adam güldü. Örümcek Adam bundan sonra topunu hep açık kumda, duvardan uzakta attı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "eli ona uzanamadı"
   - Cümle 5: «Top çok yüksekteydi ve eli ona uzanamadı.»
   - Açıklama: 'Eli uzanamadı' doğal değil; 'eli yetişmedi' ya da 'ona uzanamadı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Top bu kez hep eline"
   - Cümle 9: «Top bu kez hep eline geri döndü ve Örümcek Adam güldü.»
   - Açıklama: 'Bu kez' ile 'hep' birlikte uyumsuz; kelime anlamca yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0122` birebir aynı, `@degisim: çamurlu -> kırmızı` (tutuyorsan), ardından `@onarim: c0b8dd6ecb11bf3102734a0e915bf77e543df36c`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0123 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0123
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'fıskiye', fiil 'sürtmek', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: top çok güçlü atıldı ve duvarın üstünde kaldı | süper gücüyle duvara tırmanıp topu indirdi
@tohum: orumcek_adam-0123
@degisim: dolu -> sarı
Fıskiyenin sesi bütün parkta duyuluyordu. Örümcek Adam ile Hulk onun yanında sırayla sarı bir top atıyordu. Hulk çok güçlü attı ve top bahçedeki duvarın üstünde kaldı. Hulk üzgün üzgün duvara baktı. Örümcek Adam süper gücüyle duvara hızla tırmandı. Topu aldı ve aşağı indi. Sıra Örümcek Adam'daydı ve topu yavaşça Hulk'a attı. Hulk topu kocaman elleriyle yakaladı. Sonra sevinçle ellerini birbirine sürttü. Bu kez Hulk da topu hafifçe attı. Örümcek Adam ile Hulk sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hulk onun yanında sırayla"
   - Cümle 2: «Örümcek Adam ile Hulk onun yanında sırayla sarı bir top atıyordu.»
   - Açıklama: 'onun' zamirinin fıskiyeyi mi başka birini mi gösterdiği belli değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sevinçle ellerini birbirine sürttü"
   - Cümle 9: «Sonra sevinçle ellerini birbirine sürttü.»
   - Açıklama: El ovuşturmak sevinç hareketi değil ve Hulk'un elinde top var; fiil duruma uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0123` birebir aynı, `@degisim: dolu -> sarı` (tutuyorsan), ardından `@onarim: 7dafb1019b65084ee090a218c0e66996cac285dc`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0126 (deneme 1 -> 2)

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
Rüzgar parktaki ağaçların yapraklarını sallıyordu. Örümcek Adam ile Hulk çimenlerde vanilyalı bir keki süslemek istiyordu. Hulk ağacın tepesinde altın sarısı bir elma gördü ama ona uzanamadı. "Ağacı sallamak istemiyorum, dallar kırılır," dedi Hulk. Örümcek Adam elmaya bir ağ attı. Ağ elmaya yapıştı ve Örümcek Adam onu yavaşça çekti. Elma dalından koptu ve onun eline düştü. Örümcek Adam elmayı kekin tam ortasına oturttu. "Bu kek şimdi çok güzel oldu!" dedi Hulk. Örümcek Adam çok sevindi, çünkü kekleri artık hazırdı.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onun eline düştü"
   - Cümle 7: «Elma dalından koptu ve onun eline düştü.»
   - Açıklama: 'Onun' zamirinin Örümcek Adam'ı mı Hulk'u mu gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "koptu ve onun eline düştü"
   - Cümle 7: «Elma dalından koptu ve onun eline düştü.»
   - Açıklama: 'Onun' zamirinin Örümcek Adam'ı mı Hulk'u mu gösterdiği belli değil.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çünkü kekleri artık hazırdı"
   - Cümle 10: «Örümcek Adam çok sevindi, çünkü kekleri artık hazırdı.»
   - Açıklama: Tek bir kek varken 'kekleri' biçimi yanlış ya da belirsiz.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çünkü kekleri artık hazırdı"
   - Cümle 10: «Örümcek Adam çok sevindi, çünkü kekleri artık hazırdı.»
   - Açıklama: Hikayede tek bir vanilyalı kek varken son cümlede birden çok kek varmış gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0126` birebir aynı, ardından `@onarim: a28d997afb802d5555117d062f57e7ca8493c350`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0128 (deneme 1 -> 2)

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
Örümcek Adam ile Ghost-Spider parkta bayrak oyunu oynuyordu. Arkadaşı bayrağı kaptı ve havada süzülerek kaçtı. Ama rüzgar bayrağı elinden aldı ve fıskiyenin havuzuna düşürdü. Bayrak suyun tam ortasında yüzüyordu. Örümcek Adam havuzun kenarında bir an düşünceli durdu. Sonra ağ attı ve bayrağı sudan çekti. Bayrak çok ıslanmıştı. İkisi onu güneşte biraz salladı ve kuruttu. Bayrak kuruyunca oyun hemen yeniden başladı. Örümcek Adam çok sevindi, çünkü en sevdikleri oyun hiç yarım kalmamıştı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşı bayrağı kaptı"
   - Cümle 2: «Arkadaşı bayrağı kaptı ve havada süzülerek kaçtı.»
   - Açıklama: 'Arkadaşı' ile kimin kastedildiği adla belirtilmemiş; gönderim belirsiz.
   - Açıklama: İki kahraman adıyla tanıtıldıktan sonra 'Arkadaşı' kimi gösterdiği açık değil; 'Ghost-Spider' denmeli.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Bayrak çok ıslanmıştı"
   - Cümle 7: «Bayrak çok ıslanmıştı.»
   - Açıklama: Bayrak çıkarıldıktan sonra ıslaklık ikinci bir sorun olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0128` birebir aynı, ardından `@onarim: e1584a937d636b5cb6193925633574dfa24cb71a`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0129 (deneme 1 -> 2)

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
@plan: gizli evde garip bir tık tık sesi duyuldu | koridora gidip sesi buldu ve pencereyi kapattı
@tohum: orumcek_adam-0129
Gizli evde güneşli bir sabah başlamıştı. Örümcek Adam masadaki boyalı saksıyı suluyordu. Birden tık tık diye garip bir ses duydu. Örümcek Adam çok merak etti ama sesin nereden geldiğini bulamadı. O anda örümcek hissi ona koridorda bir sorun olduğunu haber verdi. Örümcek Adam hemen koridora yürüdü. Duvarda toplarla dolu bir file asılıydı. Açık pencereden giren rüzgar fileyi sallıyordu. Toplar da duvara çarpıyordu. Tık tık sesi buradan geliyordu. Örümcek Adam pencereyi kapattı. File durdu ve koridor sessiz oldu. Örümcek Adam gülümsedi ve çiçeğini sulamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona koridorda bir sorun olduğunu haber verdi"
   - Cümle 5: «O anda örümcek hissi ona koridorda bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi mecaz ve soyut bir anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona koridorda"
   - Cümle 5: «O anda örümcek hissi ona koridorda bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut bir kavram ve kişileştirme, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0129` birebir aynı, ardından `@onarim: d8c80de1d8c0c50bdea016cddc9b69688902814d`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0132 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0132
- yer: ev (Takımın gizli evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'testi', fiil 'korumak', sıfat 'sevinçli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: davul sesiyle masa titredi ve testi kenara kaydı | sorunu hemen gördü ve testiyi masanın ortasına koydu
@tohum: orumcek_adam-0132
Bir sabah Örümcek Adam gizli evde bir sürpriz hazırlıyordu. Ghost-Spider için bir testiye sarı çiçekler koydu ve testiyi masaya bıraktı. Ama arkadaşı yan odada davul çalıyordu ve masa titriyordu. Testi yavaş yavaş masanın kenarına kaydı. O anda örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Örümcek Adam testiyi hemen iki eliyle tuttu ve masanın ortasına koydu. Altına da yumuşak bir örtü serdi ve testi artık kaymadı. Az sonra arkadaşı odaya süzülerek geldi. "Bu çiçekler senin için," dedi Örümcek Adam. "Ne güzel bir sürpriz!" dedi arkadaşı sevinçli bir sesle. Örümcek Adam çok mutlu oldu, çünkü sürprizini korumuştu.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sorunu hemen gördü ve testiyi masanın ortasına koydu"
   - Cümle 0 (plan satırı): «davul sesiyle masa titredi ve testi kenara kaydı | sorunu hemen gördü ve testiyi masanın ortasına koydu»
   - Açıklama: Gövdede testiyi asıl durduran altına serilen örtü, plan bunu söylemiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ama arkadaşı yan odada"
   - Cümle 3: «Ama arkadaşı yan odada davul çalıyordu ve masa titriyordu.»
   - Açıklama: 'Arkadaşı' kelimesinin Ghost-Spider'ı mı yoksa başka birini mi gösterdiği belli değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Testi yavaş yavaş masanın kenarına kaydı"
   - Cümle 4: «Testi yavaş yavaş masanın kenarına kaydı.»
   - Açıklama: Testinin kayması sorunu ancak dördüncü cümlede söyleniyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 5: «O anda örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber vermesi mecaz, 3 yaşındaki çocuğa uygun değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "O anda örümcek hissi"
   - Cümle 5: «O anda örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'haber verdi' soyut, mecazlı bir anlatım.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Altına da yumuşak bir örtü serdi"
   - Cümle 7: «Altına da yumuşak bir örtü serdi ve testi artık kaymadı.»
   - Açıklama: Testiyi ortaya koyduktan sonra örtü serme üçüncü bir adım olarak ekleniyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Altına da yumuşak bir örtü serdi"
   - Cümle 7: «Altına da yumuşak bir örtü serdi ve testi artık kaymadı.»
   - Açıklama: Örtü sebepsiz beliriyor ve çözümü plan dışında getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0132` birebir aynı, ardından `@onarim: 2a5276e04fd4d5d9fc785752c5abdbbdd4c4158d`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0133
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'toka', fiil 'sıralamak', sıfat 'nazik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: top yüksek bir duvarın üstünde kaldı | süper gücüyle duvara tırmandı ve topu getirdi
@tohum: orumcek_adam-0133
@degisim: toka -> top
Dalgalar kıyıya çarpıyordu. Örümcek Adam ile Hulk kumsalda kabukları sıraladı ve küçük bir kale yaptı. Sonra Hulk topu çok güçlü attı. Top limandaki yüksek bir duvarın üstünde kaldı. "Ben tırmanırsam duvar kırılır," dedi Hulk üzgün bir sesle. "Topu ben getiririm, Hulk," dedi Örümcek Adam. Örümcek Adam süper gücüyle duvara tırmandı. Topu aldı ve yavaşça aşağı indi. Sonra topu Hulk'a verdi. Hulk bu kez topu yavaşça kaleye attı. Top kabukların arasından geçti ve ikisi de güldü. "Çok naziksin, Örümcek Adam, teşekkürler!" dedi Hulk.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra Hulk topu çok güçlü attı"
   - Cümle 3: «Sonra Hulk topu çok güçlü attı.»
   - Açıklama: Top sebepsiz beliriyor ve neden güçlü atıldığı belli değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Top limandaki yüksek bir duvarın üstünde kaldı"
   - Cümle 4: «Top limandaki yüksek bir duvarın üstünde kaldı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
   - Açıklama: Sorun ilk 3 cümlede değil, 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0133` birebir aynı, `@degisim: toka -> top` (tutuyorsan), ardından `@onarim: e485eae6ab13485be05d6e37761e099c34ce9a7c`, sonra gövde.
