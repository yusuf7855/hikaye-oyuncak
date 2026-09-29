# Editör görevi (onarım): Niloya, onarım partisi 20

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 9 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar20.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar20.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0073 (deneme 2 -> 3)

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
Bir sabah Niloya yaylaya büyük renkli bir halka getirdi. Halkayı belinde çevirmeyi ilk kez deneyecekti. Ama halka hemen yere düştü, çünkü Niloya belini çok hızlı sallıyordu. Niloya halkayı yerden aldı ve biraz düşündü. Sonra neşeli bir şarkı söylemeye başladı. Belini şarkının sesine göre yavaş yavaş salladı. Bu sefer halka düşmedi ve Niloya'nın etrafında döndü. Şarkı uzun sürdü, halka da uzun uzun döndü. Niloya şarkı bitene kadar hiç durmadı. Niloya çok sevindi, çünkü halkayı çevirmeyi sonunda öğrenmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şarkının sesine göre yavaş"
   - Cümle 6: «Belini şarkının sesine göre yavaş yavaş salladı.»
   - Açıklama: Bel şarkının sesine göre değil ritmine göre sallanır; kelime yerinde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0073` birebir aynı, `@degisim: sevimli -> renkli` (tutuyorsan), ardından `@onarim: d982d04f21ce3c639061e214d430754c1e6d0963`, sonra gövde.

### Hikâye 2: tohum niloya-0074 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Tospik
@tohum: niloya-0074
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Tospik
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'terazi', fiil 'ısınmak', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | Tospik
@plan: kaplumbağa iki ağaç kökü arasına sıkıştı | ona bir soru sordu ve onu yavaşça geri çekti
@tohum: niloya-0074
@degisim: terazi -> kök
Niloya ormanda Tospik'i arıyordu. Tospik ısınmak için güneşli bir yere gidiyordu. Ama kabuğu iki büyük ağaç kökü arasına sıkıştı. Niloya onu orada buldu. "Tospik, geri gidebilir misin?" diye sordu Niloya sevecen bir sesle. "Evet, ama öne gidemiyorum," dedi Tospik. Niloya kabuğu iki eliyle tuttu ve yavaşça geri çekti. Tospik de ayaklarıyla itti. Sonunda Tospik köklerin arasından çıktı. Niloya onu ağacın öbür yanına götürdü. Orada güneş sıcacıktı. Tospik uzandı ve gözlerini kapadı. "Teşekkürler, Niloya, burası çok sıcak!" dedi Tospik.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Evet, ama öne gidemiyorum"
   - Cümle 6: «"Evet, ama öne gidemiyorum," dedi Tospik.»
   - Açıklama: Tospik geri gidebildiğini söylüyor ama yine de sıkışmış gibi Niloya'nın onu geri çekmesi gerekiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0074` birebir aynı, `@degisim: terazi -> kök` (tutuyorsan), ardından `@onarim: 5e548f289e412830e894169be4c9caa46e339359`, sonra gövde.

