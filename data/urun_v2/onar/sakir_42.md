# Editör görevi (onarım): Şakir, onarım partisi 42

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar42.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar42.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0037 (deneme 5 -> 6)

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
@plan: spagetti çok uzundu ve tencereye sığmadı | bölmeyi önerdi ve spagettiyi şapkasında ikiye kırdı
@tohum: sakir-0037
Bir akşam Şakir babası Remzi ile mutfakta spagetti yapıyordu. Ama spagetti çok uzundu ve tencereye sığmadı. Remzi spagettiye şaşkın şaşkın baktı. "Baba, onları ikiye bölelim mi?" diye sordu Şakir. "Tamam, Şakir," dedi Remzi. Şakir beyaz şapkasını çıkardı ve ters çevirdi. Şakir spagettileri şapkanın içinde kendisi ikiye kırdı. Parçalar yere düşmedi. Remzi kısa parçaları tencereye koydu. Bu kez hepsi tencereye sığdı. Biraz sonra mutfak çok güzel kokmaya başladı. Remzi yemeği iki tabağa koydu. Şakir ile Remzi rahat sandalyelere oturup yediler. Şakir çok mutluydu, çünkü yemeği babasıyla birlikte yapmıştı.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "şapkanın içinde kendisi ikiye kırdı"
   - Cümle 7: «Şakir spagettileri şapkanın içinde kendisi ikiye kırdı.»
   - Açıklama: Özne zaten Şakir iken 'kendisi' gereksiz bir tekrar ve cümleyi bozuyor.
   - Açıklama: Özne zaten 'Şakir' olduğu için 'kendisi' gereksiz bir tekrardır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0037` birebir aynı, ardından `@onarim: 5338b28b137ed95c69b7fcbd6bae619c5a7bad51`, sonra gövde.

### Hikâye 2: tohum sakir-0155 (deneme 2 -> 3)

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
@plan: sürpriz hazırken fil erken geri geliyordu | şapkasıyla erikleri örttü ve sonra açtı
@tohum: sakir-0155
@degisim: kemer -> erik
Şakir, Fil Necati için kumsalda bir sürpriz hazırlıyordu. Çantasından Necati'nin en sevdiği ekşi erikleri aldı ve havluya dizdi. Ama Necati su kenarından erken geri geliyordu. Şakir erikleri saklamak istedi. Şakir geniş şapkasını hemen çıkardı. Şapkayla erikleri örttü. Necati geldi ve yerdeki şapkaya baktı. "Şakir, şapkan neden yerde?" diye sordu Necati. "Çünkü altında sana bir sürpriz var," dedi Şakir. Şakir şapkayı yavaşça kaldırdı. "Erikler mi, onları çok severim!" dedi Necati sevinçle. İkisi erikleri paylaştı ve mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sürpriz hazırken fil erken"
   - Cümle 0 (plan satırı): «sürpriz hazırken fil erken geri geliyordu | şapkasıyla erikleri örttü ve sonra açtı»
   - Açıklama: Plan satırı dilbilgisel değil; 'sürpriz hazırlanırken' olmalı.
   - Açıklama: Plan satırı bozuk; 'sürprizi hazırlarken' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0155` birebir aynı, `@degisim: kemer -> erik` (tutuyorsan), ardından `@onarim: c81aa399340f28047467241c97c33e39a7bb629f`, sonra gövde.

