# Editör görevi (onarım): Niloya, onarım partisi 32

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/niloya_onar32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/niloya_onar32.txt --ad urun_v2`
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

### Hikâye 1: tohum niloya-0091 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Mete
@tohum: niloya-0091
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Mete
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'baharat', fiil 'ayırmak', sıfat 'sakar'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Niloya | orman | Mete
@plan: oyuncaklar dağınıktı ve baharat kutusu kayboldu | yaprakların altına merakla bakıp kutuyu buldu
@tohum: niloya-0091
@degisim: sakar -> dağınık
Ağaçlarda kuşlar ötüyordu. Niloya ile Mete ormanda yemek yapma oyunu oynuyordu. Ama Mete'nin oyuncakları yerde dağınıktı ve baharat kutusu kaybolmuştu. "Baharat kutum nerede, Niloya?" diye sordu Mete üzgün bir sesle. Niloya merakla etrafa baktı. Rüzgar ağaçlardan kuru yapraklar düşürmüştü. Niloya eğildi ve yaprakları elleriyle tek tek ayırdı. En büyük yaprağın altında küçük kırmızı bir kutu vardı. Niloya kutuyu hemen Mete'ye verdi. Mete kutuyu oyuncak tencerenin üstünde salladı. Niloya da kaşıkla çorbayı karıştırdı. "Teşekkürler, Niloya, çorba artık çok lezzetli oldu!" dedi Mete.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Mete'nin oyuncakları yerde dağınıktı"
   - Cümle 3: «Ama Mete'nin oyuncakları yerde dağınıktı ve baharat kutusu kaybolmuştu.»
   - Açıklama: Kayıp kutunun yanında oyuncakların dağınıklığı ikinci bir sorun olarak açılıyor ve hiç çözülmüyor.
   - Açıklama: Dağınık oyuncaklar ayrı bir sorun olarak veriliyor ama hiç ele alınmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0091` birebir aynı, `@degisim: sakar -> dağınık` (tutuyorsan), ardından `@onarim: b25b6b4637451973eba39b4a9032d15c700c191d`, sonra gövde.

### Hikâye 2: tohum niloya-0095 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0095
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'anahtar', fiil 'işaretlemek', sıfat 'havalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: rüzgar bulutları hızla değiştirdi | en yavaş bulutu bulup şekli işaretledi
@tohum: niloya-0095
@degisim: havalı -> beyaz
Rüzgar evin bahçesinde hafifçe esiyordu. Niloya kağıdına bir anahtar çizmişti. Bu şekli bulutlarda arıyordu, ama rüzgar beyaz bulutları hızla değiştiriyordu. Niloya'nın bir sorusu vardı: En yavaş bulut hangisiydi? Sonra bütün bulutlara tek tek baktı. Evin üstündeki büyük bulut çok yavaş gidiyordu. Niloya yalnız bu buluta uzun uzun baktı. Bulutun bir ucu yuvarlak, öbür ucu uzundu. Bu bulut tıpkı bir anahtara benziyordu. Niloya kağıttaki anahtarı kalemiyle işaretledi. Niloya çok sevindi, çünkü aradığı şekli bulutlarda görmüştü.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "rüzgar beyaz bulutları hızla değiştiriyordu"
   - Cümle 3: «Bu şekli bulutlarda arıyordu, ama rüzgar beyaz bulutları hızla değiştiriyordu.»
   - Açıklama: Rüzgar bulutları değiştirmez, şekillerini değiştirir; fiil nesnesine tam uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Niloya kağıttaki anahtarı kalemiyle işaretledi"
   - Cümle 10: «Niloya kağıttaki anahtarı kalemiyle işaretledi.»
   - Açıklama: Zaten çizili olan anahtarı işaretlemek hiçbir işe yaramayan bir eylem.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0095` birebir aynı, `@degisim: havalı -> beyaz` (tutuyorsan), ardından `@onarim: 45d70886f16a2c6980fff19f0c580871403f5fba`, sonra gövde.

### Hikâye 3: tohum niloya-0096 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | babaannesi
@tohum: niloya-0096
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: babaannesi
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'sandalye', fiil 'fısıldamak', sıfat 'güvenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | babaannesi
@plan: oyunda sepet boştu çünkü yerde fındık yoktu | babaannesine sordu ve yaprakların altında fındık buldu
@tohum: niloya-0096
@degisim: güvenli -> dolu
Niloya ormanda yemek oyunu oynuyordu. Sepete fındık koyacaktı. Ama sepeti boştu, çünkü yerde hiç fındık yoktu. Babaannesi sandalyede oturuyordu. Niloya ona koştu. "Babaanne, fındıklar nereye düşer?" diye sordu Niloya. Babaannesi gülümsedi. "Yaprakların altına bak," diye fısıldadı babaannesi. Niloya kuru yaprakları açtı. Altında çok fındık vardı! Niloya sepetini hemen doldurdu. Dolu sepeti ona verdi. "Yemeğin hazır, babaanne!" dedi Niloya. "Çok güzel olmuş, kızım," dedi babaannesi. Niloya çok sevindi, çünkü babaannesi oyunu sevmişti.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çünkü yerde hiç fındık yoktu"
   - Cümle 3: «Ama sepeti boştu, çünkü yerde hiç fındık yoktu.»
   - Açıklama: Yerde hiç fındık olmadığı söyleniyor ama sonra yerdeki yaprakların altında çok fındık çıkıyor; sebep çelişkili kuruluyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Niloya kuru yaprakları açtı"
   - Cümle 9: «Niloya kuru yaprakları açtı.»
   - Açıklama: Yapraklar açılmaz; 'kaldırdı' ya da 'araladı' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Altında çok fındık vardı"
   - Cümle 10: «Altında çok fındık vardı!»
   - Açıklama: Çoğul yapraklara iyelik uyumu yok; 'Altlarında' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0096` birebir aynı, `@degisim: güvenli -> dolu` (tutuyorsan), ardından `@onarim: f8c602e925ea7edcd08228ee834af468d4f95bba`, sonra gövde.

