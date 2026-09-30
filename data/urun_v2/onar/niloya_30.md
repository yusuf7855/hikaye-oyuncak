# Editör görevi (onarım): Niloya, onarım partisi 30

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar30.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0108 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0108
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'palto', fiil 'somurtmak', sıfat 'hızlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: palto sandalyeden hep yere kaydı | neden kaydığını sordu ve düğmeleri kapattı
@tohum: niloya-0108
Niloya evde gemi oyunu oynuyordu. Gemisi iki sandalyeydi ama yelkeni yoktu. Niloya paltosunu bir sandalyeye astı ama palto hemen yere kaydı. Niloya onu yeniden astı ama palto yine düştü. Niloya biraz somurttu. Sonra bir soru sordu: Palto neden hep kayıyordu? Niloya iyice baktı. Düğmeler açıktı, bu yüzden palto duramıyordu. Niloya paltoyu sandalyenin arkasına geçirdi ve bütün düğmeleri kapattı. Bu kez palto dimdik durdu. Gemisinin artık bir yelkeni vardı. Niloya öbür sandalyeye oturdu ve hızlı bir gemi yolculuğuna çıktı. Niloya çok sevindi, çünkü yelkeni kendi başına kurmuştu.
```

**Hakem bulguları (4):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya onu yeniden astı ama palto yine düştü"
   - Cümle 4: «Niloya onu yeniden astı ama palto yine düştü.»
   - Açıklama: Cümleler art arda 'Niloya' ile başlayıp 'ama palto' kalıbını gereksiz tekrarlıyor.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Sonra bir soru sordu: Palto neden hep kayıyordu?"
   - Cümle 6: «Sonra bir soru sordu: Palto neden hep kayıyordu?»
   - Açıklama: Niloya soruyu kimseye değil kendi kendine soruyor.
3. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Sonra bir soru sordu"
   - Cümle 6: «Sonra bir soru sordu: Palto neden hep kayıyordu?»
   - Açıklama: Niloya soruyu kimseye değil kendine soruyor; kendi kendine konuşma.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu kez palto dimdik"
   - Cümle 10: «Bu kez palto dimdik durdu.»
   - Açıklama: Sandalyeye asılı palto dimdik durmaz; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0108` birebir aynı, ardından `@onarim: 09189e7294ad3c52f8bd6c68e554a8c98ca98e7a`, sonra gövde.

