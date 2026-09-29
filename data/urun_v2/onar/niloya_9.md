# Editör görevi (onarım): Niloya, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar9.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0002 (deneme 4 -> 5)

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
Parkta Niloya kaydırağın yanında sarı bir çiçek gördü. Çiçek güneşte yavaş yavaş açılıyordu. Niloya bunu Tospik'e göstermek istedi ama Tospik uyuyordu. Tospik, Niloya ile limonlu su satma oyunu oynamıştı ve çok yorulmuştu. Niloya onun yanına oturdu ve neşeli bir şarkı söyledi. Tospik şarkıyı duyunca gözlerini açtı. Başını kabuğundan çıkardı ve çiçeğe baktı. Çiçek daha tam açık değildi. İkisi yan yana oturdu ve bekledi. Sonra sarı yapraklar bir bir açıldı. Tospik gülümsedi ve çiçeği kokladı. Niloya çok sevindi, çünkü çiçek açarken Tospik de yanındaydı.
```

**Hakem bulguları (2):**

1. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "limonlu su satma oyunu"
   - Cümle 4: «Tospik, Niloya ile limonlu su satma oyunu oynamıştı ve çok yorulmuştu.»
   - Açıklama: Limonlu su satma oyunu kartın köy dünyasında yok ve diziyi izleyen çocuğun tanıyacağı bir öğe değil.
   - Açıklama: Limonlu su satma oyunu dizinin köy dünyasına ait değil; dizi izleyen çocuğun tanımayacağı yabancı bir öğe.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ile limonlu su satma oyunu oynamıştı ve çok yorulmuştu"
   - Cümle 4: «Tospik, Niloya ile limonlu su satma oyunu oynamıştı ve çok yorulmuştu.»
   - Açıklama: Uyumanın sebebi önce gökyüzünün maviliği, sonra yorgunluk olarak birbiriyle çelişen iki biçimde veriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0002` birebir aynı, `@degisim: düğüm -> çiçek` (tutuyorsan), ardından `@onarim: 3c10db27855b92e4457d7bd8e485e5dc6442bfd9`, sonra gövde.

### Hikâye 2: tohum niloya-0009 (deneme 4 -> 5)

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
Niloya ile babaannesi parkta bir kağıda resim çiziyordu. İkisi de güneşi boyamak istiyordu ama tek bir turuncu kalem vardı. Niloya biraz düşündü. "Babaanne, sırayla boyayalım, şarkım bitince kalem sende olsun," dedi Niloya. Sonra neşeli bir şarkı söyledi ve güneşin yarısını boyadı. Şarkı bitince kalemi babaannesine verdi. Babaannesi güneşin öbür yarısını turuncuya boyadı. Silgiyle de güneşe iki göz yaptı. Resim bitti. "Sırayla yapınca ne güzel oldu!" dedi babaannesi. Niloya bundan sonra kalem tek olunca onu babaannesiyle sırayla kullandı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Silgiyle de güneşe iki göz yaptı"
   - Cümle 8: «Silgiyle de güneşe iki göz yaptı.»
   - Açıklama: Silgi çizmek için kullanılmaz; araç fiile uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Silgiyle de güneşe iki göz yaptı"
   - Cümle 8: «Silgiyle de güneşe iki göz yaptı.»
   - Açıklama: Silgi sebepsiz beliriyor ve silgiyle göz yapmak olayla bağsız, işlevsiz bir ayrıntı.
   - Açıklama: Silgi sebepsiz beliriyor ve sorunla ilgisi olmayan işlevsiz bir ayrıntı ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0009` birebir aynı, `@degisim: yemek -> çizmek` (tutuyorsan), ardından `@onarim: af067bda85e27c608ce174148944437d36178bae`, sonra gövde.

### Hikâye 3: tohum niloya-0010 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: dedesinin küçük ağacında hiç fındık yoktu | şarkı söyleyip dedesini çağırdı ve fındıklarını paylaştı
@tohum: niloya-0010
@degisim: ferah -> serin
Rüzgar dalları savuruyordu ve orman çok serindi. Niloya ile dedesi ormanda fındık topluyordu. Niloya'nın ağacı fındıkla doluydu ama dedesinin ağacı küçüktü ve hiç fındığı yoktu. Niloya alçak dallardan bir sürü fındık kopardı. Önlüğünün cebini fındıkla doldurdu. Dedesi ise uzakta, boş elle bakıyordu. Niloya dedesini çağırmak için neşeli bir şarkı söyledi. Dedesi şarkıyı duyunca gülümsedi ve yanına geldi. "Dede, bu fındıkların yarısı senin," dedi Niloya. Sonra fındıkların yarısını dedesine verdi. "Teşekkürler, Niloya, bunları birlikte yiyelim," dedi dedesi. Niloya çok sevindi, çünkü artık ikisinin de fındığı vardı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "uzakta, boş elle bakıyordu"
   - Cümle 6: «Dedesi ise uzakta, boş elle bakıyordu.»
   - Açıklama: 'Boş elle' bakmak fiiline uymuyor; 'eli boş' denmeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0010` birebir aynı, `@degisim: ferah -> serin` (tutuyorsan), ardından `@onarim: a6057af16d10377390e1b9035364f7fff906dbef`, sonra gövde.

