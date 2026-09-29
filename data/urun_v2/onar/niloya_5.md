# Editör görevi (onarım): Niloya, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0002 (deneme 2 -> 3)

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
Parkta Niloya kaydırağın yanında sarı bir çiçek gördü. Çiçek güneşte yavaş yavaş açılıyordu. Niloya bunu Tospik'e göstermek istedi ama Tospik uyuyordu. Niloya ile limonlu kek satma oyunu oynamış, yorulmuştu. Niloya onun yanına oturdu ve neşeli bir şarkı söyledi. Tospik şarkıyı duyunca gözlerini açtı. Başını kabuğundan çıkardı ve çiçeğe baktı. Çiçek daha tam açık değildi. İkisi yan yana oturdu ve bekledi. Sonra sarı yapraklar bir bir açıldı. Tospik gülümsedi ve çiçeği kokladı. Niloya çok sevindi, çünkü çiçek açarken Tospik de yanındaydı.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Niloya ile limonlu kek satma oyunu oynamış, yorulmuştu"
   - Cümle 4: «Niloya ile limonlu kek satma oyunu oynamış, yorulmuştu.»
   - Açıklama: Cümlenin öznesi eksik; kimin Niloya ile oynadığı söylenmiyor.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "limonlu kek satma oyunu oynamış"
   - Cümle 4: «Niloya ile limonlu kek satma oyunu oynamış, yorulmuştu.»
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı kipe kayıyor; 'oynamıştı' olmalı.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Niloya ile limonlu kek"
   - Cümle 4: «Niloya ile limonlu kek satma oyunu oynamış, yorulmuştu.»
   - Açıklama: Yorulanın Tospik olduğu belli değil; özne gösterilmemiş.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Niloya ile limonlu kek satma oyunu oynamış"
   - Cümle 4: «Niloya ile limonlu kek satma oyunu oynamış, yorulmuştu.»
   - Açıklama: Cümlenin öznesi yazılmamış; oynayıp yorulanın Tospik olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0002` birebir aynı, `@degisim: düğüm -> çiçek` (tutuyorsan), ardından `@onarim: e4e14cda4062ff32832a1d1ea5c962485cd1fb20`, sonra gövde.

### Hikâye 2: tohum niloya-0004 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Murat
@tohum: niloya-0004
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'halı', fiil 'tutunmak', sıfat 'yaratıcı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | Murat
@plan: halıda hiçbir yeri tutmadı ve arkaya kaydı | iki yanını tutabilir miyim diye sordu ve tutundu
@tohum: niloya-0004
@degisim: yaratıcı -> eski
Parkta Niloya ile Murat halı çekme oyunu oynuyordu. Niloya eski bir halıya oturdu, Murat da halıyı çimenlerde çekti. Ama Niloya hiçbir yeri tutmuyordu ve halının arka ucuna kaydı. İkisi de kahkahalarla güldü. Niloya kalktı ve halıya dikkatle baktı. "Murat, halının iki yanını tutabilir miyim?" diye sordu Niloya. "Olur, hadi bir daha deneyelim," dedi Murat. Niloya yine halıya oturdu ve iki yanına sıkıca tutundu. Murat halıyı yeniden çekti. Bu kez Niloya hiç kaymadı. "Şimdi daha uzağa çek, Murat!" dedi Niloya. Murat halıyı kaydırağın yanına kadar çekti. Niloya çok mutluydu, çünkü oyunları yeniden eğlenceli olmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "İkisi de kahkahalarla güldü"
   - Cümle 4: «İkisi de kahkahalarla güldü.»
   - Açıklama: Kayma ikisini de güldürüyor, yani olay çocuğun gözünde bir sorun gibi kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0004` birebir aynı, `@degisim: yaratıcı -> eski` (tutuyorsan), ardından `@onarim: 31681358700c146ebb901faa85d55a5f03bb0000`, sonra gövde.

