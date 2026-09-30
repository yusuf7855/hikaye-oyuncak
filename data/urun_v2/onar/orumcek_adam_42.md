# Editör görevi (onarım): Örümcek Adam, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0093 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0093
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: kaybolan eşya
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'bilye', fiil 'sunmak', sıfat 'yavaş'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: mavi bilye yokuştan yuvarlandı ve kayboldu | aşağı yürüyüp bilyeyi bankın yanında buldu
@tohum: orumcek_adam-0093
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin parkın oyun alanında bilye oynuyordu. Birden Spin'in mavi bilyesi yokuştan aşağı yuvarlandı ve kayboldu. "Bilyemi bulamıyorum, Örümcek Adam," dedi Spin üzgün bir sesle. Örümcek Adam yavaş yavaş aşağı yürüdü. Bir bankın yanına geldi. Orada örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam hemen durdu ve yere baktı. Mavi bilye tam ayağının önünde, kuru yaprakların arasındaydı. Örümcek Adam onu aldı ve iki eliyle Spin'e sundu. "İşte bilyen, Spin," dedi Örümcek Adam. Spin sevinçle bilyesini tuttu. İki arkadaş oyun alanına döndü ve bilye oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 7: «Orada örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Yerde duran kayıp bilye bir tehlike ya da sorun değildir; 'sorun olduğunu haber verdi' anlamca yerinde değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Orada örümcek hissi ona bir sorun olduğunu"
   - Cümle 7: «Orada örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'bir sorun olduğunu haber verdi' soyut, 3 yaşındaki çocuğun anlamayacağı bir anlatım.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Orada örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 7: «Orada örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Sorun zaten biliniyorken örümcek hissinin 'bir sorun' haber vermesi işlevsiz ve bilyeyi buldurmayı sebepsizce getiriyor.
   - Açıklama: Örümcek hissi bilyeyi bulduruyor gibi sebepsizce devreye giriyor ve çözümü tesadüfle getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0093` birebir aynı, ardından `@onarim: 4e75015d393ca173fd88d7b82cc4fba2ec7d6783`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0098 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0098
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: paylaşmak
- yan: Spin
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'kamyon', fiil 'giyinmek', sıfat 'çizgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: kum dökülüyordu ve kale büyümüyordu | oyuncak kamyonunu arkadaşıyla paylaştı
@tohum: orumcek_adam-0098
@degisim: giyinmek -> taşımak
Bir sabah Örümcek Adam parkta çizgili oyuncak kamyonuyla oynuyordu. Biraz uzakta Spin kumdan bir kale yapıyordu. Ama Spin kumu elleriyle taşıyamıyordu, çünkü parmaklarından dökülüyordu. O sırada örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi. Hemen Spin'in yanına gitti ve onun üzgün yüzünü gördü. "Bu kale hiç büyümüyor," dedi Spin. Örümcek Adam kamyonunu Spin'e uzattı. "Al, Spin, kamyonumu birlikte kullanalım," dedi Örümcek Adam. Spin kamyonu kumla doldurdu ve kaleye götürdü. Sonra sırayla taşıdılar ve duvarlar hızla yükseldi. İkisi de çok sevindi, çünkü paylaşınca kale çabucak büyümüştü.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi"
   - Cümle 4: «O sırada örümcek hissi Örümcek Adam'a bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuk anlamaz.
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve bir hissin haber vermesi mecaz; 3 yaşındaki çocuk için uygun değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hemen Spin'in yanına gitti"
   - Cümle 5: «Hemen Spin'in yanına gitti ve onun üzgün yüzünü gördü.»
   - Açıklama: Önceki cümlenin öznesi 'örümcek hissi' olduğu için gidenin kim olduğu belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0098` birebir aynı, `@degisim: giyinmek -> taşımak` (tutuyorsan), ardından `@onarim: 0e3b806d65900ef3f98646b57b25bc8023c28793`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0101 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Hulk
