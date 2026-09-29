# Editör görevi (onarım): Niloya, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0059 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0059
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'dalga', fiil 'sunmak', sıfat 'sadık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: ağabeyinin sepetinde delik vardı ve fındıkları döküldü | kendi sağlam sepetini ağabeyiyle paylaştı
@tohum: niloya-0059
@degisim: sadık -> sağlam
Ormanda Niloya ile Murat fındık topluyordu. Ama Murat'ın sepetinin dibinde bir delik vardı. Topladığı fındıklar delikten yere dökülüyordu. Murat boş sepetine üzgün üzgün baktı. Niloya kendi sepetini ağabeyine sundu. "Abiciğim, benim sepetim sağlam, fındıklarımızı buna koyalım," dedi Niloya. "Teşekkürler, Niloya, sen çok iyisin," dedi Murat. Murat yerdekileri topladı ve Niloya'nın sepetine koydu. Sonra Niloya en sevdiği dalga şarkısını söyledi. Şarkı sürerken ikisi sırayla sepete fındık attı. Niloya ile Murat aynı sepeti mutlu mutlu doldurdu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "en sevdiği dalga şarkısını"
   - Cümle 9: «Sonra Niloya en sevdiği dalga şarkısını söyledi.»
   - Açıklama: 'Dalga şarkısı' anlamsız bir tamlama; kelime yanlış anlamda kullanılmış.
   - Açıklama: Ormanda 'dalga şarkısı' anlamı belirsiz; kelime yerinde kullanılmamış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği dalga şarkısını söyledi"
   - Cümle 9: «Sonra Niloya en sevdiği dalga şarkısını söyledi.»
   - Açıklama: Sorun sepeti paylaşarak çözülmüş, şarkı özelliği çözüme katkı vermiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra Niloya en sevdiği dalga şarkısını söyledi"
   - Cümle 9: «Sonra Niloya en sevdiği dalga şarkısını söyledi.»
   - Açıklama: Sorun sepet paylaşımıyla çözüldükten sonra şarkı özelliği işe yaramayan bir süs olarak ekleniyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "en sevdiği dalga şarkısını söyledi"
   - Cümle 9: «Sonra Niloya en sevdiği dalga şarkısını söyledi.»
   - Açıklama: Şarkı sorunla ya da çözümle ilgisi olmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0059` birebir aynı, `@degisim: sadık -> sağlam` (tutuyorsan), ardından `@onarim: 72165e86ea272756dce3b0cb6769f61b9580c66e`, sonra gövde.

### Hikâye 2: tohum niloya-0060 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0060
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'çekirdek', fiil 'karıştırmak', sıfat 'ekşi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: çiçeklerin yanından bilinmeyen bir ses geldi | yaprakları karıştırıp düşen çekirdekleri buldu
@tohum: niloya-0060
@degisim: ekşi -> kuru
Bir sabah Niloya evin bahçesinde oynuyordu. Birden çiçeklerin yanından küçük bir ses geldi. Niloya bu sesin nereden geldiğini bilmiyordu. Niloya'nın aklına hemen bir soru geldi: Bu sesi ne yapıyordu? Niloya çiçeklerin yanına yavaşça yürüdü. Yerdeki kuru yaprakları elleriyle karıştırdı. Ama yaprakların altında hiçbir şey yoktu. Sonra başını kaldırıp büyük sarı çiçeklere baktı. Rüzgar esince çiçeklerin başları sallanıyordu. Çiçeklerden küçük siyah çekirdekler düşüyordu. Çekirdekler yapraklara çarpınca tık tık diye vuruyordu. Niloya çok sevindi, çünkü o küçük sesi yapan şeyi bulmuştu.
```

