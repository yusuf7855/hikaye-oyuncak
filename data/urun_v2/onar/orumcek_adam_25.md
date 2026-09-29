# Editör görevi (onarım): Örümcek Adam, onarım partisi 25

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar25.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar25.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0062 (deneme 5 -> 6)

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
@plan: çiçek bahçesinden bilinmeyen bir ses geldi | duvara tırmandı ve sallanan çömleği yere koydu
@tohum: orumcek_adam-0062
Örümcek Adam, Ghost-Spider ile parkta yüksek bir duvarın önünde oturuyordu. Birden duvarın arkasındaki çiçek bahçesinden "tak tak" diye bir ses geldi. "Bu ne sesi, bahçede bir şey mi kırılıyor?" diye sordu arkadaşı. Örümcek Adam hemen yerden kalktı ve bu sesi çok merak etti. Örümcek gibi duvara tırmandı ve bahçeye baktı. Bir ağacın dalında ipe asılı kıpkırmızı bir çömlek vardı. Rüzgar çömleği sallıyordu ve çömlek ağaca çarpıyordu. Örümcek Adam bahçeye indi ve çömleği daldan yavaşça aldı. Onu ağacın dibine koydu ve ses durdu. Örümcek Adam çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "diye bir ses geldi"
   - Cümle 2: «Birden duvarın arkasındaki çiçek bahçesinden "tak tak" diye bir ses geldi.»
   - Açıklama: Sorun yalnız merak edilen bir ses; çocuğun önemseyeceği bir derdi ya da kaybı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0062` birebir aynı, ardından `@onarim: 5cd45e47a1bea1552e30b1c373b45b6a7025a17e`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0064 (deneme 5 -> 6)

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
@plan: rüzgar arkadaşının şemsiyesini kırdı ve arkadaşı güneşte kaldı | kendi şemsiyesini arkadaşıyla paylaştı
@tohum: orumcek_adam-0064
Bir sabah Örümcek Adam kumsalda şemsiyesinin altında oturuyordu. Biraz uzakta Spin resim yapıyordu, ama rüzgar onun şemsiyesini kırdı. Şemsiye artık bozuktu ve Spin sıcak güneşte resim yapamıyordu. Birden Örümcek Adam'ın başı örümcek hissiyle titredi ve Spin'e baktı. Kendi şemsiyesini alıp Spin'in yanına götürdü. "Şemsiyemi seninle paylaşayım, Spin," dedi Örümcek Adam. Şemsiyeyi kuma sıkıca dikti. Şemsiyenin mavi kumaşı ikisini de güneşten korudu. Spin gölgeye geçti ve resmine devam etti. Denizi ve gemileri çok güzel çizdi. Sonra resmi Örümcek Adam'a gösterdi. "Teşekkürler, Örümcek Adam, bu resim senin!" dedi Spin.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "başı örümcek hissiyle titredi ve Spin'e baktı"
   - Cümle 4: «Birden Örümcek Adam'ın başı örümcek hissiyle titredi ve Spin'e baktı.»
   - Açıklama: İkinci yüklemin öznesi 'başı' kalıyor; baş bakmaz, özne uyumu bozuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "başı örümcek hissiyle titredi"
   - Cümle 4: «Birden Örümcek Adam'ın başı örümcek hissiyle titredi ve Spin'e baktı.»
   - Açıklama: 'Örümcek hissiyle başı titremek' mecazlı ve soyut bir anlatım, 3 yaşındaki çocuk için anlaşılır değil.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0064` birebir aynı, ardından `@onarim: a90efb18768048fe880908f6a30d3138e82a19f0`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0067 (deneme 5 -> 6)

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
Parkın oyun alanında Örümcek Adam balon oyununa başladı. Uzun ipi olan kırmızı balonu eliyle havaya itiyordu. Birden rüzgar esti ve balon bir gül çalısının içine uçtu. Balon dalların arasında hareketsiz kaldı. Dallarda küçük dikenler vardı. Örümcek Adam hemen balonu tutmak istedi. Ama birden örümcek hissiyle başı hafifçe titredi. Dikenler çok sivriydi ve balonu patlatabilirdi. Örümcek Adam balonun ipini tuttu ve yavaşça çekti. Balon kolayca çalıdan çıktı. Örümcek Adam ipi bileğine bağladı ve oyuna devam etti. Örümcek Adam çok sevindi, çünkü balonunu geri almıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle başı hafifçe titredi"
   - Cümle 7: «Ama birden örümcek hissiyle başı hafifçe titredi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuğa anlaşılır değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0067` birebir aynı, `@degisim: vanilya -> balon` (tutuyorsan), ardından `@onarim: 09ad3580856d318e6c901ee8fda492abaadfc958`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0071 (deneme 4 -> 5)

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
@plan: dalgalar kumdan kaleye yaklaşıyordu | kumu çuvalın içinde yukarı taşıdı ve kaleyi orada yaptı
@tohum: orumcek_adam-0071
@degisim: süzülmek -> taşımak
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin kumsalda kale yapıyordu, yanlarında bir çuval vardı. Ama dalgalar gittikçe kaleye yaklaşıyordu. Birden örümcek hissiyle Örümcek Adam'ın başı titredi. Örümcek Adam denize baktı ve bir dalganın geleceğini anladı. "Büyük bir dalga geliyor, kumu yukarı taşıyalım!" dedi Örümcek Adam. "Sen çok zekisin, Örümcek Adam," dedi Spin. Örümcek Adam ıslak kumu çuvalın içinde yukarıdaki kuru kuma taşıdı. İkisi yeni kaleyi orada birlikte yaptı. Az sonra dalga geldi ve eski yere çarptı. Yeni kale yukarıda sağlam duruyordu. "Teşekkürler, Spin, kalemiz artık güvende!" dedi Örümcek Adam.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle Örümcek Adam'ın başı titredi"
   - Cümle 4: «Birden örümcek hissiyle Örümcek Adam'ın başı titredi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle Örümcek"
   - Cümle 4: «Birden örümcek hissiyle Örümcek Adam'ın başı titredi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 'başı titredi' küçük çocuğa anlaşılmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0071` birebir aynı, `@degisim: süzülmek -> taşımak` (tutuyorsan), ardından `@onarim: 96313b8135a503a58ff1a32584854b0d1d4c7941`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0073 (deneme 2 -> 3)

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
@plan: top çok sert atıldı ve kayboldu | duvara tırmanıp yaprakların altında topu buldu
@tohum: orumcek_adam-0073
@degisim: bornoz -> top
Gizli evin önünde Örümcek Adam ile Hulk top oynuyordu. Topun üstüne komik bir yüz çizilmişti. Hulk topu çok sert attı ve top bir daha görünmedi. İkisi evin çevresine baktı ama topu bulamadı. "Top duvarın üstüne düşmüş olabilir," dedi Örümcek Adam. Örümcek Adam süper gücüyle evin yüksek duvarına tırmandı. Duvarın üstünde bir sürü yaprak birikmişti. Yaprakların arasından topun komik yüzü görünüyordu. Örümcek Adam yaprakları kaldırdı, topu aldı ve aşağı indi. Hulk topu görünce sevinçle zıpladı. "Teşekkürler, Örümcek Adam!" dedi Hulk. Örümcek Adam ile Hulk bundan sonra topu daha yavaş attı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hulk topu görünce sevinçle zıpladı"
   - Cümle 10: «Hulk topu görünce sevinçle zıpladı.»
   - Açıklama: Hulk topu zaten eline almışken ancak şimdi görüp seviniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0073` birebir aynı, `@degisim: bornoz -> top` (tutuyorsan), ardından `@onarim: a1231b30e03929e2c679959821954213548ceee4`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0080 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: kırmızı elma çok yüksek bir dalda duruyordu | elmaya ağ atıp yumuşak paspasın üstüne çekti
@tohum: orumcek_adam-0080
@degisim: sergilemek -> göstermek
Bir sabah Örümcek Adam ile Hulk gizli evin önünde oturuyordu. Örümcek Adam ağacın en yüksek dalında kırmızı bir elma gördü. Hulk elmayı çok istedi ama dal çok yüksekti. "Elmayı ağla çekeceğim, ama sert yere düşmesin," dedi Örümcek Adam. Hulk kapının önündeki paspası getirdi ve ağacın altına serdi. Örümcek Adam elmaya ağ attı ve yavaşça çekti. Elma daldan koptu ve yumuşak paspasın üstüne düştü. Yumuşak paspas elmayı çok iyi korudu. Örümcek Adam elmayı Hulk'a gösterdi ve ona verdi. "Teşekkürler, Örümcek Adam, elma çok güzel!" dedi Hulk. Örümcek Adam bundan sonra bir meyveyi çekmeden önce altına paspas serdi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra bir meyveyi çekmeden önce altına paspas serdi"
   - Cümle 11: «Örümcek Adam bundan sonra bir meyveyi çekmeden önce altına paspas serdi.»
   - Açıklama: Genel bir alışkanlık anlatıldığı için fiil 'sererdi' olmalı; 'bundan sonra ... serdi' uyumsuz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0080` birebir aynı, `@degisim: sergilemek -> göstermek` (tutuyorsan), ardından `@onarim: 2a258787b65f636cf904c1f6cf0ec027e1a1e97f`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0081 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar karton yıldızı uçurdu ve yıldız kayboldu | duvara tırmanıp sesi yapan yıldızı buldu
