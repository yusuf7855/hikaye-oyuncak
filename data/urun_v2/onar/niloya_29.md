# Editör görevi (onarım): Niloya, onarım partisi 29

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar29.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Niloya | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar29.txt --ad urun_v2`
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

## Kart: Niloya (kaynaklı, kapalı dünya)

- Ad: Niloya (okunuş: niloya; kesme eki okunuşa uyar)
- Kimlik: Niloya, nehir kenarındaki bir köyde ailesiyle yaşayan küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Niloya'nın merakı bakarak, sorarak ve bir büyüğe haber vererek gösterilir; nehre ya da dereye girmez, suya yalnız kıyıdan bakar; ağaca ya da yüksek yere tırmanmaz.
- Özellikler:
  - keşfet: Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever. (örnek biçimler: merak etti, merakla, keşfetti)
  - soru: Merak ettiği her şeyi sorar. (örnek biçimler: sordu, soruyu, sorular)
  - şarkı: Şarkı söylemeyi çok sever. (örnek biçimler: şarkı, şarkısını)
- Yerler:
  - orman: Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.
  - dağ: Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.
  - ev: Niloya'nın nehir kenarındaki köy evi ve bahçesi.
  - park: Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Murat: Niloya'nın ağabeyi; küçük kardeşi Niloya'yı çok sever. Tür: oğlan; konuşur; huy: Top oynamayı, koşturmayı ve fındık toplamayı sever.. Yüzey biçimleri: Murat, ağabey, ağabeyi, abi, abisi, abiciğim
  - Mete: Murat'ın en yakın arkadaşı; Niloya ile aynı yaştadır ve onun da arkadaşıdır. Tür: oğlan; konuşur; huy: Oyuncaklarını dağıtır, sonra aradığını bulamaz.. Yüzey biçimleri: Mete
  - Tospik: Niloya'nın kaplumbağası ve en yakın arkadaşı. Tür: kaplumbağa; konuşur; huy: Oyun oynamayı ve uyumayı sever; Niloya'ya yetişmekte zorlanır.. Yüzey biçimleri: Tospik, kaplumbağa, kaplumbağası
  - dedesi: Niloya'nın dedesi; herkese iyi öğütler verir. Tür: dede; konuşur. Yüzey biçimleri: dede, dedesi, dedeciğim, Dede
  - babaannesi: Niloya'nın babaannesi; yemek yapmayı ve fındık toplamayı sever. Tür: babaanne; konuşur. Yüzey biçimleri: babaanne, babaannesi, babaanneciğim, Babaanne, nine, ninesi
  - annesi: Niloya'nın annesi; yemek yapmayı, ekinleri ve yaylayı sever. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, anneciğim, Anne
- Dünya kuralları:
  - Niloya'nın ağabeyi Murat'tır. Mete Niloya'nın ağabeyi değildir; Murat'ın arkadaşıdır.
  - Tospik yavaştır; Niloya'ya yetişmekte zorlanır, hızla koşmaz.
  - Köy nehir kenarındadır; hikayede kimse nehre ya da dereye girmez, suya kıyıdan bakılır.
- Yasak adlar: Elif, Mine, Fatoş, Cem, Ayşecik, Sarıkanat, Miniş
- Yasak: Babası kartta yok; hikayeye girmez (kapalı dünya).
- İzinli dünya kelimeleri: köy, nehir, yayla, fındık, kaplumbağa, kekik

## Onarılacak hikâyeler

### Hikâye 1: tohum niloya-0014 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | annesi
@tohum: niloya-0014
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'gemi', fiil 'yırtılmak', sıfat 'şaşkın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | annesi
@plan: rüzgar esti ve kağıt yelken yırtıldı | kağıdı ikiye katlayıp yeni bir yelken yaptı
@tohum: niloya-0014
Yaylada serin bir rüzgar esiyordu. Niloya ile annesi bir dala kağıt takıp gemi oyunu oynuyordu. Ama rüzgar birden kuvvetli esti ve kağıt yelken yırtıldı. Niloya şaşkın bir yüzle yelkene baktı. "Anne, kağıt neden yırtıldı?" diye sordu Niloya. "Tek kat kağıt çok ince, kızım," dedi annesi. Niloya çantadan yeni bir kağıt çıkardı. Kağıdı ikiye katladı ve dala sıkıca taktı. Rüzgar yine esti ama kalın yelken sağlam kaldı. "Gemimiz yola devam ediyor!" dedi annesi ve güldü. Niloya bundan sonra yelkenleri hep iki kat kağıttan yaptı.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kağıdı ikiye katlayıp yeni bir yelken yaptı"
   - Cümle 0 (plan satırı): «rüzgar esti ve kağıt yelken yırtıldı | kağıdı ikiye katlayıp yeni bir yelken yaptı»
   - Açıklama: Plan yelkeni Niloya'nın yaptığını söylüyor ama gövdede kağıdı annesi katlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0014` birebir aynı, ardından `@onarim: a44f5c90df89a9141a2998ffabc8401d7ee86980`, sonra gövde.