**Hakem bulguları (7):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yaprakları karıştırıp düşen çekirdekleri buldu"
   - Cümle 0 (plan satırı): «çiçeklerin yanından bilinmeyen bir ses geldi | yaprakları karıştırıp düşen çekirdekleri buldu»
   - Açıklama: Gövdede yaprakları karıştırınca hiçbir şey bulunmuyor; çekirdekler başını kaldırıp çiçeklere bakınca bulunuyor.
   - Açıklama: Gövdede yaprakları karıştırmak sonuç vermiyor; Niloya çekirdekleri başını kaldırıp çiçeklere bakınca buluyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Bu sesi ne yapıyordu"
   - Cümle 4: «Niloya'nın aklına hemen bir soru geldi: Bu sesi ne yapıyordu?»
   - Açıklama: Soru dilbilgisel olarak bozuk; 'Bu sesi ne çıkarıyordu?' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına hemen bir soru geldi"
   - Cümle 4: «Niloya'nın aklına hemen bir soru geldi: Bu sesi ne yapıyordu?»
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım.
   - Açıklama: 'Aklına gelmek' deyimi küçük çocuğa uygun değil.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "bir soru geldi: Bu sesi ne"
   - Cümle 4: «Niloya'nın aklına hemen bir soru geldi: Bu sesi ne yapıyordu?»
   - Açıklama: Aktarılan soru tırnak içinde verilmemiş.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tık tık diye vuruyordu"
   - Cümle 11: «Çekirdekler yapraklara çarpınca tık tık diye vuruyordu.»
   - Açıklama: 'Çarpınca vuruyordu' anlamca yanlış; 'tık tık diye ses çıkarıyordu' olmalı.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çarpınca tık tık diye vuruyordu"
   - Cümle 11: «Çekirdekler yapraklara çarpınca tık tık diye vuruyordu.»
   - Açıklama: Çekirdekler vurmaz; 'ses çıkarıyordu' olmalı, fiil öznesine uymuyor.
7. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "yapraklara çarpınca tık tık diye vuruyordu"
   - Cümle 11: «Çekirdekler yapraklara çarpınca tık tık diye vuruyordu.»
   - Açıklama: 'Çarpınca' ve 'vuruyordu' aynı şeyi iki kez söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0060` birebir aynı, `@degisim: ekşi -> kuru` (tutuyorsan), ardından `@onarim: ad23378a86ee43ad76f6811a747defc2d1000502`, sonra gövde.

### Hikâye 3: tohum niloya-0061 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0061
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'yemek', fiil 'bulmak', sıfat 'sabırlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: babaannesine sürpriz yapmak istedi ama elmalar yüksekteydi | yere düşmüş elmaları bulup yaprağa dizdi
@tohum: niloya-0061
@degisim: sabırlı -> kırmızı
Bir sabah Niloya ile babaannesi ormanda fındık topluyordu. Babaannesi yorulunca bir elma ağacının altına oturdu ve gözlerini kapattı. Niloya ona sürpriz bir yemek hazırlamak istedi ama elmalar çok yüksekteydi. Niloya yere baktı. Orada düşmüş kırmızı elmalar buldu. Elmaları büyük bir yaprağın üstüne dizdi. Yanlarına sepetten biraz fındık ekledi. Sonra yaprağı babaannesinin önüne koydu ve neşeli bir şarkı söyledi. Babaannesi şarkıyı duyunca gözlerini açtı. "Sürpriz, babaanne, bu yemek senin!" dedi Niloya. "Çok sağ ol, kızım," dedi babaannesi. Babaannesi fındıklardan birini yedi ve Niloya'ya mutlu mutlu sarıldı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Babaannesi fındıklardan birini yedi"
   - Cümle 12: «Babaannesi fındıklardan birini yedi ve Niloya'ya mutlu mutlu sarıldı.»
   - Açıklama: 'Babaannesi' kelimesi art arda iki cümlede gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0061` birebir aynı, `@degisim: sabırlı -> kırmızı` (tutuyorsan), ardından `@onarim: 694661129a18dda75c7f316800efceaef24692a0`, sonra gövde.

