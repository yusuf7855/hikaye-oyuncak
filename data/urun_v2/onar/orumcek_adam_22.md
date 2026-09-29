# Editör görevi (onarım): Örümcek Adam, onarım partisi 22

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/orumcek_adam_onar22.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/orumcek_adam_onar22.txt --ad urun_v2`
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

### Hikâye 1: tohum orumcek_adam-0069 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Gizli evin dışında yağmur sessizce yağıyordu. Örümcek Adam içeride küplerle basit bir kule yaptı. Sonra kulenin en üstüne büyük ve ağır bir turp koydu. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Turp ağırdı ve alt kat dardı, bu yüzden kule sallanıyordu. Örümcek Adam önce turpu ve üstteki küpleri tek tek indirdi. Sonra alt kata dört küp daha koydu. Küpleri yeniden üst üste dizdi. Turpu da en üste yerleştirdi. Bu kez kule hiç sallanmadı ve sağlam durdu. Örümcek Adam bundan sonra her kuleye geniş bir alt katla başladı.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kulenin en üstüne büyük ve ağır bir turp koydu"
   - Cümle 3: «Sonra kulenin en üstüne büyük ve ağır bir turp koydu.»
   - Açıklama: Küp kulenin üstüne turp koymak sebepsiz ve saçma bir olay; sorunu bu yapay durum doğuruyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kulenin en üstüne büyük ve ağır bir turp koydu"
   - Cümle 3: «Sonra kulenin en üstüne büyük ve ağır bir turp koydu.»
   - Açıklama: Kuleye turp koymak sebepsiz ve yapay bir nesne getiriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "büyük ve ağır bir turp"
   - Cümle 3: «Sonra kulenin en üstüne büyük ve ağır bir turp koydu.»
   - Açıklama: Turp evde sebepsizce beliriyor ve oyuna hiçbir gerekçeyle katılıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 4: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Hissin haber vermesi soyut ve mecazlı bir anlatım; küçük çocuk için anlaşılmaz.
   - Açıklama: 'Örümcek hissi' ve onun haber vermesi soyut bir kavram, 3 yaşındaki çocuk anlamaz.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Turp ağırdı ve alt kat dardı, bu yüzden kule sallanıyordu"
   - Cümle 5: «Turp ağırdı ve alt kat dardı, bu yüzden kule sallanıyordu.»
   - Açıklama: Sorun ancak 5. cümlede söyleniyor, ilk 3 cümlede değil.
6. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Turp ağırdı ve alt kat dardı"
   - Cümle 5: «Turp ağırdı ve alt kat dardı, bu yüzden kule sallanıyordu.»
   - Açıklama: Sorun ilk üç cümlede söylenmiyor; ancak 5. cümlede açıkça ortaya çıkıyor.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra alt kata dört küp daha koydu"
   - Cümle 7: «Sonra alt kata dört küp daha koydu.»
   - Açıklama: Çözüm indirme, alt kata ekleme, yeniden dizme ve turpu koyma olarak ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0069` birebir aynı, `@degisim: tasarlamak -> yapmak` (tutuyorsan), ardından `@onarim: 5ffa59440c1d8a02f36ee5c869f763ae6c4a5a59`, sonra gövde.

