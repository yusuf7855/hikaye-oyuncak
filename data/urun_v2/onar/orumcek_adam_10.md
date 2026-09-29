# Editör görevi (onarım): Örümcek Adam, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar10.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0003 (deneme 5 -> 6)

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
Parkta rüzgar sert esiyordu. Birden örümcek hissi Örümcek Adam'a piknik masasında bir sorun olduğunu haber verdi. Rüzgar büyük bir dalı kırmış ve dal piknik masasının üstüne düşmüştü. Örümcek Adam, Hulk ile orada piknik yapacaktı ve çok heyecanlıydı. Elindeki fiyonklu kek kutusunu çimenlere bıraktı ve dalı itti. Ama dal çok ağırdı ve hiç kıpırdamadı. Biraz sonra Hulk da masaya geldi. "Hulk, bu dalı kaldırabilir misin?" diye sordu Örümcek Adam. Hulk dalı kolayca kaldırdı ve ağaçların yanına taşıdı. Örümcek Adam kutuyu masaya koydu ve açtı. İki arkadaş keki birlikte yedi. Örümcek Adam çok sevindi, çünkü Hulk'tan yardım istemiş ve keki masada yemişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi Örümcek Adam'a"
   - Cümle 2: «Birden örümcek hissi Örümcek Adam'a piknik masasında bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve haber vermesi 3 yaşındaki çocuk için soyut bir kavram.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a piknik"
   - Cümle 2: «Birden örümcek hissi Örümcek Adam'a piknik masasında bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0003` birebir aynı, ardından `@onarim: bfc393e07e9fcfd81765833f2c203ef24d5068ef`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0012 (deneme 4 -> 5)

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
@plan: masanın yamuk ayağı yüzünden tencere kayıyordu | tencereyi tuttu ve yamuk ayağın altına kağıt koydu
@tohum: orumcek_adam-0012
@degisim: tekrarlamak -> karıştırmak
Örümcek Adam gizli evde yemek yapma oyunu oynuyordu. Oyuncak tencereye bezelye taneleri koyuyordu ve masanın bir ayağı yamuktu. Bu yüzden masa sallanıyordu ve tencere kenara doğru kayıyordu. Birden örümcek hissi ona tencerenin düşeceğini haber verdi. Örümcek Adam tencereyi hemen iki eliyle tuttu. Sonra bir kağıdı katladı ve yamuk ayağın altına koydu. Masa artık hiç sallanmıyordu. Örümcek Adam tencereyi ortaya koydu ve kalan taneleri tek tek ekledi. Sonra yemeği oyuncak kaşıkla güzelce karıştırdı. Örümcek Adam oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona tencerenin"
   - Cümle 4: «Birden örümcek hissi ona tencerenin düşeceğini haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona tencerenin düşeceğini haber verdi"
   - Cümle 4: «Birden örümcek hissi ona tencerenin düşeceğini haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0012` birebir aynı, `@degisim: tekrarlamak -> karıştırmak` (tutuyorsan), ardından `@onarim: 83b64b4617074c6264a1980f5703e0618e897383`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0013 (deneme 4 -> 5)

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
@plan: küçük bir dalga kumdan gemiye doğru geliyordu | geminin önüne hemen kumdan bir duvar yaptı
@tohum: orumcek_adam-0013
@degisim: tanışmak -> denemek
Örümcek Adam yağmurlu bir sabah kumsala geldi. Islak kumdan ilk kez büyük bir gemi yapmayı denedi. Gemiye iki direk yaptı ve renkli taşlarla süsledi. Birden örümcek hissi ona gemiye küçük bir dalga geleceğini haber verdi. Örümcek Adam hemen geminin önüne uzun bir kum duvarı yaptı. Az sonra dalga kumsala kadar geldi. Su duvara çarptı ve iki yana aktı. Gemi hiç bozulmadı. Örümcek Adam çok sevindi, çünkü kumdan ilk gemisini dalgadan korumuştu.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Gemiye iki direk yaptı ve renkli taşlarla süsledi.»
   - Açıklama: İlk üç cümlede sorun yok; dalga tehlikesi ancak 4. cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona gemiye küçük bir dalga geleceğini haber verdi"
   - Cümle 4: «Birden örümcek hissi ona gemiye küçük bir dalga geleceğini haber verdi.»
   - Açıklama: His haber vermez; soyut kavram ve mecaz küçük çocuğa uygun değil.
   - Açıklama: Haber veren bir 'his' soyut bir kavram ve kişileştirme; 3 yaşındaki çocuk için uygun değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "gemiye küçük bir dalga geleceğini"
   - Cümle 4: «Birden örümcek hissi ona gemiye küçük bir dalga geleceğini haber verdi.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0013` birebir aynı, `@degisim: tanışmak -> denemek` (tutuyorsan), ardından `@onarim: 3c8fe110172428547bccc7da6ca22f61733fac5c`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0015 (deneme 4 -> 5)

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
@plan: bir dalga kumdaki sandviç çantasına doğru geliyordu | çantayı dalga gelmeden kuru kuma taşıdı
@tohum: orumcek_adam-0015
Kumsalda Spin'in karnı yüksek sesle guruldadı. Spin sandviç çantasını suya yakın bıraktı ve Örümcek Adam ile çeşmeye yürüdü. Birden örümcek hissi Örümcek Adam'a bir dalganın çantaya geleceğini haber verdi. Çantada Spin'in yaptığı özel sandviçler vardı. Örümcek Adam çantayı hemen kuru kuma taşıdı. Az sonra dalga geldi ve çantanın durduğu yeri ıslattı. Ama sandviçler kuru kaldı. Örümcek Adam çantayı Spin'e verdi. İki arkadaş ellerini çeşmede yıkadı ve kuma oturdu. Spin sandviçlerden birini Örümcek Adam'a uzattı. "Teşekkürler, Örümcek Adam, sandviçler ıslanmadı!" dedi Spin.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi Örümcek Adam'a"
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a bir dalganın çantaya geleceğini haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve onun haber vermesi 3 yaşındaki çocuğun anlayamayacağı bir mecaz.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım; 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0015` birebir aynı, ardından `@onarim: 77bd2ab995c257637b5746e021e0ac57d7d474a7`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0020 (deneme 3 -> 4)

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
Örümcek Adam ile Hulk parkta renkli kartlarla oynuyordu. Birden rüzgar esti ve Hulk'ın en sevdiği kart uçtu. "Kartım kayboldu, hiçbir yerde göremiyorum!" dedi Hulk. Örümcek Adam çiçek bahçesinin duvarına baktı ve tepede kartı gördü. Örümcek Adam süper gücüyle duvara tırmandı ve kartı aldı. Kartın resmi tozdan görünmüyordu. Örümcek Adam aşağı indi ve tozu eliyle sildi. "İşte kartın, Hulk," dedi Örümcek Adam. Hulk kartı kocaman elleriyle tuttu ve sevinçle güldü. "Teşekkürler, sen harika bir arkadaşsın!" dedi Hulk. Örümcek Adam çok mutlu oldu, çünkü Hulk'ın kartını bulmuştu.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Kartın resmi tozdan görünmüyordu"
   - Cümle 6: «Kartın resmi tozdan görünmüyordu.»
   - Açıklama: Az önce uçan kartın tozla kaplanması sebepsiz ikinci bir sorun ekliyor.
   - Açıklama: Kayıp kart bulunduktan sonra tozlu kart ikinci bir sorun olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0020` birebir aynı, `@degisim: oynak -> renkli` (tutuyorsan), ardından `@onarim: f05710bfcac7286688d494d33ae9cc834365b302`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0024 (deneme 3 -> 4)

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
Örümcek Adam parkta Hulk için resimli bir klasör hazırlıyordu. Klasörü güzelleştirmek için içine kokulu çiçek yaprakları koyuyordu. Birden örümcek hissi ona Hulk'ın erkenden geldiğini haber verdi. Ama sürpriz daha bitmemişti. Örümcek Adam klasörü hemen arkasına sakladı. "Ne yapıyorsun, Örümcek Adam?" diye sordu Hulk. "Gözlerini kapat ve ona kadar say, lütfen," dedi Örümcek Adam. Hulk gözlerini kapattı ve saymaya başladı. Örümcek Adam son yaprakları klasöre hızla koydu. "Şimdi gözlerini aç!" dedi Örümcek Adam ve klasörü Hulk'a verdi. Hulk klasörü açtı ve resimleri gördü. "Çok güzel kokuyor, teşekkürler!" dedi Hulk. Örümcek Adam bundan sonra sürprizlerini daha erken hazırladı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona Hulk'ın"
   - Cümle 3: «Birden örümcek hissi ona Hulk'ın erkenden geldiğini haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona"
   - Cümle 3: «Birden örümcek hissi ona Hulk'ın erkenden geldiğini haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuk için anlaşılır değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissi ona Hulk'ın erkenden geldiğini haber verdi"
   - Cümle 3: «Birden örümcek hissi ona Hulk'ın erkenden geldiğini haber verdi.»
   - Açıklama: Kartın özellik alanında örümcek hissi bir sorunu haber verir; burada arkadaşın erken gelişini haber veren bir algı olarak kullanılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ona Hulk'ın erkenden geldiğini haber verdi"
   - Cümle 3: «Birden örümcek hissi ona Hulk'ın erkenden geldiğini haber verdi.»
   - Açıklama: Kartın özellikler alanına göre örümcek hissi bir sorun olduğunu haber verir; burada bir arkadaşın gelişini bildiren bir sezgi olarak kullanılıyor.
5. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "ona Hulk'ın erkenden geldiğini haber verdi"
   - Cümle 3: «Birden örümcek hissi ona Hulk'ın erkenden geldiğini haber verdi.»
   - Açıklama: Kartın özellikler alanındaki örümcek hissi tanımına aykırı olarak his kimin geldiğini söyleyen bir bilgi kaynağı gibi gösteriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0024` birebir aynı, ardından `@onarim: 956fd8905d61c9ece833117be598d715fad0da2b`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0025 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0025
- yer: ev (Takımın gizli evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'karnabahar', fiil 'ışıldamak', sıfat 'zor'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: yıldızı yüksek tavana asmak zordu | duvara tırmanıp yıldızı tavana astı
@tohum: orumcek_adam-0025
@degisim: karnabahar -> yıldız
Bir sabah Örümcek Adam gizli evde arkadaşı için bir sürpriz hazırlıyordu. Tavana parlak sarı kağıttan bir yıldız asmak istiyordu. Ama tavan çok yüksekti ve yıldızı oraya asmak zordu. Örümcek Adam yıldızı bir eline aldı. Sonra süper gücüyle ellerini duvara yapıştırdı ve tırmandı. Yıldızı ipinden tavana astı ve yavaşça aşağı indi. Az sonra kapı açıldı ve arkadaşı Ghost-Spider içeri girdi. Kapıdan gelen ışık yıldıza vurdu ve yıldız ışıldadı. "Bu yıldız benim için mi?" diye sordu arkadaşı. "Evet, senin için bir sürpriz!" dedi Örümcek Adam. Arkadaşı sevinçle güldü ve havada süzüldü. Sonra iki arkadaş yıldızın altında mutlu mutlu dans etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ellerini duvara yapıştırdı ve tırmandı"
   - Cümle 5: «Sonra süper gücüyle ellerini duvara yapıştırdı ve tırmandı.»
   - Açıklama: Ev içinde tavana süs asmak için tırmanma, güvenli özellik kullanımı satırındaki ev içi tırmanma yasağına aykırı ve çocukça taklit edilebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0025` birebir aynı, `@degisim: karnabahar -> yıldız` (tutuyorsan), ardından `@onarim: 32feea060821068303f9c5c83b73b0087bb7db84`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0026 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0026
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'çimen', fiil 'yükselmek', sıfat 'hazırlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: rüzgar döndü ve uçurtma ağaca doğru indi | ipi sıkıca tuttu ve ağaçtan uzağa koştu
@tohum: orumcek_adam-0026
@degisim: hazırlıklı -> komik
Parkta geniş çimenlerin üstünde hafif bir rüzgar esiyordu. Örümcek Adam ile Spin komik yüzlü bir uçurtma uçuruyordu. Birden rüzgar döndü ve uçurtma büyük bir ağaca doğru indi. Örümcek Adam o an Spin'e bakıyordu ve uçurtmayı görmedi. Ama örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam hemen döndü, ipi sıkıca tuttu ve ağaçtan uzağa koştu. Uçurtma dallara değmeden yeniden yükseldi. Gökyüzünde uçurtmanın yüzü sallandı ve iki arkadaş kahkahalarla güldü. Sonra çimenlerde koşarak oyuna devam ettiler. Örümcek Adam bundan sonra uçurtmayı ağaçlardan uzakta uçurdu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 5: «Ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' soyut ve mecazlı, 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama örümcek hissi ona"
   - Cümle 5: «Ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0026` birebir aynı, `@degisim: hazırlıklı -> komik` (tutuyorsan), ardından `@onarim: a905d10bebb4a8bf3d9850ef09e9dcf8c5546160`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0028 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Örümcek Adam ile Hulk parkta top oynuyordu. Güneş sıcacıktı ve bankta soğuk bir şişe limonata duruyordu. Hulk topa çok güçlü vurdu ve top şişeye doğru uçtu. O an örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Örümcek Adam hızla zıpladı ve topu havada tuttu. Şişe yerinde kaldı ve limonata dökülmedi. "Eyvah, topa çok güçlü vurdum!" dedi Hulk ve kahkahalarla güldü. "Hadi biraz dinlenelim, çok susadım," dedi Örümcek Adam. İkisi banka oturdu ve limonatayı paylaştı. Sonra Hulk ile Örümcek Adam oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 4: «O an örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: Soyut 'örümcek hissi' kavramı bir kişi gibi haber veriyor; 3 yaşındaki çocuğa uygun olmayan soyut ve mecazlı anlatım.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "O an örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 4: «O an örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0028` birebir aynı, `@degisim: limon -> limonata` (tutuyorsan), ardından `@onarim: 0f06a824e1e21bcdbfd568cf885430a51b621611`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0029 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0029
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'kostüm', fiil 'homurdanmak', sıfat 'faydalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: topa hızlı vurdu ve davul çubuğu suya düştü | özür diledi ve çubuğu ağla kıyıya çekti
@tohum: orumcek_adam-0029
@degisim: homurdanmak -> üzülmek
Örümcek Adam kumsalda topla oynuyordu ve Ghost-Spider onun yanında davul çalıyordu. Örümcek Adam topa çok hızlı vurdu ve top arkadaşının çubuğuna çarptı. Davul çubuğu suya düştü ve dalgalarla uzaklaşmaya başladı. Arkadaşı çok üzüldü. "Özür dilerim, dikkat etmedim," dedi Örümcek Adam. Sonra suya doğru ağ attı. Ağ çubuğa yapıştı ve Örümcek Adam onu yavaşça kıyıya çekti. Islak çubuğu arkadaşına geri verdi. Arkadaşı çubuğu kostümüyle kuruladı. "Teşekkürler, Örümcek Adam, ağın çok faydalı oldu!" dedi arkadaşı ve gülümsedi. Sonra yeniden davul çaldı ve Örümcek Adam onu mutlu mutlu dinledi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağın çok faydalı oldu"
   - Cümle 10: «"Teşekkürler, Örümcek Adam, ağın çok faydalı oldu!" dedi arkadaşı ve gülümsedi.»
   - Açıklama: 'Faydalı' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Faydalı' soyut bir kelime, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0029` birebir aynı, `@degisim: homurdanmak -> üzülmek` (tutuyorsan), ardından `@onarim: 6648f4432738f5fd4fc8f91b3c0dc1a0857c96fc`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0030 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0030
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'bileklik', fiil 'dağılmak', sıfat 'soslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: arkadaşının bilekliği suya düştü ve kayboldu | suda parlayan şeye ağ atıp bilekliği çekti
@tohum: orumcek_adam-0030
@degisim: soslu -> renkli
Kumsalda serin bir rüzgar esiyordu. Örümcek Adam ile Ghost-Spider kıyıda oturuyordu. Arkadaşı dalgalarla oynarken bilekliğini suya düşürdü. Bileklik köpüklerin altında kayboldu. Sonra köpükler dağıldı ve suda küçük bir ışık göründü. Örümcek Adam bu ışığı merak etti. Işık kıyıdan biraz uzaktaydı. Örümcek Adam ağ attı ve parlayan şeyi yakaladı. Sonra ağı yavaşça kendine çekti. Ağın içinde arkadaşının renkli bilekliği vardı. "Bu benim bilekliğim!" dedi arkadaşı ve onu hemen koluna taktı. Örümcek Adam çok sevindi, çünkü suda parlayan şeyin ne olduğunu bulmuştu.
```

**Hakem bulguları (6):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşı dalgalarla oynarken bilekliğini"
   - Cümle 3: «Arkadaşı dalgalarla oynarken bilekliğini suya düşürdü.»
   - Açıklama: 'Arkadaşı' kimi gösteriyor belli değil; Ghost-Spider adıyla bağlanmıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşı dalgalarla oynarken"
   - Cümle 3: «Arkadaşı dalgalarla oynarken bilekliğini suya düşürdü.»
   - Açıklama: Ghost-Spider adıyla tanıtıldıktan sonra hep 'arkadaşı' diye anılıyor ve kimin kastedildiği açıkça belli değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "suda küçük bir ışık göründü"
   - Cümle 5: «Sonra köpükler dağıldı ve suda küçük bir ışık göründü.»
   - Açıklama: Bilekliğin suda neden parladığı söylenmiyor; ışık çözümü sebepsizce getiriyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Örümcek Adam bu ışığı merak etti"
   - Cümle 6: «Örümcek Adam bu ışığı merak etti.»
   - Açıklama: Örümcek Adam bilekliği aramak için değil ışığı merak ettiği için harekete geçiyor; çözüm soruna doğrudan yönelmiyor.
   - Açıklama: Figür bilekliği aramaya değil merak ettiği ışığa yöneliyor; çözüm sorunun sebebine doğrudan yönelmiyor.
5. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "dedi arkadaşı ve onu"
   - Cümle 11: «"Bu benim bilekliğim!" dedi arkadaşı ve onu hemen koluna taktı.»
   - Açıklama: Konuşan yalnız 'arkadaşı' diye geçiyor, kim olduğu belli değil.
6. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "suda parlayan şeyin ne olduğunu bulmuştu"
   - Cümle 12: «Örümcek Adam çok sevindi, çünkü suda parlayan şeyin ne olduğunu bulmuştu.»
   - Açıklama: Son cümle arkadaşın bilekliğine kavuşmasına değil merakın giderilmesine bağlanıyor, hedefle kapanış örtüşmüyor.
   - Açıklama: Kapanış arkadaşının bilekliğini kurtarma hedefine değil ışığın merakına bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0030` birebir aynı, `@degisim: soslu -> renkli` (tutuyorsan), ardından `@onarim: 7c6bff23932006d4b2156be01ac496c06c4b32e9`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0031
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: kaybolan eşya
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'köfte', fiil 'dolanmak', sıfat 'temkinli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: rüzgar esti ve balon ağaçların arasında kayboldu | balonu dalda buldu ve ipini ağla çekti
@tohum: orumcek_adam-0031
@degisim: temkinli -> dikkatli
Örümcek Adam ile Hulk parkta yürüyordu. Hulk bir eliyle köfte yiyor, öbür eliyle kırmızı balonunu tutuyordu. Birden güçlü bir rüzgar esti ve balonun ipi Hulk'ın elinden kaydı. Balon uçtu ve ağaçların arasında kayboldu. "Balonum nereye gitti?" diye sordu Hulk. Örümcek Adam ağaçlara doğru yürüdü ve yukarı dikkatli dikkatli baktı. Sonunda balonu yüksek bir dalda buldu. Balonun ipi dala dolanmıştı. Örümcek Adam bileğinden ağ attı ve ipi yakaladı. Sonra ipi yavaşça çekip daldan kurtardı. Balonu Hulk'a geri verdi. "Teşekkürler, Örümcek Adam!" dedi Hulk ve kocaman güldü. Örümcek Adam çok sevindi, çünkü arkadaşının balonunu bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir eliyle köfte yiyor"
   - Cümle 2: «Hulk bir eliyle köfte yiyor, öbür eliyle kırmızı balonunu tutuyordu.»
   - Açıklama: Köfte olaya hiçbir katkı yapmayan işlevsiz bir ayrıntı olarak kalıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hulk bir eliyle köfte yiyor"
   - Cümle 2: «Hulk bir eliyle köfte yiyor, öbür eliyle kırmızı balonunu tutuyordu.»
   - Açıklama: Köfte ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0031` birebir aynı, `@degisim: temkinli -> dikkatli` (tutuyorsan), ardından `@onarim: 23b974a0bd926414bbd0b07b249646c45ab745b2`, sonra gövde.
