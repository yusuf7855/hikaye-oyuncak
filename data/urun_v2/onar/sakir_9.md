# Editör görevi (onarım): Şakir, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar9.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0001 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Remzi
@tohum: sakir-0001
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'bilye', fiil 'incelemek', sıfat 'kocaman'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | ev | Remzi
@plan: bilye dolabın altına girdi ve babasının kolu sığmadı | yere uzanıp küçük eliyle bilyeyi dışarı çekti
@tohum: sakir-0001
Şakir babası Remzi ile salonda bilye oynuyordu. Remzi'nin kocaman mavi bilyesi yuvarlandı ve dolabın altına girdi. Remzi eğildi ama kalın kolu oraya sığmadı. "Bilyemi alamıyorum, Şakir," dedi Remzi. "Ben alırım, baba, bu bir macera oyunu!" dedi Şakir. Hemen yere uzandı ve orayı dikkatle inceledi. Mavi bilye en arkada duruyordu. Şakir'in küçük eli içeri rahatça girdi. Bilyeyi parmaklarıyla tuttu ve yavaşça dışarı çekti. Sonra onu babasına verdi. Remzi sevinçle güldü ve Şakir'e sarıldı. "Teşekkürler, Şakir, şimdi oyunumuza devam edelim!" dedi Remzi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu bir macera oyunu"
   - Cümle 5: «"Ben alırım, baba, bu bir macera oyunu!" dedi Şakir.»
   - Açıklama: 'Macera' 3 yaşındaki çocuk için soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0001` birebir aynı, ardından `@onarim: de30689e08100c1e3c7e3c8072f8824e9b476037`, sonra gövde.

### Hikâye 2: tohum sakir-0003 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0003
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: bir şey yapmak
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kütük', fiil 'duymak', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: kutu kağıtla dolu olduğu için iyi ses çıkarmadı | kağıtları çıkarıp kapağı kapattı ve yeniden vurdu
@tohum: sakir-0003
@degisim: kütük -> kutu
Şakir macera oyunu için eski bir ayakkabı kutusundan davul yapmak istedi. Kutuya eliyle vurdu ama sesi zor duydu. Kutunun içi kağıtlarla dolu olduğu için davul iyi ses çıkarmıyordu. Şakir kapağı hemen açtı ve içine baktı. Kağıtları tek tek çıkardı ve bir kenara koydu. Sonra kapağı sıkıca kapattı. Davuluna yeniden vurdu. Bu kez yüksek ve güzel bir ses çıktı. Şakir masasından iki kalem aldı. Onlarla davulu hızlı hızlı çaldı. Şakir bu sesi çok beğendi ve güldü. Yeni davulunu mutlu mutlu çalmaya devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama sesi zor duydu"
   - Cümle 2: «Kutuya eliyle vurdu ama sesi zor duydu.»
   - Açıklama: 'Zor duydu' anlamca yerinde değil; sesin az çıktığı 'ses zor duyuldu' ya da 'ses çok azdı' ile anlatılmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0003` birebir aynı, `@degisim: kütük -> kutu` (tutuyorsan), ardından `@onarim: 091fec0630cc6be65065225aec55815dcdd9d1a9`, sonra gövde.