### Hikâye 4: tohum niloya-0062 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0062
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'çorap', fiil 'acıkmak', sıfat 'resimli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: çorabın ağzı açık kalıyordu ve fındıklar dökülüyordu | uzun bir otla çorabın ağzını bağladı
@tohum: niloya-0062
@degisim: acıkmak -> bağlamak
Rüzgar esiyordu ve fındık ağaçlarından yere fındıklar düşüyordu. Niloya eski, resimli bir çoraptan fındık çantası yapmak istiyordu. Ama çorabın ağzı açık kalıyordu ve fındıklar dışarı dökülüyordu. Niloya etrafa baktı ve yerde uzun, ince bir ot buldu. Otu iki eliyle çekti, ot çok sağlamdı. Çorabı yerdeki fındıklarla doldurdu. Sonra otu çorabın ağzına sıkıca bağladı. Niloya bir şarkı söyledi ve şarkı boyunca çantayı salladı. Fındıkların hepsi çorabın içinde kaldı. Niloya çok mutluydu, çünkü fındık çantasını kendisi yapmıştı.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Çorabı yerdeki fındıklarla doldurdu"
   - Cümle 6: «Çorabı yerdeki fındıklarla doldurdu.»
   - Açıklama: Fındıklar 3. cümlede çoraptan dökülüyor ama çorap ancak 6. cümlede fındıkla dolduruluyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya bir şarkı söyledi ve şarkı boyunca çantayı salladı"
   - Cümle 8: «Niloya bir şarkı söyledi ve şarkı boyunca çantayı salladı.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümüne katkı vermeyen süs olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0062` birebir aynı, `@degisim: acıkmak -> bağlamak` (tutuyorsan), ardından `@onarim: eadb8f9d41561dc0ef6fba0dc0ad8db7ebcb60c8`, sonra gövde.

### Hikâye 5: tohum niloya-0063 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0063
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'üzüm', fiil 'düzeltmek', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: yağmur yüzünden bahçede piknik yapamadı | örtüyü odaya yayıp evde piknik yaptı
@tohum: niloya-0063
Yağmur pencereye tıp tıp vuruyordu. Niloya bir tabağa üzüm koymuş, bahçede piknik yapmak istiyordu. Ama yağmur yüzünden bahçeye çıkamadı. Niloya pencereden dışarı baktı ve biraz üzüldü. Sonra piknik örtüsünü odanın ortasına yaydı. Örtünün bir ucunu elleriyle düzeltti. Üzüm tabağını da örtünün üstüne bıraktı. Yağmurun sesi odaya kadar geliyordu. Niloya bu sese uyan neşeli bir yağmur şarkısı söyledi. Şarkı söylerken üzümlerini tek tek yedi. Evdeki piknik de çok eğlenceli oldu. Niloya çok sevinçliydi, çünkü yağmurlu günde de pikniğini yapmıştı.
```

