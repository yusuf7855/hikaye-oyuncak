# Editör görevi (onarım): Niloya, onarım partisi 21

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar21.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0054 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Tospik
@tohum: niloya-0054
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'alet', fiil 'fırçalamak', sıfat 'devasa'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Tospik
@plan: kaplumbağa yavaş olduğu için hiç fındık bulamadı | fındıklarının yarısını ona ayırıp şarkıyla onu uyandırdı
@tohum: niloya-0054
@degisim: devasa -> kocaman
Bir sabah Niloya ile Tospik ormanda fındık topluyordu. Niloya'nın sepeti çabucak doldu. Ama Tospik çok yavaştı ve hiç fındık bulamadı. Tospik yoruldu ve kocaman bir elma ağacının altında uyudu. Niloya fındıklarının yarısını Tospik'e vermek istedi. Sepetinden küçük bir alet çıkardı ve fındıkların toprağını fırçaladı. Sonra fındıkları Tospik'in yanına koydu. Tospik'i uyandırmak için yavaş ve neşeli bir şarkı söyledi. Tospik şarkıyı duydu ve gözlerini açtı. "Tospik, bu fındıklar senin," dedi Niloya. "Teşekkür ederim, Niloya," dedi Tospik. Niloya bundan sonra topladığı fındıkları hep Tospik'le paylaştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "fındıkların toprağını fırçaladı"
   - Cümle 6: «Sepetinden küçük bir alet çıkardı ve fındıkların toprağını fırçaladı.»
   - Açıklama: 'Fındıkların toprağı' yanlış kullanım; fındıkların üstündeki toprağı fırçaladı olmalı.
   - Açıklama: Fındığın toprağı olmaz; 'fındıklardaki toprağı' anlamı yanlış kelimeyle kurulmuş.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Sepetinden küçük bir alet çıkardı"
   - Cümle 6: «Sepetinden küçük bir alet çıkardı ve fındıkların toprağını fırçaladı.»
   - Açıklama: Kartta Niloya'ya ait böyle bir alet ya da eşya yok; kapalı dünyaya dışarıdan bir eşya ekleniyor.
   - Açıklama: Kartta tanımlanmayan belirsiz bir alet eşya olarak kapalı dünyaya ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepetinden küçük bir alet çıkardı"
   - Cümle 6: «Sepetinden küçük bir alet çıkardı ve fındıkların toprağını fırçaladı.»
   - Açıklama: Alet sebepsiz beliriyor ve fındıkları fırçalamak sorunun çözümüne hiçbir şey katmıyor.
   - Açıklama: Alet sebepsiz beliriyor ve fırçalama ayrıntısı çözüme hiçbir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0054` birebir aynı, `@degisim: devasa -> kocaman` (tutuyorsan), ardından `@onarim: 168a9d68da3ced354fcdf08f89356bcec875611a`, sonra gövde.

### Hikâye 2: tohum niloya-0060 (deneme 4 -> 5)

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
@plan: çiçeklerin yanından bilinmeyen bir ses geldi | başını kaldırıp çiçeklerden düşen çekirdekleri gördü
@tohum: niloya-0060
@degisim: ekşi -> kuru
Bir sabah Niloya evin bahçesinde oynuyordu. Birden çiçeklerin yanından küçük bir ses geldi. Niloya'nın aklında bir soru vardı: Ses yerden mi çıkıyordu? Niloya çiçeklerin yanına yavaşça yürüdü. Yerdeki kuru yaprakları elleriyle karıştırdı. Ama yaprakların altında hiçbir şey yoktu. Sonra başını kaldırıp büyük sarı çiçeklere baktı. Rüzgar esince çiçeklerin başları sallanıyordu. Çiçeklerden küçük siyah çekirdekler düşüyordu. Çekirdekler yapraklara değince tık tık diye ses çıkarıyordu. Niloya çok sevindi, çünkü o küçük sesi yapan şeyi bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "aklında bir soru vardı"
   - Cümle 3: «Niloya'nın aklında bir soru vardı: Ses yerden mi çıkıyordu?»
   - Açıklama: 'Aklında bir soru olmak' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklında bir soru vardı"
   - Cümle 3: «Niloya'nın aklında bir soru vardı: Ses yerden mi çıkıyordu?»
   - Açıklama: 'Aklında bir soru vardı' deyimsel ve soyut bir anlatım.
   - Açıklama: 'Aklında bir soru vardı' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0060` birebir aynı, `@degisim: ekşi -> kuru` (tutuyorsan), ardından `@onarim: ce792f0d93b4f9b4f7285b2d23bd1a01609f7693`, sonra gövde.

