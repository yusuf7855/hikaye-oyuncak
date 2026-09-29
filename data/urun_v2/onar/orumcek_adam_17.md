# Editör görevi (onarım): Örümcek Adam, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar17.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0052 (deneme 2 -> 3)

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
@plan: ikisi aynı anda kapıyı açmak isteyince duvar yıkıldı | sırayla oynamayı önerdi ve duvarı ağla sardı
@tohum: orumcek_adam-0052
Rüzgar kumsalda serin serin esiyordu. Örümcek Adam ile Hulk kumdan büyük bir kale kuruyordu. İkisi de kapıyı aynı anda açmak isteyince kalenin duvarı yıkıldı. Hulk üzgün üzgün kuma baktı. "Hulk, sırayla oynayalım mı?" diye sordu Örümcek Adam. "Olur, ilk sıra senin," dedi Hulk. Örümcek Adam kumu toplayıp duvarı yeniden yaptı. Sonra duvarı ağıyla sıkıca sardı. Şimdi sıra Hulk'taydı. Hulk kocaman parmağıyla duvarda yuvarlak bir kapı açtı. İki deniz kabuğunu da kapının yanlarına yerleştirdi. Hulk kaleye baktı ve mutlu mutlu güldü. "Teşekkürler, Hulk, kalenin kapısı çok güzel oldu!" dedi Örümcek Adam.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra duvarı ağıyla sıkıca sardı"
   - Cümle 8: «Sonra duvarı ağıyla sıkıca sardı.»
   - Açıklama: Çözüm sırayı önermek, duvarı yeniden yapmak ve ağla sarmak olarak ikiden fazla adım sürüyor.
   - Açıklama: Duvar aynı anda kapı açmaya çalışıldığı için yıkıldı; ağla sarmak bu sebebe yönelmiyor ve çözüm öneri, yeniden yapma ve sarma diye 2 adımı aşıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İki deniz kabuğunu da kapının"
   - Cümle 11: «İki deniz kabuğunu da kapının yanlarına yerleştirdi.»
   - Açıklama: Deniz kabukları sebepsiz beliriyor ve olayda işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0052` birebir aynı, ardından `@onarim: 622401932d4411ad619e1a69f5940d798f32f2bc`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0053 (deneme 2 -> 3)

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
@plan: rüzgar yüzünden küçük fidan yere eğildi | fidanı iple sağlam bir sopaya bağladı
@tohum: orumcek_adam-0053
@degisim: uyanık -> sağlam
Örümcek Adam parkta bahçe oyunu oynuyordu ve ufak bir fidan dikti. Birden örümcek hissi ona fidanda bir sorun olduğunu haber verdi. Rüzgar sert esti ve ince fidan yere doğru eğildi. Örümcek Adam hemen fidanın yanına koştu ve somurttu. Sonra bahçe aletleri arasında bir ip ile sağlam bir sopa buldu. Sopayı fidanın yanında toprağa soktu. Fidanı iple sopaya yavaşça bağladı. Rüzgar yine esti ama fidan bu kez hiç eğilmedi. Örümcek Adam aletlerini topladı ve küçük fidana gülümsedi. Örümcek Adam çok sevindi, çünkü fidanı rüzgardan korumuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona fidanda bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona fidanda bir sorun olduğunu haber verdi.»
   - Açıklama: Haber veren 'örümcek hissi' ve 'sorun' soyut ve mecazlı, 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona fidanda bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona fidanda bir sorun olduğunu haber verdi.»
   - Açıklama: His haber vermez; kişileştirme ve soyut 'sorun' kavramı küçük çocuğa uygun değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "fidanın yanına koştu ve somurttu"
   - Cümle 4: «Örümcek Adam hemen fidanın yanına koştu ve somurttu.»
   - Açıklama: Yardıma koşarken 'somurttu' bağlama uymuyor ve küçük çocuğun bilmeyeceği bir kelime.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bahçe aletleri arasında bir ip ile sağlam bir sopa buldu"
   - Cümle 5: «Sonra bahçe aletleri arasında bir ip ile sağlam bir sopa buldu.»
   - Açıklama: Bahçe aletleri, ip ve sopa önceden kurulmadan tam gerektiği anda sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0053` birebir aynı, `@degisim: uyanık -> sağlam` (tutuyorsan), ardından `@onarim: 2487302d3831bb4adf24a37146b79568b024a949`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0054 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Rüzgar sert sert esiyordu. Örümcek Adam kumsalda sulu bir şeftali yiyordu. Birden arkasından garip bir "pat pat" sesi duyuldu. Örümcek Adam şeftaliyi bıraktı ve bu sesi çok merak etti. O sırada örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam sese doğru koştu. Ses, kumdaki büyük bir şemsiyeden geliyordu. Rüzgar şemsiyeyi sallıyordu ve şemsiye kumdan çıkmak üzereydi. Örümcek Adam şemsiyenin sapını iki eliyle tuttu. Sonra sapı kuma iyice bastırdı. Şemsiye artık hiç sallanmadı ve ses durdu. Örümcek Adam şeftalisini aldı ve şemsiyenin altında son lokmayı yedi. Örümcek Adam çok sevindi, çünkü garip sesin ne olduğunu bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "O sırada örümcek hissi ona"
   - Cümle 5: «O sırada örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'haber verdi' soyut, mecazlı bir anlatım; küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 5: «O sırada örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: His haber vermez; soyut ve mecazlı anlatım 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0054` birebir aynı, `@degisim: yollamak -> tutmak` (tutuyorsan), ardından `@onarim: 98cc429936a89562666cc63905904f84eddfa9ca`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0056 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0056
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: sırayla oynamak
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'yastık', fiil 'silkmek', sıfat 'elmalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: yastık parktaki duvarın tepesinde kaldı | duvara tırmanıp yastığı aldı ve tozunu silkti
@tohum: orumcek_adam-0056
@degisim: elmalı -> yumuşak
Örümcek Adam ile Spin parkta yastık oyunu oynuyordu. Sırayla küçük, yumuşak bir yastığı birbirine atıyorlardı. Ama Spin yastığı çok yükseğe attı ve yastık duvarın tepesinde kaldı. "Eyvah, yastığımız yukarıda!" dedi Spin. "Hemen alırım, Spin," dedi Örümcek Adam. Örümcek Adam duvara hızla tırmandı ve yastığı aldı. Sonra tozlu yastığı iki kez silkti. Aşağı indi ve yastığı Spin'e verdi. "Şimdi sıra sende, Örümcek Adam," dedi Spin gülerek. Oyun yine sırayla devam etti. Örümcek Adam ile Spin bundan sonra yastığı hep yavaşça attı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam duvara hızla tırmandı"
   - Cümle 6: «Örümcek Adam duvara hızla tırmandı ve yastığı aldı.»
   - Açıklama: Yastığı almak için duvara tırmanma süper güç olarak çerçevelenmeden anlatılıyor ve çocuk bunu taklit edebilir; bu, güvenli özellik kullanımı satırına aykırıdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0056` birebir aynı, `@degisim: elmalı -> yumuşak` (tutuyorsan), ardından `@onarim: d2d9e8ce730bf7cc54026fd0bddd5e02b60b56d0`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0058 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0058