### Hikâye 3: tohum sakir-0156 (deneme 2 -> 3)

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
Kumsalda Şakir annesi için kabuklardan bir kalp yapmak istedi. Annesi Kadriye o sırada örtüye patates kızartması koyuyordu ve Şakir'i görmüyordu. Ama kabuklar su kenarındaydı ve Şakir'in küçük elinden hep düşüyordu. Şakir büyük şapkasını çıkardı. Kabukları tek tek şapkanın içine koydu. Şapka doldu ve hiçbir kabuk düşmedi. Şakir şapkayı örtünün yanına taşıdı. Kabuklarla kumun üstüne büyük bir kalp yaptı. Şakir annesinin kalbi seveceğinden umutluydu. "Anne, sana bir sürprizim var!" dedi Şakir. Kadriye döndü ve kalbi görünce gülümsedi. "Teşekkürler, Şakir, gel şimdi birlikte kızartma yiyelim!" dedi Kadriye.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "ve Şakir'i görmüyordu"
   - Cümle 2: «Annesi Kadriye o sırada örtüye patates kızartması koyuyordu ve Şakir'i görmüyordu.»
   - Açıklama: Annesi görmezken Şakir su kenarında tek başına dolaşıyor; bu taklit edilince tehlikeli ve güvenli kullanım satırına aykırı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "koyuyordu ve Şakir'i görmüyordu"
   - Cümle 2: «Annesi Kadriye o sırada örtüye patates kızartması koyuyordu ve Şakir'i görmüyordu.»
   - Açıklama: Annesi görmezken Şakir su kenarına gidiyor; bu, güvenli kullanım satırındaki tek başına uzaklaşmama ilkesine ve su güvenliğine aykırı, taklit edilebilir bir davranış.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "annesinin kalbi seveceğinden umutluydu"
   - Cümle 9: «Şakir annesinin kalbi seveceğinden umutluydu.»
   - Açıklama: 'Umutluydu' soyut bir kelime ve 'annesinin kalbi' ifadesi annenin kalbi diye yanlış okunabilir.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir annesinin kalbi seveceğinden umutluydu"
   - Cümle 9: «Şakir annesinin kalbi seveceğinden umutluydu.»
   - Açıklama: 'Umutluydu' soyut bir kavram ve 'annesinin kalbi' annenin kendi kalbi gibi yanlış okunabiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0156` birebir aynı, `@degisim: ödemek -> taşımak` (tutuyorsan), ardından `@onarim: 2f21cd6db9669aea5ef0e33ef443125cb8c0758c`, sonra gövde.

### Hikâye 4: tohum sakir-0159 (deneme 2 -> 3)

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
Bir sabah Şakir kumsala küçük bir lamba getirdi. Bu lamba güneşte bekleyince karanlıkta parlıyordu. Şakir lambanın parladığını görmek istedi ama kumsal çok aydınlıktı. Önce lambayı güneşli kumun üstüne koydu. Lambanın yanına oturdu ve bir süre bekledi. Sonra geniş şapkasını çıkardı. Şapkayla lambanın üstünü örttü. Şapkanın kenarını biraz kaldırdı ve içine baktı. Şapkanın altı karanlıktı ve lamba sarı sarı parlıyordu. Şakir bunu kumda zıplayarak kutladı. Bu çok eğlenceli bir oyundu. Şakir şapkanın altındaki lambaya bakmaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Şakir kumsala"
   - Cümle 1: «Bir sabah Şakir kumsala küçük bir lamba getirdi.»
   - Açıklama: Şakir deniz kıyısında yanında bir büyük olmadan tek başına; güvenli özellik kullanımı satırı tek başına uzağa gitmemesini söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0159` birebir aynı, ardından `@onarim: 3e729e86a70dc9d7ac06053c830c20aef75fdc78`, sonra gövde.

### Hikâye 5: tohum sakir-0167 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: kum çok kuruydu ve kızak hep dağılıyordu | şapkasıyla ıslak kum getirdi
@tohum: sakir-0167
@degisim: tanıştırmak -> taşımak
Dalgalar yavaşça kıyıya geliyordu. Şakir ile babası Remzi kumdan kocaman bir kızak yapıyordu. Ama kum çok kuruydu ve kızak hep dağılıyordu. "Kızak yine dağıldı, Şakir," dedi Remzi. Şakir su kenarındaki kuma baktı. Oradaki kum ıslaktı ve sıkıydı. Şakir beyaz şapkasını çıkardı. Şapkayı ıslak kumla doldurdu ve babasına taşıdı. Sonra ıslak kumu kızağa sıkıca bastırdı. Bu kez kızak hiç bozulmadı. "Teşekkürler, Şakir, kızak çok güzel oldu!" dedi Remzi. Şakir böylece kumdan kızak için ıslak kum gerektiğini öğrendi.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "şapkasıyla ıslak kum getirdi"
   - Cümle 0 (plan satırı): «kum çok kuruydu ve kızak hep dağılıyordu | şapkasıyla ıslak kum getirdi»
   - Açıklama: Planda kumu Şakir getiriyor ama gövdede kumu Remzi dolduruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0167` birebir aynı, `@degisim: tanıştırmak -> taşımak` (tutuyorsan), ardından `@onarim: 1167cd49b970d25f9d9af9b1c76a58bbbc99e267`, sonra gövde.

### Hikâye 6: tohum sakir-0170 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0170
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'düğme', fiil 'taşınmak', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: düğmeyi arkasına sakladı ama kardeşi onu hemen gördü | düğmeyi şapkasının içine koyup başına taktı
@tohum: sakir-0170
@degisim: taşınmak -> saklamak
Kuşlar ağaçlarda ötüyordu. Şakir kamp yerinde Canan'a bir sihir oyunu gösteriyordu. Kıpkırmızı bir düğmeyi arkasına sakladı ama Canan onu hemen gördü. "Düğme arkanda, Şakir!" dedi Canan ve güldü. Şakir biraz düşündü. "Gözlerini kapat, Canan," dedi Şakir. Şakir şapkasını çıkardı ve düğmeyi içine koydu. Şapkayı yine başına taktı. Canan gözlerini açtı ve Şakir boş ellerini gösterdi. "Düğme yok oldu!" dedi Şakir. Canan her yere baktı ama düğmeyi bulamadı. Sonra Şakir başını eğdi ve düğme Canan'ın önüne düştü. Canan şaşırdı ve ellerini çırptı. İkisi sihir oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "düğmeyi şapkasının içine koyup başına taktı"
   - Cümle 0 (plan satırı): «düğmeyi arkasına sakladı ama kardeşi onu hemen gördü | düğmeyi şapkasının içine koyup başına taktı»
   - Açıklama: 'Taktı' fiilinin nesnesi (şapkayı) eksik; cümle düğmeyi başına taktı diye okunuyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Canan'a bir sihir oyunu gösteriyordu"
   - Cümle 2: «Şakir kamp yerinde Canan'a bir sihir oyunu gösteriyordu.»
   - Açıklama: Kartın tohum yasak kategorilerinde büyü var; sihir oyunu bu dünyaya aykırı olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0170` birebir aynı, `@degisim: taşınmak -> saklamak` (tutuyorsan), ardından `@onarim: 4c2c0b511f28abb3505db99fedc95c85bf967baa`, sonra gövde.

