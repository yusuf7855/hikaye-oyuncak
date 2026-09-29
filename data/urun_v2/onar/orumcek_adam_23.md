# Editör görevi (onarım): Örümcek Adam, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0052 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0052
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'kapı', fiil 'yerleştirmek', sıfat 'mutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: ikisi aynı anda kapıyı açmak isteyince duvardan kum döküldü | sırayla oynamayı önerdi ve duvarı ağla sardı
@tohum: orumcek_adam-0052
@degisim: yerleştirmek -> sarmak
Rüzgar kumsalda serin serin esiyordu. Örümcek Adam ile Hulk kumdan büyük bir kale kuruyordu. İkisi de kapıyı aynı anda açmak isteyince duvardan biraz kum döküldü. Hulk üzgün üzgün kuma baktı. "Hulk, sırayla oynayalım mı?" diye sordu Örümcek Adam. "Olur, ilk sıra senin," dedi Hulk. İlk sırada Örümcek Adam dökülen duvarı ağıyla sıkıca sardı. Şimdi sıra Hulk'taydı. Hulk kocaman parmağıyla duvarda yuvarlak bir kapı açtı. Bu kez ikisi sırayla çalıştı ve duvardan kum dökülmedi. Hulk kaleye baktı ve mutlu mutlu güldü. "Teşekkürler, Hulk, kalenin kapısı çok güzel oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dökülen duvarı ağıyla sıkıca sardı"
   - Cümle 7: «İlk sırada Örümcek Adam dökülen duvarı ağıyla sıkıca sardı.»
   - Açıklama: Duvar dökülmedi, duvardan kum döküldü; 'dökülen duvar' anlamca yanlış.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "dökülen duvarı ağıyla sıkıca sardı"
   - Cümle 7: «İlk sırada Örümcek Adam dökülen duvarı ağıyla sıkıca sardı.»
   - Açıklama: Sebep aynı anda çalışmak iken çözüm ayrıca ağla sarmayı ekliyor; çözüm iki ayrı yola dağılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0052` birebir aynı, `@degisim: yerleştirmek -> sarmak` (tutuyorsan), ardından `@onarim: d3d6722002354c047a8cebc157def3bd0db520e0`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0053 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0053
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'alet', fiil 'somurtmak', sıfat 'uyanık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: sert bir rüzgar geliyordu ve fidan çok inceydi | fidanı iple sağlam bir sopaya bağladı
@tohum: orumcek_adam-0053
@degisim: uyanık -> sağlam
Örümcek Adam parkta alet kutusuyla bahçe oyunu oynuyordu ve fidan dikti. Birden örümcek hissiyle sert bir rüzgarın geldiğini anladı. Fidan çok inceydi ve rüzgarda kırılabilirdi. Örümcek Adam fidana baktı ve somurttu. Sonra alet kutusundan bir ip ve sağlam bir sopa aldı. Sopayı fidanın yanında toprağa soktu. Fidanı iple sopaya yavaşça bağladı. Az sonra sert rüzgar esti ama fidan dik durdu. Örümcek Adam alet kutusunu kapattı ve küçük fidana gülümsedi. Örümcek Adam çok sevindi, çünkü fidanı rüzgardan korumuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bahçe oyunu oynuyordu ve fidan dikti"
   - Cümle 1: «Örümcek Adam parkta alet kutusuyla bahçe oyunu oynuyordu ve fidan dikti.»
   - Açıklama: Süreklilik bildiren 'oynuyordu' ile tamamlanmış 'dikti' aynı cümlede bağlanmış ve 'alet kutusuyla bahçe oyunu oynamak' anlamsız bir yapı.
   - Açıklama: Süren eylem ile bitmiş eylem 've' ile bağlanmış, cümle bozuk duruyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissiyle sert"
   - Cümle 2: «Birden örümcek hissiyle sert bir rüzgarın geldiğini anladı.»
   - Açıklama: 'Örümcek hissi' 3 yaşındaki çocuğun bilmediği soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0053` birebir aynı, `@degisim: uyanık -> sağlam` (tutuyorsan), ardından `@onarim: 185d25e21aedaea90d24839d91d584e78e808b59`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0054 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0054
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'lokma', fiil 'yollamak', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgarda kumdaki şemsiye sallanıp garip bir ses çıkarıyordu | şemsiyenin sapını tuttu ve kuma iyice bastırdı
@tohum: orumcek_adam-0054
@degisim: yollamak -> tutmak
Rüzgar sert sert esiyordu. Örümcek Adam kumsalda sulu bir şeftali yiyordu. Tam o sırada rüzgarla birlikte yakından garip bir "pat pat" sesi geldi. Örümcek Adam şeftaliyi bıraktı ve bu sesi çok merak etti. Örümcek hissiyle bir şeyin düşmek üzere olduğunu anladı. Örümcek Adam sese doğru koştu. Ses, kumdaki büyük bir şemsiyeden geliyordu. Rüzgar şemsiyeyi sağa sola sallıyordu. Örümcek Adam şemsiyenin sapını iki eliyle tuttu. Sonra sapı kuma iyice bastırdı. Şemsiye artık hiç sallanmadı ve ses durdu. Örümcek Adam şeftalisini aldı ve şemsiyenin altında son lokmayı yedi. Örümcek Adam çok sevindi, çünkü garip sesin ne olduğunu bulmuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissiyle bir şeyin düşmek üzere olduğunu anladı"
   - Cümle 5: «Örümcek hissiyle bir şeyin düşmek üzere olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve küçük çocuk için anlaşılır değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek hissiyle bir şeyin düşmek üzere"
   - Cümle 5: «Örümcek hissiyle bir şeyin düşmek üzere olduğunu anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, küçük çocuk için anlaşılır değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Rüzgar şemsiyeyi sağa sola sallıyordu"
   - Cümle 8: «Rüzgar şemsiyeyi sağa sola sallıyordu.»
   - Açıklama: Kimsenin olmayan bir şemsiyenin sallanıp ses çıkarması çocuğun önemseyeceği bir sorun değil, önemsiz bir olay.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "şemsiyenin sapını iki eliyle tuttu"
   - Cümle 9: «Örümcek Adam şemsiyenin sapını iki eliyle tuttu.»
   - Açıklama: Sert rüzgarda sallanan büyük şemsiyeyi elle tutmak çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0054` birebir aynı, `@degisim: yollamak -> tutmak` (tutuyorsan), ardından `@onarim: 0d9fa933f39e01b12f87db44de081702cb15b0d3`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0062 (deneme 4 -> 5)

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
Örümcek Adam, Ghost-Spider ile parkta çimlerde oturuyordu. Birden çiçek bahçesinden "tak tak" diye bir ses geldi. "Bu ne sesi, bahçede bir şey mi kırılıyor?" diye sordu arkadaşı. Örümcek Adam hemen yerden kalktı ve bu sesi çok merak etti. Örümcek gibi duvara tırmandı ve bahçeye baktı. Bir ağacın dalında ipe asılı kıpkırmızı bir çömlek vardı. Rüzgar çömleği sallıyordu ve çömlek ağaca çarpıyordu. Örümcek Adam bahçeye indi ve çömleği daldan yavaşça aldı. Onu ağacın dibine koydu ve ses durdu. Örümcek Adam çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Örümcek gibi duvara tırmandı"
   - Cümle 5: «Örümcek gibi duvara tırmandı ve bahçeye baktı.»
   - Açıklama: Parkta hiç kurulmamış bir duvar sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0062` birebir aynı, ardından `@onarim: cc44d19b68bb8a448664a7a2aa4696dd4bcbce3e`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0064 (deneme 4 -> 5)

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
Bir sabah Örümcek Adam kumsalda şemsiyesinin altında oturuyordu. Biraz uzakta Spin resim yapıyordu, ama rüzgar onun şemsiyesini kırdı. Şemsiye artık bozuktu ve Spin sıcak güneşte resim yapamıyordu. Örümcek Adam örümcek hissiyle bunu hemen fark etti. Kendi şemsiyesini alıp Spin'in yanına götürdü. "Şemsiyemi seninle paylaşayım, Spin," dedi Örümcek Adam. Şemsiyeyi kuma sıkıca dikti. Şemsiyenin mavi kumaşı ikisini de güneşten korudu. Spin gölgeye geçti ve resmine devam etti. Denizi ve gemileri çok güzel çizdi. Sonra resmi Örümcek Adam'a gösterdi. "Teşekkürler, Örümcek Adam, bu resim senin!" dedi Spin.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Adam örümcek hissiyle bunu"
   - Cümle 4: «Örümcek Adam örümcek hissiyle bunu hemen fark etti.»
   - Açıklama: 'Örümcek hissi' 3 yaşındaki çocuğun bilmediği soyut bir kavram.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam örümcek hissiyle bunu"
   - Cümle 4: «Örümcek Adam örümcek hissiyle bunu hemen fark etti.»
   - Açıklama: 'Örümcek hissi' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0064` birebir aynı, ardından `@onarim: 1f9a33c321620f41739257f1eedf1543ec16661b`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0067 (deneme 4 -> 5)

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
Parkın oyun alanında Örümcek Adam balon oyununa başladı. Uzun ipi olan kırmızı balonu eliyle havaya itiyordu. Birden rüzgar esti ve balon bir gül çalısının içine uçtu. Balon dalların arasında hareketsiz kaldı. Dallarda küçük dikenler vardı. Örümcek Adam hemen balonu tutmak istedi. Ama örümcek hissi sayesinde balonun patlayacağını anladı. Dikenler çok sivriydi. Örümcek Adam balonun ipini tuttu ve yavaşça çekti. Balon kolayca çalıdan çıktı. Örümcek Adam ipi bileğine bağladı ve oyuna devam etti. Örümcek Adam çok sevindi, çünkü balonunu geri almıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "balonun patlayacağını anladı"
   - Cümle 7: «Ama örümcek hissi sayesinde balonun patlayacağını anladı.»
   - Açıklama: Balon henüz patlamayacaktı; 'tutarsa patlayabileceğini' anlamı yerine yanlış kesinlik bildiren fiil kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0067` birebir aynı, `@degisim: vanilya -> balon` (tutuyorsan), ardından `@onarim: ded600b2dab9aedeaa2dc445e4102bd158258f3e`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0071 (deneme 3 -> 4)

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
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin kumsalda kale yapıyordu, yanlarında bir çuval vardı. Ama dalgalar gittikçe kaleye yaklaşıyordu. Birden Örümcek Adam'ın başı hafifçe titredi, bu onun örümcek hissiydi. Örümcek Adam denize baktı ve bir dalganın geleceğini anladı. "Büyük bir dalga geliyor, kumu yukarı taşıyalım!" dedi Örümcek Adam. "Sen çok zekisin, Örümcek Adam," dedi Spin. Örümcek Adam ıslak kumu çuvalın içinde yukarıdaki kuru kuma taşıdı. İkisi yeni kaleyi orada birlikte yaptı. Az sonra dalga geldi ve eski yere çarptı. Yeni kale yukarıda sağlam duruyordu. "Teşekkürler, Spin, kalemiz artık güvende!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu onun örümcek hissiydi"
   - Cümle 4: «Birden Örümcek Adam'ın başı hafifçe titredi, bu onun örümcek hissiydi.»
   - Açıklama: 'Örümcek hissi' 3 yaşındaki çocuğun bilmediği soyut bir kavram.
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0071` birebir aynı, `@degisim: süzülmek -> taşımak` (tutuyorsan), ardından `@onarim: e41fe02289ee75d62719becff4b33b0d085e655a`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0080 (deneme 3 -> 4)

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
Bir sabah Örümcek Adam ile Hulk gizli evin önünde oturuyordu. Örümcek Adam ağacın en yüksek dalında kırmızı bir elma gördü. Hulk elmayı çok istedi ama dal çok yüksekti. "Elmayı ağla çekeceğim, ama sert yere düşmesin," dedi Örümcek Adam. Hulk kapının önündeki paspası getirdi ve ağacın altına serdi. Örümcek Adam elmaya ağ attı ve yavaşça çekti. Elma daldan koptu ve yumuşak paspasın üstüne düştü. Yumuşak paspas elmayı çok iyi korudu. Örümcek Adam elmayı Hulk'a gösterdi ve ona verdi. "Teşekkürler, Örümcek Adam, elma çok güzel!" dedi Hulk. Örümcek Adam bundan sonra zor bir işte hep Hulk ile birlikte çalıştı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra zor bir işte hep Hulk ile birlikte çalıştı"
   - Cümle 11: «Örümcek Adam bundan sonra zor bir işte hep Hulk ile birlikte çalıştı.»
   - Açıklama: 'Hep' ile tekil 'zor bir işte' uyumsuz; 'zor işlerde' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "zor bir işte hep Hulk ile birlikte çalıştı"
   - Cümle 11: «Örümcek Adam bundan sonra zor bir işte hep Hulk ile birlikte çalıştı.»
   - Açıklama: 'Hep' tekil belirsiz 'zor bir işte' ile uyumsuz; 'her zor işte' ya da 'zor işlerde' olmalı.
3. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "bundan sonra zor bir işte hep Hulk ile birlikte çalıştı"
   - Cümle 11: «Örümcek Adam bundan sonra zor bir işte hep Hulk ile birlikte çalıştı.»
   - Açıklama: Kartın yanlar ilişki alanında Hulk takıma yalnız bazen yardım eden biri, hikaye onu her işte hep birlikte çalışan bir ortak yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0080` birebir aynı, `@degisim: sergilemek -> göstermek` (tutuyorsan), ardından `@onarim: 838a04eb37c0e31e5b0acacf74ae320cdd6d02cd`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0082 (deneme 2 -> 3)

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
@degisim: soğumak -> kurumak
Bir sabah Örümcek Adam parkta Spin ile top oynuyordu. Spin'in pasta resmi bankta kuruyordu, pastanın kremi pürüzsüz ve beyazdı. Örümcek Adam'ın attığı top resme çarptı ve resim rüzgarla bir dala uçtu. Spin dala bakıp üzüldü. "Özür dilerim, Spin, hiç dikkat etmedim," dedi Örümcek Adam. Sonra bir ağ attı ve resmi daldan aldı. Resim sağlamdı ve boyası da kurumuştu. Örümcek Adam resmi Spin'e uzattı. Spin resmini sıkıca tuttu ve gülümsedi. "Teşekkürler, Örümcek Adam, resmim yine çok güzel!" dedi Spin.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kremi pürüzsüz ve beyazdı"
   - Cümle 2: «Spin'in pasta resmi bankta kuruyordu, pastanın kremi pürüzsüz ve beyazdı.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "pastanın kremi pürüzsüz ve beyazdı"
   - Cümle 2: «Spin'in pasta resmi bankta kuruyordu, pastanın kremi pürüzsüz ve beyazdı.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki çocuğun bilmediği bir kelime.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "pastanın kremi pürüzsüz ve beyazdı"
   - Cümle 2: «Spin'in pasta resmi bankta kuruyordu, pastanın kremi pürüzsüz ve beyazdı.»
   - Açıklama: Resimdeki pastanın kreminin betimi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Pastanın kremi hikayede hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0082` birebir aynı, `@degisim: soğumak -> kurumak` (tutuyorsan), ardından `@onarim: 7a1dca2338b96004718c23dd12d49b4b0dc861fd`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0084 (deneme 2 -> 3)

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
Dalgalar hışır hışır kumsala vuruyordu. Örümcek Adam kumsala halısını serdi ve üstündeki kumu üfledi. Ama deniz yavaş yavaş yükseliyordu ve su halıya yaklaşıyordu. Örümcek Adam bunu görmedi, çünkü halıya uzanmış gökyüzüne bakıyordu. Birden yakından şırıl şırıl garip bir ses geldi. Aynı anda Örümcek Adam'ın başı hafifçe titredi. Bu onun örümcek hissiydi, bir sorun vardı. Örümcek Adam sesi merak etti ve kalkıp baktı. Ses, halının ucuna gelen deniz suyundan çıkıyordu. Örümcek Adam halısını hemen topladı ve kuru kuma taşıdı. Dalga geri çekildi ve halı hiç ıslanmadı. Örümcek Adam çok sevindi, çünkü halısı kupkuru kalmıştı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dalgalar hışır hışır kumsala"
   - Cümle 1: «Dalgalar hışır hışır kumsala vuruyordu.»
   - Açıklama: 'Hışır hışır' dalga sesi için uygun değil, yaprak sesi için kullanılır.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu onun örümcek hissiydi"
   - Cümle 7: «Bu onun örümcek hissiydi, bir sorun vardı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram, 3 yaşındaki çocuk anlamaz.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "halı hiç ıslanmadı"
   - Cümle 11: «Dalga geri çekildi ve halı hiç ıslanmadı.»
   - Açıklama: Deniz suyu halının ucuna geldiği söylendikten sonra halının hiç ıslanmadığı söyleniyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Dalga geri çekildi ve halı hiç ıslanmadı"
   - Cümle 11: «Dalga geri çekildi ve halı hiç ıslanmadı.»
   - Açıklama: Deniz suyu halının ucuna gelmişken halının hiç ıslanmadığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0084` birebir aynı, `@degisim: cömert -> garip` (tutuyorsan), ardından `@onarim: 2f5f6ff977de77421b84d6a7f8a28c5861cfad07`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0086 (deneme 2 -> 3)

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
@plan: top gazeteye düştü ve sayfalar dağıldı | özür diledi ve bütün sayfaları topladı
@tohum: orumcek_adam-0086
Kuşlar ötüyordu ve Örümcek Adam parkta top oynuyordu. Hulk yakındaki bankta gazete okuyor ve çikolatalı kurabiye yiyordu. Örümcek Adam topu başının üstünden arkaya attı ve top gazeteye düştü. Gazetenin sayfaları çimenlere dağıldı. Örümcek Adam arkasını göremiyordu, ama birden başı hafifçe titredi. Bu onun örümcek hissiydi, bu yüzden hemen arkasına döndü. Hulk'ın sayfalarını yerde gördü. "Özür dilerim, Hulk, bankın yanında oynamamalıydım," dedi Örümcek Adam. Sonra bütün sayfaları hızla toplayıp Hulk'a verdi. Hulk gülümsedi ve ona bir kurabiye uzattı. "Tamam, gel, birlikte yiyelim," dedi Hulk. Örümcek Adam çok sevindi, çünkü arkadaşı ona hiç kızmamıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu onun örümcek hissiydi"
   - Cümle 6: «Bu onun örümcek hissiydi, bu yüzden hemen arkasına döndü.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' soyut bir kavram, küçük çocuk için anlaşılmaz.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hulk'ın sayfalarını yerde"
   - Cümle 7: «Hulk'ın sayfalarını yerde gördü.»
   - Açıklama: Ünlü uyumuna göre ek 'Hulk'un' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0086` birebir aynı, ardından `@onarim: 0412c84e6850285b5345ae4953777b9b132fa40a`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0087 (deneme 2 -> 3)

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
@plan: bir dalga kumdan keke doğru geliyordu | dalgayı önceden anladı ve kekin önüne duvar yaptı
@tohum: orumcek_adam-0087
@degisim: ucuz -> ıslak
Rüzgar serin serin esiyordu. Örümcek Adam ile Ghost-Spider kumsalda bir kovayla sırayla kumdan kek yapıyordu. Birden Örümcek Adam'ın örümcek hissi, bir dalganın keke doğru geldiğini haber verdi. "Hemen kekin önüne bir duvar yapalım!" dedi Örümcek Adam. İkisi hızla kumdan alçak bir duvar yaptı. Dalga duvara çarptı ve geri çekildi. Kek hiç bozulmadı. "Şimdi kremayı sen koy," dedi arkadaşı. Örümcek Adam ıslak kumu krema gibi kekin üstüne sürdü. Sonra arkadaşı kovayı kumla doldurdu ve ters çevirdi. Kekin üstünde küçük bir kat daha oldu. Örümcek Adam da arkadaşı da çok sevindi, çünkü kum kekleri dalgadan kurtulmuştu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dalgayı önceden anladı"
   - Cümle 0 (plan satırı): «bir dalga kumdan keke doğru geliyordu | dalgayı önceden anladı ve kekin önüne duvar yaptı»
   - Açıklama: 'Dalgayı anlamak' yanlış anlamda; dalganın geldiğini fark etti denmeli.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Örümcek Adam'ın örümcek hissi, bir dalganın"
   - Cümle 3: «Birden Örümcek Adam'ın örümcek hissi, bir dalganın keke doğru geldiğini haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı, 3 yaşındaki çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Adam'ın örümcek hissi, bir dalganın keke doğru geldiğini haber verdi"
   - Cümle 3: «Birden Örümcek Adam'ın örümcek hissi, bir dalganın keke doğru geldiğini haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım; 3 yaşındaki çocuk anlamaz.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çünkü kum kekleri dalgadan kurtulmuştu"
   - Cümle 12: «Örümcek Adam da arkadaşı da çok sevindi, çünkü kum kekleri dalgadan kurtulmuştu.»
   - Açıklama: Tek kek var ama 'kum kekleri' çoğul kullanılmış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kum kekleri dalgadan kurtulmuştu"
   - Cümle 12: «Örümcek Adam da arkadaşı da çok sevindi, çünkü kum kekleri dalgadan kurtulmuştu.»
   - Açıklama: Hikayede tek bir kek var; çoğul 'kum kekleri' yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0087` birebir aynı, `@degisim: ucuz -> ıslak` (tutuyorsan), ardından `@onarim: 43f233ee745835d3ed449655f664ce11e924e2ab`, sonra gövde.
