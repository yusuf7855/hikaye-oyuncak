# Editör görevi (onarım): Örümcek Adam, onarım partisi 20

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar20.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar20.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0062 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0062
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'çömlek', fiil 'kalkmak', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: arkadaşı yoktu ve bahçeden bir ses geldi | duvara tırmandı ve arkadaşını buldu
@tohum: orumcek_adam-0062
Örümcek Adam parkta Ghost-Spider ile buluşacaktı. Ama arkadaşını hiçbir yerde göremedi. Birden çiçek bahçesinden "tam tam" diye bir ses geldi. Bahçenin duvarı çok yüksekti. Örümcek Adam bu sesi çok merak etti. Süper gücüyle duvara tırmandı ve aşağı baktı. Arkadaşı çimlere oturmuş, kıpkırmızı bir çömleği davul gibi çalıyordu. "Ses senden geliyormuş!" dedi Örümcek Adam. Arkadaşı sevinçle yerden kalktı ve "Gel, birlikte çalalım!" dedi. Örümcek Adam duvardan indi ve onunla çömleği çaldı. Örümcek Adam çok sevindi, çünkü hem sesi hem de arkadaşını bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arkadaşı yoktu ve"
   - Cümle 0 (plan satırı): «arkadaşı yoktu ve bahçeden bir ses geldi | duvara tırmandı ve arkadaşını buldu»
   - Açıklama: 'Arkadaşı yoktu' hiç arkadaşı olmadığı anlamına geliyor; 'arkadaşı ortada yoktu' kastedilmiş.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "arkadaşı yoktu ve bahçeden"
   - Cümle 0 (plan satırı): «arkadaşı yoktu ve bahçeden bir ses geldi | duvara tırmandı ve arkadaşını buldu»
   - Açıklama: 'Arkadaşı yoktu' hiç arkadaşı olmadığı anlamına gelir; kastedilen 'arkadaşı ortada yoktu'.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "arkadaşı yoktu ve bahçeden bir ses geldi"
   - Cümle 0 (plan satırı): «arkadaşı yoktu ve bahçeden bir ses geldi | duvara tırmandı ve arkadaşını buldu»
   - Açıklama: Hikayede kayıp arkadaş ve merak edilen ses olmak üzere iki ayrı sorun var.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "arkadaşını hiçbir yerde göremedi"
   - Cümle 2: «Ama arkadaşını hiçbir yerde göremedi.»
   - Açıklama: Kayıp arkadaş ve gizemli ses olmak üzere iki ayrı sorun açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0062` birebir aynı, ardından `@onarim: a8294c2d71164aa8a787920934e1322045fa9fe3`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0064 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0064
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: paylaşmak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kumaş', fiil 'geçmek', sıfat 'bozuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: arkadaşının şemsiyesi bozuktu ve güneşte resim yapamadı | kendi şemsiyesini arkadaşıyla paylaştı
@tohum: orumcek_adam-0064
Bir sabah Örümcek Adam kumsalda şemsiyesinin altında oturuyordu. Birden örümcek hissiyle Spin'in üzgün olduğunu anladı. Spin'in şemsiyesi bozuktu ve Spin güneşte resim yapamıyordu. Örümcek Adam şemsiyesini alıp Spin'in yanına götürdü. "Şemsiyemi seninle paylaşayım, Spin," dedi Örümcek Adam. Şemsiyeyi kuma sıkıca dikti. Şemsiyenin mavi kumaşı ikisini de güneşten korudu. Spin gölgeye geçti ve resmine devam etti. Denizi ve gemileri çok güzel çizdi. Sonra resmi Örümcek Adam'a gösterdi. "Teşekkürler, Örümcek Adam, bu resim senin!" dedi Spin.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle Spin'in"
   - Cümle 2: «Birden örümcek hissiyle Spin'in üzgün olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "örümcek hissiyle Spin'in üzgün olduğunu anladı"
   - Cümle 2: «Birden örümcek hissiyle Spin'in üzgün olduğunu anladı.»
   - Açıklama: Karttaki özellik örümcek hissinin bir sorunu haber vermesidir; burada arkadaşın duygusunu okumak için kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0064` birebir aynı, ardından `@onarim: ab4c05aa343e25ae3e619c24583c5822bdc8e1e5`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0067 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0067
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'vanilya', fiil 'başlamak', sıfat 'hareketsiz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: rüzgar balonu dikenli bir çalıya uçurdu | balonu tutmadı ve ipinden yavaşça çekti
@tohum: orumcek_adam-0067
@degisim: vanilya -> balon
Parkın oyun alanında Örümcek Adam balon oyununa başladı. Kırmızı balonu eliyle havaya itiyor ve yere düşürmüyordu. Birden rüzgar esti ve balon bir gül çalısının içine uçtu. Balon dalların arasında hareketsiz kaldı. Dallarda küçük dikenler vardı. Örümcek Adam hemen onu tutmak istedi. Ama örümcek hissiyle bunun iyi olmadığını anladı. Sonra balonun ipini buldu ve yavaşça çekti. Balon kolayca çalıdan çıktı. Örümcek Adam ipi bileğine bağladı ve oyuna devam etti. Örümcek Adam çok sevindi, çünkü balonunu geri almıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle bunun iyi olmadığını"
   - Cümle 7: «Ama örümcek hissiyle bunun iyi olmadığını anladı.»
   - Açıklama: 'Örümcek hissi' ve 'iyi olmadığını anladı' 3 yaşındaki çocuk için soyut kalıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama örümcek hissiyle bunun iyi olmadığını anladı"
   - Cümle 7: «Ama örümcek hissiyle bunun iyi olmadığını anladı.»
   - Açıklama: 'Örümcek hissi' ve 'bunun iyi olmadığını anladı' soyut anlatım, 3 yaşındaki çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra balonun ipini buldu"
   - Cümle 8: «Sonra balonun ipini buldu ve yavaşça çekti.»
   - Açıklama: Elle havaya itilen balonun ipi önceden hiç kurulmuyor ve çözümü sebepsizce getiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "balonun ipini buldu"
   - Cümle 8: «Sonra balonun ipini buldu ve yavaşça çekti.»
   - Açıklama: Elle havaya itilen balonda ip önceden kurulmadan çözümü getirmek için sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0067` birebir aynı, `@degisim: vanilya -> balon` (tutuyorsan), ardından `@onarim: 151c2562925ce41d43611fedbe4b18646baf9982`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0069 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | -
@tohum: orumcek_adam-0069
- yer: ev (Takımın gizli evi.)
- tema: bir şey yapmak
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'turp', fiil 'tasarlamak', sıfat 'basit'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | -
@plan: kulenin alt katı dar olduğu için kule sallandı | üstteki küpleri indirdi ve alt katı geniş yaptı
@tohum: orumcek_adam-0069
@degisim: tasarlamak -> yapmak
Gizli evin dışında yağmur sessizce yağıyordu. Örümcek Adam küplerle basit bir kule yaptı ve tepesine bir turp koydu. Birden örümcek hissiyle kulenin sallandığını anladı, çünkü alt katı dardı. Örümcek Adam önce turpu ve üstteki küpleri tek tek indirdi. Sonra alt kata dört küp daha koydu. Küpleri yeniden üst üste dizdi. Turpu da en üste yerleştirdi. Bu kez kule hiç sallanmadı ve sağlam durdu. Örümcek Adam bundan sonra her kuleye geniş bir alt katla başladı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tepesine bir turp koydu"
   - Cümle 2: «Örümcek Adam küplerle basit bir kule yaptı ve tepesine bir turp koydu.»
   - Açıklama: Kulenin tepesindeki turp sebepsiz beliriyor ve olaya hiçbir katkı yapmıyor.
   - Açıklama: Kulenin tepesine sebepsizce turp konuyor ve olayda hiçbir işlevi yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle kulenin"
   - Cümle 3: «Birden örümcek hissiyle kulenin sallandığını anladı, çünkü alt katı dardı.»
   - Açıklama: 'Örümcek hissi' soyut ve çocuğun bilmediği bir kavram.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle kulenin sallandığını anladı"
   - Cümle 3: «Birden örümcek hissiyle kulenin sallandığını anladı, çünkü alt katı dardı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0069` birebir aynı, `@degisim: tasarlamak -> yapmak` (tutuyorsan), ardından `@onarim: 541d1217286dc04fa1e4e6e14d9393534a8ab733`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0071 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0071
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: bir şey yapmak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'çuval', fiil 'süzülmek', sıfat 'zeki'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: dalgalar kumdan kaleye yaklaşıyordu | çuvala kum doldurup kaleyi yukarıda yeniden yaptı
@tohum: orumcek_adam-0071
@degisim: süzülmek -> taşımak
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin kumsalda kumdan bir kale yapıyordu. Ama dalgalar gittikçe kaleye yaklaşıyordu. Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi. "Büyük bir dalga geliyor, kumu yukarı taşıyalım!" dedi Örümcek Adam. "Bu çok zeki bir fikir," dedi Spin. Örümcek Adam bir çuvalı ıslak kumla doldurdu. Çuvalı kuru kumun olduğu yere taşıdı. Spin de süslemek için küçük taşlar topladı. İkisi yeni kaleyi orada birlikte yaptı. Az sonra büyük dalga geldi ve eski yere çarptı. Yeni kale yukarıda sağlam duruyordu. "Teşekkürler, Spin, kalemiz artık güvende!" dedi Örümcek Adam.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden Örümcek Adam'ın örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'örümcek hissi' ve 'haber verdi' soyut ve mecazlı bir anlatım.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım; 3 yaşındaki çocuk anlamaz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu çok zeki bir fikir"
   - Cümle 6: «"Bu çok zeki bir fikir," dedi Spin.»
   - Açıklama: Fikir zeki olmaz; 'akıllıca bir fikir' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Örümcek Adam bir çuvalı ıslak kumla doldurdu"
   - Cümle 7: «Örümcek Adam bir çuvalı ıslak kumla doldurdu.»
   - Açıklama: Çuval hiç kurulmadan sebepsizce beliriyor ve çözümü getiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Spin de süslemek için küçük taşlar topladı"
   - Cümle 9: «Spin de süslemek için küçük taşlar topladı.»
   - Açıklama: Toplanan taşlar bir daha geçmiyor ve olayda kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0071` birebir aynı, `@degisim: süzülmek -> taşımak` (tutuyorsan), ardından `@onarim: aa1c97d665a43e247b4da622d9ecf3c4b26281d6`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0072 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0072
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: paylaşmak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'kapak', fiil 'kırpmak', sıfat 'renkli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: rüzgarda uçurtma yüksek bir duvara takıldı | duvara tırmanıp uçurtmayı aldı ve paylaştı
@tohum: orumcek_adam-0072
@degisim: kapak -> uçurtma
Örümcek Adam limanda renkli uçurtmasını uçuruyordu. Spin de yanındaydı ve uçurtmaya bakıyordu. Birden sert bir rüzgar esti ve uçurtma yüksek bir duvara takıldı. Örümcek Adam duvara hızlıca tırmandı. Uçurtmayı dikkatle çıkardı ve aşağı indi. Uçurtmanın hiçbir yeri bozulmamıştı. Spin'in hiç uçurtması yoktu ve ona uzun uzun baktı. Örümcek Adam ona göz kırptı ve ipi uzattı. "Bu uçurtma ikimizin olsun, Spin," dedi Örümcek Adam. Spin ipi aldı ve koşmaya başladı. Uçurtma yeniden gökyüzüne yükseldi. "Teşekkürler, Örümcek Adam, birlikte uçurmak çok güzel!" dedi Spin.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ona uzun uzun baktı"
   - Cümle 7: «Spin'in hiç uçurtması yoktu ve ona uzun uzun baktı.»
   - Açıklama: 'Ona' zamirinin uçurtmayı mı Örümcek Adam'ı mı gösterdiği belli değil.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Spin'in hiç uçurtması yoktu"
   - Cümle 7: «Spin'in hiç uçurtması yoktu ve ona uzun uzun baktı.»
   - Açıklama: Uçurtma kurtarıldıktan sonra Spin'in uçurtmasızlığı ikinci bir sorun olarak açılıyor.
   - Açıklama: Uçurtma sorunu çözüldükten sonra Spin'in uçurtmasızlığı ikinci bir sorun olarak açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0072` birebir aynı, `@degisim: kapak -> uçurtma` (tutuyorsan), ardından `@onarim: 85fdcff2d13b175988144ed6c3459e0ca7d3194c`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0073 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0073