### Hikâye 2: tohum orumcek_adam-0071 (deneme 2 -> 3)

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
Rüzgar hafif hafif esiyordu. Örümcek Adam ile Spin kumsalda kale yapıyordu, yanlarında bir çuval vardı. Ama dalgalar gittikçe kaleye yaklaşıyordu. Birden Örümcek Adam örümcek hissiyle büyük bir dalganın geldiğini anladı. "Büyük bir dalga geliyor, kumu yukarı taşıyalım!" dedi Örümcek Adam. "Sen çok zekisin, Örümcek Adam," dedi Spin. Örümcek Adam çuvalı ıslak kumla doldurdu. Çuvalı kuru kumun olduğu yere taşıdı. İkisi yeni kaleyi orada birlikte yaptı. Az sonra büyük dalga geldi ve eski yere çarptı. Yeni kale yukarıda sağlam duruyordu. "Teşekkürler, Spin, kalemiz artık güvende!" dedi Örümcek Adam.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dalganın geldiğini anladı"
   - Cümle 4: «Birden Örümcek Adam örümcek hissiyle büyük bir dalganın geldiğini anladı.»
   - Açıklama: Dalga henüz gelmemiş; 'geleceğini' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle büyük bir dalganın"
   - Cümle 4: «Birden Örümcek Adam örümcek hissiyle büyük bir dalganın geldiğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissiyle büyük bir"
   - Cümle 4: «Birden Örümcek Adam örümcek hissiyle büyük bir dalganın geldiğini anladı.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram; 3 yaşındaki çocuk bilmez.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Örümcek Adam çuvalı ıslak kumla doldurdu"
   - Cümle 7: «Örümcek Adam çuvalı ıslak kumla doldurdu.»
   - Açıklama: Çözüm çuvalı doldurma, taşıma ve kaleyi yeniden yapma olarak ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0071` birebir aynı, `@degisim: süzülmek -> taşımak` (tutuyorsan), ardından `@onarim: a4c8c35b0448c9ae28d5be8c0125c41a8275696c`, sonra gövde.

### Hikâye 3: tohum orumcek_adam-0074 (deneme 2 -> 3)

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
Örümcek Adam karlı bir günde parkta kardan bir heykel yapıyordu. Heykelin boynuna kırmızı bir atkı takmıştı. Ama sert bir rüzgar esti ve atkıyı heykelden uzaklaştırdı. Atkı havada uçtu ve oyun alanının yüksek duvarına takıldı. Örümcek Adam süper gücüyle duvara tırmandı ve atkıyı aldı. Sonra aşağı indi ve atkıyı heykele sıkıca bağladı. Heykelin kolları için çalının yanından iki kuru dal aldı. Dalları beyaz karın içine yavaşça yerleştirdi. Örümcek Adam kardan heykelini bitirdi ve mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Heykelin kolları için çalının yanından iki kuru dal aldı"
   - Cümle 7: «Heykelin kolları için çalının yanından iki kuru dal aldı.»
   - Açıklama: Sorun çözüldükten sonra atkıyla ilgisi olmayan yeni bir dal ve kol işi ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0074` birebir aynı, `@degisim: meşgul -> beyaz` (tutuyorsan), ardından `@onarim: 343acf97175d7080858e4b3e1a148110832d5035`, sonra gövde.

### Hikâye 4: tohum orumcek_adam-0080 (deneme 2 -> 3)

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
Bir sabah Örümcek Adam ile Hulk gizli evin önünde oturuyordu. Örümcek Adam ağacın en yüksek dalında kırmızı bir elma gördü. Hulk elmayı çok istedi ama dal çok yüksekti. "Elmayı ağla çekeceğim, ama sert yere düşmesin," dedi Örümcek Adam. Hulk kapının önündeki paspası getirdi ve ağacın altına serdi. Örümcek Adam elmaya ağ attı ve yavaşça çekti. Elma daldan koptu ve yumuşak paspasın üstüne düştü. Yumuşak paspas elmayı çok iyi korudu. Örümcek Adam elmayı aldı ve Hulk'a gösterdi. "Teşekkürler, Örümcek Adam, elma çok güzel!" dedi Hulk. Örümcek Adam bundan sonra her elmayı paspasın üstüne indirdi.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Örümcek Adam bundan sonra her elmayı paspasın üstüne indirdi"
   - Cümle 11: «Örümcek Adam bundan sonra her elmayı paspasın üstüne indirdi.»
   - Açıklama: Son cümle olaydan çıkan bir ders ya da sıcak kapanış değil, sıradan bir alışkanlık eylemiyle bitiyor.
   - Açıklama: Hedef Hulk'un elmayı alması ama elma yalnız gösteriliyor ve son cümle sıcak bir kapanış yerine kuru bir alışkanlık bildiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0080` birebir aynı, `@degisim: sergilemek -> göstermek` (tutuyorsan), ardından `@onarim: 4dadd7eca027232eefb4b9ddd9e2d272e03fe14d`, sonra gövde.