### Hikâye 2: tohum niloya-0109 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0109
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'ceviz', fiil 'çözülmek', sıfat 'kabarık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: torbanın ipi çözüldü ve cevizler yapraklara döküldü | yaprakların altına bakıp cevizleri tek tek buldu
@tohum: niloya-0109
Ormanda kuşlar ötüyordu. Niloya, Mete'nin doğum günü için bir torba ceviz getirmişti. Ama torbanın ipi çözüldü ve cevizler kabarık bir yaprak yığınına döküldü. Mete biraz uzakta, oyuncaklarıyla oynuyordu ve bunu görmedi. Niloya merakla yaprakları tek tek kaldırdı ve altlarına baktı. Cevizleri bulup torbaya koydu. Birkaç ceviz de bir ağacın köküne yuvarlanmıştı. Niloya oraya da baktı ve onları topladı. Sonra torbanın ipini sıkıca bağladı. "Mete, sana bir hediyem var!" dedi Niloya. Mete koşarak geldi ve torbayı açtı. "Çok teşekkür ederim, Niloya!" dedi Mete. İkisi ağacın altına oturdu ve cevizleri mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "torbanın ipi çözüldü"
   - Cümle 3: «Ama torbanın ipi çözüldü ve cevizler kabarık bir yaprak yığınına döküldü.»
   - Açıklama: İpin neden çözüldüğü söylenmiyor; sorunun sebebi yok.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya merakla yaprakları"
   - Cümle 5: «Niloya merakla yaprakları tek tek kaldırdı ve altlarına baktı.»
   - Açıklama: Kaybolan cevizleri arayan birine 'merakla' uymuyor; 'dikkatle' olmalı.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Birkaç ceviz de bir ağacın köküne yuvarlanmıştı"
   - Cümle 7: «Birkaç ceviz de bir ağacın köküne yuvarlanmıştı.»
   - Açıklama: Çözüm yaprakları kaldırma, köke bakma ve ipi bağlama olarak ikiden fazla adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0109` birebir aynı, ardından `@onarim: aaa3589e6835dfb67126435b141b6d57f2ae1a6b`, sonra gövde.

### Hikâye 3: tohum niloya-0110 (deneme 1 -> 2)

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
Niloya parkta top oynuyordu. Annesi bankta taze ekmek ve patates kızartması hazırlıyordu. Birden rüzgar esti ve hafif top uçup çiti aştı. Niloya çitin yanına koştu ve merakla çitin arasından baktı. Top çitin arkasındaki uzun otların arasındaydı. Çit yüksekti ve Niloya ona tırmanmadı. Hemen annesinin yanına koştu. "Anne, topum çitin arkasına düştü, bana yardım eder misin?" diye sordu Niloya. Annesi başını salladı ve parkın kapısından çıktı. Niloya çitin içinden parmağıyla topun yerini gösterdi. Annesi topu otların arasından aldı ve Niloya'ya verdi. "Teşekkürler, anneciğim, şimdi birlikte kızartma yiyelim!" dedi Niloya.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çitin yanına koştu ve merakla çitin arasından"
   - Cümle 4: «Niloya çitin yanına koştu ve merakla çitin arasından baktı.»
   - Açıklama: Aynı cümlede 'çitin' gereksiz yere tekrarlanıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çitin içinden parmağıyla topun"
   - Cümle 10: «Niloya çitin içinden parmağıyla topun yerini gösterdi.»
   - Açıklama: Çitin 'içinden' gösterilmez; 'çitin arasından' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya çitin içinden parmağıyla"
   - Cümle 10: «Niloya çitin içinden parmağıyla topun yerini gösterdi.»
   - Açıklama: 'Çitin içinden' yanlış anlamda; 'çitin arasından' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0110` birebir aynı, ardından `@onarim: cfe2af4b964c88052af751db6395e5f06d8c2476`, sonra gövde.

### Hikâye 4: tohum niloya-0112 (deneme 1 -> 2)

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
@plan: su şişesini bir yere bırakıp unuttu | en son nerede su içtiğini sordu ve şişeyi buldu
@tohum: niloya-0112
Tepede güneş çok sıcak parlıyordu. Niloya kekik topluyordu ve çok susamıştı. Ama su şişesini bir yere bırakmış ve unutmuştu. Şişede nane yapraklı serin su vardı. Niloya durdu ve bir soru sordu: Şişeden en son nerede su içmişti? Sonra hatırladı. Bozuk bir çitin yanında oturup su içmişti. Niloya tepeden aşağı yürüdü ve çite gitti. Şişe çitin dibinde, otların arasında duruyordu. Niloya şişeyi açtı ve sudan içti. Nane kokulu su onu hemen serinletti. Sonra Niloya kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya durdu ve bir soru sordu"
   - Cümle 5: «Niloya durdu ve bir soru sordu: Şişeden en son nerede su içmişti?»
   - Açıklama: Yanında kimse yokken Niloya soruyu kendi kendine soruyor.
   - Açıklama: Niloya dinleyen kimse yokken kendine soru soruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0112` birebir aynı, ardından `@onarim: a99af682b1a0f741c7a8f7b8412acacad9681d07`, sonra gövde.

### Hikâye 5: tohum niloya-0113 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Mete
@tohum: niloya-0113
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'küpe', fiil 'yayılmak', sıfat 'yepyeni'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Mete
@plan: oyuncaklar otlara yayılmıştı ve harita kaybolmuştu | merakla otlara bakıp haritayı kekiklerin arasında buldu
@tohum: niloya-0113
@degisim: küpe -> harita
Niloya tepede Mete ile harita oyunu oynuyordu. Mete yepyeni bir harita çizmişti ve haritada büyük bir kaya vardı. Ama Mete'nin oyuncakları otların üstüne yayılmıştı ve harita kaybolmuştu. "Harita olmadan kayayı bulamayız," dedi Mete. Niloya merakla eğildi ve otların arasına baktı. Sonra kekiklerin arasına da baktı. Harita kekiklerin arasında duruyordu. "Buldum, Mete!" dedi Niloya. İkisi haritaya baktı ve tepeye doğru yürüdü. Az sonra büyük kayayı gördüler. "Kayayı bulduk!" dedi Mete sevinçle. Niloya bundan sonra Mete'ye oyuncaklarını tek bir yere koymasını hatırlattı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Mete'nin oyuncakları otların üstüne yayılmıştı ve harita kaybolmuştu"
   - Cümle 3: «Ama Mete'nin oyuncakları otların üstüne yayılmıştı ve harita kaybolmuştu.»
   - Açıklama: Oyuncakların yayılması haritanın neden kaybolduğunu akla yatkın biçimde açıklamıyor.
   - Açıklama: Oyuncakların yayılmasıyla haritanın kaybolması arasındaki sebep bağı kurulmuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "oyuncakları otların üstüne yayılmıştı"
   - Cümle 3: «Ama Mete'nin oyuncakları otların üstüne yayılmıştı ve harita kaybolmuştu.»
   - Açıklama: Yayılan oyuncaklar bir daha ele alınmıyor ve olaya hiçbir işlev katmıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İkisi haritaya baktı ve tepeye doğru yürüdü"
   - Cümle 9: «İkisi haritaya baktı ve tepeye doğru yürüdü.»
   - Açıklama: Çocuklar zaten tepede oynarken tepeye doğru yürüyorlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0113` birebir aynı, `@degisim: küpe -> harita` (tutuyorsan), ardından `@onarim: c799b1c8859bdf5399f42619464501fe30f9ae47`, sonra gövde.

