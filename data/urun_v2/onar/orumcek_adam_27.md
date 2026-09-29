# Editör görevi (onarım): Örümcek Adam, onarım partisi 27

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar27.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar27.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0008 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0008
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'paket', fiil 'alışmak', sıfat 'dağınık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: rüzgar kurabiye paketini ince bir duvarın üstüne uçurdu | duvara tırmanıp paketi aldı ve arkadaşına verdi
@tohum: orumcek_adam-0008
@degisim: alışmak -> paylaşmak
Örümcek Adam parkta Hulk ile dağınık yaprakları topluyordu. Birden rüzgar esti ve Hulk'ın kurabiye paketini uçurdu. Paket ince ve yüksek bir duvarın üstüne düştü. Hulk çok ağırdı ve ince duvara tırmanamazdı. "Hulk, üzülme, ben alırım!" dedi Örümcek Adam. Hemen süper gücüyle duvara tırmandı ve paketi aldı. Sonra paketi elinde tutarak duvardan yavaşça indi. Paketi Hulk'a verdi. "Teşekkürler, Örümcek Adam!" dedi Hulk. Hulk paketi açtı ve kurabiyeleri Örümcek Adam ile paylaştı. İki arkadaş kurabiyelerini yiyip yaprakları toplamaya devam etti. Örümcek Adam çok sevindi, çünkü arkadaşının paketini geri getirmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hemen süper gücüyle duvara"
   - Cümle 6: «Hemen süper gücüyle duvara tırmandı ve paketi aldı.»
   - Açıklama: 'Süper güç' soyut bir kavram; 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0008` birebir aynı, `@degisim: alışmak -> paylaşmak` (tutuyorsan), ardından `@onarim: bbccd1f2c6057c5d398d0b47bb1ad8e0101bed03`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0071 (deneme 5 -> 6)

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
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin kumsalda kale yapıyordu, yanlarında bir çuval vardı. Ama dalgalar gittikçe kaleye yaklaşıyordu. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Örümcek Adam denize baktı ve bir dalganın geleceğini anladı. "Büyük bir dalga geliyor, kumu yukarı taşıyalım!" dedi Örümcek Adam. "Sen çok zekisin, Örümcek Adam," dedi Spin. Örümcek Adam ıslak kumu çuvalın içinde yukarıdaki kuru kuma taşıdı. İkisi yeni kaleyi orada birlikte yaptı. Az sonra dalga geldi ve eski yere çarptı. Yeni kale yukarıda sağlam duruyordu. "Teşekkürler, Spin, kalemiz artık güvende!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi mecazdır; 'örümcek hissi' ve 'sorun' 3 yaşındaki çocuk için soyuttur.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0071` birebir aynı, `@degisim: süzülmek -> taşımak` (tutuyorsan), ardından `@onarim: 6806ae211672057bd6769a91713def4761813e7b`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0073 (deneme 3 -> 4)

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
Gizli evin önünde Örümcek Adam ile Hulk top oynuyordu. Topun üstüne komik bir yüz çizilmişti. Hulk topu çok sert attı ve top bir daha görünmedi. İkisi evin çevresine baktı ama topu bulamadı. "Top duvarın üstüne düşmüş olabilir," dedi Örümcek Adam. Örümcek Adam süper gücüyle evin yüksek duvarına tırmandı. Duvarın üstünde bir sürü yaprak birikmişti. Yaprakların arasından topun komik yüzü görünüyordu. Örümcek Adam yaprakları kaldırdı, topu aldı ve aşağı indi. Topu Hulk'a verdi ve Hulk çok sevindi. "Teşekkürler, Örümcek Adam!" dedi Hulk. Örümcek Adam ile Hulk bundan sonra topu daha yavaş attı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "top bir daha görünmedi"
   - Cümle 3: «Hulk topu çok sert attı ve top bir daha görünmedi.»
   - Açıklama: 'Bir daha görünmedi' hiç bulunmadığını anlatır, oysa top sonra bulunuyor; ifade yanlış anlamda kullanılmış.
   - Açıklama: 'Bir daha görünmedi' hiç bulunmadı anlamı taşıyor ama top sonra bulunuyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "evin yüksek duvarına tırmandı"
   - Cümle 6: «Örümcek Adam süper gücüyle evin yüksek duvarına tırmandı.»
   - Açıklama: Kaybolan topu almak için evin yüksek duvarına tırmanmak, güvenli özellik kullanımı satırının kaçındığı çocukça taklit edilebilir ev tırmanmasına çok yakın.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0073` birebir aynı, `@degisim: bornoz -> top` (tutuyorsan), ardından `@onarim: 81f2913b0d3ab6439fe64cfe4776782a33e3e15a`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0080 (deneme 5 -> 6)

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
Bir sabah Örümcek Adam ile Hulk gizli evin önünde oturuyordu. Örümcek Adam ağacın en yüksek dalında kırmızı bir elma gördü. Hulk elmayı çok istedi ama dal çok yüksekti. "Elmayı ağla çekeceğim, ama sert yere düşmesin," dedi Örümcek Adam. Hulk kapının önündeki paspası getirdi ve ağacın altına serdi. Örümcek Adam elmaya ağ attı ve yavaşça çekti. Elma daldan koptu ve yumuşak paspasın üstüne düştü. Yumuşak paspas elmayı çok iyi korudu. Örümcek Adam elmayı Hulk'a gösterdi ve ona verdi. "Teşekkürler, Örümcek Adam, elma çok güzel!" dedi Hulk. Örümcek Adam, meyveyi çekmeden önce altına paspas sermeyi öğrendi.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "meyveyi çekmeden önce altına paspas sermeyi öğrendi"
   - Cümle 11: «Örümcek Adam, meyveyi çekmeden önce altına paspas sermeyi öğrendi.»
   - Açıklama: Örümcek Adam paspas fikrini baştan kendisi söylemişken sonunda bunu öğrenmiş gibi anlatılıyor.
   - Açıklama: Örümcek Adam paspas fikrini zaten baştan biliyordu, sonda bunu öğrendiği söyleniyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "meyveyi çekmeden önce altına paspas sermeyi öğrendi"
   - Cümle 11: «Örümcek Adam, meyveyi çekmeden önce altına paspas sermeyi öğrendi.»
   - Açıklama: Son ders yaşanan olaydan çıkmıyor, çünkü figür zaten bunu biliyordu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0080` birebir aynı, `@degisim: sergilemek -> göstermek` (tutuyorsan), ardından `@onarim: 000002e671d6757f621d152ca02bb1b7629b774f`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0081 (deneme 4 -> 5)

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
@plan: rüzgar karton yıldızı uçurdu ve yıldız kayboldu | rüzgarın gittiği duvara tırmanıp yıldızı buldu
@tohum: orumcek_adam-0081
Limanın yanında rüzgar hızlı hızlı esiyordu. Örümcek Adam ile Ghost-Spider kumsalda parlak karton bir yıldızla oynuyordu. Birden rüzgar yıldızı uçurdu ve yıldız kayboldu. İkisi kumsala baktı ama yıldızı bulamadı. Örümcek Adam rüzgarın gittiği yere baktı. Orada limanın yüksek bir duvarı vardı. Duvarın üstünden "hışır hışır" bir ses geliyordu. Örümcek Adam bu sesi çok merak etti. "Orada ne var acaba?" diye sordu Örümcek Adam. Süper gücüyle duvara tırmandı ve duvarın üstüne baktı. Karton yıldız orada rüzgarda sallanıyordu. Örümcek Adam yıldızı aldı ve aşağı indi. İkisi yıldızla yeniden oynadı ve gülüştü. Örümcek Adam çok sevindi, çünkü kayıp yıldızı bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "rüzgarın gittiği yere baktı"
   - Cümle 5: «Örümcek Adam rüzgarın gittiği yere baktı.»
   - Açıklama: Rüzgar bir yere gitmez; 'rüzgarın estiği yöne' olmalı.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Orada ne var acaba?"
   - Cümle 9: «"Orada ne var acaba?" diye sordu Örümcek Adam.»
   - Açıklama: Örümcek Adam kimseye yönelmeden 'acaba' ile kendi kendine soruyor gibi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0081` birebir aynı, ardından `@onarim: 4411b66f03ec814fc7929fea5236dacdf225c47e`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0084 (deneme 4 -> 5)

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
Rüzgar serin serin esiyordu. Örümcek Adam kumsala halısını serdi ve üstündeki kumu üfledi. Ama deniz yavaş yavaş yükseliyordu ve su halıya yaklaşıyordu. Örümcek Adam bunu görmedi, çünkü halıya uzanmış, gökyüzüne bakıyordu. Birden yakından şırıl şırıl garip bir ses geldi. Örümcek hissi de ona bir sorun olduğunu haber verdi. Örümcek Adam sesi merak etti ve hemen kalkıp baktı. Ses, halının hemen yanına gelen deniz suyundan çıkıyordu. Örümcek Adam halısını hemen topladı ve kuru kuma taşıdı. Dalga geri çekildi ve halı hiç ıslanmadı. Örümcek Adam çok sevindi, çünkü halısı kupkuru kalmıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissi de ona bir sorun olduğunu haber verdi"
   - Cümle 6: «Örümcek hissi de ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve bir hissin haber vermesi 3 yaşındaki çocuk için soyut ve mecazlı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Örümcek hissi de ona bir sorun olduğunu haber verdi"
   - Cümle 6: «Örümcek hissi de ona bir sorun olduğunu haber verdi.»
   - Açıklama: Tohumdaki örümcek hissi süs olarak ekleniyor; sorunu fark ettiren ve çözümü başlatan garip sestir, özellik işe yaramıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "halısını hemen topladı"
   - Cümle 9: «Örümcek Adam halısını hemen topladı ve kuru kuma taşıdı.»
   - Açıklama: 'Hemen' art arda üç cümlede gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0084` birebir aynı, `@degisim: cömert -> garip` (tutuyorsan), ardından `@onarim: 6cb94dabf1f10cd7497f1a019c1cd0fc7133a510`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0086 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: arkasına bakmadan attığı top bir keki bozdu | özür diledi ve sağlam keki arkadaşına verdi