### Hikâye 3: tohum niloya-0063 (deneme 4 -> 5)

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
Yağmur pencereye tıp tıp vuruyordu. Niloya bir tabağa üzüm koymuştu ve bahçede piknik yapmak istiyordu. Ama yağmur yüzünden bahçeye çıkamadı. Niloya pencereden dışarı baktı ve biraz üzüldü. Sonra piknik örtüsünü odanın ortasına yaydı. Örtünün bir ucunu elleriyle düzeltti. Üzüm tabağını da örtünün üstüne bıraktı. Yağmurun sesi odaya kadar geliyordu. Niloya bahçede söylediği neşeli şarkıyı odada da söyledi. Şarkı söylerken üzümlerini tek tek yedi. Evdeki piknik de çok eğlenceli oldu. Niloya çok sevinçliydi, çünkü yağmurlu günde de pikniğini yapmıştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya bahçede söylediği neşeli şarkıyı"
   - Cümle 9: «Niloya bahçede söylediği neşeli şarkıyı odada da söyledi.»
   - Açıklama: Niloya bahçeye hiç çıkamadığı için 'bahçede söylediği' ifadesi anlamca yanlış; zaman kipi olaya uymuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya bahçede söylediği neşeli şarkıyı odada da söyledi"
   - Cümle 9: «Niloya bahçede söylediği neşeli şarkıyı odada da söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümüne katkı vermiyor, yalnız süs olarak geçiyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bahçede söylediği neşeli şarkıyı odada da söyledi"
   - Cümle 9: «Niloya bahçede söylediği neşeli şarkıyı odada da söyledi.»
   - Açıklama: Niloya bahçeye hiç çıkamadığı halde bahçede şarkı söylemiş gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0063` birebir aynı, ardından `@onarim: 36d2d190dac9dc8f69421cf19630f75053165a41`, sonra gövde.

### Hikâye 4: tohum niloya-0071 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0071
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: sırayla oynamak
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'defter', fiil 'gezinmek', sıfat 'mor'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: kaplumbağa yavaş olduğu için hiç çiçek bulamadı | sırayla aradılar ve şarkıyla sırayı değiştirdiler
@tohum: niloya-0071
Bir sabah Niloya ile Tospik yeşil tepede çiçek arıyordu. Niloya mor çiçekleri defterinin arasına koymak istiyordu. Ama Tospik çok yavaştı ve çiçeklere hep Niloya önce ulaştı. Tospik hiç çiçek bulamadı ve başını kabuğuna çekti. Niloya bunu gördü ve sırayla aramayı önerdi. Sonra kısa bir şarkı söyledi. Şarkı bitene kadar yalnız Tospik otların arasında gezindi. Tospik yavaş yavaş yürüdü ve büyük, mor bir çiçek buldu. Niloya çiçeği defterin ilk sayfasına koydu. Sonra sıra Niloya'ya geçti ve Tospik bekledi. Defterin sayfaları çiçeklerle doldu. Niloya ile Tospik çok mutluydu, çünkü ikisi de çiçek bulmuştu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "hep Niloya önce ulaştı"
   - Cümle 3: «Ama Tospik çok yavaştı ve çiçeklere hep Niloya önce ulaştı.»
   - Açıklama: Söz dizimi ve görünüş bozuk; 'hep önce Niloya ulaşıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0071` birebir aynı, ardından `@onarim: 850456fcd3e0532a0a7cbceae277ede6aec1ae2c`, sonra gövde.

