# Editör görevi (onarım): Niloya, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar33.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0110 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | annesi
@tohum: niloya-0110
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kızartma', fiil 'aşmak', sıfat 'taze'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | park | annesi
@plan: rüzgar topu çitin arkasına uçurdu | topun yerini buldu ve annesinden yardım istedi
@tohum: niloya-0110
Niloya parkta top oynuyordu. Annesi bankta taze ekmek ve patates kızartması hazırlıyordu. Birden rüzgar esti ve hafif top uçup çiti aştı. Niloya oraya koştu ve merakla çitin arasından baktı. Top çitin arkasındaki uzun otların arasındaydı. Çit yüksekti ve Niloya ona tırmanmadı. Hemen annesinin yanına koştu. "Anne, topum çitin arkasına düştü, bana yardım eder misin?" diye sordu Niloya. Annesi başını salladı ve parkın kapısından çıktı. Niloya parmağıyla topun yerini gösterdi. Annesi topu otların arasından aldı ve Niloya'ya verdi. "Teşekkürler, anneciğim, şimdi birlikte kızartma yiyelim!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "taze ekmek ve patates kızartması hazırlıyordu"
   - Cümle 2: «Annesi bankta taze ekmek ve patates kızartması hazırlıyordu.»
   - Açıklama: Parkta bankta patates kızartması hazırlamak kartın park tarifine ve dizinin dünyasına uymayan yanlış bir bilgi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0110` birebir aynı, ardından `@onarim: a4a4fa6e83bc706e22eb8b8876cb8417163e9246`, sonra gövde.

### Hikâye 2: tohum niloya-0112 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0112
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: kaybolan eşya
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'nane', fiil 'serinletmek', sıfat 'bozuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: su şişesini bir yere bırakıp unuttu | en son nerede su içtiğini düşündü ve şişeyi buldu
@tohum: niloya-0112
Tepede güneş çok sıcak parlıyordu. Niloya kekik topluyordu ve çok susamıştı. Ama su şişesini bir yere bırakmış ve unutmuştu. Şişede nane yapraklı serin su vardı. Niloya durdu ve şu soruyu düşündü: Şişeden en son nerede su içmişti? Sonra hatırladı. Bozuk bir çitin yanında oturup su içmişti. Niloya tepeden aşağı yürüdü ve çite gitti. Şişe çitin dibinde, otların arasında duruyordu. Niloya şişeyi açtı ve sudan içti. Nane kokulu su onu hemen serinletti. Sonra Niloya kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya durdu ve şu soruyu düşündü"
   - Cümle 5: «Niloya durdu ve şu soruyu düşündü: Şişeden en son nerede su içmişti?»
   - Açıklama: Kartın özellikler alanındaki 'sorar' özelliği kimseye soru sorulmadan yalnız içten düşünülen bir soruya indirgenmiş.
   - Açıklama: Karttaki özellik merak ettiğini sormak iken Niloya kimseye sormuyor, yalnız hatırlıyor; özellik karttaki gibi kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0112` birebir aynı, ardından `@onarim: a0c9d520390dfb6a23ec00be87222b05950db279`, sonra gövde.

