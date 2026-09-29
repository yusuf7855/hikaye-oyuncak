# Editör görevi (onarım): Keloğlan, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar11.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0007 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0007
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kartopu', fiil 'kaplamak', sıfat 'düzenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: kartopu pasta için çok küçüktü | topu karda iterek büyüttü
@tohum: keloglan-0007
Keloğlan dağda Bilgecan Dede'ye kardan bir pasta yapmak istedi. Kar bütün tepeyi kaplamıştı ve Dede ağacın altında kitap okuyordu. Ama Keloğlan'ın elleri küçüktü, bu yüzden kartopu da çok küçük oldu. Pasta için büyük bir top gerekiyordu. Keloğlan biraz sakardı ve kartopu elinden düştü. Top karda yuvarlandı ve biraz büyüdü. Keloğlan bunu gördü ve topu karda uzun uzun itti. Top kocaman oldu ve pastaya benzedi. Keloğlan pastanın üstüne küçük taşları yan yana, düzenli dizdi. "Dede, bak, sana bir sürprizim var!" dedi Keloğlan. Bilgecan Dede kitabını kapattı ve pastayı gördü. "Ne güzel bir pasta, çok teşekkür ederim, Keloğlan!" dedi Bilgecan Dede.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve kartopu elinden düştü"
   - Cümle 5: «Keloğlan biraz sakardı ve kartopu elinden düştü.»
   - Açıklama: Çözüm figürün düşünmesinden değil, rastlantısal bir düşmeden çıkıyor.
   - Açıklama: Çözüm figürün düşüncesinden değil tesadüfi bir düşürmeden sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0007` birebir aynı, ardından `@onarim: be249c2923fe9a518f5e7049fed47eabe9486da4`, sonra gövde.

### Hikâye 2: tohum keloglan-0013 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0013
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'askı', fiil 'dökmek', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: tepede ince bir sesin nereden geldiği belli değildi | suyu yere döktü ve sesin şişeden geldiğini buldu
@tohum: keloglan-0013
@degisim: işaretli -> boş
Tepede serin bir rüzgar esiyordu. Keloğlan bir kayanın yanında oturmuş dinleniyordu. Birden ağaçtan ince bir ses geldi. Keloğlan bu sesi çok merak etti. Hemen ağaca yürüdü. Çantası askısından bir dala asılıydı. Çantada ağzı açık bir su şişesi vardı. Keloğlan sesin şişeden gelip gelmediğini öğrenmek istedi. Şişedeki suyun hepsini yere döktü. Rüzgar yine esti ve boş şişeden bu kez kalın bir ses çıktı. Su gidince şişenin sesi değişmişti. Böylece Keloğlan sesin şişeden geldiğini buldu. Sonra Keloğlan şişeyle mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Keloğlan bu sesi çok merak etti"
   - Cümle 4: «Keloğlan bu sesi çok merak etti.»
   - Açıklama: Ortada gerçek bir sorun yok; yalnız bir merak var ve sorunun sebebi söylenmiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çantası askısından bir dala asılıydı"
   - Cümle 6: «Çantası askısından bir dala asılıydı.»
   - Açıklama: Keloğlan kayanın yanında otururken çantasının dalda asılı olması sebepsizce beliriyor ve çözümü getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0013` birebir aynı, `@degisim: işaretli -> boş` (tutuyorsan), ardından `@onarim: 6f4e9b5805f70f748994bc6c33f140b9d87493a5`, sonra gövde.