@tohum: orumcek_adam-0081
Limanın yanında rüzgar hızlı hızlı esiyordu. Örümcek Adam ile Ghost-Spider kumsalda parlak karton bir yıldızla oynuyordu. Birden rüzgar yıldızı uçurdu ve yıldız kayboldu. İkisi kumsala baktı ama yıldızı bulamadı. Sonra yüksek bir duvarın üstünden "hışır hışır" diye bir ses geldi. Örümcek Adam bu sesi çok merak etti. "Orada ne var acaba?" diye sordu Örümcek Adam. Süper gücüyle duvara tırmandı ve duvarın üstüne baktı. Karton yıldız orada rüzgarda sallanıyordu. Örümcek Adam yıldızı aldı ve aşağı indi. İkisi yıldızla yeniden oynadı ve gülüştü. Örümcek Adam çok sevindi, çünkü sesi yapan kayıp yıldızı bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yüksek bir duvarın üstünden"
   - Cümle 5: «Sonra yüksek bir duvarın üstünden "hışır hışır" diye bir ses geldi.»
   - Açıklama: Yıldızın yerini gösteren ses ve duvar sebepsizce beliriyor ve çözümü figürün aramasıyla değil tesadüfle getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0081` birebir aynı, ardından `@onarim: d16c7da2f8ec9590fd11ece39836e45182c354d6`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0082 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0082
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'krem', fiil 'soğumak', sıfat 'pürüzsüz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: attığı top resme çarptı ve resim dala uçtu | özür diledi ve ağ atıp resmi daldan aldı
@tohum: orumcek_adam-0082
@degisim: pürüzsüz -> beyaz
Bir sabah parkta hava biraz soğumuştu. Örümcek Adam ile Spin ısınmak için top oynuyordu. Spin'in pasta resmi bankta kuruyordu. Örümcek Adam'ın attığı top resme çarptı ve resim rüzgarla bir dala uçtu. Spin dala bakıp üzüldü. "Özür dilerim, Spin, hiç dikkat etmedim," dedi Örümcek Adam. Sonra bir ağ attı ve resmi daldan aldı. Resim sağlamdı, pastanın beyaz kremi de hiç bozulmamıştı. Örümcek Adam resmi Spin'e uzattı. Spin resmini sıkıca tuttu ve gülümsedi. "Teşekkürler, Örümcek Adam, resmim yine çok güzel!" dedi Spin.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Örümcek Adam'ın attığı top resme çarptı"
   - Cümle 4: «Örümcek Adam'ın attığı top resme çarptı ve resim rüzgarla bir dala uçtu.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede ortaya çıkıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Örümcek Adam'ın attığı top resme çarptı ve resim rüzgarla bir dala uçtu.»
   - Açıklama: Topun resme çarpıp resmi dala uçurması ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0082` birebir aynı, `@degisim: pürüzsüz -> beyaz` (tutuyorsan), ardından `@onarim: 7f65d099fd5416e52842df472d5e3353b1ae6508`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0084 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0084
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'halı', fiil 'üflemek', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: deniz suyu yavaş yavaş halıya yaklaşıyordu | garip sesi merak edip halıyı kuru kuma taşıdı
@tohum: orumcek_adam-0084
@degisim: cömert -> garip
Rüzgar serin serin esiyordu. Örümcek Adam kumsala halısını serdi ve üstündeki kumu üfledi. Ama deniz yavaş yavaş yükseliyordu ve su halıya yaklaşıyordu. Örümcek Adam bunu görmedi, çünkü halıya uzanmış gökyüzüne bakıyordu. Birden yakından şırıl şırıl garip bir ses geldi. Aynı anda örümcek hissiyle Örümcek Adam'ın başı hafifçe titredi. Örümcek Adam sesi merak etti ve kalkıp baktı. Ses, halının hemen yanına gelen deniz suyundan çıkıyordu. Örümcek Adam halısını hemen topladı ve kuru kuma taşıdı. Dalga geri çekildi ve halı hiç ıslanmadı. Örümcek Adam çok sevindi, çünkü halısı kupkuru kalmıştı.
```

**Hakem bulguları (3):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "halıya uzanmış gökyüzüne bakıyordu"
   - Cümle 4: «Örümcek Adam bunu görmedi, çünkü halıya uzanmış gökyüzüne bakıyordu.»
   - Açıklama: 'uzanmış' sonrası virgül eksik; 'uzanmış gökyüzü' diye yanlış okunabiliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle Örümcek Adam'ın"
   - Cümle 6: «Aynı anda örümcek hissiyle Örümcek Adam'ın başı hafifçe titredi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "örümcek hissiyle Örümcek Adam'ın başı hafifçe titredi"
   - Cümle 6: «Aynı anda örümcek hissiyle Örümcek Adam'ın başı hafifçe titredi.»
   - Açıklama: Örümcek hissi kuruluyor ama çözümde kullanılmıyor; Örümcek Adam yalnız sesi merak ederek harekete geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0084` birebir aynı, `@degisim: cömert -> garip` (tutuyorsan), ardından `@onarim: ee638d2a8bdf9bcd3566887c90fc74940d02808a`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0086 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0086
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gazete', fiil 'oynamak', sıfat 'çikolatalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: top gazeteye düştü ve sayfalar dağıldı | özür diledi ve bütün sayfaları topladı
@tohum: orumcek_adam-0086
Kuşlar ötüyordu ve Örümcek Adam parkta top oynuyordu. Hulk yakındaki bankta gazete okuyor ve çikolatalı kurabiye yiyordu. Örümcek Adam topu başının üstünden arkaya attı ve top gazeteye düştü. Gazetenin sayfaları çimenlere dağıldı. Örümcek Adam arkasını göremiyordu, ama örümcek hissiyle başı hafifçe titredi. Örümcek Adam hemen arkasına döndü. Yerdeki sayfaları gördü. "Özür dilerim, Hulk, bankın yanında oynamamalıydım," dedi Örümcek Adam. Sonra bütün sayfaları hızla toplayıp Hulk'a verdi. Hulk gülümsedi ve ona bir kurabiye uzattı. "Tamam, gel, birlikte yiyelim," dedi Hulk. Örümcek Adam çok sevindi, çünkü arkadaşı ona hiç kızmamıştı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Gazetenin sayfaları çimenlere dağıldı"
   - Cümle 4: «Gazetenin sayfaları çimenlere dağıldı.»
   - Açıklama: Sorun sayfaların dağılıp toplanmasından ibaret; örnekteki 'dağıttı, topladı, bitti' türünden önemsiz bir olay.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "örümcek hissiyle başı hafifçe titredi"
   - Cümle 5: «Örümcek Adam arkasını göremiyordu, ama örümcek hissiyle başı hafifçe titredi.»
   - Açıklama: 'Başı titredi' örümcek hissini anlatmak için yanlış ve anlaşılmaz bir kullanım.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama örümcek hissiyle başı hafifçe titredi"
   - Cümle 5: «Örümcek Adam arkasını göremiyordu, ama örümcek hissiyle başı hafifçe titredi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0086` birebir aynı, ardından `@onarim: f2c02e121444fdaf5153366e15641b5d8be6803e`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0087 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Ghost-Spider
@tohum: orumcek_adam-0087
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: sırayla oynamak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'krema', fiil 'çevirmek', sıfat 'ucuz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Ghost-Spider
@plan: bir dalga kumdan keke doğru geliyordu | dalganın geldiğini fark etti ve kekin önüne duvar yaptı
@tohum: orumcek_adam-0087
@degisim: ucuz -> ıslak
Rüzgar serin serin esiyordu. Örümcek Adam ile Ghost-Spider kumsalda bir kovayla sırayla kumdan kek yapıyordu. Birden Örümcek Adam'ın örümcek hissi titredi, bir dalga keke doğru geliyordu. "Hemen kekin önüne bir duvar yapalım!" dedi Örümcek Adam. İkisi hızla kumdan alçak bir duvar yaptı. Dalga duvara çarptı ve geri çekildi. Kek hiç bozulmadı. "Şimdi kremayı sen koy," dedi arkadaşı. Örümcek Adam ıslak kumu krema gibi kekin üstüne sürdü. Sonra arkadaşı kovayı kumla doldurdu ve ters çevirdi. Kekin üstünde küçük bir kat daha oldu. Örümcek Adam da arkadaşı da çok sevindi, çünkü kek dalgadan kurtulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi titredi"
   - Cümle 3: «Birden Örümcek Adam'ın örümcek hissi titredi, bir dalga keke doğru geliyordu.»
   - Açıklama: 'Örümcek hissinin titremesi' soyut ve mecazlı bir anlatımdır, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Örümcek hissinin titremesi' soyut ve mecazlı bir anlatım, küçük çocuk için anlaşılmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0087` birebir aynı, `@degisim: ucuz -> ıslak` (tutuyorsan), ardından `@onarim: 4b870b063e88b0ddee35a39129faade2129e4444`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0088 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0088
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'sucuk', fiil 'düzenlemek', sıfat 'esnek'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: rüzgar ekmek torbasını uçurdu ve torba kayboldu | sesin geldiği yere ağ atıp torbayı çekti
@tohum: orumcek_adam-0088
@degisim: esnek -> yumuşak
Örümcek Adam parkta bir bankta oturuyordu. Yanındaki kağıt torbada ekmek ve sucuk vardı. Birden rüzgar esti ve torbayı uzağa uçurdu. Örümcek Adam etrafa baktı ama torbayı göremedi. Az sonra çiçek bahçesinden garip bir ses geldi. Örümcek Adam bu sesi çok merak etti. Ses, büyük yaprakların altından geliyordu. Örümcek Adam çiçeklere basmak istemedi. Sesin geldiği yere bir ağ attı ve ağı yavaşça çekti. Yaprakların arasından kağıt torba çıktı. Sesi rüzgarda sallanan torba yapıyordu. İçindeki yumuşak ekmek de yerindeydi. Torba çıkarken birkaç çiçek yana eğilmişti. Örümcek Adam çiçekleri eliyle düzenledi. Örümcek Adam çok sevindi, çünkü torbasını ve ekmeğini bulmuştu.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ekmek ve sucuk vardı"
   - Cümle 2: «Yanındaki kağıt torbada ekmek ve sucuk vardı.»
   - Açıklama: Sucuk kuruluyor ama torba bulununca yalnız ekmekten söz ediliyor; işlevsiz ayrıntı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sesi rüzgarda sallanan torba yapıyordu"
   - Cümle 11: «Sesi rüzgarda sallanan torba yapıyordu.»
   - Açıklama: 'Ses yapmak' yanlış kelime seçimi; 'sesi torba çıkarıyordu' olmalı.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "birkaç çiçek yana eğilmişti"
   - Cümle 13: «Torba çıkarken birkaç çiçek yana eğilmişti.»
   - Açıklama: Torba bulunduktan sonra çiçeklerin eğilmesiyle ikinci bir küçük sorun açılıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çiçekleri eliyle düzenledi"
   - Cümle 14: «Örümcek Adam çiçekleri eliyle düzenledi.»
   - Açıklama: Eğilen çiçekler düzenlenmez, düzeltilir; fiil anlama uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0088` birebir aynı, `@degisim: esnek -> yumuşak` (tutuyorsan), ardından `@onarim: b4b39284d2a31a7f89d2305c49749d7c4d099662`, sonra gövde.
