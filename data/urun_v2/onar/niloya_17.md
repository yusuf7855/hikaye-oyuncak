# Editör görevi (onarım): Niloya, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar17.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0020 (deneme 5 -> 6)

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
@plan: kekik toplarken trompet cebinden kaydı ve çimenlere düştü | geldiği yoldan geri yürüyüp çalıların yanına baktı
@tohum: niloya-0020
@degisim: kurmak -> bulmak
Niloya yeşil tepede en sevdiği oyuncak trompeti çalıyordu. Sonra trompeti cebine koydu ve kekik toplamaya başladı. Ama Niloya kekik toplarken trompet cebinden kaydı ve çimenlere düştü. Niloya biraz sonra cebine baktı ama trompeti göremedi. Niloya çok üzüldü. Niloya aceleci davranmadı ve geldiği yoldan yavaş yavaş geri yürüdü. Kekik topladığı her çalının yanına merakla baktı. İlk çalının yanında hiçbir şey yoktu. İkinci çalının dibinde, çimenlerde sarı bir şey parlıyordu. Kayıp trompet oradaydı! Niloya trompeti aldı ve neşeyle üfledi. Yine güzel bir ses çıktı. Niloya çok sevindi, çünkü en sevdiği trompetini bulmuştu.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya çok üzüldü"
   - Cümle 5: «Niloya çok üzüldü.»
   - Açıklama: Art arda dört cümle 'Niloya' ile başlıyor; ad gereksiz tekrar ediliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya aceleci davranmadı"
   - Cümle 6: «Niloya aceleci davranmadı ve geldiği yoldan yavaş yavaş geri yürüdü.»
   - Açıklama: 'Aceleci davranmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya aceleci davranmadı ve"
   - Cümle 6: «Niloya aceleci davranmadı ve geldiği yoldan yavaş yavaş geri yürüdü.»
   - Açıklama: 'Aceleci davranmak' 3 yaşındaki çocuğa soyut bir kavram.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya aceleci davranmadı ve"
   - Cümle 6: «Niloya aceleci davranmadı ve geldiği yoldan yavaş yavaş geri yürüdü.»
   - Açıklama: 'Niloya' adı art arda dört cümlenin başında gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0020` birebir aynı, `@degisim: kurmak -> bulmak` (tutuyorsan), ardından `@onarim: ee5d593395e1960f64889704cd60f7ade5df7323`, sonra gövde.

### Hikâye 2: tohum niloya-0022 (deneme 5 -> 6)

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
@plan: havuç kaydırağın altına sıkıştı ve kaplumbağa yetişemedi | kolunu uzatıp havucu çıkardı ve kaplumbağaya verdi
@tohum: niloya-0022
@degisim: sıkmak -> sıkışmak
Parkta Niloya, Tospik'e küçük sebze parçaları veriyordu. Bir havuç parçası yere düştü ve kaydırağın alçak ucunun altına yuvarlandı. Tospik havucun peşinden gitti ama kabuğu kaydırağın altına sığmadı. Niloya merakla eğildi ve baktı. Havuç kaydırağın altına sıkışmıştı ve Tospik ona yetişemiyordu. "Bana yardım eder misin, Niloya?" diye sordu Tospik. "Tabii, Tospik," dedi Niloya. Niloya kolunu kaydırağın altına uzattı. Havucu parmaklarıyla tuttu ve yavaşça çekip çıkardı. "Al, Tospik, havucun burada," dedi Niloya. Tospik havucu afiyetle yedi ve ikisi parkta mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Havuç kaydırağın altına sıkışmıştı"
   - Cümle 5: «Havuç kaydırağın altına sıkışmıştı ve Tospik ona yetişemiyordu.»
   - Açıklama: Havucun kaydırağın altına gittiği ve Tospik'in ulaşamadığı 2. ve 3. cümlelerde zaten anlatılmıştı; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0022` birebir aynı, `@degisim: sıkmak -> sıkışmak` (tutuyorsan), ardından `@onarim: 8d2ee7949f4d9af517411e326c62849cc089bbbd`, sonra gövde.