### Hikâye 5: tohum orumcek_adam-0081 (deneme 2 -> 3)

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
Limanın yanında rüzgar hızlı hızlı esiyordu. Örümcek Adam ile Ghost-Spider kumsalda parlak karton bir yıldızla oynuyordu. Birden rüzgar yıldızı uçurdu ve yıldız bir daha görünmedi. İkisi kumsala baktı ama yıldızı bulamadı. Sonra yüksek bir duvarın üstünden "hışır hışır" diye bir ses geldi. "Orada ne var acaba?" diye sordu arkadaşı. Örümcek Adam da bu sesi çok merak etti. Süper gücüyle duvara tırmandı ve duvarın üstüne baktı. Karton yıldız orada rüzgarda sallanıyordu. Örümcek Adam yıldızı aldı ve aşağı indi. İkisi yıldızla yeniden oynadı ve gülüştü. Örümcek Adam çok sevindi, çünkü sesi yapan kayıp yıldızı bulmuştu.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yıldız bir daha görünmedi"
   - Cümle 3: «Birden rüzgar yıldızı uçurdu ve yıldız bir daha görünmedi.»
   - Açıklama: Yıldızın bir daha görünmediği söyleniyor ama sonra bulunuyor.
2. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: ""Orada ne var acaba?" diye sordu arkadaşı"
   - Cümle 6: «"Orada ne var acaba?" diye sordu arkadaşı.»
   - Açıklama: 'Arkadaşı' kimin arkadaşı ve konuşanın kim olduğu belli değil.
3. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "diye sordu arkadaşı"
   - Cümle 6: «"Orada ne var acaba?" diye sordu arkadaşı.»
   - Açıklama: Soruyu soranın adı verilmiyor, yalnız 'arkadaşı' deniyor; konuşan açıkça belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0081` birebir aynı, ardından `@onarim: a8779ec46112a54f59f075dc7c76db3344173802`, sonra gövde.

### Hikâye 6: tohum orumcek_adam-0082 (deneme 1 -> 2)

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
@plan: koşarken bankı salladı ve resim dala uçtu | özür diledi ve ağ atıp resmi daldan aldı
@tohum: orumcek_adam-0082
@degisim: soğumak -> kurumak
Bir sabah Örümcek Adam parkta Spin ile top oynuyordu. Spin'in krem rengi, pürüzsüz kağıda yaptığı resim bankta kuruyordu. Örümcek Adam koşarken bankı salladı ve resim bir dala uçtu. Spin dala bakıp üzüldü. "Özür dilerim, Spin, hiç dikkat etmedim," dedi Örümcek Adam. Sonra bir ağ attı ve resmi daldan aldı. Resim sağlamdı ve boyası da kurumuştu. Örümcek Adam resmi Spin'e uzattı. Spin resmini sıkıca tuttu ve gülümsedi. "Teşekkürler, Örümcek Adam, resmim yine çok güzel!" dedi Spin.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "krem rengi, pürüzsüz kağıda"
   - Cümle 2: «Spin'in krem rengi, pürüzsüz kağıda yaptığı resim bankta kuruyordu.»
   - Açıklama: 'Pürüzsüz' ve 'krem rengi' 3 yaşındaki çocuğun bilmediği kelimeler.
   - Açıklama: 'Pürüzsüz' ve 'krem rengi' 3 yaşındaki çocuğun bilmeyebileceği kelimeler.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "koşarken bankı salladı ve resim bir dala uçtu"
   - Cümle 3: «Örümcek Adam koşarken bankı salladı ve resim bir dala uçtu.»
   - Açıklama: Bankın sallanması bir kağıdı yüksek bir dala uçurmaz; sorunun sebebi akla yatkın değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bankı salladı ve resim bir dala uçtu"
   - Cümle 3: «Örümcek Adam koşarken bankı salladı ve resim bir dala uçtu.»
   - Açıklama: Bankın sallanmasıyla resmin ağaç dalına uçması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0082` birebir aynı, `@degisim: soğumak -> kurumak` (tutuyorsan), ardından `@onarim: 3fd9cd73ecd53c4c2aae771007f0c8307deb5821`, sonra gövde.

