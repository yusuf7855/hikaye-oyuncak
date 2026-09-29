# Editör görevi (onarım): Niloya, onarım partisi 23

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar23.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar23.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0054 (deneme 5 -> 6)

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
@plan: kaplumbağa yavaş olduğu için hiç fındık bulamadı | fındıklarının yarısını ona ayırıp şarkıyla onu uyandırdı
@tohum: niloya-0054
@degisim: devasa -> kocaman
Bir sabah Niloya ile Tospik ormanda fındık topluyordu. Niloya'nın sepeti çabucak doldu. Ama Tospik çok yavaştı ve hiç fındık bulamadı. Tospik yoruldu ve kocaman bir elma ağacının altında uyudu. Niloya fındıklarının yarısını Tospik'e vermek istedi. Niloya bir yaprağı alet gibi kullandı ve fındıklardaki toprağı fırçaladı. Sonra fındıkları Tospik'in yanına koydu. Tospik'i uyandırmak için yavaş ve neşeli bir şarkı söyledi. Tospik şarkıyı duydu ve gözlerini açtı. "Tospik, bu fındıklar senin," dedi Niloya. "Teşekkür ederim, Niloya," dedi Tospik. Niloya bundan sonra topladığı fındıkları hep Tospik'le paylaştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir yaprağı alet gibi kullandı"
   - Cümle 6: «Niloya bir yaprağı alet gibi kullandı ve fındıklardaki toprağı fırçaladı.»
   - Açıklama: 'Alet gibi kullandı' soyut bir benzetme, küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir yaprağı alet gibi"
   - Cümle 6: «Niloya bir yaprağı alet gibi kullandı ve fındıklardaki toprağı fırçaladı.»
   - Açıklama: 'Alet gibi kullandı' küçük çocuk için soyut ve belirsiz bir anlatım.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya bir yaprağı alet gibi kullandı"
   - Cümle 6: «Niloya bir yaprağı alet gibi kullandı ve fındıklardaki toprağı fırçaladı.»
   - Açıklama: Yaprakla fındık fırçalama sorunla ilgisiz, işlevsiz bir ayrıntı.
   - Açıklama: Fındıkları yaprakla fırçalama ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0054` birebir aynı, `@degisim: devasa -> kocaman` (tutuyorsan), ardından `@onarim: a22b94328484f80557d802fa0050a8b080c0017b`, sonra gövde.

### Hikâye 2: tohum niloya-0076 (deneme 3 -> 4)

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
@plan: rüzgar esince örtü hep uçuyordu | dört taş bulup örtünün üstüne koydu
@tohum: niloya-0076
@degisim: damga -> börek
Bir sabah Niloya dedesiyle yeşil tepeye çıktı. Dede kekik toplarken Niloya ona sürpriz bir sofra kurmak istedi. Ama rüzgar esiyordu ve çimenlerdeki örtü hep uçuyordu. Niloya merakla çevresine baktı. Kekiklerin arasına karışmış dört büyük taş buldu. Taşları örtünün dört ucuna koydu. Bu kez örtü hiç uçmadı. Niloya sepetteki peynirli böreği örtünün ortasına koydu. "Dedeciğim, gel, sana bir sürprizim var!" dedi Niloya. Dede geldi ve sofrayı gördü. "Ne güzel bir sofra, teşekkürler, Niloya," dedi dede. İkisi böreği birlikte yedi. Niloya çok mutluydu, çünkü dedesini sevindirmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kekiklerin arasına karışmış dört büyük taş"
   - Cümle 5: «Kekiklerin arasına karışmış dört büyük taş buldu.»
   - Açıklama: Taşlar kekiklere karışmaz; 'kekiklerin arasında' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0076` birebir aynı, `@degisim: damga -> börek` (tutuyorsan), ardından `@onarim: 0ea04a44f16a278673ab68e21e551ce4fdd32694`, sonra gövde.