@tohum: orumcek_adam-0101
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Hulk
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'harita', fiil 'beslemek', sıfat 'sağlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Hulk
@plan: harita suyun kenarında kaldı ve dalga geliyordu | haritayı hemen aldı ve özür diledi
@tohum: orumcek_adam-0101
@degisim: beslemek -> yemek
Kumsalda Örümcek Adam ile Hulk hazine oyunu oynuyordu. Örümcek Adam, Hulk'ın çizdiği haritayı suyun kenarına bıraktı. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Uzaktan büyük bir dalga geliyordu. Örümcek Adam haritayı hemen aldı ve sudan uzağa koştu. Dalga, haritanın durduğu yeri ıslattı. "Özür dilerim, Hulk, haritanı suya çok yakın bıraktım," dedi Örümcek Adam. "Teşekkürler, harita kuru kaldı," dedi Hulk. İkisi haritadaki yolu izleyip büyük bir kayanın yanına yürüdü. Kayanın arkasında Hulk'ın sakladığı sağlıklı meyveler vardı. Örümcek Adam ile Hulk kumda oturdu ve meyveleri mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' soyut anlatım, küçük çocuğa uygun değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede yalnız bir sorun olduğu söyleniyor; dalga tehlikesi ancak 4. cümlede açıkça geçiyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: İlk üç cümlede yalnız bir sorun olduğu söyleniyor; dalga sorunu ancak dördüncü cümlede açıkça söyleniyor.
4. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Uzaktan büyük bir dalga geliyordu"
   - Cümle 4: «Uzaktan büyük bir dalga geliyordu.»
   - Açıklama: Su kenarına yaklaşan büyük dalga küçük çocuk için korkutucu bir öğe.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0101` birebir aynı, `@degisim: beslemek -> yemek` (tutuyorsan), ardından `@onarim: c2562ec8e055f9d4b1d2571834af0f0017bcda78`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0103 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0103
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'sakız', fiil 'dilemek', sıfat 'kapalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: büyük bir bina denize inen güneşi kapatıyordu | binanın duvarına tırmanıp güneşi gördü
@tohum: orumcek_adam-0103
@degisim: sakız -> güneş
Örümcek Adam limanda yürüyordu. Güneş denize doğru iniyordu ve gökyüzü kırmızı olmuştu. Ama büyük bir liman binası güneşi kapatıyordu. Örümcek Adam güneş denize inerken bir dilek dilemek istiyordu. Binanın kapısı kapalıydı. Örümcek Adam süper gücüyle binanın duvarına tırmandı. Duvarın üstünden kırmızı güneşi ve parlayan denizi gördü. Güneşe baktı ve yarın da güneşli bir gün olsun diye dilek diledi. Güneş yavaş yavaş denize indi. Örümcek Adam mutlu mutlu duvardan indi. Örümcek Adam bundan sonra batan güneşi hep bu duvarın üstünden izledi.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "batan güneşi hep bu duvarın üstünden izledi"
   - Cümle 11: «Örümcek Adam bundan sonra batan güneşi hep bu duvarın üstünden izledi.»
   - Açıklama: Yüksek bir bina duvarının üstüne çıkıp güneşe bakmak alışkanlık olarak gösteriliyor ve çocuk için taklit edilince tehlikeli.
   - Açıklama: Yüksek bir bina duvarının üstünde oturup güneş izlemek çocuğun taklit edebileceği bir yükseğe çıkma alışkanlığı olarak sunuluyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "bundan sonra batan güneşi hep bu duvarın üstünden izledi"
   - Cümle 11: «Örümcek Adam bundan sonra batan güneşi hep bu duvarın üstünden izledi.»
   - Açıklama: Son cümle olaydan çıkan bir ders değil, sonraki günlere atlayan bir alışkanlık anlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0103` birebir aynı, `@degisim: sakız -> güneş` (tutuyorsan), ardından `@onarim: 05ec618f360fdd5a6c470a61a10f8c9f62605fd6`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0108 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0108
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'zarf', fiil 'ovuşturmak', sıfat 'tuzlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: yüksek duvardan garip bir ses geldi | duvara tırmanıp sesi çıkaran uçurtmayı buldu
@tohum: orumcek_adam-0108
@degisim: zarf -> uçurtma
Rüzgar hafif hafif esiyordu. Örümcek Adam kıyıda, denizin tuzlu suyuyla oynarken garip bir ses duydu. Ses yüksek bir taş duvarın tepesinden geliyordu. Örümcek Adam gözlerini ovuşturdu ve yukarı baktı. Ama aşağıdan hiçbir şey göremedi. Sesi çok merak etti. Örümcek Adam süper gücüyle duvara tırmandı ve tepeye çıktı. Orada kırmızı bir uçurtma takılı kalmıştı. Uçurtmanın kağıdı rüzgarda sallanıp ses çıkarıyordu. Örümcek Adam uçurtmayı dikkatle kurtardı ve aşağı indi. Örümcek Adam çok sevindi, çünkü o garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Örümcek Adam gözlerini ovuşturdu"
   - Cümle 4: «Örümcek Adam gözlerini ovuşturdu ve yukarı baktı.»
   - Açıklama: Göz ovuşturma olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Örümcek Adam çok sevindi"
   - Cümle 11: «Örümcek Adam çok sevindi, çünkü o garip sesin nereden geldiğini bulmuştu.»
   - Açıklama: Tek karakterli hikayede 'Örümcek Adam' adı art arda cümlelerde gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0108` birebir aynı, `@degisim: zarf -> uçurtma` (tutuyorsan), ardından `@onarim: 57db3c8a83d2f9a3b0755027f84d7b034842d16f`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0109 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0109
- yer: ev (Takımın gizli evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'çim', fiil 'bırakmak', sıfat 'kıvrımlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: koşarken yerdeki resme bastı ve resim buruştu | özür diledi ve resmi açıp duvara astı
@tohum: orumcek_adam-0109
@degisim: kıvrımlı -> yeşil
Örümcek Adam gizli evin önünde koşarak oynuyordu. Spin kağıda yeşil çimler çizmiş, resmi kurusun diye yere bırakmıştı. Örümcek Adam resmi görmedi ve üstüne bastı. Resim buruştu ve Spin çok üzüldü. Örümcek Adam hemen durdu ve Spin'den özür diledi. Resmi yerde bırakmak istemedi, çünkü koşarken yine basabilirdi. Bir örümcek gibi evin dış duvarına tırmandı. Resmi orada düzgünce açtı ve bir çiviye astı. Resim duvarda güneşte kurudu. Spin yukarıdaki resmine baktı ve gülümsedi. Örümcek Adam rahatladı, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kağıda yeşil çimler çizmiş, resmi kurusun diye"
   - Cümle 2: «Spin kağıda yeşil çimler çizmiş, resmi kurusun diye yere bırakmıştı.»
   - Açıklama: Çizilen resim kurumaz; boyanmış resim için 'boyamış' olmalıydı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir örümcek gibi evin dış duvarına tırmandı"
   - Cümle 7: «Bir örümcek gibi evin dış duvarına tırmandı.»
   - Açıklama: Tırmanma süper güç olarak belirtilmeden evin duvarına yapılıyor; güvenli özellik kullanımı satırına aykırı ve çocuk taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0109` birebir aynı, `@degisim: kıvrımlı -> yeşil` (tutuyorsan), ardından `@onarim: 53e411fd012a3f117d3be177ebf0de929bd330e4`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0110 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | -
