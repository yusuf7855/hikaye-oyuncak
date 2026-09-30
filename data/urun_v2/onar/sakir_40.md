# Editör görevi (onarım): Şakir, onarım partisi 40

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar40.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Şakir | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar40.txt --ad urun_v2`
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

## Kart: Şakir (kaynaklı, kapalı dünya)

- Ad: Şakir (okunuş: şakir; kesme eki okunuşa uyar)
- Kimlik: Şakir, ailesiyle bir apartmanda yaşayan, okula giden yavru bir aslandır.
- Tür: aslan
- Güvenli özellik kullanımı: Şakir'in macerası güvenli bir oyun olarak kalır; yüksekten atlamaz, ateşle oynamaz, tek başına uzağa gitmez.
- Özellikler:
  - şapka: Hep şapka takar; şapkası yerden yere değişir. (örnek biçimler: şapka, şapkasını)
  - macera: Macerayı çok sever. (örnek biçimler: macera, macerayı)
- Yerler:
  - deniz: Deniz kıyısı ve kumsal.
  - orman: Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.
  - park: Şehirdeki park.
  - ev: Şakir'in ailesiyle yaşadığı apartman dairesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Remzi: Şakir'in ve Canan'ın babası; kırmızı kazak giyer, bankada çalışır, çocuk gibi eğlenir. Tür: aslan; konuşur. Yüzey biçimleri: Remzi, baba, babası, babacığım
  - Kadriye: Şakir'in ve Canan'ın annesi. Tür: kedi; konuşur. Yüzey biçimleri: Kadriye, anne, annesi, anneciğim
  - Canan: Şakir'in kız kardeşi; çok akıllıdır, kitap okumayı sever. Tür: kedi; konuşur. Yüzey biçimleri: Canan, kardeş, kardeşi
  - Necati: Remzi'nin en iyi arkadaşı; sık sık Şakir'lerin evine gelir, yemek yer ve oyun oynar. Tür: fil; konuşur. Yüzey biçimleri: Necati, Fil Necati, fil
- Dünya kuralları:
  - Remzi ve Şakir aslandır; Kadriye ve Canan beyaz kedidir; Necati mor bir fildir.
  - Necati Şakir'in akrabası değil, babasının arkadaşıdır; Şakir'in dedesi ve başka akrabası kartta yoktur.
- Yasak adlar: Peyami, Filsu, Tanju, Mirket, Kürşat, Ercan, Necmi, Cüneyt, Polat, Kumpir, Cemşit, Arif, Vedat, Refik
- Yasak: Video oyunu ve ekran başında oyun hikayeye girmez.
- İzinli dünya kelimeleri: şapka, aslan, apartman, macera, fil

## Onarılacak hikâyeler

### Hikâye 1: tohum sakir-0203 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0203
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'maske', fiil 'düzenlemek', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: çadırın içinden bir tık tık sesi geldi | şapkasına bir damla düştü ve yukarıdaki deliği gördü
@tohum: sakir-0203
Yağmur yeni dinmişti. Şakir çadırın içinde eşyalarını düzenliyordu. Birden bir tık tık sesi duydu ve bu sesi çok merak etti. Ses çadırın ortasından geliyordu ama orada yalnız yepyeni maskesi vardı. Şakir maskeye doğru eğildi. O anda şapkasının üstüne bir damla düştü ve tık diye ses çıktı. Şakir hemen yukarı baktı. Çadırın tepesinde küçük bir delik vardı. Yağmur suyu oradan maskenin üstüne damlıyordu. Ses bu damlalardan geliyordu! Şakir maskesini alıp kuru bir köşeye koydu. Sonra deliğin altına boş bir kap bıraktı. Şakir bundan sonra bir ses duyunca önce yukarıya da baktı.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "şapkasına bir damla düştü ve yukarıdaki deliği gördü"
   - Cümle 0 (plan satırı): «çadırın içinden bir tık tık sesi geldi | şapkasına bir damla düştü ve yukarıdaki deliği gördü»
   - Açıklama: Plan çözümü yalnız deliğin fark edilmesini söylüyor; gövdedeki asıl çözüm maskeyi kuru köşeye koyup deliğin altına kap bırakmak.
   - Açıklama: Plan çözüm olarak rastlantısal keşfi söylüyor; gövdedeki çözüm maskeyi kuru köşeye koyup deliğin altına kap bırakmak.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "önce yukarıya da baktı"
   - Cümle 13: «Şakir bundan sonra bir ses duyunca önce yukarıya da baktı.»
   - Açıklama: 'Önce' ile 'da' birlikte cümleyi bozuyor; 'önce yukarıya baktı' olmalı.
   - Açıklama: 'Önce' ile 'da' birlikte kullanılınca cümle bozuk duruyor; 'önce yukarıya baktı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0203` birebir aynı, ardından `@onarim: 72e1aa79ef18ade531b707a900e511b416b098e3`, sonra gövde.