### Hikâye 3: tohum niloya-0075 (deneme 1 -> 2)

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
@plan: annesinin sakladığı hazineyi hiçbir yerde bulamadı | annesi bir bilmece ekledi ve hazineyi elbisenin cebinde buldu
@tohum: niloya-0075
Yağmur pencereye tıp tıp vuruyordu. Niloya evde annesiyle hazine oyunu oynuyordu. Annesi odada ona bir hazine saklamıştı. Ama hazine çok iyi saklanmıştı ve cesur Niloya onu hiçbir yerde bulamadı. "Anneciğim, bana biraz yardım eder misin?" dedi Niloya. Annesi gülümsedi ve oyuna bir bilmece ekledi. "Hazine mavi bir cepte duruyor," dedi annesi. Niloya odaya merakla yeniden baktı. Sandalyenin üstünde mavi elbisesini gördü. Elbisenin cebine elini soktu. Cepte bir kurabiye vardı! Niloya kurabiyeyi ikiye böldü. Yarısını annesine verdi. Niloya çok sevindi, çünkü hazineyi sonunda kendisi bulmuştu.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "annesi bir bilmece ekledi ve hazineyi elbisenin cebinde buldu"
   - Cümle 0 (plan satırı): «annesinin sakladığı hazineyi hiçbir yerde bulamadı | annesi bir bilmece ekledi ve hazineyi elbisenin cebinde buldu»
   - Açıklama: Plan satırında 'buldu' fiilinin öznesi annesi gibi okunuyor; hazineyi kimin bulduğu belli değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "cesur Niloya onu hiçbir yerde"
   - Cümle 4: «Ama hazine çok iyi saklanmıştı ve cesur Niloya onu hiçbir yerde bulamadı.»
   - Açıklama: Tohumdaki özellik keşfet/merak iken kartın özellikler alanında olmayan cesaret ikinci bir özellik olarak ekleniyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "cesur Niloya onu hiçbir"
   - Cümle 4: «Ama hazine çok iyi saklanmıştı ve cesur Niloya onu hiçbir yerde bulamadı.»
   - Açıklama: Tohumdaki özellik keşfet; cesaret karttaki özelliklerde olmayan ikinci bir özellik olarak ekleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "hazine çok iyi saklanmıştı"
   - Cümle 4: «Ama hazine çok iyi saklanmıştı ve cesur Niloya onu hiçbir yerde bulamadı.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor, ilk 3 cümlede değil.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "oyuna bir bilmece ekledi"
   - Cümle 6: «Annesi gülümsedi ve oyuna bir bilmece ekledi.»
   - Açıklama: Annenin söylediği bir bilmece değil ipucu; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0075` birebir aynı, ardından `@onarim: f0bdea38cf11d4c31d7514b9a0ffba40d589de87`, sonra gövde.

### Hikâye 4: tohum niloya-0076 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: sofrayı süslemek için yakında hiç çiçek yoktu | taşın arkasına bakıp sarı çiçekler buldu
@tohum: niloya-0076
@degisim: damga -> börek
Bir sabah Niloya dedesiyle yeşil tepeye çıktı. Niloya dedesine sürpriz bir sofra hazırlamak istedi. Ama sofrayı süslemek için yakında hiç çiçek yoktu. Dede biraz ileride kekik topluyordu. Niloya çimenlere bir örtü serdi ve sepetteki peynirli böreği koydu. Niloya merakla büyük bir taşın arkasına baktı. Orada sarı çiçekler buldu. Birkaç çiçek topladı ve böreğin yanına koydu. Çiçeklerin kokusu kekik kokusuyla karıştı. "Dedeciğim, gel, sana bir sürprizim var!" dedi Niloya. Dede geldi ve süslü sofrayı gördü. "Ne güzel bir sofra, teşekkürler, Niloya," dedi dede. İkisi böreği birlikte yedi. Niloya çok mutluydu, çünkü dedesini sevindirmişti.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yakında hiç çiçek yoktu"
   - Cümle 3: «Ama sofrayı süslemek için yakında hiç çiçek yoktu.»
   - Açıklama: Yakında hiç çiçek olmadığı söyleniyor ama Niloya hemen yakındaki taşın arkasında sarı çiçekler buluyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Orada sarı çiçekler buldu"
   - Cümle 7: «Orada sarı çiçekler buldu.»
   - Açıklama: Başta yakında hiç çiçek olmadığı söyleniyor ama çiçekler hemen yakındaki taşın arkasında çıkıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çiçeklerin kokusu kekik kokusuyla karıştı"
   - Cümle 9: «Çiçeklerin kokusu kekik kokusuyla karıştı.»
   - Açıklama: Kekik kokusu ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0076` birebir aynı, `@degisim: damga -> börek` (tutuyorsan), ardından `@onarim: b612a1b8145dc1faa86f1690c5bed69e04b6fc6e`, sonra gövde.

