# Editör görevi (onarım): Şakir, onarım partisi 6

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar6.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar6.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0001 (deneme 3 -> 4)

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
Şakir babası Remzi ile salonda bilye oynuyordu. Remzi'nin kocaman mavi bilyesi yuvarlandı ve dolabın altına girdi. Remzi eğildi ama kalın kolu oraya sığmadı. "Bilyemi alamıyorum, Şakir," dedi Remzi. "Ben alırım, baba," dedi Şakir. Macerayı çok seven Şakir hemen yere uzandı. Dolabın altını dikkatle inceledi. Mavi bilye en arkada duruyordu. Şakir'in küçük eli içeri rahatça girdi. Bilyeyi parmaklarıyla tuttu ve yavaşça dışarı çekti. Sonra onu babasına verdi. Remzi sevinçle güldü ve Şakir'e sarıldı. "Teşekkürler, Şakir, şimdi oyunumuza devam edelim!" dedi Remzi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 6: «Macerayı çok seven Şakir hemen yere uzandı.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0001` birebir aynı, ardından `@onarim: bbdc8031498cb5ee035f90e0408759da9ee0d0c7`, sonra gövde.

### Hikâye 2: tohum sakir-0003 (deneme 3 -> 4)

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
Şakir eski bir ayakkabı kutusundan davul yapmak istedi. Kutuya eliyle vurdu ama sesi zor duydu. Kutunun içi kağıtlarla dolu olduğu için davul iyi ses çıkarmıyordu. Şakir macerayı çok severdi ve kapağı hemen açıp içine baktı. Kağıtları tek tek çıkardı ve bir kenara koydu. Sonra kapağı sıkıca kapattı. Davuluna yeniden vurdu. Bu kez yüksek ve güzel bir ses çıktı. Şakir masasından iki kalem aldı. Onlarla davulu hızlı hızlı çaldı. Şakir bu sesi çok beğendi ve güldü. Yeni davulunu mutlu mutlu çalmaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi ve kapağı hemen açıp içine baktı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve kapağı hemen açıp içine baktı"
   - Cümle 4: «Şakir macerayı çok severdi ve kapağı hemen açıp içine baktı.»
   - Açıklama: Tohumdaki macera özelliği kutunun kapağını açmaya işe yarar bir bağ kurmadan yalnızca söylenmiş.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi ve kapağı hemen açıp içine baktı.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenip geçiliyor, kutunun içine bakmak kartın macera özelliğini işe yarar biçimde kullanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0003` birebir aynı, `@degisim: kütük -> kutu` (tutuyorsan), ardından `@onarim: d43bcae30f1324fc1237446929ba5edd057d168a`, sonra gövde.

### Hikâye 3: tohum sakir-0012 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0012
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kurdele', fiil 'kullanmak', sıfat 'ucuz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: rüzgar yapraktan bayrağı çubuktan uçuruyordu | şapkasındaki kurdeleyle yaprağı çubuğa bağladı
@tohum: sakir-0012
@degisim: ucuz -> kırmızı
Rüzgar ağaçların arasında esiyordu. Şakir kamp yerinde gemi oyunu oynuyordu. Ama rüzgar, gemisinin yapraktan bayrağını çubuktan durmadan uçuruyordu. Şakir'in gemisi, yerde yatan kalın bir kütüktü. Şakir yeşil yaprağı yerden aldı ve biraz düşündü. Sonra şapkasındaki kırmızı kurdeleyi çözdü. Kurdeleyi ip gibi kullandı ve yaprağı çubuğa sıkıca bağladı. Az sonra hava yine esti. Bu kez yaprak uçmadı, çubuğun ucunda dalgalandı. Şakir çubuğu kütüğün yanındaki toprağa dikti. Sonra gemisinin üstüne oturdu ve bayrağına uzun uzun baktı. Şakir çok sevindi, çünkü bayrak sonunda yerinde duruyordu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Az sonra hava yine esti"
   - Cümle 8: «Az sonra hava yine esti.»
   - Açıklama: Hava esmez, rüzgar eser; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0012` birebir aynı, `@degisim: ucuz -> kırmızı` (tutuyorsan), ardından `@onarim: 13ccfb407fc8aea543e983f01f8caed95cdce8af`, sonra gövde.

