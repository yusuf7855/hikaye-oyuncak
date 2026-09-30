# Editör görevi (onarım): Şakir, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0037 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Remzi
@tohum: sakir-0037
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: bir şey yapmak
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'spagetti', fiil 'kokmak', sıfat 'rahat'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Remzi
@plan: spagetti çok uzundu ve tencereye sığmadı | bölmeyi önerdi ve spagettiyi şapkasının içinde kırdı
@tohum: sakir-0037
Bir akşam Şakir babası Remzi ile mutfakta spagetti yapıyordu. Ama spagetti çok uzundu ve tencereye sığmadı. Remzi spagettiye şaşkın şaşkın baktı. "Baba, onları ikiye bölelim mi?" diye sordu Şakir. "Tamam, Şakir," dedi Remzi. Şakir beyaz şapkasını çıkardı ve ters çevirdi. Spagettileri şapkanın içinde ikiye kırdı, böylece parçalar yere düşmedi. Remzi kısa parçaları tencereye koydu. Bu kez hepsi tencereye sığdı. Biraz sonra mutfak çok güzel kokmaya başladı. Remzi yemeği iki tabağa koydu. Şakir ile Remzi rahat sandalyelere oturup yediler. Şakir çok mutluydu, çünkü yemeği babasıyla birlikte yapmıştı.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "spagettiyi şapkasının içinde kırdı"
   - Cümle 0 (plan satırı): «spagetti çok uzundu ve tencereye sığmadı | bölmeyi önerdi ve spagettiyi şapkasının içinde kırdı»
   - Açıklama: Planda spagettiyi Şakir kırıyor ama gövdede Remzi kırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0037` birebir aynı, ardından `@onarim: 9b1150f5f9887fc09e2afbf5058be057b0fbbbc1`, sonra gövde.

### Hikâye 2: tohum sakir-0149 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0149
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'elbise', fiil 'cevaplamak', sıfat 'kısa'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: koşarken filin çiçek sepetini düşürüp kırdı | özür diledi ve çiçekleri şapkasına topladı
@tohum: sakir-0149
@degisim: elbise -> çiçek
Bir sabah Şakir kamp yerinde hızlı hızlı koşuyordu. Koşarken Necati'nin çiçek sepetine çarptı. Sepet yere düşüp kırıldı ve çiçekler kısa otlara dağıldı. Necati bu çiçekleri çadırını süslemek için toplamıştı. Necati kırık sepete baktı ve ne olduğunu sordu. Şakir soruyu hemen doğru cevapladı ve özür diledi. Sonra başındaki yeşil şapkasını çıkardı. Otların arasındaki çiçekleri tek tek toplayıp şapkaya koydu. Şapka bir sepet gibi doldu. Şakir şapkayı Necati'ye uzattı. Necati gülümsedi ve şapkayı çadırın önüne koydu. Şakir çok sevindi, çünkü Necati'nin çadırı yine çiçeklerle süslüydü.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir soruyu hemen doğru cevapladı"
   - Cümle 6: «Şakir soruyu hemen doğru cevapladı ve özür diledi.»
   - Açıklama: 'Soruyu doğru cevapladı' bu bağlamda anlamca uygun değil; kastedilen doğruyu söylemesi.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "soruyu hemen doğru cevapladı"
   - Cümle 6: «Şakir soruyu hemen doğru cevapladı ve özür diledi.»
   - Açıklama: 'Doğru cevapladı' sınav sorusu anlamı taşır, bu bağlamda yanlış kelime seçimi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0149` birebir aynı, `@degisim: elbise -> çiçek` (tutuyorsan), ardından `@onarim: d4d1dec61e4056e4cae808ffe77800b0a85c1559`, sonra gövde.