### Hikâye 4: tohum niloya-0097 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | -
@tohum: niloya-0097
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'battaniye', fiil 'güldürmek', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | -
@plan: şarkı çok uzundu ve sözler unutuldu | sözlerin yerine ormandaki şeyleri söyledi
@tohum: niloya-0097
Niloya ormanda yere büyük bir battaniye serdi. Battaniye onun sahnesiydi. Niloya orada eğlenceli bir şarkı oyunu oynuyordu. Ama şarkı çok uzundu ve Niloya ortasında sözleri unuttu. Oyunun bitmesini istemedi ve biraz düşündü. Sonra sözlerin yerine ormandaki şeyleri söylemeye başladı. Fındıkları, yaprakları ve ağaçları şarkıya kattı. Bir fındık yere düştü ve Niloya onu da şarkıya ekledi. Bu yeni şarkı Niloya'yı çok güldürdü. Niloya şarkıyı sonuna kadar söyledi. Niloya bundan sonra sözleri unutunca ormandaki şeyleri söyledi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Battaniye onun sahnesiydi"
   - Cümle 2: «Battaniye onun sahnesiydi.»
   - Açıklama: Battaniyeyi sahne yerine koyan mecaz 3 yaşındaki çocuğa uygun değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Niloya orada eğlenceli bir şarkı oyunu oynuyordu.»
   - Açıklama: Sorun ancak dördüncü cümlede söyleniyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Niloya ortasında sözleri unuttu"
   - Cümle 4: «Ama şarkı çok uzundu ve Niloya ortasında sözleri unuttu.»
   - Açıklama: 'Ortasında' neyin ortası olduğunu göstermiyor; 'şarkının ortasında' olmalı.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama şarkı çok uzundu ve Niloya ortasında sözleri unuttu.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor; ilk üç cümlede sorun yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0097` birebir aynı, ardından `@onarim: b919f8ba354e7f5e5aa9dace0845e1a81009fac8`, sonra gövde.

### Hikâye 5: tohum niloya-0098 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | Murat
@tohum: niloya-0098
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: sırayla oynamak
- yan: Murat
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'çeşme', fiil 'guruldamak', sıfat 'yalnız'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Niloya | orman | Murat
@plan: tek bir top vardı ve ikisi de istedi | şarkı bitene kadar sırayla oynamayı önerdi
@tohum: niloya-0098
@degisim: çeşme -> top
Niloya ile Murat ormanda fındık ağaçlarının arasında oynuyordu. Yanlarında yalnız bir top vardı. İkisi de topu ilk atmak istedi ve oyun durdu. Niloya biraz düşündü. "Murat, bir şarkı boyunca sen oyna, sonra ben," dedi Niloya. "Olur, önce sen söyle," dedi Murat. Murat topu aldı ve Niloya kısa bir şarkı söyledi. Şarkı bitince Murat topu Niloya'ya verdi. Sonra Murat şarkı söyledi ve Niloya topu attı. Oyunun sonunda Murat'ın karnı guruldadı. İkisi ağacın altındaki fındıkları da sırayla mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Murat'ın karnı guruldadı"
   - Cümle 10: «Oyunun sonunda Murat'ın karnı guruldadı.»
   - Açıklama: Oyun sorunu çözüldükten sonra sebepsiz yeni bir olay (açlık) ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oyunun sonunda Murat'ın karnı guruldadı"
   - Cümle 10: «Oyunun sonunda Murat'ın karnı guruldadı.»
   - Açıklama: Karın guruldaması top sorunundan çıkmayan, sona eklenmiş işlevsiz yeni bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0098` birebir aynı, `@degisim: çeşme -> top` (tutuyorsan), ardından `@onarim: 94b05f1c21c302fca931df6c8f5389f5460ccbbc`, sonra gövde.