### Hikâye 5: tohum niloya-0077 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: toprakta yuvarlak bir çukur suyla doluyordu | taşı kaldırıp suyun toprağın altından geldiğini buldu
@tohum: niloya-0077
Niloya yeşil tepede kekik topluyordu. Birden toprakta yuvarlak, küçük bir çukur gördü. Çukur yavaş yavaş suyla doluyordu. Ama hava güneşliydi ve hiç yağmur yağmamıştı. Niloya suyun nereden geldiğini merakla düşündü. Çukurun yanına eğildi ve dikkatle baktı. Suyun içinde minik baloncuklar vardı. Baloncuklar çukurun kenarındaki bir taşın altından çıkıyordu. Niloya küçük taşı yavaşça kaldırdı. Taşın altından ince bir su akıyordu. Su, toprağın altından geliyordu! Niloya elini serin suya değdirdi ve güldü. Niloya çok sevindi, çünkü çukurdaki suyun nereden geldiğini bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Çukur yavaş yavaş suyla doluyordu"
   - Cümle 3: «Çukur yavaş yavaş suyla doluyordu.»
   - Açıklama: Suyla dolan çukur Niloya için gerçek bir sorun değil, yalnız bir merak konusu; çözülmesi gereken bir dert yok.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya elini serin suya değdirdi"
   - Cümle 12: «Niloya elini serin suya değdirdi ve güldü.»
   - Açıklama: Kartın güvenli özellik kullanımı satırı suya yalnız kıyıdan bakılmasını söylüyor; Niloya suya elini sokuyor.
   - Açıklama: Kartın güvenli özellik kullanımı satırı suya yalnız kıyıdan bakılmasını söylüyor; Niloya tek başına suya elini değdiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0077` birebir aynı, ardından `@onarim: e96fa98a0551bd69b1d436a6538e2b2c1a34aa30`, sonra gövde.

### Hikâye 6: tohum niloya-0078 (deneme 1 -> 2)

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
Bir sabah Niloya ile Murat yeşil tepeye çıktı. Murat yumuşak çimenlerde ip atlamak istiyordu. Ama ip hep ayağına takıldı, çünkü Murat çok hızlı atlıyordu. Murat yere oturdu ve üzgünce ipe baktı. "Murat, sen şarkıya göre yavaşça atla," dedi Niloya. Niloya başını sağa sola oynattı ve yavaş bir şarkı söyledi. Murat şarkıyı dinleyerek zıpladı. Bu kez ip ayağına hiç takılmadı. Murat on kez, sonra yirmi kez atladı. Niloya da ellerini çırptı. Murat ipi bıraktı ve Niloya'ya sarıldı. "Şarkın sayesinde atlamak çok kolay, Niloya!" dedi Murat sevinçle.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya da ellerini çırptı"
   - Cümle 10: «Niloya da ellerini çırptı.»
   - Açıklama: Başka kimse el çırpmadığı için 'da' bağlacı yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0078` birebir aynı, `@degisim: kum -> ip` (tutuyorsan), ardından `@onarim: 513e85d8d25fc15a030aba95daa125c6e46c4e40`, sonra gövde.

