# Editör görevi (onarım): Niloya, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar15.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0040 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: tepelerden şarkısı ince bir sesle geri geldi | kısa bir ses çıkarıp kendi sesi olduğunu buldu
@tohum: niloya-0040
Yağmur yavaş yavaş yağıyordu. Niloya evin bahçesinde kırmızı şemsiyesinin altında şarkı söylüyordu. Birden tepelerden aynı şarkı ince bir sesle geri geldi. Niloya bu sesin nereden geldiğini çok merak etti. Bahçe kapısına koştu ve tepelere dikkatle baktı. Ama orada hiçbir şey göremedi. Niloya bu kez yalnız kısa ve basit bir ses çıkardı. Aynı ses az sonra tepelerden yine geldi. Niloya susunca tepelerden hiçbir ses gelmedi. O zaman Niloya anladı: bu, tepelerden geri dönen kendi sesiydi. Niloya güldü ve şemsiyesinin altında sesiyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya bu sesin nereden geldiğini çok merak etti"
   - Cümle 4: «Niloya bu sesin nereden geldiğini çok merak etti.»
   - Açıklama: Tohumdaki özellik şarkı; merak ikinci bir kart özelliği olarak ekleniyor.
   - Açıklama: Tohumdaki özellik şarkı; kartın merak özelliği ikinci bir özellik olarak ekleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sesiyle mutlu mutlu oynamaya"
   - Cümle 11: «Niloya güldü ve şemsiyesinin altında sesiyle mutlu mutlu oynamaya devam etti.»
   - Açıklama: 'Sesiyle oynamak' mecazlı bir ifade, küçük çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0040` birebir aynı, ardından `@onarim: 141402aeaf2a1ae30147595d249ea29bd2db5b61`, sonra gövde.

### Hikâye 2: tohum niloya-0042 (deneme 2 -> 3)

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
@plan: ikisi aynı anda koyunca elleri çarpıştı ve parçalar düştü | dedesine sırayla koymayı sordu ve resmi tamamladılar
@tohum: niloya-0042
Evin bahçesinde Niloya ile dedesi masaya bir yapboz döktü. Parçalar çok karışıktı. İkisi aynı anda koymaya çalışınca elleri çarpıştı ve birkaç parça yere düştü. Niloya onları topladı ve biraz düşündü. "Dede, sırayla koysak olur mu?" diye sordu Niloya. "Olur, önce sen başla," dedi dedesi. Niloya bir parça yerleştirdi, sonra dedesi bir tane ekledi. Böylece masada yavaş yavaş bir resim belirdi. Bu, gökyüzünde parlayan gümüş bir yıldızdı. En son dedesi kalan parçayı Niloya'ya uzattı. Niloya onu yıldızın ucuna taktı ve resim tamamlandı. "Birlikte yaptık, dedeciğim, yıldızımız çok güzel!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedesine sırayla koymayı sordu"
   - Cümle 0 (plan satırı): «ikisi aynı anda koyunca elleri çarpıştı ve parçalar düştü | dedesine sırayla koymayı sordu ve resmi tamamladılar»
   - Açıklama: Bir öneri 'sordu' fiiliyle verilmiş; 'önerdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0042` birebir aynı, ardından `@onarim: 0dda042ec2bcf23ab9b0862cf1487bda850b703c`, sonra gövde.