### Hikâye 2: tohum sakir-0205 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0205
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'pelerin', fiil 'kurmak', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: saray oyunu için bir taç yoktu | benekli yaprakları şapkasına dizip taç yaptı
@tohum: sakir-0205
Şakir kamp yerinde saray oyunu oynamak istedi. Kırmızı pelerinini taktı ve taşlardan küçük bir taht kurdu. Ama oyun için bir taç gerekiyordu ve Şakir'in tacı yoktu. Şakir etrafa baktı. Yerde sarı, benekli yapraklar vardı. Şakir bu yaprakları topladı. Sonra onları şapkasının kenarına tek tek sıkıştırdı. Yaprakların sivri uçları yukarı doğru duruyordu. Artık başında sarı bir taç vardı! Şakir tahtına oturdu, pelerinini düzeltti ve başını dik tuttu. Şakir çok sevindi, çünkü kendi tacını kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Kırmızı pelerinini taktı"
   - Cümle 2: «Kırmızı pelerinini taktı ve taşlardan küçük bir taht kurdu.»
   - Açıklama: Kartta Şakir'e ait bir pelerin yok; kapalı dünyaya kartta olmayan kişisel bir eşya ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0205` birebir aynı, ardından `@onarim: 57b8b448130841bd8657e30addbe603829e70e4e`, sonra gövde.

### Hikâye 3: tohum sakir-0206 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0206
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'limon', fiil 'uzamak', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: kaygan limon her seferinde elinden kayıp düştü | şapkasını ters çevirdi ve limonu içine aldı
@tohum: sakir-0206
Parkta Şakir ile annesi limon atma oyunu oynuyordu. Topları yoktu, bu yüzden Kadriye çantasından bir limon çıkarmıştı. Kadriye limonu atıyor, Şakir tutuyordu. Ama limon çok kaygandı ve Şakir'in elinden hep kayıp düşüyordu. Limon çimenlerin üstünde uzağa yuvarlandı. Şakir her seferinde limonun peşinden koştu. Sonra şapkasını çıkardı ve ters çevirip önünde tuttu. Kadriye limonu yine attı. Limon bu kez tam içine düştü ve hiç kaymadı. Kadriye çok memnun oldu ve alkışladı. Oyun uzadıkça ikisi de daha çok güldü. Şakir bundan sonra kaygan bir şeyi tutarken bir kap kullandı.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bu yüzden Kadriye çantasından"
   - Cümle 2: «Topları yoktu, bu yüzden Kadriye çantasından bir limon çıkarmıştı.»
   - Açıklama: Kadriye'nin Şakir'in annesi olduğu söylenmeden adla tanıtılıyor; kimi gösterdiği belli değil.
   - Açıklama: Kadriye'nin 'annesi' olduğu söylenmeden adıyla anılıyor; kimi gösterdiği belli değil.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kadriye limonu atıyor, Şakir tutuyordu.»
   - Açıklama: Limonun kayıp düşmesi sorunu ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Ama limon çok kaygandı ve Şakir'in elinden hep kayıp düşüyordu.»
   - Açıklama: Limonun kayıp düşmesi sorunu ancak 4. cümlede söyleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama limon çok kaygandı"
   - Cümle 4: «Ama limon çok kaygandı ve Şakir'in elinden hep kayıp düşüyordu.»
   - Açıklama: Oyunda limon atmak ve limonun kaygan olması akla yatkın bir sorun sebebi değil.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kadriye çok memnun oldu"
   - Cümle 10: «Kadriye çok memnun oldu ve alkışladı.»
   - Açıklama: 'Memnun' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Memnun olmak' 3 yaşındaki çocuk için soyut; 'sevindi' daha uygun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0206` birebir aynı, ardından `@onarim: 13e8f702b6003838288336cb1c0427b23d2d793a`, sonra gövde.