- yer: ev (Takımın gizli evi.)
- tema: sırayla oynamak
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'dalga', fiil 'sıkışmak', sıfat 'değişik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: davul çubuğu kaydı ve kanepenin altına sıkıştı | ağ atıp çubuğu dışarı çekti
@tohum: orumcek_adam-0058
Dışarıda soğuk bir rüzgar esiyordu. Örümcek Adam gizli evde arkadaşı Ghost-Spider ile sırayla davul çalıyordu. Ama arkadaşı hızlı çalınca çubuk kaydı ve kanepenin altına sıkıştı. Kanepenin altı çok dardı ve eller oraya girmiyordu. Örümcek Adam ince bir ağ attı. Ağ çubuğa yapıştı ve çubuk dışarı çıktı. "Sıra daha sende," dedi Örümcek Adam ve çubuğu arkadaşına verdi. Arkadaşı davulu yavaşça çaldı. Davuldan dalga sesine benzeyen değişik bir ses çıktı. Sonra çubuğu gülerek Örümcek Adam'a uzattı. "Sırayla oynamak çok eğlenceli!" dedi Örümcek Adam.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sıra daha sende"
   - Cümle 7: «"Sıra daha sende," dedi Örümcek Adam ve çubuğu arkadaşına verdi.»
   - Açıklama: 'Daha' burada yanlış anlamda kullanılmış; 'Sıra hâlâ sende' ya da 'Sıra sende' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: ""Sıra daha sende," dedi"
   - Cümle 7: «"Sıra daha sende," dedi Örümcek Adam ve çubuğu arkadaşına verdi.»
   - Açıklama: 'Daha' burada 'hâlâ' anlamında yanlış ve anlaşılmaz kullanılmış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Davuldan dalga sesine benzeyen değişik bir ses çıktı"
   - Cümle 9: «Davuldan dalga sesine benzeyen değişik bir ses çıktı.»
   - Açıklama: Dalga sesine benzeyen değişik ses sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Değişik ses ayrıntısı kurulup hiçbir işe yaramıyor.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra çubuğu gülerek Örümcek Adam'a uzattı"
   - Cümle 10: «Sonra çubuğu gülerek Örümcek Adam'a uzattı.»
   - Açıklama: Önceki cümlenin öznesi ses olduğundan çubuğu kimin uzattığı belirsiz.
   - Açıklama: Özne söylenmemiş; önceki cümlenin öznesi ses olduğundan kimin uzattığı belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0058` birebir aynı, ardından `@onarim: 7febe436e972a43717cb1a835b78374f263725d5`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0060 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0060
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'papatya', fiil 'şişirmek', sıfat 'çabuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: rüzgar balonu uçurdu ve ipi papatyalara dolandı | duvara tırmandı ve ipi dikkatle çözdü
@tohum: orumcek_adam-0060
Bir sabah Örümcek Adam limanda kırmızı bir balon şişirdi. Birden rüzgar esti ve balonu elinden aldı. Balon çabuk yükseldi ve yüksek bir duvarın tepesine takıldı. Balonun ipi, tepedeki papatyalara dolanmıştı. Örümcek Adam duvarın dibine koştu ve yukarı baktı. Sonra hemen duvara tırmandı. İpi papatyaların arasından dikkatle çözdü. Sonra balonu sıkıca tuttu ve yavaşça aşağı indi. Bu kez ipi bileğine bağladı. Kırmızı balon başının üstünde sallandı. Örümcek Adam çok sevindi, çünkü balonunu geri almıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çabuk yükseldi ve yüksek"
   - Cümle 3: «Balon çabuk yükseldi ve yüksek bir duvarın tepesine takıldı.»
   - Açıklama: Aynı cümlede 'yükseldi' ve 'yüksek' gereksiz tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0060` birebir aynı, ardından `@onarim: 356028380da85d30092b78e03e7ff9dc46e310f7`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0061 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0061
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: paylaşmak
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'tebeşir', fiil 'gezinmek', sıfat 'plastik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: arkadaşının tebeşiri eline çok küçük geldi | tebeşirlerini paylaştı ve ağla kalın bir tebeşir yaptı
@tohum: orumcek_adam-0061
Limanın taş yolunda Örümcek Adam tebeşirle resim yapıyordu. Hulk da yanında üzgün üzgün geziniyordu. Tebeşiri kocaman eline çok küçük geldiği için resim yapamıyordu. Örümcek Adam plastik kutusundan dört tebeşir çıkardı. Onları yan yana koydu ve ağıyla sıkıca sardı. Böylece tutması kolay, kalın bir tebeşir oldu. "Al, Hulk, bu tebeşir artık senin," dedi Örümcek Adam. Hulk yeni tebeşiri rahatça tuttu. Sonra yere büyük yeşil bir ağaç çizdi. Örümcek Adam da ağacın yanına kırmızı bir güneş ekledi. "Teşekkürler, Örümcek Adam, bu tebeşir çok güzel!" dedi Hulk.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Tebeşiri kocaman eline çok küçük geldiği için"
   - Cümle 3: «Tebeşiri kocaman eline çok küçük geldiği için resim yapamıyordu.»
   - Açıklama: Yan cümlenin öznesi ek uyumsuz; 'Tebeşir kocaman eline küçük geldiği için' ya da 'Tebeşirinin' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0061` birebir aynı, ardından `@onarim: d372927869e7fab97a007aafa28a6f8f544b5401`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0062 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: yüksek duvarın arkasından garip bir ses geldi | duvara tırmanıp sesi yapan çömleği buldu
@tohum: orumcek_adam-0062
Örümcek Adam parkta çiçek bahçesinin yanından yürüyordu. Birden yüksek duvarın arkasından garip bir ses geldi. Bu sesi çok merak etti. Ama duvarın arkası hiç görünmüyordu. Örümcek Adam süper gücüyle duvara hızla tırmandı ve aşağı baktı. Çimlerin üstünde kıpkırmızı, boş bir çiçek çömleği duruyordu. Ghost-Spider yere oturmuş, çömleği davul gibi çalıyordu. "Ses buradan geliyormuş!" dedi Örümcek Adam. Arkadaşı yerden kalktı ve güldü. "Gel, birlikte çalalım," dedi arkadaşı. Örümcek Adam duvardan indi ve onun yanına oturdu. Örümcek Adam çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yüksek duvarın arkasından garip bir ses geldi"
   - Cümle 2: «Birden yüksek duvarın arkasından garip bir ses geldi.»
   - Açıklama: Garip bir ses gerçek bir sorun değil, önemsiz bir merak olayı.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Arkadaşı yerden kalktı ve güldü"
   - Cümle 9: «Arkadaşı yerden kalktı ve güldü.»
   - Açıklama: Ghost-Spider yerden kalkıyor ama Örümcek Adam hemen ardından onun yanına oturuyor, konumlar çelişiyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Örümcek Adam duvardan indi ve onun yanına oturdu"
   - Cümle 11: «Örümcek Adam duvardan indi ve onun yanına oturdu.»
   - Açıklama: Arkadaşı yerden kalkmışken Örümcek Adam onun yanına oturuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0062` birebir aynı, ardından `@onarim: 2a213e24a31efa768951f869a339803104735521`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0063 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0063
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: sırayla oynamak
- yan: Hulk
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'fincan', fiil 'getirmek', sıfat 'kırmızı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: arkadaşı topu çok hızlı attı ve top denize uçtu | ağ atıp topu havada yakaladı
@tohum: orumcek_adam-0063
Bir sabah Örümcek Adam ile Hulk kumsalda oyun oynuyordu. Sırayla küçük bir topu kırmızı bir fincana atıyorlardı. Hulk topu çok hızlı attı ve top denize doğru uçtu. Örümcek Adam hemen ağını attı. Ağ topu havada yakaladı. Topu geri çekti ve Hulk'a getirdi. "Bu kez biraz yavaş dene," dedi Örümcek Adam. Hulk topu bu kez yavaşça attı. Top bir kez zıpladı ve tam fincanın içine düştü. Hulk sevinçle ellerini çırptı. "Aferin, Hulk, şimdi sıra bende!" dedi Örümcek Adam.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Topu geri çekti ve Hulk'a getirdi."
   - Cümle 6: «Topu geri çekti ve Hulk'a getirdi.»
   - Açıklama: Önceki cümlenin öznesi 'Ağ' olduğu için topu kimin çekip getirdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0063` birebir aynı, ardından `@onarim: 44cfd5d2728a2d141d91545e7bb5b97b278eed15`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0064 (deneme 1 -> 2)

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
Bir sabah Örümcek Adam kumsalda şemsiyesinin altında oturuyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Spin'in şemsiyesi bozuktu ve Spin güneşte resim yapamıyordu. Örümcek Adam şemsiyesini alıp Spin'in yanına götürdü. "Şemsiyemi seninle paylaşayım, Spin," dedi Örümcek Adam. Şemsiyeyi kuma sıkıca dikti. Şemsiyenin mavi kumaşı ikisini de güneşten korudu. Spin gölgeye geçti ve resmine devam etti. Denizi ve gemileri çok güzel çizdi. Sonra resmi Örümcek Adam'a gösterdi. "Paylaştığın için teşekkürler, Örümcek Adam, bu resim senin!" dedi Spin.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut ve mecazlı bir kavram; 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 2: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Bir hissin haber vermesi soyut bir anlatım, 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0064` birebir aynı, ardından `@onarim: b0fa278ce1b729aa78aea7f7abaaf0f84ee449e8`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0066 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Ghost-Spider
@tohum: orumcek_adam-0066
- yer: ev (Takımın gizli evi.)
- tema: sırayla oynamak
- yan: Ghost-Spider
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'hediye', fiil 'bulmak', sıfat 'utangaç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Ghost-Spider
@plan: kutu yüksek dolabın üstündeydi ve alamadı | ağ atıp kutuyu aşağı indirdi
@tohum: orumcek_adam-0066
@degisim: utangaç -> yüksek
Gizli evde Örümcek Adam ile Ghost-Spider sırayla bir bulma oyunu oynuyordu. Bu kez arkadaşı küçük bir hediye kutusunu sakladı. Örümcek Adam kutuyu dolabın üstünde gördü ama dolap çok yüksekti. Hemen ince bir ağ attı. Ağ kutuya yapıştı ve kutu yavaşça onun ellerine indi. "Buldum!" dedi Örümcek Adam sevinçle. Kutuyu açtı ve içinde kağıttan bir yıldız gördü. Arkadaşı güldü ve ellerini çırptı. "Şimdi sıra sende," dedi arkadaşı. Örümcek Adam çok sevindi, çünkü hediye kutusunu kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kutu yavaşça onun ellerine indi"
   - Cümle 5: «Ağ kutuya yapıştı ve kutu yavaşça onun ellerine indi.»
   - Açıklama: 'Onun' zamiri Örümcek Adam'ı mı arkadaşını mı gösterdiği belirsizdir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0066` birebir aynı, `@degisim: utangaç -> yüksek` (tutuyorsan), ardından `@onarim: 56635a4ec4cbcb0ed9031900f146a7d04d2d9f80`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0067 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: top arkaya doğru yuvarlandı ve dondurmaya gitti | sorunu fark etti ve topu hemen tuttu