### Hikâye 2: tohum niloya-0091 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0091
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'baharat', fiil 'ayırmak', sıfat 'sakar'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: sepet devrildi ve fındıklar yaprakların arasına karıştı | yaprakların altına merakla bakıp fındıkları ayırdı
@tohum: niloya-0091
@degisim: baharat -> fındık
Rüzgar ağaçların arasında hafifçe esiyordu. Niloya ile Mete ormanda yemek yapma oyunu oynuyordu. Ama sakar Mete sepete çarptı ve fındıklar kuru yaprakların arasına döküldü. "Oyun kekimiz ne olacak?" diye sordu Mete üzgün bir sesle. Niloya merakla eğildi ve yaprakları tek tek kaldırdı. Her yaprağın altında küçük bir fındık vardı. Niloya fındıkları yapraklardan ayırdı ve sepete koydu. Mete de sepeti iki eliyle sıkıca tuttu. Kısa sürede sepet yine doldu. İkisi fındıkları yere yuvarlak bir kek gibi dizdi. "Teşekkürler, Niloya, kekimiz yine hazır!" dedi Mete.
```

**Hakem bulguları (2):**

1. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "Ama sakar Mete sepete çarptı"
   - Cümle 3: «Ama sakar Mete sepete çarptı ve fındıklar kuru yaprakların arasına döküldü.»
   - Açıklama: Anlatıcı Mete'yi 'sakar' diye etiketliyor; bu karttaki huyla da örtüşmeyen küçümseyici bir niteleme.
   - Açıklama: Mete'ye anlatıcı tarafından 'sakar' diye olumsuz bir etiket yapıştırılıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "fındıklar kuru yaprakların arasına döküldü"
   - Cümle 3: «Ama sakar Mete sepete çarptı ve fındıklar kuru yaprakların arasına döküldü.»
   - Açıklama: Dökülen fındıkları toplayıp bitirmek önemsiz, topla-bitir türü bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0091` birebir aynı, `@degisim: baharat -> fındık` (tutuyorsan), ardından `@onarim: 4c4472580a15e2000e781dabe62263894291068f`, sonra gövde.