### Hikâye 4: tohum sakir-0209 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0209
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ayakkabı', fiil 'uçuşmak', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: narin baloncuklar rüzgarda hemen patladı | şapkasını rüzgara karşı tuttu ve arkasında üfledi
@tohum: sakir-0209
@degisim: ayakkabı -> baloncuk
Rüzgar esiyordu. Şakir kumsalda ilk kez baloncuk yapmayı denedi. Elinde bir şişe sabunlu su ve küçük bir çubuk vardı. Ama narin baloncuklar rüzgarda hemen patladı. Şakir tekrar üfledi ama yine büyük bir baloncuk olmadı. Sonra biraz düşündü. Şakir şapkasını çıkardı ve rüzgarın geldiği yöne doğru tuttu. Onun arkasında hava sakindi. Şakir çubuğa yavaşça üfledi. Büyük ve parlak bir baloncuk oldu. Arkasından küçük baloncuklar da havada uçuştu. Hepsi güneşte çok güzel görünüyordu. Şakir çok sevindi, çünkü baloncuk yapmayı sonunda başarmıştı.
```

**Hakem bulguları (7):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "tuttu ve arkasında üfledi"
   - Cümle 0 (plan satırı): «narin baloncuklar rüzgarda hemen patladı | şapkasını rüzgara karşı tuttu ve arkasında üfledi»
   - Açıklama: Plan satırında kimin ya da neyin arkasında üflendiği belli değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama narin baloncuklar rüzgarda"
   - Cümle 4: «Ama narin baloncuklar rüzgarda hemen patladı.»
   - Açıklama: 'Narin' 3 yaşındaki çocuğun bilmediği bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "narin baloncuklar rüzgarda hemen"
   - Cümle 4: «Ama narin baloncuklar rüzgarda hemen patladı.»
   - Açıklama: Plan satırında da 'narin' kelimesi var.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama narin baloncuklar"
   - Cümle 4: «Ama narin baloncuklar rüzgarda hemen patladı.»
   - Açıklama: 'Narin' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
5. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama narin baloncuklar rüzgarda hemen patladı"
   - Cümle 4: «Ama narin baloncuklar rüzgarda hemen patladı.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor, ilk 3 cümlede yok.
6. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "narin baloncuklar rüzgarda hemen patladı"
   - Cümle 4: «Ama narin baloncuklar rüzgarda hemen patladı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
7. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun arkasında hava sakindi"
   - Cümle 8: «Onun arkasında hava sakindi.»
   - Açıklama: 'Onun' şapkayı mı Şakir'i mi gösteriyor belli değil.
   - Açıklama: 'Onun' zamirinin şapkayı mı Şakir'i mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0209` birebir aynı, `@degisim: ayakkabı -> baloncuk` (tutuyorsan), ardından `@onarim: cdba5dfdb14dbd23eda9bb4823a6ff928a7e1d48`, sonra gövde.