### Hikâye 3: tohum niloya-0026 (deneme 5 -> 6)

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
@plan: rüzgarda sallanan sepet uyuyan babaannenin yanında ses yapıyordu | sesin sepetten geldiğini bulup sepeti daldan indirdi
@tohum: niloya-0026
@degisim: kremalı -> boş
Rüzgar esiyordu ve ağaçların arasından tak tak bir ses geliyordu. Niloya'nın babaannesi yorulmuştu ve küçük bir taburede uyuyordu. Niloya babaannesinin rahat rahat uyumasını istedi. Sesi bulmak için etrafa baktı. Babaannesinin boş sepeti alçak bir dala asılıydı. Sepet rüzgarda sallanıyor ve ağaca çarpıyordu. Niloya sepeti daldan yavaşça indirdi ve yere koydu. Ses hemen kesildi. Niloya onun yanına oturdu ve yumuşak bir şarkı söyledi. Babaannesi uykusunda gülümsedi ve tatlı tatlı uyudu. Niloya da onun yanında mutlu mutlu dinlendi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Niloya onun yanına oturdu"
   - Cümle 9: «Niloya onun yanına oturdu ve yumuşak bir şarkı söyledi.»
   - Açıklama: Son anılan varlık sepet olduğu için 'onun' zamirinin babaanneyi gösterdiği belli değil.
   - Açıklama: Son anılan adlar ses ve sepet olduğu için 'onun' zamirinin babaanneyi gösterdiği belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "yumuşak bir şarkı söyledi"
   - Cümle 9: «Niloya onun yanına oturdu ve yumuşak bir şarkı söyledi.»
   - Açıklama: Sorun sepeti indirerek çözülmüş, şarkı özelliği çözüme katkı vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0026` birebir aynı, `@degisim: kremalı -> boş` (tutuyorsan), ardından `@onarim: 38ddf1782bdfc95764f687d4ea77daba1c442e6c`, sonra gövde.

### Hikâye 4: tohum niloya-0037 (deneme 4 -> 5)

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
Ormanda kuşlar ötüyordu. Niloya ağaçların dibinde küçük kırmızı güller gördü. Ama rüzgarın getirdiği plastik bir poşet güllerin üstüne takılmıştı. Poşet çiçeklerin çoğunu kapatıyordu. Niloya güllerin hepsini görmek istedi. Niloya merakla güllerin etrafında dolaştı ve dikkatle baktı. Poşet yalnız bir ucundan takılmıştı. Niloya öbür ucunu tuttu ve poşeti yavaşça çekip çıkardı. Hiçbir çiçek ezilmedi. Sonra poşeti küçük küçük katladı ve cebine koydu. Niloya çok sevindi, çünkü bütün kırmızı güller yeniden görünüyordu.
```

**Hakem bulguları (1):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "ağaçların dibinde küçük kırmızı güller"
   - Cümle 2: «Niloya ağaçların dibinde küçük kırmızı güller gördü.»
   - Açıklama: Kartın orman tarifi meyve ve fındık ağaçlarıyla sınırlı; ağaç dibinde güller bu tarife uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0037` birebir aynı, `@degisim: paylaşmak -> katlamak` (tutuyorsan), ardından `@onarim: 5bed59824d489fbc5b729cabfa2120e2d5976e07`, sonra gövde.

### Hikâye 5: tohum niloya-0038 (deneme 4 -> 5)

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
Bir sabah Niloya ile Mete parka geldi. Parkta yalnız bir salıncak vardı ve ikisi de binmek istedi. Aynı anda salıncağa koştular. "Sırayla binelim, Mete, önce sen bin, şarkı bitince de ben," dedi Niloya. Mete sevindi ve ilk o oturdu. Niloya onu hafifçe itti ve yüksek sesle neşeli bir şarkı söyledi. Şarkı bitince Mete hemen indi. "Sıra sende, Niloya," dedi Mete. Bu kez Mete salıncağı güçlü kollarıyla itti ve aynı şarkıyı söyledi. Mete susunca Niloya indi ve gülerek Mete'yi gıdıkladı. "Bu şarkı oyunu çok güzel, Mete, yine oynayalım!" dedi Niloya.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Mete salıncağı güçlü kollarıyla itti"
   - Cümle 9: «Bu kez Mete salıncağı güçlü kollarıyla itti ve aynı şarkıyı söyledi.»
   - Açıklama: Küçük bir çocuğun salıncağı güçlü kollarla itmesi taklit edilince düşmeye yol açabilecek bir davranış.
2. **C6** (K merceği) — Kalıp yargı yok.
   - Alıntı: "Mete salıncağı güçlü kollarıyla itti"
   - Cümle 9: «Bu kez Mete salıncağı güçlü kollarıyla itti ve aynı şarkıyı söyledi.»
   - Açıklama: Niloya hafifçe iterken oğlan Mete'nin güçlü kollarıyla itmesi cinsiyete dayalı kalıp yargıyı pekiştiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0038` birebir aynı, `@degisim: nilüfer -> salıncak` (tutuyorsan), ardından `@onarim: 84dc088385cff041ef1358f7215c02717c5bcd3a`, sonra gövde.