### Hikâye 3: tohum niloya-0005 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Niloya parkta salıncakta sallanıyor, annesi de onu itiyordu. Birden rüzgar esti ve annesinin saçları yüzüne döküldü. Annesinin yanında toka yoktu ve yüzü somurtkan oldu. Niloya salıncaktan indi. Saçında iki pembe fiyonk vardı. "Anne, bir fiyonk da senin olsun," dedi Niloya. Hemen bir fiyonk çözdü ve annesinin saçlarını arkadan bağladı. Bu sırada annesine en sevdiği şarkıyı söyledi. Annesi şarkıyı dinledi ve gülümsedi. "Teşekkürler, Niloya, fiyonk bana çok yakıştı!" dedi annesi. Sonra annesi Niloya'yı yine salıncakta sallamaya başladı. Niloya bundan sonra fazla fiyonk olunca hep paylaştı.
```

**Hakem bulguları (8):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yüzü somurtkan oldu"
   - Cümle 3: «Annesinin yanında toka yoktu ve yüzü somurtkan oldu.»
   - Açıklama: 'somurtkan olmak' yüz için yanlış kullanım; 'yüzü asıldı' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yüzü somurtkan oldu"
   - Cümle 3: «Annesinin yanında toka yoktu ve yüzü somurtkan oldu.»
   - Açıklama: 'Somurtkan' küçük çocuğa ağır bir kelime ve 'yüzü somurtkan oldu' kuruluşu doğal değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "annesine en sevdiği şarkıyı söyledi"
   - Cümle 8: «Bu sırada annesine en sevdiği şarkıyı söyledi.»
   - Açıklama: Şarkının Niloya'nın mı annesinin mi en sevdiği olduğu belli değil.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "annesine en sevdiği şarkıyı"
   - Cümle 8: «Bu sırada annesine en sevdiği şarkıyı söyledi.»
   - Açıklama: Şarkının Niloya'nın mı annesinin mi en sevdiği olduğu belli değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu sırada annesine en sevdiği şarkıyı söyledi"
   - Cümle 8: «Bu sırada annesine en sevdiği şarkıyı söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümünde işe yaramıyor; sorunu fiyonk çözüyor, şarkı süs olarak ekleniyor.
   - Açıklama: Tohumdaki şarkı özelliği sorunu çözmüyor; sorun fiyonkla çözülüyor ve şarkı süs olarak kalıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu sırada annesine en sevdiği şarkıyı söyledi"
   - Cümle 8: «Bu sırada annesine en sevdiği şarkıyı söyledi.»
   - Açıklama: Şarkı söyleme sorunla ya da çözümle ilgisiz, işlevsiz bir ayrıntı.
   - Açıklama: Şarkı sorunla ya da çözümle ilgisiz, işlevsiz bir ayrıntı.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fazla fiyonk olunca hep paylaştı"
   - Cümle 12: «Niloya bundan sonra fazla fiyonk olunca hep paylaştı.»
   - Açıklama: Cümle bozuk; 'fazla fiyonku olunca' gibi iyelik eki eksik.
8. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fazla fiyonk olunca hep"
   - Cümle 12: «Niloya bundan sonra fazla fiyonk olunca hep paylaştı.»
   - Açıklama: İyelik eki eksik; 'fazla fiyonku olunca' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0005` birebir aynı, `@degisim: kilitlemek -> bağlamak` (tutuyorsan), ardından `@onarim: 0b18b7a58a27ddc1603364fc0fdb8d3e728eef93`, sonra gövde.