### Hikâye 7: tohum sakir-0173 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0173
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'baloncuk', fiil 'özlemek', sıfat 'parlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: güneş çok parlaktı ve baloncukların nereden geldiği görünmedi | şapkasını gözlerinin üstüne çekti ve kardeşini buldu
@tohum: sakir-0173
@degisim: özlemek -> üflemek
Şakir kumsalda kumdan bir kale yapıyordu. Birden havada küçük baloncuklar uçuştu. Şakir baloncukların nereden geldiğini merak etti ama güneş çok parlaktı. Şakir baloncukların geldiği yere baktı ama hiçbir şey göremedi. Sonra şapkasını gözlerinin üstüne biraz çekti. Şimdi her şeyi daha iyi görüyordu. Bir kayanın arkasında Canan'ın beyaz kuyruğu görünüyordu. Şakir kayaya doğru koştu. Canan orada oturmuş, elindeki şişeyle baloncuk üflüyordu. "Canan, baloncuklar senden mi geliyor?" diye sordu Şakir. "Evet, sen de dener misin?" dedi Canan. Şakir üfledi ve kocaman bir baloncuk yaptı. "Bu oyun çok güzel, Canan!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şakir baloncukların geldiği yere baktı"
   - Cümle 4: «Şakir baloncukların geldiği yere baktı ama hiçbir şey göremedi.»
   - Açıklama: Art arda iki cümle aynı 'Şakir baloncukların ... ama' kalıbını gereksiz tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0173` birebir aynı, `@degisim: özlemek -> üflemek` (tutuyorsan), ardından `@onarim: 8e7f4a3dfd57d4f578aaf8979f39d9920e27944a`, sonra gövde.

### Hikâye 8: tohum sakir-0183 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0183
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: kaybolan eşya
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'çörek', fiil 'boşalmak', sıfat 'heyecanlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: delik çantadan kitap ve çörekler yolda düştü | yoldan geri yürüdü ve kitabı buldu
@tohum: sakir-0183
Bir sabah Şakir ile Canan kumsalda yürüdü. Canan çok heyecanlıydı, çünkü kitabını denizin yanında okuyacaktı. Ama Canan'ın çantası delikti ve yolda boşalmıştı. Kitap da çörek paketi de kaybolmuştu. "Kitabım nerede, Şakir?" diye sordu Canan. "Yoldan geri yürüyelim, Canan," dedi Şakir. İkisi yavaş yavaş geri yürüdü. Şakir kumda çörek paketini buldu ve şapkasının içine koydu. Biraz ileride kitap kumun üstünde duruyordu. Şakir kitabı alıp Canan'a verdi. "Teşekkürler, Şakir, kitabım burada!" dedi Canan. Sonra ikisi kuma oturdu ve çörek yedi. Canan kitabını Şakir'e mutlu mutlu okudu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kitap ve çörekler yolda düştü"
   - Cümle 0 (plan satırı): «delik çantadan kitap ve çörekler yolda düştü | yoldan geri yürüdü ve kitabı buldu»
   - Açıklama: Yönelme eki gerekir; 'yola düştü' olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir ile Canan kumsalda yürüdü"
   - Cümle 1: «Bir sabah Şakir ile Canan kumsalda yürüdü.»
   - Açıklama: Güvenli kullanım satırına göre Şakir tek başına uzağa gitmez; iki küçük çocuk yetişkinsiz kumsalda.
   - Açıklama: Güvenli kullanım satırı tek başına uzağa gitmemeyi söylerken iki çocuk yetişkinsiz kumsalda ve yolda yürüyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çörek paketini buldu ve şapkasının içine koydu"
   - Cümle 8: «Şakir kumda çörek paketini buldu ve şapkasının içine koydu.»
   - Açıklama: Tohumdaki şapka özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.
   - Açıklama: Tohumdaki şapka özelliği sorunun çözümüne katkı vermeden yalnız kap olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0183` birebir aynı, ardından `@onarim: 20765bd3f95ed2bba3ef1a370b21042ae274c302`, sonra gövde.

