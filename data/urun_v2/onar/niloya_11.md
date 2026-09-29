# Editör görevi (onarım): Niloya, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar11.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0002 (deneme 5 -> 6)

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
Parkta Niloya kaydırağın yanında sarı bir çiçek gördü. Çiçek güneşte yavaş yavaş açılıyordu. Niloya bunu Tospik'e göstermek istedi ama Tospik uyuyordu. Az önce ikisi oyuncaklarla limonlu kek satma oyunu oynamıştı. Tospik bu oyundan çok yorulmuştu. Niloya onun yanına oturdu ve neşeli bir şarkı söyledi. Tospik şarkıyı duyunca gözlerini açtı. Başını kabuğundan çıkardı ve çiçeğe baktı. Çiçek daha tam açık değildi. İkisi yan yana oturdu ve bekledi. Sonra sarı yapraklar bir bir açıldı. Tospik gülümsedi ve çiçeği kokladı. Niloya çok sevindi, çünkü çiçek açarken Tospik de yanındaydı.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "limonlu kek satma oyunu"
   - Cümle 4: «Az önce ikisi oyuncaklarla limonlu kek satma oyunu oynamıştı.»
   - Açıklama: Kartın kapalı dünyasında olmayan, başka bir dünyadan gelen kek satma nesnesi ve etkinliği ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0002` birebir aynı, `@degisim: düğüm -> çiçek` (tutuyorsan), ardından `@onarim: fcb66026789c91c83c3e4f27e716373e4c0ae51e`, sonra gövde.

### Hikâye 2: tohum niloya-0009 (deneme 5 -> 6)

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
Niloya ile babaannesi parkta bir kağıda resim çiziyordu. İkisi de güneşi boyamak istiyordu ama tek bir turuncu kalem vardı. Niloya biraz düşündü. "Babaanne, sırayla boyayalım, şarkım bitince kalem sende olsun," dedi Niloya. Sonra neşeli bir şarkı söyledi ve güneşin yarısını boyadı. Şarkı bitince kalemi babaannesine verdi. Babaannesi güneşin öbür yarısını turuncuya boyadı. Taşan bir çizgiyi de silgiyle sildi. Resim bitti. "Sırayla yapınca ne güzel oldu!" dedi babaannesi. Niloya bundan sonra kalem tek olunca onu babaannesiyle sırayla kullandı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Taşan bir çizgiyi de silgiyle sildi"
   - Cümle 8: «Taşan bir çizgiyi de silgiyle sildi.»
   - Açıklama: Silgi ve taşan çizgi sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Silgi ve taşan çizgi sebepsiz beliriyor, olaya katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0009` birebir aynı, `@degisim: yemek -> çizmek` (tutuyorsan), ardından `@onarim: af29be81a87be1f3c7c5608c932318a187e0871d`, sonra gövde.

### Hikâye 3: tohum niloya-0010 (deneme 5 -> 6)

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
@plan: dedesinin küçük ağacında hiç fındık yoktu | şarkı söyleyip dedesini çağırdı ve fındıklarını paylaştı
@tohum: niloya-0010
@degisim: ferah -> serin
Rüzgar dalları savuruyordu ve orman çok serindi. Niloya ile dedesi ormanda fındık topluyordu. Niloya'nın ağacı fındıkla doluydu ama dedesinin ağacı küçüktü ve hiç fındığı yoktu. Niloya alçak dallardan bir sürü fındık kopardı. Önlüğünün cebini fındıkla doldurdu. Dedesinin eli boştu. Niloya dedesini çağırmak için neşeli bir şarkı söyledi. Dedesi şarkıyı duyunca gülümsedi ve yanına geldi. "Dede, bu fındıkların yarısı senin," dedi Niloya. Sonra fındıkların yarısını dedesine verdi. "Teşekkürler, Niloya, bunları birlikte yiyelim," dedi dedesi. Niloya çok sevindi, çünkü artık ikisinin de fındığı vardı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "dedesini çağırmak için neşeli bir şarkı söyledi"
   - Cümle 7: «Niloya dedesini çağırmak için neşeli bir şarkı söyledi.»
   - Açıklama: Yanındaki dedesini çağırmak için şarkı söylemek sebepsiz; şarkı çözüme gerekçesiz sokuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0010` birebir aynı, `@degisim: ferah -> serin` (tutuyorsan), ardından `@onarim: 52ed7714fd5b0bb5e24885ac6ef885c9a4847f59`, sonra gövde.

### Hikâye 4: tohum niloya-0013 (deneme 4 -> 5)

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
Niloya ormandaydı ve güneş yeni doğuyordu. İnce bir dala yapraklar takıp bir taç yaptı. Ama taç çok büyüktü ve başından gözlerine kaydı. Tacı çıkardı ve ona uzun uzun baktı. Niloya içinden sordu: Dal çok mu uzundu? Dalı başının çevresine tuttu ve gerçekten çok uzun olduğunu gördü. Dalın iki ucunu biraz daha üst üste getirdi. Dalı kırmamak için çok dikkatli davrandı. Dalı sıkıca sardı. Taç bu kez tam başına oturdu. Niloya yapraklı tacıyla ormanda neşeyle dolaştı. Niloya taç yaparken dalı önce başına göre ölçmeyi öğrendi.
```