### Hikâye 4: tohum niloya-0009 (deneme 2 -> 3)

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
Niloya ile babaannesi parkta bir kağıda resim çiziyordu. İkisi de kağıttaki güneşi boyamak istiyordu. Ama yanlarında ucunda silgi olan tek bir turuncu kalem vardı. Niloya biraz düşündü. "Babaanne, sırayla boyayalım," dedi Niloya. "Şarkım bitince kalem sende olsun." Sonra neşeli bir şarkı söyledi ve güneşin yarısını boyadı. Şarkı bitince kalemi babaannesine verdi. Babaannesi önce silgiyle yamuk bir çizgiyi sildi. Sonra güneşin öbür yarısını turuncuya boyadı. Resim bitti. "Sırayla yapınca ne güzel oldu!" dedi babaannesi. Niloya bundan sonra tek kalem olunca hep sırayla kullandı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Babaannesi önce silgiyle yamuk bir çizgiyi sildi"
   - Cümle 9: «Babaannesi önce silgiyle yamuk bir çizgiyi sildi.»
   - Açıklama: Kalemin silgisi özenle kuruluyor ama sıra sorunuyla ilgisiz, işlevsiz bir ayrıntı olarak kalıyor.
   - Açıklama: Silgi ve yamuk çizgi sebepsiz beliriyor ve sorunun çözümünde hiçbir işe yaramıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "tek kalem olunca hep sırayla kullandı"
   - Cümle 13: «Niloya bundan sonra tek kalem olunca hep sırayla kullandı.»
   - Açıklama: Tekil özneyle 'sırayla kullandı' eksik kalıyor; nesne ve kiminle sırayla kullandığı belirtilmemiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0009` birebir aynı, `@degisim: yemek -> çizmek` (tutuyorsan), ardından `@onarim: b6c6d8ff24120d00298f704f25e7f76074ebbc73`, sonra gövde.

### Hikâye 5: tohum niloya-0010 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: dedesinin önüne hiç fındık düşmedi | şarkı söyleyip dedesini çağırdı ve fındık verdi
@tohum: niloya-0010
Ormanda serin bir rüzgar esiyordu, hava çok ferah ve güzeldi. Rüzgar dalları savurdu ve fındıklar yalnız Niloya'nın önüne düştü. Biraz uzakta duran dedesinin önüne ise hiç fındık düşmedi. Niloya önlüğünün büyük cebini fındıkla doldurdu. Sonra dedesini çağırmak için onun sevdiği şarkıyı söyledi. Dedesi şarkıyı duyunca gülümseyerek yanına geldi. "Dede, bu fındıklar ikimizin," dedi Niloya. Cebindeki fındıkların yarısını dedesinin avucuna koydu. "Paylaşmak çok güzel, kızım," dedi dedesi. Dedesi fındıkları kendi cebine koydu. Niloya çok sevindi, çünkü dedesinin eli artık boş değildi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hava çok ferah ve güzeldi"
   - Cümle 1: «Ormanda serin bir rüzgar esiyordu, hava çok ferah ve güzeldi.»
   - Açıklama: 'Ferah' kelimesi 3 yaşındaki çocuğun bilmeyeceği soyut bir kelimedir.
   - Açıklama: 'Ferah' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "fındıklar yalnız Niloya'nın önüne düştü"
   - Cümle 2: «Rüzgar dalları savurdu ve fındıklar yalnız Niloya'nın önüne düştü.»
   - Açıklama: Rüzgarın fındıkları yalnız Niloya'nın önüne düşürmesi akla yatkın bir sebep değil.
   - Açıklama: Rüzgarın fındıkları yalnız Niloya'nın önüne düşürmesi akla yatkın olmayan, zorlama bir sebep.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Dedesi fındıkları kendi cebine koydu"
   - Cümle 10: «Dedesi fındıkları kendi cebine koydu.»
   - Açıklama: Dede fındıkları cebine koyduğu halde son cümle elinin artık boş olmadığını söylüyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "dedesinin eli artık boş değildi"
   - Cümle 11: «Niloya çok sevindi, çünkü dedesinin eli artık boş değildi.»
   - Açıklama: Dedesi fındıkları cebine koymuşken son cümle elinin artık boş olmadığını söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0010` birebir aynı, ardından `@onarim: e94bebd3ef89100729b536f35554d2ae3ae20ba0`, sonra gövde.

