# Editör görevi (onarım): Niloya, onarım partisi 39

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar39.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0147 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0147
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'bluz', fiil 'birleştirmek', sıfat 'kıpkırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: kulenin küçük topu hep kayıp düştü | büyük topun üstünü düz yaptı ve topları birleştirdi
@tohum: niloya-0147
@degisim: bluz -> eldiven
Bir sabah köyün yanındaki tepelere kar yağmıştı. Niloya kıpkırmızı eldivenlerini giydi ve kardan bir kule yapmaya başladı. Ama kulenin küçük topu büyük topun üstünde hiç durmuyordu. Niloya küçük topu yeniden koydu, ama top kayıp yere düştü. Niloya'nın aklına bir soru geldi: Küçük top neden kayıyordu? Niloya büyük topa iyice baktı. Büyük topun üstü çok yuvarlaktı. Niloya onun üstüne elleriyle bastırdı ve düz yaptı. Sonra iki topu sıkıca birleştirdi. Bu kez küçük top hiç kaymadı ve kule bitti. Niloya bundan sonra kule yaparken önce büyük topun üstünü düz yaptı.
```

**Hakem bulguları (2):**

1. **K7** (K merceği) — Yer, kartın o yer için verdiği tarife uygun.
   - Alıntı: "köyün yanındaki tepelere kar yağmıştı"
   - Cümle 1: «Bir sabah köyün yanındaki tepelere kar yağmıştı.»
   - Açıklama: Kartın dağ tarifi kekik toplanan yeşil tepeler diyor; karla kaplı tepeler bu tarife uymuyor.
   - Açıklama: Kartın dağ tarifi kekik toplanan yeşil tepelerdir; karla kaplı tepe bu tarife uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına bir soru geldi"
   - Cümle 5: «Niloya'nın aklına bir soru geldi: Küçük top neden kayıyordu?»
   - Açıklama: 'Aklına soru gelmek' deyimi 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0147` birebir aynı, `@degisim: bluz -> eldiven` (tutuyorsan), ardından `@onarim: 7f64e9b889fb6c7423d33e9e55af846f27395d01`, sonra gövde.

### Hikâye 2: tohum niloya-0154 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0154
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'top', fiil 'inanmak', sıfat 'özel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: topu atıp tutmak istedi ama top düştü | şarkı söyleyerek topu yavaşça attı ve tuttu
@tohum: niloya-0154
Niloya ormanda dedesiyle sirk oyunu oynuyordu. Topu beş kez havaya atıp tutmak istiyordu. Ama acele ediyordu ve top her seferinde yere düşüyordu. "Dede, bana inan, bu kez tutacağım," dedi Niloya. Sonra en sevdiği özel şarkısını söylemeye başladı. Şarkının her sözünde topu yavaşça havaya attı. Niloya bir, iki, üç, dört, beş diye saydı ve hepsini tuttu. Dedesi ellerini çırptı. "Çok güzel oynadın, Niloya!" dedi dedesi. Niloya bundan sonra topu atıp tutarken hep şarkı söyledi.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "dedesiyle sirk oyunu oynuyordu"
   - Cümle 1: «Niloya ormanda dedesiyle sirk oyunu oynuyordu.»
   - Açıklama: Sirk kartın köy dünyasında yok; kapalı dünyaya dışarıdan bir öğe ekleniyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "beş diye saydı ve hepsini tuttu"
   - Cümle 7: «Niloya bir, iki, üç, dört, beş diye saydı ve hepsini tuttu.»
   - Açıklama: Tek top var; 'hepsini' zamirinin neyi gösterdiği belli değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "diye saydı ve hepsini tuttu"
   - Cümle 7: «Niloya bir, iki, üç, dört, beş diye saydı ve hepsini tuttu.»
   - Açıklama: Tek top var; 'hepsini' zamirinin neyi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0154` birebir aynı, ardından `@onarim: aacc65cd9dcf2986190553f869db6cc4e34b34ab`, sonra gövde.

### Hikâye 3: tohum niloya-0156 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0156
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: bir şey yapmak
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'tablo', fiil 'yaklaşmak', sıfat 'dürüst'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: rüzgar kağıdı salladı ve tablo bozuldu | rüzgarın geldiği yere bakıp büyük bir kayanın arkasına oturdu
@tohum: niloya-0156
@degisim: dürüst -> büyük
Rüzgar tepede hızlı hızlı esiyordu. Niloya orada boyalarıyla güzel bir tablo yapmak istiyordu. Ama rüzgar kağıdını sallıyordu ve tablo bozuluyordu. Niloya içinden sordu: Rüzgar nereden geliyordu? Otlara baktı. Bütün otlar aynı yana eğiliyordu. Rüzgar karşıdaki tepeden esiyordu. Niloya yakındaki büyük bir kayaya yaklaştı. Kayanın öbür yanına oturdu. Orada rüzgar yoktu ve kağıt hiç kıpırdamadı. Niloya köyü, nehri ve evleri rahatça boyadı. Niloya bundan sonra rüzgarlı günlerde resmini büyük bir kayanın arkasında yaptı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "güzel bir tablo yapmak"
   - Cümle 2: «Niloya orada boyalarıyla güzel bir tablo yapmak istiyordu.»
   - Açıklama: 'Tablo' 3 yaşındaki çocuğun bilmediği bir kelime; 'resim' olmalı.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "Niloya içinden sordu: Rüzgar nereden geliyordu?"
   - Cümle 4: «Niloya içinden sordu: Rüzgar nereden geliyordu?»
   - Açıklama: Niloya kendi kendine soru soruyor.
   - Açıklama: Niloya kendi kendine soru soruyor ve iç soru tırnaksız verilmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0156` birebir aynı, `@degisim: dürüst -> büyük` (tutuyorsan), ardından `@onarim: 1a1dc68087c7537ee1f4575129ea0ca6ae1b24bd`, sonra gövde.