### Hikâye 3: tohum niloya-0116 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0116
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'marul', fiil 'çalıştırmak', sıfat 'pürüzsüz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: yürürken yanından garip bir ses geliyordu | şarkı söyleyip adım attı ve sesi sepette buldu
@tohum: niloya-0116
@degisim: çalıştırmak -> durmak
Ormanda garip bir gıcır sesi geliyordu. Niloya kolunda sepetiyle ağaçların arasında yürüyordu. Ses, o yürürken hep yanından geliyordu. Niloya ağaçların arkasına baktı ama bir şey göremedi. Sonra bir yürüme şarkısı söyledi ve her kelimede bir adım attı. Her adımda gıcır sesi de geldi. Niloya durunca ses de durdu. Niloya kolundaki sepete baktı. Ses sepetten geliyordu! Niloya çok güldü. Sepeti pürüzsüz bir taşın üstüne koydu ve yanına oturdu. Sonra sepetteki ekmeği ve marulu mutlu mutlu yedi.
```

**Hakem bulguları (6):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Ormanda garip bir gıcır sesi geliyordu"
   - Cümle 1: «Ormanda garip bir gıcır sesi geliyordu.»
   - Açıklama: Ormanda yalnız yürüyen çocuğu izleyen kaynağı görünmez garip bir ses korkutucu bir gerilim kuruyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "garip bir gıcır sesi"
   - Cümle 1: «Ormanda garip bir gıcır sesi geliyordu.»
   - Açıklama: 'Gıcır' ad değil yansıma kökü; 'gıcırtı sesi' olmalı.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Ses, o yürürken hep yanından geliyordu"
   - Cümle 3: «Ses, o yürürken hep yanından geliyordu.»
   - Açıklama: Ormanda yürüyen çocuğu izleyen ve kaynağı görünmeyen garip bir ses küçük çocuklar için ürkütücü bir öğedir.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ses sepetten geliyordu!"
   - Cümle 9: «Ses sepetten geliyordu!»
   - Açıklama: Sepetin neden gıcırdadığı hiç söylenmiyor, sorunun sebebi açıklanmadan kalıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sepeti pürüzsüz bir taşın"
   - Cümle 11: «Sepeti pürüzsüz bir taşın üstüne koydu ve yanına oturdu.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "pürüzsüz bir taşın üstüne"
   - Cümle 11: «Sepeti pürüzsüz bir taşın üstüne koydu ve yanına oturdu.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0116` birebir aynı, `@degisim: çalıştırmak -> durmak` (tutuyorsan), ardından `@onarim: 79797c827499227527b065625ddf7ddd8dc75339`, sonra gövde.

### Hikâye 4: tohum niloya-0118 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | babaannesi
@tohum: niloya-0118
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'rüzgar', fiil 'kaymak', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | dağ | babaannesi
@plan: yokuşun kenarına bıraktığı sepet aşağı kaydı | özür diledi ve çalıların arkasına bakıp sepeti buldu
@tohum: niloya-0118
Bir sabah Niloya ile babaannesi yeşil tepede kekik topluyordu. Niloya dolu sepeti yokuşun kenarına bıraktı. Sonra çevik adımlarla bir çiçeğe koştu. Tam o sırada rüzgar esti ve sepet otların üstünden aşağı kaydı. Babaannesi sepeti yerinde bulamadı ve şaşırdı. "Özür dilerim, babaanne, sepeti oraya ben koydum," dedi Niloya. Niloya babaannesinin elini tuttu. İkisi yavaşça aşağı indi. Niloya sepetin nerede olduğunu merak etti. Çalıların arkasına tek tek baktı. Sepet büyük bir çalının arkasında duruyordu. Kekikler yine içindeydi. Niloya sepeti iki eliyle babaannesine verdi. "Sağ ol, Niloya, sepeti sen buldun!" dedi babaannesi.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra çevik adımlarla bir"
   - Cümle 3: «Sonra çevik adımlarla bir çiçeğe koştu.»
   - Açıklama: Tohumdaki özellik merak; kartta olmayan çeviklik ikinci bir özellik olarak ekleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Sonra çevik adımlarla bir çiçeğe koştu.»
   - Açıklama: Sepetin kayması ancak 4. cümlede anlatılıyor; ilk 3 cümlede sorun yok.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "sepet otların üstünden aşağı kaydı"
   - Cümle 4: «Tam o sırada rüzgar esti ve sepet otların üstünden aşağı kaydı.»
   - Açıklama: Sorun ancak 4. cümlede ortaya çıkıyor, ilk 3 cümlede söylenmiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Özür dilerim, babaanne, sepeti oraya ben koydum"
   - Cümle 6: «"Özür dilerim, babaanne, sepeti oraya ben koydum," dedi Niloya.»
   - Açıklama: Özür dileme sebebe yönelmiyor ve çözüm aşağı inip çalıları tek tek aramakla ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0118` birebir aynı, ardından `@onarim: f109ee6f8b5b1ba78574fe4a88fcd35923d9030a`, sonra gövde.

### Hikâye 5: tohum niloya-0124 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0124
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kapak', fiil 'parıldamak', sıfat 'yırtık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: şemsiye yırtıktı ve damlalar başına düştü | parka bakıp kaydırağın altında kuru bir yer buldu
@tohum: niloya-0124
@degisim: kapak -> şemsiye
Yağmur birden hızlı hızlı yağmaya başladı. Niloya parkta hemen şemsiyesini açtı. Ama şemsiye yırtıktı ve damlalar Niloya'nın başına düştü. Niloya parkta kuru bir yer olup olmadığını merak etti ve dolaştı. Kaydırağın altında küçük, kuru bir yer gördü. Oraya yürüdü ve yağmurdan korundu. Orada başı hiç ıslanmadı. Niloya şemsiyesini kapattı ve yanına koydu. Biraz sonra yağmur dindi ve güneş çıktı. Parktaki damlalar güneşte parıldadı. Niloya kaydırağın altından çıktı ve su birikintilerinin üstünden mutlu mutlu zıpladı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Orada başı hiç ıslanmadı"
   - Cümle 7: «Orada başı hiç ıslanmadı.»
   - Açıklama: Bir önceki cümledeki 'yağmurdan korundu' bilgisini gereksiz yere tekrarlıyor.
   - Açıklama: Önceki cümledeki 'yağmurdan korundu' bilgisini gereksizce tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0124` birebir aynı, `@degisim: kapak -> şemsiye` (tutuyorsan), ardından `@onarim: 76f47a7118b23231f564db249ef4c72da4362248`, sonra gövde.

