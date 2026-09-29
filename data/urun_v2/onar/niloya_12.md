# Editör görevi (onarım): Niloya, onarım partisi 12

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar12.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar12.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0031 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Murat
@tohum: niloya-0031
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: paylaşmak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'kızak', fiil 'katılmak', sıfat 'yardımsever'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | Murat
@plan: rüzgar ağabeyinin sepetindeki kekikleri uçurdu | kendi kekiklerinin yarısını ona verdi
@tohum: niloya-0031
@degisim: kızak -> sepet
Niloya ile Murat yeşil tepede kekik topluyordu. Birden güçlü bir rüzgar esti ve Murat'ın sepeti devrildi. Sepetteki kekikler rüzgarla uçup gitti. Murat boş sepetine baktı ve üzüldü. Niloya ağabeyini güldürmek için neşeli bir şarkı söyledi. Murat biraz gülümsedi ve şarkıya katıldı. Sonra Niloya kendi dolu sepetine baktı. Kekiklerinin yarısını Murat'ın sepetine koydu. "Al, abi, yarısı senin," dedi Niloya. "Sen çok yardımseversin, Niloya!" dedi Murat. Niloya ile Murat tepede mutlu mutlu kekik toplamaya devam etti.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Niloya ağabeyini güldürmek için neşeli bir şarkı söyledi"
   - Cümle 5: «Niloya ağabeyini güldürmek için neşeli bir şarkı söyledi.»
   - Açıklama: Çözüm önce sebebe yönelmeyen bir şarkıyla dolaşıyor, kekik paylaşımı sonra geliyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya ağabeyini güldürmek için neşeli bir şarkı söyledi"
   - Cümle 5: «Niloya ağabeyini güldürmek için neşeli bir şarkı söyledi.»
   - Açıklama: Şarkı sorunu çözmüyor ve çözüme yol açmıyor; işlevsiz bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0031` birebir aynı, `@degisim: kızak -> sepet` (tutuyorsan), ardından `@onarim: 646ebb1ac78abaf70cdec3ef84ffe35e097d80ea`, sonra gövde.

### Hikâye 2: tohum niloya-0032 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | annesi
@tohum: niloya-0032
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'zambak', fiil 'sıçratmak', sıfat 'tekerlekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | annesi
@plan: bir ağacın yanından bilinmeyen bir ses geldi | yavaşça bakıp sesi yapan damlaları buldu
@tohum: niloya-0032
@degisim: zambak -> ağaç
Niloya annesiyle ormanda meyve toplayıp tekerlekli sepetlerine koyuyordu. Birden büyük bir fındık ağacının yanından küçük bir ses geldi. Niloya bu sesi çok merak etti. "Anne, şu sese bakacağım," dedi Niloya. Annesi başını salladı ve onun arkasından yürüdü. Niloya yavaşça ağaca yaklaştı ve alçak dalların altına baktı. Orada küçük bir su birikintisi vardı. Ağacın yeşil yapraklarından birikintiye damlalar düşüyordu. Her damla suyu biraz sıçratıyor ve o sesi yapıyordu. "Ses yağmurdan kalan damlalardan geliyor, anne!" dedi Niloya. Annesi gülümsedi ve "Doğru buldun," dedi. Sonra Niloya ile annesi meyve toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "tekerlekli sepetlerine koyuyordu"
   - Cümle 1: «Niloya annesiyle ormanda meyve toplayıp tekerlekli sepetlerine koyuyordu.»
   - Açıklama: Kartın köy dünyasında tekerlekli sepet gibi bir eşya yok; kapalı dünyaya aykırı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve o sesi yapıyordu"
   - Cümle 9: «Her damla suyu biraz sıçratıyor ve o sesi yapıyordu.»
   - Açıklama: Doğru eşdizim 'ses çıkarmak'tır, 'ses yapmak' değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0032` birebir aynı, `@degisim: zambak -> ağaç` (tutuyorsan), ardından `@onarim: 04d4645b97987e963bc48764cd0d1ef120878b6e`, sonra gövde.