### Hikâye 4: tohum niloya-0012 (deneme 3 -> 4)

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
@plan: kaplumbağası uyumak istedi ama toprak çok serindi | ılık bir taş bulup üstüne yumuşak bir giysi serdi
@tohum: niloya-0012
Evin bahçesinde serin bir rüzgar esiyordu. Niloya'nın kaplumbağası Tospik uyumak istiyordu ama toprak çok serindi. "Niloya, bana sıcak bir yer bulur musun?" diye sordu Tospik. Niloya merakla bahçeyi dolaştı ve her yere baktı. Evin yanında güneş alan düz bir taş buldu. Taşa elini koydu, taş eline ılık geldi. Niloya eski ve yumuşak bir giysi getirdi ve taşın üstüne serdi. Tospik yavaş yavaş yürüdü ve giysinin üstüne çıktı. "Burayı çok beğendim, teşekkürler, Niloya!" dedi Tospik. Tospik orada rahatça uyudu, Niloya da onun yanında oturup gülümsedi.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya merakla bahçeyi dolaştı"
   - Cümle 4: «Niloya merakla bahçeyi dolaştı ve her yere baktı.»
   - Açıklama: Sıcak yer arayan Niloya için 'merakla' anlama uymuyor.
   - Açıklama: Sıcak yer aramak meraktan değil; 'merakla' bağlama uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "taş eline ılık geldi"
   - Cümle 6: «Taşa elini koydu, taş eline ılık geldi.»
   - Açıklama: 'eline ılık geldi' deyimsel bir anlatım, küçük çocuk için açık değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0012` birebir aynı, ardından `@onarim: 56dba7f8af34d62f191e8180c0d01561fd2f18ac`, sonra gövde.

### Hikâye 5: tohum niloya-0013 (deneme 3 -> 4)

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
Niloya ormandaydı ve güneş yeni doğuyordu. Niloya ince bir dala yapraklar takıp bir taç yaptı. Ama taç çok büyüktü ve başından gözlerine kaydı. Niloya tacı çıkardı ve ona uzun uzun baktı. Niloya'nın bir sorusu vardı: Dal çok mu uzundu? Dalı başının çevresine tuttu ve gerçekten çok uzun olduğunu gördü. Niloya dalın iki ucunu biraz daha üst üste getirdi. Dalı kırmamak için çok dikkatli davrandı. Dalı sıkıca sardı. Taç bu kez tam başına oturdu. Niloya yapraklı tacıyla ormanda neşeyle dolaştı. Niloya taç yaparken dalı önce başına göre ölçmeyi öğrendi.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Niloya ince bir dala"
   - Cümle 2: «Niloya ince bir dala yapraklar takıp bir taç yaptı.»
   - Açıklama: Niloya adı art arda cümlelerde ve hikayede gereksiz sıklıkta tekrarlanıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Niloya'nın bir sorusu vardı"
   - Cümle 5: «Niloya'nın bir sorusu vardı: Dal çok mu uzundu?»
   - Açıklama: Karttaki 'soru' özelliği merak ettiğini sormaktır; burada kimseye soru sorulmuyor, yalnız anlatıcı bir sorusu olduğunu söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0013` birebir aynı, `@degisim: pedal -> dal` (tutuyorsan), ardından `@onarim: a8314cee6eb97086fb5aa79b6e884a9462ddd192`, sonra gövde.