### Hikâye 3: tohum keloglan-0015 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0015
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'maske', fiil 'okumak', sıfat 'ekşi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: eşeğe verilecek elmalar çok ekşiydi | sepetlere bakıp tatlı elmalar buldu
@tohum: keloglan-0015
@degisim: okumak -> aramak
Bir sabah Keloğlan evin önünde eşeği Karakaçan için sürpriz hazırladı. Yüzünde komik bir maskeyle ona tatlı elmalar verecekti. Ama sepetteki elmalar yeşildi ve çok ekşiydi. Keloğlan dürüst ve azimli bir çocuktu, işini bırakmadı. Evdeki sepetlere tek tek bakıp tatlı elma aradı. Kapının yanındaki küçük sepette kırmızı elmalar buldu. Bir elmayı tattı ve elma çok tatlıydı. Keloğlan bu elmaları büyük bir tabağa dizdi. Sonra kağıttan yaptığı eşek maskesini yüzüne taktı. Islık çaldı ve Karakaçan hemen geldi. Eşek komik maskeyi görünce anırdı. Karakaçan elmaları bir bir yedi ve başını salladı. Sonra Keloğlan ile Karakaçan mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yüzünde komik bir maskeyle ona tatlı elmalar verecekti"
   - Cümle 2: «Yüzünde komik bir maskeyle ona tatlı elmalar verecekti.»
   - Açıklama: Maske sorunla ve çözümle hiç ilgisi olmayan, hikayeye sebepsiz eklenmiş bir ayrıntı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 4: «Keloğlan dürüst ve azimli bir çocuktu, işini bırakmadı.»
   - Açıklama: 'Dürüst' ve 'azimli' soyut kelimeler, olaya da bağlı değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu, işini bırakmadı"
   - Cümle 4: «Keloğlan dürüst ve azimli bir çocuktu, işini bırakmadı.»
   - Açıklama: 'Dürüst', 'azimli' ve 'işini bırakmadı' soyut ve deyimsel ifadeler, olaya bağlı somut bir ders değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0015` birebir aynı, `@degisim: okumak -> aramak` (tutuyorsan), ardından `@onarim: 160aefad461c0310b006d59524de8068275a0949`, sonra gövde.

### Hikâye 4: tohum keloglan-0016 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0016
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'testi', fiil 'oynamak', sıfat 'minik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: top ağacın dibinde dar bir deliğe düştü | arkadaşından yardım isteyip deliğe su döktü
@tohum: keloglan-0016
Ormanda büyük ağaçların altında Keloğlan ile Balkız top oynuyordu. Yanlarında içmek için su dolu bir testi vardı. Birden minik top yuvarlandı ve ağacın dibinde dar bir deliğe düştü. Keloğlan eğilip baktı, top deliğin dibindeydi. Keloğlan deliğe su dökmeyi düşündü, ama testi çok ağırdı. Keloğlan sakardı ve eşyalar sık sık elinden düşerdi. "Balkız, testiyi benimle tutar mısın?" diye sordu Keloğlan. Balkız testinin bir yanından tuttu. İkisi testiyi yavaşça deliğe eğdi. Minik top suyla yukarı çıktı ve Keloğlan onu aldı. Keloğlan çok sevindi, çünkü minik topunu geri almıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan sakardı ve eşyalar sık sık elinden düşerdi"
   - Cümle 6: «Keloğlan sakardı ve eşyalar sık sık elinden düşerdi.»
   - Açıklama: Sakarlık kartın güvenli özellik kullanımı satırındaki gibi bir şeyi düşürerek gösterilmiyor, yalnız söyleniyor ve sorunu doğurmuyor.
   - Açıklama: Tohumdaki sakarlık özelliği yalnız söyleniyor, hiçbir şey düşmüyor ve çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0016` birebir aynı, ardından `@onarim: 530f1c9a925db135198fe4821c861e05e5510c66`, sonra gövde.