### Hikâye 3: tohum niloya-0092 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Tospik
@tohum: niloya-0092
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'raf', fiil 'heyecanlanmak', sıfat 'uyanık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | Tospik
@plan: kaplumbağa acıkmıştı ama tabak boştu | mutfaktaki rafa bakıp elma buldu ve verdi
@tohum: niloya-0092
Mutfaktan tık tık diye bir ses geliyordu. Niloya mutfağa gitti ve Tospik'i boş bir tabağın yanında gördü. Tospik uyanıktı ve çok acıkmıştı, ama tabak boştu. "Karnım çok aç, Niloya," dedi Tospik. Niloya mutfaktaki alçak rafa merakla baktı. Rafta küçük bir kasenin içinde elma dilimleri vardı. Niloya elmaları görünce çok heyecanlandı. Kaseyi aldı ve elmaları tabağa koydu. Tospik yavaş yavaş yemeye başladı. Biraz sonra tabakta hiç elma kalmadı. Tospik başını kaldırdı ve Niloya'ya baktı. "Teşekkürler, Niloya, karnım artık tok!" dedi Tospik.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Mutfaktan tık tık diye bir ses geliyordu"
   - Cümle 1: «Mutfaktan tık tık diye bir ses geliyordu.»
   - Açıklama: Tık tık sesi olayı başlatıyor ama sesin neden geldiği hiç söylenmiyor ve bir daha kullanılmıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ama tabak boştu"
   - Cümle 3: «Tospik uyanıktı ve çok acıkmıştı, ama tabak boştu.»
   - Açıklama: Tabağın boş olduğu bir önceki cümlede söylendi; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0092` birebir aynı, ardından `@onarim: 367dff8bd242dcc122f59463853110330c98be71`, sonra gövde.

### Hikâye 4: tohum niloya-0094 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0094
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'sayfa', fiil 'sıkışmak', sıfat 'konuşkan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: ikisi aynı anda şarkı söyledi ve sesler karıştı | her sayfayı sırayla söylemeyi önerdi
@tohum: niloya-0094
@degisim: sıkışmak -> dinlemek
Bir sabah Niloya ile dedesi ormanda fındık ağaçlarının altına oturdu. Dedesinin elinde resimli bir şarkı kitabı vardı. İkisi de ilk şarkıyı söylemek istedi ve aynı anda başladı. Sesler birbirine karıştı ve şarkılar hiç güzel olmadı. Konuşkan dedesi hemen güldü. Niloya biraz düşündü. "Dede, sırayla söyleyelim, bir sayfa ben, bir sayfa sen," dedi Niloya. Niloya ilk sayfayı neşeyle söyledi. Dedesi onu sessizce dinledi. Sonra dedesi ikinci sayfayı söyledi. Bu kez iki şarkı da çok güzel oldu. Niloya bundan sonra şarkıları dedesiyle hep sırayla söyledi.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "her sayfayı sırayla söylemeyi"
   - Cümle 0 (plan satırı): «ikisi aynı anda şarkı söyledi ve sesler karıştı | her sayfayı sırayla söylemeyi önerdi»
   - Açıklama: Sayfa söylenmez; şarkı ya da sayfadaki şarkı söylenir.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Konuşkan dedesi hemen güldü"
   - Cümle 5: «Konuşkan dedesi hemen güldü.»
   - Açıklama: Kartın dede yanındaki ilişki alanı dedeyi iyi öğütler veren biri olarak tanımlıyor; 'konuşkan' huyu kartta yok.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Konuşkan dedesi hemen güldü"
   - Cümle 5: «Konuşkan dedesi hemen güldü.»
   - Açıklama: Dedeye kartın 'yanlar' alanında olmayan 'konuşkan' huyu eklenmiş; kart onu iyi öğütler veren biri olarak tanımlıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Konuşkan dedesi hemen güldü"
   - Cümle 5: «Konuşkan dedesi hemen güldü.»
   - Açıklama: Dedenin konuşkanlığı ve gülmesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya ilk sayfayı neşeyle söyledi"
   - Cümle 8: «Niloya ilk sayfayı neşeyle söyledi.»
   - Açıklama: Sayfa söylenmez, şarkı söylenir; fiil nesnesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0094` birebir aynı, `@degisim: sıkışmak -> dinlemek` (tutuyorsan), ardından `@onarim: bffe03918253dc656b13a92579cd4a29d477bcd5`, sonra gövde.

