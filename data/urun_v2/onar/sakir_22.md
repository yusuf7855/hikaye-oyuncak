# Editör görevi (onarım): Şakir, onarım partisi 22

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar22.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar22.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0060 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0060
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'altın', fiil 'birleşmek', sıfat 'turuncu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: tek bir turuncu kova vardı ve ikisi de istedi | kovayı sırayla kullanmayı önerdi
@tohum: sakir-0060
Şakir kumsalda Necati ile oyun oynuyordu. Oyuncak altın için kumdan büyük bir kale yapacaklardı. Ama tek bir turuncu kova vardı ve ikisi de onu istedi. "Necati, kovayı sırayla dolduralım mı?" diye sordu Şakir. "Olur, önce sen başla," dedi Necati. Şakir kovayı kumla doldurdu ve sol yanda bir kule yaptı. Sonra Necati kovayı aldı ve sağ yana ikinci bir kule dikti. Şakir macerayı çok severdi, beklerken kalenin altına bir tünel kazdı. Kuleler büyüdükçe duvarları ortada birleşti. Şakir oyuncak altını bu tünelden kalenin ortasına götürdü. "Ne güzel bir kale oldu, Şakir!" dedi Necati. Şakir çok sevindi, çünkü birlikte kocaman bir kale yapmışlardı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şakir macerayı çok severdi, beklerken"
   - Cümle 8: «Şakir macerayı çok severdi, beklerken kalenin altına bir tünel kazdı.»
   - Açıklama: İki bağımsız cümle virgülle bağlanmış ve anlam bağı kurulmamış; cümle dilbilgisel olarak kopuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 8: «Şakir macerayı çok severdi, beklerken kalenin altına bir tünel kazdı.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "beklerken kalenin altına bir tünel kazdı"
   - Cümle 8: «Şakir macerayı çok severdi, beklerken kalenin altına bir tünel kazdı.»
   - Açıklama: Tünel sorunla ilgisiz, özellik satırı için sonradan eklenmiş bir yan olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0060` birebir aynı, ardından `@onarim: d3abd7fa8cf820157798ba79aef1b1c680366444`, sonra gövde.

### Hikâye 2: tohum sakir-0064 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0064
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'etek', fiil 'yoğurmak', sıfat 'dar'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: bardak çok dar olduğu için kumdan pasta çıkmadı | şapkasını kalıp olarak kullandı ve büyük bir pasta yaptı
@tohum: sakir-0064
@degisim: etek -> bardak
Kumsalda dalgaların sesi duyuluyordu. Şakir ile Necati ıslak kumu yoğurdu ve pasta yapmaya başladı. Ama Şakir'in bardağı çok dardı ve pasta bardaktan çıkmadı. Şakir bardağı salladı, ama kum içeride kaldı. "Pasta bardağa yapıştı!" dedi Necati ve ikisi birlikte güldü. Şakir geniş şapkasına baktı. Şapkayı çıkardı ve içini kumla doldurdu. Sonra şapkayı kumun üstüne ters çevirdi ve yavaşça kaldırdı. Kumda kocaman, yuvarlak bir pasta duruyordu. "Ne büyük bir pasta bu, Şakir!" dedi Necati. Necati hortumuyla pastanın üstüne küçük bir kabuk koydu. Şakir bundan sonra pastaları şapkasıyla yaptı ve Necati ile çok eğlendi.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Şakir bundan sonra pastaları şapkasıyla yaptı"
   - Cümle 12: «Şakir bundan sonra pastaları şapkasıyla yaptı ve Necati ile çok eğlendi.»
   - Açıklama: Son cümle ders cümlesi değil ama 'bundan sonra' ile olayın ötesine zaman atlıyor.
   - Açıklama: Son cümle ders cümlesi değil, olayın ötesine zaman atlayan bir anlatı cümlesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0064` birebir aynı, `@degisim: etek -> bardak` (tutuyorsan), ardından `@onarim: cc4c30d4efa39914889e95b57342d0e2c52c549e`, sonra gövde.