### Hikâye 6: tohum niloya-0115 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Murat
@tohum: niloya-0115
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Murat
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'peçete', fiil 'yüklemek', sıfat 'şirin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Murat
@plan: koşarken peçeteye takıldı ve fındıklar yuvarlandı | özür diledi ve fındıkları arayıp topladı
@tohum: niloya-0115
@degisim: yüklemek -> toplamak
Yeşil tepede Murat çimenlere beyaz bir peçete serdi ve üstüne fındık koydu. Niloya şirin bir çiçek görünce ona doğru hızla koştu. Ayağı peçeteye takıldı ve fındıklar her yere yuvarlandı. Murat boş peçeteyi görünce çok üzüldü. "Özür dilerim, abi, önüme bakmadan koştum," dedi Niloya. Sonra Niloya merakla her taşın ve her çalının arkasına baktı. Fındıkları otların arasında tek tek buldu. Hepsini topladı ve peçeteye geri koydu. Murat gülümsedi ve Niloya'ya sarıldı. "Sağ ol, Niloya, hepsi burada!" dedi Murat. Niloya bundan sonra koşarken hep önüne baktı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sonra Niloya merakla her taşın"
   - Cümle 6: «Sonra Niloya merakla her taşın ve her çalının arkasına baktı.»
   - Açıklama: Niloya fındıkları arıyor; 'merakla' bu arayışa uygun bir kelime değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sonra Niloya merakla her"
   - Cümle 6: «Sonra Niloya merakla her taşın ve her çalının arkasına baktı.»
   - Açıklama: Kaybolan fındıkları ararken 'merakla' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0115` birebir aynı, `@degisim: yüklemek -> toplamak` (tutuyorsan), ardından `@onarim: c493da1b9f2a6020dc4807823068ddbdfee34932`, sonra gövde.

### Hikâye 7: tohum niloya-0118 (deneme 1 -> 2)

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
Bir sabah Niloya ile babaannesi yeşil tepede kekik topluyordu. Niloya dolu sepeti yokuşun kenarına bıraktı ve bir çiçeğe koştu. Tam o sırada rüzgar esti ve sepet otların üstünden aşağı kaydı. Babaannesi sepeti görmedi ve şaşırdı. "Özür dilerim, babaanne, sepeti yokuşa ben koydum," dedi Niloya. Sonra Niloya çevik adımlarla yokuştan aşağı indi. Merakla çalıların ve taşların arkasına tek tek baktı. Sepet büyük bir çalının arkasında duruyordu. Kekikler yine içindeydi. Niloya sepeti iki eliyle babaannesine getirdi. "Sağ ol, Niloya, sepeti sen buldun!" dedi babaannesi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Babaannesi sepeti görmedi ve şaşırdı"
   - Cümle 4: «Babaannesi sepeti görmedi ve şaşırdı.»
   - Açıklama: Sepeti bulamama anlamında 'görmedi' yanlış; 'göremedi/bulamadı' olmalı.
   - Açıklama: Sepet ortadan kaybolmuşken 'görmedi' yanlış fiil; 'göremedi' ya da 'bulamadı' olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya çevik adımlarla yokuştan"
   - Cümle 6: «Sonra Niloya çevik adımlarla yokuştan aşağı indi.»
   - Açıklama: Niloya büyüğe haber vermeden yokuştan tek başına hızla iniyor; çocuğun taklit edebileceği riskli bir davranış.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya çevik adımlarla yokuştan aşağı indi"
   - Cümle 6: «Sonra Niloya çevik adımlarla yokuştan aşağı indi.»
   - Açıklama: Niloya bir büyüğe haber vermeden yokuştan tek başına hızla iniyor; bu, kartın güvenli özellik kullanımı satırındaki bakma, sorma ve büyüğe haber verme yolunun dışında taklit edilince tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0118` birebir aynı, ardından `@onarim: 26b8626b23f5cd7ae8bfe99ed85b4e58ba881f40`, sonra gövde.