### Hikâye 6: tohum niloya-0039 (deneme 4 -> 5)

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
Parkta güneşli bir sabah Niloya yerde oturmuş, topunu kaydırağa yuvarlıyordu. Top her seferinde geri geliyordu ve Niloya gülüyordu. Ama bir kez top hızla geri geldi ve bankın altına kaçtı. Niloya hemen kalktı ve bankın yanına koştu. Top bankın altında, arka köşede duruyordu. Niloya kolunu uzattı ama topa yetişemedi. Niloya'nın bir sorusu vardı: Bankın arkasından topa yetişebilir miydi? Niloya bankın arkasına geçti ve topu kolayca aldı. Bu kez topu kaydırağa daha yavaş yuvarladı. Top kaydıraktan indi ve tam Niloya'nın önünde durdu. Niloya çok memnun oldu ve oyununa neşeyle devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya'nın bir sorusu vardı"
   - Cümle 7: «Niloya'nın bir sorusu vardı: Bankın arkasından topa yetişebilir miydi?»
   - Açıklama: Kimseye sorulmayan içten merak 'sorusu vardı' diye anlatılmış; 'merak etti' ya da 'düşündü' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya'nın bir sorusu vardı"
   - Cümle 7: «Niloya'nın bir sorusu vardı: Bankın arkasından topa yetişebilir miydi?»
   - Açıklama: Tohumdaki soru özelliği kimseye sorulmayan iç soru olarak geçiyor, karttaki 'merak ettiği her şeyi sorar' biçiminde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0039` birebir aynı, `@degisim: turp -> top` (tutuyorsan), ardından `@onarim: 9de39b46380c4cc8b11ab81ee63f8ce69ebeeba2`, sonra gövde.

### Hikâye 7: tohum niloya-0045 (deneme 3 -> 4)

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
Güneş parlıyordu. Bugün babaannesinin doğum günüydü ve Niloya parkta ona kumdan pasta yapmak istedi. Ama kum un gibi kuruydu ve pasta hemen dağıldı. "Babaanne, biraz su var mı?" diye sordu Niloya. "Var, al bakalım," dedi babaannesi ve su şişesini verdi. Niloya kumu biraz ıslattı ve yeniden şekil verdi. Bu kez pasta sağlam kaldı. Niloya onu incecik bir dalla süsledi. Sonra babaannesini pastanın yanına çağırdı. "İyi ki doğdun, babaanneciğim!" dedi Niloya. Babaannesi Niloya'ya sıkıca sarıldı ve ikisi parkta mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kum un gibi kuruydu"
   - Cümle 3: «Ama kum un gibi kuruydu ve pasta hemen dağıldı.»
   - Açıklama: 'Un gibi' benzetmesi mecazlı anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0045` birebir aynı, `@degisim: uyutmak -> süslemek` (tutuyorsan), ardından `@onarim: 7841dd62e5b07316aa688e892de162991ef2397e`, sonra gövde.