### Hikâye 5: tohum niloya-0075 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | annesi
@tohum: niloya-0075
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'elbise', fiil 'eklemek', sıfat 'cesur'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | annesi
@plan: annesinin sakladığı hazineyi hiçbir yerde bulamadı | annesinden yardım istedi ve hazineyi elbisenin cebinde buldu
@tohum: niloya-0075
@degisim: cesur -> mavi
Yağmur pencereye tıp tıp vuruyordu. Niloya evde annesiyle hazine oyunu oynuyordu. Annesi odada bir hazine saklamıştı ama Niloya onu hiçbir yerde bulamadı. "Anneciğim, bana biraz yardım eder misin?" dedi Niloya. Annesi gülümsedi ve bir şey daha ekledi. "Hazine mavi bir cepte duruyor," dedi annesi. Niloya odaya merakla yeniden baktı. Sandalyenin üstünde mavi elbisesini gördü. Elbisenin cebine elini soktu. Cepte bir kurabiye vardı! Niloya kurabiyeyi ikiye böldü. Yarısını annesine verdi. Niloya çok sevindi, çünkü hazineyi sonunda kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gülümsedi ve bir şey daha ekledi"
   - Cümle 5: «Annesi gülümsedi ve bir şey daha ekledi.»
   - Açıklama: Annesi daha önce bir şey söylemediği için 'bir şey daha ekledi' yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir şey daha ekledi"
   - Cümle 5: «Annesi gülümsedi ve bir şey daha ekledi.»
   - Açıklama: Anne daha önce bir şey söylemediği için 'daha ekledi' yanlış anlamda; 'bir ipucu verdi' olmalı.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Annesi gülümsedi ve bir şey daha ekledi"
   - Cümle 5: «Annesi gülümsedi ve bir şey daha ekledi.»
   - Açıklama: Annesi daha önce hiçbir şey söylemediği halde bir şey daha eklediği söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0075` birebir aynı, `@degisim: cesur -> mavi` (tutuyorsan), ardından `@onarim: 868a5150eba79a34930823e5fb710a0470529cd9`, sonra gövde.

### Hikâye 6: tohum niloya-0076 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | dedesi
@tohum: niloya-0076
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: dedesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'damga', fiil 'karışmak', sıfat 'peynirli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | dedesi
@plan: sofrayı süslemek için ortada hiç çiçek görünmüyordu | taşın arkasına bakıp sarı çiçekler buldu
@tohum: niloya-0076
@degisim: damga -> börek
Bir sabah Niloya dedesiyle yeşil tepeye çıktı. Niloya dedesine sürpriz bir sofra hazırlamak istedi. Ama sofrayı süslemek için ortada hiç çiçek görünmüyordu. Dede biraz ileride kekik topluyordu. Niloya çimenlere bir örtü serdi ve sepetteki peynirli böreği koydu. Niloya merakla büyük bir taşın arkasına baktı. Orada kekiklerin arasına karışmış sarı çiçekler buldu. Birkaç çiçek topladı ve böreğin yanına koydu. "Dedeciğim, gel, sana bir sürprizim var!" dedi Niloya. Dede geldi ve süslü sofrayı gördü. "Ne güzel bir sofra, teşekkürler, Niloya," dedi dede. İkisi böreği birlikte yedi. Niloya çok mutluydu, çünkü dedesini sevindirmişti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ortada hiç çiçek görünmüyordu"
   - Cümle 3: «Ama sofrayı süslemek için ortada hiç çiçek görünmüyordu.»
   - Açıklama: Çiçek olmamasının sebebi söylenmiyor ve sorun çok zayıf kalıyor.
   - Açıklama: Çiçeklerin neden görünmediği söylenmiyor; sorunun sebebi verilmiyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sepetteki peynirli böreği koydu"
   - Cümle 5: «Niloya çimenlere bir örtü serdi ve sepetteki peynirli böreği koydu.»
   - Açıklama: 'Koydu' fiilinin yönelme tümleci eksik; 'örtüye koydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0076` birebir aynı, `@degisim: damga -> börek` (tutuyorsan), ardından `@onarim: 5b7f4b70680e49560b30919fe25214906173b659`, sonra gövde.