### Hikâye 3: tohum sakir-0151 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0151
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kapak', fiil 'şaşırmak', sıfat 'büyük'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | -
@plan: kapak çok düz olduğu için kum kulesi yıkıldı | şapkasını kumla doldurup ters çevirdi
@tohum: sakir-0151
Şakir parktaki kum havuzunda büyük bir kapak ile oynuyordu. Kapağı kumla doldurdu ve ters çevirip bir kule yaptı. Ama kapak çok düzdü ve kule hemen yıkıldı. Şakir bir kez daha denedi, ama kule yine yıkıldı. Sonra yuvarlak şapkasına baktı. Şapka çok derindi. Şakir şapkasını çıkardı ve içini kumla doldurdu. Kumu elleriyle sıkıca bastırdı. Sonra şapkayı ters çevirdi ve yavaşça kaldırdı. Kumdan yüksek bir kule çıktı ve hiç yıkılmadı. Kule tıpkı şapkaya benziyordu ve Şakir buna çok şaşırdı. Hemen yanına iki şapka kulesi daha yaptı. Şakir kum kalesini yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama kapak çok düzdü ve kule hemen yıkıldı"
   - Cümle 3: «Ama kapak çok düzdü ve kule hemen yıkıldı.»
   - Açıklama: Düz bir kapaktan zaten kule çıkmaz; kapağın düz olmasıyla kulenin yıkılması arasındaki sebep akla yatkın değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir kum kalesini yapmaya"
   - Cümle 13: «Şakir kum kalesini yapmaya mutlu mutlu devam etti.»
   - Açıklama: Daha önce hiç kale geçmediği halde belirli 'kum kalesini' kullanılıyor, yapılan şey kuleydi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0151` birebir aynı, ardından `@onarim: 7aa973980ebe3426741e1f92867438baf0156435`, sonra gövde.

### Hikâye 4: tohum sakir-0154 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0154
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yama', fiil 'akmak', sıfat 'sakin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: oyuncak kayık taşa çarptı ve yelkeni yırtıldı | bez şapkasını yelken yapıp kayığı taşa götürdü
@tohum: sakir-0154
Deniz sakindi ve hafif bir rüzgar esiyordu. Şakir ile Canan kumsalda gemi oyunu oynuyordu. Ama oyuncak kayık küçük bir taşa çarptı ve kağıt yelkeni yırtıldı. Kayık, kumda akan ince bir suyun içinde durdu. İkisi kayığı büyük taşa götürmek istiyordu. "Şakir, yelkene bir yama yapalım mı?" diye sordu Canan. Şakir bez şapkasına baktı. "Yama yerine şapkamı takalım," dedi Şakir. Şakir şapkayı kayığın küçük direğine taktı. Rüzgar şapkaya doldu ve kayık yeniden yüzdü. Kayık büyük taşa kadar gitti. "Yaşasın, Şakir, taşa vardık!" dedi Canan. Kardeşler gemi oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kardeşler gemi oyununa mutlu"
   - Cümle 13: «Kardeşler gemi oyununa mutlu mutlu devam etti.»
   - Açıklama: Şakir ile Canan'ın kardeş olduğu hiç söylenmediği için 'Kardeşler' kimi gösterdiği belirsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0154` birebir aynı, ardından `@onarim: 3376aa570078731ffd8173d5dfb3a03fdbb0838b`, sonra gövde.

### Hikâye 5: tohum sakir-0155 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0155
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kemer', fiil 'almak', sıfat 'ekşi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: fil sürpriz hazır olmadan geri geldi | şapkasıyla erikleri örttü ve sonra açtı
@tohum: sakir-0155
@degisim: kemer -> erik
Şakir, Necati için kumsalda bir sürpriz hazırlıyordu. Çantasından Necati'nin en sevdiği ekşi erikleri aldı ve havluya dizdi. Ama Necati su kenarından erken geri geliyordu. Şakir erikleri saklamak istedi. Şakir geniş şapkasını hemen çıkardı. Şapkayla erikleri örttü. Necati geldi ve yerdeki şapkaya baktı. "Şakir, şapkan neden yerde?" diye sordu Necati. "Çünkü altında sana bir sürpriz var," dedi Şakir. Şakir şapkayı yavaşça kaldırdı. "Erikler mi, onları çok severim!" dedi Necati sevinçle. İkisi erikleri paylaştı ve mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "fil sürpriz hazır olmadan geri geldi"
   - Cümle 0 (plan satırı): «fil sürpriz hazır olmadan geri geldi | şapkasıyla erikleri örttü ve sonra açtı»
   - Açıklama: Gövdede fil yok; geri gelen Necati'dir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0155` birebir aynı, `@degisim: kemer -> erik` (tutuyorsan), ardından `@onarim: 4f7b40c7e51c4f9548407d9e34125a0d705d8f74`, sonra gövde.

