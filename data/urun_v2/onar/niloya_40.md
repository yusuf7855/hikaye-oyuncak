# Editör görevi (onarım): Niloya, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar40.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0171 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0171
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'fırça', fiil 'dağıtmak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: tek fırça vardı ve ikisi de önce boyamak istedi | fırçayı sırayla kullanmayı sordu
@tohum: niloya-0171
Ormanda, fındık ağaçlarının altında düz taşlar vardı. Niloya ile dedesi bu taşları boyamaya gelmişti. Ama çantada yalnız bir fırça vardı ve ikisi de önce boyamak istedi. "Dede, fırçayı sırayla kullanalım mı?" diye sordu Niloya. "Tamam, önce sen başla," dedi dedesi. Dede boyaları ikisine dağıttı. Niloya ilk taşa kırmızı bir çiçek yaptı. Sonra fırçayı dedesine verdi. Dede ikinci taşa sarı bir güneş çizdi. Niloya sırasını beklerken yeni bir renk seçti ve hazırlıklı durdu. Fırça ona gelince üçüncü taşa mavi bir yıldız yaptı. Niloya çok sevindi, çünkü sırayla oynayınca ikisi de eğlenmişti.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fırçayı sırayla kullanmayı sordu"
   - Cümle 0 (plan satırı): «tek fırça vardı ve ikisi de önce boyamak istedi | fırçayı sırayla kullanmayı sordu»
   - Açıklama: 'Kullanmayı sordu' dilbilgisel olarak kusurlu; 'kullanmayı önerdi' ya da 'kullanalım mı diye sordu' olmalı.
   - Açıklama: 'Kullanmayı sordu' dilbilgisel değil; 'kullanmayı önerdi' ya da 'kullanalım mı diye sordu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dede boyaları ikisine dağıttı"
   - Cümle 6: «Dede boyaları ikisine dağıttı.»
   - Açıklama: Dede kendisi de dahil ikisine dağıtamaz; 'dağıttı' fiili bu duruma uymuyor.
   - Açıklama: Dede de ikisinden biri olduğu için 'ikisine dağıttı' yanlış anlamda kullanılmış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hazırlıklı durdu"
   - Cümle 10: «Niloya sırasını beklerken yeni bir renk seçti ve hazırlıklı durdu.»
   - Açıklama: 'Hazırlıklı' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0171` birebir aynı, ardından `@onarim: 6a8fd57466eeb1a52fd1052a0c26ff9edebb1621`, sonra gövde.

### Hikâye 2: tohum niloya-0172 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0172
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'etek', fiil 'damlamak', sıfat 'heyecanlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: dans için müzik yoktu ve hızlı dönemedi | kendi şarkısını söyledi ve dans etti
@tohum: niloya-0172
Ormanda yapraklardan yavaş yavaş su damlıyordu. Niloya kırmızı eteğini giydi ve ağaçların arasını bir sahne yaptı. Ama dans için hiç müzik yoktu, yalnız suyun yavaş sesi vardı. Bu sesle Niloya hızlı dönemedi. Niloya biraz düşündü ve en sevdiği şarkıyı söylemeye başladı. Şarkı başlayınca ayakları da hızlandı. Niloya bir sağa, bir sola döndü. Eteği bir çiçek gibi açıldı. Niloya heyecanlı bir sesle şarkısını sonuna kadar söyledi. Dans bitince durdu ve gülümsedi. Niloya bundan sonra müzik yokken kendi şarkısıyla dans etti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağaçların arasını bir sahne yaptı"
   - Cümle 2: «Niloya kırmızı eteğini giydi ve ağaçların arasını bir sahne yaptı.»
   - Açıklama: Ağaçların arasını sahne yapmak mecazlı ve 3 yaşındaki çocuğa soyut.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yalnız suyun yavaş sesi vardı"
   - Cümle 3: «Ama dans için hiç müzik yoktu, yalnız suyun yavaş sesi vardı.»
   - Açıklama: Ses yavaş olmaz; sıfat öznesine uymuyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yalnız suyun yavaş sesi"
   - Cümle 3: «Ama dans için hiç müzik yoktu, yalnız suyun yavaş sesi vardı.»
   - Açıklama: Ses 'yavaş' olmaz; 'hafif ses' olmalı.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bu sesle Niloya hızlı dönemedi"
   - Cümle 4: «Bu sesle Niloya hızlı dönemedi.»
   - Açıklama: Müzik olmadığı için hızlı dönememek akla yatkın bir sebep değil; sorun zayıf ve inandırıcı değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0172` birebir aynı, ardından `@onarim: 7e0c20ba2500e22669f2953e148f3757703d614a`, sonra gövde.