@tohum: orumcek_adam-0110
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: örümcek hissi (Örümcek hissi bir sorun olduğunu ona haber verir.)
- kelimeler: isim 'gökkuşağı', fiil 'eğlendirmek', sıfat 'yuvarlak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | deniz | -
@plan: dalgalar kum kalesine yaklaşıyordu | kalenin önüne çukur kazdı ve kumdan duvar yaptı
@tohum: orumcek_adam-0110
@degisim: gökkuşağı -> kum
Kumsalda güneşli ve sıcak bir gündü. Örümcek Adam suyun yakınında yuvarlak bir kum kalesi yapıyordu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam denize dikkatle baktı. Her dalga kuma biraz daha yukarı geliyordu. Kale yapmak Örümcek Adam'ı çok eğlendiriyordu. Kalesini kaybetmek istemiyordu. Hemen kalenin önüne uzun bir çukur kazdı. Çıkan kumla çukurun arkasına alçak bir duvar yaptı. Sonra büyük bir dalga geldi. Su çukura doldu ve duvarda durdu. Yuvarlak kale hiç ıslanmadı. Örümcek Adam kalesinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve haber vermesi mecaz; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, küçük çocuğa uygun değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Üçüncü cümle yalnız bir sorun olduğunu söylüyor; dalgaların kaleye yaklaştığı ancak beşinci cümlede anlaşılıyor.
   - Açıklama: Örümcek hissi yalnız bir sorun olduğunu söylüyor; dalgaların kaleye yaklaştığı ancak 5. cümlede açıkça söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0110` birebir aynı, `@degisim: gökkuşağı -> kum` (tutuyorsan), ardından `@onarim: 39bd597993626f4570c88dbe252c194c161795b4`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0111 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | ev | Spin
@tohum: orumcek_adam-0111
- yer: ev (Takımın gizli evi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'bez', fiil 'savrulmak', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | ev | Spin
@plan: rüzgar resimli bezi çatıya savurdu | arkadaşından yardım istedi ve duvara tırmanıp bezi aldı
@tohum: orumcek_adam-0111
Bir sabah Örümcek Adam ile Spin gizli evin önünde oynuyordu. Spin, büyük bir bezin üstüne güzel bir resim yapmıştı. Birden sert bir rüzgar esti ve bez havaya savruldu. Bez çatıda bir yere düştü ve orada saklı kaldı. Spin çok üzüldü, çünkü resmi Örümcek Adam'a hediye edecekti. Örümcek Adam bezi göremedi ve Spin'den yardım istedi. Spin bezin düştüğü yeri görmüştü ve eliyle çatının sol ucunu gösterdi. Örümcek Adam süper gücüyle evin dış duvarına tırmandı. Çatının sol ucunda bezi buldu ve aşağı indi. Spin bezi açtı ve resmi Örümcek Adam'a verdi. Örümcek Adam çok sevindi, çünkü hediyesini Spin ile birlikte bulmuştu.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "arkadaşından yardım istedi"
   - Cümle 0 (plan satırı): «rüzgar resimli bezi çatıya savurdu | arkadaşından yardım istedi ve duvara tırmanıp bezi aldı»
   - Açıklama: Gövdede Örümcek Adam yardım istemiyor; Spin kendiliğinden yeri gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0111` birebir aynı, ardından `@onarim: 4a4c1f36baf2d17fb98198496f306c7d662c51cc`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0116 (deneme 4 -> 5)

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
@plan: açık pencereden esen rüzgar kağıt uçağı çatıya uçurdu | özür dileyip tırmandı ve uçağı çatıdan ayırdı
@tohum: orumcek_adam-0116
@degisim: tablo -> uçak
Rüzgar gizli evin açık penceresinden esiyordu. Örümcek Adam pencereyi açık bırakmıştı ve Hulk kağıttan yaratıcı bir uçak yapıyordu. Birden rüzgar uçağı pencereden dışarı uçurdu ve uçak çatının kenarına takıldı. "Uçağım çok yukarıda kaldı!" dedi Hulk. "Özür dilerim, Hulk, pencereyi ben açık bıraktım," dedi Örümcek Adam. Örümcek Adam hemen evin dış duvarına tırmandı. Uçağı çatının kenarından yavaşça ayırdı ve Hulk'a getirdi. "Sorun yok, dostum," dedi Hulk ve gülümsedi. Sonra Örümcek Adam ile Hulk uçağı birlikte mutlu mutlu uçurdu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kağıttan yaratıcı bir uçak"
   - Cümle 2: «Örümcek Adam pencereyi açık bırakmıştı ve Hulk kağıttan yaratıcı bir uçak yapıyordu.»
   - Açıklama: 'Yaratıcı' bir nesneyi nitelemez; kelime öznesine uymuyor.
   - Açıklama: Uçak yaratıcı olamaz; özellik kelimesi yanlış nesneye bağlanmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kağıttan yaratıcı bir uçak"
   - Cümle 2: «Örümcek Adam pencereyi açık bırakmıştı ve Hulk kağıttan yaratıcı bir uçak yapıyordu.»
   - Açıklama: 'Yaratıcı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "evin dış duvarına tırmandı"
   - Cümle 6: «Örümcek Adam hemen evin dış duvarına tırmandı.»
   - Açıklama: Evin dış duvarından çatı kenarına tırmanıp oyuncak almak çocuğun taklit edebileceği yükseğe tırmanma örneğidir.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam hemen evin dış duvarına tırmandı"
   - Cümle 6: «Örümcek Adam hemen evin dış duvarına tırmandı.»
   - Açıklama: Evin dış duvarından çatıya tırmanma süper güç diye çerçevelenmeden anlatılıyor ve çocuğun taklit edebileceği yükseğe tırmanma örneği oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0116` birebir aynı, `@degisim: tablo -> uçak` (tutuyorsan), ardından `@onarim: 2661108d2000830379855f13f4c83145b5a75530`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0118 (deneme 4 -> 5)

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
@plan: turşu kavanozu kumda suya doğru yuvarlandı | koşup kavanozu suya gelmeden yakaladı
@tohum: orumcek_adam-0118
@degisim: sabırlı -> düz
Örümcek Adam ilk kez turşu deneyecekti ve çok sabırsızlanıyordu. Kumsalda oturdu ve turşu kavanozunu yanına koydu. Ama kum suya doğru iniyordu ve kavanoz yuvarlanmaya başladı. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam arkasına döndü ve kavanozun suya yaklaştığını gördü. Hemen koştu ve kavanozu suya gelmeden yakaladı. Sonra yere oturdu ve kavanozu iki elinin arasında tuttu. Kavanozun kapağını açtı ve bir turşu aldı. Turşu biraz ekşiydi ama Örümcek Adam tadını sevdi. Örümcek Adam bundan sonra kavanozunu hep düz bir yere koydu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kum suya doğru iniyordu"
   - Cümle 3: «Ama kum suya doğru iniyordu ve kavanoz yuvarlanmaya başladı.»
   - Açıklama: Kum inmez; eğimi anlatmak için fiil öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Hisse haber verdirmek soyut bir kişileştirme; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi' haber vermesi soyut ve mecazlı bir anlatımdır.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hemen koştu ve kavanozu suya gelmeden yakaladı"
   - Cümle 6: «Hemen koştu ve kavanozu suya gelmeden yakaladı.»
   - Açıklama: Suya doğru yuvarlanan bir eşyanın peşinden suya koşmak çocuğun taklit edebileceği tehlikeli bir davranıştır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0118` birebir aynı, `@degisim: sabırlı -> düz` (tutuyorsan), ardından `@onarim: 42223c596ccbfad4462987e08ae3215a37a8f44d`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0119 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: çantada bir delik vardı ve paket kayıyordu | düşmek üzere olan paketi yakaladı ve deliği bağladı