### Hikâye 6: tohum niloya-0125 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0125
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'saksı', fiil 'kazanmak', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: kaydırak ve oyuncaklar ıslaktı, oynanacak bir şey yoktu | saksıyı ters çevirip damla sesiyle şarkı söyledi
@tohum: niloya-0125
@degisim: kazanmak -> çevirmek
Parkta yağmur tıp tıp yağıyordu. Niloya oynamak istedi, ama kaydırak ve oyuncaklar çok ıslaktı. Niloya oynayacak başka bir şey aradı ve bankın altına eğilip baktı. Orada boş ve kuru bir saksı buldu. Niloya saksıyı ters çevirdi ve yağmurun altına koydu. Damlalar saksıya düşünce davul gibi güzel bir ses çıktı. Niloya bu sesle birlikte en sevdiği şarkıyı söyledi. Damlalar hızlı düşünce Niloya da hızlı söyledi. Damlalar yavaş düşünce Niloya da yavaş söyledi. Niloya ıslak kaydırağı unuttu ve yeni oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Orada boş ve kuru bir saksı buldu"
   - Cümle 4: «Orada boş ve kuru bir saksı buldu.»
   - Açıklama: Çözümü getiren saksı parkta bankın altında tesadüfen ve sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0125` birebir aynı, `@degisim: kazanmak -> çevirmek` (tutuyorsan), ardından `@onarim: fbedba0662624f006fd63ff0b3760a2d538f66ca`, sonra gövde.

### Hikâye 7: tohum niloya-0128 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Tospik
@tohum: niloya-0128
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'domates', fiil 'düşünmek', sıfat 'meraklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | Tospik
@plan: kaplumbağanın karnı açtı ama yiyecek bulamadı | ne istediğini sordu ve ona küçük bir domates verdi
@tohum: niloya-0128
Evin bahçesinde sıcak bir öğle vaktiydi. Niloya domateslerin yanında oturuyordu ve Tospik yavaşça yanına geldi. Tospik'in karnı açtı, ama bahçede yiyecek bir şey bulamamıştı. "Tospik, ne yemek istersin?" diye sordu Niloya. Tospik biraz düşündü. "Kırmızı ve sulu bir şey istiyorum," dedi Tospik. Sonra meraklı gözlerle domateslere baktı. Ama kırmızı domatesler Tospik için çok yüksekteydi. Niloya en kırmızı olanı dalından kopardı. Onu Tospik'in önüne, yere koydu. Tospik onu yavaş yavaş yedi. "Çok lezzetli, teşekkürler, Niloya!" dedi Tospik. Niloya bundan sonra Tospik acıkınca ona ne istediğini sordu.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "ona küçük bir domates verdi"
   - Cümle 0 (plan satırı): «kaplumbağanın karnı açtı ama yiyecek bulamadı | ne istediğini sordu ve ona küçük bir domates verdi»
   - Açıklama: Gövdede küçük değil en kırmızı domates veriliyor ve asıl engel olan domateslerin yüksekliği planda yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Tospik acıkınca ona ne istediğini sordu"
   - Cümle 13: «Niloya bundan sonra Tospik acıkınca ona ne istediğini sordu.»
   - Açıklama: Tohumdaki soru özelliği bir kez yerine iki kez kullanılmış; kartın özellikler alanındaki kullanım bir kez olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0128` birebir aynı, ardından `@onarim: 685219b725438e5a78ab3f498eea14a8cb4d8180`, sonra gövde.