### Hikâye 3: tohum niloya-0173 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0173
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: kaybolan eşya
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'yağ', fiil 'sergilemek', sıfat 'tüylü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: arkadaşının tüylü topu kayboldu | oynarken söyledikleri şarkıyı söyleyip topun yerini hatırladı
@tohum: niloya-0173
@degisim: yağ -> kütük
Ormanda rüzgar hafif esiyordu. Mete oyuncaklarını büyük bir kütüğün üstünde Niloya'ya sergiliyordu. Ama tüylü sarı topu yoktu. Mete onu nereye koyduğunu bilmiyordu. "Topum kayboldu!" dedi Mete. Niloya biraz düşündü. Az önce top oynarken bir şarkı söylemişlerdi. Niloya o şarkıyı yeniden söyledi. Şarkının sonunda oyun fındık ağacının yanında bitmişti. "Mete, gel, top ağacın yanında!" dedi Niloya. İkisi fındık ağacına koştu. Tüylü top yaprakların arasında duruyordu. Mete topu sevinçle kütüğe koydu. Sonra iki arkadaş bütün oyuncaklarla mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük bir kütüğün üstünde Niloya'ya sergiliyordu"
   - Cümle 2: «Mete oyuncaklarını büyük bir kütüğün üstünde Niloya'ya sergiliyordu.»
   - Açıklama: 'Sergilemek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime; 'gösteriyordu' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kütüğün üstünde Niloya'ya sergiliyordu"
   - Cümle 2: «Mete oyuncaklarını büyük bir kütüğün üstünde Niloya'ya sergiliyordu.»
   - Açıklama: 'Sergilemek' 3 yaşındaki bir çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0173` birebir aynı, `@degisim: yağ -> kütük` (tutuyorsan), ardından `@onarim: 0b6133146c13450394c1c82b3fe4bc4574cf083a`, sonra gövde.

### Hikâye 4: tohum niloya-0174 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0174
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: yeni bir şeyi denemek
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'şeker', fiil 'yetiştirmek', sıfat 'reçelli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: su çok hızlı döküldü ve toprağa girmedi | yavaş bir şarkı söyleyerek suyu azar azar döktü
@tohum: niloya-0174
@degisim: şeker -> fidan
Ormanda Niloya'nın dedesi küçük fındık ağaçları yetiştiriyordu. Niloya ilk kez bir fidanı kovayla kendisi sulamak istedi. Ama suyu çok hızlı döktü ve su toprağa girmeden aktı. "Dede, su fidanın dibine gitmedi," dedi Niloya. "Suyu yavaş dök, Niloya," dedi dedesi. Niloya yavaş bir şarkı söylemeye başladı. Şarkı boyunca suyu azar azar döktü. Şarkı bitince bütün su toprağa girmişti. "Aferin, bu kez oldu," dedi dedesi. Niloya ile dedesi fidanın yanına oturdu ve reçelli ekmeklerini mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Suyu yavaş dök, Niloya"
   - Cümle 5: «"Suyu yavaş dök, Niloya," dedi dedesi.»
   - Açıklama: Çözümü dede doğrudan söylüyor; Niloya yalnız uyguluyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "reçelli ekmeklerini mutlu mutlu yedi"
   - Cümle 10: «Niloya ile dedesi fidanın yanına oturdu ve reçelli ekmeklerini mutlu mutlu yedi.»
   - Açıklama: Reçelli ekmekler daha önce kurulmadan sonda sebepsiz beliriyor.
   - Açıklama: Reçelli ekmekler önceden kurulmadan sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0174` birebir aynı, `@degisim: şeker -> fidan` (tutuyorsan), ardından `@onarim: d30bbcb86a3be506ee385beba676bf1d94ba390f`, sonra gövde.