@tohum: orumcek_adam-0119
Yağmur gizli evin çatısına tıp tıp vuruyordu. Örümcek Adam içeride paket oyunu oynuyor ve yepyeni bluz paketlerini odalara dağıtıyordu. Ama çantasının köşesinde küçük bir delik vardı ve bir paket kayıyordu. Çanta onun arkasındaydı ve Örümcek Adam deliği göremedi. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Hemen çantasına baktı. Bir paket delikten düşmek üzereydi. Örümcek Adam paketi elleriyle yakaladı. Sonra çantanın delikli köşesini sıkıca bağladı. Kalan paketleri de odalara tek tek bıraktı. Örümcek Adam çok sevindi, çünkü hiçbir paket yere düşmedi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çatısına tıp tıp vuruyordu"
   - Cümle 1: «Yağmur gizli evin çatısına tıp tıp vuruyordu.»
   - Açıklama: Yağmur sesi için yerleşik yansıma 'tıpır tıpır'dır; 'tıp tıp' yanlış kelime.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "paket oyunu oynuyor"
   - Cümle 2: «Örümcek Adam içeride paket oyunu oynuyor ve yepyeni bluz paketlerini odalara dağıtıyordu.»
   - Açıklama: 'Paket oyunu oynamak' anlamı belirsiz, yerleşik olmayan bir söyleyiş.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 5: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Soyut 'örümcek hissi' kavramı kişileştirilmiş; 3 yaşındaki çocuk için anlaşılmaz.
   - Açıklama: 'Örümcek hissi' ve 'sorun' soyut kavramlar küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0119` birebir aynı, ardından `@onarim: 4bf48a4047ec2b560a504634e7bc92f383a3d1f6`, sonra gövde.

### Hikâye 12: tohum orumcek_adam-0120 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | deniz | Spin
@tohum: orumcek_adam-0120
- yer: deniz (Şehrin kumsalı ve limanı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Spin
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'ayçiçeği', fiil 'güzelleşmek', sıfat 'gizemli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | deniz | Spin
@plan: suyun içindeki parlak şey kıyıdan uzaktaydı | ağ atıp parlak şeyi kıyıya çekti
@tohum: orumcek_adam-0120
@degisim: gizemli -> parlak
Kıyıda dalgaların sesi duyuluyordu. Örümcek Adam ile Spin, kuma çizdikleri ayçiçeğinin ortasına bir süs arıyordu. Suyun içinde parlak bir şey gördüler ama o şey kıyıdan uzaktaydı. "Bu ne olabilir, Örümcek Adam?" diye sordu Spin. Örümcek Adam kıyıda durdu ve ağ attı. Ağ parlak şeye yapıştı ve Örümcek Adam onu kıyıya çekti. Parlak şey, içi pembe büyük bir deniz kabuğu çıktı. "Ne güzel bir kabuk!" dedi Spin. Örümcek Adam kabuğu ayçiçeğinin ortasına koydu ve resim daha da güzelleşti. Örümcek Adam bundan sonra uzanamadığı şeyleri ağıyla yavaşça kıyıya çekti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Örümcek Adam bundan sonra uzanamadığı şeyleri ağıyla yavaşça kıyıya çekti"
   - Cümle 10: «Örümcek Adam bundan sonra uzanamadığı şeyleri ağıyla yavaşça kıyıya çekti.»
   - Açıklama: 'Bundan sonra' ile tek seferlik 'çekti' uyuşmuyor; 'çekiyordu' ya da 'çekecekti' olmalı.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Örümcek Adam bundan sonra uzanamadığı şeyleri ağıyla yavaşça kıyıya çekti"
   - Cümle 10: «Örümcek Adam bundan sonra uzanamadığı şeyleri ağıyla yavaşça kıyıya çekti.»
   - Açıklama: Son cümle sıcak bir kapanış ya da olaydan çıkan bir ders değil, genel bir alışkanlık cümlesi; hikaye kapanışsız kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0120` birebir aynı, `@degisim: gizemli -> parlak` (tutuyorsan), ardından `@onarim: 46b904e9c08130cc54fd2ded3babd6a2f31b4d55`, sonra gövde.