### Hikâye 3: tohum niloya-0079 (deneme 3 -> 4)

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
Hava çok güneşliydi. Niloya ile babaannesi fındık topluyordu ve ikisi de acıktı. Ama sepette tek dilim reçelli ekmek vardı. "Babaanne, bu ekmeği ikimiz paylaşalım," dedi Niloya. Babaanne ekmeği ikiye böldü ve yarısını ona verdi. Ama yarım ekmekle ikisi de doymadı. Niloya meyve ağaçlarının arasına merakla baktı. Yere yakın bir dalda kırmızı kirazlar gördü. Eteğini tuttu ve kirazları içine topladı. Kirazların yarısını da babaannesine verdi. Babaanne kirazları yedi ve güldü. "İkimiz de doyduk, Niloya," dedi babaanne. "Afiyet olsun, babaanneciğim!" dedi Niloya.
```

**Hakem bulguları (2):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ama yarım ekmekle ikisi de doymadı"
   - Cümle 6: «Ama yarım ekmekle ikisi de doymadı.»
   - Açıklama: İlk çözüm işe yaramıyor ve sorun ikinci ayrı bir çözümle kapanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yere yakın bir dalda kırmızı kirazlar"
   - Cümle 8: «Yere yakın bir dalda kırmızı kirazlar gördü.»
   - Açıklama: Kirazlar önceden kurulmadan beliriyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0079` birebir aynı, ardından `@onarim: 9dfc03c6e400ddc8a72670f1d08797d4a10f2bb2`, sonra gövde.

### Hikâye 4: tohum niloya-0082 (deneme 3 -> 4)

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
@plan: tomurcuk kapalıydı ve içi görünmüyordu | güneşin gelmesini bekledi ve açılan çiçeği gördü
@tohum: niloya-0082
@degisim: şapkalı -> mor
Yeşil tepede güneş yeni doğuyordu. Niloya kekiklerin yanında küçük bir tomurcuk buldu. Onun içini görmek istedi ama tomurcuk sımsıkı kapalıydı. Üstünde boncuk gibi su damlaları vardı. Tomurcuk neden açılmıyordu? Niloya bu soruyu düşündü ve çevreye baktı. Tomurcuğun üstüne daha güneş ışığı gelmemişti. Niloya ona hiç dokunmadı. Çimenlere oturdu ve ona baktı. Sonra güneş yükseldi ve ışığı çiçeğe değdi. Su damlaları yavaş yavaş kurudu. Sonunda tomurcuk açıldı. İçinden mor yapraklar çıktı. Niloya bundan sonra kapalı bir tomurcuk görünce güneşin gelmesini bekledi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "boncuk gibi su damlaları"
   - Cümle 4: «Üstünde boncuk gibi su damlaları vardı.»
   - Açıklama: Benzetme 3 yaşındaki çocuk için mecazlı anlatım.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sonra güneş yükseldi ve ışığı çiçeğe değdi"
   - Cümle 10: «Sonra güneş yükseldi ve ışığı çiçeğe değdi.»
   - Açıklama: Sorunu Niloya değil güneş çözüyor; Niloya yalnız oturup bakıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0082` birebir aynı, `@degisim: şapkalı -> mor` (tutuyorsan), ardından `@onarim: acd68d620f14bd06068cbaa9508c2e0e706ab016`, sonra gövde.

### Hikâye 5: tohum niloya-0083 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0083
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: babaannesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'yama', fiil 'dikmek', sıfat 'kirli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: toprak yumuşaktı ve dal hep yere düştü | sert bir toprak bulup dalı oraya dikti
@tohum: niloya-0083
@degisim: yama -> dal
Ormanda Niloya ile babaannesi fındık ağaçlarının altında oyun oynuyordu. Babaanne ince bir dalı toprağa koymuştu ve sırayla dala fındık atıyorlardı. Ama toprak çok yumuşaktı, bu yüzden fındık değince dal hep yere düştü. "Böyle oynayamayız," dedi babaannesi. Niloya etrafa merakla baktı. Büyük bir taşın yanındaki toprağa elini bastırdı. Toprak sertti ve eli hiç kirli olmadı. Dalı oraya götürdü ve toprağa sıkıca dikti. Babaannesi ilk fındığı attı ve fındık dala değdi. Bu sefer dal yere düşmedi. Niloya sevinçle ellerini çırptı. "Sıra sende, Niloya, dalımız artık hiç düşmüyor!" dedi babaannesi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "dal hep yere düştü"
   - Cümle 3: «Ama toprak çok yumuşaktı, bu yüzden fındık değince dal hep yere düştü.»
   - Açıklama: Tekrarlanan olay 'hep' ile anlatılırken '-dı' yerine 'düşüyordu' olmalı; aynı kusur plan satırında da var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0083` birebir aynı, `@degisim: yama -> dal` (tutuyorsan), ardından `@onarim: 43963212b27d0f24181651b52a6db35fabb989e1`, sonra gövde.