### Hikâye 7: tohum orumcek_adam-0083 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Hulk
@tohum: orumcek_adam-0083
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: paylaşmak
- yan: Hulk
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'kaya', fiil 'düşünmek', sıfat 'sırılsıklam'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | Hulk
@plan: rüzgar tek havluyu duvarın tepesine uçurdu | duvara tırmanıp havluyu aldı ve paylaştı
@tohum: orumcek_adam-0083
Örümcek Adam parkta Hulk ile fıskiyenin suyunda oynuyordu. İkisi de sırılsıklam oldu ve çok güldü. Ama Örümcek Adam'ın tek havlusunu rüzgar yüksek bir duvarın tepesine uçurdu. Hulk büyük bir kayanın üstüne oturdu ve duvara baktı. Örümcek Adam biraz düşündü. Sonra duvara hızla tırmandı ve havluyu aldı. Aşağı indi ve önce Hulk'ın yeşil kollarını kuruladı. "Havlu senin, neden bana veriyorsun?" diye sordu Hulk. "Havlu ikimize de yeter, paylaşalım," dedi Örümcek Adam. Sonra kendi yüzünü sildi. Hulk sevinçle gülümsedi. Kuruyan iki arkadaş parkta mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hulk büyük bir kayanın üstüne oturdu"
   - Cümle 4: «Hulk büyük bir kayanın üstüne oturdu ve duvara baktı.»
   - Açıklama: Kaya sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra duvara hızla tırmandı"
   - Cümle 6: «Sonra duvara hızla tırmandı ve havluyu aldı.»
   - Açıklama: Yüksek duvara tırmanma, kartın güvenli kullanım satırının istediği gibi süper güç olarak belirtilmiyor ve çocuk bunu taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0083` birebir aynı, ardından `@onarim: f14b98213b7e808d54cb11bd11f0b8a0e8f50dcd`, sonra gövde.

### Hikâye 8: tohum orumcek_adam-0084 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kumsaldan garip ve ince bir ses geldi | sesin geldiği yere yürüdü ve kumdaki şişeyi buldu
@tohum: orumcek_adam-0084
@degisim: cömert -> garip
Rüzgar hafif hafif esiyordu. Örümcek Adam kumsala küçük bir halı serdi ve oturdu. Birden yakından garip ve ince bir ses geldi. Aynı anda örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam sesi çok merak etti. Kalktı ve sesin geldiği yere yürüdü. Kumun içinde yarısı gömülü bir cam şişe buldu. Rüzgar şişenin ağzından geçiyordu ve ses oradan çıkıyordu. Örümcek Adam şişenin ağzına kendisi de üfledi. Aynı ince ses yine duyuldu. Örümcek Adam şişeyi kumdan çekip çıkardı ve çöp kutusuna attı. Sonra halısına döndü ve denize baktı. Örümcek Adam çok sevindi, çünkü sesi bulmuş ve şişeyi kumsaldan kaldırmıştı.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden yakından garip ve ince bir ses geldi"
   - Cümle 3: «Birden yakından garip ve ince bir ses geldi.»
   - Açıklama: Sorun zararsız bir ses; örümcek hissinin haber verdiği bir sorun olarak zayıf ve çocuğun önemseyeceği bir şey değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "garip ve ince bir ses geldi"
   - Cümle 3: «Birden yakından garip ve ince bir ses geldi.»
   - Açıklama: Şişeden gelen ince ses çocuğun önemseyeceği gerçek bir sorun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 4: «Aynı anda örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut bir kavram ve bir hissin haber vermesi mecaz; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Örümcek hissi haber verdi' soyut ve mecazlı bir anlatım, 3 yaşındaki çocuk anlamaz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 4: «Aynı anda örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Örümcek hissi tehlike yokken sebepsizce devreye giriyor ve olayda işe yaramıyor.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Örümcek Adam şişenin ağzına kendisi de üfledi"
   - Cümle 9: «Örümcek Adam şişenin ağzına kendisi de üfledi.»
   - Açıklama: Çocuk kumda bulduğu cam şişeyi alıp ağzına üflemeyi taklit edebilir.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "şişenin ağzına kendisi de üfledi"
   - Cümle 9: «Örümcek Adam şişenin ağzına kendisi de üfledi.»
   - Açıklama: Kumdan bulunan cam şişeyi elleyip ağzına üflemek çocuğun taklit edebileceği sağlıksız ve tehlikeli bir davranış.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şişenin ağzına kendisi de üfledi"
   - Cümle 9: «Örümcek Adam şişenin ağzına kendisi de üfledi.»
   - Açıklama: Şişeye üflemek çözüme bir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0084` birebir aynı, `@degisim: cömert -> garip` (tutuyorsan), ardından `@onarim: 9f0f760389f4af003583b8d6e91168ed169d230e`, sonra gövde.