- yer: ev (Takımın gizli evi.)
- tema: kaybolan eşya
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'bornoz', fiil 'birikmek', sıfat 'komik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: top çok güçlü atıldı ve kayboldu | duvara tırmanıp çatıdaki yaprakların altında topu buldu
@tohum: orumcek_adam-0073
@degisim: bornoz -> top
Gizli evin önünde Örümcek Adam ile Hulk top oynuyordu. Top yeşildi ve üstünde komik bir yüz vardı. Hulk topu çok güçlü attı ve top bir daha görünmedi. İkisi evin çevresine baktı ama topu bulamadı. "Top çatıya düşmüş olabilir," dedi Örümcek Adam. Örümcek Adam evin duvarına tırmandı ve çatıya çıktı. Çatının köşesinde bir sürü yaprak birikmişti. Örümcek Adam yaprakları kaldırdı ve topu buldu. Topu aldı ve aşağı indi. Hulk topu görünce sevinçle zıpladı. "Teşekkürler, Örümcek Adam!" dedi Hulk. Örümcek Adam ile Hulk bundan sonra topu daha yavaş attı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "top çok güçlü atıldı"
   - Cümle 0 (plan satırı): «top çok güçlü atıldı ve kayboldu | duvara tırmanıp çatıdaki yaprakların altında topu buldu»
   - Açıklama: Plan satırında da 'güçlü' fiili nitelemek için yanlış kullanılmış.
   - Açıklama: 'Güçlü' zarf olarak yanlış kullanılmış; 'sert atıldı' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Top yeşildi ve üstünde komik bir yüz vardı"
   - Cümle 2: «Top yeşildi ve üstünde komik bir yüz vardı.»
   - Açıklama: Topun rengi ve komik yüzü hiçbir işe yaramayan işlevsiz bir ayrıntı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hulk topu çok güçlü attı"
   - Cümle 3: «Hulk topu çok güçlü attı ve top bir daha görünmedi.»
   - Açıklama: 'Güçlü' sıfatı atma fiilini nitelemeye uygun değil; 'sert attı' olmalı.
   - Açıklama: 'Güçlü attı' yerine 'sert attı' olmalı.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "evin duvarına tırmandı ve çatıya çıktı"
   - Cümle 6: «Örümcek Adam evin duvarına tırmandı ve çatıya çıktı.»
   - Açıklama: Kaybolan topu almak için çatıya çıkmak çocuğun taklit edebileceği bir yükseğe tırmanma örneğidir ve güvenli özellik kullanımı satırıyla çelişir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0073` birebir aynı, `@degisim: bornoz -> top` (tutuyorsan), ardından `@onarim: 6d8ac09a1f5ee93c1177fd270c6a5e8cba0653ce`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0074 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0074
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'çalı', fiil 'uzaklaştırmak', sıfat 'meşgul'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: rüzgar atkıyı yüksek bir duvara uçurdu | duvara tırmanıp atkıyı aldı ve heykele bağladı
@tohum: orumcek_adam-0074
@degisim: meşgul -> beyaz
Örümcek Adam karlı bir günde parkta kardan bir heykel yapıyordu. Onun boynuna kırmızı bir atkı takmıştı. Ama sert bir rüzgar esti ve atkıyı heykelden uzaklaştırdı. Atkı havada uçtu ve oyun alanının yüksek duvarına takıldı. Örümcek Adam duvara hızlıca tırmandı ve atkıyı aldı. Sonra aşağı indi ve atkıyı heykele sıkıca bağladı. Onun daha kolları yoktu. Örümcek Adam çalının yanında iki kuru dal buldu. Dalları beyaz karın içine yavaşça yerleştirdi. Örümcek Adam kardan heykelini bitirdi ve mutlu mutlu güldü.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvara hızlıca tırmandı"
   - Cümle 5: «Örümcek Adam duvara hızlıca tırmandı ve atkıyı aldı.»
   - Açıklama: Oyun alanının yüksek duvarına tırmanma süper güç olarak çerçevelenmemiş ve çocuğun taklit edebileceği bir yerde geçiyor, 'guvenli_ozellik_kullanimi' satırına aykırı olabilir.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun daha kolları yoktu"
   - Cümle 7: «Onun daha kolları yoktu.»
   - Açıklama: 'Onun' zamirinin heykeli mi Örümcek Adam'ı mı gösterdiği belli değil.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Onun daha kolları yoktu"
   - Cümle 7: «Onun daha kolları yoktu.»
   - Açıklama: Atkı sorunu çözüldükten sonra heykelin kolları olmaması diye ikinci bir sorun açılıyor.
   - Açıklama: Atkı sorunu çözüldükten sonra heykelin kolları eksik diye ikinci bir sorun açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0074` birebir aynı, `@degisim: meşgul -> beyaz` (tutuyorsan), ardından `@onarim: 98490c0ac17c2c5ff78864d0d7ff9f59730b32f4`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0076 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0076
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'vagon', fiil 'bitmek', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: kurabiye dolu vagon trenden ayrılıp suya doğru kaydı | ağ atıp vagonu geri çekti
@tohum: orumcek_adam-0076
Örümcek Adam kumsalda oyuncak treniyle oynuyordu. Trenin son vagonu meyveli kurabiyelerle doluydu. Ama vagon trenden ayrıldı ve kumda suya doğru kaydı. Kurabiyeler neredeyse suya düşecekti. Örümcek Adam bileğinden hızlıca ağ attı. Ağ vagonu yakaladı ve vagon durdu. Örümcek Adam vagonu yavaşça geri çekti. Kurabiyelerin hiçbiri ıslanmadı. Vagonu trene yeniden taktı ve bu kez sıkıca bağladı. Sonra treni kumda uzun bir yolda gezdirdi ve trenin sesini yaptı. Oyun bitince Örümcek Adam kurabiyeleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "vagon trenden ayrıldı ve kumda suya doğru kaydı"
   - Cümle 3: «Ama vagon trenden ayrıldı ve kumda suya doğru kaydı.»
   - Açıklama: Vagonun trenden neden ayrıldığı söylenmiyor; sorunun sebebi eksik.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0076` birebir aynı, ardından `@onarim: 4e673987472ec5576d08a1408584353770e359f8`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0080 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | ev | Hulk
@tohum: orumcek_adam-0080
- yer: ev (Takımın gizli evi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'paspas', fiil 'sergilemek', sıfat 'iyi'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Hulk
@plan: rüzgar yaprağı yüksek bir dala uçurdu | ağ atıp yaprağı geri çekti
@tohum: orumcek_adam-0080
@degisim: sergilemek -> göstermek
Bir sabah Örümcek Adam gizli evin kapısını açtı. Paspasın üstünde kocaman, kırmızı bir yaprak duruyordu. Onu Hulk'a göstermek istedi ama rüzgar yaprağı yüksek bir dala uçurdu. Hulk da kapıya geldi ve dala baktı. "Bu dal çok yüksek," dedi Hulk üzülerek. Örümcek Adam bileğinden dala doğru ağ attı. Ağ yaprağa yapıştı ve Örümcek Adam yaprağı yavaşça çekti. Yaprak hiç bozulmamıştı. Örümcek Adam yaprağı Hulk'a verdi. Hulk yaprağı büyük eline aldı ve güldü. "Çok iyi yakaladın, Örümcek Adam!" dedi Hulk. Örümcek Adam bundan sonra güzel yaprakları hemen içeri getirdi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar yaprağı yüksek bir dala uçurdu"
   - Cümle 3: «Onu Hulk'a göstermek istedi ama rüzgar yaprağı yüksek bir dala uçurdu.»
   - Açıklama: Paspasta bulunan bir yaprağın rüzgarla uçması çocuk için önemsiz bir sorun.
   - Açıklama: Rüzgarın bir yaprağı uçurması önemsiz bir olay; çocuğun önemseyeceği bir sorun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yaprak hiç bozulmamıştı."
   - Cümle 8: «Yaprak hiç bozulmamıştı.»
   - Açıklama: Yaprak için 'bozulmak' uygun değil; 'yırtılmamıştı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0080` birebir aynı, `@degisim: sergilemek -> göstermek` (tutuyorsan), ardından `@onarim: d2e8f22534f3390e54121b9d7b5289f23d436e4b`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0081 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0081
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Ghost-Spider
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'karton', fiil 'gülüşmek', sıfat 'parlak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: yüksek bir duvarın üstünde parlak bir şey vardı | duvara tırmanıp kartondan bir taç buldu
@tohum: orumcek_adam-0081
Limanın yanında hava güneşliydi. Örümcek Adam ile Ghost-Spider kumsalda yürüyordu. Birden yüksek bir duvarın üstünde parlak bir şey gördüler. "Orada ne var acaba?" diye sordu arkadaşı. Örümcek Adam da merak etti. Duvara hızlıca tırmandı. Orada kartondan yapılmış bir taç vardı. Taç sarı, parlayan kağıtlarla kaplıydı. Örümcek Adam tacı aldı ve aşağı indi. Arkadaşı tacı başına taktı ve ikisi gülüştü. "Bu taç sana yakıştı," dedi Örümcek Adam. Örümcek Adam çok sevindi, çünkü duvardaki şeyin ne olduğunu bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yüksek bir duvarın üstünde parlak bir şey gördüler"
   - Cümle 3: «Birden yüksek bir duvarın üstünde parlak bir şey gördüler.»
   - Açıklama: Duvarda parlak bir şey görmek bir sorun değil, yalnız bir merak; kartondan tacın oraya neden konduğu da söylenmiyor.
   - Açıklama: Ortada gerçek bir sorun yok, yalnız merak var ve kumsaldaki duvarda karton tacın neden bulunduğu söylenmiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Duvara hızlıca tırmandı"
   - Cümle 6: «Duvara hızlıca tırmandı.»
   - Açıklama: Yüksek duvara merakla tırmanma süper güç olarak belirtilmiyor; güvenli özellik kullanımı satırına göre tırmanma yalnız süper güç olarak kullanılır ve çocuk bunu taklit edebilir.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Arkadaşı tacı başına taktı"
   - Cümle 10: «Arkadaşı tacı başına taktı ve ikisi gülüştü.»
   - Açıklama: Tacın kimin başına takıldığı belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0081` birebir aynı, ardından `@onarim: 931928bf2af48551207aa3b44353590e0267031a`, sonra gövde.