### Hikâye 6: tohum niloya-0099 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | orman | dedesi
@tohum: niloya-0099
- yer: orman (Köyün yanında ağaçların olduğu yer; meyve ağaçları ve fındık ağaçları vardır.)
- tema: bir şey yapmak
- yan: dedesi
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'elma', fiil 'yollamak', sıfat 'umutlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | orman | dedesi
@plan: sepete on elma koyacaklardı ama sayı karıştı | şarkı söyleyerek elmaları tek tek saydı
@tohum: niloya-0099
@degisim: yollamak -> saymak
Bir sabah Niloya ile dedesi ormanda elma topluyordu. Dedesi, "Bu sepete on elma koyalım," dedi. Ama yerde çok elma vardı ve Niloya sayıyı karıştırdı. Niloya biraz düşündü ve umutlu bir yüzle dedesine baktı. "Dede, sayarken şarkı söyleyelim mi?" diye sordu Niloya. Dedesi başını salladı. Niloya sepeti boşalttı ve şarkıya başladı. "Bir, iki, üç elma, gel sepete elma!" diye söyledi Niloya. Şarkıdaki her sayıda sepete bir elma koydu. Şarkı bitince sepette tam on elma vardı. "Aferin, Niloya, sepet hazır!" dedi dedesi. Niloya çok sevindi, çünkü sepeti dedesiyle doldurmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "umutlu bir yüzle dedesine"
   - Cümle 4: «Niloya biraz düşündü ve umutlu bir yüzle dedesine baktı.»
   - Açıklama: 'Umutlu bir yüzle' soyut bir anlatım, 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Umutlu' soyut bir kelime ve 3 yaşındaki çocuk için zor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0099` birebir aynı, `@degisim: yollamak -> saymak` (tutuyorsan), ardından `@onarim: 9c7a4d1cdf71136e0986b41241e9d85ca562e969`, sonra gövde.

### Hikâye 7: tohum niloya-0100 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0100
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şarkı (Şarkı söylemeyi çok sever.)
- kelimeler: isim 'boru', fiil 'yıkanmak', sıfat 'kırık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: dalın kırık yerinde delik vardı ve ses az çıktı | deliği parmağıyla kapatıp yeniden söyledi
@tohum: niloya-0100
@degisim: yıkanmak -> ıslanmak
Yağmur yeni dinmişti ve tepedeki otlar ıslanmıştı. Niloya otların arasında boru gibi içi boş bir dal buldu. İçine ilk kez şarkı söyledi, ama ses çok az çıktı. Niloya dalı çevirdi ve kırık yerde küçük bir delik gördü. Deliği parmağıyla sıkıca kapattı. Sonra en sevdiği şarkıyı yeniden dalın içine söyledi. Bu kez ses yüksek ve çok komik çıktı. Niloya güldü ve şarkısını bir kez daha söyledi. Niloya çok mutlu oldu, çünkü deliği kapatınca şarkısı çok güzel çıkmıştı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ses yüksek ve çok komik çıktı"
   - Cümle 7: «Bu kez ses yüksek ve çok komik çıktı.»
   - Açıklama: Ses önce komik çıktı deniyor, son cümlede ise şarkının çok güzel çıktığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0100` birebir aynı, `@degisim: yıkanmak -> ıslanmak` (tutuyorsan), ardından `@onarim: d78ea93269e7e7ac9c80aeb90b04cc8541720b0b`, sonra gövde.

### Hikâye 8: tohum niloya-0101 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | -
@tohum: niloya-0101
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'tereyağı', fiil 'gizlenmek', sıfat 'kocaman'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | -
@plan: rüzgar esince kule yıkıldı çünkü taşlar yuvarlaktı | etrafa merakla bakıp düz taşlar buldu
@tohum: niloya-0101
@degisim: tereyağı -> taş
Yaylada serin bir rüzgar esiyordu. Niloya yeşil tepede taşlardan kocaman bir kule yapmak istiyordu. Ama rüzgar esince kule hemen yıkıldı, çünkü taşlar çok yuvarlaktı. Yuvarlak taşlar çimlerin üstünde zıplaya zıplaya gitti. Niloya buna çok güldü. Sonra düz taşlar bulmak için etrafa merakla baktı. Uzun otların altında gizlenmiş birkaç düz taş gördü. Niloya onları tek tek topladı. Sonra taşları üst üste dikkatle dizdi. Rüzgar yine esti, ama kule bu kez yıkılmadı. Kule Niloya'nın dizine kadar yükseldi. Niloya çok sevindi, çünkü düz taşlarla sağlam bir kule yapmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yuvarlak taşlar çimlerin üstünde zıplaya zıplaya gitti"
   - Cümle 4: «Yuvarlak taşlar çimlerin üstünde zıplaya zıplaya gitti.»
   - Açıklama: Taşların zıplaması ve Niloya'nın buna gülmesi olaya hiçbir şey katmayan işlevsiz ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0101` birebir aynı, `@degisim: tereyağı -> taş` (tutuyorsan), ardından `@onarim: 7d5f772679922ce4a23b1a838e20f16b58f19f81`, sonra gövde.