### Hikâye 8: tohum niloya-0119 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0119
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Tospik
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'yün', fiil 'atlamak', sıfat 'sıcacık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: rüzgar atkıyı sık bir çalının altına uçurdu | kaplumbağasından yardım istedi ve atkıyı geri aldı
@tohum: niloya-0119
Bir sabah Niloya ile Tospik yeşil tepede oyun oynuyordu. Niloya taşların üstünden atlıyordu, Tospik de sayıyordu. Birden rüzgar esti ve Niloya'nın sıcacık yün atkısı bir çalının altına uçtu. Niloya'nın eli sık dalların arasına sığmadı. "Tospik, çalının altına girip atkıyı getirir misin?" diye sordu Niloya. Tospik yavaş yavaş çalının altına girdi. Atkıyı ağzıyla tuttu ve dışarı çekti. Niloya atkısını boynuna sardı ve Tospik'e teşekkür etti. Niloya ile Tospik oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya taşların üstünden atlıyordu"
   - Cümle 2: «Niloya taşların üstünden atlıyordu, Tospik de sayıyordu.»
   - Açıklama: Tepede taştan taşa atlamak çocuğun taklit edince düşebileceği bir davranış ve güvenli kullanım satırının yüksek yere çıkmama ruhuna aykırı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "girip atkıyı getirir misin?"
   - Cümle 5: «"Tospik, çalının altına girip atkıyı getirir misin?" diye sordu Niloya.»
   - Açıklama: Tohumdaki soru özelliği kartta merakla soru sormak iken burada yalnız yardım isteği olarak kullanılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çalının altına girip atkıyı getirir misin"
   - Cümle 5: «"Tospik, çalının altına girip atkıyı getirir misin?" diye sordu Niloya.»
   - Açıklama: Tohumdaki özellik merakla soru sormak; burada soru merak değil yalnız bir yardım ricası olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0119` birebir aynı, ardından `@onarim: 4a6dcb33687eb18f23f6adbf490ca86dc52d3e3e`, sonra gövde.

### Hikâye 9: tohum niloya-0120 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0120
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'vazo', fiil 'yaymak', sıfat 'yakın'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: vazoyu doldurmak için etrafta kekik yoktu | kokunun geldiği yere bakıp kekikleri buldu
@tohum: niloya-0120
Niloya yeşil tepede küçük bir vazo taşıyordu. Vazosunu mor kekik çiçekleriyle doldurmak istiyordu. Ama etrafında hiç kekik yoktu. Birden rüzgar esti ve havaya güzel bir koku yaydı. Niloya bu kokuyu çok merak etti. Kokunun geldiği yöne yürüdü ve büyük taşların arkasına baktı. Hemen yakında bir sürü mor kekik vardı. Niloya birkaç dal kopardı ve vazosuna koydu. Vazo doldu ve çok hoş koktu. Niloya buna çok sevindi. Niloya bundan sonra çiçek ararken kokulara da dikkat etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama etrafında hiç kekik yoktu"
   - Cümle 3: «Ama etrafında hiç kekik yoktu.»
   - Açıklama: Kekik olmamasının sebebi söylenmiyor.
   - Açıklama: Tepede neden hiç kekik olmadığı söylenmiyor, üstelik hemen yakında bir sürü kekik çıkıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden rüzgar esti ve havaya güzel bir koku yaydı"
   - Cümle 4: «Birden rüzgar esti ve havaya güzel bir koku yaydı.»
   - Açıklama: Çözümü tesadüfen esen rüzgar sebepsizce getiriyor.
   - Açıklama: Çözümü getiren koku sebepsizce, tesadüfen esen rüzgarla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0120` birebir aynı, ardından `@onarim: d211b717cd6753c58de8dbb1742f8eb82ff87d90`, sonra gövde.

