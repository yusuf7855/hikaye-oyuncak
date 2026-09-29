# Editör görevi (onarım): Niloya, onarım partisi 7

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar7.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar7.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0002 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Tospik
@tohum: niloya-0002
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'düğüm', fiil 'satmak', sıfat 'limonlu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | Tospik
@plan: çiçek açıyordu ama kaplumbağası uyuyordu | yanına oturup şarkı söyledi ve onu uyandırdı
@tohum: niloya-0002
@degisim: düğüm -> çiçek
Parkta Niloya kaydırağın yanında sarı bir çiçek gördü. Çiçek güneşte yavaş yavaş açılıyordu. Niloya bunu Tospik'e göstermek istedi ama Tospik uyuyordu. Tospik limonlu kek satma oyunu oynamıştı ve çok yorulmuştu. Niloya onun yanına oturdu ve neşeli bir şarkı söyledi. Tospik şarkıyı duyunca gözlerini açtı. Başını kabuğundan çıkardı ve çiçeğe baktı. Çiçek daha tam açık değildi. İkisi yan yana oturdu ve bekledi. Sonra sarı yapraklar bir bir açıldı. Tospik gülümsedi ve çiçeği kokladı. Niloya çok sevindi, çünkü çiçek açarken Tospik de yanındaydı.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Tospik limonlu kek satma oyunu oynamıştı"
   - Cümle 4: «Tospik limonlu kek satma oyunu oynamıştı ve çok yorulmuştu.»
   - Açıklama: Limonlu kek satma oyunu kartın kapalı dünyasında olmayan, başka diziden gelen bir öğe gibi duruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0002` birebir aynı, `@degisim: düğüm -> çiçek` (tutuyorsan), ardından `@onarim: 5df580b18b90263512bb6bfd1199faedb3190ff6`, sonra gövde.

### Hikâye 2: tohum niloya-0005 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | park | annesi
@tohum: niloya-0005
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: paylaşmak
- yan: annesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'fiyonk', fiil 'kilitlemek', sıfat 'somurtkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | annesi
@plan: rüzgar esti ve annesinin saçı yüzüne döküldü | bir fiyonk verip annesinin saçını bağladı
@tohum: niloya-0005
@degisim: kilitlemek -> bağlamak
Niloya parkta salıncakta sallanıyor, annesi de onu itiyordu. Birden rüzgar esti ve annesinin saçları yüzüne döküldü. Annesinin yanında toka yoktu. Annesi somurtkan bir yüzle saçlarını tuttu. Niloya salıncaktan indi. Saçında iki pembe fiyonk vardı. "Anne, bir fiyonk da senin olsun," dedi Niloya. Hemen bir fiyonk çözdü. Sonra annesine neşeli bir şarkı söyledi. Annesi şarkıyı dinlerken kıpırdamadan durdu ve gülümsedi. Niloya da onun saçlarını arkadan bağladı. "Teşekkürler, Niloya, fiyonk bana çok yakıştı!" dedi annesi. Sonra annesi Niloya'yı yine salıncakta sallamaya başladı. Niloya bundan sonra bir fiyonk fazla olunca onu annesiyle paylaştı.
```

**Hakem bulguları (8):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "annesinin saçları yüzüne döküldü"
   - Cümle 2: «Birden rüzgar esti ve annesinin saçları yüzüne döküldü.»
   - Açıklama: Dizide Niloya'nın annesi başörtülüdür; saçlarının açıkta uçuşması diziyi izleyen çocuğun tanıdığı görünüşe aykırı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "annesinin saçları yüzüne döküldü"
   - Cümle 2: «Birden rüzgar esti ve annesinin saçları yüzüne döküldü.»
   - Açıklama: Saçın rüzgarla yüze dökülmesi çocuğun önemseyeceği bir sorun olmaktan uzak, önemsiz bir olay.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Annesi somurtkan bir yüzle"
   - Cümle 4: «Annesi somurtkan bir yüzle saçlarını tuttu.»
   - Açıklama: 'Somurtkan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Somurtkan' 3 yaşındaki bir çocuğun bilmediği bir kelime.
4. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Annesi somurtkan bir yüzle saçlarını tuttu"
   - Cümle 4: «Annesi somurtkan bir yüzle saçlarını tuttu.»
   - Açıklama: Kartta annesinin huyu yemek, ekinler ve yaylayı sevmektir; somurtkan anne dizideki karaktere uymuyor.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Hemen bir fiyonk çözdü."
   - Cümle 8: «Hemen bir fiyonk çözdü.»
   - Açıklama: Son özne anne olduğundan fiyonku kimin çözdüğü belli değil.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra annesine neşeli bir şarkı söyledi"
   - Cümle 9: «Sonra annesine neşeli bir şarkı söyledi.»
   - Açıklama: Şarkı çözüme hiçbir katkı yapmadan araya sokulmuş işlevsiz bir ayrıntı.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bir fiyonk fazla olunca onu annesiyle paylaştı"
   - Cümle 14: «Niloya bundan sonra bir fiyonk fazla olunca onu annesiyle paylaştı.»
   - Açıklama: Cümle kuruluşu bozuk; alışkanlık anlatımı için 'fazla olunca onu annesiyle paylaşırdı' gibi olmalı.
   - Açıklama: Cümle bozuk kurulmuş; 'fazla fiyonku olunca' gibi bir yapı gerekir.
8. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Niloya bundan sonra bir fiyonk fazla olunca onu annesiyle paylaştı"
   - Cümle 14: «Niloya bundan sonra bir fiyonk fazla olunca onu annesiyle paylaştı.»
   - Açıklama: 'Bundan sonra' ile tekil geçmiş 'paylaştı' uyumsuz ve cümle bozuk kurulmuş; alışkanlık için 'paylaşırdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0005` birebir aynı, `@degisim: kilitlemek -> bağlamak` (tutuyorsan), ardından `@onarim: 0a14c3e5f3f1dd1b55b2c7a125bbbf246d8d6d36`, sonra gövde.