### Hikâye 6: tohum niloya-0012 (deneme 1 -> 2)

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
Evin bahçesinde serin bir rüzgar esiyordu. Niloya'nın kaplumbağası Tospik uyumak istiyordu ama toprak çok serindi. "Niloya, bana sıcak bir yer bulur musun?" diye sordu Tospik. Niloya merakla bahçeyi dolaştı ve her yere baktı. Evin yanında güneş alan düz bir taş buldu. Taşa elini koydu, taş eline ılık geldi. Niloya eski ve yumuşak bir giysi getirdi ve taşın üstüne serdi. Tospik yavaş yavaş yürüdü ve onun üstüne çıktı. "Burayı çok beğendim, teşekkürler, Niloya!" dedi Tospik. Tospik orada rahatça uyudu, Niloya da onun yanında oturup gülümsedi.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yürüdü ve onun üstüne çıktı"
   - Cümle 8: «Tospik yavaş yavaş yürüdü ve onun üstüne çıktı.»
   - Açıklama: 'Onun' zamirinin taşı mı giysiyi mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0012` birebir aynı, ardından `@onarim: d4b1f8f7d3b8f88d0e0b42d000d048889dfd8cbd`, sonra gövde.

### Hikâye 7: tohum niloya-0013 (deneme 1 -> 2)

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
Niloya ormandaydı ve güneş yeni doğuyordu. Niloya ince bir dalı yuvarlak yapıp yapraklardan bir taç yaptı. Ama taç çok büyüktü ve başından gözlerine kaydı. Niloya tacı çıkardı ve ona uzun uzun baktı. Sonra bir soru düşündü: Dal çok mu uzundu? Dalı başının çevresine tuttu ve gerçekten çok uzun olduğunu gördü. Niloya dalın iki ucunu biraz daha üst üste getirdi. Dalı kırmamak için çok dikkatli davrandı. Uçları sıkıca birbirine sardı. Taç bu kez tam başına oturdu. Niloya yapraklı tacıyla ormanda neşeyle dolaştı. Niloya bundan sonra taç yaparken önce dalı başına göre ölçtü.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "dalı yuvarlak yapıp yapraklardan bir taç yaptı"
   - Cümle 2: «Niloya ince bir dalı yuvarlak yapıp yapraklardan bir taç yaptı.»
   - Açıklama: Aynı cümlede 'yapıp' ve 'yaptı' gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0013` birebir aynı, `@degisim: pedal -> dal` (tutuyorsan), ardından `@onarim: 3ab9e0c459e2924fe65fea5f00258aafe6213200`, sonra gövde.