### Hikâye 3: tohum sakir-0017 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0017
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'fındık', fiil 'anlamak', sıfat 'peynirli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kayaların arasından bilinmeyen bir ses geldi | şapkasını öne çekip delikteki fındığı gördü
@tohum: sakir-0017
Bir sabah Şakir ile Canan kumsalda peynirli poğaça ve fındık yiyordu. Birden kayaların arasından tık tık diye bir ses geldi. Şakir bu sesin ne olduğunu anlamak istedi. "Canan, bu ses nereden geliyor?" diye sordu Şakir. "Şu küçük delikten geliyor," dedi Canan. Şakir deliğe baktı, ama güneş gözlerine geliyordu ve içini göremedi. Hemen geniş şapkasını öne doğru çekti. Şapka gözlerine gölge yaptı ve deliğin içi göründü. İçeride bir fındık vardı ve küçük dalgalar onu taşa vuruyordu. "Az önce elimden düşen fındık oraya yuvarlanmış!" dedi Canan gülerek. "Yaşasın, Canan, sesin nereden geldiğini birlikte bulduk!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "güneş gözlerine geliyordu"
   - Cümle 6: «Şakir deliğe baktı, ama güneş gözlerine geliyordu ve içini göremedi.»
   - Açıklama: 'Güneş gözüne gelmek' deyimsel bir kullanım; 'güneş gözlerini alıyordu' gibi somut anlatım gerekir.
   - Açıklama: 'Güneş gözüne gelmek' deyimsel bir anlatım, 3 yaşındaki çocuğa uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Az önce elimden düşen fındık oraya yuvarlanmış!"
   - Cümle 10: «"Az önce elimden düşen fındık oraya yuvarlanmış!" dedi Canan gülerek.»
   - Açıklama: Fındığın düşüp deliğe yuvarlanması önceden kurulmadan sonradan sebepsizce ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0017` birebir aynı, ardından `@onarim: 79d4bd5138c948c4d935b1bec2667d896319c80a`, sonra gövde.

### Hikâye 4: tohum sakir-0021 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0021
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'simit', fiil 'sarmak', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: fil acıkmıştı ama yanında yiyecek yoktu | simidini ikiye böldü ve yarısını file verdi
@tohum: sakir-0021
Bir sabah Şakir ile Necati ormanda, ağaçların arasında yürüyordu. Ama Necati'nin karnı acıkmıştı ve yanında hiç yiyecek yoktu. Şakir bu macera yürüyüşü için bir beze sardığı ılık bir simit getirmişti. Şakir simidi çıkardı ve bezi açtı. Sonra simidi iki eşit parçaya böldü. "Necati, yarısı senin," dedi Şakir. Necati simidin yarısını hortumuyla aldı. "Teşekkür ederim, Şakir, çok acıkmıştım," dedi Necati. İkisi bir kütüğün üstüne oturdu ve simidi birlikte yedi. Necati her lokmada hortumunu salladı. Şakir buna güldü. Şakir çok sevindi, çünkü simidini Necati ile paylaşmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu macera yürüyüşü için"
   - Cümle 3: «Şakir bu macera yürüyüşü için bir beze sardığı ılık bir simit getirmişti.»
   - Açıklama: 'Macera yürüyüşü' soyut bir ifade; 3 yaşındaki çocuk 'macera' kelimesini bilmeyebilir.
   - Açıklama: 'Macera yürüyüşü' soyut bir ifade, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0021` birebir aynı, ardından `@onarim: bd927628e1aa55cbde01d318b05f2c8fdea9edc9`, sonra gövde.

### Hikâye 5: tohum sakir-0024 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Canan
@tohum: sakir-0024
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'sebze', fiil 'yürümek', sıfat 'pahalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Canan
@plan: hızlı yürürken sebze sepetine çarptı ve sebzeler döküldü | kardeşinden özür diledi ve sebzeleri topladı
@tohum: sakir-0024
@degisim: pahalı -> dolu
Evde Şakir ile Canan mutfaktaydı. Şakir hızlı hızlı yürürken önüne bakmadı. Canan'ın masadaki dolu sebze sepetine çarptı ve sebzeler yere döküldü. Canan onları az önce sepete koymuştu. Canan üzüldü ve yere baktı. Şakir hemen durdu. "Özür dilerim, Canan, dikkat etmedim," dedi Şakir. Bazı domatesler masanın altındaydı. Şakir macera oyunu oynar gibi masanın altına girdi. Havuçları ve domatesleri tek tek topladı. Canan da ona yardım etti. Kısa sürede sepet yine doldu. "Tamam, Şakir, birlikte hepsini topladık," dedi Canan ve gülümsedi. Şakir çok rahatladı, çünkü kardeşi artık üzgün değildi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macera oyunu oynar gibi"
   - Cümle 9: «Şakir macera oyunu oynar gibi masanın altına girdi.»
   - Açıklama: 'Macera oyunu oynar gibi' benzetmesi soyut ve 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "macera oyunu oynar gibi"
   - Cümle 9: «Şakir macera oyunu oynar gibi masanın altına girdi.»
   - Açıklama: Benzetme ve soyut 'macera' kelimesi 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0024` birebir aynı, `@degisim: pahalı -> dolu` (tutuyorsan), ardından `@onarim: 66ad650d090ccd9742846757964c5c52318b680e`, sonra gövde.

### Hikâye 6: tohum sakir-0025 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0025
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'piyano', fiil 'küçültmek', sıfat 'şanslı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: fazla çiçek yüzünden taç çok büyük oldu | üç çiçek çıkarıp tacı şapkasına göre küçülttü
@tohum: sakir-0025
@degisim: piyano -> çiçek
Şakir, ormandaki kamp yerinde annesi Kadriye için bir sürpriz hazırlıyordu. Orada çok çiçek vardı ve Şakir onlardan bir taç yaptı. Ama fazla çiçek koyduğu için taç çok büyük oldu. Şakir tacı şapkasına taktı ama taç aşağı düştü. Üç çiçek çıkardı ve tacı küçülttü. Bu kez taç şapkada kaldı. Sonra şapkayı arkasına sakladı ve annesinin yanına koştu. "Anne, gözlerini kapar mısın?" diye sordu Şakir. Kadriye gülümsedi ve gözlerini kapadı. Şakir şapkayı tacıyla birlikte annesinin başına yavaşça koydu. Kadriye gözlerini açtı ve tacı eliyle tuttu. "Teşekkür ederim, Şakir, ben çok şanslı bir anneyim!" dedi Kadriye.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben çok şanslı bir anneyim"
   - Cümle 12: «"Teşekkür ederim, Şakir, ben çok şanslı bir anneyim!" dedi Kadriye.»
   - Açıklama: 'Şanslı' soyut bir kavram ve küçük çocuk için uygun değil.
   - Açıklama: 'Şanslı' soyut bir kavram, 3 yaşındaki çocuk için somut değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0025` birebir aynı, `@degisim: piyano -> çiçek` (tutuyorsan), ardından `@onarim: 8ac8c25680a68d1c5b6cb3210efe9d804225a72f`, sonra gövde.