### Hikâye 3: tohum niloya-0043 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: hızlı yürürken şişe hep yere düşüyordu | yavaş bir şarkı söyleyip yavaş yürüdü
@tohum: niloya-0043
Rüzgar esiyordu ve ağaçların altını kuru yapraklar örtmüştü. Niloya ufak bir su şişesini başına koyup yürümeye çalışıyordu. Ama hızlı yürürken şişe hep kayıyor ve yere düşüyordu. Niloya bu komik oyunu çok seviyordu ve bırakmak istemedi. Şişeyi yerden aldı ve yeniden başına koydu. Sonra yavaş bir şarkı söylemeye başladı. Şarkı yavaş olduğu için Niloya da yavaş yürüdü. Şişe bu kez hiç kaymadı ve başının üstünde kaldı. Niloya ağaçların arasında tam on adım attı. Niloya güldü ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Ama hızlı yürürken şişe hep kayıyor"
   - Cümle 3: «Ama hızlı yürürken şişe hep kayıyor ve yere düşüyordu.»
   - Açıklama: '-ken' yan cümlesinin öznesi belirsiz; yürüyen şişe değil Niloya, 'Niloya hızlı yürürken' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0043` birebir aynı, ardından `@onarim: c6c85f5f53f87222c1d578bd25f8502b6b916a42`, sonra gövde.

### Hikâye 4: tohum niloya-0044 (deneme 2 -> 3)

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
Niloya evin bahçesinde kırmızı çemberini belinde çeviriyordu. Murat kapının önünde sakin sakin oturuyordu. Onun topu patlamıştı ve oynayacak bir şeyi yoktu. Niloya durdu ve ağabeyine baktı. "Murat, sen hiç çember çevirmeyi denedin mi?" diye sordu Niloya. "Hayır, hiç denemedim," dedi Murat. Niloya çemberini ona verdi. Murat denedi ama çember hemen yere düştü. İkisi birlikte güldü. Sonra sırayla oynadılar ve Niloya her turu saydı. Sonunda Murat da tam on tur yaptı. Niloya çok sevindi, çünkü çemberini paylaşınca ağabeyi de eğlenmişti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çemberini ona verip sırayla oynadılar"
   - Cümle 0 (plan satırı): «ağabeyinin topu patlamıştı ve oynayacak şeyi yoktu | çemberini ona verip sırayla oynadılar»
   - Açıklama: 'verip' fiilinin öznesi tekil (Niloya), ana fiil 'oynadılar' çoğul; zarf-fiil ile ana fiilin öznesi uyuşmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0044` birebir aynı, `@degisim: dilemek -> oynamak` (tutuyorsan), ardından `@onarim: d5b95751ebaa1aba91d3657f1d5ea0138d4d42d5`, sonra gövde.

### Hikâye 5: tohum niloya-0045 (deneme 2 -> 3)

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
Güneş parlıyordu. Bugün babaannesinin doğum günüydü ve Niloya parkta ona kumdan pasta yapmak istedi. Ama kum un gibi kuruydu ve pasta hemen dağıldı. "Babaanne, biraz su var mı?" diye sordu Niloya. "Var, al bakalım," dedi babaannesi ve su şişesini verdi. Niloya kumu biraz ıslattı ve yeniden şekil verdi. Bu kez pasta sağlam kaldı. Niloya onu incecik bir dalla süsledi. Sonra babaannesini kumun yanına çağırdı. "İyi ki doğdun, babaanneciğim!" dedi Niloya. Babaannesi Niloya'ya sıkıca sarıldı ve ikisi parkta mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "babaannesini kumun yanına çağırdı"
   - Cümle 9: «Sonra babaannesini kumun yanına çağırdı.»
   - Açıklama: Niloya zaten kumun başında; 'pastanın yanına' kastediliyor, kelime yanlış yerde.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0045` birebir aynı, `@degisim: uyutmak -> süslemek` (tutuyorsan), ardından `@onarim: 4c7af670b97232eac0dc99e59e52bfb17a0cc85e`, sonra gövde.

### Hikâye 6: tohum niloya-0047 (deneme 2 -> 3)

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
@plan: annesinin tokası kaydıraktan hızla kayarken otlara düştü | özür diledi ve kaydırağın altına bakıp tokayı buldu
@tohum: niloya-0047
@degisim: lamba -> toka
Parkta Niloya annesinin mavi tokasını saçına takmıştı. Sonra tokayı çıkarmadan kaydıraktan hızla kaydı ve toka otların içine düştü. Annesi bankta oturuyordu. Niloya hemen annesinin yanına gitti. "Özür dilerim, anne, tokanı düşürdüm," dedi Niloya. "Gel, birlikte bakalım," dedi annesi. Niloya kaydırağın altına merakla baktı. Orada mavi bir şey parlıyordu. Niloya tokayı çıkardı ve üstündeki tozu üfledi. Sonra onu annesine uzattı. Annesi gülümsedi ve Niloya'ya sarıldı. Niloya gururlu ve mutluydu, çünkü tokayı bulup annesine geri vermişti.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "annesinin tokası kaydıraktan hızla kayarken otlara düştü"
   - Cümle 0 (plan satırı): «annesinin tokası kaydıraktan hızla kayarken otlara düştü | özür diledi ve kaydırağın altına bakıp tokayı buldu»
   - Açıklama: Plan cümlesinde 'kayarken' fiilinin öznesi toka olarak kalıyor; kayanın Niloya olduğu belirtilmemiş.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tokası kaydıraktan hızla kayarken"
   - Cümle 0 (plan satırı): «annesinin tokası kaydıraktan hızla kayarken otlara düştü | özür diledi ve kaydırağın altına bakıp tokayı buldu»
   - Açıklama: Plan satırında kaydıraktan kayan özne toka olmuş; kayan Niloya'dır.
   - Açıklama: Plan satırında 'kayarken' fiili tokaya bağlanıyor; kayan toka değil Niloya'dır.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya gururlu ve mutluydu"
   - Cümle 12: «Niloya gururlu ve mutluydu, çünkü tokayı bulup annesine geri vermişti.»
   - Açıklama: 'Gururlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0047` birebir aynı, `@degisim: lamba -> toka` (tutuyorsan), ardından `@onarim: 0ed3dedd26ffe521d9d6abffb855cb94dc852b9f`, sonra gövde.