### Hikâye 8: tohum niloya-0014 (deneme 1 -> 2)

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
Yaylada tatlı bir rüzgar esiyordu. Niloya ile annesi bir dala kağıt takıp gemi oyunu oynuyordu. Ama rüzgar birden kuvvetli esti ve kağıt yelken yırtıldı. Niloya şaşkın bir yüzle yelkene baktı. "Anne, kağıt neden yırtıldı?" diye sordu Niloya. "Tek kat kağıt çok ince, kızım," dedi annesi. Niloya çantadan yeni bir kağıt çıkardı. Kağıdı ikiye katladı ve dala sıkıca taktı. Rüzgar yine esti ama kalın yelken sağlam kaldı. "Gemimiz yola devam ediyor!" dedi annesi ve güldü. Niloya bundan sonra yelkenleri hep iki kat kağıttan yaptı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yaylada tatlı bir rüzgar"
   - Cümle 1: «Yaylada tatlı bir rüzgar esiyordu.»
   - Açıklama: 'Tatlı rüzgar' mecazlı bir kullanımdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0014` birebir aynı, ardından `@onarim: 978896c2b168ff4096d6d5427e96f9b3aef8a182`, sonra gövde.

### Hikâye 9: tohum niloya-0015 (deneme 1 -> 2)

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
@plan: karşı tepeden aynı ses geri geldi | şarkı söyleyip sesin kendi sesleri olduğunu buldu
@tohum: niloya-0015
@degisim: leke -> rüzgar
Tepelerde hafif bir rüzgar esiyordu. Niloya ile Mete kekik toplarken Mete "Buldum!" diye bağırdı. Karşı tepeden de aynı ses geri geldi. "Bu ses nereden geliyor?" diye sordu Mete. Niloya karşı tepeye baktı ama orada kimseyi göremedi. Sonra en sevdiği şarkıyı yüksek sesle söyledi. Biraz sonra aynı şarkı tepeden duyuldu. "Mete, bu bizim sesimiz, tepe onu bize geri gönderiyor!" dedi Niloya. Mete güldü ve kalın sesini de şarkıya kattı. Tepeden bu kez iki ses birden geldi. İki arkadaş şarkı söyleyerek kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sesin kendi sesleri olduğunu buldu"
   - Cümle 0 (plan satırı): «karşı tepeden aynı ses geri geldi | şarkı söyleyip sesin kendi sesleri olduğunu buldu»
   - Açıklama: Tekil özneli 'buldu' ile çoğul iyelikli 'kendi sesleri' uyumsuz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "tepe onu bize geri gönderiyor"
   - Cümle 8: «"Mete, bu bizim sesimiz, tepe onu bize geri gönderiyor!" dedi Niloya.»
   - Açıklama: Tepe ses göndermez; kişileştirme 3 yaşındaki çocuğa uygun değil.
   - Açıklama: Tepenin sesi geri göndermesi kişileştirme ve mecaz; küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0015` birebir aynı, `@degisim: leke -> rüzgar` (tutuyorsan), ardından `@onarim: 41b1acd6e6b1a5b055f55e7adadd8c9f670a0973`, sonra gövde.

### Hikâye 10: tohum niloya-0016 (deneme 1 -> 2)

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
Bir sabah Niloya parkta yeni ve büyük bir salıncak gördü. Salıncak biraz tozluydu, Niloya onu eliyle sildi. Sonra merakla salıncağa bindi ama salıncak hiç sallanmadı. Niloya kıpırdamadan oturuyordu. Niloya salıncağın iplerine baktı ve düşündü. Sonra ayaklarını öne uzattı ve geriye çekti. Salıncak biraz ileri gitti ve geri geldi. Niloya bunu birkaç kez yaptı. Salıncak ileri geri güzelce sallanmaya başladı. Serin rüzgar yüzüne esti. Niloya yeni salıncakta mutlu mutlu sallandı ve güldü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Salıncak biraz tozluydu, Niloya onu eliyle sildi"
   - Cümle 2: «Salıncak biraz tozluydu, Niloya onu eliyle sildi.»
   - Açıklama: Toz ve silme olayı hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Toz silme olayı sonraki olaylarla bağlantısız, işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0016` birebir aynı, `@degisim: inci -> salıncak` (tutuyorsan), ardından `@onarim: 4f46985f9f5ae0260e5d0ac98aa393bbf18f7f3d`, sonra gövde.

### Hikâye 11: tohum niloya-0017 (deneme 1 -> 2)

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
Bir sabah Niloya ormanda fındık topluyordu. Birden ağaçların arasında, yerdeki küçük suda beyaz, yuvarlak bir şey gördü. Niloya bir soru düşündü: Suya ay mı düşmüştü? Suyun yanına eğildi ve ona dikkatle baktı. Parmağıyla suya dokununca beyaz şey titredi ve dağıldı. Su durunca beyaz şey yine yerine geldi. Niloya başını kaldırıp gökyüzüne baktı. Ağaçların üstünde beyaz ay duruyordu. Su bir ayna gibiydi. Ay gökyüzündeydi, suda yalnız görünüyordu. Niloya gülümsedi ve fındıkları neşeyle eve götürdü.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya bir soru düşündü"
   - Cümle 3: «Niloya bir soru düşündü: Suya ay mı düşmüştü?»
   - Açıklama: 'Soru düşünmek' doğal bir kullanım değil; 'merak etti' ya da 'kendine sordu' anlamı bozuk.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya bir soru düşündü"
   - Cümle 3: «Niloya bir soru düşündü: Suya ay mı düşmüştü?»
   - Açıklama: Tohumdaki özellik 'merak ettiği her şeyi sorar' iken Niloya kimseye sormuyor, soruyu yalnız düşünüyor; özellik kartın güvenli kullanım satırındaki 'sorarak' biçimiyle kullanılmamış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Su bir ayna gibiydi"
   - Cümle 9: «Su bir ayna gibiydi.»
   - Açıklama: Benzetme 3 yaşındaki çocuk için soyut bir anlatım.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "suda yalnız görünüyordu"
   - Cümle 10: «Ay gökyüzündeydi, suda yalnız görünüyordu.»
   - Açıklama: 'Yalnız' burada 'tek başına' olarak da okunabiliyor; 'yalnızca suda görünüyordu' denmeli.
   - Açıklama: 'Yalnız' burada 'sadece' anlamında kullanılmış ama 'tek başına' diye okunuyor; anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0017` birebir aynı, `@degisim: yetenekli -> yuvarlak` (tutuyorsan), ardından `@onarim: 632daf238d6adcd3959048535500c51e1bcb064b`, sonra gövde.