### Hikâye 5: tohum niloya-0095 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0095
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'anahtar', fiil 'işaretlemek', sıfat 'havalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: rüzgar bulutları hızla değiştirdi | en yavaş bulutu bulup şekilleri işaretledi
@tohum: niloya-0095
@degisim: havalı -> beyaz
Rüzgar bahçede hafifçe esiyordu. Niloya kağıdına bir kalp, bir anahtar ve bir ev çizmişti. Bu şekilleri bulutlarda arıyordu, ama rüzgar beyaz bulutları hızla değiştiriyordu. Niloya bir soru düşündü: En yavaş bulut hangisiydi? Sonra bütün bulutlara tek tek baktı. Nehrin üstündeki büyük bulut çok yavaş gidiyordu. Niloya yalnız bu buluta baktı ve bekledi. Bulutun ucu önce bir kalbe benzedi. Niloya kağıttaki kalbi kalemiyle işaretledi. Sonra bulut bir anahtar, en son da küçük bir ev gibi oldu. Niloya onları da kağıtta işaretledi. Niloya çok sevindi, çünkü üç şekli de bulutlarda görmüştü.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Rüzgar bahçede hafifçe esiyordu"
   - Cümle 1: «Rüzgar bahçede hafifçe esiyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede ve nehir kenarında geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya bir soru düşündü"
   - Cümle 4: «Niloya bir soru düşündü: En yavaş bulut hangisiydi?»
   - Açıklama: 'Soru düşünmek' doğal bir kullanım değil; 'Niloya düşündü' olmalı.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Nehrin üstündeki büyük bulut çok yavaş gidiyordu"
   - Cümle 6: «Nehrin üstündeki büyük bulut çok yavaş gidiyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede ve nehir kenarında geçiyor gibi.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bulutun ucu önce bir kalbe benzedi"
   - Cümle 8: «Bulutun ucu önce bir kalbe benzedi.»
   - Açıklama: Tek bir bulutun sırayla tam aranan üç şekle dönüşmesi çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0095` birebir aynı, `@degisim: havalı -> beyaz` (tutuyorsan), ardından `@onarim: c16cb226765d7f17ad7cdc1746e47b33c76866d6`, sonra gövde.

### Hikâye 6: tohum niloya-0097 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0097
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'battaniye', fiil 'güldürmek', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: şarkı çok uzundu ve sözler unutuldu | sözlerin yerine ormandaki şeyleri söyledi
@tohum: niloya-0097
Niloya ormanda yere büyük bir battaniye serdi. Battaniye onun sahnesiydi ve Niloya eğlenceli bir şarkı oyunu oynuyordu. Ama şarkı çok uzundu ve Niloya ortasında sözleri unuttu. Oyunu bitsin istemedi ve biraz düşündü. Sonra sözlerin yerine ormandaki şeyleri söylemeye başladı. Fındıkları, yaprakları ve ağaçları şarkıya kattı. Bir fındık yere düştü ve Niloya onu da şarkıya ekledi. Bu yeni şarkı Niloya'yı çok güldürdü. Sonra şarkıyı sonuna kadar söyledi. Sonra battaniyeye oturdu ve güldü. Niloya bundan sonra sözleri unutunca ormandaki şeylerle yeni sözler buldu.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra battaniyeye oturdu"
   - Cümle 10: «Sonra battaniyeye oturdu ve güldü.»
   - Açıklama: Art arda iki cümle 'Sonra' ile başlıyor ve 'güldü' tekrar ediliyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra battaniyeye oturdu ve güldü"
   - Cümle 10: «Sonra battaniyeye oturdu ve güldü.»
   - Açıklama: Art arda iki cümle 'Sonra' ile başlıyor ve 'güldürdü/güldü' gereksiz tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0097` birebir aynı, ardından `@onarim: 9a45e6c71e519bb731bc00d3a3b666f145a78716`, sonra gövde.