**Hakem bulguları (1):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "bir tabağa üzüm koymuş"
   - Cümle 2: «Niloya bir tabağa üzüm koymuş, bahçede piknik yapmak istiyordu.»
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı biçime kayıyor; 'koymuştu' olmalı.
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı biçime kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0063` birebir aynı, ardından `@onarim: 70af0112381dc03b5d2b289df3dc6ddf91485ac3`, sonra gövde.

### Hikâye 6: tohum niloya-0064 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0064
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'hamur', fiil 'yoğurmak', sıfat 'bilgili'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: dedesi de oynamak istedi ama hamur tekti | hamuru ikiye bölüp bir parçasını dedesine verdi
@tohum: niloya-0064
@degisim: bilgili -> yeşil
Niloya dedesiyle ormanda fındık ağaçlarının altında oturuyordu. Elinde yeşil bir oyun hamuru vardı. Dedesi de hamurla oynamak istedi, ama hamur tek bir taneydi. Niloya hamura baktı ve biraz düşündü. Sonra hamuru ikiye böldü ve bir parçasını dedesine verdi. Dedesi parçayı elleriyle yoğurdu ve ondan yuvarlak bir fındık yaptı. Niloya da küçük bir elma yaptı. Hamurla oynarken Niloya neşeli bir şarkı söyledi. Dedesi de gülümseyerek şarkıya katıldı. Şarkı bitince ikisi yaptıklarını birbirine gösterdi. Sonra Niloya ile dedesi yeni şekiller denemeye mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hamur tek bir taneydi"
   - Cümle 3: «Dedesi de hamurla oynamak istedi, ama hamur tek bir taneydi.»
   - Açıklama: Hamur için 'tane' uygun değil; 'hamur bir tane/tek parçaydı' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya neşeli bir şarkı söyledi"
   - Cümle 8: «Hamurla oynarken Niloya neşeli bir şarkı söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümüne katkı vermiyor, yalnız süs olarak geçiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hamurla oynarken Niloya neşeli bir şarkı söyledi"
   - Cümle 8: «Hamurla oynarken Niloya neşeli bir şarkı söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği süs olarak geçiyor, hamur sorununun çözümünde işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hamurla oynarken Niloya neşeli bir şarkı söyledi"
   - Cümle 8: «Hamurla oynarken Niloya neşeli bir şarkı söyledi.»
   - Açıklama: Şarkı bölümü sorun ve çözümle ilgisiz, olaydan çıkmayan işlevsiz bir ayrıntı.
   - Açıklama: Şarkı sorunla ya da çözümle ilgisiz, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0064` birebir aynı, `@degisim: bilgili -> yeşil` (tutuyorsan), ardından `@onarim: f65decf06a4262d4f2c8d51d77b7369868be7e8e`, sonra gövde.