### Hikâye 6: tohum sakir-0156 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0156
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kızartma', fiil 'ödemek', sıfat 'umutlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: kabuklar küçük elinden hep düşüyordu | kabukları şapkasına doldurup taşıdı
@tohum: sakir-0156
@degisim: ödemek -> taşımak
Kumsalda Şakir annesi için kabuklardan bir kalp yapmak istedi. Kadriye o sırada örtüye patates kızartması koyuyordu. Ama kabuklar su kenarındaydı ve Şakir'in küçük elinden hep düşüyordu. Şakir büyük şapkasını çıkardı. Kabukları tek tek şapkanın içine koydu. Şapka doldu ve hiçbir kabuk düşmedi. Şakir şapkayı örtünün yanına taşıdı. Kabuklarla kumun üstüne büyük bir kalp yaptı. Sonra umutlu bir yüzle annesine baktı. "Anne, sana bir sürprizim var!" dedi Şakir. Kadriye döndü ve kalbi görünce gülümsedi. "Teşekkürler, Şakir, bu çok güzel bir sürpriz!" dedi Kadriye.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kadriye o sırada örtüye"
   - Cümle 2: «Kadriye o sırada örtüye patates kızartması koyuyordu.»
   - Açıklama: Kadriye'nin Şakir'in annesi olduğu söylenmeden adıyla sahneye giriyor, kimi gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "örtüye patates kızartması koyuyordu"
   - Cümle 2: «Kadriye o sırada örtüye patates kızartması koyuyordu.»
   - Açıklama: Patates kızartması kurulup hiçbir işe yaramıyor; işlevsiz ayrıntı.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra umutlu bir yüzle annesine"
   - Cümle 9: «Sonra umutlu bir yüzle annesine baktı.»
   - Açıklama: 'Umutlu bir yüz' soyut bir ifade, küçük çocuk için uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "umutlu bir yüzle annesine"
   - Cümle 9: «Sonra umutlu bir yüzle annesine baktı.»
   - Açıklama: 'Umutlu bir yüzle' soyut bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0156` birebir aynı, `@degisim: ödemek -> taşımak` (tutuyorsan), ardından `@onarim: 827f4e1dd9046766f26d85f55a99288282cae840`, sonra gövde.

### Hikâye 7: tohum sakir-0159 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0159
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'lamba', fiil 'kutlamak', sıfat 'eğlenceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: kumsal çok aydınlıktı ve lambanın ışığı görünmedi | lambanın üstüne şapkasını koyup altına baktı
@tohum: sakir-0159
Bir sabah Şakir kumsala küçük bir lamba getirdi. Bu lamba güneşte bekleyince karanlıkta parlıyordu. Şakir parladığını görmek istedi ama kumsal çok aydınlıktı. Önce lambayı güneşli kumun üstüne koydu. Lambanın yanına oturdu ve bir süre bekledi. Sonra geniş şapkasını çıkardı. Şapkayla lambanın üstünü örttü. Şapkanın kenarını biraz kaldırdı ve içine baktı. Şapkanın altı karanlıktı ve lamba sarı sarı parlıyordu. Şakir bunu kumda zıplayarak kutladı. Bu çok eğlenceli bir oyundu. Şakir şapkanın altındaki lambaya bakmaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şakir parladığını görmek istedi"
   - Cümle 3: «Şakir parladığını görmek istedi ama kumsal çok aydınlıktı.»
   - Açıklama: 'parladığını' kelimesinin neyi gösterdiği açıkça söylenmiyor; 'lambanın parladığını' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0159` birebir aynı, ardından `@onarim: 23e637dfcaf5390fa43469d34da27374b6ebe6b5`, sonra gövde.