### Hikâye 3: tohum niloya-0009 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | babaannesi
@tohum: niloya-0009
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: sırayla oynamak
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'silgi', fiil 'yemek', sıfat 'turuncu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | babaannesi
@plan: ikisi de güneşi boyamak istedi ama tek kalem vardı | şarkı bitince kalemi sırayla kullandılar
@tohum: niloya-0009
@degisim: yemek -> çizmek
Niloya ile babaannesi parkta bir kağıda resim çiziyordu. İkisi de kağıttaki güneşi boyamak istiyordu. Ama yanlarında ucunda silgi olan tek bir turuncu kalem vardı. Niloya biraz düşündü. "Babaanne, sırayla boyayalım," dedi Niloya. "Şarkım bitince kalem sende olsun." Sonra neşeli bir şarkı söyledi ve güneşin yarısını boyadı. Acele edince boya biraz güneşin dışına taştı. Şarkı bitince kalemi babaannesine verdi. Babaannesi önce silgiyle taşan yeri sildi. Sonra güneşin öbür yarısını turuncuya boyadı. Resim bitti. "Sırayla yapınca ne güzel oldu!" dedi babaannesi. Niloya bundan sonra kalem tek olunca onu babaannesiyle sırayla kullandı.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Niloya biraz düşündü.»
   - Açıklama: Tek kalem olduğu, yani asıl sorun, ancak 4. cümlede söyleniyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Acele edince boya biraz güneşin dışına taştı"
   - Cümle 8: «Acele edince boya biraz güneşin dışına taştı.»
   - Açıklama: Kalem sorununun yanına boyanın taşması diye ikinci bir sorun ekleniyor.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "boya biraz güneşin dışına taştı"
   - Cümle 8: «Acele edince boya biraz güneşin dışına taştı.»
   - Açıklama: Kalem paylaşma sorununun yanına boyanın taşması diye ikinci bir sorun ekleniyor ve onu babaanne çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0009` birebir aynı, `@degisim: yemek -> çizmek` (tutuyorsan), ardından `@onarim: 74cbeaacfb06db8e96cafe7b7fdda659d10a72eb`, sonra gövde.

### Hikâye 4: tohum niloya-0010 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0010
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'önlük', fiil 'savurmak', sıfat 'ferah'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: dedesinin ağacında hiç fındık yoktu | şarkı söyleyip dedesini çağırdı ve fındıklarını paylaştı
@tohum: niloya-0010
@degisim: ferah -> serin
Rüzgar esiyordu ve orman çok serindi. Niloya ile dedesi ormanda fındık topluyordu. Niloya'nın ağacı fındıkla doluydu ama dedesinin ağacında hiç fındık yoktu. Rüzgar dalları savurdu ve Niloya'nın önüne bir sürü fındık düştü. Niloya önlüğünün cebini fındıkla doldurdu. Dedesi ise biraz uzakta, boş elle ağaçlara bakıyordu. Niloya dedesini çağırmak için neşeli bir şarkı söyledi. Dedesi şarkıyı duyunca gülümsedi ve yanına geldi. "Dede, bu fındıkların yarısı senin," dedi Niloya. Sonra fındıkların yarısını dedesine verdi. "Teşekkürler, Niloya, bunları birlikte yiyelim," dedi dedesi. Niloya çok sevindi, çünkü artık ikisinin de fındığı vardı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "dedesinin ağacında hiç fındık yoktu"
   - Cümle 3: «Niloya'nın ağacı fındıkla doluydu ama dedesinin ağacında hiç fındık yoktu.»
   - Açıklama: Dedenin ağacında neden fındık olmadığı söylenmiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rüzgar dalları savurdu ve Niloya'nın önüne"
   - Cümle 4: «Rüzgar dalları savurdu ve Niloya'nın önüne bir sürü fındık düştü.»
   - Açıklama: Niloya'nın ağacı zaten fındıkla doluyken rüzgarın fındık düşürmesi sebepsiz ve gereksiz bir tesadüf.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Rüzgar dalları savurdu ve Niloya'nın önüne bir sürü fındık düştü"
   - Cümle 4: «Rüzgar dalları savurdu ve Niloya'nın önüne bir sürü fındık düştü.»
   - Açıklama: Fındıklar sebepsizce rüzgarla önüne düşüyor; ağacı zaten dolu olan Niloya için bu olay çözümü kolaylaştıran işlevsiz bir rastlantı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0010` birebir aynı, `@degisim: ferah -> serin` (tutuyorsan), ardından `@onarim: 922b016b156ab767c0f1c4801ef50428abb31962`, sonra gövde.

