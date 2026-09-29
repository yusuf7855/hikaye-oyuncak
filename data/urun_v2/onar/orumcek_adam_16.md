# Editör görevi (onarım): Örümcek Adam, onarım partisi 16

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar16.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0020 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0020
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: kaybolan eşya
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'kart', fiil 'silmek', sıfat 'oynak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: rüzgar arkadaşının kartını uçurdu ve kart kayboldu | duvara tırmanıp kartı aldı ve tozunu sildi
@tohum: orumcek_adam-0020
@degisim: oynak -> renkli
Örümcek Adam ile Hulk parkta renkli kartlarla oynuyordu. Birden rüzgar esti ve Hulk'ın en sevdiği kart uçtu. "Kartım kayboldu, hiçbir yerde göremiyorum!" dedi Hulk. Örümcek Adam çiçek bahçesinin duvarına baktı ve kartı tozlu tepede gördü. Örümcek Adam süper gücüyle duvara tırmandı ve kartı aldı. Sonra aşağı indi ve kartın tozunu eliyle sildi. "İşte kartın, Hulk," dedi Örümcek Adam. Hulk kartı kocaman elleriyle tuttu ve sevinçle güldü. "Teşekkürler, sen harika bir arkadaşsın!" dedi Hulk. Örümcek Adam çok mutlu oldu, çünkü Hulk'ın kartını bulmuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kartı tozlu tepede gördü"
   - Cümle 4: «Örümcek Adam çiçek bahçesinin duvarına baktı ve kartı tozlu tepede gördü.»
   - Açıklama: Tamlama eksik; duvarın tepesi kastediliyorsa 'duvarın tozlu tepesinde' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kartı tozlu tepede gördü"
   - Cümle 4: «Örümcek Adam çiçek bahçesinin duvarına baktı ve kartı tozlu tepede gördü.»
   - Açıklama: 'Tepe' duvarın üstü için yanlış kelime; 'duvarın üstünde' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0020` birebir aynı, `@degisim: oynak -> renkli` (tutuyorsan), ardından `@onarim: 18fd973d1d87800cd78d6f63e491426af0829570`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0024 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0024
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'klasör', fiil 'güzelleştirmek', sıfat 'kokulu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: arkadaşı sürpriz hazır olmadan erken geldi | klasörü sakladı ve arkadaşından gözlerini kapatmasını istedi
@tohum: orumcek_adam-0024
Örümcek Adam parkta Hulk için resimli bir klasör hazırlıyordu. Klasörü güzelleştirmek için içine kokulu çiçek yaprakları koyuyordu. Örümcek hissi Örümcek Adam'a sürprizin bozulacağını haber verdi, çünkü Hulk erkenden geliyordu. Örümcek Adam klasörü hemen arkasına sakladı. "Ne yapıyorsun, Örümcek Adam?" diye sordu Hulk. "Gözlerini kapat ve ona kadar say," dedi Örümcek Adam. Hulk gözlerini kapattı ve saymaya başladı. Örümcek Adam son yaprakları klasöre hızla koydu. "Şimdi gözlerini aç!" dedi Örümcek Adam ve klasörü Hulk'a verdi. Hulk klasörü açtı ve resimleri gördü. "Çok güzel kokuyor, teşekkürler!" dedi Hulk. Örümcek Adam bundan sonra sürprizlerini daha erken hazırladı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "resimli bir klasör hazırlıyordu"
   - Cümle 1: «Örümcek Adam parkta Hulk için resimli bir klasör hazırlıyordu.»
   - Açıklama: 'Klasör' 3 yaşındaki bir çocuğun bilmediği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi Örümcek Adam'a sürprizin bozulacağını haber verdi"
   - Cümle 3: «Örümcek hissi Örümcek Adam'a sürprizin bozulacağını haber verdi, çünkü Hulk erkenden geliyordu.»
   - Açıklama: 'Örümcek hissi' ve 'sürprizin bozulması' soyut, 3 yaşındaki çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sürprizin bozulacağını haber verdi"
   - Cümle 3: «Örümcek hissi Örümcek Adam'a sürprizin bozulacağını haber verdi, çünkü Hulk erkenden geliyordu.»
   - Açıklama: Kartın özellikler alanında örümcek hissi bir sorun olduğunu haber verir; burada sürprizin bozulacağını önceden bildiren bir kehanet gibi kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0024` birebir aynı, ardından `@onarim: af007c1bdea9f6de731d26678d8d57564aa6f23d`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0028 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0028
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'limon', fiil 'susamak', sıfat 'sıcacık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: top limonata şişesine doğru hızla uçtu | zıplayıp topu havada tuttu
@tohum: orumcek_adam-0028
@degisim: limon -> limonata
Örümcek Adam ile Hulk parkta top oynuyordu. Güneş sıcacıktı ve bankta soğuk bir şişe limonata duruyordu. Hulk topu çok güçlü attı ve top şişeye doğru uçtu. O an örümcek hissi Örümcek Adam'a şişenin düşeceğini haber verdi. Örümcek Adam hızla zıpladı ve topu havada tuttu. Şişe yerinde kaldı ve limonata dökülmedi. "Topu çok güzel tuttun, Örümcek Adam!" dedi Hulk ve güldü. "Hadi biraz dinlenelim, çok susadım," dedi Örümcek Adam. İkisi banka oturdu ve limonatayı paylaştı. Sonra Hulk ile Örümcek Adam oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "topu çok güçlü attı"
   - Cümle 3: «Hulk topu çok güçlü attı ve top şişeye doğru uçtu.»
   - Açıklama: 'Güçlü' zarf olarak yanlış kullanılmış; 'çok sert attı' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "top şişeye doğru uçtu"
   - Cümle 3: «Hulk topu çok güçlü attı ve top şişeye doğru uçtu.»
   - Açıklama: Sorun yalnız bir tehlike anı; şişe hiç düşmeden aynı an kurtarılıyor, gerçek bir sorun kurulmuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a şişenin düşeceğini haber verdi"
   - Cümle 4: «O an örümcek hissi Örümcek Adam'a şişenin düşeceğini haber verdi.»
   - Açıklama: His haber vermez; mecaz ve soyut anlatım küçük çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0028` birebir aynı, `@degisim: limon -> limonata` (tutuyorsan), ardından `@onarim: 91e513e7c1e629b6ccbf4e1c44c27ee869183a42`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0032 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0032
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: bir şey yapmak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'fotoğraf', fiil 'güldürmek', sıfat 'karmakarışık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: rüzgar fotoğrafı uçurdu ve fotoğraf dallara takıldı | duvara tırmanıp fotoğrafı dallardan aldı
@tohum: orumcek_adam-0032
@degisim: karmakarışık -> yüksek
Örümcek Adam ile Spin parkta büyük bir resim yapıyordu. Spin bir çiçek fotoğrafına bakıyor ve çiçekler çiziyordu. Birden rüzgar esti ve fotoğrafı havaya uçurdu. Fotoğraf bahçedeki taş duvarın üstündeki yüksek dallara takıldı. "Onu nasıl alacağız?" diye sordu Spin. Örümcek Adam bir örümcek gibi duvara hızla tırmandı. Fotoğrafı dallardan yavaşça çıkardı ve yere indi. Spin fotoğrafa baktı ve son çiçeği de çizdi. Sonra resmin köşesine duvara tırmanan küçük bir Örümcek Adam çizdi. Bu komik çizim Örümcek Adam'ı çok güldürdü. "Teşekkürler, Spin, bu çok eğlenceli oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bahçedeki taş duvarın üstündeki"
   - Cümle 4: «Fotoğraf bahçedeki taş duvarın üstündeki yüksek dallara takıldı.»
   - Açıklama: Hikaye parkta başlıyor ama fotoğraf bir bahçedeki duvara takılıyor; yer belirsizleşiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0032` birebir aynı, `@degisim: karmakarışık -> yüksek` (tutuyorsan), ardından `@onarim: 6532ab2b1c2c0d9938ad315e01c66f950f10d1b4`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0036 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0036