**Hakem bulguları (6):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya içinden sordu: Dal çok mu uzundu?"
   - Cümle 5: «Niloya içinden sordu: Dal çok mu uzundu?»
   - Açıklama: Niloya kendi kendine soru soruyor.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya içinden sordu: Dal"
   - Cümle 5: «Niloya içinden sordu: Dal çok mu uzundu?»
   - Açıklama: Niloya kendi kendine soru soruyor.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "içinden sordu: Dal çok mu uzundu?"
   - Cümle 5: «Niloya içinden sordu: Dal çok mu uzundu?»
   - Açıklama: İç konuşma tırnak içine alınmamış.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "sordu: Dal çok mu uzundu?"
   - Cümle 5: «Niloya içinden sordu: Dal çok mu uzundu?»
   - Açıklama: Soru tırnak içine alınmamış ve anlatımla karışıyor.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Dalı başının çevresine tuttu"
   - Cümle 6: «Dalı başının çevresine tuttu ve gerçekten çok uzun olduğunu gördü.»
   - Açıklama: Durum eki yanlış; 'başının çevresinde tuttu' olmalı.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Dalı sıkıca sardı."
   - Cümle 9: «Dalı sıkıca sardı.»
   - Açıklama: 'Dal/Dalı' art arda cümlelerin başında gereksiz tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0013` birebir aynı, `@degisim: pedal -> dal` (tutuyorsan), ardından `@onarim: bfd8230b4abaf34f9427232f649ffcc75a281399`, sonra gövde.

### Hikâye 5: tohum niloya-0015 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: karşı tepeden aynı ses geldi ama kimse görünmedi | şarkı söyleyip sesin geri geldiğini gösterdi
@tohum: niloya-0015
@degisim: leke -> rüzgar
Tepelerde hafif bir rüzgar esiyordu. Niloya ile Mete yeşil tepede kekik topluyordu. Mete eğlenmek için kalın bir sesle "Merhaba!" diye bağırdı. Karşı tepeden de aynı ses geldi. Mete karşı tepeye baktı ama orada kimseyi göremedi. "Niloya, orada kim var?" diye sordu Mete. Niloya biraz düşündü ve kısa bir şarkı söyledi. Karşı tepeden aynı şarkı geri geldi. "Bu bizim sesimiz, Mete, ses tepeye çarpıp geri geliyor," dedi Niloya. Mete güldü ve o da sesini Niloya'nın şarkısına kattı. Karşı tepeden iki ses birden geldi. İki arkadaş şarkı söyleyerek kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "orada kimseyi göremedi"
   - Cümle 5: «Mete karşı tepeye baktı ama orada kimseyi göremedi.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü ve beşinci cümlede ortaya çıkıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sesini Niloya'nın şarkısına kattı"
   - Cümle 10: «Mete güldü ve o da sesini Niloya'nın şarkısına kattı.»
   - Açıklama: 'Sesini şarkıya katmak' mecazlı bir anlatım, küçük çocuğa uygun değil.
   - Açıklama: 'Sesini şarkıya katmak' mecazlı bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0015` birebir aynı, `@degisim: leke -> rüzgar` (tutuyorsan), ardından `@onarim: 8305c337e172a84c68a4dd3fbd5aced1f4f46e73`, sonra gövde.