### Hikâye 6: tohum niloya-0015 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: kayaların arkasından bir şarkı geldi ama söyleyen görünmedi | şarkıyı söyleyip cevap veren sesi buldu
@tohum: niloya-0015
@degisim: leke -> rüzgar
Tepelerde hafif bir rüzgar esiyordu. Niloya yeşil tepede sepetine kekik topluyordu. Birden kayaların arkasından bir şarkı sesi geldi. Ama tepede çok kaya vardı ve Niloya kimseyi göremedi. Bu, Niloya'nın en sevdiği şarkıydı. Niloya da aynı şarkıyı yüksek sesle söyledi. Hemen bir kayanın arkasından ses ona cevap verdi. Niloya o kayanın yanına yürüdü. Arkasında Mete oturuyordu. "Mete, sen miydin?" dedi Niloya. "Evet, bu şarkıyı senden öğrendim," dedi Mete. Mete elindeki kalın kekik demetini Niloya'nın sepetine kattı. İki arkadaş şarkı söyleyerek kekik toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden kayaların arkasından bir şarkı sesi geldi"
   - Cümle 3: «Birden kayaların arkasından bir şarkı sesi geldi.»
   - Açıklama: Görünmeyen birinin şarkı söylemesi Niloya için gerçek bir sorun değil, yalnız küçük bir merak.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya o kayanın yanına yürüdü"
   - Cümle 8: «Niloya o kayanın yanına yürüdü.»
   - Açıklama: Niloya kimin olduğunu bilmediği gizli bir sese büyüğe haber vermeden tek başına gidiyor; güvenli kullanım satırı merakın bir büyüğe haber vererek gösterilmesini ister.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "elindeki kalın kekik demetini"
   - Cümle 12: «Mete elindeki kalın kekik demetini Niloya'nın sepetine kattı.»
   - Açıklama: 'Kekik demeti' 3 yaşındaki bir çocuğun bilmeyeceği kelimeler içeriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0015` birebir aynı, `@degisim: leke -> rüzgar` (tutuyorsan), ardından `@onarim: 2a28d8aca35e0f5f763c4d07fe83efbebeec01bf`, sonra gövde.

### Hikâye 7: tohum niloya-0017 (deneme 3 -> 4)

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
Bir sabah Niloya ormanda topladığı fındıkları sepetine götürüyordu. Birden yerdeki küçük bir su birikintisinde beyaz, yuvarlak bir şey gördü. Niloya'nın bir sorusu vardı: Suya ay mı düşmüştü? Suyun yanına eğildi ve ona dikkatle baktı. Sonra suya küçük bir yaprak attı. Beyaz şey titredi ve dağıldı. Su durunca beyaz şey yine yerine geldi. Niloya başını kaldırıp gökyüzüne baktı. Ağaçların üstünde beyaz ay duruyordu. Ay suya hiç düşmemişti, gökyüzündeydi. Niloya gülümsedi ve fındık toplamaya neşeyle devam etti.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "topladığı fındıkları sepetine götürüyordu"
   - Cümle 1: «Bir sabah Niloya ormanda topladığı fındıkları sepetine götürüyordu.»
   - Açıklama: Niloya fındık toplamayı bitirip götürürken sonda fındık toplamaya devam ediyor; bu iki durum çelişiyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "eğildi ve ona dikkatle baktı"
   - Cümle 4: «Suyun yanına eğildi ve ona dikkatle baktı.»
   - Açıklama: 'Ona' zamirinin suyu mu yoksa beyaz şeyi mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0017` birebir aynı, `@degisim: yetenekli -> yuvarlak` (tutuyorsan), ardından `@onarim: 15d5639a231926a303120aaae1390bcf15268c58`, sonra gövde.