### Hikâye 7: tohum niloya-0052 (deneme 1 -> 2)

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
@plan: yağmur damlaları narin çiçeğin sapını eğdi | havluyu çiçeğin üstünde tuttu ve bekledi
@tohum: niloya-0052
Niloya ormanda narin, mor bir çiçeğin yanında oturuyordu. Birden yağmur başladı ve iri damlalar çiçeğin ince sapını eğdi. Niloya çiçeği korumak istedi. Sepetinde bir havlu vardı, çünkü hava çok bulutluydu. Havluyu hemen çıkardı ve iki eliyle çiçeğin üstünde tuttu. Damlalar artık havluya düşüyordu. Niloya beklerken en sevdiği yağmur şarkısını söyledi. Az sonra yağmur dindi ve güneş çıktı. Niloya havluyu salladı ve suyu etrafa saçtı. Mor çiçeğin sapı yavaşça doğruldu. Niloya dik duran çiçeğe gülümsedi ve sepetiyle ormanda mutlu mutlu gezmeye başladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "narin, mor bir çiçeğin"
   - Cümle 1: «Niloya ormanda narin, mor bir çiçeğin yanında oturuyordu.»
   - Açıklama: 'Narin' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
   - Açıklama: 'Narin' 3 yaşındaki bir çocuğun bilmediği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepetinde bir havlu vardı, çünkü hava çok bulutluydu"
   - Cümle 4: «Sepetinde bir havlu vardı, çünkü hava çok bulutluydu.»
   - Açıklama: Havlunun sepette olması akla yatkın bir sebebe bağlanmıyor ve çözümü kolaylıkla getiriyor.
   - Açıklama: Çözümü getiren havlu, bulutlu hava gibi zayıf bir gerekçeyle sebepsizce hazır çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0052` birebir aynı, ardından `@onarim: 12ad93fa29e63a77c5dffc0a8caf91f526abb6f0`, sonra gövde.

### Hikâye 8: tohum niloya-0053 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0053
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'gitar', fiil 'izlemek', sıfat 'kahverengi'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: yer eğikti ve fındıklar aşağı yuvarlandı | düz bir taş bulup fındıkları üstüne dizdi
@tohum: niloya-0053
@degisim: gitar -> fındık
Niloya ormanda ağabeyi Murat'la fındık topluyordu. Ona sürpriz olarak kahverengi fındıklarla yere bir kalp yapmak istedi. Ama yer eğikti ve fındıklar hep aşağı yuvarlandı. Murat biraz ileride kendi sepetini dolduruyordu. Niloya arada bir ağabeyini izledi. Murat hiç arkasına bakmadı. Niloya etrafa baktı ve düz, büyük bir taş buldu. Fındıkları taşın üstüne tek tek dizdi. Bu kez hiçbiri kaymadı. Kalp bitince Niloya ağabeyini yanına çağırdı. Murat gelince Niloya ona neşeli bir şarkı söyledi. Murat taşın üstündeki kalbi görünce kocaman gülümsedi. Sonra Niloya'ya sıkıca sarıldı. Niloya çok sevindi, çünkü sürprizi ağabeyini mutlu etmişti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Murat gelince Niloya ona neşeli bir şarkı söyledi"
   - Cümle 11: «Murat gelince Niloya ona neşeli bir şarkı söyledi.»
   - Açıklama: Tohumdaki şarkı özelliği sorunun çözümüne katkı vermiyor, yalnız süs olarak geçiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya ona neşeli bir şarkı söyledi"
   - Cümle 11: «Murat gelince Niloya ona neşeli bir şarkı söyledi.»
   - Açıklama: Şarkı olayla ilgisiz, işlevsiz bir ayrıntı olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0053` birebir aynı, `@degisim: gitar -> fındık` (tutuyorsan), ardından `@onarim: 62b68c66514d1bd6594cd0778d5bbbc2fc1aae80`, sonra gövde.