### Hikâye 5: tohum keloglan-0018 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0018
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'vanilya', fiil 'küçülmek', sıfat 'sıkı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: üç kurabiyeyi ikisine bölmek zordu | evde bir kurabiye yediğini söyleyip ikisini annesine verdi
@tohum: keloglan-0018
@degisim: küçülmek -> bölmek
Keloğlan ile anası dağda bir kayanın üstüne oturdu. Anası çantasını açtı ve üç vanilyalı kurabiye çıkardı. Ama üç kurabiyeyi ikisine bölmek zordu, bir tane fazlaydı. "Sen iki tane ye, Keloğlan," dedi anası. Keloğlan dürüst bir çocuktu ve başını iki yana salladı. "Hayır, anneciğim, ben sabah evde bir kurabiye yedim," dedi Keloğlan. Sonra iki kurabiyeyi annesine verdi ve kendisi bir tane aldı. Böylece ikisi de iki kurabiye yedi. Anası gülümsedi ve Keloğlan'a sıkı sıkı sarıldı. "Çok teşekkürler, Keloğlan, seninle burada olmak çok güzel!" dedi anası.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "üç kurabiyeyi ikisine bölmek zordu"
   - Cümle 3: «Ama üç kurabiyeyi ikisine bölmek zordu, bir tane fazlaydı.»
   - Açıklama: 'İkisine bölmek' dilbilgisel değil; 'ikisi arasında paylaştırmak' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "üç kurabiyeyi ikisine bölmek zordu"
   - Cümle 3: «Ama üç kurabiyeyi ikisine bölmek zordu, bir tane fazlaydı.»
   - Açıklama: 'İkisine bölmek' yanlış; 'ikisi arasında paylaştırmak' olmalı.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "üç kurabiyeyi ikisine bölmek zordu"
   - Cümle 3: «Ama üç kurabiyeyi ikisine bölmek zordu, bir tane fazlaydı.»
   - Açıklama: Anası hemen bir çözüm önerdiği için bölüşme gerçek bir sorun değil ve sorun çocuğa zayıf, yapay geliyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ben sabah evde bir kurabiye yedim"
   - Cümle 6: «"Hayır, anneciğim, ben sabah evde bir kurabiye yedim," dedi Keloğlan.»
   - Açıklama: Kartın dürüstlük özelliği, annesine fazla kurabiye vermek için söylenmiş bir bahane gibi okunan sözle gösteriliyor; dürüstlük işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0018` birebir aynı, `@degisim: küçülmek -> bölmek` (tutuyorsan), ardından `@onarim: b0966bc942f6a453317aaed43719ab0561b5b77b`, sonra gövde.

### Hikâye 6: tohum keloglan-0019 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0019
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çember', fiil 'eğlenmek', sıfat 'uykulu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: odunları tutan eski ip koptu ve odunlar döküldü | odunları toplayıp çemberin içine dizdi
@tohum: keloglan-0019
Bir sabah Keloğlan ormanda tahta çemberini yuvarlayıp eğleniyordu. Uykulu eşeği Karakaçan da sırtında odunlarla yanında yürüyordu. Birden odunları tutan eski ip koptu ve odunlar yere döküldü. Karakaçan durdu ve üzgün üzgün başını eğdi. "Üzülme, Karakaçan, odunları ben toplarım," dedi Keloğlan. Karakaçan başını kaldırdı. Odunlar çoktu, ama dürüst ve azimli Keloğlan işini bırakmadı. Bütün odunları tek tek topladı. Sonra odunları çemberin içine sıkıca dizdi. Çember bütün odunları bir arada tuttu. Keloğlan yükü eşeğinin sırtına koydu. Karakaçan esnedi, başını salladı ve yavaşça yürüdü. Keloğlan bundan sonra yola çıkmadan önce ipleri hep kontrol etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama dürüst ve azimli Keloğlan"
   - Cümle 7: «Odunlar çoktu, ama dürüst ve azimli Keloğlan işini bırakmadı.»
   - Açıklama: 'Dürüst' kelimesi odun toplama eylemiyle ilgisiz, yanlış bağlamda kullanılmış.
   - Açıklama: Odun toplamakla ilgisi olmayan 'dürüst' kelimesi bu bağlamda doğru anlamda kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0019` birebir aynı, ardından `@onarim: 1cd5b30a330c841e675b807d4f4165011d148029`, sonra gövde.

### Hikâye 7: tohum keloglan-0022 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0022
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kese', fiil 'gıdıklamak', sıfat 'kıvrımlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: saklanan küçük kese bulunamadı | yardım isteyip uzun otların arasında keseyi buldu
@tohum: keloglan-0022
@degisim: gıdıklamak -> ayırmak
Ormanda büyük ağaçların altında kıvrımlı bir yol vardı. Keloğlan bu yolda hazine arama oyunu oynuyordu, ama hazineyi bulamıyordu. Bilgecan Dede hazine olarak yolun bir yanına küçük bir kese saklamıştı. Keloğlan biraz sakardı ve hep yanlış yana baktı. "Dede, bana biraz yardım eder misin?" diye sordu Keloğlan. "Hazine uzun otların arasında," dedi Bilgecan Dede. Keloğlan hemen uzun otlara doğru yürüdü. Otları eliyle ayırdı ve kahverengi keseyi gördü. Kesenin içinde üç tane ceviz vardı. "Gel, cevizleri birlikte yiyelim, Dede!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "biraz sakardı ve hep yanlış yana baktı"
   - Cümle 4: «Keloğlan biraz sakardı ve hep yanlış yana baktı.»
   - Açıklama: 'Sakar' beceriksiz demektir, yanlış yöne bakmakla anlamca uyuşmuyor.
   - Açıklama: 'Sakar' beceriksizlik demektir, yanlış yana bakmakla anlamca uyuşmuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "hep yanlış yana baktı"
   - Cümle 4: «Keloğlan biraz sakardı ve hep yanlış yana baktı.»
   - Açıklama: Kartın güvenli özellik kullanımı satırı sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterir; yanlış yana bakmak sakarlık değildir ve özellik işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve hep yanlış yana baktı"
   - Cümle 4: «Keloğlan biraz sakardı ve hep yanlış yana baktı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre sakarlık yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; burada yanlış yana bakmak olarak kullanılıyor ve çözüme katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0022` birebir aynı, `@degisim: gıdıklamak -> ayırmak` (tutuyorsan), ardından `@onarim: b09c721773a44ad17cc538d54e80887e5ca1b68a`, sonra gövde.

### Hikâye 8: tohum keloglan-0023 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Balkız
@tohum: keloglan-0023
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'alet', fiil 'oturtmak', sıfat 'eski'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | Balkız
@plan: masanın bir ayağı kısaydı ve masa sallandı | kısa ayağın altına küçük bir tahta koydu
@tohum: keloglan-0023
Evin mutfağında Keloğlan ile Balkız çorba oyunu oynuyordu. Keloğlan çorbayı yapacaktı ve Balkız'ı eski masaya oturttu. Ama masanın bir ayağı kısaydı ve masa sallanıyordu. "Böyle yemek yiyemem, Keloğlan," dedi Balkız gülerek. Keloğlan alet kutusunu getirdi, ama içinde tahta göremedi. Keloğlan biraz sakardı ve kutu elinden kayıp düştü. Aletler döküldü ve kutunun dibindeki küçük tahta göründü. Keloğlan tahtayı masanın kısa ayağının altına koydu. Masa artık hiç sallanmadı. "Buyur, sıcak çorban hazır," dedi Keloğlan. Balkız boş tabaktan çorba içer gibi yaptı ve güldü. Keloğlan bundan sonra oyuna başlamadan önce masanın ayaklarına bakardı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kutu elinden kayıp düştü"
   - Cümle 6: «Keloğlan biraz sakardı ve kutu elinden kayıp düştü.»
   - Açıklama: Tahta, figürün bir çabasıyla değil kutunun kazayla düşmesiyle tesadüfen ortaya çıkıyor; çözüm sebepsizce geliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kutunun dibindeki küçük tahta göründü"
   - Cümle 7: «Aletler döküldü ve kutunun dibindeki küçük tahta göründü.»
   - Açıklama: Çözüm Keloğlan'ın arayışıyla değil, kutunun kazara düşmesiyle sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0023` birebir aynı, ardından `@onarim: cbd9e247cad92efe784afabec65d446d7705dc45`, sonra gövde.