### Hikâye 8: tohum niloya-0019 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0019
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: kaybolan eşya
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'topaç', fiil 'gerinmek', sıfat 'mükemmel'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: toprak düz olmadığı için topaç çiçeklerin arasına yuvarlandı | çiçeklerin arasına baktı, sonra ayağa kalkınca topacı gördü
@tohum: niloya-0019
@degisim: mükemmel -> düz
Evin bahçesinde Niloya kırmızı topacını çeviriyordu. Topaç hızla döndü ama bahçenin toprağı düz değildi. Topaç bir yana kaydı ve çiçeklerin arasına yuvarlandı. Niloya topacın nereye gittiğini çok merak etti. Çiçeklerin arasına eğildi ve her yere baktı. Ama topaç orada yoktu. Niloya uzun süre eğilmişti. Ayağa kalktı ve gerindi. O sırada çitin yanında kırmızı bir şey gördü. Hemen oraya koştu. Topaç çitin dibinde duruyordu. Niloya topacını aldı ve sevinçle güldü. Niloya bundan sonra topacını hep düz yerde çevirdi.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Ama topaç orada yoktu"
   - Cümle 6: «Ama topaç orada yoktu.»
   - Açıklama: Topacın çiçeklerin arasına yuvarlandığı söylenip sonra orada olmadığı ve çitin dibinde olduğu açıklamasız kalıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ayağa kalktı ve gerindi"
   - Cümle 8: «Ayağa kalktı ve gerindi.»
   - Açıklama: Çözüm sebebe yönelmiyor; Niloya topacı aramayı bırakıp gerinirken tesadüfen buluyor.
   - Açıklama: Çözüm sebebe yönelmiyor; topaç gerinirken rastlantıyla görülüyor.
   - Açıklama: Niloya topacı sebebe yönelen bir çabayla değil, gerinirken tesadüfen görerek buluyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada çitin yanında kırmızı bir şey gördü"
   - Cümle 9: «O sırada çitin yanında kırmızı bir şey gördü.»
   - Açıklama: Topaç figürün bir eylemiyle değil sebepsiz bir rastlantıyla ortaya çıkıyor.
   - Açıklama: Topacın çitin dibinde bulunması sebepsizce, şans eseri geliyor.
   - Açıklama: Çözüm sebepsizce, şans eseri geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0019` birebir aynı, `@degisim: mükemmel -> düz` (tutuyorsan), ardından `@onarim: 7c7e841350e4c0e67ba77b07e351038863a401ce`, sonra gövde.

### Hikâye 9: tohum niloya-0020 (deneme 2 -> 3)

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
@plan: rüzgar oyuncak trompeti yokuştan aşağı yuvarladı | yokuşun dibine inip çalıların altına bakınca trompeti buldu
@tohum: niloya-0020
@degisim: kurmak -> bulmak
Niloya yeşil tepede oyuncak trompetini çalıyordu. Sonra onu çimenlere bıraktı ve kekik toplamaya başladı. Birden güçlü bir rüzgar esti ve trompet yokuştan aşağı yuvarlandı. Niloya arkasına döndü ama trompetini göremedi. Aceleci adımlarla yokuşun dibine indi. Orada büyük kekik çalıları vardı. Niloya çalıların yanına gitti ve merakla eğildi. İlk çalının arkasında hiçbir şey yoktu. İkinci çalının altında sarı bir şey parlıyordu. Bu, onun trompetiydi! Niloya onu aldı ve neşeyle üfledi. Trompetten güzel bir ses çıktı. Niloya çok sevindi, çünkü kaybolan trompetini bulmuştu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Aceleci adımlarla yokuşun dibine indi"
   - Cümle 5: «Aceleci adımlarla yokuşun dibine indi.»
   - Açıklama: Tek başına aceleyle yokuş aşağı inmek çocuğun taklit edebileceği düşme riski taşıyan bir davranış.
   - Açıklama: Yokuştan aceleyle inmek taklit edilince düşmeye yol açabilecek bir davranıştır.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Aceleci adımlarla yokuşun dibine"
   - Cümle 5: «Aceleci adımlarla yokuşun dibine indi.»
   - Açıklama: 'Aceleci' kişi özelliğidir, adımlara uymuyor; 'hızlı adımlarla' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0020` birebir aynı, `@degisim: kurmak -> bulmak` (tutuyorsan), ardından `@onarim: 0cb8b564bce52ba8067e29a07b0399cfd0bafc5c`, sonra gövde.