### Hikâye 9: tohum sakir-0184 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0184
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'top', fiil 'tamamlamak', sıfat 'çamurlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: küçük bir kedi sudan çıkamıyordu | şapkasını suya uzatıp kediyi dışarı aldı
@tohum: sakir-0184
Şakir kamp yerinde annesi Kadriye ile top oynuyordu. Top çamurlu bir su birikintisinin yanına yuvarlandı. Küçük bir kedi çamurlu suya düşmüştü ve dışarı çıkamıyordu. "Anne, kedi sudan çıkamıyor!" dedi Şakir. Kadriye suya baktı. "Su çok çamurlu, içine basma, Şakir," dedi Kadriye. Şakir şapkasını çıkardı ve kenarını suya yavaşça değdirdi. Kedi hemen şapkanın içine girdi. Şakir şapkayı kaldırdı ve kediyi otların üstüne bıraktı. Kedi ağaçlara doğru koşup gitti. Sonra Şakir ve annesi top oyununu mutlu mutlu tamamladı.
```

**Hakem bulguları (6):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Küçük bir kedi çamurlu suya düşmüştü"
   - Cümle 3: «Küçük bir kedi çamurlu suya düşmüştü ve dışarı çıkamıyordu.»
   - Açıklama: Suya düşüp çıkamayan yavru hayvan küçük çocuk için korkutucu bir tehlike sahnesi.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Küçük bir kedi çamurlu suya düşmüştü"
   - Cümle 3: «Küçük bir kedi çamurlu suya düşmüştü ve dışarı çıkamıyordu.»
   - Açıklama: Başlıktaki Yan alanında yalnız Kadriye var; isimsiz kedi olaya katılan ek bir yan karakter.
   - Açıklama: Başlığın Yan alanında yalnız Kadriye var; olaya katılan kedi kartın yanlar bölümünde yok.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Küçük bir kedi çamurlu suya düşmüştü"
   - Cümle 3: «Küçük bir kedi çamurlu suya düşmüştü ve dışarı çıkamıyordu.»
   - Açıklama: Kartın yanlar bölümünde olmayan bir kedi karakter olarak hikayeye giriyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Küçük bir kedi çamurlu suya düşmüştü ve dışarı çıkamıyordu"
   - Cümle 3: «Küçük bir kedi çamurlu suya düşmüştü ve dışarı çıkamıyordu.»
   - Açıklama: Kedinin bir su birikintisinden neden çıkamadığı söylenmiyor ve akla yatkın değil.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Küçük bir kedi çamurlu suya düşmüştü"
   - Cümle 3: «Küçük bir kedi çamurlu suya düşmüştü ve dışarı çıkamıyordu.»
   - Açıklama: Bir kedinin küçük bir su birikintisinden neden çıkamadığı söylenmiyor ve akla yatkın değil.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kenarını suya yavaşça değdirdi"
   - Cümle 7: «Şakir şapkasını çıkardı ve kenarını suya yavaşça değdirdi.»
   - Açıklama: Çocuk su birikintisine düşmüş bir hayvanı kurtarmak için suya uzanmayı taklit edebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0184` birebir aynı, ardından `@onarim: 0c0477b4f1249dd8bf38f3a200482d0007af85e5`, sonra gövde.