### Hikâye 4: tohum sakir-0018 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0018
- yer: park (Şehirdeki park.)
- tema: sırayla oynamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bileklik', fiil 'karıştırmak', sıfat 'pürüzsüz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: ikisi aynı anda attı ve taşlar karıştı | sırayla atmayı önerdi ve taşları tek tek attılar
@tohum: sakir-0018
@degisim: bileklik -> taş
Şakir parkta şapkasını çimenlerin üstüne koydu. Annesi Kadriye ile şapkanın içine pürüzsüz taşlar atmaya başladılar. Ama ikisi hep aynı anda attı ve taşları karıştırdılar. Şakir şapkanın içindeki taşlara baktı ve düşündü. "Anne, sırayla atalım mı?" diye sordu Şakir. "Olur, önce sen at," dedi Kadriye. Şakir bir taş attı ve taş şapkanın içine düştü. Sonra Kadriye attı, onun taşı da içeri girdi. İkisi taşları tek tek, sırayla atmaya devam etti. Artık her taşı kimin attığı belliydi. Kadriye her sayıda ellerini çırptı. Şakir çok sevindi, çünkü sırayla oynayınca oyun daha güzel olmuştu.
```

**Hakem bulguları (8):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir parkta şapkasını çimenlerin üstüne koydu"
   - Cümle 1: «Şakir parkta şapkasını çimenlerin üstüne koydu.»
   - Açıklama: Tohumdaki şapka özelliği yalnız hedef kap olarak defalarca geçiyor, çözüm olan sırayla atmada işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir parkta şapkasını çimenlerin"
   - Cümle 1: «Şakir parkta şapkasını çimenlerin üstüne koydu.»
   - Açıklama: Tohumdaki şapka özelliği yalnız taş atma hedefi olarak geçiyor, sorunun çözümünde (sırayla atma) işe yaramıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şapkanın içine pürüzsüz taşlar"
   - Cümle 2: «Annesi Kadriye ile şapkanın içine pürüzsüz taşlar atmaya başladılar.»
   - Açıklama: 'Pürüzsüz' 3 yaşındaki bir çocuğun bileceği bir kelime değil.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ikisi hep aynı anda attı ve taşları karıştırdılar"
   - Cümle 3: «Ama ikisi hep aynı anda attı ve taşları karıştırdılar.»
   - Açıklama: Aynı özne 'ikisi' için tekil 'attı' ile çoğul 'karıştırdılar' arasında uyum bozuk.
   - Açıklama: Aynı cümlede 'ikisi attı' tekil, 'karıştırdılar' çoğul çekimlenmiş; uyum tutarsız.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi hep aynı anda attı ve taşları karıştırdılar"
   - Cümle 3: «Ama ikisi hep aynı anda attı ve taşları karıştırdılar.»
   - Açıklama: Taşların karışması belirsiz ve önemsiz bir sorun; neyin bozulduğu çocuğa açık değil.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kadriye her sayıda ellerini çırptı"
   - Cümle 11: «Kadriye her sayıda ellerini çırptı.»
   - Açıklama: 'Her sayıda' yanlış anlamda; 'her atışta' olmalı.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kadriye her sayıda ellerini"
   - Cümle 11: «Kadriye her sayıda ellerini çırptı.»
   - Açıklama: 'Her sayıda' yanlış anlamda; 'her atışta' olmalı.
8. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kadriye her sayıda ellerini çırptı"
   - Cümle 11: «Kadriye her sayıda ellerini çırptı.»
   - Açıklama: Hikayede hiç sayı ya da sayma kurulmamışken sayı sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0018` birebir aynı, `@degisim: bileklik -> taş` (tutuyorsan), ardından `@onarim: 3a53ffb912d7bedc983d27013e25fb84658ff458`, sonra gövde.