### Hikâye 3: tohum niloya-0037 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0037
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'gül', fiil 'paylaşmak', sıfat 'plastik'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: rüzgarın getirdiği poşet güllerin üstüne takıldı | poşete dikkatle bakıp ucundan yavaşça çekti
@tohum: niloya-0037
@degisim: paylaşmak -> katlamak
Ormanda kuşlar ötüyordu. Niloya fındık ağaçlarının yanında güzel kırmızı güller gördü. Ama rüzgarın getirdiği plastik bir poşet güllerin üstüne takılmıştı. Poşet çiçeklerin çoğunu kapatıyordu. Niloya güllerin hepsini görmek istedi. Niloya merakla güllerin etrafında dolaştı ve dikkatle baktı. Poşet yalnız bir ucundan takılmıştı. Niloya öbür ucunu tuttu ve onu yavaşça çekip çıkardı. Hiçbir çiçek ezilmedi. Sonra poşeti küçük küçük katladı ve cebine koydu. Niloya çok sevindi, çünkü bütün kırmızı güller yeniden görünüyordu.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onu yavaşça çekip çıkardı"
   - Cümle 8: «Niloya öbür ucunu tuttu ve onu yavaşça çekip çıkardı.»
   - Açıklama: 'Onu' zamiri poşeti mi öbür ucu mu gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0037` birebir aynı, `@degisim: paylaşmak -> katlamak` (tutuyorsan), ardından `@onarim: 653167f3ad09ae1735d3c87638e0713a10a5f17a`, sonra gövde.

### Hikâye 4: tohum niloya-0038 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Mete
@tohum: niloya-0038
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'nilüfer', fiil 'gıdıklamak', sıfat 'güçlü'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | park | Mete
@plan: tek salıncak vardı ve ikisi de binmek istedi | bir şarkı bitince sırayı değiştirmeyi önerdi
@tohum: niloya-0038
@degisim: nilüfer -> salıncak
Bir sabah Niloya ile Mete parka geldi. Parkta yalnız bir salıncak vardı ve ikisi de binmek istedi. Aynı anda salıncağa koştular. "Sırayla binelim, Mete, önce sen bin, şarkı bitince de ben," dedi Niloya. Mete sevindi ve ilk o oturdu. Niloya onu hafifçe itti ve güçlü bir sesle neşeli bir şarkı söyledi. Şarkı bitince Mete hemen indi. "Sıra sende, Niloya," dedi Mete. Bu kez Mete salıncağı yavaş yavaş itti. Salıncak durunca Mete Niloya'yı gıdıkladı ve ikisi de güldü. "Bu şarkı oyunu çok güzel, Mete, yine oynayalım!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Salıncak durunca Mete Niloya'yı gıdıkladı"
   - Cümle 10: «Salıncak durunca Mete Niloya'yı gıdıkladı ve ikisi de güldü.»
   - Açıklama: Niloya'nın sırasında şarkı kuralı kullanılmıyor, sıra salıncak durunca bitiyor ve gıdıklama sebepsizce ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0038` birebir aynı, `@degisim: nilüfer -> salıncak` (tutuyorsan), ardından `@onarim: 2f9612f0cde6cf49d8493a745d5812f436cc5017`, sonra gövde.