@tohum: orumcek_adam-0067
Parkın oyun alanında Örümcek Adam top oyununa başladı. Vanilyalı dondurması küçük bir kapta, arkasındaki çimlerin üstünde duruyordu. Top bir ağaca çarptı ve arkaya, dondurmaya doğru yuvarlandı. Örümcek Adam bunu görmedi ama örümcek hissi bir sorun olduğunu haber verdi. Hızla döndü ve koştu. Topu dondurmanın hemen önünde iki eliyle tuttu. Dondurma kabın içinde hareketsiz duruyordu. Dondurmasından bir kaşık aldı ve tadına baktı. Topu yeniden ağaca doğru attı. Örümcek Adam çok sevindi, çünkü hem oyunu hem de dondurması kurtulmuştu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yuvarlandı ve dondurmaya gitti"
   - Cümle 0 (plan satırı): «top arkaya doğru yuvarlandı ve dondurmaya gitti | sorunu fark etti ve topu hemen tuttu»
   - Açıklama: Top dondurmaya 'gitmez'; fiil öznesine uygun değil, 'doğru yuvarlandı' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "arkasındaki çimlerin üstünde duruyordu"
   - Cümle 2: «Vanilyalı dondurması küçük bir kapta, arkasındaki çimlerin üstünde duruyordu.»
   - Açıklama: 'Arkasındaki' kimin ya da neyin arkası olduğu belli değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "dondurmaya doğru yuvarlandı"
   - Cümle 3: «Top bir ağaca çarptı ve arkaya, dondurmaya doğru yuvarlandı.»
   - Açıklama: Sorun yalnız bir tehlike anı; top dondurmaya ulaşmadan aynı an tutuluyor, çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi bir sorun olduğunu haber verdi"
   - Cümle 4: «Örümcek Adam bunu görmedi ama örümcek hissi bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
   - Açıklama: Bir hissin haber vermesi soyut bir anlatım, 3 yaşındaki çocuk için uygun değil.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hem oyunu hem de dondurması kurtulmuştu"
   - Cümle 10: «Örümcek Adam çok sevindi, çünkü hem oyunu hem de dondurması kurtulmuştu.»
   - Açıklama: Oyun kurtulmaz; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0067` birebir aynı, ardından `@onarim: be7729ef248e2a5e7d91dc1032a625dcc6e13bbd`, sonra gövde.