### Hikâye 7: tohum niloya-0077 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0077
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'toprak', fiil 'dolmak', sıfat 'yuvarlak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: yakında az kekik vardı ve sepet dolmadı | güzel kokunun geldiği yere gidip çok kekik buldu
@tohum: niloya-0077
Niloya yeşil tepede kekik topluyordu. Yuvarlak sepetini kekikle doldurmak istiyordu. Ama yakında az kekik vardı ve sepet dolmadı. Birden rüzgar esti ve güzel bir koku getirdi. Niloya bu kokunun nereden geldiğini çok merak etti. Kokunun geldiği yöne yavaş yavaş yürüdü. Büyük bir taşın arkasına baktı. Orada yumuşak toprakta bir sürü kekik vardı. Koku bu kekiklerden geliyordu! Niloya kekikleri tek tek topladı. Sonunda sepet kekikle doldu. Niloya çok sevindi, çünkü sepeti sonunda kekikle dolmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden rüzgar esti ve güzel bir koku getirdi"
   - Cümle 4: «Birden rüzgar esti ve güzel bir koku getirdi.»
   - Açıklama: Çözümü tam gereken anda sebepsizce esen rüzgar getiriyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "sepeti sonunda kekikle dolmuştu"
   - Cümle 12: «Niloya çok sevindi, çünkü sepeti sonunda kekikle dolmuştu.»
   - Açıklama: Bir önceki cümledeki 'Sonunda sepet kekikle doldu' bilgisi gereksiz yere tekrarlanıyor.
   - Açıklama: Sepetin kekikle dolduğu bir önceki cümlede söylenmişken son cümlede aynen tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0077` birebir aynı, ardından `@onarim: cd010f0ff3629f963a5705387cb5d8771aebba42`, sonra gövde.

### Hikâye 8: tohum niloya-0078 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Murat
@tohum: niloya-0078
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'kum', fiil 'oynatmak', sıfat 'yumuşak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | dağ | Murat
@plan: ip hep ağabeyinin ayağına takıldı çünkü çok hızlı atlıyordu | yavaş bir şarkı söyledi ve ağabeyi şarkıya göre atladı
@tohum: niloya-0078
@degisim: kum -> ip
Bir sabah Niloya ile Murat yeşil tepeye çıktı. Murat yumuşak çimenlerde ip atlamak istiyordu. Ama ip hep ayağına takıldı, çünkü Murat çok hızlı atlıyordu. Murat yere oturdu ve üzgünce ipe baktı. "Murat, sen şarkıya göre yavaşça atla," dedi Niloya. Niloya başını sağa sola oynattı ve yavaş bir şarkı söyledi. Murat şarkıyı dinleyerek zıpladı. Bu kez ip ayağına hiç takılmadı. Murat on kez, sonra yirmi kez atladı. Niloya güldü ve ellerini çırptı. Murat ipi bıraktı ve Niloya'ya sarıldı. "Şarkın sayesinde atlamak çok kolay, Niloya!" dedi Murat sevinçle.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şarkın sayesinde atlamak"
   - Cümle 12: «"Şarkın sayesinde atlamak çok kolay, Niloya!" dedi Murat sevinçle.»
   - Açıklama: 'Sayesinde' soyut bir ilgeç; 3 yaşındaki bir çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0078` birebir aynı, `@degisim: kum -> ip` (tutuyorsan), ardından `@onarim: d286af832e56b2f8cafdbd067e2d1c02ea0afb3a`, sonra gövde.

### Hikâye 9: tohum niloya-0079 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0079
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'reçel', fiil 'tutmak', sıfat 'güneşli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: ikisi de acıktı ama sepette tek bir ekmek vardı | ekmeği paylaştı ve bulduğu kirazları da verdi
@tohum: niloya-0079
Hava çok güneşliydi. Niloya ile babaannesi fındık topluyordu ve ikisi de acıktı. Ama sepette tek dilim reçelli ekmek vardı. "Babaanne, bu ekmeği ikimiz paylaşalım," dedi Niloya. Babaanne ekmeği ikiye böldü ve yarısını ona verdi. Sonra Niloya ağaçların arasına merakla baktı. Yere yakın bir dalda kırmızı kirazlar gördü. Eteğini tuttu ve kirazları içine topladı. Kirazların yarısını da babaannesine verdi. Babaanne kirazları yedi ve güldü. "İkimiz de doyduk, Niloya," dedi babaanne. "Afiyet olsun, babaanneciğim!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yere yakın bir dalda kırmızı kirazlar gördü"
   - Cümle 7: «Yere yakın bir dalda kırmızı kirazlar gördü.»
   - Açıklama: Kirazlar sebepsizce beliriyor ve açlık sorununu kolayca çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0079` birebir aynı, ardından `@onarim: c15a684e5d7dfe28fa10f8c007b738bd62ab0f57`, sonra gövde.

### Hikâye 10: tohum niloya-0082 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0082
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'boncuk', fiil 'değmek', sıfat 'şapkalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: tomurcuk kapalıydı ve içi görünmüyordu | güneşin gelmesini bekledi ve açılan çiçeği gördü
@tohum: niloya-0082
@degisim: şapkalı -> mor
Yeşil tepede güneş yeni doğuyordu. Niloya kekiklerin yanında küçük bir tomurcuk buldu. Onun içini görmek istedi ama tomurcuk sımsıkı kapalıydı. Üstünde boncuk gibi su damlaları vardı. Tomurcuk neden açılmıyordu? Niloya bu soruyu düşündü ve çevreye baktı. Onun üstüne daha güneş ışığı gelmemişti. Niloya ona hiç dokunmadı. Çimenlere oturdu ve ona baktı. Sonra güneş yükseldi ve ışığı çiçeğe değdi. Su damlaları yavaş yavaş kurudu. Sonunda tomurcuk açıldı. İçinden mor yapraklar çıktı. Niloya bundan sonra kapalı tomurcukları zorla açmadı, bekledi.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun üstüne daha güneş"
   - Cümle 7: «Onun üstüne daha güneş ışığı gelmemişti.»
   - Açıklama: Önceki cümlenin öznesi Niloya olduğu için 'onun' zamirinin tomurcuğu mu Niloya'yı mı gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun üstüne daha güneş ışığı gelmemişti"
   - Cümle 7: «Onun üstüne daha güneş ışığı gelmemişti.»
   - Açıklama: Önceki cümlenin öznesi Niloya olduğu için 'Onun' zamirinin tomurcuğu gösterdiği belli değil.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Niloya bundan sonra kapalı tomurcukları zorla açmadı"
   - Cümle 14: «Niloya bundan sonra kapalı tomurcukları zorla açmadı, bekledi.»
   - Açıklama: Niloya hiç zorlamayı denemediği için ders yaşanan olaydan çıkmıyor ve kapanış sıcak değil.
   - Açıklama: Niloya hiç zorla açmaya çalışmadığı için ders yaşanan olaydan çıkmıyor ve sıcak bir kapanış yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0082` birebir aynı, `@degisim: şapkalı -> mor` (tutuyorsan), ardından `@onarim: 6bb7d14f58d43049b7ba3f38b99cbafc84b315fe`, sonra gövde.