### Hikâye 7: tohum niloya-0098 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0098
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'çeşme', fiil 'guruldamak', sıfat 'yalnız'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: tek bir top vardı ve ikisi de istedi | şarkı bitene kadar sırayla oynamayı önerdi
@tohum: niloya-0098
@degisim: çeşme -> top
Niloya ile Murat ormanda fındık ağaçlarının arasında oynuyordu. Yanlarında yalnız bir top vardı. İkisi de topu ilk atmak istedi ve oyun durdu. Niloya biraz düşündü. "Murat, bir şarkı boyunca sen oyna, sonra ben," dedi Niloya. "Olur, önce sen söyle," dedi Murat. Murat topu aldı ve Niloya kısa bir şarkı söyledi. Şarkı bitince Murat topu Niloya'ya verdi. Sonra Murat şarkı söyledi ve Niloya topu attı. Birden Murat'ın karnı guruldadı ve ikisi de güldü. İkisi fındık ağacının altında birkaç fındık yedi. Sonra sırayla top oynamaya mutlu mutlu devam ettiler.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden Murat'ın karnı guruldadı ve ikisi de güldü"
   - Cümle 10: «Birden Murat'ın karnı guruldadı ve ikisi de güldü.»
   - Açıklama: Sorun çözüldükten sonra karın guruldaması ve fındık yeme sebepsiz ekleniyor ve olaya hizmet etmiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden Murat'ın karnı guruldadı"
   - Cümle 10: «Birden Murat'ın karnı guruldadı ve ikisi de güldü.»
   - Açıklama: Karın guruldaması ve fındık yeme sorunla ve çözümle ilgisi olmayan işlevsiz bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0098` birebir aynı, `@degisim: çeşme -> top` (tutuyorsan), ardından `@onarim: 61c4f5569b1f99f687c691a455ccff785c7dd5ee`, sonra gövde.

### Hikâye 8: tohum niloya-0100 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0100
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'boru', fiil 'yıkanmak', sıfat 'kırık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: dalın kırık yerinden ses kaçtı ve şarkı zayıf çıktı | kırık yeri parmağıyla kapatıp yeniden söyledi
@tohum: niloya-0100
Yağmur yeni dinmişti ve kekikler yağmurda yıkanmıştı. Niloya kekiklerin arasında boru gibi içi boş bir dal buldu. İçine ilk kez şarkı söyledi, ama ses dalın kırık yerinden kaçtı. Niloya dalı çevirdi ve küçük deliği gördü. Deliği parmağıyla sıkıca kapattı. Sonra en sevdiği şarkıyı yeniden borunun içine söyledi. Bu kez ses yüksek ve çok komik çıktı. Şarkı tepelerde uzaklara kadar gitti. Niloya güldü ve şarkısını bir kez daha söyledi. Niloya çok mutlu oldu, çünkü yeni boru şarkısı çok güzel çıkmıştı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve şarkı zayıf çıktı"
   - Cümle 0 (plan satırı): «dalın kırık yerinden ses kaçtı ve şarkı zayıf çıktı | kırık yeri parmağıyla kapatıp yeniden söyledi»
   - Açıklama: 'Şarkı zayıf çıktı' ifadesinde kelime yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kekikler yağmurda yıkanmıştı"
   - Cümle 1: «Yağmur yeni dinmişti ve kekikler yağmurda yıkanmıştı.»
   - Açıklama: Kekiklerin yıkanması mecazdır; küçük çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ses dalın kırık yerinden kaçtı"
   - Cümle 3: «İçine ilk kez şarkı söyledi, ama ses dalın kırık yerinden kaçtı.»
   - Açıklama: Sesin kaçması mecazlı bir anlatım.
   - Açıklama: Sesin kaçması mecazlı bir anlatım, küçük çocuğa uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şarkı tepelerde uzaklara kadar gitti"
   - Cümle 8: «Şarkı tepelerde uzaklara kadar gitti.»
   - Açıklama: Şarkının gitmesi mecazdır.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yeni boru şarkısı çok güzel"
   - Cümle 10: «Niloya çok mutlu oldu, çünkü yeni boru şarkısı çok güzel çıkmıştı.»
   - Açıklama: 'Boru şarkısı' anlamsız bir tamlama; dal ile söylenen şarkıyı doğru anlatmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0100` birebir aynı, ardından `@onarim: 2d37c0aca2aced4c386594810e6c07babe1b445e`, sonra gövde.