### Hikâye 6: tohum niloya-0017 (deneme 4 -> 5)

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
Bir sabah Niloya ormanda fındık dolu sepetini götürüyordu. Birden yerdeki küçük bir su birikintisinde beyaz, yuvarlak bir şey gördü. Niloya'nın bir sorusu vardı: Suya ay mı düşmüştü? Suyun yanına eğildi ve beyaz şeye dikkatle baktı. Sonra suya küçük bir yaprak attı. Beyaz şey titredi ve dağıldı. Su durunca beyaz şey yine yerine geldi. Niloya başını kaldırıp gökyüzüne baktı. Ağaçların üstünde beyaz ay duruyordu. Ay suya hiç düşmemişti, gökyüzündeydi. Niloya gülümsedi ve sepetiyle neşeyle yürümeye devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir su birikintisinde"
   - Cümle 2: «Birden yerdeki küçük bir su birikintisinde beyaz, yuvarlak bir şey gördü.»
   - Açıklama: 'Su birikintisi' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya'nın bir sorusu vardı"
   - Cümle 3: «Niloya'nın bir sorusu vardı: Suya ay mı düşmüştü?»
   - Açıklama: Kartın soru özelliği 'merak ettiği her şeyi sorar' diyor; Niloya kimseye sormuyor, soru yalnız içinden geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0017` birebir aynı, `@degisim: yetenekli -> yuvarlak` (tutuyorsan), ardından `@onarim: e6da597e3e2bcdf521a3e147a353edd1e9e256d6`, sonra gövde.

### Hikâye 7: tohum niloya-0019 (deneme 4 -> 5)

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
@plan: toprak düz olmadığı için topaç çiçeklerin arasından ileri yuvarlandı | çiçeklerin ötesine, çitin yanına baktı ve topacı buldu
@tohum: niloya-0019
@degisim: mükemmel -> düz
Evin bahçesinde Niloya kırmızı topacını çeviriyordu. Topaç hızla döndü ama bahçenin toprağı düz değildi. Topaç bir yana kaydı ve çiçeklerin arasından ileri yuvarlandı. Niloya topacın nereye gittiğini çok merak etti. Çiçeklerin arasına eğildi ve her yere baktı. Ama topaç orada yoktu. Niloya uzun süre eğilmişti. Ayağa kalktı ve gerindi. Sonra çiçeklerin ötesine, çitin yanına baktı. Kırmızı topacı çitin dibinde duruyordu. Niloya hemen oraya koştu ve topacını sevinçle aldı. Niloya bundan sonra topacını hep düz yerde çevirdi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ayağa kalktı ve gerindi"
   - Cümle 8: «Ayağa kalktı ve gerindi.»
   - Açıklama: Gerinme ayrıntısı olayda hiçbir işe yaramıyor ve çözümü getirmiyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Kırmızı topacı çitin dibinde duruyordu"
   - Cümle 10: «Kırmızı topacı çitin dibinde duruyordu.»
   - Açıklama: Özne yalın olmalı; 'Kırmızı topaç çitin dibinde duruyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0019` birebir aynı, `@degisim: mükemmel -> düz` (tutuyorsan), ardından `@onarim: 135ab20f29a6f6a06dd54c6a8b8ae33d105661ed`, sonra gövde.