### Hikâye 9: tohum niloya-0054 (deneme 1 -> 2)

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
@plan: toprak sertti ve küçük kürek zor giriyordu | tırmığı arkadaşına verdi ve toprağı birlikte kazdılar
@tohum: niloya-0054
@degisim: fırçalamak -> dikmek
Bir sabah Niloya ile Tospik ormandaki devasa fındık ağacının altına geldi. Niloya küçük küreğiyle bir fındık dikmek istiyordu. Ama toprak çok sertti ve kürek zor giriyordu. Sepette bir alet daha vardı, küçük bir tırmık. "Tospik, bu tırmık senin olsun," dedi Niloya. "Sağ ol, ben de yardım ederim," dedi Tospik. Tospik tırmıkla toprağı yavaş yavaş kazdı. Toprak yumuşayınca Niloya küreği kolayca soktu. Tospik yorulunca Niloya neşeli bir şarkı söyledi ve arkadaşı yeniden çalıştı. Niloya fındığı açılan çukura koydu ve üstünü toprakla örttü. "Birlikte çok daha hızlı oldu," dedi Tospik. Niloya bundan sonra aletlerini hep arkadaşlarıyla paylaştı.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "devasa fındık ağacının altına"
   - Cümle 1: «Bir sabah Niloya ile Tospik ormandaki devasa fındık ağacının altına geldi.»
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime; 'çok büyük' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ormandaki devasa fındık ağacının"
   - Cümle 1: «Bir sabah Niloya ile Tospik ormandaki devasa fındık ağacının altına geldi.»
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki bir çocuk bilmeyebilir; 'kocaman' olmalı.
3. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Tospik tırmıkla toprağı yavaş yavaş kazdı"
   - Cümle 7: «Tospik tırmıkla toprağı yavaş yavaş kazdı.»
   - Açıklama: Kartta tür değeri kaplumbağa olan Tospik elle alet tutup kazamaz; diziyi bilen çocuğa yanlış bilgi verir.
   - Açıklama: Kartta türü kaplumbağa olan Tospik'in alet kullanarak toprak kazması dizideki bilgisine uymuyor olabilir.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Tospik tırmıkla toprağı yavaş yavaş kazdı"
   - Cümle 7: «Tospik tırmıkla toprağı yavaş yavaş kazdı.»
   - Açıklama: Sert toprağı Niloya değil Tospik kazarak yumuşatıyor; yan karakter sorunu çözüyor.
   - Açıklama: Sert toprağı Niloya değil yan karakter Tospik yumuşatıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tospik yorulunca Niloya neşeli bir şarkı söyledi"
   - Cümle 9: «Tospik yorulunca Niloya neşeli bir şarkı söyledi ve arkadaşı yeniden çalıştı.»
   - Açıklama: Şarkı adımı sorundan çıkmıyor ve çözüme bir şey katmayan işlevsiz bir ayrıntı.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya neşeli bir şarkı söyledi"
   - Cümle 9: «Tospik yorulunca Niloya neşeli bir şarkı söyledi ve arkadaşı yeniden çalıştı.»
   - Açıklama: Şarkı ve Tospik'in yorulması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0054` birebir aynı, `@degisim: fırçalamak -> dikmek` (tutuyorsan), ardından `@onarim: 07f8404a69f048a719d99392778135feb6070af1`, sonra gövde.