### Hikâye 5: tohum sakir-0210 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0210
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'süt', fiil 'silmek', sıfat 'çıtır'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: tek bir dal vardı ve ikisi de çizmek istedi | şapkayı babasına verip sırayı gösterdi
@tohum: sakir-0210
Şakir babasıyla kumsalda resim oyunu oynuyordu. Oyunda kuma resim çizip ne olduğunu buluyorlardı. Ama yalnız bir dal vardı ve ikisi de önce çizmek istedi. Şakir biraz düşündü ve şapkasını babasının başına koydu. "Baba, şapka kimdeyse o çizer!" dedi Şakir. Remzi kuma büyük bir şişe çizdi. "Süt!" dedi Şakir hemen. Remzi güldü ve resmi eliyle sildi. Sonra dalı ve şapkayı Şakir'e verdi. Şakir kuma yuvarlak bir simit çizdi. "Çıtır simit!" dedi Remzi. Şakir ile babası sırayla oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Remzi kuma büyük bir"
   - Cümle 6: «Remzi kuma büyük bir şişe çizdi.»
   - Açıklama: Baba hiç adıyla tanıtılmadan birden 'Remzi' diye anılıyor; kimin kastedildiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Remzi kuma büyük bir şişe çizdi"
   - Cümle 6: «Remzi kuma büyük bir şişe çizdi.»
   - Açıklama: Remzi adı babanın adı olduğu söylenmeden birden geçiyor; kimi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0210` birebir aynı, ardından `@onarim: 1b2a7241909afa3cabdfdd81842fe551dc3cb975`, sonra gövde.

### Hikâye 6: tohum sakir-0212 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0212
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'halat', fiil 'doğmak', sıfat 'sağlıklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: iki kardeş atlamak istedi ama tek halat vardı | halatı dala bağladı ve şapkayı takan atladı
@tohum: sakir-0212
@degisim: sağlıklı -> uzun
Şakir kamp yerinde uzun bir halatı çevirip üstünden atlıyordu. Güneş yeni doğmuştu ve hava serindi. Canan da atlamak istedi, ama orada tek bir halat vardı. "Ben de atlayabilir miyim, Şakir?" diye sordu Canan. Şakir durdu ve biraz düşündü. Sonra halatı yere yakın bir dala bağladı. Şapkasını çıkardı ve Canan'ın başına koydu. "Şapka kimde olursa o atlayacak," dedi Şakir. Canan on kez atladı ve şapkayı Şakir'e geri verdi. Bu kez Canan halatı çevirdi ve Şakir atladı. Şakir ile Canan sırayla atlayıp mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "iki kardeş atlamak istedi"
   - Cümle 0 (plan satırı): «iki kardeş atlamak istedi ama tek halat vardı | halatı dala bağladı ve şapkayı takan atladı»
   - Açıklama: Gövdede Şakir ile Canan'ın kardeş olduğu hiç söylenmiyor; plan gövdeye uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "halatı yere yakın bir dala bağladı"
   - Cümle 6: «Sonra halatı yere yakın bir dala bağladı.»
   - Açıklama: Şakir halatı tek başına çevirip atlayabildiği için halatı dala bağlamanın işlevi belirsiz; sıra sorununu çözen şey yalnız şapka kuralı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0212` birebir aynı, `@degisim: sağlıklı -> uzun` (tutuyorsan), ardından `@onarim: faab8c5c214f8a0c4b80186f5e497e4898e400d0`, sonra gövde.

### Hikâye 7: tohum sakir-0215 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0215
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: yeni bir şeyi denemek
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'çan', fiil 'esmek', sıfat 'çiçekli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: rüzgar durdu ve çan hiç çalmadı | şapkasını salladı, rüzgar yaptı ve çanı çaldı
@tohum: sakir-0215
Ormandaki kamp yerinde hafif bir rüzgar esiyordu. Şakir annesinin verdiği çiçekli çanı ilk kez deneyecekti. Çanı bir dala astı, ama rüzgar durdu ve çan çalmadı. "Anne, çan neden çalmıyor?" diye sordu Şakir. "Çan rüzgar esince çalar," dedi Kadriye. Şakir hemen şapkasını çıkardı. Şapkayı çanın önünde hızlı hızlı salladı. Çan hafifçe kıpırdadı ve çın çın çaldı. Kadriye güldü ve ellerini çırptı. Şakir şapkasını yeniden başına taktı. "Teşekkürler, anne, çan çok güzel çalıyor!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "esince çalar," dedi Kadriye"
   - Cümle 5: «"Çan rüzgar esince çalar," dedi Kadriye.»
   - Açıklama: Kadriye'nin anne olduğu hiç söylenmiyor; konuşan kişi belli değil.
   - Açıklama: Kadriye'nin Şakir'in annesi olduğu söylenmeden konuşturuluyor, konuşanın kim olduğu çocuğa belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0215` birebir aynı, ardından `@onarim: 0480587b809c1ab5c820cac0938eee87c94eb2ed`, sonra gövde.

### Hikâye 8: tohum sakir-0217 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0217
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'mektup', fiil 'paketlemek', sıfat 'güçlü'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: rüzgar hediyenin paket kağıdını uçurdu | hediyeyi şapkasının içine koyup yaprakla kapattı
@tohum: sakir-0217
Ormandaki kamp yerinde Şakir, Canan için parlak bir taş paketliyordu. Taşın yanına küçük bir mektup da yazmıştı. Ama güçlü bir rüzgar esti ve paket kağıdını uçurdu. Kağıt ağaçların arasında kayboldu. Şakir başındaki şapkasına baktı ve biraz düşündü. Şapkasını çıkardı ve ters çevirdi. Taşı ve mektubu şapkanın içine koydu. Sonra şapkanın üstünü büyük bir yaprakla kapattı. Canan gelince Şakir şapkayı ona uzattı. "Bu senin için, Canan," dedi Şakir. Canan yaprağı kaldırdı ve mektubu okudu. "Ne güzel bir taş, teşekkürler!" dedi Canan. Şakir çok mutlu oldu, çünkü hediyesi kardeşini sevindirmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Taşın yanına küçük bir mektup da yazmıştı"
   - Cümle 2: «Taşın yanına küçük bir mektup da yazmıştı.»
   - Açıklama: Mektup taşın yanına yazılmaz; 'yazıp koymuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0217` birebir aynı, ardından `@onarim: ef74fe56f39a2dcc13ecf343e8f74600a6ea9e78`, sonra gövde.