- yer: ev (Takımın gizli evi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'dilim', fiil 'açılmak', sıfat 'minicik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: yüksek pencere açıldı ve içeri yağmur girdi | arkadaşından yardım istedi ve o pencereyi kapadı
@tohum: orumcek_adam-0036
Örümcek Adam gizli evde bir dilim karpuz yiyordu. Birden örümcek hissi ona içeri yağmur girdiğini haber verdi. Örümcek Adam döndü ve rüzgarla açılan pencereyi gördü. Pencere çok yüksekteydi ve evin içinde tırmanmak yasaktı. "Ghost-Spider, bana yardım eder misin?" diye sordu Örümcek Adam. "Tabii, geliyorum," dedi arkadaşı. Arkadaşı havada süzüldü ve pencereyi kapadı. Sonra pencerenin minicik kolunu sıkıca çevirdi. Yağmur artık içeri girmiyordu. Örümcek Adam arkadaşına da bir dilim karpuz verdi. Örümcek Adam çok mutluydu, çünkü arkadaşı ona hemen yardım etmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona içeri"
   - Cümle 2: «Birden örümcek hissi ona içeri yağmur girdiğini haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve o pencereyi kapadı"
   - Cümle 7: «Arkadaşı havada süzüldü ve pencereyi kapadı.»
   - Açıklama: 'o' zamiri arkadaşı mı gösteriyor yoksa 'o pencere' mi belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0036` birebir aynı, ardından `@onarim: ede845f05cba87f49d7acf09c7a3512a402dbd84`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0038 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0038
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'fındık', fiil 'kapamak', sıfat 'memnun'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: rüzgar esti ve taşın yanından tık tık sesi geldi | sesi yapan torbayı buldu ve ağzını kapadı
@tohum: orumcek_adam-0038
@degisim: memnun -> mutlu
Örümcek Adam ile Ghost-Spider kumsalda fındık yiyordu. Fındık torbası büyük bir taşın üstünde duruyordu. Birden rüzgar esti ve taşın yanından tık tık diye bir ses geldi. Örümcek hissi Örümcek Adam'a torbanın düştüğünü haber verdi. İkisi hemen taşa baktı. Fındıklar torbanın ağzından taşa tek tek dökülüyordu. Tık tık sesini bu fındıklar yapıyordu. Örümcek Adam torbayı kaldırdı ve ağzını sıkıca kapadı. Arkadaşı taşın üstündeki fındıkları topladı ve torbaya koydu. "Sesi bulduk ve fındıklar kaybolmadı, çok mutluyum!" dedi Örümcek Adam.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve taşın yanından tık tık sesi geldi"
   - Cümle 0 (plan satırı): «rüzgar esti ve taşın yanından tık tık sesi geldi | sesi yapan torbayı buldu ve ağzını kapadı»
   - Açıklama: Sorun yalnız bir ses olarak kuruluyor; rüzgarın fındıkları nasıl döktüğü akla yatkın bir sebeple söylenmiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve taşın yanından tık tık"
   - Cümle 3: «Birden rüzgar esti ve taşın yanından tık tık diye bir ses geldi.»
   - Açıklama: Rüzgarın torbadan fındık dökmesi akla yatkın değil ve sorun yalnız bir ses olarak kuruluyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "torbanın düştüğünü haber verdi"
   - Cümle 4: «Örümcek hissi Örümcek Adam'a torbanın düştüğünü haber verdi.»
   - Açıklama: His haber vermez ve torba düşmemişti; fiil öznesine ve olaya uymuyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi Örümcek Adam'a"
   - Cümle 4: «Örümcek hissi Örümcek Adam'a torbanın düştüğünü haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Örümcek hissi Örümcek Adam'a torbanın düştüğünü haber verdi"
   - Cümle 4: «Örümcek hissi Örümcek Adam'a torbanın düştüğünü haber verdi.»
   - Açıklama: Torbanın düştüğü söyleniyor ama torba taşın üstünde duruyor ve fındıklar taşa dökülüyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "torbanın düştüğünü haber verdi"
   - Cümle 4: «Örümcek hissi Örümcek Adam'a torbanın düştüğünü haber verdi.»
   - Açıklama: Torbanın düştüğü söyleniyor ama torba taşın üstünde fındık döküyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0038` birebir aynı, `@degisim: memnun -> mutlu` (tutuyorsan), ardından `@onarim: 17b5640390a123bb77176810a1502872831a9d50`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0040 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0040
- yer: ev (Takımın gizli evi.)
- tema: yağmur ya da kar günü
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'süs', fiil 'süslenmek', sıfat 'ışıltılı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: yağmur yüzünden parka gidemediler ve sıkıldılar | duvara tırmanıp süsleri arkadaşıyla birlikte astı
@tohum: orumcek_adam-0040
Dışarıda yağmur şıp şıp yağıyordu. Örümcek Adam ile Hulk bu yüzden parka gidemedi. İkisi gizli evde oturuyordu ve biraz sıkılmıştı. "Hulk, evi süsleyelim mi?" diye sordu Örümcek Adam. "Evet, çok güzel olur!" dedi Hulk. Örümcek Adam dolaptan ışıltılı süslerle dolu bir kutu çıkardı. Hulk süsleri kapıya ve pencereye astı. Az sonra yağmur dindi. Örümcek Adam en büyük yıldız süsünü aldı ve dışarı çıktı. Süper gücüyle evin dış duvarına tırmandı. Yıldızı pencerenin üstüne taktı. Sonunda bütün ev süslendi. Süsler pırıl pırıl parlıyordu. "Yağmurlu gün bile çok eğlenceli oldu, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "İkisi gizli evde oturuyordu"
   - Cümle 3: «İkisi gizli evde oturuyordu ve biraz sıkılmıştı.»
   - Açıklama: İyelik eki eksik; 'gizli evlerinde' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Az sonra yağmur dindi"
   - Cümle 8: «Az sonra yağmur dindi.»
   - Açıklama: Yağmur sebepsizce dinip dış duvara tırmanmayı mümkün kılıyor ve sıkılma sorununu kendiliğinden ortadan kaldırıyor.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "aldı ve dışarı çıktı"
   - Cümle 9: «Örümcek Adam en büyük yıldız süsünü aldı ve dışarı çıktı.»
   - Açıklama: Hikaye evin içinde başlıyor ama sahne evin dışına, dış duvara taşınıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Süper gücüyle evin dış duvarına tırmandı"
   - Cümle 10: «Süper gücüyle evin dış duvarına tırmandı.»
   - Açıklama: Ev süslemek için evin duvarına tırmanıp pencerenin üstüne süs takmak, güvenli kullanım satırının kaçındığı ev ve pencere çevresi tırmanmasına yakın, çocuğun taklit edebileceği bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0040` birebir aynı, ardından `@onarim: 29069c168e7983bed8b81f7024f68b244b90fef6`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0042 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0042
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'tuz', fiil 'eğmek', sıfat 'hazır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: arkadaşı salıncağa binmek için arkada sessizce bekliyordu | arkasına baktı ve sırayı arkadaşına verdi
@tohum: orumcek_adam-0042
@degisim: tuz -> salıncak
Parkın oyun alanında tek bir salıncak vardı. Örümcek Adam salıncakta uzun uzun sallanıyordu. Hulk da binmek istiyordu ama arkada sessizce bekliyordu. Birden örümcek hissi Örümcek Adam'a arkada bir sorun olduğunu haber verdi. Örümcek Adam arkasına baktı ve arkadaşını gördü. Hulk başını eğmişti ve biraz üzgündü. Örümcek Adam hemen salıncaktan indi. "Sıra sende, Hulk! On kere sallan, sonra sıra bende," dedi Örümcek Adam. Hulk sevindi ve salıncağa oturdu. Örümcek Adam yüksek sesle saydı. Sonra yer değiştirdiler. "Hazır mısın, Örümcek Adam?" diye sordu Hulk. Bu kez Hulk saydı. İkisi sırayla sallandı ve çok güldü. "Sırayla oynamak çok eğlenceli, Hulk!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "arkada bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden örümcek hissi Örümcek Adam'a arkada bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissinin haber vermesi' soyut ve mecazlı bir anlatımdır.
   - Açıklama: Örümcek hissinin haber vermesi soyut ve mecazlı bir anlatım, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0042` birebir aynı, `@degisim: tuz -> salıncak` (tutuyorsan), ardından `@onarim: 7062bb2698851bd8e443cf3ad611616322ca181a`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0044 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0044
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gül', fiil 'aydınlanmak', sıfat 'sıkı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar kum gemisinin bayrağını düşürmek üzereydi | çubuğu tuttu ve kuma daha derine soktu
@tohum: orumcek_adam-0044
@degisim: gül -> bayrak
Kumsal güneşle aydınlanmıştı ve güçlü bir rüzgar esiyordu. Örümcek Adam kumdan bir gemi yapmıştı ve gemi oyunu oynuyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Bayrağın çubuğu kumda sağa sola eğiliyordu. Örümcek Adam çubuğu hemen sıkı sıkı tuttu. Onu kuma daha derine soktu. Çubuk artık kumda dik durdu. Rüzgar yine esti ama bayrak düşmedi. Örümcek Adam gemisinin önüne oturdu ve gülümsedi. Kırmızı bayrak rüzgarda sallanıyordu. Örümcek Adam çok mutluydu, çünkü gemisinin bayrağı yine yerinde duruyordu.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çubuğu tuttu ve kuma daha derine soktu"
   - Cümle 0 (plan satırı): «rüzgar kum gemisinin bayrağını düşürmek üzereydi | çubuğu tuttu ve kuma daha derine soktu»
   - Açıklama: Gövdede çubuk kuma daha derine sokulmuyor, yalnız tutuluyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' soyut, 3 yaşındaki çocuğun anlamayacağı bir anlatım.
   - Açıklama: Hissin haber vermesi mecazlı ve soyut bir anlatım, küçük çocuğa uygun değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: İlk 3 cümlede yalnız 'bir sorun' olduğu söyleniyor; bayrağın eğilmesi ancak 4. cümlede açıklanıyor.
   - Açıklama: İlk üç cümlede yalnız belirsiz bir sorundan söz ediliyor; bayrak çubuğunun eğilmesi ancak 4. cümlede söyleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: İlk 3 cümlede sorunun ne olduğu söylenmiyor; eğilen çubuk ancak 4. cümlede açıklanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0044` birebir aynı, `@degisim: gül -> bayrak` (tutuyorsan), ardından `@onarim: 557f8a1914b9d2137dde0d28586b615f5a2a0ac7`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0046 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0046
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'tekne', fiil 'kaybetmek', sıfat 'zarif'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: rüzgar hafif tekneleri çalıya doğru itiyordu | tekneleri çalısı olmayan başka bir suya götürdü
@tohum: orumcek_adam-0046
@degisim: zarif -> hafif
Bir sabah parkta hafif bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider bir su birikintisinde kağıt tekne yarışı yapıyordu. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Rüzgar hafif tekneleri suyun kenarındaki çalıya doğru itiyordu. Örümcek Adam tekneleri çalıda kaybetmek istemedi. Hemen iki tekneyi de sudan aldı. Onları çalısı olmayan başka bir su birikintisine götürdü ve suya bıraktı. Bu kez rüzgar tekneleri suyun öbür kenarına itti. Yarışta arkadaşının teknesi daha hızlı gitti. Arkadaşı sevinçle güldü. Örümcek Adam yarışı kaybetti ama o da güldü. Örümcek Adam bundan sonra tekneleri hep çalıdan uzak suya bıraktı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: Haber veren 'örümcek hissi' soyut bir kavram ve kişileştirme.
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım; 3 yaşındaki çocuk için uygun değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: İlk 3 cümlede yalnız 'bir sorun' olduğu söyleniyor; rüzgarın tekneleri çalıya itmesi ancak 4. cümlede açıklanıyor.
   - Açıklama: 3. cümle yalnız 'bir sorun' olduğunu söylüyor; sorunun ne olduğu ancak 4. cümlede açıklanıyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "tekneleri hep çalıdan uzak suya bıraktı"
   - Cümle 12: «Örümcek Adam bundan sonra tekneleri hep çalıdan uzak suya bıraktı.»
   - Açıklama: Hikaye yarışın kaybedilmesinden sonra sıcak bir kapanış yerine çıplak bir alışkanlık cümlesiyle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0046` birebir aynı, `@degisim: zarif -> hafif` (tutuyorsan), ardından `@onarim: 23c8c4b55e585c4a892e5efba64cf2254c6e7405`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0047 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0047
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: kaybolan eşya
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'salıncak', fiil 'taşmak', sıfat 'siyah'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar siyah kovayı yuvarladı ve kova kayboldu | kumdaki izi takip etti ve kovayı buldu
@tohum: orumcek_adam-0047
@degisim: salıncak -> kova
Örümcek Adam kumsalda kumdan bir kale yapıyordu. O sırada rüzgar siyah kovasını yuvarladı ve uzağa götürdü. Bunu görmedi ama örümcek hissi ona bir sorun olduğunu haber verdi. Hemen yanına baktı ve kovasının yerinde olmadığını gördü. Sonra kumda uzun bir iz gördü. Örümcek Adam izi yavaş yavaş takip etti. İz onu suyun kenarına götürdü. Siyah kova orada, kumun üstünde dik duruyordu. Dalgalar kovayı doldurmuştu ve su kovadan taşmıştı. Örümcek Adam kovayı aldı ve kalesinin yanına geri döndü. Kovadaki suyu kuma döktü. Islak kumla kalesine yeni bir kule yaptı. Örümcek Adam çok sevindi, çünkü kaybolan kovasını kendisi bulmuştu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Bunu görmedi ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir"
   - Cümle 3: «Bunu görmedi ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "İz onu suyun kenarına götürdü"
   - Cümle 7: «İz onu suyun kenarına götürdü.»
   - Açıklama: İz birini götürmez; mecazlı anlatım.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kumun üstünde dik duruyordu"
   - Cümle 8: «Siyah kova orada, kumun üstünde dik duruyordu.»
   - Açıklama: Rüzgarın yuvarladığı kova suyun kenarında dik duruyor ve ağzına kadar dolu; yuvarlanan kovanın dik durması çelişkili.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "orada, kumun üstünde dik duruyordu"
   - Cümle 8: «Siyah kova orada, kumun üstünde dik duruyordu.»
   - Açıklama: Rüzgarla yuvarlanan kovanın dik durup dalgayla dolması inandırıcı değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0047` birebir aynı, `@degisim: salıncak -> kova` (tutuyorsan), ardından `@onarim: 4ad0ba01ba62e74a0369ae9e330129a7631f4a4d`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0049 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0049
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'havlu', fiil 'küçültmek', sıfat 'tuhaf'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: sürpriz balonlarından birinin ipi çözüldü ve duvara takıldı | duvara tırmanıp balonu aldı ve banka bağladı
@tohum: orumcek_adam-0049
@degisim: küçültmek -> bağlamak
Bir sabah Örümcek Adam parkta Spin için bir sürpriz hazırlıyordu. Çimlere büyük bir havlu serdi ve üstüne kurabiyeler koydu. Ama tuhaf bir şey gördü, bankın yanındaki üç balondan birinin ipi çözülmüştü. O balon uçmuş ve duvarın üstüne takılmıştı. Örümcek Adam hemen duvarın yanına koştu. Duvara hızla tırmandı. Balonu dikkatle aldı ve aşağı indi. Sonra ipi banka sıkıca bağladı. Az sonra Spin parka geldi. "Sürpriz, Spin!" dedi Örümcek Adam. Spin havluyu, kurabiyeleri ve üç balonu gördü. "Teşekkürler, Örümcek Adam, bu çok güzel bir sürpriz!" dedi Spin.
```

**Hakem bulguları (4):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "tuhaf bir şey gördü, bankın yanındaki"
   - Cümle 3: «Ama tuhaf bir şey gördü, bankın yanındaki üç balondan birinin ipi çözülmüştü.»
   - Açıklama: Açıklama öncesinde virgül yerine iki nokta kullanılmalı ya da cümle bölünmeli.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "tuhaf bir şey gördü, bankın"
   - Cümle 3: «Ama tuhaf bir şey gördü, bankın yanındaki üç balondan birinin ipi çözülmüştü.»
   - Açıklama: Açıklama öncesinde virgül yerine iki nokta gerekir.
   - Açıklama: Açıklama öncesinde virgül değil iki nokta gerekir.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "birinin ipi çözülmüştü"
   - Cümle 3: «Ama tuhaf bir şey gördü, bankın yanındaki üç balondan birinin ipi çözülmüştü.»
   - Açıklama: Balonun ipinin neden çözüldüğü söylenmiyor.
   - Açıklama: Balonun ipinin neden çözüldüğü hiç söylenmiyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Duvara hızla tırmandı"
   - Cümle 6: «Duvara hızla tırmandı.»
   - Açıklama: Balonu almak için duvara tırmanma süper güç olarak çerçevelenmeden anlatılıyor ve çocuk bunu taklit edebilir; bu, güvenli özellik kullanımı satırına aykırıdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0049` birebir aynı, `@degisim: küçültmek -> bağlamak` (tutuyorsan), ardından `@onarim: 042a276d4784dc0fd362d9778785ea287c2db6d0`, sonra gövde.