### Hikâye 10: tohum niloya-0055 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | babaannesi
@tohum: niloya-0055
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'dolma', fiil 'göndermek', sıfat 'sağlıklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | ev | babaannesi
@plan: yaprak kaygandı ve pirinç hep döküldü | babaannesinden yardım isteyip yaprak sarmayı öğrendi
@tohum: niloya-0055
@degisim: göndermek -> sarmak
Niloya yaprak sarmayı öğrenmeyi çok merak ediyordu. Babaannesi mutfakta sağlıklı bir öğle yemeği için dolma yapıyordu. Niloya da bir yaprak aldı ama yaprak kaygandı ve pirinç hep döküldü. Birkaç kez denedi ama yaprak yine açıldı. "Babaanneciğim, bana da gösterir misin?" diye sordu Niloya. "Tabii, az pirinç koy ve kenarları içe katla," dedi babaannesi. Niloya yaprağa biraz pirinç koydu. Kenarları katladı ve yaprağı sıkıca sardı. Bu kez pirinç hiç dökülmedi. Babaannesi gülümsedi ve Niloya'nın yaprağını tencereye yerleştirdi. "Aferin, çok güzel oldu," dedi babaannesi. Sonra Niloya ile babaannesi bütün yaprakları mutlu mutlu birlikte sardı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sarmayı öğrenmeyi çok merak ediyordu"
   - Cümle 1: «Niloya yaprak sarmayı öğrenmeyi çok merak ediyordu.»
   - Açıklama: 'Öğrenmeyi merak etmek' yanlış kullanım; 'öğrenmeyi çok istiyordu' olmalı.
   - Açıklama: 'Öğrenmeyi merak etmek' uygun değil; 'öğrenmeyi çok istiyordu' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "az pirinç koy ve kenarları içe katla"
   - Cümle 6: «"Tabii, az pirinç koy ve kenarları içe katla," dedi babaannesi.»
   - Açıklama: Sebep yaprağın kaygan olması olarak verilmiş ama çözüm kayganlığa değil pirinç miktarına ve katlamaya yöneliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0055` birebir aynı, `@degisim: göndermek -> sarmak` (tutuyorsan), ardından `@onarim: 6dc1965516af14d143a7bfb9c51954b811c9d5b0`, sonra gövde.

### Hikâye 11: tohum niloya-0056 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | annesi
@tohum: niloya-0056
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'yelpaze', fiil 'kurtulmak', sıfat 'harika'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | annesi
@plan: yelpazeyi salladı ve kekikler çimenlere uçtu | özür dileyip kekikleri tek tek topladı
@tohum: niloya-0056
Niloya annesiyle tepede kekik topluyordu. Annesi sıcaktan kurtulmak için arada yelpazesini sallıyordu. Niloya da yelpazeyi sepete salladı ve kekikler çimenlere uçtu. "Anne, kekikler neden sepetten çıktı?" diye sordu Niloya. "Yelpaze rüzgar yaptı, kekikler de çok hafif," dedi annesi. "Özür dilerim, anne, hepsini ben toplarım," dedi Niloya. Niloya yere eğildi ve kekikleri tek tek topladı. Sonra onları sepete geri koydu. Annesi kızına sarıldı. "Harika, sepet yine dolu," dedi annesi. Niloya çok sevindi, çünkü bütün kekikleri geri toplamıştı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yelpazeyi sepete salladı"
   - Cümle 3: «Niloya da yelpazeyi sepete salladı ve kekikler çimenlere uçtu.»
   - Açıklama: Yelpaze bir yere sallanmaz; 'sepete doğru salladı' olmalı.
   - Açıklama: 'Sepete sallamak' yanlış kullanım; 'sepete doğru salladı' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yelpazeyi sepete salladı ve kekikler çimenlere uçtu"
   - Cümle 3: «Niloya da yelpazeyi sepete salladı ve kekikler çimenlere uçtu.»
   - Açıklama: Sorun Niloya'nın sebepsizce sepete yelpaze sallamasıyla çıkan önemsiz bir dağılma; kekikler toplanınca bitiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya da yelpazeyi sepete salladı"
   - Cümle 3: «Niloya da yelpazeyi sepete salladı ve kekikler çimenlere uçtu.»
   - Açıklama: Niloya'nın yelpazeyi sepete sallaması önceki olaydan çıkmıyor, sorunu sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0056` birebir aynı, ardından `@onarim: ede86114bda63ccd868a32eca5acaba203bbec54`, sonra gövde.

### Hikâye 12: tohum niloya-0057 (deneme 1 -> 2)

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
Rüzgar ağaçların arasında hafifçe esiyordu. Niloya merakla gezerken bulduğu sağlam dalla toprağa resim çiziyordu. Mete de çizmek istedi ama yerdeki öteki dallar hemen kırılıyordu. Niloya dala baktı, sonra Mete'ye baktı. Dalı gülümseyerek Mete'ye uzattı ve sırayla çizmeye başladılar. Önce Mete toprağa büyük bir ağaç çizdi. Sonra Niloya ağacın yanına küçük bir çiçek çizdi. Mete ağacın üstüne yuvarlak bir güneş ekledi. Niloya da güneşin altına el ele tutuşan iki çocuk çizdi. Resim bitince ikisi de ona bakıp güldü. Niloya çok sevindi, çünkü sırayla çizince kocaman bir resim yapmışlardı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya merakla gezerken bulduğu"
   - Cümle 2: «Niloya merakla gezerken bulduğu sağlam dalla toprağa resim çiziyordu.»
   - Açıklama: Tohumdaki keşfet özelliği yalnız geçerken anılıyor, çözümde işe yarar biçimde kullanılmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yerdeki öteki dallar hemen kırılıyordu"
   - Cümle 3: «Mete de çizmek istedi ama yerdeki öteki dallar hemen kırılıyordu.»
   - Açıklama: Gövdede dalların neden kırıldığı söylenmiyor; kuru olma sebebi yalnız planda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0057` birebir aynı, `@degisim: kitaplık -> dal` (tutuyorsan), ardından `@onarim: 8d995b0fa3306d3e80846d9a2cbbcf395ccc5c14`, sonra gövde.