### Hikâye 7: tohum niloya-0079 (deneme 1 -> 2)

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
Hava çok güneşliydi ve kuşlar ötüyordu. Niloya babaannesiyle ormanda fındık topluyordu. Bir süre sonra ikisi de acıktı. Ama sepette tek dilim reçelli ekmek vardı. "Babaanne, bu ekmeği ikimiz paylaşalım," dedi Niloya. Babaanne ekmeği ikiye böldü ve yarısını ona verdi. Sonra Niloya ağaçların arasına merakla baktı. Yere yakın bir dalda kırmızı kirazlar gördü. Eteğini tuttu ve kirazları içine topladı. Kirazların yarısını da babaannesine verdi. Babaanne kirazları yedi ve güldü. "İkimiz de doyduk, Niloya," dedi babaanne. "Afiyet olsun, babaanneciğim!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "sepette tek dilim reçelli ekmek vardı"
   - Cümle 4: «Ama sepette tek dilim reçelli ekmek vardı.»
   - Açıklama: Asıl sorun olan tek dilim ekmek ilk üç cümlede değil dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0079` birebir aynı, ardından `@onarim: ea12eefacee2bd704749168e72491ae4ec491ac5`, sonra gövde.

### Hikâye 8: tohum niloya-0080 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | Mete
@tohum: niloya-0080
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'tarak', fiil 'tanımak', sıfat 'sarı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | Mete
@plan: kekiklerin arasında sarı bir şey parlıyordu | yakından bakıp onun küçük bir tarak olduğunu buldu
@tohum: niloya-0080
Bir sabah Niloya ile Mete yeşil tepede kekik topluyordu. Birden Niloya kekiklerin arasında sarı bir şey gördü. Güneşte parlıyordu ama ne olduğu belli değildi. Niloya merakla yaklaştı ve otları elleriyle yana itti. Yerde küçük, sarı bir tarak duruyordu. "Mete, bu tarağı tanıyor musun?" dedi Niloya. Mete ona baktı ve hemen tanıdı. "Bu benim tarağım, çantadan düşmüş!" dedi Mete. Mete tarağı aldı ve saçını taradı. Sonra tarağı çantasına koydu ve çantayı sıkıca kapattı. Niloya ona bakıp güldü. Sonra Niloya ile Mete kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onun küçük bir tarak olduğunu buldu"
   - Cümle 0 (plan satırı): «kekiklerin arasında sarı bir şey parlıyordu | yakından bakıp onun küçük bir tarak olduğunu buldu»
   - Açıklama: Bir şeyin ne olduğunu anlamak için 'buldu' değil 'anladı' kullanılmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kekiklerin arasında sarı bir şey parlıyordu"
   - Cümle 0 (plan satırı): «kekiklerin arasında sarı bir şey parlıyordu | yakından bakıp onun küçük bir tarak olduğunu buldu»
   - Açıklama: Sorun yalnız parlayan bir şeyin ne olduğu merakı; kimse tarağı aramıyor ve çocuğun önemseyeceği bir sorun kurulmuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Güneşte parlıyordu ama ne olduğu belli değildi"
   - Cümle 3: «Güneşte parlıyordu ama ne olduğu belli değildi.»
   - Açıklama: Parlayan bir şey görmek gerçek bir sorun değil; kimse bir şey kaybettiğini bilmiyor ve çocuğun önemseyeceği bir derdi yok.
4. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Mete ona baktı ve"
   - Cümle 7: «Mete ona baktı ve hemen tanıdı.»
   - Açıklama: 'ona' zamirinin Niloya'yı mı tarağı mı gösterdiği belli değil.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Mete ona baktı"
   - Cümle 7: «Mete ona baktı ve hemen tanıdı.»
   - Açıklama: 'Ona' zamirinin tarağı mı Niloya'yı mı gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0080` birebir aynı, ardından `@onarim: 72301e859bd6f84c536e8131ceccd9bee90f1cc1`, sonra gövde.

### Hikâye 9: tohum niloya-0082 (deneme 1 -> 2)

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
@plan: tomurcuk kapalıydı ve içi görünmüyordu | acele etmeden bekledi ve güneşle açılan çiçeği gördü
@tohum: niloya-0082
@degisim: şapkalı -> mor
Yeşil tepede güneş yeni doğuyordu. Niloya kekiklerin yanında küçük bir tomurcuk buldu. Onun içini görmek istedi ama tomurcuk sımsıkı kapalıydı. Üstünde boncuk gibi su damlaları vardı. Niloya'nın tek bir sorusu vardı. Bu çiçeğin içi hangi renkti? Niloya ona hiç dokunmadı. Çimenlere oturdu ve sessizce bekledi. Bir süre sonra güneş tomurcuğa değdi. Su damlaları yavaş yavaş kurudu. Sonunda tomurcuk açıldı. İçinden mor yapraklar çıktı. Çiçeğin içi mordu! Niloya bundan sonra kapalı tomurcukları zorla açmadı, bekledi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya'nın tek bir sorusu vardı"
   - Cümle 5: «Niloya'nın tek bir sorusu vardı.»
   - Açıklama: Tohumdaki soru özelliği kimseye sorulmuyor ve sorunu çözmüyor; çözüm karttaki 'sorar' özelliği yerine beklemekle geliyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çimenlere oturdu ve sessizce bekledi"
   - Cümle 8: «Çimenlere oturdu ve sessizce bekledi.»
   - Açıklama: Tohumdaki özellik soru sormak; sorun soruyla değil sabırla bekleyerek çözülüyor, sabır ikinci bir özellik olarak ekleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "güneş tomurcuğa değdi"
   - Cümle 9: «Bir süre sonra güneş tomurcuğa değdi.»
   - Açıklama: Güneş tomurcuğa değmez; 'güneş ışığı tomurcuğa vurdu' olmalı.
   - Açıklama: Güneş bir şeye değmez; 'güneş ışığı değdi' olmalı, fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0082` birebir aynı, `@degisim: şapkalı -> mor` (tutuyorsan), ardından `@onarim: 7d7041122c38ab6a9007a12b71588711f78d80a5`, sonra gövde.