### Hikâye 8: tohum niloya-0047 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | annesi
@tohum: niloya-0047
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'lamba', fiil 'üflemek', sıfat 'gururlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | annesi
@plan: kaydıraktan kayarken annesinin tokasını otlara düşürdü | özür diledi ve kaydırağın altına bakıp tokayı buldu
@tohum: niloya-0047
@degisim: lamba -> toka
Parkta Niloya annesinin mavi tokasını saçına takmıştı. Sonra tokayı çıkarmadan kaydıraktan hızla kaydı ve toka otların içine düştü. Annesi bankta oturuyordu. Niloya hemen annesinin yanına gitti. "Özür dilerim, anne, tokanı düşürdüm," dedi Niloya. "Gel, birlikte bakalım," dedi annesi. Niloya kaydırağın altına merakla baktı. Orada mavi bir şey parlıyordu. Niloya tokayı aldı ve üstündeki tozu üfledi. Sonra onu annesine uzattı. Annesi gülümsedi ve Niloya'ya sarıldı. Niloya çok sevindi ve gururlu oldu, çünkü tokayı kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çok sevindi ve gururlu oldu"
   - Cümle 12: «Niloya çok sevindi ve gururlu oldu, çünkü tokayı kendisi bulmuştu.»
   - Açıklama: 'Gururlu oldu' doğal olmayan bir kullanım ve 'gurur' küçük çocuk için soyut bir kavram.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sevindi ve gururlu oldu"
   - Cümle 12: «Niloya çok sevindi ve gururlu oldu, çünkü tokayı kendisi bulmuştu.»
   - Açıklama: 'Gururlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmeyebilir ve 'gururlu oldu' doğal bir kullanım değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0047` birebir aynı, `@degisim: lamba -> toka` (tutuyorsan), ardından `@onarim: 6d3eb53a955273107e1d1d615950424800dba5b1`, sonra gövde.

### Hikâye 9: tohum niloya-0052 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0052
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'havlu', fiil 'saçmak', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: yağmur damlaları küçük çiçeğin sapını eğdi | havluyu çiçeğin üstünde tuttu ve bekledi
@tohum: niloya-0052
@degisim: narin -> küçük
Niloya ormanda havlusunun üstünde, küçük mor bir çiçeğin yanında oturuyordu. Birden yağmur başladı ve iri damlalar çiçeğin ince sapını eğdi. Niloya çiçeği korumak istedi. Hemen kalktı ve havluyu iki eliyle çiçeğin üstünde tuttu. Damlalar artık havluya düşüyordu. Niloya beklerken en sevdiği yağmur şarkısını söyledi. Az sonra yağmur dindi ve güneş çıktı. Niloya havluyu salladı ve suyu etrafa saçtı. Mor çiçeğin sapı yavaşça doğruldu. Niloya dik duran çiçeğe gülümsedi ve ormanda mutlu mutlu gezmeye başladı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "en sevdiği yağmur şarkısını söyledi"
   - Cümle 6: «Niloya beklerken en sevdiği yağmur şarkısını söyledi.»
   - Açıklama: Çiçek havluyla korunuyor, şarkı özelliği çözüme katkı vermiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya beklerken en sevdiği yağmur şarkısını söyledi"
   - Cümle 6: «Niloya beklerken en sevdiği yağmur şarkısını söyledi.»
   - Açıklama: Çiçeği havlu koruyor; tohumdaki şarkı özelliği çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0052` birebir aynı, `@degisim: narin -> küçük` (tutuyorsan), ardından `@onarim: af58118d64cdd1ed66dcbf895989529a1d82d289`, sonra gövde.

### Hikâye 10: tohum niloya-0054 (deneme 2 -> 3)

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
@plan: toprak sertti ve küçük kürek zor giriyordu | tırmıkla toprağı kazdı ve bir fındığı arkadaşına verdi
@tohum: niloya-0054
@degisim: fırçalamak -> dikmek
Bir sabah Niloya ile Tospik ormandaki devasa fındık ağacının altına geldi. Niloya küçük küreğiyle bir fındık dikmek istiyordu. Ama toprak çok sertti ve kürek zor giriyordu. Sepette bir alet daha vardı, küçük bir tırmık. Niloya tırmıkla toprağı kazdı ve iki çukur açtı. Tospik ağacın altında uyuyordu. Niloya neşeli bir şarkı söyledi ve Tospik uyandı. "Tospik, bu fındık senin," dedi Niloya. "Sağ ol, Niloya," dedi Tospik. Niloya fındıkları çukurlara koydu ve üstünü toprakla örttü. Niloya bundan sonra fındıklarını hep arkadaşlarıyla paylaştı.
```