### Hikâye 4: tohum niloya-0157 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | Tospik
@tohum: niloya-0157
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: yeni bir şeyi denemek
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'çim', fiil 'hazırlanmak', sıfat 'parlak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | ev | Tospik
@plan: hızlı dansta kaplumbağa geride kaldı | yavaş bir şarkı söyleyip adımlarını yavaşlattı
@tohum: niloya-0157
Bahçede kuşlar ötüyordu. Parlak güneşin altında Niloya ile Tospik çimlerde ilk kez dans ediyordu. Ama Niloya hızlı hızlı dönüyordu ve Tospik ona yetişemiyordu. "Çok hızlısın, Niloya," dedi Tospik. Niloya biraz düşündü. Sonra yavaş bir şarkı söylemeye başladı. Adımlarını da şarkıya göre yavaşlattı. Tospik şarkıyı duyunca yeniden dansa hazırlandı. Tospik bu kez Niloya'ya kolayca yetişti ve sallandı. "Şimdi çok güzel oldu, Niloya," dedi Tospik. İkisi şarkı bitene kadar bahçede mutlu mutlu dans etti.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede kuşlar ötüyordu"
   - Cümle 1: «Bahçede kuşlar ötüyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye güneş altında bahçedeki çimlerde geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye baştan sona bahçede çimlerin üstünde geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0157` birebir aynı, ardından `@onarim: a4ea923090f22ff2e56ad080e626a1c9e2dda5b8`, sonra gövde.

### Hikâye 5: tohum niloya-0160 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0160
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'etiket', fiil 'doldurmak', sıfat 'keyifli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: fındıklar yüksek dallarda kaldı | şarkı söyleyerek abisini yardıma çağırdı
@tohum: niloya-0160
@degisim: etiket -> sepet
Ormanda fındık ağaçlarının altında Niloya çok keyifliydi. Niloya sepetini fındıkla doldurmak istiyordu. Ama yerdeki fındıklar bitmişti ve Niloya'nın eli dallara yetişmiyordu. Murat biraz ileride top oynuyordu. "Abiciğim, abiciğim, gel bana yardım et!" diye şarkı söyledi Niloya. Murat bu sesi duyunca güldü ve koşarak geldi. "Fındıklar yukarıda kaldı, Murat," dedi Niloya. Murat uzanıp bir dalı tuttu ve yavaşça salladı. Fındıklar yere pıt pıt düştü. Niloya hepsini tek tek topladı ve sepet doldu. Niloya ile Murat dolu sepetin yanına oturup fındıkları mutlu mutlu saydı.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Murat uzanıp bir dalı tuttu ve yavaşça salladı"
   - Cümle 8: «Murat uzanıp bir dalı tuttu ve yavaşça salladı.»
   - Açıklama: Fındıkları düşüren asıl çözüm adımını Niloya değil Murat atıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0160` birebir aynı, `@degisim: etiket -> sepet` (tutuyorsan), ardından `@onarim: ea4fb22b9a255094025a5603f90208b753caeb37`, sonra gövde.

