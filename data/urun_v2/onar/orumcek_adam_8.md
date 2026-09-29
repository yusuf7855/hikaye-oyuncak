# Editör görevi (onarım): Örümcek Adam, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0002 (deneme 4 -> 5)

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
Örümcek Adam parkta Ghost-Spider için sürpriz bir piknik hazırlıyordu. Ağacın altına büyük bir örtü serdi ve peynirli sandviçleri dizdi. Elinde kırmızı bir balon vardı. Ama birden rüzgar esti ve balon elinden kaçtı. Balon uçtu ve ağacın yüksek bir dalına takıldı. Örümcek Adam dala doğru bir ağ attı. Ağ balonun ipine yapıştı. Örümcek Adam ipi yavaşça çekti ve balon aşağı indi. Sonra ipi örtünün köşesine sıkıca bağladı. İki bardağa da soğuk süt döktü. Az sonra arkadaşı havada süzülerek geldi. Örtüyü ve sandviçleri görünce çok şaşırdı. Sevinçle Örümcek Adam'a sarıldı. İki arkadaş kırmızı balonun yanında oturdu ve mutlu mutlu piknik yaptı.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Elinde kırmızı bir balon vardı.»
   - Açıklama: Balonun kaçması ancak 4. cümlede geliyor; ilk üç cümle yalnız piknik hazırlığını anlatıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "birden rüzgar esti ve balon elinden kaçtı"
   - Cümle 4: «Ama birden rüzgar esti ve balon elinden kaçtı.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede söyleniyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Örümcek Adam ipi yavaşça çekti"
   - Cümle 8: «Örümcek Adam ipi yavaşça çekti ve balon aşağı indi.»
   - Açıklama: 'İpi' sözcüğünün ağın ipini mi balonun ipini mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0002` birebir aynı, `@degisim: mercan -> balon` (tutuyorsan), ardından `@onarim: 3a72db5124c6a504d6aa90bfb49648d0f9685bc4`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0003 (deneme 4 -> 5)

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
Parkta rüzgar sert esiyordu. Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti. Rüzgar büyük bir dalı kırmış ve dal piknik masasının üstüne düşmüştü. Örümcek Adam, Hulk ile orada piknik yapacaktı ve çok heyecanlıydı. Elindeki fiyonklu kek kutusunu çimenlere bıraktı ve dalı itti. Ama dal çok ağırdı ve hiç kıpırdamadı. Biraz sonra Hulk da masaya geldi. "Hulk, bu dalı kaldırabilir misin?" diye sordu Örümcek Adam. Hulk dalı kolayca kaldırdı ve ağaçların yanına taşıdı. Örümcek Adam kutuyu masaya koydu ve açtı. İki arkadaş keki birlikte yedi. Örümcek Adam çok sevindi, çünkü Hulk'tan yardım istemiş ve keki masada yemişti.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 2: «Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: Sıfat cümleciği yanlış yere bağlanmış; süper güç Örümcek Adam'ın, cümle bozuk kuruluyor.
   - Açıklama: Sıfat öbeği yanlış bağlanmış; cümle dilbilgisel olarak bozuk ve karışık.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "olan örümcek hissiyle bir sorun"
   - Cümle 2: «Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun fark etti"
   - Cümle 2: «Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' ve 'süper güç' soyut kavramlar, 3 yaşındaki çocuğa uygun değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "örümcek hissiyle bir sorun fark etti"
   - Cümle 2: «Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: Masadaki dal gözle görülür bir durum; örümcek hissi işlevsiz biçimde özellikten eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0003` birebir aynı, ardından `@onarim: 3dde1c6ed5bc61a05879867994d8270ff752c461`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0012 (deneme 3 -> 4)

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
Örümcek Adam gizli evde yemek yapma oyunu oynuyordu. Oyuncak tencereye bezelye taneleri koyuyordu ve masanın bir ayağı yamuktu. Birden süper gücü olan örümcek hissiyle bir sorun fark etti. Masa sallanıyordu ve tencere kenara doğru kayıyordu. Tencere neredeyse masadan düşecekti. Örümcek Adam tencereyi hemen iki eliyle tuttu. Sonra bir kağıdı katladı ve yamuk ayağın altına koydu. Masa artık hiç sallanmıyordu. Örümcek Adam tencereyi ortaya koydu ve kalan taneleri tek tek ekledi. Sonra yemeği oyuncak kaşıkla güzelce karıştırdı. Örümcek Adam oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: Sıfat-fiil yapısı bozuk; süper güç örümcek hissine bağlanmış gibi duruyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: Süper güç Örümcek Adam'ın özelliğidir, hissin değil; tamlama anlamca yanlış kuruluyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun fark etti"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' ve 'sorun fark etmek' soyut kavramlar, küçük çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: Üçüncü cümle yalnız 'bir sorun' diyor; tencerenin kayması ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0012` birebir aynı, `@degisim: tekrarlamak -> karıştırmak` (tutuyorsan), ardından `@onarim: ff43f1983a88685bbf1bef869e1745be1c54ce8a`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0013 (deneme 3 -> 4)

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
Örümcek Adam yağmurlu bir sabah kumsala geldi. Islak kumdan ilk kez büyük bir gemi yapmayı denedi. Birden süper gücü olan örümcek hissiyle bir sorun fark etti. Küçük bir dalga gemiye doğru geliyordu. Örümcek Adam hemen geminin önüne uzun bir kum duvarı yaptı. Az sonra dalga kumsala geldi. Su duvara çarptı ve iki yana aktı. Gemi hiç bozulmadı. Örümcek Adam gemiye baktı ve sevinçle ellerini çırptı. Örümcek Adam çok sevindi, çünkü ilk kumdan gemisini dalgadan korumuştu.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: Sıfat öbeği yanlış kurulmuş; süper güç 'örümcek hissi'ne bağlanıyor ve tamlama bozuk.
   - Açıklama: Tamlama bozuk; süper gücü olan his değil Örümcek Adam'dır.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun fark etti"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir ifade.
   - Açıklama: 'Örümcek hissi' ile sorun fark etmek soyut bir kavramdır.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'Süper güç' ve 'örümcek hissi' soyut kavramlar, 3 yaşındaki çocuk bilmez.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Küçük bir dalga gemiye doğru geliyordu"
   - Cümle 4: «Küçük bir dalga gemiye doğru geliyordu.»
   - Açıklama: Dalga sorunu ilk 3 cümlede değil 4. cümlede açıkça söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede açıkça söyleniyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ilk kumdan gemisini dalgadan korumuştu"
   - Cümle 10: «Örümcek Adam çok sevindi, çünkü ilk kumdan gemisini dalgadan korumuştu.»
   - Açıklama: Sözcük sırası bozuk; 'kumdan ilk gemisini' olmalı.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ilk kumdan gemisini dalgadan"
   - Cümle 10: «Örümcek Adam çok sevindi, çünkü ilk kumdan gemisini dalgadan korumuştu.»
   - Açıklama: Sözcük sırası bozuk; 'kumdan ilk gemisini' olmalı.
7. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Örümcek Adam çok sevindi"
   - Cümle 10: «Örümcek Adam çok sevindi, çünkü ilk kumdan gemisini dalgadan korumuştu.»
   - Açıklama: Önceki cümledeki sevinç ve ad gereksiz yere tekrarlanıyor.
   - Açıklama: Bir önceki cümlede sevinçle el çırptığı söylenmişken sevinç yeniden tekrarlanıyor.
   - Açıklama: Bir önceki cümlede sevinç anlatıldıktan hemen sonra aynı ad ve sevinç tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0013` birebir aynı, `@degisim: tanışmak -> denemek` (tutuyorsan), ardından `@onarim: 78bbd8637c0ce9e999543f53787346aa81aac79f`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0015 (deneme 3 -> 4)

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
Kumsalda Spin'in karnı yüksek sesle guruldadı. Spin sandviç çantasını suya yakın bıraktı ve Örümcek Adam ile çeşmeye yürüdü. Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti. Büyük bir dalga çantaya doğru geliyordu. Çantada Spin'in yaptığı özel sandviçler vardı. Örümcek Adam çantayı hemen kuru kuma taşıdı. Az sonra dalga geldi ve çantanın durduğu yeri ıslattı. Ama sandviçler kuru kaldı. Örümcek Adam çantayı Spin'e verdi. İki arkadaş ellerini çeşmede yıkadı ve kuma oturdu. Spin sandviçlerden birini Örümcek Adam'a uzattı. "Teşekkürler, Örümcek Adam, sandviçler ıslanmadı!" dedi Spin.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: Sıfat yan cümlesi yanlış bağlanmış; 'süper gücü olan' örümceği niteliyor gibi okunuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "süper gücü olan örümcek hissiyle bir sorun fark etti"
   - Cümle 3: «Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' ve 'sorun fark etmek' 3 yaşındaki çocuk için soyut ve anlaşılmaz.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun fark etti"
   - Cümle 3: «Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' ve 'sorun fark etmek' 3 yaşındaki çocuk için soyut.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden Örümcek Adam süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: İlk üç cümlede yalnız belirsiz bir sorun fark ediliyor; dalganın çantaya geldiği ancak 4. cümlede söyleniyor.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Büyük bir dalga çantaya doğru geliyordu"
   - Cümle 4: «Büyük bir dalga çantaya doğru geliyordu.»
   - Açıklama: Sorun ancak 4. cümlede açıkça söyleniyor; 3. cümlede yalnız belirsiz bir sorun fark ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0015` birebir aynı, ardından `@onarim: 6ef14c030be0d8d144759399294a62cfbca43b21`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0020 (deneme 2 -> 3)

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
@plan: rüzgar arkadaşının kartını uçurdu ve kart kayboldu | duvara tırmanıp kartı buldu ve tozunu sildi
@tohum: orumcek_adam-0020
@degisim: oynak -> renkli
Örümcek Adam ile Hulk parkta renkli kartlarla oynuyordu. Birden rüzgar esti ve Hulk'ın en sevdiği kart uçtu. "Kartım kayboldu, hiçbir yerde göremiyorum!" dedi Hulk. Örümcek Adam çimenlere ve çiçeklere baktı ama kartı bulamadı. Sonra çiçek bahçesinin duvarına baktı. Duvarın tepesinde bir kart gördü. Örümcek Adam süper gücüyle duvara tırmandı ve kartı aldı. Kartın üstünde biraz toz vardı. Örümcek Adam aşağı indi ve tozu eliyle sildi. "İşte kartın, Hulk," dedi Örümcek Adam. Hulk kartı kocaman elleriyle tuttu ve sevinçle güldü. "Teşekkürler, sen harika bir arkadaşsın!" dedi Hulk. Örümcek Adam çok mutlu oldu, çünkü Hulk'ın kartını bulmuştu.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "çimenlere ve çiçeklere baktı ama kartı bulamadı"
   - Cümle 4: «Örümcek Adam çimenlere ve çiçeklere baktı ama kartı bulamadı.»
   - Açıklama: Çözüm başarısız aramayla, duvara bakmayla, tırmanmayla ve toz silmeyle iki adımı aşıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kartın üstünde biraz toz vardı"
   - Cümle 8: «Kartın üstünde biraz toz vardı.»
   - Açıklama: Toz ayrıntısı soruna ya da çözüme hiçbir katkı yapmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0020` birebir aynı, `@degisim: oynak -> renkli` (tutuyorsan), ardından `@onarim: 242b3ee5c35419a788f09a4dc500187fa43b1443`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0021 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0021
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'dolap', fiil 'sarılmak', sıfat 'yeterli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: koşup arkadaşının salıncak sırasını aldı | özür diledi ve salıncağı arkadaşına verdi
@tohum: orumcek_adam-0021
@degisim: dolap -> salıncak
Bir sabah Örümcek Adam parkta salıncağa doğru koştu. Ghost-Spider salıncağın yanında sırasını bekliyordu ama Örümcek Adam onu görmedi. Hemen salıncağa oturdu ve sallanmaya başladı. Birden süper gücü olan örümcek hissi sayesinde bir sorun fark etti. Örümcek Adam arkasına baktı ve üzgün arkadaşını gördü. Salıncağı yavaşça durdurdu ve indi. "Özür dilerim, seni görmedim," dedi Örümcek Adam. "Önemli değil, özür dilemen yeterli," dedi arkadaşı. İki arkadaş birbirine sıkıca sarıldı. Sonra arkadaşı salıncağa bindi ve sevinçle güldü. Örümcek Adam bundan sonra salıncak için sırasını bekledi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "süper gücü olan örümcek hissi"
   - Cümle 4: «Birden süper gücü olan örümcek hissi sayesinde bir sorun fark etti.»
   - Açıklama: Süper gücü olan şey his değil Örümcek Adam'dır; anlam yanlış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi sayesinde bir sorun fark etti"
   - Cümle 4: «Birden süper gücü olan örümcek hissi sayesinde bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' ve 'sayesinde' soyut ve 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi sayesinde bir sorun"
   - Cümle 4: «Birden süper gücü olan örümcek hissi sayesinde bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0021` birebir aynı, `@degisim: dolap -> salıncak` (tutuyorsan), ardından `@onarim: 1f39aeab06b4676b62ae6e14ed174aa5b14fc975`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0022 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0022
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'perde', fiil 'şaşırtmak', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar şemsiyeyi yüksek bir duvarın üstüne uçurdu | duvara tırmanıp şemsiyeyi geri aldı
@tohum: orumcek_adam-0022
@degisim: perde -> şemsiye
Bir sabah hava bulutluydu ve Örümcek Adam limanda yürüyordu. Birden başlayan yağmur Örümcek Adam'ı şaşırttı. Şemsiyesini açtı ama rüzgar onu yüksek bir duvarın üstüne uçurdu. Şemsiye duvarın tepesinde takılı kaldı. Örümcek Adam hiç beklemeden duvara tırmandı. Şemsiyeyi aldı ve yavaşça aşağı indi. Bu kez şemsiyeyi rüzgara karşı sıkı tuttu. Yağmur damlaları şemsiyenin üstünde tıp tıp ses yaptı. Örümcek Adam kuru kaldı ve gülümsedi. Sonra şemsiyesinin altında limanda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "hiç beklemeden duvara tırmandı"
   - Cümle 5: «Örümcek Adam hiç beklemeden duvara tırmandı.»
   - Açıklama: Rüzgarın uçurduğu şemsiyeyi almak için yüksek bir duvara tırmanmak çocuğun taklit edebileceği yükseğe tırmanma davranışıdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0022` birebir aynı, `@degisim: perde -> şemsiye` (tutuyorsan), ardından `@onarim: 8d50a62cbade20c23768e942b3ee2dedfb7b4a77`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0024 (deneme 2 -> 3)

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
Örümcek Adam parkta Hulk için resimlerle dolu bir klasör hazırlıyordu. Klasörü güzelleştirmek için içine kokulu çiçek yaprakları koyuyordu. Birden süper gücü olan örümcek hissiyle bir sorun fark etti. Hulk erkenden geliyordu ve sürpriz daha bitmemişti. Örümcek Adam klasörü hemen sırtının arkasına sakladı. "Merhaba, Örümcek Adam, ne yapıyorsun?" diye sordu Hulk. "Gözlerini kapat ve ona kadar say, lütfen," dedi Örümcek Adam. Hulk gözlerini kapattı ve saymaya başladı. Örümcek Adam son yaprakları klasöre hızla koydu. "Şimdi açabilirsin!" dedi Örümcek Adam. Hulk klasörü açtı ve resimleri gördü. "Ne kadar güzel kokuyor, çok teşekkürler!" dedi Hulk. Örümcek Adam bundan sonra sürprizlerini daha erken hazırladı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "süper gücü olan örümcek hissiyle"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: Sıfat öbeği yanlış kurulmuş; süper güç 'örümcek hissi'ne bağlanıyor ve tamlama bozuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun fark etti"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir ifade.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "süper gücü olan örümcek hissiyle bir sorun fark etti"
   - Cümle 3: «Birden süper gücü olan örümcek hissiyle bir sorun fark etti.»
   - Açıklama: 'örümcek hissi' ve 'bir sorun fark etti' soyut, 3 yaşındaki çocuğa uygun değil.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Hulk erkenden geliyordu ve sürpriz daha bitmemişti.»
   - Açıklama: Sorunun ne olduğu ancak 4. cümlede söyleniyor; 3. cümle yalnız 'bir sorun fark etti' diyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hulk klasörü açtı ve resimleri gördü"
   - Cümle 11: «Hulk klasörü açtı ve resimleri gördü.»
   - Açıklama: Klasör Hulk'a hiç verilmeden Hulk onu açıyor; olay öncekinden çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0024` birebir aynı, ardından `@onarim: 3f780286957cbe274d4ebfbb1dcd7a82d16b3e3b`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0025 (deneme 2 -> 3)

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
Bir sabah Örümcek Adam gizli evde arkadaşı için bir sürpriz hazırlıyordu. Tavana parlak sarı kağıttan bir yıldız asmak istiyordu. Ama tavan çok yüksekti ve yıldızı oraya asmak zordu. Örümcek Adam yıldızı bir eline aldı. Sonra süper gücüyle bir örümcek gibi duvara tırmandı. Yıldızı ipinden tavana astı ve yavaşça aşağı indi. Az sonra kapı açıldı ve arkadaşı Ghost-Spider içeri girdi. Kapıdan gelen ışık yıldıza vurdu ve yıldız ışıldadı. "Bu yıldız benim için mi?" diye sordu arkadaşı. "Evet, senin için bir sürpriz!" dedi Örümcek Adam. Arkadaşı sevinçle güldü ve havada süzüldü. Sonra iki arkadaş yıldızın altında mutlu mutlu dans etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bir örümcek gibi duvara tırmandı"
   - Cümle 5: «Sonra süper gücüyle bir örümcek gibi duvara tırmandı.»
   - Açıklama: Güvenli kullanım satırı ev içi taklit edilebilir tırmanmayı yasaklıyor; ev içinde tavana ulaşmak için duvara tırmanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0025` birebir aynı, `@degisim: karnabahar -> yıldız` (tutuyorsan), ardından `@onarim: 9624208cecf9d30cb53113db6c0287b8de89bd78`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0026 (deneme 2 -> 3)

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
Parkta geniş çimenlerin üstünde hafif bir rüzgar esiyordu. Örümcek Adam ile Spin komik yüzlü bir uçurtma uçuruyordu. Birden rüzgar döndü ve uçurtma büyük bir ağaca doğru indi. Örümcek Adam o an Spin'e bakıyordu ve uçurtmayı görmedi. Ama örümcek hissiyle bir sorun olduğunu anladı. Örümcek Adam hemen döndü, ipi sıkıca tuttu ve ağaçtan uzağa koştu. Uçurtma dallara değmeden yeniden yükseldi. Gökyüzünde uçurtmanın yüzü sallandı ve iki arkadaş kahkahalarla güldü. Sonra çimenlerde koşarak oyuna devam ettiler. Örümcek Adam bundan sonra uçurtmayı ağaçlardan uzakta uçurdu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun"
   - Cümle 5: «Ama örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun olduğunu anladı"
   - Cümle 5: «Ama örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk anlamaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0026` birebir aynı, `@degisim: hazırlıklı -> komik` (tutuyorsan), ardından `@onarim: 837b5ffd6078fcee7ec0ec8b19abd193d27ec350`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0028 (deneme 2 -> 3)

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
Örümcek Adam ile Hulk parkta top oynuyordu. Güneş sıcacıktı ve bankta soğuk bir şişe limonata duruyordu. Hulk topa çok güçlü vurdu ve top şişeye doğru uçtu. O an Örümcek Adam örümcek hissiyle bir sorun olduğunu anladı. Örümcek Adam hızla zıpladı ve topu havada tuttu. Şişe yerinde kaldı ve limonata dökülmedi. "Eyvah, top benden hızlı kaçtı!" dedi Hulk ve kahkahalarla güldü. "Hadi biraz dinlenelim, çok susadım," dedi Örümcek Adam. İkisi banka oturdu ve limonatayı paylaştı. Sonra Örümcek Adam ile Hulk oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bir sorun olduğunu anladı"
   - Cümle 4: «O an Örümcek Adam örümcek hissiyle bir sorun olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Örümcek hissi' ve 'bir sorun olduğunu anladı' soyut ve 3 yaşındaki çocuğa uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "top benden hızlı kaçtı"
   - Cümle 7: «"Eyvah, top benden hızlı kaçtı!" dedi Hulk ve kahkahalarla güldü.»
   - Açıklama: Top kaçmaz ve topa Hulk vurduğu için 'benden hızlı kaçtı' anlamca uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0028` birebir aynı, `@degisim: limon -> limonata` (tutuyorsan), ardından `@onarim: 38dd5c3ee52bda5239d58780309f46e0bd21cb97`, sonra gövde.