### Hikâye 8: tohum niloya-0020 (deneme 3 -> 4)

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
@plan: rüzgar oyuncak trompeti yokuştan aşağı yuvarladı | yokuşun dibine inip çalıların altına bakınca trompeti buldu
@tohum: niloya-0020
@degisim: kurmak -> bulmak
Niloya yeşil tepede oyuncak trompetini çalıyordu. Sonra onu çimenlere bıraktı ve kekik toplamaya başladı. Birden güçlü bir rüzgar esti ve trompet yokuştan aşağı yuvarlandı. Niloya arkasına döndü ama trompetini göremedi. Niloya aceleci davranmadı ve yokuştan yavaş yavaş indi. Orada büyük kekik çalıları vardı. Niloya çalıların yanına gitti ve merakla eğildi. İlk çalının arkasında hiçbir şey yoktu. İkinci çalının altında sarı bir şey parlıyordu. Bu, onun trompetiydi! Niloya onu aldı ve neşeyle üfledi. Trompetten güzel bir ses çıktı. Niloya çok sevindi, çünkü kaybolan trompetini bulmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya aceleci davranmadı ve"
   - Cümle 5: «Niloya aceleci davranmadı ve yokuştan yavaş yavaş indi.»
   - Açıklama: 'Aceleci davranmak' 3 yaşındaki çocuk için soyut bir ifade.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0020` birebir aynı, `@degisim: kurmak -> bulmak` (tutuyorsan), ardından `@onarim: 7827c61f6d1a5dab1c4fa53c1f7a87acdf5d7ab5`, sonra gövde.

### Hikâye 9: tohum niloya-0022 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Tospik
@tohum: niloya-0022
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'sebze', fiil 'sıkmak', sıfat 'küçük'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | Tospik
@plan: kaplumbağa havucun peşinden gidip kaydırağın altında sıkıştı | arkasına havuç koyup onu geri çağırdı
@tohum: niloya-0022
@degisim: sıkmak -> sıkışmak
Parkta Niloya, Tospik'e küçük sebze parçaları veriyordu. Bir havuç parçası yere düştü ve kaydırağın alçak ucunun altına yuvarlandı. Tospik havucun peşinden gitti ama kabuğu kaydırağın altına sığmadı. Oradan ince bir ses geldi. Niloya merakla eğildi ve baktı. Tospik ileri gidemiyordu, çünkü kabuğu biraz sıkışmıştı. "Bana yardım eder misin, Niloya?" diye sordu Tospik. "Tabii, Tospik," dedi Niloya. Niloya başka bir havucu Tospik'in arkasına koydu. "Geri gel, Tospik, havuç burada," dedi Niloya. Tospik yavaşça geri geri yürüdü ve kolayca dışarı çıktı. Sonra havucu afiyetle yedi ve ikisi parkta mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "kabuğu biraz sıkışmıştı"
   - Cümle 6: «Tospik ileri gidemiyordu, çünkü kabuğu biraz sıkışmıştı.»
   - Açıklama: Tospik'in kaydırağın altında sıkışıp kalması küçük çocukları kaygılandırabilecek bir tehlike anı içeriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0022` birebir aynı, `@degisim: sıkmak -> sıkışmak` (tutuyorsan), ardından `@onarim: 6bf33a37fca14360c56559838a5a9b526465a1d2`, sonra gövde.

### Hikâye 10: tohum niloya-0023 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | babaannesi
@tohum: niloya-0023
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: sırayla oynamak
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'şeftali', fiil 'susamak', sıfat 'yağmurlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | babaannesi
@plan: ikisi aynı anda şarkı söyledi ve sesler karıştı | şeftaliyi tutan şarkı söyledi, diğeri sustu
@tohum: niloya-0023
@degisim: susamak -> susmak
Dışarıda yağmurlu bir hava vardı ve damlalar cama tık tık vuruyordu. Niloya ile babaannesi evde şarkı söyleyerek oynuyordu. Ama ikisi aynı anda şarkı söyledi ve sesler karıştı. Niloya masadaki şeftaliyi aldı. "Babaanne, şeftali kimin elindeyse şarkıyı o söyler," dedi Niloya. Önce Niloya şeftaliyi tuttu ve neşeli bir şarkı söyledi. Babaannesi sustu ve onu dinledi. Şarkı bitince Niloya şeftaliyi babaannesine verdi. Babaannesi de güzel bir şarkı söyledi. Bu kez Niloya sessizce dinledi. "Sırayla şarkı söylemek çok eğlenceli, babaanne!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ikisi aynı anda şarkı söyledi"
   - Cümle 3: «Ama ikisi aynı anda şarkı söyledi ve sesler karıştı.»
   - Açıklama: Tohumdaki şarkı özelliği bir kez değil defalarca kullanılıyor ve çözümü şeftali sırası getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0023` birebir aynı, `@degisim: susamak -> susmak` (tutuyorsan), ardından `@onarim: 8f024abd06c35204614dfadbf2c37a340bd46a8b`, sonra gövde.

### Hikâye 11: tohum niloya-0024 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | dedesi
@tohum: niloya-0024
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: bir şey yapmak
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'teneke', fiil 'şaşırtmak', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | dedesi
@plan: boş kutuya elle vurunca ses zayıf çıktı | dedesine sordu ve kuru çubuklarla vurdu
@tohum: niloya-0024
Bir sabah Niloya ile dedesi yeşil tepede meyveli kurabiyeleri bitirdi. Niloya boş teneke kutudan bir davul yapmak istedi. Ama eliyle vurunca kutu çok zayıf bir ses çıkardı. Niloya kutuya neyle vurabileceğini dedesine sordu. Dedesi ona kuru bir çubukla vurmasını söyledi. Niloya çimenlerin arasında iki kuru çubuk buldu. Sonra çubuklarla kutuya sırayla vurdu. Tepede güçlü ve neşeli bir ses yayıldı. Bu ses Niloya'yı çok şaşırttı. Dedesi gülerek ellerini çırptı. Niloya davulunu çalarak tepede yürüdü. Niloya çok sevindi, çünkü kendi davulunu yapmıştı.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "boş teneke kutudan bir davul"
   - Cümle 2: «Niloya boş teneke kutudan bir davul yapmak istedi.»
   - Açıklama: Açık teneke kutuyla oynamak kesik riski taşıyan, taklit edilebilir bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0024` birebir aynı, ardından `@onarim: 7d53a5c916e8e8dfaca59acb18bccec16b66f57f`, sonra gövde.