### Hikâye 8: tohum niloya-0129 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0129
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'file', fiil 'bozulmak', sıfat 'soğuk'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | -
@plan: kar tanesi sıcak elinde eridi ve bozuldu | kaydırağın soğuk üstündeki karlara baktı
@tohum: niloya-0129
@degisim: file -> kaydırak
Parkta kar yağıyordu ve hava çok soğuktu. Niloya yıldız gibi kar tanelerini yakından görmek istedi. Ama bir kar tanesi eline düştü, hemen eridi ve şekli bozuldu. Niloya başka bir yer bulmak için etrafa merakla baktı. Kaydırağın üstünde de ince bir kar vardı. Niloya kaydırağa yaklaştı ve eğildi. Kaydırak soğuktu ve kar taneleri orada erimiyordu. Niloya onlara yakından baktı. Hepsinin altı küçük kolu vardı! Kar taneleri gerçekten minik yıldızlara benziyordu. Niloya çok sevindi, çünkü kar tanelerini sonunda yakından görmüştü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hepsinin altı küçük kolu vardı"
   - Cümle 9: «Hepsinin altı küçük kolu vardı!»
   - Açıklama: Kar tanesine 'kol' demek mecazdır ve 'altı' küçük çocukta 'alt' ile karışabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0129` birebir aynı, `@degisim: file -> kaydırak` (tutuyorsan), ardından `@onarim: 3e236096587b3d791ba5bf6cff63ceb122d2bad7`, sonra gövde.

### Hikâye 9: tohum niloya-0131 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Tospik
@tohum: niloya-0131
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'fidan', fiil 'koparmak', sıfat 'lezzetli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | Tospik
@plan: kaplumbağa çiçeklerin arasında kayboldu | şarkı söyledi ve kaplumbağa sesi izleyip geldi
@tohum: niloya-0131
@degisim: fidan -> çiçek
Niloya bahçede Tospik için lezzetli bir marul yaprağı kopardı. Ama Tospik bir sürü çiçeğin arasında kaybolmuştu. "Niloya, buradan çıkamıyorum!" diye seslendi Tospik. Niloya çiçeklere basmak istemedi. Niloya biraz düşündü. "Tospik, sesimi izle ve gel!" dedi Niloya. Sonra en sevdiği şarkıyı söylemeye başladı. Tospik şarkıyı duydu ve sese doğru yavaş yavaş yürüdü. Sonunda yaprakların arasından başını çıkardı. Niloya marul yaprağını ona uzattı. Tospik yaprağı hemen yedi. "Teşekkürler, Niloya, hem şarkın hem de yaprak çok güzeldi!" dedi Tospik.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesimi izle ve gel"
   - Cümle 6: «"Tospik, sesimi izle ve gel!" dedi Niloya.»
   - Açıklama: 'İzlemek' ses için doğru anlamda kullanılmamış; 'sesime doğru gel' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0131` birebir aynı, `@degisim: fidan -> çiçek` (tutuyorsan), ardından `@onarim: 0609d25dc740474f466743e7a963d2c15f8e0748`, sonra gövde.