@tohum: orumcek_adam-0086
Rüzgar hafif hafif esiyordu ve Örümcek Adam parkta top oynuyordu. Hulk çimene bir gazete sermiş, üstüne iki çikolatalı kek koymuştu. Örümcek Adam topu arkaya attı ve top bir keke düştü. Örümcek Adam bunu görmedi. Ama örümcek hissi ona bir sorun olduğunu haber verdi. Hemen arkasına döndü ve bozulmuş keki gördü. Hulk da keke üzgün üzgün bakıyordu. "Özür dilerim, Hulk, arkaya bakmadan attım," dedi Örümcek Adam. Sonra sağlam keki alıp Hulk'a uzattı. Hulk gülümsedi ve keki ikiye böldü. "Tamam, bunu birlikte yiyelim," dedi Hulk. İkisi gazetenin yanına oturdu ve keki yedi. Örümcek Adam çok sevindi, çünkü Hulk ona hiç kızmamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 5: «Ama örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber vermek' soyut ve mecazlı; küçük çocuk anlamaz.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sağlam keki alıp Hulk'a uzattı"
   - Cümle 9: «Sonra sağlam keki alıp Hulk'a uzattı.»
   - Açıklama: Kekler zaten Hulk'undu; ona kendi kekini vermek bozulan keki telafi eden bir çözüm değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0086` birebir aynı, ardından `@onarim: 7d48fcc66f7162b1edb804b7aeaadc3b888a02bb`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0087 (deneme 4 -> 5)

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
Rüzgar serin serin esiyordu. Örümcek Adam ile Ghost-Spider kumsalda bir kovayla sırayla kumdan kek yapıyordu. Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Bir dalga keke doğru geliyordu. "Hemen kekin önüne bir duvar yapalım!" dedi Örümcek Adam. İkisi hızla kumdan alçak bir duvar yaptı. Dalga duvara çarptı ve geri çekildi. Kek hiç bozulmadı. "Şimdi kremayı sen koy," dedi arkadaşı. Örümcek Adam ıslak kumu krema gibi kekin üstüne sürdü. Sonra arkadaşı kovayı kumla doldurdu ve ters çevirdi. Kekin üstünde küçük bir kat daha oldu. Örümcek Adam da arkadaşı da çok sevindi, çünkü kek dalgadan kurtulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: Bir hissin haber vermesi soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' ve 'haber verdi' soyut ve mecazlı; 3 yaşındaki çocuk anlamaz.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede yalnız bir sorun olduğu söyleniyor; dalganın keke gelmesi ancak dördüncü cümlede açıkça söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0087` birebir aynı, `@degisim: ucuz -> ıslak` (tutuyorsan), ardından `@onarim: 540fa44d62e05951af99c836fb76283630cddf54`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0088 (deneme 4 -> 5)

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
Örümcek Adam parkta bir bankta oturuyordu. Yanındaki kağıt torbada ekmek ve sucuk vardı. Birden rüzgar esti ve torbayı uzağa uçurdu. Örümcek Adam etrafa baktı ama torbayı göremedi. Az sonra çiçek bahçesinden garip bir ses geldi. Örümcek Adam bu sesi çok merak etti. Ses, büyük yaprakların altından geliyordu. Örümcek Adam çiçeklere basmak istemedi. Sesin geldiği yere bir ağ attı ve ağı yavaşça çekti. Yaprakların arasından kağıt torba çıktı. Torba rüzgarda sallanıyor ve ses çıkarıyordu. İçindeki yumuşak ekmek ve sucuk da yerindeydi. Örümcek Adam bankta küçük bir sofra düzenledi. Örümcek Adam çok sevindi, çünkü torbasını ve ekmeğini bulmuştu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Örümcek Adam çok sevindi"
   - Cümle 14: «Örümcek Adam çok sevindi, çünkü torbasını ve ekmeğini bulmuştu.»
   - Açıklama: Art arda iki cümlede özne olarak 'Örümcek Adam' adı gereksizce tekrarlanıyor.
   - Açıklama: 'Örümcek Adam' adı art arda cümlelerde gereksiz yere tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0088` birebir aynı, `@degisim: esnek -> yumuşak` (tutuyorsan), ardından `@onarim: 462472a187d43e57e24774d44e90b79ccca21af0`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0090 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Ghost-Spider
@tohum: orumcek_adam-0090
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Ghost-Spider
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'iz', fiil 'satmak', sıfat 'ahşap'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Ghost-Spider
@plan: yağmur geliyordu ve kurabiyeler bankın üstündeydi | tabağı hemen alıp büyük ağacın altına koştu
@tohum: orumcek_adam-0090
@degisim: iz -> yağmur
Parkta, büyük bir ağacın yanında ahşap bir bank vardı. Örümcek Adam ile Ghost-Spider bankta kurabiyelerle sırayla dükkan oyunu oynuyordu. Birden örümcek hissi, Örümcek Adam'a yağmurun geldiğini haber verdi. Kurabiyeler ıslanmasın diye Örümcek Adam tabağı hemen aldı. İkisi büyük ağacın altına koştu. Az sonra hafif bir yağmur başladı. Ama ağacın yaprakları çok sıktı ve tabağa hiç damla düşmedi. Oyun ağacın altında devam etti. Bu sefer Örümcek Adam arkadaşına bir kurabiye sattı. Arkadaşı da ona para yerine iki yaprak verdi. Örümcek Adam çok sevindi, çünkü kurabiyeler yağmurda hiç ıslanmadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi, Örümcek Adam'a yağmurun geldiğini haber verdi"
   - Cümle 3: «Birden örümcek hissi, Örümcek Adam'a yağmurun geldiğini haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Hissin haber vermesi mecazdır ve 'örümcek hissi' 3 yaşındaki çocuk için soyut bir kavramdır.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Örümcek Adam'a yağmurun geldiğini haber verdi"
   - Cümle 3: «Birden örümcek hissi, Örümcek Adam'a yağmurun geldiğini haber verdi.»
   - Açıklama: Kartın özelliklerinde örümcek hissi bir sorun olduğunu haber verir; burada hava tahmini gibi yağmuru önceden bildiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0090` birebir aynı, `@degisim: iz -> yağmur` (tutuyorsan), ardından `@onarim: fa2d730025bfc91ee69be6514d01111b09c51cc3`, sonra gövde.