### Hikâye 10: tohum niloya-0022 (deneme 2 -> 3)

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
@plan: kaplumbağa havucun peşinden gidip kaydırağın altında sıkıştı | sesi duyunca eğildi ve onu yavaşça geri çekti
@tohum: niloya-0022
@degisim: sıkmak -> sıkışmak
Parkta Niloya, Tospik'e küçük sebze parçaları veriyordu. Bir havuç parçası yere düştü ve kaydırağın alçak ucunun altına yuvarlandı. Tospik havucun peşinden gitti ama kabuğu kaydırağa takıldı. Oradan ince bir ses geldi. Niloya merakla eğildi ve baktı. Tospik'in kabuğu kaydırakla yer arasında biraz sıkışmıştı. "Bana yardım eder misin, Niloya?" diye sordu Tospik. "Tabii, Tospik," dedi Niloya. Niloya kabuğu iki eliyle tuttu ve Tospik'i yavaşça geri çekti. Tospik kolayca dışarı çıktı. Niloya havuç parçasını da buldu ve ona verdi. Tospik havucu afiyetle yedi ve ikisi parkta mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "kabuğu kaydırağa takıldı"
   - Cümle 3: «Tospik havucun peşinden gitti ama kabuğu kaydırağa takıldı.»
   - Açıklama: Tospik'in kaydırağın altında sıkışıp kalması küçük çocuk için ürkütücü bir tehlike anı olabilir.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Niloya kabuğu iki eliyle tuttu"
   - Cümle 9: «Niloya kabuğu iki eliyle tuttu ve Tospik'i yavaşça geri çekti.»
   - Açıklama: Sıkışan hayvanı bir büyüğe haber vermeden kendi başına çekip çıkarmak taklit edilince hayvana zarar verebilir; güvenli kullanım satırı büyüğe haber vermeyi söyler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0022` birebir aynı, `@degisim: sıkmak -> sıkışmak` (tutuyorsan), ardından `@onarim: 94b68f00de64051f1582622650d7af7581d8daca`, sonra gövde.

### Hikâye 11: tohum niloya-0023 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | ev | babaannesi
@tohum: niloya-0023
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: sırayla oynamak
- yan: babaannesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'şeftali', fiil 'susamak', sıfat 'yağmurlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | babaannesi
@plan: uzun şarkıdan sonra çok susadı | sırayı babaannesine verip su içti
@tohum: niloya-0023
Yağmurlu bir günde damlalar cama tık tık vuruyordu. Niloya ile babaannesi evde sırayla şarkı söylüyordu. Niloya uzun bir şarkı söyledi ve sonunda çok susadı. "Babaanne, sıra sende, ben biraz su içeyim," dedi Niloya. Babaannesi gülümsedi ve yeni bir şarkıya başladı. Niloya mutfağa gitti ve bir bardak su içti. Masada sulu şeftaliler vardı. Niloya babaannesi için bir şeftali aldı. Geri gelip babaannesini sonuna kadar dinledi. Şarkı bitince şeftaliyi ona verdi. "Bu senin için, babaanneciğim," dedi Niloya. Sonra sıra yine Niloya'ya geldi ve o da neşeyle bir şarkı söyledi. "Seninle sırayla oynamak çok eğlenceli, babaanne!" dedi Niloya.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Niloya uzun bir şarkı söyledi ve sonunda çok susadı"
   - Cümle 3: «Niloya uzun bir şarkı söyledi ve sonunda çok susadı.»
   - Açıklama: Susayıp su içmek hikaye taşıyacak kadar önemli bir sorun değil, hemen kendiliğinden çözülüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Masada sulu şeftaliler vardı"
   - Cümle 7: «Masada sulu şeftaliler vardı.»
   - Açıklama: Şeftali sorunla (susuzluk) ilgisiz bir yan olay olarak beliriyor.
   - Açıklama: Şeftali sorunla ilgisiz biçimde beliriyor ve hikayeye ikinci, işlevsiz bir olay ekliyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Geri gelip babaannesini sonuna kadar dinledi"
   - Cümle 9: «Geri gelip babaannesini sonuna kadar dinledi.»
   - Açıklama: 'Sonuna kadar' babaanneye değil şarkıya bağlanmalı; 'babaannesinin şarkısını sonuna kadar dinledi' olmalı.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Seninle sırayla oynamak çok eğlenceli"
   - Cümle 13: «"Seninle sırayla oynamak çok eğlenceli, babaanne!" dedi Niloya.»
   - Açıklama: Niloya ile babaannesi oyun oynamıyor, şarkı söylüyor; 'oynamak' olaya uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0023` birebir aynı, ardından `@onarim: 42ca53ebb5dacdbfd542f089830721d135ec8c35`, sonra gövde.

### Hikâye 12: tohum niloya-0024 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | dedesi
@tohum: niloya-0024
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: bir şey yapmak
- yan: dedesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'teneke', fiil 'şaşırtmak', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | dedesi
@plan: boş kutuya elle vurunca ses zayıf çıktı | dedesine sordu ve kuru çubuklarla vurdu
@tohum: niloya-0024
Bir sabah Niloya ile dedesi yeşil tepede meyveli kurabiyeleri bitirdi. Niloya boş teneke kutudan bir davul yapmak istedi. Ama eliyle vurunca kutu çok zayıf bir ses çıkardı. Niloya kutuya neyle vurabileceğini dedesine sordu. Dedesi ona kuru bir çubukla vurmasını söyledi. Niloya çimenlerin arasında iki kuru çubuk buldu. Sonra çubuklarla kutuya sırayla vurdu. Tepede güçlü ve neşeli bir ses yayıldı. Bu ses ikisini de çok şaşırttı. Dedesi gülerek ellerini çırptı. Niloya davulunu çalarak tepede yürüdü. Niloya çok sevindi, çünkü kendi davulunu yapmıştı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bu ses ikisini de çok şaşırttı"
   - Cümle 9: «Bu ses ikisini de çok şaşırttı.»
   - Açıklama: Çubukla vurmayı dedesi önerdiği halde çıkan sese dedesinin de şaşırması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0024` birebir aynı, ardından `@onarim: d668a7182f2a5ded965c40de86dd70da76a94050`, sonra gövde.