### Hikâye 9: tohum keloglan-0024 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0024
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'balkabağı', fiil 'incelemek', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kabak düştü ve çalıların arkasında kayboldu | yerdeki izi inceledi ve kabağı buldu
@tohum: keloglan-0024
@degisim: balkabağı -> kabak
Ormanda büyük ağaçların arasında dar bir yol vardı. Keloğlan elinde büyük bir kabakla bu yoldan eve dönüyordu. Keloğlan biraz sakardı, kabak elinden düştü ve çalıların arkasında kayboldu. Keloğlan çalıların arkasına baktı ama orada bir şey yoktu. Kabağın nereye gittiğini çok merak etti. Keloğlan yere eğildi ve yaprakları dikkatle inceledi. Yapraklarda uzun bir iz vardı. Keloğlan izin yanından yavaşça yürüdü. İz büyük bir ağacın dibinde bitti. Kabak orada duruyordu. Keloğlan kabağını bulduğu için çok memnundu. Kabağı aldı ve eve doğru mutlu mutlu yürüdü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı"
   - Cümle 3: «Keloğlan biraz sakardı, kabak elinden düştü ve çalıların arkasında kayboldu.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0024` birebir aynı, `@degisim: balkabağı -> kabak` (tutuyorsan), ardından `@onarim: 13102a995d6a236b365c7e06781aeefd62a991b0`, sonra gövde.

### Hikâye 10: tohum keloglan-0025 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0025
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yaprak', fiil 'heyecanlanmak', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: tepeden ıslık sesi geldi ama ıslık çalan yoktu | yere eğilince sesi yapan boş dalı buldu
@tohum: keloglan-0025
Keloğlan tepede güzel sarı yapraklar topluyordu. Birden rüzgar esti ve ince bir ıslık sesi duyuldu. Ama tepede ıslık çalan kimse yoktu. Keloğlan çok heyecanlandı ve bu sesi merak etti. Sesin geldiği yere doğru yürüdü. Otların arasına baktı ama bir şey göremedi. Keloğlan biraz sakardı ve eğilirken yapraklar elinden düştü. Yaprakları toplarken sesin yerden geldiğini duydu. Kuru otların altında küçük bir dal buldu. Dalın içi boştu ve ucunda bir delik vardı. Keloğlan deliği parmağıyla kapattı ve ıslık kesildi. Parmağını çekince ıslık yeniden başladı. Ses, dalın içinden geçen rüzgardan çıkıyordu. Keloğlan dalı rüzgara doğru tuttu ve ıslığı mutlu mutlu dinledi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi yapan boş dalı buldu"
   - Cümle 0 (plan satırı): «tepeden ıslık sesi geldi ama ıslık çalan yoktu | yere eğilince sesi yapan boş dalı buldu»
   - Açıklama: 'Boş dal' anlamsız; 'içi boş dal' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Otların arasına baktı ama bir şey göremedi"
   - Cümle 6: «Otların arasına baktı ama bir şey göremedi.»
   - Açıklama: Çözüm sebebe doğrudan yönelmiyor; arama, başarısız bakış ve tesadüf gibi ikiden fazla adıma yayılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "eğilirken yapraklar elinden düştü"
   - Cümle 7: «Keloğlan biraz sakardı ve eğilirken yapraklar elinden düştü.»
   - Açıklama: Dalın bulunması figürün çabasından değil, yaprakların tesadüfen düşmesinden çıkıyor; çözüm sebepsizce geliyor.
   - Açıklama: Çözüm Keloğlan'ın aramasından değil, yaprakların tesadüfen düşmesinden sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0025` birebir aynı, ardından `@onarim: 88209501079e264b28f2e1300570cca7f19f5c7f`, sonra gövde.