### Hikâye 10: tohum sakir-0187 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0187
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sırayla oynamak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'papatya', fiil 'güldürmek', sıfat 'kabarık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: ikisi aynı anda konuşunca kimse kimseyi duymadı | şapka kimde olursa sıranın onda olduğunu söyledi
@tohum: sakir-0187
Rüzgar esiyordu ve havada kabarık bulutlar vardı. Şakir ile Fil Necati kamp yerinde komik bir oyun oynuyordu. Ama ikisi aynı anda konuştu ve kimse kimseyi duymadı. Şakir şapkasını çıkardı ve Necati'ye uzattı. "Şapka sende olunca sıra sende, Necati," dedi Şakir. Necati şapkayı kocaman başına taktı. Sonra kulağına bir papatya taktı. "Bak, Şakir, ben çiçekli bir filim!" dedi Necati. Şakir çok güldü. Sonra Necati şapkayı Şakir'e geri verdi. Şakir komik bir aslan sesi çıkardı ve Necati'yi güldürdü. Necati hortumunu salladı ve kahkaha attı. Şakir çok sevindi, çünkü sırayla oynadıkları için ikisi de çok eğlenmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra kulağına bir papatya taktı"
   - Cümle 7: «Sonra kulağına bir papatya taktı.»
   - Açıklama: Papatya sebepsiz beliriyor ve sorunla ilgili bir işe yaramıyor.
   - Açıklama: Papatya sebepsiz beliriyor ve sorunla ya da çözümle hiçbir ilgisi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0187` birebir aynı, ardından `@onarim: 50e6072b3061de778312e61115410490f86717ae`, sonra gövde.

### Hikâye 11: tohum sakir-0189 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0189
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ekmek', fiil 'sığmak', sıfat 'hafif'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: hafif tüy rüzgarla uçuyor ve elinden kaçıyordu | şapkasını tüyün altında tuttu ve tüy içine düştü
@tohum: sakir-0189
@degisim: ekmek -> tüy
Şakir annesi Kadriye ile kumsalda yürürken havada bembeyaz bir tüy gördü. Şakir tüyü yakalamak istedi ama tüy hep elinden kaçtı. Tüy çok hafifti ve rüzgarla bir yukarı, bir aşağı uçuyordu. "Anne, bu tüyü yakalayamıyorum!" dedi Şakir. Sonra Şakir şapkasını çıkardı ve tüyün altında tuttu. Tüy yavaşça aşağı indi ve geniş şapkanın içine rahatça sığdı. Şakir tüyü annesine verdi. "Teşekkürler, Şakir, bu çok güzel bir hediye," dedi Kadriye. Şakir çok sevindi, çünkü tüyü sonunda yakalamıştı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkanın içine rahatça sığdı"
   - Cümle 6: «Tüy yavaşça aşağı indi ve geniş şapkanın içine rahatça sığdı.»
   - Açıklama: Küçük tüy için 'rahatça sığdı' yanlış fiil; 'düştü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0189` birebir aynı, `@degisim: ekmek -> tüy` (tutuyorsan), ardından `@onarim: 598764ed9b6715898876ae1e0d94c0d8b5ab0adc`, sonra gövde.

### Hikâye 12: tohum sakir-0192 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0192
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'sucuk', fiil 'taramak', sıfat 'faydalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: güneş çok parlaktı ve hazinenin yanındaki dal görünmedi | şapkasını gözlerinin üstüne çekti ve kumsalı taradı
@tohum: sakir-0192
@degisim: faydalı -> parlak
Bir sabah Şakir kumsalda babası Remzi ile hazine oyunu oynuyordu. Remzi hazineyi kuma gömmüş ve yanına bir dal dikmişti. Ama güneş çok parlaktı ve Şakir dalı göremedi. "Hazineyi bul, Şakir!" dedi Remzi. Şakir şapkasını gözlerinin üstüne indirdi. Artık gözleri gölgede kaldı. Şakir bütün kumsalı yavaş yavaş taradı. Sonunda kumsalın ucunda küçük dalı gördü. Hemen oraya koştu ve dalın dibini kazdı. Kumun altından bir kutu çıktı. Kutunun içinde iki sucuklu ekmek vardı. "Hazineyi buldum, baba!" dedi Şakir. İkisi kuma oturdu ve ekmekleri afiyetle yedi. Şakir bundan sonra güneşte uzağa bakarken gözlerini hep gölgede tuttu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bütün kumsalı yavaş yavaş taradı"
   - Cümle 7: «Şakir bütün kumsalı yavaş yavaş taradı.»
   - Açıklama: 'Taramak' gözle bakma anlamında mecazlı kullanılmış, küçük çocuk bilmez.
   - Açıklama: 'Taramak' bakmak anlamında mecazlı, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0192` birebir aynı, `@degisim: faydalı -> parlak` (tutuyorsan), ardından `@onarim: 6fb17338a977617b71b9384260f3f13909d1e5aa`, sonra gövde.