### Hikâye 5: tohum niloya-0039 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0039
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'turp', fiil 'kalkmak', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: hızla geri gelen top bankın altına kaçtı | bankın arkasına geçip topu kolayca aldı
@tohum: niloya-0039
@degisim: turp -> top
Parkta güneşli bir sabah Niloya yerde oturmuş, topunu kaydırağa yuvarlıyordu. Top her seferinde geri geliyordu ve Niloya gülüyordu. Ama bir kez top hızla geri geldi ve bankın altına kaçtı. Niloya hemen kalktı ve bankın yanına koştu. Top bankın altında, arka köşede duruyordu. Niloya kolunu uzattı ama topa yetişemedi. Sonra Niloya bir soru düşündü: Topu bankın arkasından alabilir miydi? Niloya bankın arkasına geçti ve topu kolayca aldı. Bu kez topu kaydırağa daha yavaş yuvarladı. Top kaydıraktan indi ve tam Niloya'nın önünde durdu. Niloya çok memnun oldu ve oyununa neşeyle devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya bir soru düşündü"
   - Cümle 7: «Sonra Niloya bir soru düşündü: Topu bankın arkasından alabilir miydi?»
   - Açıklama: 'Bir soru düşünmek' doğal bir kullanım değil; 'düşündü' ya da 'kendine sordu' olmalı.
   - Açıklama: 'Soru düşünmek' doğal bir kullanım değil; tırnaksız soru da anlatımı karıştırıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya bir soru düşündü"
   - Cümle 7: «Sonra Niloya bir soru düşündü: Topu bankın arkasından alabilir miydi?»
   - Açıklama: Kartın 'soru' özelliği merak ettiğini sormaktır; burada Niloya kimseye sormuyor, yalnız içinden düşünüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0039` birebir aynı, `@degisim: turp -> top` (tutuyorsan), ardından `@onarim: e82907438307bb584d9b121fefb3bac51513157f`, sonra gövde.

### Hikâye 6: tohum niloya-0040 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0040
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'şemsiye', fiil 'koşmak', sıfat 'basit'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: kapının arkasından garip bir ses geldi | kapıya koşup baktı ve şemsiyeye düşen damlaları buldu
@tohum: niloya-0040
Yağmur yağıyordu. Niloya evde pencerenin önünde oturuyordu. Birden kapının arkasından garip bir ses geldi. Niloya sesin nereden geldiğini öğrenmek istedi. Hemen kapıya koştu ve onu yavaşça açtı. Önce yerde bir şey aradı ama bulamadı. Sonra başını kaldırdı ve yukarıya baktı. Duvarda onun kırmızı şemsiyesi asılıydı. Damlalar tek tek şemsiyenin üstüne düşüyordu. Bu, basit bir yağmur sesiydi. Niloya güldü ve damlaları bir süre izledi. Sonra Niloya yağmuru dinleyerek mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kapının arkasından garip bir ses"
   - Cümle 3: «Birden kapının arkasından garip bir ses geldi.»
   - Açıklama: Garip ses sıradan bir yağmur sesi çıkıyor; Niloya zaten yağmuru görürken bunun garip gelmesinin sebebi akla yatkın değil ve ortada çözülecek bir sorun yok.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hemen kapıya koştu ve onu yavaşça açtı"
   - Cümle 5: «Hemen kapıya koştu ve onu yavaşça açtı.»
   - Açıklama: Niloya garip bir sesin geldiği kapıyı bir büyüğe haber vermeden açıyor; bu, kartın güvenli özellik kullanımı satırına aykırı ve taklit edilince tehlikeli.
   - Açıklama: Güvenli kullanım satırı merakın bir büyüğe haber vererek gösterilmesini ister; çocuk garip bir sesin geldiği kapıyı tek başına açıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Duvarda onun kırmızı şemsiyesi"
   - Cümle 8: «Duvarda onun kırmızı şemsiyesi asılıydı.»
   - Açıklama: 'onun' zamiri Niloya'nın kendisini gösterirken başka birini de gösterebilir; 'kendi' ya da yalnız 'kırmızı şemsiyesi' daha açık olur.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bu, basit bir yağmur sesiydi"
   - Cümle 10: «Bu, basit bir yağmur sesiydi.»
   - Açıklama: Sorun yalnız garip bir sesin yağmur olduğunun anlaşılması; çocuğun önemseyeceği gerçek bir sorun yok.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "mutlu mutlu şarkı söyledi"
   - Cümle 12: «Sonra Niloya yağmuru dinleyerek mutlu mutlu şarkı söyledi.»
   - Açıklama: Tohumdaki özellik şarkı sorunun çözümünde işe yaramıyor, yalnız sona süs olarak eklenmiş; çözümü merak taşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0040` birebir aynı, ardından `@onarim: f65079d33f12cbef0c2b07b06c80b9d99a3ed5c1`, sonra gövde.