### Hikâye 5: tohum niloya-0012 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Tospik
@tohum: niloya-0012
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'giysi', fiil 'beğenmek', sıfat 'ılık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | ev | Tospik
@plan: kaplumbağası uyumak istedi ama toprak çok serindi | bahçede ılık bir taş bulup üstüne giysi serdi
@tohum: niloya-0012
Evin bahçesinde serin bir rüzgar esiyordu. Niloya'nın kaplumbağası Tospik uyumak istiyordu ama toprak çok serindi. "Niloya, bana sıcak bir yer bulur musun?" diye sordu Tospik. Niloya merakla bahçeyi dolaştı ve her yere baktı. Evin yanında güneş alan düz bir taş buldu. Taşa elini koydu, taş eline ılık geldi. Niloya eski ve yumuşak bir giysi getirdi ve taşın üstüne serdi. Tospik yavaş yavaş yürüdü ve giysinin üstüne çıktı. "Burayı çok beğendim, teşekkürler, Niloya!" dedi Tospik. Tospik orada rahatça uyudu, Niloya da onun yanında oturup gülümsedi.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "bahçede ılık bir taş bulup üstüne giysi serdi"
   - Cümle 0 (plan satırı): «kaplumbağası uyumak istedi ama toprak çok serindi | bahçede ılık bir taş bulup üstüne giysi serdi»
   - Açıklama: Planda giysiyi Niloya seriyor ama gövdede giysiyi Tospik getirip seriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0012` birebir aynı, ardından `@onarim: 99366d53d7015d9af0efc211529872a54bfa0628`, sonra gövde.

### Hikâye 6: tohum niloya-0013 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0013
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'pedal', fiil 'doğmak', sıfat 'dikkatli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: yapraklı taç çok büyüktü ve gözlerine kaydı | dalın uçlarını üst üste getirip tacı küçülttü
@tohum: niloya-0013
@degisim: pedal -> dal
Niloya ormandaydı ve güneş yeni doğuyordu. Niloya ince bir dala yapraklar takıp bir taç yaptı. Ama taç çok büyüktü ve başından gözlerine kaydı. Niloya tacı çıkardı ve ona uzun uzun baktı. Sonra bir soru düşündü: Dal çok mu uzundu? Dalı başının çevresine tuttu ve gerçekten çok uzun olduğunu gördü. Niloya dalın iki ucunu biraz daha üst üste getirdi. Dalı kırmamak için çok dikkatli davrandı. Uçları sıkıca birbirine sardı. Taç bu kez tam başına oturdu. Niloya yapraklı tacıyla ormanda neşeyle dolaştı. Niloya bundan sonra taç yaparken önce dalı başına göre ölçtü.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sonra bir soru düşündü"
   - Cümle 5: «Sonra bir soru düşündü: Dal çok mu uzundu?»
   - Açıklama: 'Bir soru düşündü' doğal olmayan bir kullanım.
   - Açıklama: 'Bir soru düşünmek' doğal değil; 'aklına bir soru geldi' olmalı.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Niloya bundan sonra taç yaparken önce dalı başına göre ölçtü"
   - Cümle 12: «Niloya bundan sonra taç yaparken önce dalı başına göre ölçtü.»
   - Açıklama: 'Bundan sonra' ile sürekli alışkanlık anlatılırken -dı'lı geçmiş zaman uymuyor; 'ölçtü' yerine 'ölçerdi' gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0013` birebir aynı, `@degisim: pedal -> dal` (tutuyorsan), ardından `@onarim: 9b12d7606a05a3a37f3ad2fa199aa8667aeed88d`, sonra gövde.

### Hikâye 7: tohum niloya-0015 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | Mete
@tohum: niloya-0015
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'leke', fiil 'katmak', sıfat 'kalın'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | Mete
@plan: karşı tepeden aynı ses geri geldi | şarkı söyledi ve aynı şarkıyı tepeden duydu
@tohum: niloya-0015
@degisim: leke -> rüzgar
Tepelerde hafif bir rüzgar esiyordu. Niloya ile Mete kekik toplarken Mete "Buldum!" diye bağırdı. Karşı tepeden de aynı ses geri geldi. "Bu ses nereden geliyor?" diye sordu Mete. Niloya karşı tepeye baktı ama orada kimseyi göremedi. Sonra en sevdiği şarkıyı yüksek sesle söyledi. Biraz sonra aynı şarkı tepeden duyuldu. "Mete, bu bizim sesimiz, karşı tepeden geri geliyor!" dedi Niloya. Mete güldü ve kalın sesini de şarkıya kattı. Tepeden bu kez iki ses birden geldi. İki arkadaş şarkı söyleyerek kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Karşı tepeden de aynı ses geri geldi"
   - Cümle 3: «Karşı tepeden de aynı ses geri geldi.»
   - Açıklama: Yankı gerçek bir sorun değil; hiçbir şey ters gitmiyor, çözülecek bir dert yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kalın sesini de şarkıya kattı"
   - Cümle 9: «Mete güldü ve kalın sesini de şarkıya kattı.»
   - Açıklama: 'Sesini şarkıya katmak' mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "kalın sesini de şarkıya kattı"
   - Cümle 9: «Mete güldü ve kalın sesini de şarkıya kattı.»
   - Açıklama: Kartın ilişki alanına göre Mete Niloya ile aynı yaşta küçük bir çocuk; kalın ses ona uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0015` birebir aynı, `@degisim: leke -> rüzgar` (tutuyorsan), ardından `@onarim: aa6c109ff6b7c4c61819caba906ad7413aa8e89f`, sonra gövde.

### Hikâye 8: tohum niloya-0016 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0016
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'inci', fiil 'binmek', sıfat 'tozlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: salıncak hiç sallanmadı | ayaklarını öne uzatıp geriye çekti
@tohum: niloya-0016
@degisim: inci -> salıncak
Bir sabah Niloya parkta yeni ve büyük bir salıncak gördü. Salıncak tozluydu, bu yüzden Niloya önce onu eliyle sildi. Sonra merakla salıncağa bindi ama salıncak hiç sallanmadı. Niloya kıpırdamadan oturuyordu. Niloya salıncağın iplerine baktı ve düşündü. Sonra ayaklarını öne uzattı ve geriye çekti. Salıncak biraz ileri gitti ve geri geldi. Niloya bunu birkaç kez yaptı. Salıncak ileri geri güzelce sallanmaya başladı. Serin rüzgar yüzüne esti. Niloya yeni salıncakta mutlu mutlu sallandı ve güldü.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Salıncak tozluydu, bu yüzden Niloya önce onu eliyle sildi"
   - Cümle 2: «Salıncak tozluydu, bu yüzden Niloya önce onu eliyle sildi.»
   - Açıklama: Tozlu salıncak ve silme ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "önce onu eliyle sildi"
   - Cümle 2: «Salıncak tozluydu, bu yüzden Niloya önce onu eliyle sildi.»
   - Açıklama: Salıncağın tozlu olup silinmesi soruna ya da çözüme hiçbir katkı yapmayan işlevsiz bir ayrıntı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra merakla salıncağa bindi"
   - Cümle 3: «Sonra merakla salıncağa bindi ama salıncak hiç sallanmadı.»
   - Açıklama: Tohumdaki keşfet özelliği yalnız süs olarak bir zarfla geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0016` birebir aynı, `@degisim: inci -> salıncak` (tutuyorsan), ardından `@onarim: 393a1910205b09eefa220828f21d277a72c23508`, sonra gövde.