### Hikâye 7: tohum niloya-0066 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0066
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'çatal', fiil 'içmek', sıfat 'şık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: tek dal vardı ve ikisi aynı anda söyledi | sırayla söylemeyi önerip dalı ağabeyine verdi
@tohum: niloya-0066
@degisim: şık -> neşeli
Ormanda kuşlar ötüyordu. Niloya ile Murat neşeli bir şarkı oyunu oynuyordu. Mikrofon olarak çatal bir dal kullanıyorlardı. Ama dal bir taneydi ve ikisi de aynı anda söylemek istedi. Sesleri birbirine karıştı ve şarkı bozuldu. Niloya biraz düşündü ve sırayla söylemeyi önerdi. Önce Niloya dalı tuttu ve fındık şarkısını söyledi. Murat onu dinledi ve alkışladı. Şarkı bitince Niloya dalı Murat'a verdi ve şişesinden su içti. Bu sefer Murat top şarkısını söyledi. Niloya da ağabeyini sevinçle dinledi. Niloya ile Murat çok mutluydu, çünkü sırayla söyleyince şarkılar güzel olmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ikisi aynı anda söyledi"
   - Cümle 0 (plan satırı): «tek dal vardı ve ikisi aynı anda söyledi | sırayla söylemeyi önerip dalı ağabeyine verdi»
   - Açıklama: Nesnesiz 'söyledi' şarkı söylemeyi değil bir şey demeyi anlatıyor; 'şarkı söyledi' olmalı.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Mikrofon olarak çatal bir dal"
   - Cümle 3: «Mikrofon olarak çatal bir dal kullanıyorlardı.»
   - Açıklama: Mikrofon kartın köy dünyasında olmayan çağdaş bir teknoloji eşyası olarak anılıyor.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Mikrofon olarak çatal bir dal kullanıyorlardı"
   - Cümle 3: «Mikrofon olarak çatal bir dal kullanıyorlardı.»
   - Açıklama: Mikrofon kartın köy dünyasında olmayan çağdaş bir teknoloji eşyasıdır (tohum yasak kategorileri: teknoloji).
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şişesinden su içti"
   - Cümle 9: «Şarkı bitince Niloya dalı Murat'a verdi ve şişesinden su içti.»
   - Açıklama: Su şişesi sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0066` birebir aynı, `@degisim: şık -> neşeli` (tutuyorsan), ardından `@onarim: fdb40a28ce297507f24e0d80e1cb60946337aa1a`, sonra gövde.

### Hikâye 8: tohum niloya-0068 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | babaannesi
@tohum: niloya-0068
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babaannesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'küp', fiil 'oturmak', sıfat 'kokulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | babaannesi
@plan: güzel bir koku geldi ama nereden geldiği belli değildi | babaannesine sordu ve çimenlerde kekikleri buldu
@tohum: niloya-0068
@degisim: küp -> sepet
Tepelerde hafif bir rüzgar esiyordu. Niloya ile babaannesi yaylada boş bir sepetin yanına oturdu. Birden rüzgarla güzel bir koku geldi, ama Niloya onu neyin yaptığını bilmiyordu. "Babaanne, bu koku nereden geliyor?" diye sordu Niloya. "Etrafa bak, belki sen bulursun," dedi babaannesi. Niloya kalktı ve çimenlerin arasına eğilip baktı. Taşların yanında küçük mor çiçekli bitkiler buldu. Yapraklarından o güzel koku geliyordu. "Bunlar kokulu kekikler, çorbaya koyarız," dedi babaannesi. Niloya birkaç dal kekik kopardı ve sepete koydu. Niloya çok sevindi, çünkü o güzel kokuyu yapan bitkiyi bulmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya onu neyin yaptığını bilmiyordu"
   - Cümle 3: «Birden rüzgarla güzel bir koku geldi, ama Niloya onu neyin yaptığını bilmiyordu.»
   - Açıklama: Koku yapılmaz; 'yapmak' fiili kokuya uygun değil, 'neyin koktuğunu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onu neyin yaptığını bilmiyordu"
   - Cümle 3: «Birden rüzgarla güzel bir koku geldi, ama Niloya onu neyin yaptığını bilmiyordu.»
   - Açıklama: Koku 'yapılmaz'; 'kokunun nereden geldiğini' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "o güzel kokuyu yapan bitkiyi"
   - Cümle 11: «Niloya çok sevindi, çünkü o güzel kokuyu yapan bitkiyi bulmuştu.»
   - Açıklama: Kokuyu 'yapan' bitki yanlış fiil; 'o güzel kokan bitkiyi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0068` birebir aynı, `@degisim: küp -> sepet` (tutuyorsan), ardından `@onarim: 2434cb880302d4ed8462774175e95e49edd67f7d`, sonra gövde.

### Hikâye 9: tohum niloya-0070 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0070
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'bot', fiil 'zıplamak', sıfat 'tuzlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: botu ayağından çıktı ve yaprakların arasında kayboldu | dağılmış yaprakları açıp botunu buldu
@tohum: niloya-0070
@degisim: tuzlu -> kırmızı
Niloya ormanda kuru yaprakların üstünde zıplıyordu. Birden sağ botu ayağından çıktı ve uzağa fırladı. Bot yaprakların arasına düştü ve kayboldu. Niloya tek ayağıyla durdu ve etrafına baktı. Yerde bir sürü sarı yaprak vardı, ama bot görünmüyordu. Niloya'nın aklına bir soru geldi: Bot nereye düşmüştü? Niloya önündeki yapraklara dikkatle baktı. Bir yerde yapraklar dağılmıştı. Niloya oradaki yaprakları elleriyle yavaşça açtı. Kırmızı botu yaprakların altında duruyordu. Niloya botu ayağına giydi ve bağcıklarını sıkıca bağladı. Niloya çok sevindi, çünkü kaybolan botunu bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına bir soru geldi"
   - Cümle 6: «Niloya'nın aklına bir soru geldi: Bot nereye düşmüştü?»
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım, küçük çocuğa uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oradaki yaprakları elleriyle yavaşça açtı"
   - Cümle 9: «Niloya oradaki yaprakları elleriyle yavaşça açtı.»
   - Açıklama: Yapraklar açılmaz; 'kenara itti' ya da 'araladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0070` birebir aynı, `@degisim: tuzlu -> kırmızı` (tutuyorsan), ardından `@onarim: e11508c0e94ba0aa24838517a4011b38401767a1`, sonra gövde.