### Hikâye 6: tohum niloya-0084 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | park | -
@tohum: niloya-0084
- yer: park (Köydeki çocuk parkı; kaydırak ve oyuncaklar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'çekmece', fiil 'yedirmek', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | park | -
@plan: oyuncak saat düştü ve hiçbir yerde görünmedi | çalan saatin sesini izleyip saati çekmecede buldu
@tohum: niloya-0084
@degisim: yedirmek -> susmak
Bir sabah Niloya parktaki oyuncak mutfakta oynuyordu. Kırmızı oyuncak saatini mutfağın üstüne koymuştu. Ama saat oradan düşmüştü ve Niloya onu hiçbir yerde göremedi. Birden değişik bir çın çın sesi duyuldu. Niloya bu sesin nereden geldiğini çok merak etti. Sese doğru yavaşça yürüdü. Ses, mutfağın yarı açık çekmecesinden geliyordu. Niloya çekmeceyi açtı ve içine baktı. Kırmızı saati orada buldu ve saat çalıyordu. Saat düşerken açık çekmeceye girmişti. Niloya saatin düğmesine bastı ve saat sustu. Sonra saati sevinçle cebine koydu. Niloya bundan sonra sevdiği saatini hep cebinde taşıdı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden değişik bir çın çın sesi duyuldu"
   - Cümle 4: «Birden değişik bir çın çın sesi duyuldu.»
   - Açıklama: Saatin tam o anda çalması sebepsiz bir rastlantı olarak çözümü getiriyor.
   - Açıklama: Saat hiçbir sebep olmadan çalmaya başlıyor ve çözümü tesadüfle getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0084` birebir aynı, `@degisim: yedirmek -> susmak` (tutuyorsan), ardından `@onarim: ffc972b9309ba5af099eb72f8af4e1f9db5d3555`, sonra gövde.

### Hikâye 7: tohum niloya-0086 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Mete
@tohum: niloya-0086
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: paylaşmak
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'elmas', fiil 'çizmek', sıfat 'cömert'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | dağ | Mete
@plan: arkadaşının tek kaleminin ucu kırıldı | çantasındaki renkli kalemleri onunla paylaştı
@tohum: niloya-0086
@degisim: cömert -> renkli
Niloya ile Mete tepede oturmuş, kağıda resim çiziyordu. Mete'nin tek bir kalemi vardı ve kalemin ucu birden kırıldı. Mete elmas resmini bitiremedi ve çok üzüldü. Niloya çantasının içine merakla baktı. Çantada üç tane renkli kalem vardı. "Mete, kırmızı kalemi sen al," dedi Niloya. "Çok teşekkür ederim, Niloya," dedi Mete. Mete kırmızı kalemle elmasını bitirdi. Niloya da mavi kalemle bir çiçek çizdi. Yeşil kalemi ise sırayla kullandılar. İkisi mutlu mutlu resim yapmaya devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kalemin ucu birden kırıldı"
   - Cümle 2: «Mete'nin tek bir kalemi vardı ve kalemin ucu birden kırıldı.»
   - Açıklama: Kalemin ucunun neden kırıldığı söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0086` birebir aynı, `@degisim: cömert -> renkli` (tutuyorsan), ardından `@onarim: c066950daabd6144267e48caa000c998c0ca1b5e`, sonra gövde.

### Hikâye 8: tohum niloya-0087 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0087
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'bilye', fiil 'taşmak', sıfat 'zor'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: kekikleri alırken bilyesi düştü ve kayboldu | tık sesinin geldiği yere gidip bilyeyi buldu
@tohum: niloya-0087
Tepede Niloya küçük sepetine kekik topluyordu. Sepet çok doldu ve kekikler kenarından taştı. Niloya onları alırken cebinden mavi bilyesi düştü. Bilye yokuştan yuvarlandı ve otların arasında kayboldu. Otlar çok sıktı ve bilyeyi görmek zordu. Birden otların arasından küçük bir tık sesi geldi. Niloya'nın aklına bir soru geldi: Sesi bilye mi yapıyordu? Niloya o yere yavaşça yürüdü. Otları eliyle araladı ve dikkatle baktı. Mavi bilye küçük bir taşın yanında duruyordu. Bilye yuvarlanırken bu taşa tık diye çarpmıştı. Niloya bilyeyi aldı ve cebine koydu. Niloya çok sevindi, çünkü en sevdiği bilyesini bulmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Birden otların arasından küçük bir tık sesi geldi"
   - Cümle 6: «Birden otların arasından küçük bir tık sesi geldi.»
   - Açıklama: Bilye çoktan kaybolmuşken tık sesi sebepsizce sonradan duyuluyor ve çözümü tesadüfle getiriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Niloya'nın aklına bir soru geldi"
   - Cümle 7: «Niloya'nın aklına bir soru geldi: Sesi bilye mi yapıyordu?»
   - Açıklama: 'Aklına soru gelmek' deyimsel ve soyut bir anlatım.
   - Açıklama: 'Aklına bir soru gelmek' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0087` birebir aynı, ardından `@onarim: ab5d537d5e5b3b691f3f25546c57ef3d19f186a9`, sonra gövde.

### Hikâye 9: tohum niloya-0089 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | annesi
@tohum: niloya-0089
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'koni', fiil 'yalamak', sıfat 'süslü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | ev | annesi
@plan: kekten parmağıyla krema alıp yaladı | annesinden özür diledi ve çukuru kremayla kapattı
@tohum: niloya-0089
@degisim: koni -> krema
Dışarıda yağmur yağıyordu. Niloya'nın annesi mutfakta süslü bir kek yapmıştı. Niloya kekin kenarından parmağıyla biraz krema aldı ve yaladı. Kekin kenarında küçük bir çukur oldu. Annesi mutfağa geldi ve keke baktı. "Özür dilerim, anne, kremayı sormadan yedim," dedi Niloya. "Doğruyu söyledin, sağ ol, Niloya," dedi annesi. Niloya çukuru kapatmak istedi. Mutfağa merakla baktı ve kasede kalan kremayı buldu. Kremayı kaşıkla aldı ve çukuru güzelce kapattı. Kek yine eskisi gibi oldu. "Anneciğim, bundan sonra önce sana soracağım!" dedi Niloya.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Mutfağa merakla baktı ve"
   - Cümle 9: «Mutfağa merakla baktı ve kasede kalan kremayı buldu.»
   - Açıklama: Kremayı arayan Niloya için 'merakla' uygun değil ve zaten mutfakta olduğu için 'mutfağa baktı' anlamca yanlış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0089` birebir aynı, `@degisim: koni -> krema` (tutuyorsan), ardından `@onarim: 4e522d2cd9665f2bc6b43da797dc034752a96a42`, sonra gövde.

### Hikâye 10: tohum niloya-0090 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | dedesi
@tohum: niloya-0090
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'kavun', fiil 'kurulamak', sıfat 'ilginç'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | dedesi
@plan: kavun çok ağırdı ve kaldıramadı | dedesinden yardım istedi ve birlikte taşıdılar
@tohum: niloya-0090
@degisim: ilginç -> ağır
Niloya bahçede büyük bir kavun buldu. Kavunu dedesiyle mutfakta yemek istedi. Ama kavun çok ağırdı ve Niloya onu kaldıramadı. "Dedeciğim, kavunu taşımama yardım eder misin?" diye sordu Niloya. Dedesi hemen geldi ve kavunun bir yanından tuttu. Niloya da öbür yanından tuttu. "Aynı anda adım atalım," dedi dedesi. Niloya neşeli bir şarkı söyledi ve ikisi aynı anda yürüdü. Kavunu yavaş yavaş eve taşıdılar. Kavun topraktan kirlenmişti. Niloya onu suyla yıkadı ve havluyla kuruladı. Dedesi kavunu dilim dilim kesti ve ikisi birlikte yedi. Niloya çok sevindi, çünkü dedesinin yardımıyla kavunu eve taşımıştı.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Kavun topraktan kirlenmişti"
   - Cümle 10: «Kavun topraktan kirlenmişti.»
   - Açıklama: Taşıma sorunu çözüldükten sonra kavunun kirlenmesi ikinci bir sorun olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0090` birebir aynı, `@degisim: ilginç -> ağır` (tutuyorsan), ardından `@onarim: ad6490430acf27c2a427dd718fac933d0ca124e8`, sonra gövde.