### Hikâye 9: tohum niloya-0103 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | dağ | Tospik
@tohum: niloya-0103
- yer: dağ (Köyün yanındaki tepeler ve yayla; kekik toplanan yeşil tepeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Tospik
- özellik: soru (Merak ettiği her şeyi sorar.)
- kelimeler: isim 'atkı', fiil 'takılmak', sıfat 'dalgalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | dağ | Tospik
@plan: rüzgar atkıyı uçurdu ve atkı bir çalıya takıldı | kaplumbağasından yardım istedi ve atkıyı birlikte kurtardılar
@tohum: niloya-0103
Tepede serin bir rüzgar esiyordu. Niloya ile Tospik orada kekik topluyordu. Birden rüzgar Niloya'nın atkısını uçurdu ve atkı bir çalıya takıldı. Niloya dalgalı çizgili atkısını çok seviyordu. Atkı çalının en alt dalına dolanmıştı. Niloya çalının altına sığmıyordu. Niloya, Tospik'ten yardım istedi. Ona bir soru sordu: Çalının altına girebilir miydi? Tospik başını salladı ve yavaşça çalının altına girdi. Sonra atkıyı daldan itti. Niloya atkıyı dikkatle çekti ve atkı daldan çıktı. Niloya atkısını boynuna sardı ve Tospik'e sarıldı. Niloya çok sevindi, çünkü atkıyı Tospik ile birlikte kurtarmışlardı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Çalının altına girebilir miydi?"
   - Cümle 8: «Ona bir soru sordu: Çalının altına girebilir miydi?»
   - Açıklama: Tırnaksız dolaylı soruda çalının altına kimin gireceği belli değil; özne Niloya da Tospik de olabilir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Ona bir soru sordu"
   - Cümle 8: «Ona bir soru sordu: Çalının altına girebilir miydi?»
   - Açıklama: Karttaki özellik merak ettiğini sormak iken soru burada merakla değil bir yardım ricası olarak kullanılıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "atkıyı Tospik ile birlikte kurtarmışlardı"
   - Cümle 13: «Niloya çok sevindi, çünkü atkıyı Tospik ile birlikte kurtarmışlardı.»
   - Açıklama: Özne Niloya ve 'Tospik ile birlikte' varken fiil çoğul çekilmiş; 'kurtarmıştı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0103` birebir aynı, ardından `@onarim: dc39ff97cd4ab514f6cfef1c4b447860ef09db11`, sonra gövde.

### Hikâye 10: tohum niloya-0105 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0105
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: kaybolan eşya
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'kurabiye', fiil 'büyütmek', sıfat 'şekerli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: rüzgar kurabiye torbasını uçurdu | merak edip evin arkasındaki otlara baktı ve buldu
@tohum: niloya-0105
@degisim: büyütmek -> aramak
Bahçede güçlü bir rüzgar esiyordu. Niloya şekerli kurabiyelerini bir torbaya koymuştu. Ama rüzgar torbayı uçurdu ve uzağa götürdü. Niloya torbayı bahçede aradı. Önce çiçeklere baktı ama torba orada yoktu. Sonra kapının önüne baktı, orada da yoktu. Niloya evin arkasındaki uzun otları merak etti. Oraya gitti ve otları eliyle açtı. Torba otların arasındaydı! Niloya torbayı açıp içine baktı. Kurabiyeler kırılmamıştı. Niloya bir kurabiye yedi ve güldü. Niloya çok sevindi, çünkü kurabiyelerini kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar torbayı uçurdu ve uzağa götürdü"
   - Cümle 3: «Ama rüzgar torbayı uçurdu ve uzağa götürdü.»
   - Açıklama: Rüzgar torbayı uçuruyor, Niloya buluyor ve bitiyor; sorun önemsiz bir olay.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce çiçeklere baktı ama torba orada yoktu"
   - Cümle 5: «Önce çiçeklere baktı ama torba orada yoktu.»
   - Açıklama: Çözüm rüzgarın yönüne yönelmiyor, rastgele üç yere bakılıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 7: «Niloya evin arkasındaki uzun otları merak etti.»
   - Açıklama: Niloya torbayı ancak çiçekler ve kapıdan sonra üçüncü denemede otlarda buluyor; çözüm iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0105` birebir aynı, `@degisim: büyütmek -> aramak` (tutuyorsan), ardından `@onarim: 1439745a36af71f31cd783bda4094b29e19f5b7a`, sonra gövde.

### Hikâye 11: tohum niloya-0106 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Niloya | ev | -
@tohum: niloya-0106
- yer: ev (Niloya'nın nehir kenarındaki köy evi ve bahçesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: keşfet (Öğrenmeyi, merak ettiği yerlere bakmayı ve yeni şeyler bulmayı sever.)
- kelimeler: isim 'yumurta', fiil 'solmak', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Niloya | ev | -
@plan: yolda bir taş vardı ve yumurta çimlere yuvarlandı | merakla bakıp yumurtayı yaprakların arasında buldu
@tohum: niloya-0106
@degisim: düzenli -> yavaş
Bir sabah Niloya evin bahçesinde eğlenceli bir oyun oynuyordu. Kaşığın üstünde haşlanmış bir yumurta taşıyordu. Ama yolda bir taş vardı ve yumurta düşüp çimlere yuvarlandı. Niloya yumurtayı göremedi. Önce merakla çalıların altına baktı ama orada bir şey yoktu. Sonra bahçenin ucundaki solmuş yaprakların arasına baktı. Yumurta yaprakların içinde duruyordu. Niloya yumurtayı aldı ve yeniden kaşığa koydu. Bu kez taşın yanından yavaş adımlarla geçti. Yumurta hiç düşmedi. Niloya sonunda kapıya vardı ve ellerini çırptı. Niloya çok mutluydu, çünkü hem yumurtayı bulmuş hem de oyunu bitirmişti.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bu kez taşın yanından yavaş adımlarla geçti"
   - Cümle 9: «Bu kez taşın yanından yavaş adımlarla geçti.»
   - Açıklama: Çözüm çalılara bakma, yapraklara bakma ve taştan yavaş geçme olarak ikiden fazla adıma yayılıyor ve sebep olan taşa ancak sonda dönülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0106` birebir aynı, `@degisim: düzenli -> yavaş` (tutuyorsan), ardından `@onarim: 8228c9c5c8f73db8153ad6b38595759240078c27`, sonra gövde.

### Hikâye 12: tohum niloya-0109 (deneme 2 -> 3)

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
@plan: torba dala takıldı, ipi çözüldü ve cevizler döküldü | yaprakların altına bakıp cevizleri tek tek buldu
@tohum: niloya-0109
Ormanda kuşlar ötüyordu. Niloya, Mete'nin doğum günü için bir torba ceviz getirmişti. Ama torba bir dala takıldı, ipi çözüldü ve cevizler yapraklara döküldü. Mete biraz uzakta, oyuncaklarıyla oynuyordu ve bunu görmedi. Niloya, cevizler nereye gitti diye merak etti. Kabarık yaprakları tek tek kaldırdı ve altlarına baktı. Bütün cevizleri bulup torbaya koydu. Sonra torbanın ipini sıkıca bağladı. "Mete, sana bir hediyem var!" dedi Niloya. Mete koşarak geldi ve torbayı açtı. "Çok teşekkür ederim, Niloya!" dedi Mete. İkisi bir ağacın altına oturdu ve cevizleri mutlu mutlu paylaştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kabarık yaprakları tek tek"
   - Cümle 6: «Kabarık yaprakları tek tek kaldırdı ve altlarına baktı.»
   - Açıklama: 'Kabarık' yaprak için doğal bir sıfat değil; 'yere düşen yaprakları' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: niloya-0109` birebir aynı, ardından `@onarim: e7cc2917ecd677ee556086ca23c9afdf8e561567`, sonra gövde.