### Hikâye 12: tohum niloya-0018 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: ağabeyi çok uykuluydu ve sürprizi göremiyordu | şarkı söyleyip ağabeyini uyandırdı ve filizi gösterdi
@tohum: niloya-0018
Ormanda fındık ağaçlarının altında Niloya küçük, yeşil bir filiz buldu. Onu bir sürprizle Murat'a göstermek istedi. Ama Murat topunu çok zıplattı ve şimdi uykuluydu. Bir ağacın yanında oturmuş, gözlerini kapatıyordu. Niloya önce filizin çevresine küçük taşlar dizdi. Sonra Murat'ın yanına gidip neşeli bir şarkı söyledi. Murat şarkıyı duyunca gözlerini açtı ve gülümsedi. "Abi, gel, sana bir sürprizim var!" dedi Niloya. Murat kalktı ve taşların ortasındaki filizi gördü. "Ne güzel, Niloya, yeni bir fındık ağacı!" dedi Murat. İkisi taşların yanında sevinçle el çırptı. Niloya bundan sonra güzel bir şey görünce hemen ağabeyine gösterdi.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Onu bir sürprizle Murat'a"
   - Cümle 2: «Onu bir sürprizle Murat'a göstermek istedi.»
   - Açıklama: 'Bir sürprizle göstermek' dilbilgisel olarak yanlış kurulmuş; 'sürpriz yapmak için' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Murat topunu çok zıplattı ve şimdi uykuluydu"
   - Cümle 3: «Ama Murat topunu çok zıplattı ve şimdi uykuluydu.»
   - Açıklama: Önceki olay için -mişti gerekir; 'zıplatmıştı' olmalı.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Murat topunu çok zıplattı ve şimdi uykuluydu"
   - Cümle 3: «Ama Murat topunu çok zıplattı ve şimdi uykuluydu.»
   - Açıklama: Önceki olay '-mıştı' ile verilmeli; 'şimdi' ile zaman sırası kayıyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Murat topunu çok zıplattı ve şimdi uykuluydu"
   - Cümle 3: «Ama Murat topunu çok zıplattı ve şimdi uykuluydu.»
   - Açıklama: Top zıplatmaktan uykulu olmak zayıf bir sebep ve uykulu ağabeyin sürprizi görememesi çocuğun önemseyeceği bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0018` birebir aynı, ardından `@onarim: 8f954915cab28df4cb0501d4467d32a48c103586`, sonra gövde.