**Hakem bulguları (11):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "bir fındığı arkadaşına verdi"
   - Cümle 0 (plan satırı): «toprak sertti ve küçük kürek zor giriyordu | tırmıkla toprağı kazdı ve bir fındığı arkadaşına verdi»
   - Açıklama: Fındığı arkadaşına vermek sert toprak sorununun çözümü değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormandaki devasa fındık ağacının"
   - Cümle 1: «Bir sabah Niloya ile Tospik ormandaki devasa fındık ağacının altına geldi.»
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime; 'çok büyük' olmalı.
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tospik ağacın altında uyuyordu"
   - Cümle 6: «Tospik ağacın altında uyuyordu.»
   - Açıklama: Tospik'in uyuması ve şarkıyla uyanması sert toprak sorunuyla ilgisiz, işlevsiz bir ayrıntı.
   - Açıklama: Uyuyan Tospik ve şarkı olaydan çıkmıyor ve sorunun çözümüne hiçbir katkı yapmıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya neşeli bir şarkı söyledi"
   - Cümle 7: «Niloya neşeli bir şarkı söyledi ve Tospik uyandı.»
   - Açıklama: Tohumdaki şarkı özelliği sert toprak sorununun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Tospik, bu fındık senin"
   - Cümle 8: «"Tospik, bu fındık senin," dedi Niloya.»
   - Açıklama: Niloya fındığı Tospik'e veriyor ama sonra fındıkları kendisi çukurlara koyuyor; tek fındık için de iki çukur açılıyor.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fındıkları çukurlara koydu ve üstünü toprakla örttü"
   - Cümle 10: «Niloya fındıkları çukurlara koydu ve üstünü toprakla örttü.»
   - Açıklama: Çoğul 'fındıkları/çukurlara' ile tekil 'üstünü' uyumsuz; 'üstlerini' olmalı.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve üstünü toprakla örttü"
   - Cümle 10: «Niloya fındıkları çukurlara koydu ve üstünü toprakla örttü.»
   - Açıklama: Çoğul 'fındıkları' ile tekil 'üstünü' uyumsuz; 'üstlerini' olmalı.
8. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Niloya fındıkları çukurlara koydu"
   - Cümle 10: «Niloya fındıkları çukurlara koydu ve üstünü toprakla örttü.»
   - Açıklama: Niloya bir fındık dikmek istiyordu ve fındığı Tospik'e verdi, ama sonra birden çok fındığı çukurlara koyuyor.
9. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "fındıklarını hep arkadaşlarıyla paylaştı"
   - Cümle 11: «Niloya bundan sonra fındıklarını hep arkadaşlarıyla paylaştı.»
   - Açıklama: Notlanan çoğul canlı arkadaşlar paylaşma olayına katılıyor; kartta yalnız başlıktaki yan olmalı.
   - Açıklama: Notlanan çoğul canlı arkadaşlar paylaşımın alıcısı olarak olaya katılıyor.
10. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Niloya bundan sonra fındıklarını hep arkadaşlarıyla paylaştı"
   - Cümle 11: «Niloya bundan sonra fındıklarını hep arkadaşlarıyla paylaştı.»
   - Açıklama: Dikme sorununun yanına paylaşma konusu ikinci bir iplik olarak ekleniyor.
11. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Niloya bundan sonra fındıklarını hep arkadaşlarıyla paylaştı"
   - Cümle 11: «Niloya bundan sonra fındıklarını hep arkadaşlarıyla paylaştı.»
   - Açıklama: Paylaşma dersi yaşanan sert toprak sorunundan çıkmıyor.
   - Açıklama: Paylaşma dersi yaşanan olaydan çıkmıyor; hikayenin sorunu sert topraktı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0054` birebir aynı, `@degisim: fırçalamak -> dikmek` (tutuyorsan), ardından `@onarim: f4c23550177b14b58b072028d1b7f6e064ff014f`, sonra gövde.

### Hikâye 11: tohum niloya-0057 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0057
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kitaplık', fiil 'kırılmak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: öteki dallar kuruydu ve hemen kırılıyordu | tek sağlam dalı sırayla kullanıp resim çizdiler
@tohum: niloya-0057
@degisim: kitaplık -> dal
Rüzgar ağaçların arasında hafifçe esiyordu. Niloya bulduğu sağlam bir dalla toprağa resim çiziyordu. Mete de çizmek istedi ama yerdeki öteki dallar kuruydu ve hemen kırılıyordu. Niloya etrafa merakla baktı ama başka sağlam dal bulamadı. Dalı gülümseyerek Mete'ye uzattı ve ikisi sırayla çizmeye başladı. Önce Mete toprağa büyük bir ağaç çizdi. Sonra Niloya ağacın yanına küçük bir çiçek çizdi. Mete ağacın üstüne yuvarlak bir güneş ekledi. Niloya da güneşin altına el ele tutuşan iki çocuk çizdi. Resim bitince ikisi de ona bakıp güldü. Niloya çok sevindi, çünkü sırayla çizince kocaman bir resim yapmışlardı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya etrafa merakla baktı ama başka sağlam dal bulamadı"
   - Cümle 4: «Niloya etrafa merakla baktı ama başka sağlam dal bulamadı.»
   - Açıklama: Tohumdaki keşfet özelliği sonuçsuz kalıyor, sorunun çözümüne işe yarar biçimde katkı vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0057` birebir aynı, `@degisim: kitaplık -> dal` (tutuyorsan), ardından `@onarim: 243715e74b53ae51e437c8ab8d207657b7e5c537`, sonra gövde.

### Hikâye 12: tohum niloya-0058 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Tospik
@tohum: niloya-0058
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Tospik
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'soğan', fiil 'silmek', sıfat 'gürültülü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Tospik
@plan: koşarken çamura bastı ve arkadaşının kabuğu kirlendi | özür dileyip kabuğu bir yaprakla sildi
@tohum: niloya-0058
@degisim: soğan -> çamur
Kuşlar ağaçlarda gürültülü bir sesle ötüyordu. Niloya ileride kırmızı elmalı bir ağaç gördü ve merakla koştu. Koşarken yoldaki çamura bastı ve yanındaki Tospik'in kabuğu kirlendi. "Kabuğuma çamur sıçradı," dedi Tospik üzgün bir sesle. Niloya durdu ve Tospik'in yanına geri döndü. "Özür dilerim, Tospik, bakmadan koştum," dedi Niloya. Büyük bir yaprak aldı ve kabuğu yavaşça sildi. Kabuk yine tertemiz oldu. "Teşekkürler, Niloya, kabuğum şimdi parlıyor," dedi Tospik. Sonra ikisi elma ağacına birlikte yürüdü. Niloya çok sevindi, çünkü arkadaşı artık üzgün değildi.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "gördü ve merakla koştu"
   - Cümle 2: «Niloya ileride kırmızı elmalı bir ağaç gördü ve merakla koştu.»
   - Açıklama: Tohumdaki merak özelliği sorunu çözmekte işe yaramıyor, yalnız sorunu doğuruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0058` birebir aynı, `@degisim: soğan -> çamur` (tutuyorsan), ardından `@onarim: b76d9f15ec3967c97384f6e63a30bd9810bab50e`, sonra gövde.