### Hikâye 7: tohum sakir-0026 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0026
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'palmiye', fiil 'tutunmak', sıfat 'yeterli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: palmiyeler arasında rüzgar yeterli değildi | açık bir yere koşup ipe sıkıca tutundu
@tohum: sakir-0026
Şakir babasıyla kumsalda ilk kez uçurtma uçuracaktı. Remzi ona mavi bir uçurtma verdi. Ama palmiyeler arasında rüzgar yeterli değildi ve uçurtma hep kuma düştü. Şakir macerayı çok severdi ve bir daha denemek istedi. Etrafına baktı ve deniz kenarında açık bir yer gördü. Uçurtmayı alıp babasıyla oraya koştu. Orada rüzgar daha güçlüydü. Şakir ipe iki eliyle sıkıca tutundu. Remzi de uçurtmayı havaya bıraktı. Mavi uçurtma hızla yükseldi ve ağaçların üstüne çıktı. Remzi sevinçle zıplayıp güldü. "Babacığım, ilk uçurtmam gökyüzünde uçuyor!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Remzi ona mavi bir uçurtma verdi."
   - Cümle 2: «Remzi ona mavi bir uçurtma verdi.»
   - Açıklama: Remzi'nin Şakir'in babası olduğu söylenmeden adıyla anılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "rüzgar yeterli değildi"
   - Cümle 3: «Ama palmiyeler arasında rüzgar yeterli değildi ve uçurtma hep kuma düştü.»
   - Açıklama: 'Yeterli' soyut bir kelime, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Yeterli' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ipe iki eliyle sıkıca tutundu"
   - Cümle 8: «Şakir ipe iki eliyle sıkıca tutundu.»
   - Açıklama: Uçurtma ipi tutulur; 'tutunmak' asılıp destek almak anlamında, 'ipi sıkıca tuttu' olmalı.
   - Açıklama: Tutunmak destek almak demektir; uçurtma ipi için 'ipi sıkıca tuttu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0026` birebir aynı, ardından `@onarim: f643ea9b8146264718d21ceeaf45ae7ca692cb4c`, sonra gövde.