### Hikâye 7: tohum niloya-0041 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0041
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Tospik
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'salata', fiil 'mırıldanmak', sıfat 'gri'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: kekiklere koştu ve kaplumbağası geride kaldı | neden üzgün olduğunu sordu ve özür diledi
@tohum: niloya-0041
Bir sabah Niloya ile Tospik yeşil tepeye çıktı. Sepetlerinde ikisi için bir salata vardı. Ama Niloya kekikleri görünce Tospik'i beklemeden ileri koştu. Tospik ona yetişemedi ve gri bir taşın yanında durdu. Niloya geri gelince Tospik yavaşça bir şeyler mırıldanıyordu. "Tospik, neden üzgünsün?" diye sordu Niloya. "Sen koştun ve ben geride kaldım," dedi Tospik. "Özür dilerim, Tospik, seni beklemedim," dedi Niloya. Tospik başını kaldırdı ve gülümsedi. Sonra taşın yanında salatalarını birlikte yediler. Niloya bundan sonra yürürken hep Tospik'i bekledi.
```

**Hakem bulguları (1):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Tospik yavaşça bir şeyler mırıldanıyordu"
   - Cümle 5: «Niloya geri gelince Tospik yavaşça bir şeyler mırıldanıyordu.»
   - Açıklama: Tospik kendi kendine mırıldanarak konuşuyor.
   - Açıklama: Tospik kendi kendine mırıldanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0041` birebir aynı, ardından `@onarim: 8af00b96f7b5f68fa6443a07e75d6c668c144b50`, sonra gövde.