### Hikâye 10: tohum niloya-0133 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0133
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'bağcık', fiil 'dizmek', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: fındıklar çok fazlaydı ve saymak zordu | şarkı söyleyip sırayla birer fındık dizdiler
@tohum: niloya-0133
@degisim: saygılı -> uzun
Yapraklar hışır hışır sallanıyordu. Niloya ile Murat ormanda bir torba fındık toplamıştı. Fındıkları paylaşmak istediler, ama fındıklar çok fazlaydı ve saymak zordu. Murat torbanın bağcığını açtı. Niloya biraz düşündü ve bir şarkı söylemeye başladı. Şarkı sürerken ikisi de sırayla birer fındık aldı. Fındıkları kütüğün üstüne iki uzun sıra halinde dizdiler. Torbada fındık bitene kadar şarkıyı söylediler. Sonunda iki sırada da aynı sayıda fındık vardı. Murat sevinçle ellerini çırptı. Niloya bundan sonra bir şeyi paylaşırken hep bu şarkıyı söyledi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir şarkı söylemeye başladı"
   - Cümle 5: «Niloya biraz düşündü ve bir şarkı söylemeye başladı.»
   - Açıklama: Şarkı fındıkların eşit paylaşılmasında hiçbir işlev görmüyor, çözümü sırayla almak getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0133` birebir aynı, `@degisim: saygılı -> uzun` (tutuyorsan), ardından `@onarim: 69a9dd236ddf71f85c616d1043ceae770db6ed55`, sonra gövde.

### Hikâye 11: tohum niloya-0134 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0134
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: kaybolan eşya
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'patates', fiil 'koşturmak', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: rüzgar şapkayı yüksek otların arasına götürdü | rüzgarın yönünü düşündü ve o yöne gidip şapkayı buldu
@tohum: niloya-0134
@degisim: patates -> şapka
Rüzgar birden sertçe esti. Niloya ormanda koşturuyordu ve sarı şapkası başından uçtu. Şapka yüksek otların arasına düştü ve kayboldu. Niloya otların arasına baktı ama şapkasını göremedi. Niloya durdu ve bir soru düşündü: Rüzgar hangi yöne esiyordu? Niloya ağaçların dallarına baktı. Dallar hep aynı yöne doğru sallanıyordu. Niloya o yöne doğru yavaşça yürüdü. Otları elleriyle araladı ve dikkatle baktı. Şapkası bir çalının dibinde duruyordu. Niloya şapkayı aldı ve başına sıkıca taktı. Niloya çok sevindi, çünkü şapkasını kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya ormanda koşturuyordu"
   - Cümle 2: «Niloya ormanda koşturuyordu ve sarı şapkası başından uçtu.»
   - Açıklama: Küçük çocuk ormanda yalnız koşturuyor ve bir büyüğe haber vermeden yüksek otların arasına gidiyor, taklit edilince güvensiz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "durdu ve bir soru düşündü"
   - Cümle 5: «Niloya durdu ve bir soru düşündü: Rüzgar hangi yöne esiyordu?»
   - Açıklama: 'Bir soru düşünmek' doğal bir kullanım değil; 'kendine sordu' ya da 'düşündü' olmalı.
   - Açıklama: 'Soru düşünmek' doğal değil; 'kendine sordu' ya da 'düşündü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0134` birebir aynı, `@degisim: patates -> şapka` (tutuyorsan), ardından `@onarim: 8962a4da0055e1c6ce02ec7a0358d4b91369eed3`, sonra gövde.

### Hikâye 12: tohum niloya-0135 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0135
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'koltuk', fiil 'sabırsızlanmak', sıfat 'yeterli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: güzel bir koku vardı ama kaya önünü kapattı | kayanın öbür yanına baktı ve kekikleri buldu
@tohum: niloya-0135
@degisim: koltuk -> kaya
Niloya dağda yürürken çok güzel bir koku fark etti. Kokunun nereden geldiğini bulmak istedi. Ama önünde büyük bir kaya vardı ve arkasını göremiyordu. Niloya biraz sabırsızlandı. Kokuyu bulmak için kayanın öbür yanını merak etti. Kayanın yanından dolaşıp öbür tarafa yürüdü. Birkaç adım yeterli oldu. Kayanın arkasında mor çiçekli kekikler vardı! Güzel koku bu kekiklerden geliyordu. Niloya eğildi ve kekikleri yavaşça kokladı. Sonra derin bir nefes aldı ve gülümsedi. Niloya çok sevindi, çünkü güzel kokunun nereden geldiğini bulmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya biraz sabırsızlandı"
   - Cümle 4: «Niloya biraz sabırsızlandı.»
   - Açıklama: 'Sabırsızlanmak' soyut bir duygu kelimesidir; 3 yaşındaki çocuk bilmeyebilir.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kayanın öbür yanını merak etti"
   - Cümle 5: «Kokuyu bulmak için kayanın öbür yanını merak etti.»
   - Açıklama: 'Bulmak için merak etti' anlamca uyumsuz; merak etmek bir amaç için yapılan eylem değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Birkaç adım yeterli oldu"
   - Cümle 7: «Birkaç adım yeterli oldu.»
   - Açıklama: 'Yeterli oldu' soyut bir ifade, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0135` birebir aynı, `@degisim: koltuk -> kaya` (tutuyorsan), ardından `@onarim: 13a3920d58f6c9938df7eb9d6df656a57badebb7`, sonra gövde.