### Hikâye 9: tohum niloya-0017 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0017
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'ay', fiil 'götürmek', sıfat 'yetenekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: suyun içindeki beyaz ve yuvarlak şeyi merak etti | gökyüzüne bakıp ayın suda göründüğünü buldu
@tohum: niloya-0017
@degisim: yetenekli -> yuvarlak
Bir sabah Niloya ormanda fındık topluyordu. Birden ağaçların arasında, yerdeki küçük suda beyaz, yuvarlak bir şey gördü. Niloya'nın aklına bir soru geldi: Suya ay mı düşmüştü? Suyun yanına eğildi ve ona dikkatle baktı. Parmağıyla suya dokununca beyaz şey titredi ve dağıldı. Su durunca beyaz şey yine yerine geldi. Niloya başını kaldırıp gökyüzüne baktı. Ağaçların üstünde beyaz ay duruyordu. Ay suya hiç düşmemişti, gökyüzündeydi. Niloya gülümsedi ve fındıkları neşeyle eve götürdü.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yerdeki küçük suda beyaz"
   - Cümle 2: «Birden ağaçların arasında, yerdeki küçük suda beyaz, yuvarlak bir şey gördü.»
   - Açıklama: 'Küçük su' birikinti anlamında doğal değil; 'su birikintisi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yerdeki küçük suda"
   - Cümle 2: «Birden ağaçların arasında, yerdeki küçük suda beyaz, yuvarlak bir şey gördü.»
   - Açıklama: 'Küçük su' yanlış kullanım; 'küçük su birikintisi' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına bir soru geldi"
   - Cümle 3: «Niloya'nın aklına bir soru geldi: Suya ay mı düşmüştü?»
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım.
   - Açıklama: 'Aklına gelmek' deyimdir, 3 yaşındaki çocuğa uygun değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Parmağıyla suya dokununca beyaz"
   - Cümle 5: «Parmağıyla suya dokununca beyaz şey titredi ve dağıldı.»
   - Açıklama: Güvenli kullanım satırına göre Niloya suya yalnız bakar, burada suya dokunuyor.
5. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "fındıkları neşeyle eve götürdü"
   - Cümle 10: «Niloya gülümsedi ve fındıkları neşeyle eve götürdü.»
   - Açıklama: Hikaye ormanda başlıyor ama son cümlede Niloya eve gidiyor ve sahne başlıktaki yerin dışına çıkıyor.
   - Açıklama: Hikaye ormanda başlıyor ama son cümlede sahne eve taşınıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0017` birebir aynı, `@degisim: yetenekli -> yuvarlak` (tutuyorsan), ardından `@onarim: 39fa9706e3aa72fb4fe0407ebc7ff2b4869bcf41`, sonra gövde.

### Hikâye 10: tohum niloya-0018 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0018
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'filiz', fiil 'zıplatmak', sıfat 'uykulu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: uykulu ağabeyinin topu yüzünden filiz kırılabilirdi | filizi taşlarla çevirip ağabeyine gösterdi
@tohum: niloya-0018
Ormanda, fındık ağaçlarının altında Niloya küçük, yeşil bir filiz buldu. Niloya bu filizi Murat'a sürpriz olarak göstermek istedi. Ama uykulu Murat topunu tam oraya zıplatıyordu, filiz kırılabilirdi. Niloya hemen filizi küçük taşlarla çevirdi. Sonra Murat'ı çağırmak için neşeli bir şarkı söyledi. Murat şarkıyı duyunca topunu bıraktı ve yanına geldi. "Abi, bak, burada yeni bir filiz var!" dedi Niloya. Murat taşların ortasındaki filizi görünce gülümsedi. "Ne güzel bir sürpriz, Niloya, topumu buradan uzakta oynarım!" dedi Murat. İkisi taşların yanında sevinçle el çırptı. Niloya bundan sonra küçük bir filiz görünce onu taşlarla çevirdi.
```

**Hakem bulguları (4):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Ama uykulu Murat topunu"
   - Cümle 3: «Ama uykulu Murat topunu tam oraya zıplatıyordu, filiz kırılabilirdi.»
   - Açıklama: Kartta Murat'ın huyu top oynamak ve koşturmaktır; uykululuk Tospik'in huyudur.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "uykulu Murat topunu tam oraya zıplatıyordu"
   - Cümle 3: «Ama uykulu Murat topunu tam oraya zıplatıyordu, filiz kırılabilirdi.»
   - Açıklama: Murat'ın uykulu olması hiçbir işe yaramıyor ve top zıplatmasıyla da uyuşmuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama uykulu Murat topunu"
   - Cümle 3: «Ama uykulu Murat topunu tam oraya zıplatıyordu, filiz kırılabilirdi.»
   - Açıklama: Murat'ın uykulu olması işlevsiz ve top zıplatmasıyla da uyuşmuyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "topumu buradan uzakta oynarım"
   - Cümle 9: «"Ne güzel bir sürpriz, Niloya, topumu buradan uzakta oynarım!" dedi Murat.»
   - Açıklama: 'Topumu oynarım' dilbilgisel değil; 'topumla oynarım' olmalı.
   - Açıklama: Ek yanlış; 'topumla oynarım' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0018` birebir aynı, ardından `@onarim: 96ab8b94686e805f5d4d374bf4bdbb88a8bfd18a`, sonra gövde.

### Hikâye 11: tohum niloya-0019 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0019
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: kaybolan eşya
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'topaç', fiil 'gerinmek', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: topaç dönerken çiçeklerin arasına yuvarlandı | yaprakların altına sonra çiçeklerin arkasına bakıp topacı buldu
@tohum: niloya-0019
@degisim: mükemmel -> düz
Evin bahçesinde Niloya kırmızı topacını çeviriyordu. Topaç hızla döndü ve çiçeklerin arasına yuvarlandı. Niloya çiçeklerin arasını aradı ama topacı göremedi. Merakla eğildi ve yaprakların altına tek tek baktı. Topaç orada da yoktu. Niloya çok eğilmişti. Ayağa kalktı ve gerindi. Sonra çiçeklerin arkasına geçip baktı. Kırmızı topaç çitin yanında duruyordu. Niloya topacı aldı ve evin önündeki taşların üstünde çevirdi. Taşlar düzdü ve topaç uzun süre döndü. Niloya bundan sonra topacını hep taşların üstünde çevirdi.
```