### Hikâye 9: tohum niloya-0101 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0101
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'tereyağı', fiil 'gizlenmek', sıfat 'kocaman'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: rüzgar esince kule yıkıldı çünkü taşlar yuvarlaktı | etrafa merakla bakıp düz taşlar buldu
@tohum: niloya-0101
@degisim: tereyağı -> taş
Yaylada serin bir rüzgar esiyordu. Niloya yeşil tepede taşlardan kocaman bir kule yapmak istiyordu. Ama rüzgar esince kule hemen yıkıldı, çünkü taşlar çok yuvarlaktı. Yuvarlak taşlar çimlerin üstünde zıplaya zıplaya gitti. Niloya buna çok güldü. Sonra düz taşlar bulmak için etrafa merakla baktı. Kekiklerin arasında birkaç düz taş gizlenmişti. Niloya onları tek tek topladı. Sonra taşları üst üste dikkatle dizdi. Rüzgar yine esti, ama kule bu kez yıkılmadı. Kule Niloya'nın dizine kadar yükseldi. Niloya çok sevindi, çünkü düz taşlarla sağlam bir kule yapmıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "birkaç düz taş gizlenmişti"
   - Cümle 7: «Kekiklerin arasında birkaç düz taş gizlenmişti.»
   - Açıklama: Taşlar kendiliğinden gizlenmez; fiil öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kekiklerin arasında birkaç"
   - Cümle 7: «Kekiklerin arasında birkaç düz taş gizlenmişti.»
   - Açıklama: 'Kekik' 3 yaşındaki bir çocuğun bileceği bir kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0101` birebir aynı, `@degisim: tereyağı -> taş` (tutuyorsan), ardından `@onarim: 4efbc14e94b30345187ade583dd80e0a7ab0e2d8`, sonra gövde.

### Hikâye 10: tohum niloya-0103 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0103
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Tospik
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'atkı', fiil 'takılmak', sıfat 'dalgalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: rüzgar atkıyı uçurdu ve atkı bir çalıya takıldı | kaplumbağasından yardım istedi ve atkıyı birlikte kurtardılar
@tohum: niloya-0103
Tepede serin bir rüzgar esiyordu. Niloya ile Tospik orada kekik topluyordu. Birden rüzgar Niloya'nın atkısını uçurdu ve atkı bir çalıya takıldı. Niloya dalgalı çizgili atkısını çok seviyordu. Atkının ucu çalının en alt dalına dolanmıştı. Niloya çalının altına sığmıyordu. Niloya, Tospik'ten yardım istedi. Ona çalının altına girebilir mi diye sordu. Tospik başını salladı ve yavaşça çalının altına girdi. Sonra atkıyı daldan itti. Niloya atkıyı dikkatle çekti ve atkı daldan kurtuldu. Niloya atkısını boynuna sardı ve Tospik'e sarıldı. Niloya çok sevindi, çünkü Tospik'ten yardım istemişti ve atkısı kurtulmuştu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Ona çalının altına girebilir mi diye sordu"
   - Cümle 8: «Ona çalının altına girebilir mi diye sordu.»
   - Açıklama: Dolaylı soru tırnaksız ve bozuk kurulmuş; 'girip giremeyeceğini sordu' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çalının altına girebilir mi diye sordu"
   - Cümle 8: «Ona çalının altına girebilir mi diye sordu.»
   - Açıklama: Tohumdaki soru özelliği kartta merakla soru sormak iken burada yalnız yardım isteği olarak kullanılıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çünkü Tospik'ten yardım istemişti"
   - Cümle 13: «Niloya çok sevindi, çünkü Tospik'ten yardım istemişti ve atkısı kurtulmuştu.»
   - Açıklama: Son cümle yardım isteme ve atkının kurtulmasını gereksiz yere yeniden anlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0103` birebir aynı, ardından `@onarim: 26c71de517f5fd74bb5c7d806658f208eaac5a2e`, sonra gövde.