### Hikâye 9: tohum orumcek_adam-0085 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | Spin
@tohum: orumcek_adam-0085
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Spin
- özellik: tırman (Duvarlara tırmanabilir.)
- kelimeler: isim 'gardırop', fiil 'göstermek', sıfat 'şaşkın'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Örümcek Adam | park | Spin
@plan: yakından bakınca resmin düz olup olmadığını göremedi | arkadaşından yardım istedi ve resmi düz astı
@tohum: orumcek_adam-0085
@degisim: gardırop -> resim
Örümcek Adam parkta Spin'in büyük resmini duvara asmak istedi. Resmi alıp duvara hızla tırmandı. Ama duvara çok yakındı ve resmin düz olup olmadığını göremedi. Örümcek Adam biraz şaşkındı. "Spin, doğru yeri bana gösterir misin?" diye sordu Örümcek Adam. Spin aşağıda durdu ve resme dikkatle baktı. "Sol tarafı biraz yukarı kaldır," dedi Spin. Örümcek Adam resmin sol tarafını yukarı kaldırdı. Spin başını salladı ve iki elini çırptı. "Şimdi tam düz oldu!" dedi Spin. Örümcek Adam resmi duvara bantla yapıştırdı ve aşağı indi. Örümcek Adam çok sevindi, çünkü yardım isteyince resim düz asılmıştı.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "büyük resmini duvara asmak istedi"
   - Cümle 1: «Örümcek Adam parkta Spin'in büyük resmini duvara asmak istedi.»
   - Açıklama: Kartın park tarifi oyun alanı, ağaçlar ve çiçek bahçesinden söz ediyor; resim asılacak bir duvar tarifte yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0085` birebir aynı, `@degisim: gardırop -> resim` (tutuyorsan), ardından `@onarim: bb745a1c8d78279e0a1fc37bcb0875a50effc496`, sonra gövde.

### Hikâye 10: tohum orumcek_adam-0086 (deneme 1 -> 2)

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
Kuşlar ötüyordu ve Örümcek Adam parkta top oynuyordu. Hulk yakındaki bankta gazete okuyor ve çikolatalı kurabiye yiyordu. Örümcek Adam topu başının üstünden arkaya attı ve top gazeteye düştü. Gazetenin sayfaları çimenlere dağıldı. Birden örümcek hissi ona bir sorun olduğunu haber verdi. Örümcek Adam dönüp dağılan sayfaları gördü. "Özür dilerim, Hulk, bankın yanında oynamamalıydım," dedi Örümcek Adam. Sonra bütün sayfaları hızla toplayıp Hulk'a verdi. Hulk gülümsedi ve ona bir kurabiye uzattı. "Tamam, gel, birlikte yiyelim," dedi Hulk. Örümcek Adam çok sevindi, çünkü arkadaşı ona hiç kızmamıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 5: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' soyut ve mecazlı bir kavram; his haber vermez ve 3 yaşındaki çocuk bunu anlamaz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birden örümcek hissi ona"
   - Cümle 5: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: 'Örümcek hissi' ve 'sorun olduğunu haber verdi' 3 yaşındaki çocuk için soyut bir kavram.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Birden örümcek hissi ona bir sorun olduğunu haber verdi"
   - Cümle 5: «Birden örümcek hissi ona bir sorun olduğunu haber verdi.»
   - Açıklama: Örümcek hissi sorun zaten olup görüldükten sonra geliyor, bu yüzden özellik işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0086` birebir aynı, ardından `@onarim: da542b61851917fc865eb7b22d624694dddf2f65`, sonra gövde.