### Hikâye 12: tohum niloya-0026 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0026
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'tabure', fiil 'uyumak', sıfat 'kremalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: rüzgarda sallanan sepet uyuyan babaannenin yanında ses yapıyordu | sepeti daldan indirdi ve ona yumuşak bir şarkı söyledi
@tohum: niloya-0026
@degisim: kremalı -> boş
Rüzgar esiyordu ve ağaçların arasından tak tak bir ses geliyordu. Niloya'nın babaannesi yorulmuş, küçük bir taburede uyuyordu. Niloya babaannesinin rahat rahat uyumasını istedi. Sesin nereden geldiğini bulmak için etrafa baktı. Babaannesinin boş sepeti alçak bir dala asılıydı. Sepet rüzgarda sallanıyor ve ağaca çarpıyordu. Niloya sepeti daldan yavaşça indirdi ve yere koydu. Ses hemen kesildi. Ama babaannesi biraz kıpırdadı. Niloya onun yanına oturdu ve yumuşak bir sesle şarkı söyledi. Babaannesi gülümsedi ve tatlı tatlı uyudu. Niloya da onun yanında mutlu mutlu fındık topladı.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve ona yumuşak bir şarkı söyledi"
   - Cümle 0 (plan satırı): «rüzgarda sallanan sepet uyuyan babaannenin yanında ses yapıyordu | sepeti daldan indirdi ve ona yumuşak bir şarkı söyledi»
   - Açıklama: Plan satırında 'ona' en yakın ad olan sepeti gösteriyor; babaanne kastedildiği belli değil.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "sepeti daldan indirdi ve ona yumuşak bir şarkı söyledi"
   - Cümle 0 (plan satırı): «rüzgarda sallanan sepet uyuyan babaannenin yanında ses yapıyordu | sepeti daldan indirdi ve ona yumuşak bir şarkı söyledi»
   - Açıklama: Planda şarkı sepete söyleniyor gibi; gövdede babaanneye söyleniyor.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "babaannesi yorulmuş, küçük bir"
   - Cümle 2: «Niloya'nın babaannesi yorulmuş, küçük bir taburede uyuyordu.»
   - Açıklama: Anlatımda -mış biçimi kullanılmış; 'yorulmuştu' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "mutlu mutlu fındık topladı"
   - Cümle 12: «Niloya da onun yanında mutlu mutlu fındık topladı.»
   - Açıklama: Fındık sebepsizce son cümlede beliriyor ve olayla bağı yok.
   - Açıklama: Fındık hikayede hiç kurulmadan son cümlede sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0026` birebir aynı, `@degisim: kremalı -> boş` (tutuyorsan), ardından `@onarim: 100d8aa74f1818e9a339bfffdc8d35c1d301a179`, sonra gövde.