### Hikâye 6: tohum niloya-0161 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0161
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'eşarp', fiil 'ışıldamak', sıfat 'minicik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | park | -
@plan: parkta şarkıyı tekrar eden minicik bir ses duydu | sesin kaydıraktan gelen kendi sesi olduğunu buldu
@tohum: niloya-0161
@degisim: eşarp -> kaydırak
Niloya parkta salıncakta şarkı söylüyordu. Birden minicik bir ses onun şarkısını tekrarladı. Niloya bu sesi bulmak istedi ve hemen salıncaktan indi. Ses kapalı kaydıraktan geliyordu. Kaydırak güneşte ışıldıyordu. Niloya kaydırağın ağzına gitti. Şarkısını bir kez daha söyledi. Minicik ses bu kez kaydırağın içinden geldi. Niloya içeri eğilip baktı ama orada kimse yoktu. Kaydırak onun kendi sesini geri veriyordu. Niloya bunu bulduğu için çok sevindi. Niloya kaydırağın önünde ellerini çırptı ve sesiyle mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya kaydırağın ağzına gitti"
   - Cümle 6: «Niloya kaydırağın ağzına gitti.»
   - Açıklama: Kaydırağın 'ağzı' mecazlı bir kullanımdır; 3 yaşındaki çocuk için somut değildir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve sesiyle mutlu mutlu oynadı"
   - Cümle 12: «Niloya kaydırağın önünde ellerini çırptı ve sesiyle mutlu mutlu oynadı.»
   - Açıklama: 'Sesiyle oynamak' mecazlı ve soyut bir anlatım, küçük çocuğa açık değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0161` birebir aynı, `@degisim: eşarp -> kaydırak` (tutuyorsan), ardından `@onarim: cebed67e1475ea07057b11f20633dabc969a792f`, sonra gövde.

### Hikâye 7: tohum niloya-0162 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | dedesi
@tohum: niloya-0162
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'beşik', fiil 'yeşillenmek', sıfat 'kararlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | dedesi
@plan: oyuncak beşik saksıya çarptı ve saksı devrildi | dedesinden özür diledi ve ne yapacağını sordu
@tohum: niloya-0162
@degisim: kararlı -> küçük
Niloya evde oyuncak beşiği ile oynuyordu. Yanında dedesinin küçük saksısı duruyordu. İçinde yeni yeşillenmiş filizler vardı. Niloya beşiği hızlı hızlı salladı ve beşik saksıya çarptı. Saksı devrildi ve toprak yere döküldü. Dedesi hemen yanına geldi. "Dedeciğim, özür dilerim. Şimdi ne yapalım?" diye sordu Niloya. "Toprağı geri koyalım ve biraz su verelim," dedi dedesi. Niloya toprağı ve filizleri elleriyle saksıya geri koydu. Sonra onlara biraz su verdi. Filizler yeniden dik durdu. Niloya çok sevindi, çünkü dedesinin saksısı yine yeşildi.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «İçinde yeni yeşillenmiş filizler vardı.»
   - Açıklama: Saksının devrilmesi sorunu ilk üç cümlede değil, dördüncü ve beşinci cümlede geliyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Niloya beşiği hızlı hızlı salladı ve beşik saksıya çarptı"
   - Cümle 4: «Niloya beşiği hızlı hızlı salladı ve beşik saksıya çarptı.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0162` birebir aynı, `@degisim: kararlı -> küçük` (tutuyorsan), ardından `@onarim: a882372af2ac064e42a0d4a7826ca4ccf687bf88`, sonra gövde.

### Hikâye 8: tohum niloya-0163 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0163
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'mermer', fiil 'korumak', sıfat 'büyük'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: alttaki küçük taşlar yüzünden kale hep yıkıldı | büyük bir mermer taşı en alta koydu
@tohum: niloya-0163
Tepede kuşlar ötüyordu. Niloya orada kale oyunu oynuyordu. Önce taşlardan bir kale yapacak, sonra onu koruyacaktı. Ama altta küçük taşlar vardı ve kale hep yıkılıyordu. Niloya kaleye baktı ve içinden sordu: Kale neden duramıyordu? Alttaki taşlar küçük ve yuvarlaktı. Üstteki taşları hiç tutamıyordu. Niloya otların arasında büyük, düz bir mermer taşı buldu. Onu kalenin en altına koydu. Küçük taşları da üstüne dizdi. Kale bu kez yıkılmadı. Niloya kalesinin önüne oturdu ve onu korudu. Niloya bundan sonra kale yaparken büyük taşları hep en alta koydu.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Önce taşlardan bir kale yapacak, sonra onu koruyacaktı.»
   - Açıklama: Kalenin yıkılma sorunu ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "kaleye baktı ve içinden sordu"
   - Cümle 5: «Niloya kaleye baktı ve içinden sordu: Kale neden duramıyordu?»
   - Açıklama: Niloya kendi kendine soru soruyor.
3. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "baktı ve içinden sordu"
   - Cümle 5: «Niloya kaleye baktı ve içinden sordu: Kale neden duramıyordu?»
   - Açıklama: Niloya kendi kendine soru soruyor.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "içinden sordu: Kale neden duramıyordu?"
   - Cümle 5: «Niloya kaleye baktı ve içinden sordu: Kale neden duramıyordu?»
   - Açıklama: İç konuşma tırnak içinde değil ve anlatı zamanıyla karışmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0163` birebir aynı, ardından `@onarim: 751295b3d01b7f1a067f6cf3644bbd7aebc949d9`, sonra gövde.

### Hikâye 9: tohum niloya-0165 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0165
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: paylaşmak
- yan: Murat
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'resim', fiil 'kaplamak', sıfat 'gizli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: ağabeyinin resim yapacak kağıdı yoktu | kağıdını ikiye bölüp ağabeyiyle paylaştı
@tohum: niloya-0165
@degisim: kaplamak -> boyamak
Niloya ormanda, fındık ağacının altındaki gizli köşede resim yapıyordu. Murat da gelip yanına oturdu ama hiç kağıdı yoktu. Murat onun resmine bakıp sessizce bekledi. "Abi, neden bekliyorsun?" diye sordu Niloya. "Ben de resim yapmak istiyorum ama kağıdım yok," dedi Murat. Niloya büyük kağıdına baktı. Kağıdı ikiye katladı ve dikkatle yırttı. "Yarısı senin, abi," dedi Niloya. Kalemlerini de ortaya koydu. Murat fındık ağaçlarını yeşile boyadı. Niloya da kırmızı elmaları boyadı. İkisi resimlerini bitirip birbirine mutlu mutlu gösterdi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama hiç kağıdı yoktu"
   - Cümle 2: «Murat da gelip yanına oturdu ama hiç kağıdı yoktu.»
   - Açıklama: Murat'ın neden kağıdı olmadığı söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0165` birebir aynı, `@degisim: kaplamak -> boyamak` (tutuyorsan), ardından `@onarim: f22b35c40b0623ad0a8ef51621ee8396954dcc9a`, sonra gövde.

### Hikâye 10: tohum niloya-0167 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0167
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'bulut', fiil 'kıvırmak', sıfat 'renkli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: taşın arkasından ince bir ıslık sesi geldi | taşın arkasına bakıp sesi yapan yaprağı buldu
@tohum: niloya-0167
Güçlü bir rüzgar esiyordu ve bulutlar hızla geçiyordu. Niloya yeşil tepede renkli çiçeklerin arasında kekik topluyordu. Birden büyük bir taşın arkasından ince bir ıslık sesi geldi. Niloya sesin nereden geldiğini bulmak istedi. Taşın arkasına yavaşça yürüdü ve merakla baktı. Orada iki taşın arasında kuru bir yaprak sıkışmıştı. Yaprak küçük bir boru gibiydi. Rüzgar yaprağın içinden geçince o ses çıkıyordu. Niloya yerden başka bir yaprak aldı ve kıvırdı. Sonra onu rüzgara doğru tuttu. Onun yaprağından da aynı ıslık sesi geldi. Niloya çok sevindi ve güldü. Sonra yaprağını elinde tutarak mutlu mutlu kekik toplamaya devam etti.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Birden büyük bir taşın arkasından ince bir ıslık sesi geldi"
   - Cümle 3: «Birden büyük bir taşın arkasından ince bir ıslık sesi geldi.»
   - Açıklama: Güçlü rüzgarda tek başına tepede büyük taşın arkasından gelen gizemli ses küçük çocuk için ürkütücü olabilir.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "taşın arkasından ince bir ıslık sesi geldi"
   - Cümle 3: «Birden büyük bir taşın arkasından ince bir ıslık sesi geldi.»
   - Açıklama: Islık sesi Niloya için gerçek bir sorun değil; yalnız bir merak olayı ve hikayede aşılacak bir güçlük yok.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun yaprağından da aynı"
   - Cümle 11: «Onun yaprağından da aynı ıslık sesi geldi.»
   - Açıklama: 'Onun' Niloya'yı gösteriyor ama bu kullanım belirsiz ve doğal değil; 'Kendi yaprağından' ya da 'Niloya'nın yaprağından' olmalı.
   - Açıklama: 'Onun' zamirinin kimi gösterdiği belirsiz ve cümle doğal değil; 'Niloya'nın yaprağından da' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0167` birebir aynı, ardından `@onarim: 8702a79da7647fb457b111ae11ab5e94a33e3c1d`, sonra gövde.