### Hikâye 10: tohum niloya-0072 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0072
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'testi', fiil 'yaratmak', sıfat 'yumuşacık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: yakından ince ve uzun bir ses geldi | sesin rüzgarla testiden çıktığını buldu
@tohum: niloya-0072
@degisim: yaratmak -> üflemek
Bir sabah Niloya yaylada yumuşacık çimenlere oturdu. Su testisini de yanına koydu. Birden yakından ince ve uzun bir ses geldi. Niloya etrafına baktı ama sesi neyin yaptığını göremedi. Niloya'nın aklına bir soru geldi: Bu ses nereden geliyordu? Sonra rüzgar durdu ve ses de kesildi. Rüzgar tekrar esince ses geri geldi. Niloya kulağını testiye yaklaştırdı. Ses testiden geliyordu! Rüzgar testinin ağzına esince bu ses çıkıyordu. Niloya da testiye üfledi ve aynı sesi kendisi yaptı. Sonra Niloya rüzgarla birlikte testiden sesler çıkarmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi neyin yaptığını göremedi"
   - Cümle 4: «Niloya etrafına baktı ama sesi neyin yaptığını göremedi.»
   - Açıklama: Ses 'yapılmaz', 'çıkarılır'; fiil nesnesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına bir soru geldi"
   - Cümle 5: «Niloya'nın aklına bir soru geldi: Bu ses nereden geliyordu?»
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım.
   - Açıklama: 'Aklına soru gelmek' deyimsel bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0072` birebir aynı, `@degisim: yaratmak -> üflemek` (tutuyorsan), ardından `@onarim: d7da5a443b50293205fe27155804c5057669a534`, sonra gövde.

### Hikâye 11: tohum niloya-0073 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0073
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'halka', fiil 'sürmek', sıfat 'sevimli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: halka belinde dönmedi ve hep yere düştü | şarkı söyleyip belini yavaşça salladı
@tohum: niloya-0073
@degisim: sevimli -> renkli
Bir sabah Niloya yaylaya büyük renkli bir halka getirdi. Halkayı belinde çevirmeyi ilk kez deneyecekti. Ama halka hemen yere düştü, çünkü Niloya belini çok hızlı sallıyordu. Niloya halkayı yerden aldı ve biraz düşündü. Sonra neşeli bir şarkı söylemeye başladı. Belini şarkının sesine göre yavaş yavaş salladı. Bu sefer halka düşmedi ve Niloya'nın etrafında döndü. Şarkı uzun sürdü ve halka da o kadar döndü. Niloya şarkı bitene kadar hiç durmadı. Niloya çok sevindi, çünkü halkayı çevirmeyi sonunda öğrenmişti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "halka da o kadar döndü"
   - Cümle 8: «Şarkı uzun sürdü ve halka da o kadar döndü.»
   - Açıklama: 'O kadar' neyin ölçüsü olduğunu söylemiyor; 'o kadar uzun döndü' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "halka da o kadar döndü"
   - Cümle 8: «Şarkı uzun sürdü ve halka da o kadar döndü.»
   - Açıklama: 'O kadar döndü' anlamca belirsiz; 'o kadar uzun döndü' kastediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0073` birebir aynı, `@degisim: sevimli -> renkli` (tutuyorsan), ardından `@onarim: 5eeefebe35ac9cfee98700b41b7cd0c3e9f13ee1`, sonra gövde.