**Hakem bulguları (6):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "yaprakların altına sonra çiçeklerin arkasına"
   - Cümle 0 (plan satırı): «topaç dönerken çiçeklerin arasına yuvarlandı | yaprakların altına sonra çiçeklerin arkasına bakıp topacı buldu»
   - Açıklama: Plan satırında sıralanan iki eylem arasında virgül eksik: 'altına, sonra'.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Topaç hızla döndü ve çiçeklerin arasına yuvarlandı"
   - Cümle 2: «Topaç hızla döndü ve çiçeklerin arasına yuvarlandı.»
   - Açıklama: Topacın neden yuvarlandığı söylenmiyor; sonda çıkan taş dersi söylenmemiş bir sebebe dayanıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "yaprakların altına tek tek baktı"
   - Cümle 4: «Merakla eğildi ve yaprakların altına tek tek baktı.»
   - Açıklama: Topacı bulmak için çiçeklerin arası, yaprakların altı ve çiçeklerin arkası olmak üzere ikiden fazla adım gerekiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya çok eğilmişti. Ayağa kalktı ve gerindi"
   - Cümle 7: «Ayağa kalktı ve gerindi.»
   - Açıklama: Eğilip gerinme ayrıntısı olayda işlevsiz.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ayağa kalktı ve gerindi"
   - Cümle 7: «Ayağa kalktı ve gerindi.»
   - Açıklama: Eğilip gerinme olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "evin önündeki taşların üstünde çevirdi"
   - Cümle 10: «Niloya topacı aldı ve evin önündeki taşların üstünde çevirdi.»
   - Açıklama: Düz taşlar sebepsizce beliriyor ve sona yeni bir olay ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0019` birebir aynı, `@degisim: mükemmel -> düz` (tutuyorsan), ardından `@onarim: f4a54f7c63b2d93a717d4882f6e232bd070910ec`, sonra gövde.

### Hikâye 12: tohum niloya-0020 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0020
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: kaybolan eşya
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'trompet', fiil 'kurmak', sıfat 'aceleci'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: rüzgar oyuncak trompeti yokuştan aşağı yuvarladı | acele etmeden çalıların altına bakıp trompeti buldu
@tohum: niloya-0020
@degisim: kurmak -> bulmak
Niloya yeşil tepede oyuncak trompetini çalıyordu. Sonra onu çimenlere bıraktı ve kekik toplamaya başladı. Birden güçlü bir rüzgar esti ve trompet yokuştan aşağı yuvarlandı. Niloya arkasına döndü ama trompetini göremedi. Aceleci davranmadı ve etrafına dikkatle baktı. Yokuşun dibinde büyük kekik çalıları vardı. Niloya çalıların yanına yavaşça yürüdü ve merakla eğildi. İlk çalının arkasında hiçbir şey yoktu. İkinci çalının altında sarı bir şey parlıyordu. Bu, onun trompetiydi! Niloya onu aldı ve neşeyle üfledi. Trompetten güzel bir ses çıktı. Niloya çok sevindi, çünkü kaybolan trompetini bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Aceleci davranmadı ve etrafına"
   - Cümle 5: «Aceleci davranmadı ve etrafına dikkatle baktı.»
   - Açıklama: 'Aceleci davranmak' küçük çocuk için soyut; 'acele etmedi' gibi somut bir anlatım gerekir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Aceleci davranmadı ve etrafına dikkatle baktı"
   - Cümle 5: «Aceleci davranmadı ve etrafına dikkatle baktı.»
   - Açıklama: Tohumdaki özellik keşfet/merak; sabır ve dikkat ikinci bir özellik olarak ekleniyor, kartın özellikler alanında yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0020` birebir aynı, `@degisim: kurmak -> bulmak` (tutuyorsan), ardından `@onarim: fe7929f42d6a1f3b861ca762b858168ab3944b8e`, sonra gövde.