### Hikâye 8: tohum sakir-0027 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0027
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: paylaşmak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'süpürge', fiil 'çözmek', sıfat 'sessiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kardeşi kitabını unuttuğu için sessiz oturuyordu | çantanın ipini çözdü ve ikinci küreği paylaştı
@tohum: sakir-0027
@degisim: süpürge -> kürek
Rüzgar hafif hafif esiyordu. Şakir kumsalda küreğiyle büyük bir kale yapıyordu. Yanındaki oyuncak çantasında bir kürek daha vardı. Kardeşi Canan ise kitabını evde unuttuğu için sessiz oturuyordu. Şakir, Canan'ın üzgün olduğunu gördü. Çantanın ipini çözdü ve ikinci küreği çıkardı. "Canan, bu kürek senin olsun, gel birlikte oynayalım!" dedi Şakir. "Ne oynayacağız?" diye sordu Canan. "Bir macera oyunu, kalenin etrafına uzun bir yol kazalım!" dedi Şakir. Canan küreği aldı ve gülümsedi. İkisi yan yana kumu kazdı. Sonunda yol kalenin etrafını tam sardı. Şakir ile Canan, kalelerinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Yanındaki oyuncak çantasında bir kürek daha vardı.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor, ilk üç cümlede yok.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "kitabını evde unuttuğu için sessiz oturuyordu"
   - Cümle 4: «Kardeşi Canan ise kitabını evde unuttuğu için sessiz oturuyordu.»
   - Açıklama: Sorun ancak dördüncü cümlede söyleniyor; ilk üç cümle yalnız kale oyununu kuruyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Çantanın ipini çözdü ve ikinci küreği çıkardı"
   - Cümle 6: «Çantanın ipini çözdü ve ikinci küreği çıkardı.»
   - Açıklama: Sorunun sebebi unutulan kitap, ama çözüm kitaba değil başka bir oyuna yöneliyor.
   - Açıklama: Sebep unutulan kitap ama çözüm kitaba değil başka bir oyuna yöneliyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bir macera oyunu"
   - Cümle 9: «"Bir macera oyunu, kalenin etrafına uzun bir yol kazalım!" dedi Şakir.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Macera' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelimedir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0027` birebir aynı, `@degisim: süpürge -> kürek` (tutuyorsan), ardından `@onarim: 1eabf4a9284218488da78da56038eeb59b2626b0`, sonra gövde.

### Hikâye 9: tohum sakir-0028 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0028
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tüy', fiil 'gülümsemek', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: kumdan pastanın mumu eksikti | şemsiyenin yanında beyaz bir tüy bulup pastaya dikti
@tohum: sakir-0028
Kumsalda Fil Necati büyük bir şemsiyenin altında uyuyordu. Şakir ona sürpriz olarak kumdan bir pasta yaptı ve üstüne kabuklar dizdi. Ama pastanın mumu eksikti ve kumsalda hiç mum yoktu. Şakir mum yerine başka bir şey bulmak istedi. Macera oyunu oynar gibi şemsiyenin yanındaki kumu aradı. Kumun üstünde uzun, beyaz bir tüy buldu. Tüyü pastanın tam ortasına dikti. Şimdi pasta tamamdı. Biraz sonra Necati uyandı ve pastayı gördü. Hortumuyla tüye yavaşça dokundu ve gülümsedi. Şakir de sevinçle ellerini çırptı. Şakir bundan sonra bir şey eksik olunca önce etrafına dikkatle baktı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macera oyunu oynar gibi"
   - Cümle 5: «Macera oyunu oynar gibi şemsiyenin yanındaki kumu aradı.»
   - Açıklama: Benzetme ve soyut 'macera' kavramı 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Macera oyunu oynar gibi' benzetmesi ve 'macera' kelimesi 3 yaşındaki çocuk için soyut.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0028` birebir aynı, ardından `@onarim: 54546f3a38f687653c9cd81614dd064bd387a2a4`, sonra gövde.

