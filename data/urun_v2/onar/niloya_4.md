# Editör görevi (onarım): Niloya, onarım partisi 4

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 6 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar4.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar4.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0001 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | babaannesi
@tohum: niloya-0001
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'düdük', fiil 'gülüşmek', sıfat 'pahalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | babaannesi
@plan: çimenlerde kekik yoktu ve sepet boş kaldı | kayalara baktı ve kekik bulunca düdük çaldı
@tohum: niloya-0001
@degisim: pahalı -> yeşil
Rüzgar tepelerde hafif hafif esiyordu. Niloya babaannesiyle dağda kekik topluyordu. Ama sepet boştu, çünkü çimenlerin arasında hiç kekik yoktu. "Ben burada ararım, sen de şu kayalara bak," dedi babaannesi. Babaannesi Niloya'ya küçük bir düdük verdi. "Kekik bulursan bu düdüğü çal," dedi babaannesi. Niloya yakındaki büyük kayaların arasını keşfetti. Bir kayanın arkasında yeşil kekikler buldu. Niloya hemen düdüğü çaldı. Babaannesi sesi duydu ve Niloya'nın yanına geldi. "Burada ne çok kekik var!" dedi babaannesi. İkisi sepeti birlikte doldurdu. Sonra dolu sepete bakıp gülüştüler. Niloya çok mutluydu, çünkü babaannesine yardım etmişti.
```

**Hakem bulguları (4):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "sen de şu kayalara bak"
   - Cümle 4: «"Ben burada ararım, sen de şu kayalara bak," dedi babaannesi.»
   - Açıklama: Kekiğin nerede aranacağını ve düdük fikrini babaanne veriyor; çözümü yan karakter yönlendiriyor.
   - Açıklama: Kekiği kayalarda aramak fikrini Niloya değil babaannesi veriyor; çözümü yan karakter getiriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "büyük kayaların arasını keşfetti"
   - Cümle 7: «Niloya yakındaki büyük kayaların arasını keşfetti.»
   - Açıklama: Kekik aramak için 'keşfetmek' yanlış anlamda; 'aradı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kayaların arasını keşfetti"
   - Cümle 7: «Niloya yakındaki büyük kayaların arasını keşfetti.»
   - Açıklama: 'Keşfetmek' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük kayaların arasını keşfetti"
   - Cümle 7: «Niloya yakındaki büyük kayaların arasını keşfetti.»
   - Açıklama: 'Keşfetti' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime; 'aradı' ya da 'baktı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0001` birebir aynı, `@degisim: pahalı -> yeşil` (tutuyorsan), ardından `@onarim: a839277b826279824079244808acb149c3606e7f`, sonra gövde.