### Hikâye 11: tohum orumcek_adam-0089 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Örümcek Adam | park | -
@tohum: orumcek_adam-0089
- yer: park (Şehrin büyük parkı; oyun alanı, ağaçlar ve çiçek bahçesi vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: ağ (Bileğinden ağ atar.)
- kelimeler: isim 'pilav', fiil 'süpürmek', sıfat 'devasa'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Örümcek Adam | park | -
@plan: kaydırağa yukarıdan kozalaklar düştü | dalların altına ağ atıp kozalakları süpürdü
@tohum: orumcek_adam-0089
@degisim: pilav -> kozalak
Örümcek Adam parkta kaydırağın önünde duruyordu. Birden kaydıraktan tık tık diye sesler geldi. Örümcek Adam bu sesleri merak etti ve yaklaştı. Kaydırağın üstünde küçük kozalaklar vardı. Örümcek Adam başını kaldırdı ve yukarı baktı. Hemen üstte devasa bir çam ağacı vardı. Rüzgar dalları sallıyordu ve kozalaklar aşağı düşüyordu. Örümcek Adam bileğinden geniş bir ağ attı. Ağ, dalların altında bir çatı gibi gerildi. Yeni düşen kozalaklar ağın üstünde kaldı. Sonra Örümcek Adam eski kozalakları eliyle süpürdü. Kaydırak tertemiz oldu ve Örümcek Adam mutlu mutlu kaydı.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Örümcek Adam bu sesleri merak etti ve yaklaştı.»
   - Açıklama: İlk üç cümlede yalnız ses duyuluyor; kaydıraktaki kozalak sorunu ancak 4. cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Kaydırağın üstünde küçük kozalaklar vardı.»
   - Açıklama: Kaydıraktaki kozalak sorunu ilk 3 cümlede değil, 4. cümlede ortaya çıkıyor ve kaymak hedefi hiç açıkça söylenmiyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hemen üstte devasa"
   - Cümle 6: «Hemen üstte devasa bir çam ağacı vardı.»
   - Açıklama: 'Devasa' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir çatı gibi gerildi"
   - Cümle 9: «Ağ, dalların altında bir çatı gibi gerildi.»
   - Açıklama: Benzetme küçük çocuğa uygun değil.
   - Açıklama: Benzetme (çatı gibi) küçük çocuk için soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: orumcek_adam-0089` birebir aynı, `@degisim: pilav -> kozalak` (tutuyorsan), ardından `@onarim: 0e626958bb7d807b0bf26e3e62495320db34687b`, sonra gövde.