### Hikâye 10: tohum sakir-0029 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Remzi
@tohum: sakir-0029
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kek', fiil 'gezinmek', sıfat 'tuzlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Remzi
@plan: rüzgar oyunun haritasını uçurdu | babasından sıcak soğuk demesini isteyip kutuyu buldu
@tohum: sakir-0029
@degisim: tuzlu -> sarı
Parkta Şakir ile babası Remzi bir macera oyunu oynuyordu. Remzi sarı bir kutuya kek koyup saklamış, bir de harita çizmişti. Ama rüzgar esti ve harita uçup gitti. Ama Şakir hiç üzülmedi ve oyunu bırakmadı. "Baba, yaklaşınca 'sıcak', uzaklaşınca 'soğuk' der misin?" diye sordu Şakir. "Tamam, haydi başla!" dedi Remzi gülerek. Şakir parkta gezinmeye başladı. "Soğuk, çok soğuk!" dedi Remzi ve titriyormuş gibi yaptı. Şakir döndü ve banklara doğru yürüdü. "Sıcak, çok sıcak!" dedi Remzi. Şakir bankın altına baktı ve sarı kutuyu buldu. Sonra ikisi banka oturdu ve keki mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Ama Şakir hiç üzülmedi"
   - Cümle 4: «Ama Şakir hiç üzülmedi ve oyunu bırakmadı.»
   - Açıklama: Art arda iki cümle 'Ama' ile başlıyor, gereksiz tekrar.
   - Açıklama: Art arda iki cümle 'Ama' ile başlıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0029` birebir aynı, `@degisim: tuzlu -> sarı` (tutuyorsan), ardından `@onarim: a38613ece0577de5aa7b8091c4a9aeaf88a68070`, sonra gövde.

### Hikâye 11: tohum sakir-0030 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0030
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'hamur', fiil 'parlamak', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: ıslak kumdaki parlak şeyi dalgalar kapatıyordu | şapkasıyla alıp bir kabuk olduğunu gördü
@tohum: sakir-0030
@degisim: hamur -> kabuk
Rüzgar hafifçe esiyordu. Şakir kumsalda yürürken ıslak kumda parlayan bir şey gördü. Ama küçük dalgalar gelip gidiyordu ve onu hep kapatıyordu. Şakir onun ne olduğunu çok merak etti. Suya girmedi ve kumda bekledi. Dalga gidince Şakir şapkasını çıkardı. Parlayan şeyi şapkasıyla yavaşça aldı. Şapkanın içinde küçük, ıslak bir deniz kabuğu vardı. Kabuğun rengi pembe bir tatlıya benziyordu. Şakir kabuğu avucuna aldı ve güneşe tuttu. Kabuk yine parladı. Şakir çok sevindi, çünkü parlayan şeyin ne olduğunu bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "pembe bir tatlıya benziyordu"
   - Cümle 9: «Kabuğun rengi pembe bir tatlıya benziyordu.»
   - Açıklama: Rengi tatlıya benzetmek mecazlı ve belirsiz bir benzetme.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kabuğun rengi pembe bir tatlıya benziyordu"
   - Cümle 9: «Kabuğun rengi pembe bir tatlıya benziyordu.»
   - Açıklama: Kabuğun tatlıya benzeyen rengi işlevsiz bir ayrıntı ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0030` birebir aynı, `@degisim: hamur -> kabuk` (tutuyorsan), ardından `@onarim: 7e43f173dfa0d37936484f5c99b3a63490f23943`, sonra gövde.

### Hikâye 12: tohum sakir-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0031
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'patates', fiil 'göstermek', sıfat 'kırılgan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: fil ağır adımlarla yoldaki çiçeğe doğru geliyordu | fili durdurup çiçeğin etrafına taş dizdi
@tohum: sakir-0031
@degisim: patates -> çiçek
Bir sabah Şakir ile Fil Necati parkta yürüyordu. Şakir yolun ortasında ince saplı, kırılgan bir çiçek gördü. Ama Necati ağır adımlarla tam çiçeğe doğru geliyordu. "Dur, Necati, sana bir çiçek göstermek istiyorum!" dedi Şakir. Necati durdu ve eğilip çiçeğe baktı. "Onu hiç görmemiştim," dedi Necati. Şakir macerayı çok severdi ve hemen çalıların arasında taş aradı. Dört büyük taş buldu ve onları çiçeğin etrafına dizdi. Şimdi çiçek uzaktan kolayca görünüyordu. Necati ayak uçlarında yürüdü ve çiçeğin yanından dikkatle geçti. "Artık çiçeğe kimse basmaz, Necati!" dedi Şakir sevinçle.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 7: «Şakir macerayı çok severdi ve hemen çalıların arasında taş aradı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi ve hemen çalıların arasında taş aradı"
   - Cümle 7: «Şakir macerayı çok severdi ve hemen çalıların arasında taş aradı.»
   - Açıklama: Taş arama maceracılığa sebepsizce bağlanıyor; olay öncekinden çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0031` birebir aynı, `@degisim: patates -> çiçek` (tutuyorsan), ardından `@onarim: ba4c39e7c5cd946665493876729defaf9ff5a8f7`, sonra gövde.