### Hikâye 3: tohum sakir-0066 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0066
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kanepe', fiil 'konuşmak', sıfat 'akıllı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: gemi oyununda geminin bayrağı yoktu | şapkasını bir dalın ucuna takıp bayrak yaptı
@tohum: sakir-0066
Bir sabah Şakir ile annesi Kadriye kamp yerindeydi. Şakir yerdeki kalın bir kütüğü gemi yaptı ve gemi oyunu kurdu. Ama gemisinin bayrağı yoktu ve ağaçların arasında hiç bayrak bulamadı. Şakir biraz düşündü ve başındaki şapkaya dokundu. Sonra yerden uzun bir dal aldı. Şapkasını dalın ucuna taktı ve dalı kütüğün yanında toprağa dikti. Şapka rüzgarda bayrak gibi sallandı. Kadriye de gelip gemiye bindi. "Bu gemi evdeki kanepe kadar rahat," dedi Kadriye. Şakir ile annesi gemide uzun uzun konuştu. "Sen çok akıllısın, Şakir," dedi Kadriye. Şakir çok sevindi, çünkü gemisinin artık güzel bir bayrağı vardı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu gemi evdeki kanepe kadar rahat"
   - Cümle 9: «"Bu gemi evdeki kanepe kadar rahat," dedi Kadriye.»
   - Açıklama: Kanepe repliği ve uzun konuşma sorunla bağsız, işlevsiz ayrıntılar.
   - Açıklama: Kanepe benzetmesi ve uzun sohbet sorunla ilgisiz, işlevsiz ayrıntılar.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir ile annesi gemide uzun uzun konuştu"
   - Cümle 10: «Şakir ile annesi gemide uzun uzun konuştu.»
   - Açıklama: Uzun sohbet olaydan çıkmıyor ve hikayeye hiçbir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0066` birebir aynı, ardından `@onarim: 685b9aa5bd297208a31bd9752c55184a39597f93`, sonra gövde.

### Hikâye 4: tohum sakir-0069 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0069
- yer: park (Şehirdeki park.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'meşe', fiil 'sallamak', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | -
@plan: parkta çok ağaç vardı ve kağıttaki ağacı bulamadı | yapraklara bakıp kağıttaki meşe ağacını buldu
@tohum: sakir-0069
Bir sabah Şakir parkta harita oyunu oynuyordu. Elinde işaretli bir kağıt vardı. Kağıda büyük yapraklı bir meşe ağacı çizmişti. Ama parkta çok ağaç vardı ve Şakir o ağacı hemen bulamadı. Şakir macerayı çok severdi, bu yüzden hemen aramaya başladı. Ağaçların yapraklarına tek tek baktı. Sonunda resimdeki yapraklara benzeyen bir ağaç gördü. Alçak bir dalı hafifçe salladı ve birkaç yaprak eline düştü. Yapraklar kağıttaki resmin aynısıydı ve bu ağaç bir meşe ağacıydı. Şakir yaprakları kağıdın yanına koydu ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama parkta çok ağaç vardı"
   - Cümle 4: «Ama parkta çok ağaç vardı ve Şakir o ağacı hemen bulamadı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0069` birebir aynı, ardından `@onarim: 68cb13f3843989f5f9d60c281def00e5cc388ca5`, sonra gövde.

### Hikâye 5: tohum sakir-0070 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0070
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'ruj', fiil 'dokunmak', sıfat 'şirin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: şirin bir kabuk ağır bir kütüğün altında kaldı | yardım istedi ve fil kütüğü kenara itti
@tohum: sakir-0070
@degisim: ruj -> kütük
Denizden serin bir rüzgar esiyordu. Şakir macerayı çok severdi ve Necati ile kumsalın her yerine bakıyordu. Birden şirin, pembe bir kabuk gördü ama kabuk ağır bir kütüğün altındaydı. Şakir kütüğü iki eliyle çekti ama kütük hiç kıpırdamadı. "Necati, bana yardım eder misin?" diye sordu Şakir. Necati hortumuyla kütüğü kolayca kenara itti. Şakir kabuğu aldı ve ona parmağıyla yavaşça dokundu. Kabuğun içi çok parlaktı. "Çok güzel bir kabuk buldun, Şakir," dedi Necati. "Teşekkürler, Necati, bu kabuğu hep saklayacağım!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 2: «Şakir macerayı çok severdi ve Necati ile kumsalın her yerine bakıyordu.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0070` birebir aynı, `@degisim: ruj -> kütük` (tutuyorsan), ardından `@onarim: 4eb18fceddbb078dd6c4346d6c45ce85469d711d`, sonra gövde.