### Hikâye 5: tohum niloya-0176 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0176
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'kutu', fiil 'ilgilenmek', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: ip her seferinde ayağına takıldı | şarkı söyledi ve şarkının sesiyle zıpladı
@tohum: niloya-0176
@degisim: elmalı -> sarı
Niloya ormanda ip atlama oyunuyla ilgileniyordu. İpini sarı bir kutudan çıkardı ve atlamaya başladı. Ama ip her seferinde ayağına takıldı, çünkü Niloya çok erken zıplıyordu. Niloya ipi yere bıraktı ve biraz düşündü. Sonra en sevdiği şarkıyı söylemeye başladı. İpi çevirdi ve şarkının sesiyle birlikte zıpladı. İp bir kez, iki kez, on kez döndü. Bu kez ayağına hiç takılmadı. Niloya şarkıyı sonuna kadar söyledi ve durmadan atladı. Niloya çok sevindi, çünkü şarkı söyleyince ip atlamayı başarmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ip atlama oyunuyla ilgileniyordu"
   - Cümle 1: «Niloya ormanda ip atlama oyunuyla ilgileniyordu.»
   - Açıklama: 'İlgilenmek' 3 yaşındaki bir çocuk için soyut bir kelime.
   - Açıklama: 'ilgilenmek' 3 yaşındaki çocuk için soyut bir kelime; 'ip atlıyordu' yeterli.
   - Açıklama: 'İlgilenmek' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir fiil; 'ip atlıyordu' yeterli.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şarkının sesiyle birlikte zıpladı"
   - Cümle 6: «İpi çevirdi ve şarkının sesiyle birlikte zıpladı.»
   - Açıklama: 'Şarkının sesiyle zıplamak' anlamca yanlış; şarkıya uyarak zıplamak kastediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0176` birebir aynı, `@degisim: elmalı -> sarı` (tutuyorsan), ardından `@onarim: 3e278e8b4003e517511d602790035d3467ca613c`, sonra gövde.

### Hikâye 6: tohum niloya-0177 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0177
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'güneş', fiil 'yakalanmak', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: ağaçların altında gölgesi kayboldu | yukarı baktı ve açık bir yere koştu
@tohum: niloya-0177
Bir sabah ormanda güneş parlıyordu. Niloya simsiyah gölgesiyle kovalamaca oynuyordu. Ama ağaçların altına girdi ve gölgesi birden kayboldu. Niloya durdu ve bir soru sordu: Gölgem nereye gitti? Sonra yukarı baktı. Yapraklar güneşi kapatıyordu. Gölge yalnız güneşte oluyordu! Niloya hemen açık bir yere koştu. Gölgesi yine yanında çıktı. Niloya zıpladı, gölgesi de zıpladı. Niloya onu yakalamaya çalıştı ama gölge hiç yakalanmadı. Niloya buna çok güldü. Niloya bundan sonra gölge oyununu hep güneşte oynadı.
```

**Hakem bulguları (4):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya durdu ve bir soru sordu"
   - Cümle 4: «Niloya durdu ve bir soru sordu: Gölgem nereye gitti?»
   - Açıklama: Yanında kimse yokken Niloya kendi kendine soru soruyor.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "bir soru sordu: Gölgem nereye gitti?"
   - Cümle 4: «Niloya durdu ve bir soru sordu: Gölgem nereye gitti?»
   - Açıklama: Niloya'nın sorusu tırnak içinde yazılmamış.
   - Açıklama: Doğrudan aktarılan soru tırnak içine alınmamış.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Gölgesi yine yanında çıktı."
   - Cümle 9: «Gölgesi yine yanında çıktı.»
   - Açıklama: 'Yanında çıktı' kuruluşu bozuk; 'yine yanında belirdi' ya da 'yine ortaya çıktı' olmalı.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya buna çok güldü."
   - Cümle 12: «Niloya buna çok güldü.»
   - Açıklama: Art arda dört cümle gereksiz yere 'Niloya' adıyla başlıyor.
   - Açıklama: Art arda dört cümle 'Niloya' ile başlıyor; ad gereksiz tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0177` birebir aynı, ardından `@onarim: 7f36aa94e8754cc0ec82cad1ec821734745008f2`, sonra gövde.

### Hikâye 7: tohum niloya-0178 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0178
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'kebap', fiil 'bırakmak', sıfat 'soslu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: rüzgarla güzel bir koku geldi | kokunun nereden geldiğini sordu ve kekikleri buldu
@tohum: niloya-0178
@degisim: soslu -> kokulu
Bir sabah Niloya yeşil tepede yürüyordu. Rüzgar esince burnuna güzel bir koku geldi. Bu koku kebap kokusuna benziyordu ama tepede kebap yoktu. Niloya bir soru sordu: Bu koku nereden geliyordu? Niloya rüzgarın geldiği yöne doğru yürüdü. Taşların arasında küçük mor çiçekli otlar gördü. Eğildi ve bir yaprağı kokladı. Koku bu kekiklerden geliyordu! Niloya birkaç dal kopardı, öteki dalları yerinde bıraktı. Kokulu dalları avucunda sıkıca tuttu. Niloya çok sevindi, çünkü güzel kokunun kekiklerden geldiğini bulmuştu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgarla güzel bir koku geldi"
   - Cümle 0 (plan satırı): «rüzgarla güzel bir koku geldi | kokunun nereden geldiğini sordu ve kekikleri buldu»
   - Açıklama: Güzel bir koku gelmesi gerçek bir sorun değil; çözülecek bir dert yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "burnuna güzel bir koku geldi"
   - Cümle 2: «Rüzgar esince burnuna güzel bir koku geldi.»
   - Açıklama: Güzel bir kokunun gelmesi bir sorun değil; çözülecek gerçek bir güçlük yok.
3. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya bir soru sordu: Bu koku nereden geliyordu?"
   - Cümle 4: «Niloya bir soru sordu: Bu koku nereden geliyordu?»
   - Açıklama: Niloya yanında kimse yokken soru soruyor; kendi kendine konuşma gibi.
4. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya bir soru sordu"
   - Cümle 4: «Niloya bir soru sordu: Bu koku nereden geliyordu?»
   - Açıklama: Niloya tek başına, soruyu kimseye değil kendi kendine soruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0178` birebir aynı, `@degisim: soslu -> kokulu` (tutuyorsan), ardından `@onarim: 5e757ec94700fa3af0f3490e95bc091451c97deb`, sonra gövde.