### Hikâye 8: tohum niloya-0042 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | dedesi
@tohum: niloya-0042
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: sırayla oynamak
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'gümüş', fiil 'belirmek', sıfat 'karışık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | dedesi
@plan: ikisi aynı anda koyunca yapboz parçaları düştü | sırayla koymak için dedesine sordu ve resmi tamamladılar
@tohum: niloya-0042
Evin bahçesinde Niloya ile dedesi masaya bir yapboz döktü. Parçalar çok karışıktı. İkisi aynı anda koymaya çalıştı ve hepsi yere düştü. Niloya onları topladı ve biraz düşündü. "Dede, sırayla koysak olur mu?" diye sordu Niloya. "Olur, önce sen başla," dedi dedesi. Niloya bir parça yerleştirdi, sonra dedesi bir tane ekledi. Böylece masada yavaş yavaş bir resim belirdi. Bu, gökyüzünde parlayan gümüş bir yıldızdı. En son dedesi kalan parçayı Niloya'ya uzattı. Niloya onu yıldızın ucuna taktı ve resim tamamlandı. "Birlikte yaptık, dedeciğim, yıldızımız çok güzel!" dedi Niloya.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sırayla koymak için dedesine sordu"
   - Cümle 0 (plan satırı): «ikisi aynı anda koyunca yapboz parçaları düştü | sırayla koymak için dedesine sordu ve resmi tamamladılar»
   - Açıklama: 'Koymak için sordu' yanlış kurulmuş; 'sırayla koymayı dedesine sordu' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "İkisi aynı anda koymaya çalıştı ve hepsi yere düştü"
   - Cümle 3: «İkisi aynı anda koymaya çalıştı ve hepsi yere düştü.»
   - Açıklama: Aynı anda parça koymanın bütün parçaları yere düşürmesi akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0042` birebir aynı, ardından `@onarim: 23627ef2664b381cb307b5f252442fa4659ceee9`, sonra gövde.

### Hikâye 9: tohum niloya-0043 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0043
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'şişe', fiil 'örtmek', sıfat 'ufak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: ağaçtan düşen fındık şişenin içine girdi | şişeyi ters çevirip fındığı çıkardı
@tohum: niloya-0043
@degisim: örtmek -> çevirmek
Rüzgar ormanda hafif hafif esiyordu. Niloya fındık ağacının altında boş su şişesiyle oynuyordu. Şişenin ağzına şarkı söyleyince sesi çok komik çıkıyordu. Niloya buna kahkahalarla güldü. Ama birden ağaçtan ufak bir fındık düştü ve şişenin içine girdi. Şimdi içeriden yalnız tıkır tıkır bir ses geliyordu. Niloya şişeyi ters çevirdi ve yavaşça salladı. Fındık hemen avucuna düştü. Niloya bu kez ağaçtan biraz uzağa oturdu. Sonra şişenin ağzına yeniden eğildi. Niloya fındığı cebine koydu ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şişenin ağzına şarkı söyleyince"
   - Cümle 3: «Şişenin ağzına şarkı söyleyince sesi çok komik çıkıyordu.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümünde işe yaramıyor, yalnız oyun olarak geçiyor.
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümünde işe yaramıyor; fındık şişe ters çevrilerek çıkarılıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Şişenin ağzına şarkı söyleyince sesi çok komik çıkıyordu.»
   - Açıklama: Sorun ilk üç cümlede yok, ancak beşinci cümlede ortaya çıkıyor.
   - Açıklama: Fındığın şişeye girmesi ancak 5. cümlede söyleniyor; ilk 3 cümlede sorun yok.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ağaçtan ufak bir fındık düştü ve şişenin içine girdi"
   - Cümle 5: «Ama birden ağaçtan ufak bir fındık düştü ve şişenin içine girdi.»
   - Açıklama: Fındığın şişeye girip ters çevirince hemen çıkması önemsiz, düş-topla-bitti türü bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0043` birebir aynı, `@degisim: örtmek -> çevirmek` (tutuyorsan), ardından `@onarim: e9b3c6c127ba47f3b39152faf4035b0b55a65192`, sonra gövde.

### Hikâye 10: tohum niloya-0044 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Murat
@tohum: niloya-0044
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: paylaşmak
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'çember', fiil 'dilemek', sıfat 'sakin'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | Murat
@plan: ağabeyinin topu patlamıştı ve oynayacak şeyi yoktu | çemberini ona verip sırayla oynadılar
@tohum: niloya-0044
@degisim: dilemek -> oynamak
Niloya bahçede kırmızı çemberini belinde çeviriyordu. Murat kapının önünde sakin sakin oturuyordu. Onun topu patlamıştı ve oynayacak bir şeyi yoktu. Niloya durdu ve ağabeyine baktı. "Murat, sen de çevirmek ister misin?" diye sordu Niloya. "Evet, lütfen," dedi Murat. Niloya çemberini ona verdi. Murat denedi ama çember hemen yere düştü. İkisi birlikte güldü. Sonra sırayla oynadılar ve Niloya her turu saydı. Sonunda Murat da tam on tur yaptı. Niloya çok sevindi, çünkü çemberini paylaşınca ağabeyi de eğlenmişti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Niloya bahçede kırmızı çemberini belinde çeviriyordu"
   - Cümle 1: «Niloya bahçede kırmızı çemberini belinde çeviriyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sen de çevirmek ister misin?"
   - Cümle 5: «"Murat, sen de çevirmek ister misin?" diye sordu Niloya.»
   - Açıklama: Tohumdaki soru özelliği merak ettiğini sorma olarak değil, bir teklif olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0044` birebir aynı, `@degisim: dilemek -> oynamak` (tutuyorsan), ardından `@onarim: 82beeef9dccf7ba4ce265f74d7dfed48423a79b9`, sonra gövde.

### Hikâye 11: tohum niloya-0045 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | babaannesi
@tohum: niloya-0045
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: babaannesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'un', fiil 'uyutmak', sıfat 'incecik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | babaannesi
@plan: kum çok kuruydu ve pasta hemen dağıldı | babaannesinden su isteyip kumu ıslattı
@tohum: niloya-0045
@degisim: uyutmak -> süslemek
Güneş parlıyordu. Bugün babaannesinin doğum günüydü ve Niloya onunla parka gelmişti. Babaannesi bankta otururken Niloya ona kumdan bir pasta yapmak istedi. Ama kum un gibi kuruydu ve pasta hemen dağıldı. "Babaanne, biraz su var mı?" diye sordu Niloya. "Var, al bakalım," dedi babaannesi ve su şişesini verdi. Niloya kumu biraz ıslattı ve yeniden şekil verdi. Bu kez pasta sağlam kaldı. Niloya onu incecik bir dalla süsledi. Sonra babaannesini kumun yanına çağırdı. "İyi ki doğdun, babaanneciğim!" dedi Niloya. Babaannesi Niloya'ya sıkıca sarıldı ve ikisi parkta mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kum un gibi kuruydu"
   - Cümle 4: «Ama kum un gibi kuruydu ve pasta hemen dağıldı.»
   - Açıklama: Sorun ancak dördüncü cümlede söyleniyor, ilk üç cümlede yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0045` birebir aynı, `@degisim: uyutmak -> süslemek` (tutuyorsan), ardından `@onarim: c1751dae955a43a7cf4e64b571f5d4f85cb9b8f6`, sonra gövde.