### Hikâye 11: tohum niloya-0083 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0083
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'yama', fiil 'dikmek', sıfat 'kirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: toprak yumuşaktı ve dal hep yere düştü | sert bir toprak bulup dalı oraya dikti
@tohum: niloya-0083
@degisim: yama -> dal
Ormanda Niloya ile babaannesi fındık ağaçlarının altında oyun oynuyordu. Babaanne ince bir dalı toprağa koymuştu ve sırayla dala fındık atıyorlardı. Ama toprak çok yumuşaktı, bu yüzden fındık değince dal hep yere düştü. "Böyle oynayamayız," dedi babaannesi. Niloya etrafa merakla baktı. Büyük bir taşın yanında sert bir toprak buldu. Dalı oraya götürdü ve toprağa sıkıca dikti. Elleri biraz kirli olmuştu ama dal artık hiç sallanmıyordu. Babaannesi ilk fındığı attı ve fındık dala değdi. Bu sefer dal yere düşmedi. Niloya sevinçle ellerini çırptı. "Sıra sende, Niloya, dalımız artık hiç düşmüyor!" dedi babaannesi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elleri biraz kirli olmuştu"
   - Cümle 8: «Elleri biraz kirli olmuştu ama dal artık hiç sallanmıyordu.»
   - Açıklama: Ellerin kirlenmesi hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0083` birebir aynı, `@degisim: yama -> dal` (tutuyorsan), ardından `@onarim: 0161405c7d02b674ce2946f39860e0ebe6c92535`, sonra gövde.

### Hikâye 12: tohum niloya-0084 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0084
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'çekmece', fiil 'yedirmek', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | -
@plan: parkta değişik bir çın çın sesi duyuldu | sesi aradı ve çekmecede oyuncak saati buldu
@tohum: niloya-0084
@degisim: yedirmek -> susmak
Bir sabah Niloya parkta kaydıraktan kayıyordu. Birden değişik bir çın çın sesi duydu. Niloya bu sesin nereden geldiğini çok merak etti. Önce kaydırağın altına baktı ama orada bir şey yoktu. Sonra sese doğru yavaşça yürüdü. Ses, parktaki oyuncak mutfaktan geliyordu. Niloya mutfağın küçük çekmecesini açtı. Çekmecede kırmızı bir oyuncak saat vardı. Saat çın çın diye çalıyordu. Niloya saatin düğmesine bastı ve saat sustu. Sonra saati yine çekmeceye koydu ve güldü. Niloya bundan sonra bir ses duyunca çekmeceleri de açıp baktı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden değişik bir çın çın sesi duydu"
   - Cümle 2: «Birden değişik bir çın çın sesi duydu.»
   - Açıklama: Bir ses duymak gerçek bir sorun değil; sebebi olan, çocuğun önemseyeceği bir sorun kurulmuyor.
   - Açıklama: Sorun yalnız bir ses ve oyuncak saatin parktaki çekmecede neden çaldığı hiç söylenmiyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Niloya bundan sonra bir ses duyunca çekmeceleri de açıp baktı"
   - Cümle 12: «Niloya bundan sonra bir ses duyunca çekmeceleri de açıp baktı.»
   - Açıklama: Son cümle olaydan doğal çıkmayan tuhaf bir genelleme; sıcak ve doyurucu bir kapanış vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0084` birebir aynı, `@degisim: yedirmek -> susmak` (tutuyorsan), ardından `@onarim: 040c71661f6e3e9d0eaa0e94624a95e08791d497`, sonra gövde.