### Hikâye 8: tohum sakir-0161 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0161
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'baharat', fiil 'işaretlemek', sıfat 'yardımsever'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: rüzgar baharat paketlerini masadan uçurdu | şapkasıyla paketleri yakalayıp annesine verdi
@tohum: sakir-0161
@degisim: işaretlemek -> uçmak
Rüzgar esiyordu. Şakir ile annesi Kadriye kamp masasında salata yapıyordu. Kadriye salataya baharat koyacaktı. Birden rüzgar hafif baharat paketlerini masadan uçurdu. Paketler otların üstünde uçup gidiyordu. "Şakir, paketleri tutar mısın?" diye sordu Kadriye. Şakir büyük şapkasını hemen çıkardı. Paketlere doğru koştu ve onları şapkayla tek tek yakaladı. Üç paketin hepsi şapkanın içine girdi. Şakir şapkayı annesine uzattı. Kadriye bir paketi açtı ve salataya biraz baharat koydu. "Teşekkürler, Şakir, sen çok yardımseversin!" dedi Kadriye.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Birden rüzgar hafif baharat paketlerini masadan uçurdu"
   - Cümle 4: «Birden rüzgar hafif baharat paketlerini masadan uçurdu.»
   - Açıklama: Sorun ilk üç cümlede değil, dördüncü cümlede söyleniyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden rüzgar hafif baharat paketlerini masadan uçurdu"
   - Cümle 4: «Birden rüzgar hafif baharat paketlerini masadan uçurdu.»
   - Açıklama: Rüzgarın dağıttığı paketlerin toplanıp bitmesi çocuğun önemseyeceği bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0161` birebir aynı, `@degisim: işaretlemek -> uçmak` (tutuyorsan), ardından `@onarim: 780ee5b496e7a85e16a9fc9f7a13add2275af0ab`, sonra gövde.

### Hikâye 9: tohum sakir-0162 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0162
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bayrak', fiil 'hatırlamak', sıfat 'düz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: kalenin bayrağı evde kalmıştı | düz bir çubuğa şapkasını takıp bayrak yaptı
@tohum: sakir-0162
Şakir ile babası Remzi kumsalda büyük bir kale yapmıştı. Remzi kalenin tepesine bir bayrak koymak istedi. "Ah, bayrağı evde unuttum!" dedi Remzi. Remzi üzgün üzgün kaleye baktı. Şakir biraz düşündü ve bir şey hatırladı. Az önce kumda düz ve uzun bir çubuk görmüştü. Şakir çubuğu getirdi ve ucuna küçük kırmızı şapkasını taktı. Sonra çubuğu kalenin tepesine dikti. Şapka rüzgarda bir bayrak gibi sallandı. Remzi sevinçle ellerini çırptı. "Harika bir bayrak, Şakir!" dedi Remzi. Şakir ile babası kaleyle mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Az önce kumda düz ve uzun bir çubuk görmüştü"
   - Cümle 6: «Az önce kumda düz ve uzun bir çubuk görmüştü.»
   - Açıklama: Çözümü sağlayan çubuk önceden kurulmadan sonradan hatırlanarak sebepsizce beliriyor.
   - Açıklama: Çözümü getiren çubuk önceden kurulmadan tam gerektiği anda sonradan hatırlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0162` birebir aynı, ardından `@onarim: 347c87c2624a0818a199144308ffc47f96501fb4`, sonra gövde.

### Hikâye 10: tohum sakir-0164 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0164
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'değnek', fiil 'olgunlaşmak', sıfat 'mavi'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: küçük bir dalga mavi topu kıyıdan uzağa götürdü | şapkasını değneğin ucuna takıp topu aldı
@tohum: sakir-0164
@degisim: olgunlaşmak -> yakalamak
Şakir kumsalda mavi topuyla oynuyordu. Top su kenarında sallanıyordu. Ama küçük bir dalga topu kıyıdan biraz uzağa götürdü. Şakir suya girmedi ve kıyıda kaldı. Kumda uzun bir değnek buldu. Ama değnek topu tutamadı, top hep kaydı. Şakir yuvarlak şapkasını çıkardı. Şapkayı değneğin ucuna sıkıca taktı. Değnek küçük bir ağ gibi oldu. Şakir şapkayı suya soktu ve topu içine aldı. Sonra değneği yavaşça kıyıya çekti. Şakir çok sevindi, çünkü topunu kendisi yakalamıştı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "top hep kaydı"
   - Cümle 6: «Ama değnek topu tutamadı, top hep kaydı.»
   - Açıklama: 'hep' süreklilik bildirdiği için bitmiş geçmişle uyumsuz; 'hep kayıyordu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama değnek topu tutamadı"
   - Cümle 6: «Ama değnek topu tutamadı, top hep kaydı.»
   - Açıklama: Değnek bir şey tutmaz; özne uygun değil, 'değnekle topu tutamadı' olmalı.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Ama değnek topu tutamadı, top hep kaydı"
   - Cümle 6: «Ama değnek topu tutamadı, top hep kaydı.»
   - Açıklama: Çözüm önce işe yaramayan bir değnek denemesinden geçiyor, sonra şapka takılıyor; çözüm iki adımı aşıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Değnek küçük bir ağ gibi oldu"
   - Cümle 9: «Değnek küçük bir ağ gibi oldu.»
   - Açıklama: Benzetme hem mecazlı hem yanlış; ağa benzeyen değnek değil şapkalı değnek.
5. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir şapkayı suya soktu ve topu içine aldı"
   - Cümle 10: «Şakir şapkayı suya soktu ve topu içine aldı.»
   - Açıklama: Kumsalda yalnız bir çocuğun dalganın uzaklaştırdığı topa değnekle suya uzanması taklit edilince tehlikelidir ve güvenli kullanım satırındaki güvenli oyun sınırını zorlar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0164` birebir aynı, `@degisim: olgunlaşmak -> yakalamak` (tutuyorsan), ardından `@onarim: 75d64d415562843e368c450d670ef100503967fe`, sonra gövde.

### Hikâye 11: tohum sakir-0166 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0166
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'limonata', fiil 'bakmak', sıfat 'kokulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: rüzgar limonata bardağının içine yaprak attı | şapkasını bardağın üstüne kapak gibi koydu
@tohum: sakir-0166
Rüzgar esiyordu ve Şakir kamp yerinde annesiyle komik bir oyun oynuyordu. Kocaman adımlarla annesine kokulu bir limonata taşıyordu. Ama rüzgar bardağın içine küçük bir yaprak attı. "Şakir, limonatada yaprak var!" dedi Kadriye ve güldü. Şakir bardağa baktı ve yaprağı çıkardı. Sonra şapkasını bardağın üstüne kapak gibi koydu. Yine aynı adımlarla annesine doğru yürüdü. Rüzgar yeniden esti ama bardağa hiçbir şey düşmedi. Kadriye limonatayı içti. "Çok güzel olmuş, teşekkürler," dedi Kadriye. Şakir çok sevindi, çünkü annesine temiz bir limonata getirmişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "annesine kokulu bir limonata"
   - Cümle 2: «Kocaman adımlarla annesine kokulu bir limonata taşıyordu.»
   - Açıklama: 'Kokulu' limonata için uygun bir sıfat değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar bardağın içine küçük bir yaprak attı"
   - Cümle 3: «Ama rüzgar bardağın içine küçük bir yaprak attı.»
   - Açıklama: Bardağa düşen yaprak hemen çıkarılabilen önemsiz bir olay; sorun tek hareketle bitiyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "dedi Kadriye ve güldü"
   - Cümle 4: «"Şakir, limonatada yaprak var!" dedi Kadriye ve güldü.»
   - Açıklama: Kadriye'nin Şakir'in annesi olduğu söylenmeden adı ansızın kullanılıyor; kimi gösterdiği belli değil.
   - Açıklama: Kadriye'nin, önceki cümlelerdeki anne olduğu belirtilmeden birden ortaya çıkıyor ve kim olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0166` birebir aynı, ardından `@onarim: 128e1c3d60be96c66a09422ec8cfc315682f6164`, sonra gövde.

### Hikâye 12: tohum sakir-0167 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0167
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kızak', fiil 'tanıştırmak', sıfat 'beyaz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: küçük kabuklar babasının elinden kuma düşüyordu | kabukları şapkasına doldurup babasına taşıdı
@tohum: sakir-0167
@degisim: tanıştırmak -> taşımak
Dalgalar yavaşça kıyıya geliyordu. Şakir ile babası Remzi kumdan kocaman bir kızak yapmıştı. Ama küçük beyaz kabuklar Remzi'nin elinden hep kuma düşüyordu. "Kızağı bu kabuklarla süslemek istiyorum," dedi Remzi. Şakir hemen şapkasını çıkardı. Su kenarından kabukları toplayıp içine doldurdu. Sonra hepsini babasına taşıdı. Bu kez hiçbir kabuk kuma düşmedi. Remzi kabukları tek tek aldı ve kızağa dizdi. "Teşekkürler, Şakir, kızak çok güzel oldu!" dedi Remzi. Şakir bundan sonra babası zorlandığında ona hemen yardım etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Remzi'nin elinden hep kuma düşüyordu"
   - Cümle 3: «Ama küçük beyaz kabuklar Remzi'nin elinden hep kuma düşüyordu.»
   - Açıklama: Kabukların neden elden düştüğü söylenmiyor ve kuma düşen kabuğu yerden almak kolay olduğundan sorun önemsiz kalıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük beyaz kabuklar Remzi'nin elinden hep kuma düşüyordu"
   - Cümle 3: «Ama küçük beyaz kabuklar Remzi'nin elinden hep kuma düşüyordu.»
   - Açıklama: Kabukların neden düştüğü söylenmiyor ve kuma düşen kabuk yerden alınabilecek önemsiz bir olay.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şakir bundan sonra babası zorlandığında ona hemen yardım etti"
   - Cümle 11: «Şakir bundan sonra babası zorlandığında ona hemen yardım etti.»
   - Açıklama: Anlatıda 'bundan sonra' ile süreklilik için 'ondan sonra ... yardım ederdi' olmalı; zaman/zarf uyumu bozuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0167` birebir aynı, `@degisim: tanıştırmak -> taşımak` (tutuyorsan), ardından `@onarim: 0b31d24cfcb8ebcec1149194918269a5fb6f0d9d`, sonra gövde.