### Hikâye 12: tohum niloya-0046 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Mete
@tohum: niloya-0046
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mete
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'ipek', fiil 'sektirmek', sıfat 'uzun'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Mete
@plan: sormadan aldığı top uzun otlara kaçtı | özür dileyip arkadaşıyla topu aradı ve buldu
@tohum: niloya-0046
Niloya yeşil tepede Mete'nin topunu sormadan aldı. Topu yere sektirmeye başladı. Ama top uzun otların arasına yuvarlandı ve kayboldu. Mete koşarak geldi ve etrafa baktı. "Topum nerede?" diye sordu Mete. Niloya başını eğdi. "Özür dilerim, Mete, topunu izinsiz aldım. Birlikte arayalım mı?" dedi Niloya. Mete başını salladı. İkisi otları yavaş yavaş ayırdı. Sonunda Niloya topu ipek gibi yumuşak çimenlerin üstünde buldu. "Buldun, teşekkürler, Niloya!" dedi Mete. Niloya bundan sonra başkasının oyuncağını almadan önce hep izin istedi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "diye sordu Mete"
   - Cümle 5: «"Topum nerede?" diye sordu Mete.»
   - Açıklama: Tohumdaki 'soru' özelliği Niloya'nındır ama hikayede soran Mete; Niloya'nın merakla sorması işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Birlikte arayalım mı?"
   - Cümle 8: «Birlikte arayalım mı?" dedi Niloya.»
   - Açıklama: Tohumdaki soru özelliği (merak ettiğini sorma) Niloya tarafından merakla kullanılmıyor; tek soru bir öneri.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "topu ipek gibi yumuşak"
   - Cümle 11: «Sonunda Niloya topu ipek gibi yumuşak çimenlerin üstünde buldu.»
   - Açıklama: 'İpek gibi' benzetmesi mecazdır; ayrıca otlar çimen gibi anlatılıyor.
   - Açıklama: 'İpek gibi' benzetmesi mecaz ve küçük çocuğa uygun değil.
   - Açıklama: 'İpek gibi' benzetmesi küçük çocuğa uygun olmayan bir mecaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0046` birebir aynı, ardından `@onarim: 7d51d30957449fb910f963990a8be85cca67637f`, sonra gövde.