### Hikâye 10: tohum niloya-0121 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0121
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'poğaça', fiil 'kurutmak', sıfat 'çizgili'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: ikisi de topa ilk vurmak istedi ve oyun durdu | şarkı söyleyip sırayı seçti
@tohum: niloya-0121
@degisim: kurutmak -> yemek
Ormanda, fındık ağaçlarının altında Niloya ile Mete top oynuyordu. Mete'nin çizgili topuna ikisi de ilk vurmak istedi. İkisi aynı anda koştu ve oyun durdu. "Hadi sırayla vuralım, Mete," dedi Niloya. "Peki, ama önce kim?" diye sordu Mete. Niloya kısa bir şarkı söyledi ve parmağıyla sırayla ikisini gösterdi. Şarkı bitince parmağı Mete'yi gösteriyordu. Mete topa ilk vurdu, sonra Niloya vurdu. İkisi sırayla oynadı ve çok güldü. Oyundan sonra Niloya'nın getirdiği poğaçaları birlikte yediler. Niloya çok sevindi, çünkü sırayla oynamak çok eğlenceliydi.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya'nın getirdiği poğaçaları birlikte yediler"
   - Cümle 10: «Oyundan sonra Niloya'nın getirdiği poğaçaları birlikte yediler.»
   - Açıklama: Poğaçalar sebepsiz beliriyor ve sorunla hiçbir ilgisi yok.
   - Açıklama: Poğaçalar sebepsiz beliriyor ve sorunla ilgisi olmayan işlevsiz bir ayrıntı ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0121` birebir aynı, `@degisim: kurutmak -> yemek` (tutuyorsan), ardından `@onarim: 74296a74bc0bd1ede0a7917cb0eef070f93884a9`, sonra gövde.

### Hikâye 11: tohum niloya-0122 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | babaannesi
@tohum: niloya-0122
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'pantolon', fiil 'dolaşmak', sıfat 'yapışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | dağ | babaannesi
@plan: uzaktan bir şarkı sesi geldi | aynı şarkıyı söyleyip sesin geldiği yerde babaannesini buldu
@tohum: niloya-0122
Niloya tepede kekik bulmak için dolaşıyordu. Birden uzaktan ince bir şarkı sesi geldi. Niloya bu sesi çok merak etti ama kimseyi göremedi. Niloya aynı şarkıyı yüksek sesle söyledi. Uzaktaki ses hemen şarkıya katıldı. Ses büyük bir kayanın arkasından geliyordu. Niloya çalıların arasından kayaya yürüdü. Yürürken pantolonuna yapışkan küçük tohumlar takıldı. Kayanın arkasında babaannesi oturmuş, kekik topluyordu. "Babaanne, bu şarkıyı sen mi söyledin?" diye sordu Niloya. "Evet, bu benim en sevdiğim şarkı," dedi babaannesi. Babaannesi tohumları pantolonundan tek tek aldı. "Gel, Niloya, şarkıyı birlikte bitirelim!" dedi babaannesi.
```