### Hikâye 9: tohum sakir-0223 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0223
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'vanilya', fiil 'sergilemek', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: kütük yamuk olduğu için kozalaklar yere yuvarlandı | şapkasını ters koyup kozalakları içine dizdi
@tohum: sakir-0223
@degisim: saygılı -> büyük
Ormandaki kamp yerinde Şakir pasta dükkanı oyunu oynuyordu. Kozalakları pasta gibi bir kütüğün üstünde sergiliyordu. Ama kütük yamuktu ve kozalaklar birer birer yere yuvarlandı. Şakir güldü ve onları tek tek topladı. Sonra şapkasını çıkardı ve kütüğün üstüne ters koydu. Kozalakları şapkanın içine dikkatle dizdi. Bu kez hiçbir kozalak yere düşmedi. Şakir en büyük kozalağa vanilya pastası adını verdi. Onu şapkanın tam ortasına koydu. Pastalar şapkanın içinde çok güzel görünüyordu. Şakir pasta dükkanı oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "pasta gibi bir kütüğün üstünde"
   - Cümle 2: «Kozalakları pasta gibi bir kütüğün üstünde sergiliyordu.»
   - Açıklama: 'Pasta gibi' benzetmesi yanlış yerde; kozalakları değil kütüğü nitelemiş gibi okunuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kütüğün üstünde sergiliyordu"
   - Cümle 2: «Kozalakları pasta gibi bir kütüğün üstünde sergiliyordu.»
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuğun bilmediği bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kütüğün üstünde sergiliyordu"
   - Cümle 2: «Kozalakları pasta gibi bir kütüğün üstünde sergiliyordu.»
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0223` birebir aynı, `@degisim: saygılı -> büyük` (tutuyorsan), ardından `@onarim: fec5ba14afe17e73b69ac723f4bf5d86ab55d3e7`, sonra gövde.

### Hikâye 10: tohum sakir-0228 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0228
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yaprak', fiil 'içmek', sıfat 'aydınlık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: annesi mutfağa geliyordu ve sürprizi görecekti | şapkasını tepsiye kapatıp sürprizi sakladı
@tohum: sakir-0228
Dışarıda yağmur yağıyordu. Şakir aydınlık mutfakta annesi için tepsiye süt ve yaprak şeklinde kurabiye koymuştu. Ama Kadriye o sırada içeri geliyordu ve sürprizi görecekti. Şakir hemen şapkasını çıkardı. Şapkayı bardağın ve kurabiyenin üstüne kapattı. Kadriye mutfağa girdi ve şapkayı gördü. "Şapkan neden orada, Şakir?" diye sordu Kadriye. "Önce gözlerini kapat, anne," dedi Şakir. Kadriye gülümsedi ve gözlerini kapattı. "Şimdi aç, anneciğim!" dedi Şakir ve şapkayı kaldırdı. Kadriye sevinçle sütünü içti ve kurabiyeyi yedi. Şakir çok mutlu oldu, çünkü annesi sürprizini sevmişti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ama Kadriye o sırada içeri geliyordu"
   - Cümle 3: «Ama Kadriye o sırada içeri geliyordu ve sürprizi görecekti.»
   - Açıklama: Önce 'annesi' denip sonra bağlantı kurulmadan 'Kadriye' adı geçiyor; Kadriye'nin kim olduğu belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Ama Kadriye o sırada"
   - Cümle 3: «Ama Kadriye o sırada içeri geliyordu ve sürprizi görecekti.»
   - Açıklama: Kadriye adı annesi ile bağlanmadan geliyor; kimin kastedildiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0228` birebir aynı, ardından `@onarim: e45ed60f8e4b997ccad8165bc7fc656d44754b71`, sonra gövde.