### Hikâye 2: tohum niloya-0003 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | dedesi
@tohum: niloya-0003
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yağmur ya da kar günü
- yan: dedesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kalem', fiil 'barışmak', sıfat 'ıslak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | dedesi
@plan: yağmur başladı ve kağıda damlalar düştü | kayanın altında kuru bir yer buldu ve orada çizdi
@tohum: niloya-0003
@degisim: barışmak -> çizmek
Yağmur birden tıp tıp yağmaya başladı. Niloya o sırada dedesiyle dağda kalemle resim çiziyordu. Birkaç damla Niloya'nın kağıdına düştü. "Kağıt ıslanırsa resim bozulur," dedi dedesi. Niloya hemen kayaların arasını keşfetti. Büyük bir kayanın altında kuru bir yer buldu. "Dede, gel, burası hiç ıslak değil," dedi Niloya. İkisi kayanın altına oturdu. Niloya resmine devam etti ve yeşil tepeleri çizdi. Dedesi resme baktı ve gülümsedi. "Çok güzel olmuş, Niloya," dedi dedesi. Dedesi de Niloya da çok mutluydu, çünkü resim yağmurda bile bitmişti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya hemen kayaların arasını keşfetti"
   - Cümle 5: «Niloya hemen kayaların arasını keşfetti.»
   - Açıklama: 'Keşfetti' burada yanlış anlamda kullanılmış; 'aradı' ya da 'baktı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kayaların arasını keşfetti"
   - Cümle 5: «Niloya hemen kayaların arasını keşfetti.»
   - Açıklama: 'Keşfetmek' burada yanlış anlamda kullanılmış; 'aradı' ya da 'baktı' olmalı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kayaların arasını keşfetti"
   - Cümle 5: «Niloya hemen kayaların arasını keşfetti.»
   - Açıklama: 'Keşfetmek' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya hemen kayaların arasını keşfetti"
   - Cümle 5: «Niloya hemen kayaların arasını keşfetti.»
   - Açıklama: 'Keşfetmek' 3 yaşındaki çocuğa göre soyut ve zor bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0003` birebir aynı, `@degisim: barışmak -> çizmek` (tutuyorsan), ardından `@onarim: 698e3ba41415669098ad1714c15fbcf390e82787`, sonra gövde.

### Hikâye 3: tohum niloya-0004 (deneme 4 -> 5)

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
@plan: halıda tutacak yer yoktu ve halıdan yuvarlandı | iki yanını tutabilir miyim diye sordu ve tutundu
@tohum: niloya-0004
@degisim: yaratıcı -> eski
Parkta Niloya ile Murat halı çekme oyunu oynuyordu. Niloya eski bir halıya oturdu, Murat da halıyı çimenlerde çekti. Ama halıda tutacak bir yer yoktu ve Niloya çimenlere yuvarlandı. İkisi de kahkahalarla güldü. Niloya kalktı ve halıya dikkatle baktı. "Murat, halının iki yanını tutabilir miyim?" diye sordu Niloya. "Olur, hadi bir daha deneyelim," dedi Murat. Niloya yine halıya oturdu ve iki yanına sıkıca tutundu. Murat halıyı yeniden çekti. Bu kez Niloya halıdan hiç düşmedi. "Şimdi daha uzağa çek, Murat!" dedi Niloya. Murat halıyı kaydırağın yanına kadar çekti. Niloya çok mutluydu, çünkü oyunları yeniden eğlenceli olmuştu.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya çimenlere yuvarlandı"
   - Cümle 3: «Ama halıda tutacak bir yer yoktu ve Niloya çimenlere yuvarlandı.»
   - Açıklama: Çekilen halıdan yuvarlanıp düşme, çocuğun taklit edebileceği riskli bir oyun olarak gösteriliyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ama halıda tutacak bir yer yoktu ve Niloya çimenlere yuvarlandı"
   - Cümle 3: «Ama halıda tutacak bir yer yoktu ve Niloya çimenlere yuvarlandı.»
   - Açıklama: Çekilen halının üstünde oturup düşmek çocuğun taklit edebileceği tehlikeli bir oyun olarak sunuluyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "halıda tutacak bir yer yoktu"
   - Cümle 3: «Ama halıda tutacak bir yer yoktu ve Niloya çimenlere yuvarlandı.»
   - Açıklama: Halıda tutacak yer olmadığı söyleniyor ama sonra Niloya halının iki yanına tutunarak sorunu çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0004` birebir aynı, `@degisim: yaratıcı -> eski` (tutuyorsan), ardından `@onarim: 82a748067afb3a645b88def5f7ba734ba3ed7498`, sonra gövde.