### Hikâye 11: tohum keloglan-0027 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0027
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'gümüş', fiil 'düzenlemek', sıfat 'sabırsız'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: sepet düştü ve çilekler otlara döküldü | özür diledi ve çilekleri toplayıp düzenledi
@tohum: keloglan-0027
@degisim: gümüş -> çilek
Keloğlan anasıyla ormanda çilek topluyordu. Keloğlan sabırsızdı ve dolu sepeti hızla kaptı. Ama biraz sakardı, sepet elinden kaydı ve çilekler otlara döküldü. Keloğlan anasına üzgün üzgün baktı. "Özür dilerim, anne, acele ettim," dedi Keloğlan. "Üzülme, gel birlikte toplayalım," dedi anası. Keloğlan çilekleri otların arasından tek tek topladı. Sonra onları sepette güzelce düzenledi. Bu kez sepeti iki eliyle sıkıca tuttu. Anası gülümsedi ve onun başını okşadı. "Teşekkürler, anneciğim, çilekleri birlikte yiyelim!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan sabırsızdı ve dolu sepeti hızla kaptı"
   - Cümle 2: «Keloğlan sabırsızdı ve dolu sepeti hızla kaptı.»
   - Açıklama: Tohumdaki özellik sakarlık; kartın özellikler alanında olmayan sabırsızlık ikinci bir özellik olarak ekleniyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan sabırsızdı ve dolu"
   - Cümle 2: «Keloğlan sabırsızdı ve dolu sepeti hızla kaptı.»
   - Açıklama: Tohumdaki özellik sakarlık; sabırsızlık kartın özellikler alanında olmayan ikinci bir özellik olarak ekleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama biraz sakardı"
   - Cümle 3: «Ama biraz sakardı, sepet elinden kaydı ve çilekler otlara döküldü.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0027` birebir aynı, `@degisim: gümüş -> çilek` (tutuyorsan), ardından `@onarim: 6e6cedbaaf8fd7b3b170a955a0e5bdabd31d9d3c`, sonra gövde.

### Hikâye 12: tohum keloglan-0029 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0029
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'fırça', fiil 'tamamlamak', sıfat 'sessiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: tek bir fırça vardı ve arkadaşının fırçası kırılmıştı | fırçayı paylaştı ve sırayla boyadılar
@tohum: keloglan-0029
Bir sabah Keloğlan ile Balkız sessiz ormanda bir ağacın resmini yapıyordu. Ama tek bir fırça vardı, çünkü Balkız'ın fırçası kırılmıştı. "Ben nasıl boyayacağım?" diye sordu Balkız üzgün üzgün. Keloğlan elindeki fırçaya baktı ve biraz düşündü. Keloğlan, Balkız'dan yaprak boyamayı öğrenmek istiyordu. "Fırçayı paylaşalım, önce sen boya," dedi Keloğlan. Balkız ağacın yapraklarını yeşile boyadı. Keloğlan onu dikkatle izledi. Sonra Balkız fırçayı Keloğlan'a verdi. Keloğlan ağacın dallarına küçük yapraklar boyadı. İkisi resmi sırayla boyadı ve tamamladı. Keloğlan ile Balkız resimlerine bakıp mutlu mutlu güldüler.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dallarına küçük yapraklar boyadı"
   - Cümle 10: «Keloğlan ağacın dallarına küçük yapraklar boyadı.»
   - Açıklama: Olmayan yapraklar boyanmaz; 'yapraklar çizdi' ya da 'yaptı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0029` birebir aynı, ardından `@onarim: b48447f4d670eea6d79c6eb05407b25204927ae4`, sonra gövde.