### Hikâye 11: tohum sakir-0229 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0229
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kese', fiil 'belirmek', sıfat 'mükemmel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: rüzgar numara örtüsünü uçurdu | keseyi şapkasının altına koyup yeniden gösterdi
@tohum: sakir-0229
Ormanda serin bir rüzgar esiyordu. Şakir, Necati'ye bir kese numarası yapacaktı. Ama rüzgar numara örtüsünü uçurdu ve ağaçların arasına götürdü. "Örtü olmadan numara nasıl olacak?" diye sordu Necati. Şakir hemen şapkasını çıkardı. Küçük keseyi yere koydu ve üstüne şapkayı kapattı. "Kese yok oldu!" dedi Şakir. Necati hortumunu kaldırdı ve şaşırmış gibi yaptı. "Kese nereye gitti?" diye sordu Necati. Şakir şapkayı yavaşça kaldırdı ve kese yeniden belirdi. Şakir şapkasını başına taktı ve eğilerek selam verdi. "Mükemmel bir numara, Şakir!" dedi Necati.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "üstüne şapkayı kapattı"
   - Cümle 6: «Küçük keseyi yere koydu ve üstüne şapkayı kapattı.»
   - Açıklama: Şapka kapatılmaz; 'üstünü şapkayla kapattı' ya da 'üstüne şapkayı koydu' olmalı.
   - Açıklama: Şapka kapatılmaz, üstüne örtülür ya da konur.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0229` birebir aynı, ardından `@onarim: 8ecf93ca3ef3b8f770d782bb0fb958374a7c56a6`, sonra gövde.

### Hikâye 12: tohum sakir-0233 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0233
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kabak', fiil 'inmek', sıfat 'değerli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: çorba için boş tencere yoktu | şapkasını tencere gibi kullanıp oyun çorbası yaptı
@tohum: sakir-0233
@degisim: değerli -> küçük
Ormandaki kamp yerinde Şakir yemek oyunu oynuyordu. Annesine küçük bir kabakla oyun çorbası yapacaktı. Ama tencerede annesinin gerçek çorbası vardı. Şakir oturduğu kütükten indi ve biraz düşündü. Sonra şapkasını çıkarıp ters çevirdi. "Anne, şapkam tencere olsun!" dedi Şakir. Kabağı ve birkaç yaprağı şapkanın içine koydu. Bir dalla hepsini yavaşça karıştırdı. "Kabak çorbası hazır, anneciğim!" dedi Şakir. Kadriye çorbayı içer gibi yaptı ve güldü. "Çok güzel olmuş, Şakir," dedi Kadriye. Şakir ile annesi yemek oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kadriye çorbayı içer gibi"
   - Cümle 10: «Kadriye çorbayı içer gibi yaptı ve güldü.»
   - Açıklama: Anne 'annesi' diye anılıp birden Kadriye adıyla geçiyor; Kadriye'nin kim olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0233` birebir aynı, `@degisim: değerli -> küçük` (tutuyorsan), ardından `@onarim: ecbd4d39f629017fd3eb5560a79e9b0da8b54770`, sonra gövde.