### Hikâye 11: tohum niloya-0104 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0104
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babaannesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'zarf', fiil 'kaydetmek', sıfat 'sıcak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: babaanne resim olan zarfını düşürdü ve bulamadı | zarfı en son nerede gördüğünü sordu ve orada buldu
@tohum: niloya-0104
@degisim: kaydetmek -> düşürmek
Bir sabah Niloya ile babaannesi ormanda fındık topluyordu. Birden babaannesi cebine baktı ve üzüldü. Cebindeki zarfı bir yere düşürmüştü. Zarfın içinde Niloya'nın ona çizdiği bir resim vardı. Babaannesi bu resmi hep yanında taşırdı. "Babaanne, zarfı en son nerede gördün?" diye sordu Niloya. Babaannesi biraz düşündü. "Sıcaktan yorulunca büyük fındık ağacının altında oturmuştum," dedi babaannesi. Niloya hemen o ağacın altına koştu. Yaprakların arasında beyaz zarfı buldu. Zarfı babaannesine verdi. Babaannesi zarfı açtı ve resme bakıp gülümsedi. "Teşekkürler, Niloya, en sevdiğim resmi buldun!" dedi babaannesi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "babaanne resim olan zarfını"
   - Cümle 0 (plan satırı): «babaanne resim olan zarfını düşürdü ve bulamadı | zarfı en son nerede gördüğünü sordu ve orada buldu»
   - Açıklama: Tamlama eksik; 'içinde resim olan zarfını' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0104` birebir aynı, `@degisim: kaydetmek -> düşürmek` (tutuyorsan), ardından `@onarim: 2d556ef7072192d4e20ebeec053eb6aa02bfa407`, sonra gövde.

### Hikâye 12: tohum niloya-0106 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0106
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'yumurta', fiil 'solmak', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: yolda bir taş vardı ve yumurta çimlere yuvarlandı | merakla bakıp yumurtayı yaprakların arasında buldu
@tohum: niloya-0106
Bir sabah Niloya bahçede eğlenceli bir oyun oynuyordu. Kaşığın üstünde haşlanmış bir yumurta taşıyordu. Ama yolda bir taş vardı ve yumurta düşüp çimlere yuvarlandı. Niloya yumurtayı göremedi. Önce merakla çalıların altına baktı ama orada bir şey yoktu. Sonra bahçenin ucundaki solmuş yaprakların arasına baktı. Yumurta yaprakların içinde duruyordu. Niloya yumurtayı aldı ve yeniden kaşığa koydu. Bu kez taşın yanından düzenli adımlarla, yavaşça geçti. Yumurta hiç düşmedi. Niloya sonunda kapıya vardı ve ellerini çırptı. Niloya çok mutluydu, çünkü hem yumurtayı bulmuş hem de oyunu bitirmişti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Niloya bahçede eğlenceli bir oyun"
   - Cümle 1: «Bir sabah Niloya bahçede eğlenceli bir oyun oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "taşın yanından düzenli adımlarla"
   - Cümle 9: «Bu kez taşın yanından düzenli adımlarla, yavaşça geçti.»
   - Açıklama: 'Düzenli' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Düzenli adımlarla' 3 yaşındaki çocuğun bilmeyeceği soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0106` birebir aynı, ardından `@onarim: d2d14f640c4f365a248ef9c59e5b57771a8b5826`, sonra gövde.