### Hikâye 4: tohum niloya-0007 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0007
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'peynir', fiil 'sallanmak', sıfat 'düzgün'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: ikisi de dalı ilk çekmek istedi | sırayla dalı çektiler ve fındık topladılar
@tohum: niloya-0007
@degisim: peynir -> fındık
Ormanda Niloya ile Mete fındık topluyordu. Niloya ağaçların arasını keşfetti ve alçak bir dalda çok fındık gördü. Ama dal tekti ve ikisi de onu ilk çekmek istiyordu. "Sırayla yapalım, Mete, önce sen çek," dedi Niloya. Mete dalı çekti. Dal sallandı ve fındıklar yere düştü. Niloya fındıkları toplayıp bir taşın üstüne düzgün bir şekilde dizdi. Sonra sıra Niloya'ya geldi. Niloya dalı çekince yine fındıklar düştü. Bu kez Mete fındıkları toplayıp ilk fındıkların yanına dizdi. "Bak, ne çok fındık oldu!" dedi Mete. Niloya ile Mete gülüştü ve sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ağaçların arasını keşfetti"
   - Cümle 2: «Niloya ağaçların arasını keşfetti ve alçak bir dalda çok fındık gördü.»
   - Açıklama: 'Keşfetti' 3 yaşındaki bir çocuğa uygun olmayan soyut bir kelime.
   - Açıklama: 'Keşfetmek' soyut bir kelime ve 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0007` birebir aynı, `@degisim: peynir -> fındık` (tutuyorsan), ardından `@onarim: 8845f510fb6471415a583ef6ee0b917d48165527`, sonra gövde.

### Hikâye 5: tohum niloya-0008 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0008
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Mete
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'yonca', fiil 'yürümek', sıfat 'sessiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: ikisi aynı anda şarkı söyledi ve oyun olmadı | sırayla oynamayı önerdi ve önce kendisi söyledi
@tohum: niloya-0008
Bir sabah Niloya ile Mete ormanda dur oyunu oynamak istedi. Oyunda şarkı bitince yürüyen hemen duracaktı. Ama ikisi de aynı anda şarkı söylemeye başladı ve oyun başlamadı. "Böyle olmaz ki!" dedi Mete gülerek. "Sırayla oynayalım, Mete, önce ben söyleyeyim," dedi Niloya. Niloya şarkı söyledi, Mete de yeşil yonca üstünde sessiz adımlarla yürüdü. Şarkı bitince Mete hemen durdu ve hiç kıpırdamadı. Sonra Mete şarkı söyledi, Niloya yürüdü. Mete şarkıyı birden kesince Niloya tek ayağının üstünde kaldı. İkisi kahkahalarla güldü. Niloya çok mutluydu, çünkü sırayla oynamak çok eğlenceliydi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yeşil yonca üstünde sessiz adımlarla"
   - Cümle 6: «Niloya şarkı söyledi, Mete de yeşil yonca üstünde sessiz adımlarla yürüdü.»
   - Açıklama: Yonca kayboldu denmişken Mete sonra yonca üstünde yürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0008` birebir aynı, ardından `@onarim: 82fa6402e66b91f2b1cca6febfda751277bf7a8a`, sonra gövde.

### Hikâye 6: tohum niloya-0011 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | Murat
@tohum: niloya-0011
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Murat
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'ekmek', fiil 'akmak', sıfat 'çikolatalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | Murat
@plan: sıcakta çikolata eridi ve kurabiyeden aktı | kaydırağın altında gölge buldu ve kurabiyeyi orada soğuttu
@tohum: niloya-0011
@degisim: ekmek -> kurabiye
Parkta güneş çok sıcaktı. Niloya, Murat'a sürpriz yapmak için çikolatalı bir kurabiye getirmişti. Ama sıcakta çikolata eridi ve kurabiyeden akmaya başladı. Niloya kaydırağın çevresini keşfetti ve altında serin bir gölge buldu. Kurabiyeyi gölgeye koydu ve biraz bekledi. Çikolata soğudu ve artık akmıyordu. Niloya kurabiyeyi arkasına sakladı ve top oynayan Murat'a gitti. "Gözlerini kapat, abi," dedi Niloya. Murat gözlerini kapattı ve Niloya kurabiyeyi onun eline verdi. Murat gözlerini açınca çok sevindi. "Teşekkürler, Niloya, tam acıkmıştım!" dedi Murat. Murat kurabiyeyi ikiye böldü ve yarısını Niloya'ya verdi. Niloya bundan sonra çikolatayı hep serin bir yerde sakladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kaydırağın çevresini keşfetti"
   - Cümle 4: «Niloya kaydırağın çevresini keşfetti ve altında serin bir gölge buldu.»
   - Açıklama: 'Keşfetti' 3 yaşındaki çocuğun bilmeyeceği bir kelime ve burada 'baktı' anlamında zorlama kullanılmış.
   - Açıklama: 'Keşfetti' 3 yaşındaki çocuğun bileceği bir kelime değil ve burada yerinde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0011` birebir aynı, `@degisim: ekmek -> kurabiye` (tutuyorsan), ardından `@onarim: 5e42028c80b97d893f318bf5c6913b93e60cb59d`, sonra gövde.