### Hikâye 5: tohum sakir-0021 (deneme 1 -> 2)

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
Bir sabah Şakir ile Necati kamp yerinde küçük bir maceraya çıkmıştı. Ama Necati'nin karnı acıkmıştı ve yanında hiç yiyecek yoktu. Şakir'in çantasında, bir beze sardığı ılık bir simit vardı. Şakir simidi çıkardı ve bezi açtı. Sonra simidi iki eşit parçaya böldü. "Necati, bu yarısı senin," dedi Şakir. Necati simidi hortumuyla aldı. "Teşekkür ederim, Şakir, çok acıkmıştım," dedi Necati. İkisi bir kütüğün üstüne oturdu ve simidi birlikte yedi. Necati her lokmada hortumunu salladı. Şakir buna çok güldü. Şakir çok sevindi, çünkü simidini paylaşınca ikisinin de karnı doymuştu.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir maceraya çıkmıştı"
   - Cümle 1: «Bir sabah Şakir ile Necati kamp yerinde küçük bir maceraya çıkmıştı.»
   - Açıklama: 'Macera' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "küçük bir maceraya çıkmıştı"
   - Cümle 1: «Bir sabah Şakir ile Necati kamp yerinde küçük bir maceraya çıkmıştı.»
   - Açıklama: Tohumdaki macera özelliği yalnız açılışta anılıyor, simidi paylaşma çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "küçük bir maceraya çıkmıştı"
   - Cümle 1: «Bir sabah Şakir ile Necati kamp yerinde küçük bir maceraya çıkmıştı.»
   - Açıklama: Macera kurulup hiç kullanılmıyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Necati, bu yarısı senin"
   - Cümle 6: «"Necati, bu yarısı senin," dedi Şakir.»
   - Açıklama: 'Bu yarısı' dilbilgisel değil; 'bu yarı senin' ya da 'yarısı senin' olmalı.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ikisinin de karnı doymuştu"
   - Cümle 12: «Şakir çok sevindi, çünkü simidini paylaşınca ikisinin de karnı doymuştu.»
   - Açıklama: Bir fil yarım simitle doymuş gösteriliyor, bu akla aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0021` birebir aynı, ardından `@onarim: e2d34fb6200c1b7865000aa9210b28889ac71038`, sonra gövde.

### Hikâye 6: tohum sakir-0024 (deneme 1 -> 2)

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
@plan: koşarken sebze sepetine çarptı ve sebzeler döküldü | kardeşinden özür dileyip sebzeleri topladı
@tohum: sakir-0024
@degisim: pahalı -> dolu
Evde Şakir büyük bir macera oyunu oynuyordu. Mutfakta hızlı hızlı yürürken önüne bakmadı. Canan'ın masadaki dolu sebze sepetine çarptı ve sebzeler yere döküldü. Canan onları az önce sepete koymuştu. Kardeşi üzüldü ve yere baktı. Şakir hemen durdu. "Özür dilerim, Canan, önüme bakmadım," dedi Şakir. Sonra yere eğildi ve havuçları, domatesleri tek tek topladı. Canan da ona yardım etti. Kısa sürede sepet yine doldu. "Tamam, Şakir, birlikte hepsini topladık," dedi Canan ve gülümsedi. Şakir çok rahatladı, çünkü kardeşi ona artık kızgın değildi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük bir macera oyunu"
   - Cümle 1: «Evde Şakir büyük bir macera oyunu oynuyordu.»
   - Açıklama: 'Macera' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Evde Şakir büyük bir macera oyunu oynuyordu"
   - Cümle 1: «Evde Şakir büyük bir macera oyunu oynuyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız anılıyor ve sorunu doğuruyor, çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0024` birebir aynı, `@degisim: pahalı -> dolu` (tutuyorsan), ardından `@onarim: c434e9307af42f58731fbc3497dcaa78d3d1c45f`, sonra gövde.

### Hikâye 7: tohum sakir-0025 (deneme 1 -> 2)

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
@plan: çiçeklerden yapılan taç çok büyük olmuştu | tacın bir parçasını kopardı ve tacı küçülttü
@tohum: sakir-0025
@degisim: piyano -> çiçek
Şakir, kamp yerinde annesi Kadriye için bir sürpriz hazırlıyordu. Şapkasını çiçeklerle doldurmuş, onlardan bir taç yapmıştı. Ama uzun saplar yüzünden taç çok büyük olmuştu. Şakir tacın bir parçasını kopardı ve tacı küçülttü. Sonra tacı arkasına sakladı ve annesinin yanına koştu. "Anne, gözlerini kapar mısın?" diye sordu Şakir. Kadriye gülümsedi ve gözlerini kapadı. Şakir çiçekli tacı annesinin başına yavaşça koydu. Taç tam oldu, hiç kaymadı. Kadriye gözlerini açtı ve tacı eliyle tuttu. "Ne güzel bir sürpriz, Şakir, ben çok şanslı bir anneyim!" dedi Kadriye.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şapkasını çiçeklerle doldurmuş, onlardan bir taç yapmıştı"
   - Cümle 2: «Şapkasını çiçeklerle doldurmuş, onlardan bir taç yapmıştı.»
   - Açıklama: Tohumdaki şapka özelliği yalnız çiçek kabı olarak geçiyor, sorunun çözümünde (tacı küçültme) işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şapkasını çiçeklerle doldurmuş"
   - Cümle 2: «Şapkasını çiçeklerle doldurmuş, onlardan bir taç yapmıştı.»
   - Açıklama: Tohumdaki şapka özelliği yalnız çiçek kabı olarak geçiyor, tacı küçültme çözümünde işe yaramıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "tacın bir parçasını kopardı"
   - Cümle 4: «Şakir tacın bir parçasını kopardı ve tacı küçülttü.»
   - Açıklama: Sorunun sebebi uzun saplar ama çözüm sapları değil tacın rastgele bir parçasını koparıyor ve halkanın nasıl kapandığı belirsiz.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben çok şanslı bir anneyim"
   - Cümle 11: «"Ne güzel bir sürpriz, Şakir, ben çok şanslı bir anneyim!" dedi Kadriye.»
   - Açıklama: 'Şanslı' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0025` birebir aynı, `@degisim: piyano -> çiçek` (tutuyorsan), ardından `@onarim: 80e13cd30f298f1ce5b232c3d83d136ee5e22eac`, sonra gövde.