### Hikâye 8: tohum niloya-0179 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0179
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'oyuncak', fiil 'yerleştirmek', sıfat 'sırılsıklam'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: yağmurda oyuncaklar sırılsıklam oldu | güneşli bir yere koydu ve şarkı söyleyerek bekledi
@tohum: niloya-0179
Bahçede yağmur yeni dinmişti. Niloya'nın çimenlerde kalan oyuncakları sırılsıklam olmuştu. Niloya onları kurutmak istedi ama bahçenin çoğu gölgeydi. Sonra çitin yanında küçük bir güneşli yer gördü. Niloya oyuncakları tek tek oraya yerleştirdi. Güneş onları ısıttı. Ne kadar bekleyeceğini bilmiyordu. Bu yüzden en sevdiği şarkıyı söylemeye başladı. Şarkıyı üç kez baştan sona söyledi. Sonra oyuncaklara dokundu. Hepsi güneşte kurumuştu. Niloya bir oyuncağını aldı ve ona sarıldı. Niloya çok sevindi, çünkü oyuncaklarıyla yine oynayabilirdi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "küçük bir güneşli yer gördü"
   - Cümle 4: «Sonra çitin yanında küçük bir güneşli yer gördü.»
   - Açıklama: Sıfat dizilişi bozuk; 'küçük, güneşli bir yer' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu yüzden en sevdiği şarkıyı söylemeye başladı"
   - Cümle 8: «Bu yüzden en sevdiği şarkıyı söylemeye başladı.»
   - Açıklama: Tohumdaki şarkı özelliği sorunu çözmüyor, oyuncakları güneş kurutuyor; özellik yalnız süs olarak kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0179` birebir aynı, ardından `@onarim: a6d830ae21eb28f927f7db4b8011a11b34b81977`, sonra gövde.

### Hikâye 9: tohum niloya-0181 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Murat
@tohum: niloya-0181
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'kova', fiil 'gelmek', sıfat 'garip'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Murat
@plan: ağabeyi kırmızı kovasını bir yere bırakıp unuttu | en son nerede gördüğünü sorup taşın arkasında buldu
@tohum: niloya-0181
@degisim: garip -> kırmızı
Niloya ile Murat yeşil tepelerde kekik topluyordu. Bir süre sonra Murat üzgün bir yüzle Niloya'nın yanına geldi. Kırmızı kovasını bir yere bırakmış ve yerini unutmuştu. Bu yüzden kekikleri koyacak bir yeri yoktu. Niloya ona kovayı en son nerede gördüğünü sordu. Murat biraz düşündü. Büyük taşın yanında oturduğunu hatırladı. İkisi birlikte büyük taşa doğru yürüdü. Niloya taşın çevresine baktı. Kırmızı kova taşın arkasında, kekiklerin arasında duruyordu. Niloya kovayı aldı ve ağabeyine verdi. Murat kovayı sıkıca tuttu ve gülümsedi. Sonra ikisi kovayı kekikle birlikte doldurdu. Niloya çok sevindi, çünkü ağabeyinin kovasını bulmuştu.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kovayı kekikle birlikte doldurdu"
   - Cümle 13: «Sonra ikisi kovayı kekikle birlikte doldurdu.»
   - Açıklama: 'Kekikle birlikte' yanlış yapı; 'ikisi birlikte kovayı kekikle doldurdu' olmalı.
   - Açıklama: 'Kekikle birlikte' kovanın kekikle beraber doldurulduğu anlamını veriyor; 'birlikte kovayı kekikle doldurdu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0181` birebir aynı, `@degisim: garip -> kırmızı` (tutuyorsan), ardından `@onarim: 9c0ed8c1d4d523923e32c59b4ab6d55092e0b27e`, sonra gövde.