### Hikâye 11: tohum niloya-0169 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0169
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Tospik
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'gözlük', fiil 'çiğnemek', sıfat 'yamuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: hızlı yürüdü ve kaplumbağası kabuğuna girdi | özür diledi ve şarkı söyleyerek onu dışarı çıkardı
@tohum: niloya-0169
@degisim: gözlük -> yaprak
Niloya ile Tospik yeşil tepede kekik topluyordu. Niloya yamuk yolda çok hızlı yürüdü ve Tospik'i geride bıraktı. Tospik ona yetişemedi ve üzüldü, sonra kabuğuna girdi. Niloya hemen geri döndü ve kaplumbağasının yanına oturdu. "Özür dilerim, Tospik, seni beklemeden yürüdüm," dedi Niloya. Ama Tospik kabuğundan çıkmadı. Niloya ona tatlı ve yavaş bir şarkı söyledi. Tospik şarkıyı duyunca önce başını, sonra ayaklarını dışarı çıkardı. "Bu şarkı çok güzel," dedi Tospik. Niloya ona taze bir yaprak verdi ve Tospik yaprağı mutlu mutlu çiğnedi. "Bundan sonra seninle yan yana yürüyeceğim," dedi Niloya.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya yamuk yolda"
   - Cümle 2: «Niloya yamuk yolda çok hızlı yürüdü ve Tospik'i geride bıraktı.»
   - Açıklama: 'Yamuk' yol için doğru kelime değil; 'eğri' ya da 'kıvrımlı yol' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya yamuk yolda çok"
   - Cümle 2: «Niloya yamuk yolda çok hızlı yürüdü ve Tospik'i geride bıraktı.»
   - Açıklama: Yol için 'yamuk' yanlış kelime; 'eğri' ya da 'dolambaçlı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0169` birebir aynı, `@degisim: gözlük -> yaprak` (tutuyorsan), ardından `@onarim: c0b5ba044f1f09f4dc61a5ff106a5f2c0c60d6e9`, sonra gövde.

### Hikâye 12: tohum niloya-0170 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0170
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'cetvel', fiil 'göstermek', sıfat 'boyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: ağacın resmini çizerken çizgiler yamuk oldu | çantasındaki cetvelle düz çizgiler çizdi
@tohum: niloya-0170
Ormanda rüzgar esiyordu. Niloya fındık ağacının altında oturmuş, ağacın resmini yapıyordu. Ağacın gövdesini çizdi ama çizgiler yamuk oldu. Niloya resmine baktı ve bir soru sordu: Düz çizgiyi nasıl çizecekti? Sonra boya çantasını açtı ve içinde bir cetvel buldu. Cetveli kağıdın üstüne koydu ve kenarından çizdi. Bu kez gövde düz oldu. Niloya dalları yeşile, gövdeyi kahverengiye boyadı. Boyalı resim ağacın bütün dallarını gösteriyordu. Niloya resmi ağacın yanına tuttu ve ikisine baktı. Niloya çok sevindi, çünkü resmi gerçek ağaca çok benziyordu.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çizgiler yamuk oldu"
   - Cümle 3: «Ağacın gövdesini çizdi ama çizgiler yamuk oldu.»
   - Açıklama: Çizgilerin neden yamuk olduğu hiç söylenmiyor; sorunun sebebi eksik.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "bir soru sordu: Düz çizgiyi nasıl çizecekti?"
   - Cümle 4: «Niloya resmine baktı ve bir soru sordu: Düz çizgiyi nasıl çizecekti?»
   - Açıklama: Yanında kimse yokken Niloya soru soruyor; kendi kendine konuşma.
3. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "ve bir soru sordu"
   - Cümle 4: «Niloya resmine baktı ve bir soru sordu: Düz çizgiyi nasıl çizecekti?»
   - Açıklama: Niloya kimse yokken soru soruyor, yani kendi kendine konuşuyor.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "sordu: Düz çizgiyi nasıl çizecekti?"
   - Cümle 4: «Niloya resmine baktı ve bir soru sordu: Düz çizgiyi nasıl çizecekti?»
   - Açıklama: Soru sorulduğu söylenen cümle tırnaksız ve dolaylı anlatımla karışık yazılmış.
5. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "sordu: Düz çizgiyi nasıl"
   - Cümle 4: «Niloya resmine baktı ve bir soru sordu: Düz çizgiyi nasıl çizecekti?»
   - Açıklama: İki noktadan sonra gelen soru ne tırnak içinde ne de düzgün aktarılmış; noktalama karışık.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0170` birebir aynı, ardından `@onarim: ce01f84c302427b95484d9d36a5a629e0159246c`, sonra gövde.