**Hakem bulguları (6):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden uzaktan ince bir şarkı sesi geldi"
   - Cümle 2: «Birden uzaktan ince bir şarkı sesi geldi.»
   - Açıklama: Uzaktan gelen bir şarkı sesi gerçek bir sorun değil, çocuğun önemseyeceği bir güçlük yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya bu sesi çok merak etti"
   - Cümle 3: «Niloya bu sesi çok merak etti ama kimseyi göremedi.»
   - Açıklama: Tohumdaki özellik şarkı; merak ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik şarkı; kartın 'ozellikler' alanındaki merak ikinci bir özellik olarak ekleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Uzaktaki ses hemen şarkıya katıldı"
   - Cümle 5: «Uzaktaki ses hemen şarkıya katıldı.»
   - Açıklama: Ses şarkıya katılmaz; fiil öznesine uymuyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya çalıların arasından kayaya yürüdü"
   - Cümle 7: «Niloya çalıların arasından kayaya yürüdü.»
   - Açıklama: Niloya kimin olduğunu bilmediği bir sese büyüğe haber vermeden tek başına gidiyor; güvenli kullanım satırı bir büyüğe haber vermeyi söylüyor.
   - Açıklama: Niloya kimseyi görmeden bilinmeyen bir sese tek başına gidiyor; 'güvenli özellik kullanımı' merakı bakarak, sorarak ve büyüğe haber vererek gösterir.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "pantolonuna yapışkan küçük tohumlar takıldı"
   - Cümle 8: «Yürürken pantolonuna yapışkan küçük tohumlar takıldı.»
   - Açıklama: Tohumlar şarkı sorunuyla ilgisiz, işlevsiz ikinci bir ayrıntı olarak kuruluyor.
   - Açıklama: Tohumlar sebepsiz beliriyor ve hedefe hiçbir katkısı olmayan ikinci bir küçük olay açıyor.
6. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Babaannesi tohumları pantolonundan tek tek aldı"
   - Cümle 12: «Babaannesi tohumları pantolonundan tek tek aldı.»
   - Açıklama: 'pantolonundan' zamiri babaannenin kendi pantolonunu da gösterebiliyor; Niloya'nın pantolonu olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0122` birebir aynı, ardından `@onarim: 26203a7d169cacb4e72b9f57584651c721c2003f`, sonra gövde.

### Hikâye 12: tohum niloya-0123 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | annesi
@tohum: niloya-0123
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: annesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'portakal', fiil 'seslenmek', sıfat 'çabuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | annesi
@plan: annesi saklanan portakalı bulamadı | yaklaşınca yüksek, uzaklaşınca yavaş şarkı söyledi
@tohum: niloya-0123
Bahçede Niloya ile annesi saklambaç oynuyordu. Niloya bir portakalı çiçeklerin arasına sakladı. Annesi her yere baktı ama portakalı bulamadı. "Niloya, bana biraz yardım et!" diye seslendi annesi. Niloya güldü ve yeni bir oyun buldu. "Portakala yaklaşınca yüksek sesle, uzaklaşınca yavaş sesle şarkı söyleyeceğim," dedi Niloya. Niloya şarkısına başladı ve annesi kapıya doğru yürüdü. Şarkının sesi hemen azaldı. Annesi geri döndü ve çiçeklere yürüdü. Bu kez şarkının sesi yükseldi. Annesi çabuk adımlarla çiçeklerin yanına gitti ve portakalı buldu. "Buldum, Niloya, bu oyun çok eğlenceli!" dedi annesi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "uzaklaşınca yavaş şarkı söyledi"
   - Cümle 0 (plan satırı): «annesi saklanan portakalı bulamadı | yaklaşınca yüksek, uzaklaşınca yavaş şarkı söyledi»
   - Açıklama: 'Yavaş' hız bildirir; sesin azaldığı anlatılmak isteniyor, 'alçak sesle' olmalı.
   - Açıklama: 'Yavaş şarkı' ağır tempo demektir; kastedilen 'alçak sesle' ya da 'kısık sesle'dir.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede Niloya ile annesi"
   - Cümle 1: «Bahçede Niloya ile annesi saklambaç oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Portakala yaklaşınca yüksek sesle"
   - Cümle 6: «"Portakala yaklaşınca yüksek sesle, uzaklaşınca yavaş sesle şarkı söyleyeceğim," dedi Niloya.»
   - Açıklama: Zarf-fiilin öznesi eksik; yaklaşanın anne olduğu belirtilmeli ('Sen portakala yaklaşınca').
   - Açıklama: Zarf-fiilin öznesi eksik; cümle Niloya'nın yaklaşacağını söylüyor, 'sen portakala yaklaşınca' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0123` birebir aynı, ardından `@onarim: fba3d8b8bbd746fa69fa7c7cafe10098efa98add`, sonra gövde.