### Hikâye 6: tohum sakir-0071 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0071
- yer: park (Şehirdeki park.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ceket', fiil 'bindirmek', sıfat 'soslu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: kumdan pasta yapmak için kalıbı yoktu | şapkasını kalıp yapıp kumdan pasta yaptı
@tohum: sakir-0071
@degisim: bindirmek -> dökmek
Şakir parkta kum havuzunda yemek oyunu oynuyordu. Ceketini önlük gibi beline bağladı. Kum sabah yağan yağmurdan ıslaktı. Şakir büyük bir pasta yapmak istedi ama kalıbı yoktu. Kum elinde dağılıyor ve hiç yuvarlak olmuyordu. Şakir biraz düşündü ve şapkasını çıkardı. Şapkayı ıslak kumla doldurdu ve sıkıca bastırdı. Sonra şapkayı ters çevirdi ve yavaşça kaldırdı. Kumda yuvarlak bir pasta duruyordu. Şakir onun üstüne sos gibi ince kum döktü. Böylece güzel, soslu bir kum pastası oldu. Şakir bundan sonra kalıp bulamayınca yanındaki eşyalara baktı.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "şapkasını kalıp yapıp kumdan pasta yaptı"
   - Cümle 0 (plan satırı): «kumdan pasta yapmak için kalıbı yoktu | şapkasını kalıp yapıp kumdan pasta yaptı»
   - Açıklama: Plan satırında 'yapıp' ve 'yaptı' gereksiz yere tekrarlanıyor; 'şapkasını kalıp olarak kullanıp' olmalı.
   - Açıklama: 'yapıp ... yaptı' gereksiz tekrar.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ceketini önlük gibi beline bağladı"
   - Cümle 2: «Ceketini önlük gibi beline bağladı.»
   - Açıklama: Ceketi önlük gibi bağlama ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.
   - Açıklama: Önlük gibi bağlanan ceket bir daha geçmiyor ve olayda hiçbir işe yaramıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şakir bundan sonra kalıp bulamayınca yanındaki eşyalara baktı"
   - Cümle 12: «Şakir bundan sonra kalıp bulamayınca yanındaki eşyalara baktı.»
   - Açıklama: 'bundan sonra' alışkanlık anlatır; fiil 'bakardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0071` birebir aynı, `@degisim: bindirmek -> dökmek` (tutuyorsan), ardından `@onarim: aa9b5b7c46e19f7b3c2f873614c1b3b7cdedace9`, sonra gövde.

### Hikâye 7: tohum sakir-0072 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0072
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: kaybolan eşya
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'bulmaca', fiil 'eğilmek', sıfat 'kremalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: rüzgar bulmaca kağıdını ağaçların arasına uçurdu | çalının altına eğilip kağıdı buldu
@tohum: sakir-0072
Şakir babası Remzi ile kamp yerinde bulmaca yapıyordu. Yanlarında bir paket kremalı bisküvi vardı. Birden rüzgar esti ve bulmaca kağıdı ağaçların arasına uçtu. "Baba, kağıdı ben bulurum!" dedi Şakir. Şakir macerayı çok severdi, bu yüzden aramaya hemen başladı. Yakındaki ağaçlara tek tek baktı. Sonra bir çalının yanında durdu. Eğildi ve çalının altına baktı. Beyaz kağıt oradaydı. Şakir kağıdı aldı ve babasına koştu. "Aferin, Şakir!" dedi Remzi ve ona kremalı bir bisküvi verdi. Şakir çok sevindi, çünkü kayıp kağıdı kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve bulmaca kağıdı ağaçların arasına uçtu"
   - Cümle 3: «Birden rüzgar esti ve bulmaca kağıdı ağaçların arasına uçtu.»
   - Açıklama: Rüzgarın kağıdı uçurması ve kağıdın hemen bulunması örnekteki 'dağıttı, topladı, bitti' türü önemsiz bir sorun.
   - Açıklama: Rüzgar kağıdı uçuruyor, Şakir bakıp buluyor; sorun 'uçtu, aradı, buldu, bitti' türünden önemsiz bir olay.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi, bu yüzden aramaya hemen başladı.»
   - Açıklama: 'Macera' 3 yaşındaki çocuk için soyut bir kavramdır.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0072` birebir aynı, ardından `@onarim: 9c24e4396208cc4d8e03544dac5c7da470b352d4`, sonra gövde.

### Hikâye 8: tohum sakir-0073 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0073
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'başörtüsü', fiil 'buluşmak', sıfat 'güneşli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: sarı kelebekler ağaçların arkasında kayboldu | onların gittiği yere yürüyüp çiçeklerin üstünde buldu
@tohum: sakir-0073
@degisim: başörtüsü -> çiçek
Güneşli bir sabah Şakir parkta yürüyordu. Birden önünden sarı kelebekler uçtu ve ağaçların arkasında kayboldu. Şakir kelebeklerin nereye gittiğini çok merak etti. Macerayı çok seven Şakir onların uçtuğu yönde yürüdü. Yol ağaçların arasından geçiyordu. Şakir iki yolun buluştuğu yere geldi ve durdu. Orada kırmızı çiçeklerle dolu küçük bir bahçe vardı. Sarı kelebekler çiçeklerin üstüne konmuştu. Şakir onları uzaktan sessizce seyretti. Kelebekleri bulduğu için çok mutluydu. Şakir bundan sonra kelebekleri görünce en yakın çiçeklere baktı.
```

**Hakem bulguları (7):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "önünden sarı kelebekler uçtu"
   - Cümle 2: «Birden önünden sarı kelebekler uçtu ve ağaçların arkasında kayboldu.»
   - Açıklama: Notlanan çoğul canlı kelebekler arka planda kalmıyor, olayın sorununa katılıyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Birden önünden sarı kelebekler uçtu ve ağaçların arkasında kayboldu"
   - Cümle 2: «Birden önünden sarı kelebekler uçtu ve ağaçların arkasında kayboldu.»
   - Açıklama: Arka planda kalması gereken çoğul canlı kelebekler sorunun ve olayın merkezine katılıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sarı kelebekler uçtu ve ağaçların arkasında kayboldu"
   - Cümle 2: «Birden önünden sarı kelebekler uçtu ve ağaçların arkasında kayboldu.»
   - Açıklama: Kelebeklerin gözden kaybolması gerçek bir sorun değil, yalnız merak.
   - Açıklama: Kelebeklerin uçup gitmesi gerçek bir sorun değil, çocuğun önemseyeceği bir kayıp ya da engel yok.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Macerayı çok seven Şakir onların uçtuğu yönde yürüdü"
   - Cümle 4: «Macerayı çok seven Şakir onların uçtuğu yönde yürüdü.»
   - Açıklama: Güvenli kullanım satırına göre Şakir tek başına uzağa gitmez, burada yalnız başına kelebekleri izleyip uzaklaşıyor.
   - Açıklama: Şakir tek başına kelebekleri izleyerek ağaçların arasına gidiyor; güvenli kullanım satırı tek başına uzağa gitmemesini söylüyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 4: «Macerayı çok seven Şakir onların uçtuğu yönde yürüdü.»
   - Açıklama: 'Macera' soyut bir kavram.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bilmeyebilir.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "iki yolun buluştuğu yere geldi ve durdu"
   - Cümle 6: «Şakir iki yolun buluştuğu yere geldi ve durdu.»
   - Açıklama: İki yolun buluştuğu yer bir seçim gibi kuruluyor ama hiçbir işe yaramıyor.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şakir bundan sonra kelebekleri görünce en yakın çiçeklere baktı"
   - Cümle 11: «Şakir bundan sonra kelebekleri görünce en yakın çiçeklere baktı.»
   - Açıklama: Sürekli alışkanlık anlatılırken '-dı' kullanılmış; 'bakardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0073` birebir aynı, `@degisim: başörtüsü -> çiçek` (tutuyorsan), ardından `@onarim: 6e16eee167f50a26dbeede9736605e8aa99a96f1`, sonra gövde.

### Hikâye 9: tohum sakir-0074 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0074
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'damga', fiil 'çekilmek', sıfat 'kahverengi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kuru kumda çizgiler hemen dağılıyordu | ıslak kuma şapkasını bastırıp çiçek yaptı
@tohum: sakir-0074
Kumsalda deniz yavaşça geri çekiliyordu. Şakir, kitap okuyan kardeşi Canan için kuma çiçek yapmak istedi. Ama kuru kum çok yumuşaktı ve çizgiler hemen dağılıyordu. Şakir suyun çekildiği yere baktı. Orada kum koyu kahverengiydi. Şakir oraya gitti ve eliyle dokundu. Burası ıslak ve sıkıydı. Hemen şapkasını çıkardı ve yere bastırdı. Yerde yuvarlak bir damga kaldı. Şakir ilk damganın etrafına beş damga daha yaptı. Böylece güzel bir çiçek oluştu. "Canan, bak, bu çiçek senin için!" dedi Şakir. "Çok güzel olmuş, Şakir, teşekkür ederim!" dedi Canan.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "gitti ve eliyle dokundu"
   - Cümle 6: «Şakir oraya gitti ve eliyle dokundu.»
   - Açıklama: 'Dokundu' fiilinin yönelme durumundaki nesnesi eksik; 'kuma dokundu' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yerde yuvarlak bir damga"
   - Cümle 9: «Yerde yuvarlak bir damga kaldı.»
   - Açıklama: 'Damga' kelimesini 3 yaşındaki bir çocuk bilmeyebilir; 'iz' daha uygun olur.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0074` birebir aynı, ardından `@onarim: f0da30cf6ddc2cef024ddab9584195305cd14fef`, sonra gövde.

### Hikâye 10: tohum sakir-0075 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0075
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'cüzdan', fiil 'köpürmek', sıfat 'yeni'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: fil çok hızlı üfledi ve köpükler uçtu | ona hafif üfle dedi ve kova köpükle doldu
@tohum: sakir-0075
@degisim: cüzdan -> kova
Ormanda kamp yerinde Şakir ile Fil Necati bir kova sabunlu suyla oynuyordu. Kovayı köpükle doldurmak Şakir için yeni bir maceraydı. Ama Necati hortumuyla suya çok hızlı üfledi ve köpükler havaya uçtu. Köpükler Necati'nin başına kondu ve kovada hiç köpük kalmadı. Şakir buna çok güldü. "Necati, bu kez hafifçe üfle," dedi Şakir. Necati hortumunu suya soktu ve öyle yaptı. Su yavaş yavaş köpürdü. Beyaz köpük kovanın ağzına kadar çıktı. "Bak, Şakir, kova doldu!" dedi Necati. İkisi köpüklerle oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "ona hafif üfle dedi"
   - Cümle 0 (plan satırı): «fil çok hızlı üfledi ve köpükler uçtu | ona hafif üfle dedi ve kova köpükle doldu»
   - Açıklama: Plandaki doğrudan söz tırnaksız ve noktalamasız yazılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir için yeni bir maceraydı"
   - Cümle 2: «Kovayı köpükle doldurmak Şakir için yeni bir maceraydı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
   - Açıklama: Köpük doldurmayı 'macera' diye anlatmak soyut ve mecazlı bir kullanım.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kovayı köpükle doldurmak Şakir için yeni bir maceraydı"
   - Cümle 2: «Kovayı köpükle doldurmak Şakir için yeni bir maceraydı.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0075` birebir aynı, `@degisim: cüzdan -> kova` (tutuyorsan), ardından `@onarim: ea63865ebdeaec556aee9c89f46014852053ac52`, sonra gövde.

### Hikâye 11: tohum sakir-0076 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0076
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tost', fiil 'koşuşturmak', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: kumda büyük ve garip pati izleri vardı | izlerin yanından yürüyüp şemsiyenin arkasında babasını buldu
@tohum: sakir-0076
Şakir kumsalda kumdan bir kale yapıyordu. Kaleyi bitirince başını kaldırdı ve kumda büyük pati izleri gördü. Şakir bu izleri kimin yaptığını çok merak etti. Macerayı çok severdi, bu yüzden izlerin yanından yürümeye başladı. İzler büyük bir şemsiyenin arkasına gidiyordu. Şakir yavaşça şemsiyenin arkasına baktı. Orada babası Remzi gülerek oturuyordu ve elinde iki tost vardı. "İzleri ben yaptım," dedi Remzi sevecen bir sesle. "Ne güzel bir oyun, baba!" dedi Şakir. Sonra ikisi tostlarını yedi ve kumda koşuşturdu. Şakir çok sevindi, çünkü izleri kimin yaptığını bulmuştu.
```

**Hakem bulguları (7):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "kumda büyük ve garip pati izleri"
   - Cümle 0 (plan satırı): «kumda büyük ve garip pati izleri vardı | izlerin yanından yürüyüp şemsiyenin arkasında babasını buldu»
   - Açıklama: Kimin olduğu bilinmeyen büyük ve garip pati izleri küçük çocuk için ürkütücü bir gizem kuruyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bu yüzden izlerin yanından yürümeye başladı"
   - Cümle 4: «Macerayı çok severdi, bu yüzden izlerin yanından yürümeye başladı.»
   - Açıklama: Çocuk tek başına bilinmeyen büyük bir hayvanın izlerini takip ediyor; bu, güvenli kullanım satırındaki tek başına uzağa gitmeme kuralına ve taklit güvenliğine aykırı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok severdi, bu yüzden"
   - Cümle 4: «Macerayı çok severdi, bu yüzden izlerin yanından yürümeye başladı.»
   - Açıklama: 'Macera' 3 yaşındaki çocuk için soyut bir kavramdır.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "elinde iki tost vardı"
   - Cümle 7: «Orada babası Remzi gülerek oturuyordu ve elinde iki tost vardı.»
   - Açıklama: Tostlar sebepsiz beliriyor ve olayın çözümünde hiçbir işe yaramıyor.
   - Açıklama: Tostlar sebepsiz beliriyor ve sorunla hiçbir bağı yok.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Remzi sevecen bir sesle"
   - Cümle 8: «"İzleri ben yaptım," dedi Remzi sevecen bir sesle.»
   - Açıklama: 'Sevecen' 3 yaşındaki çocuğun bilmediği bir kelimedir.
6. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: ""İzleri ben yaptım," dedi Remzi"
   - Cümle 8: «"İzleri ben yaptım," dedi Remzi sevecen bir sesle.»
   - Açıklama: Babanın büyük pati izlerini nasıl yaptığı hiç söylenmiyor, sorunun sebebi akla yatkın değil.
7. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "İzleri ben yaptım"
   - Cümle 8: «"İzleri ben yaptım," dedi Remzi sevecen bir sesle.»
   - Açıklama: Babanın kumda nasıl pati izi yaptığı hiç açıklanmıyor, bu yüzden sorunun sebebi akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0076` birebir aynı, ardından `@onarim: 95b759f53f79dbcc620fa279e5bcf1c4546f2828`, sonra gövde.

### Hikâye 12: tohum sakir-0077 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0077
- yer: park (Şehirdeki park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'taş', fiil 'getirmek', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: dikenli çalının altında parlak bir şey vardı | şapkasıyla onu dışarı çekti
@tohum: sakir-0077
Bir sabah Şakir parkta küçük taşlar topluyordu. Birden dikenli bir çalının altında parlak bir şey gördü. Şakir onun ne olduğunu çok merak etti ama çalı çok dikenliydi. Biraz düşündü ve başından şapkasını aldı. Şapkasıyla o şeyi yavaşça dışarı çekti. Bu, beyaz ve pürüzsüz bir taştı. Güneşte ışıl ışıl parlıyordu. Şakir sevinçli bir yüzle onu öteki taşlarının yanına getirdi. Yeni taş hepsinin en güzeli oldu. Şakir bundan sonra dikenli yerlere elini değil, şapkasını uzattı.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şapkasıyla o şeyi yavaşça dışarı çekti"
   - Cümle 5: «Şapkasıyla o şeyi yavaşça dışarı çekti.»
   - Açıklama: Çocuk dikenli çalının altındaki bilinmeyen parlak bir nesneyi alıp getirmeyi taklit edebilir (cam gibi tehlikeli olabilir).
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "beyaz ve pürüzsüz bir taştı"
   - Cümle 6: «Bu, beyaz ve pürüzsüz bir taştı.»
   - Açıklama: 'Pürüzsüz' kelimesi 3 yaşındaki bir çocuk için zor; 'düz' daha uygun.
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0077` birebir aynı, ardından `@onarim: 4b82ec455afaf2ae2974b6722ba3ee57eedae363`, sonra gövde.
