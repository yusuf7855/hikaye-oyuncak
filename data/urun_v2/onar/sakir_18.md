# Editör görevi (onarım): Şakir, onarım partisi 18

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar18.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar18.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0026 (deneme 5 -> 6)

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
@plan: palmiyeler arasında rüzgar güçlü değildi | açık bir yere koşup ipi sıkıca tuttu
@tohum: sakir-0026
@degisim: yeterli -> güçlü
Şakir, babası Remzi ile kumsalda ilk kez uçurtma uçuracaktı. Remzi ona mavi bir uçurtma verdi. Ama palmiyeler arasında rüzgar güçlü değildi ve uçurtma hep kuma düştü. Şakir rüzgarlı bir yer bulmak istedi. Etrafına baktı ve deniz kenarında açık bir yer gördü. Macerayı çok seven Şakir babasının eline tutunarak oraya koştu. Orada rüzgar daha güçlüydü. Şakir ipi iki eliyle sıkıca tuttu. Remzi de uçurtmayı havaya bıraktı. Mavi uçurtma hızla yükseldi ve ağaçların üstüne çıktı. Remzi sevinçle zıplayıp güldü. "Babacığım, ilk uçurtmam gökyüzünde uçuyor!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 6: «Macerayı çok seven Şakir babasının eline tutunarak oraya koştu.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir babasının eline tutunarak"
   - Cümle 6: «Macerayı çok seven Şakir babasının eline tutunarak oraya koştu.»
   - Açıklama: Tohumdaki macera özelliği bir sıfat gibi sayılıyor, çözüme işe yarar biçimde katılmıyor.
   - Açıklama: Tohumdaki macera özelliği süs olarak anılıyor, çözümde işlevi yok.
   - Açıklama: Tohumdaki macera özelliği süs olarak anılıyor, sorunun çözümüne katkısı yok; kartın özellikler alanındaki gibi işe yarar kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0026` birebir aynı, `@degisim: yeterli -> güçlü` (tutuyorsan), ardından `@onarim: 6852b4db644e2c5ddfa03951d7126e280f59581c`, sonra gövde.

### Hikâye 2: tohum sakir-0027 (deneme 5 -> 6)

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
@plan: kardeşi kitabını unuttuğu için oynayacak bir şeyi yoktu | çantanın ipini çözdü ve ikinci küreği paylaştı
@tohum: sakir-0027
@degisim: süpürge -> kürek
Rüzgar hafif hafif esiyordu. Şakir kumsalda küreğiyle büyük bir kale yapıyordu. Kardeşi Canan kitabını evde unuttuğu için oynayacak bir şeyi yoktu. Canan kumun üstünde sessiz oturuyordu. Şakir'in oyuncak çantasında bir kürek daha vardı. Şakir çantanın ipini çözdü ve ikinci küreği çıkardı. "Canan, bu kürek senin olsun, gel birlikte kazalım!" dedi Şakir. "Ne yapacağız?" diye sordu Canan. "Kalenin etrafına uzun bir macera yolu kazalım!" dedi Şakir. Canan küreği aldı ve gülümsedi. İkisi yan yana kumu kazdı. Sonunda yol kalenin etrafını tam sardı. Şakir ile Canan, kalelerinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "uzun bir macera yolu"
   - Cümle 9: «"Kalenin etrafına uzun bir macera yolu kazalım!" dedi Şakir.»
   - Açıklama: 'Macera' soyut bir kelime, 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Macera yolu' soyut bir ifade, küçük çocuk için uygun değil.
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Şakir ile Canan, kalelerinin"
   - Cümle 13: «Şakir ile Canan, kalelerinin yanında mutlu mutlu oynamaya devam etti.»
   - Açıklama: Özne ile yüklem arasına gereksiz virgül konmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0027` birebir aynı, `@degisim: süpürge -> kürek` (tutuyorsan), ardından `@onarim: 17e381b45f7dbee8b59798a44899e7c9e7655f5b`, sonra gövde.

### Hikâye 3: tohum sakir-0028 (deneme 5 -> 6)

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
Kumsalda Fil Necati büyük bir şemsiyenin altında uyuyordu. Şakir ona sürpriz olarak kumdan bir pasta yaptı ve üstüne kabuklar dizdi. Ama pastanın mumu eksikti ve kumsalda hiç mum yoktu. Şakir mum yerine uzun ve ince bir şey bulmak istedi. Şakir macerayı çok severdi ve şemsiyenin çevresini adım adım gezdi. Sonunda kumun üstünde uzun, beyaz bir tüy buldu. Tüyü pastanın tam ortasına dikti. Şimdi pasta tamamdı. Biraz sonra Necati uyandı ve pastayı gördü. Hortumuyla tüye yavaşça dokundu ve gülümsedi. Şakir de sevinçle ellerini çırptı. Şakir bundan sonra bir şey eksik olunca önce etrafına dikkatle baktı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi ve şemsiyenin çevresini adım adım gezdi.»
   - Açıklama: 'Macera' soyut bir kavram ve olaya bağlanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0028` birebir aynı, ardından `@onarim: da7bd13ed5e126e07e87ef9eaa5dbad57a88310a`, sonra gövde.

### Hikâye 4: tohum sakir-0029 (deneme 5 -> 6)

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
@plan: rüzgar oyunun haritasını uçurdu | babasından yardım istedi ve sarı kutuyu buldu
@tohum: sakir-0029
@degisim: tuzlu -> sarı
Parkta Şakir ile babası Remzi bir macera oyunu oynuyordu. Remzi içinde kek olan sarı bir kutuyu saklamış ve bir harita çizmişti. Ama rüzgar esti ve harita uçup gitti. Şakir hiç üzülmedi ve oyunu bırakmadı. "Baba, yaklaşınca 'sıcak', uzaklaşınca 'soğuk' der misin?" diye sordu Şakir. "Tamam, haydi başla!" dedi Remzi gülerek. Şakir parkta gezinmeye başladı. "Soğuk, çok soğuk!" dedi Remzi ve titriyormuş gibi yaptı. Şakir döndü ve banklara doğru yürüdü. "Sıcak, çok sıcak!" dedi Remzi. Şakir bankın altına baktı ve sarı kutuyu buldu. Sonra ikisi banka oturdu ve keki mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir macera oyunu oynuyordu"
   - Cümle 1: «Parkta Şakir ile babası Remzi bir macera oyunu oynuyordu.»
   - Açıklama: 'Macera' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0029` birebir aynı, `@degisim: tuzlu -> sarı` (tutuyorsan), ardından `@onarim: bfde4241ce0dd0f92c9c52f5d113214c196fe3f5`, sonra gövde.

### Hikâye 5: tohum sakir-0031 (deneme 5 -> 6)

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
@plan: fil ağır adımlarla küçük çiçeğe doğru geliyordu | fili durdurup çiçeğin etrafına taş dizdi
@tohum: sakir-0031
@degisim: patates -> çiçek
Bir sabah Şakir ile Fil Necati parkta yürüyordu. Şakir yolun ortasında küçük bir çiçek gördü. Çiçeğin sapı çok ince ve kırılgandı, bir basınca hemen kırılırdı. Ama Necati ağır adımlarla tam çiçeğe doğru geliyordu. "Dur, Necati, sana bir çiçek göstermek istiyorum!" dedi Şakir. Necati durdu ve eğilip çiçeğe baktı. "Onu hiç görmemiştim," dedi Necati. Şakir çiçeği korumak istedi. Macerayı çok seven Şakir çalıların arasına girdi ve dört taş buldu. Taşları çiçeğin etrafına dizdi. Şimdi çiçek uzaktan kolayca görünüyordu. Necati yavaş yavaş yürüdü ve çiçeğin yanından dikkatle geçti. "Artık çiçeğe kimse basmaz, Necati!" dedi Şakir sevinçle.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bir basınca hemen kırılırdı"
   - Cümle 3: «Çiçeğin sapı çok ince ve kırılgandı, bir basınca hemen kırılırdı.»
   - Açıklama: Özne eksik ve bozuk; 'biri basınca' olmalı.
   - Açıklama: 'Bir basınca' dilbilgisel değil; 'biri basınca' olmalı.
   - Açıklama: 'Bir basınca' dilbilgisel olarak tuhaf; 'basınca' fiil gibi okunuyor, 'birisi basınca' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çok ince ve kırılgandı"
   - Cümle 3: «Çiçeğin sapı çok ince ve kırılgandı, bir basınca hemen kırılırdı.»
   - Açıklama: 'Kırılgan' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir basınca hemen kırılırdı"
   - Cümle 3: «Çiçeğin sapı çok ince ve kırılgandı, bir basınca hemen kırılırdı.»
   - Açıklama: 'Basınç' ve 'kırılgan' soyut kelimeler, 3 yaşındaki çocuk bilmez.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama Necati ağır adımlarla tam çiçeğe doğru geliyordu"
   - Cümle 4: «Ama Necati ağır adımlarla tam çiçeğe doğru geliyordu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 9: «Macerayı çok seven Şakir çalıların arasına girdi ve dört taş buldu.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 9: «Macerayı çok seven Şakir çalıların arasına girdi ve dört taş buldu.»
   - Açıklama: Özellik kartın özellik satırı aynen sayılarak ekleniyor, çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0031` birebir aynı, `@degisim: patates -> çiçek` (tutuyorsan), ardından `@onarim: b42187f45b76a91daa4e6651c18fa90d56180f29`, sonra gövde.

### Hikâye 6: tohum sakir-0033 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0033
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'pota', fiil 'üflemek', sıfat 'ahşap'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: üflerken topun havası geri kaçıyordu | kardeşinden topun ağzını tutmasını istedi
@tohum: sakir-0033
@degisim: pota -> top
Kumsalda Şakir ile Canan ahşap oyuncak kutusunu açtı. İçinden havası inmiş mavi bir deniz topu çıktı. Şakir topa üfledi, ama nefes alırken hava hep geri kaçtı. Şakir bu topla bir macera oyunu oynamak istiyordu. "Canan, ben nefes alırken topun ağzını tutar mısın?" diye sordu Şakir. "Tabii, tutarım," dedi Canan. Şakir yine üfledi ve nefes aldı. O sırada Canan topun ağzını parmağıyla kapattı. Böylece hava hiç kaçmadı. Top yavaş yavaş büyüdü ve yuvarlak oldu. Sonunda Şakir topun ağzını sıkıca kapattı. "Teşekkürler, Canan, şimdi birlikte oynayabiliriz!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir macera oyunu oynamak"
   - Cümle 4: «Şakir bu topla bir macera oyunu oynamak istiyordu.»
   - Açıklama: 'macera' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir bu topla bir macera oyunu"
   - Cümle 4: «Şakir bu topla bir macera oyunu oynamak istiyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak geçiyor, topu şişirme çözümünde işlevi yok.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bu topla bir macera oyunu"
   - Cümle 4: «Şakir bu topla bir macera oyunu oynamak istiyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız anılıyor, çözüm Canan'ın topun ağzını tutmasıyla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0033` birebir aynı, `@degisim: pota -> top` (tutuyorsan), ardından `@onarim: 8f5174d7bcf233c143d846929c7380689989df99`, sonra gövde.

### Hikâye 7: tohum sakir-0034 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Canan
@tohum: sakir-0034
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tartı', fiil 'ısınmak', sıfat 'şekerli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | ev | Canan
@plan: uğur böcekleri tartıya ters düştü ve dönemedi | yaprak uzatıp böcekleri güneşe taşıdı
@tohum: sakir-0034
@degisim: şekerli -> yeşil
Şakir mutfakta kardeşi Canan ile birlikteydi. Şakir macerayı çok severdi, bu yüzden her köşeye dikkatle bakıyordu. Birden tartının üstünde ters dönmüş minik uğur böcekleri gördü. Böcekler pencerenin önündeki çiçekten tartıya düşmüştü ve dönemiyordu. "Canan, onlara nasıl yardım ederiz?" diye sordu Şakir. "Onlara bir yaprak uzat, yaprağı tutarlar," dedi Canan. Şakir o çiçekten yeşil bir yaprak kopardı. Yaprağı böceklerin ayaklarına yavaşça yaklaştırdı. Böcekler yaprağa tutundu ve döndü. Şakir yaprağı güneşli pencerenin önüne koydu. Uğur böcekleri güneşte ısındı ve kanatlarını açtı. Sonra uçup yine çiçeğe kondular. "Teşekkürler, Canan, böceklere birlikte yardım ettik!" dedi Şakir.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 2: «Şakir macerayı çok severdi, bu yüzden her köşeye dikkatle bakıyordu.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 2: «Şakir macerayı çok severdi, bu yüzden her köşeye dikkatle bakıyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız anılıyor, böceklere yardım çözümünde işe yaramıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Böcekler pencerenin önündeki çiçekten tartıya düşmüştü"
   - Cümle 4: «Böcekler pencerenin önündeki çiçekten tartıya düşmüştü ve dönemiyordu.»
   - Açıklama: Birden çok uğur böceğinin aynı anda çiçekten tartıya ters düşmesi akla yatkın bir sebep değil.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Böcekler yaprağa tutundu ve döndü"
   - Cümle 9: «Böcekler yaprağa tutundu ve döndü.»
   - Açıklama: Notlanan çoğul canlı uğur böcekleri arka planda kalmıyor, olaya katılıyor.
5. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Böcekler yaprağa tutundu"
   - Cümle 9: «Böcekler yaprağa tutundu ve döndü.»
   - Açıklama: Çoğul canlı uğur böcekleri arka planda kalmıyor, olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0034` birebir aynı, `@degisim: şekerli -> yeşil` (tutuyorsan), ardından `@onarim: 47e7cd42c42dbafa3ae80f0ed263234591ff61eb`, sonra gövde.

### Hikâye 8: tohum sakir-0035 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0035
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'mürekkep', fiil 'bağlamak', sıfat 'üzgün'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: kalemin mürekkebi birden bitti | kalemini paylaştı ve ikisi sırayla çizdi
@tohum: sakir-0035
@degisim: bağlamak -> paylaşmak
Şakir, Necati ile kamp yerinde bir orman haritası çiziyordu. Necati büyük ağaçları çizecekti. Ama Necati'nin kaleminin mürekkebi birden bitti. Necati üzgün bir yüzle kalemine baktı. "Kalemim artık çizmiyor," dedi Necati. Şakir bu haritayla bir macera oyunu oynamak istiyordu. Şakir'in tek bir kırmızı kalemi vardı. Şakir bu kalemi hemen Necati'ye uzattı. "Kalemimi seninle paylaşırım, sırayla çizelim," dedi Şakir. Önce Necati ağaçları çizdi. Sonra Şakir çadırı ve yolu çizdi. Harita bitince Şakir ile Necati onu alıp kamp yerini mutlu mutlu gezdi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir macera oyunu oynamak"
   - Cümle 6: «Şakir bu haritayla bir macera oyunu oynamak istiyordu.»
   - Açıklama: 'Macera' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir bu haritayla bir macera oyunu oynamak istiyordu"
   - Cümle 6: «Şakir bu haritayla bir macera oyunu oynamak istiyordu.»
   - Açıklama: Macera oyunu işe yarayacakmış gibi kuruluyor ama hikayede hiç oynanmıyor ve sorunun çözümüyle ilgisi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0035` birebir aynı, `@degisim: bağlamak -> paylaşmak` (tutuyorsan), ardından `@onarim: dcad6ac749485901305e0dc9f588170420aa265e`, sonra gövde.

### Hikâye 9: tohum sakir-0039 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0039
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'fide', fiil 'çekinmek', sıfat 'dolu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: su dolu kova çok ağırdı ve kaldıramadı | annesinden yardım isteyip kovayı birlikte taşıdı
@tohum: sakir-0039
@degisim: fide -> fidan
Bir sabah Şakir kamp yerinde küçük bir fidan dikti. Şakir fidanı kendisi sulamak istedi. Ama su dolu kova çok ağırdı ve Şakir onu kaldıramadı. Annesi Kadriye çadırın önünde oturuyordu. Şakir hiç çekinmedi ve annesinin yanına koştu. "Anne, bir macera oyunu oynayalım, kovayı birlikte taşır mıyız?" diye sordu Şakir. "Tabii, hemen geliyorum," dedi Kadriye. İkisi kovayı iki yanından tuttu ve fidanın yanına taşıdı. Şakir suyu fidana yavaş yavaş döktü. Kuru toprak ıslandı ve fidanın yaprakları parladı. "Teşekkürler, anneciğim, fidan artık susuz değil!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir macera oyunu oynayalım"
   - Cümle 6: «"Anne, bir macera oyunu oynayalım, kovayı birlikte taşır mıyız?" diye sordu Şakir.»
   - Açıklama: 'macera' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime ve kova taşımaya uymuyor.
   - Açıklama: 'Macera oyunu' soyut bir kavram ve kova taşımakla uyuşmuyor, küçük çocuk için anlaşılır değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bir macera oyunu oynayalım"
   - Cümle 6: «"Anne, bir macera oyunu oynayalım, kovayı birlikte taşır mıyız?" diye sordu Şakir.»
   - Açıklama: Tohumdaki macera özelliği yalnız bir etiket olarak ekleniyor; kovayı taşımayı yardım istemek çözüyor, macera işe yarar biçimde kullanılmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir macera oyunu oynayalım"
   - Cümle 6: «"Anne, bir macera oyunu oynayalım, kovayı birlikte taşır mıyız?" diye sordu Şakir.»
   - Açıklama: Kovayı taşımanın macera oyunu diye sunulması olaya bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0039` birebir aynı, `@degisim: fide -> fidan` (tutuyorsan), ardından `@onarim: 4e958bb85664ce655a66c1a6ec06543feeb6ae9c`, sonra gövde.

### Hikâye 10: tohum sakir-0042 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0042
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kamyon', fiil 'yollamak', sıfat 'taze'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: oyuncak kamyon kumdaki çukura girdi ve takıldı | kamyonu çıkarıp çukuru kumla doldurdu
@tohum: sakir-0042
Parkta Şakir ile Necati kamyonla bir macera oyunu oynuyordu. Şakir taze bir elmayı oyuncak kamyona koydu ve kamyonu Necati'ye yolladı. Ama kamyon kumdaki bir çukura girdi ve tekerlekleri takıldı. "Kamyon çukurdan çıkamıyor!" dedi Şakir. Hemen çukurun başına koştu ve kamyonu çukurdan çıkardı. Sonra çukuru avuç avuç kumla doldurdu ve düzeltti. Kamyonu yeniden itip Necati'ye yolladı. Bu kez kamyon düz kumdan geçti ve Necati'nin önünde durdu. Necati elmayı hortumuyla aldı ve güldü. "Elma geldi, teşekkürler, Şakir!" dedi Necati. Sonra Şakir ile Necati oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kamyonla bir macera oyunu"
   - Cümle 1: «Parkta Şakir ile Necati kamyonla bir macera oyunu oynuyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki macera özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0042` birebir aynı, ardından `@onarim: cdaed196e9b09e6ec7d0e10930f7ebcc61111d57`, sonra gövde.

### Hikâye 11: tohum sakir-0043 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0043
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'yelek', fiil 'sevmek', sıfat 'cesur'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kırmızı yelek bir taneydi ve ikisi de istedi | sırayla giymeyi söyleyip önce kardeşine verdi
@tohum: sakir-0043
Bir sabah Şakir ile Canan kumsalda sevdikleri macera oyununu oynuyordu. Kumdan bir gemi yapmışlardı. Kırmızı yeleği giyen gemiyi sürecekti ama yelek bir taneydi. Şakir de Canan da gemiyi sürmek istedi. "Canan, sırayla sürelim, önce sen giy," dedi Şakir. Canan yeleği giydi ve geminin önüne oturdu. "Çok cesuruz, gemimiz yola çıktı!" dedi Canan. Şakir onun arkasında iki eliyle kürek çekti. Sonra Canan yeleği çıkarıp Şakir'e verdi. Bu kez gemiyi Şakir sürdü ve Canan kürek çekti. Kardeşler bol bol güldü. Şakir çok sevindi, çünkü sırayla oynayınca ikisi de gemiyi sürmüştü.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sevdikleri macera oyununu oynuyordu"
   - Cümle 1: «Bir sabah Şakir ile Canan kumsalda sevdikleri macera oyununu oynuyordu.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sevdikleri macera oyununu oynuyordu"
   - Cümle 1: «Bir sabah Şakir ile Canan kumsalda sevdikleri macera oyununu oynuyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0043` birebir aynı, ardından `@onarim: 164c888d3a2198dc391cba01989e281b96c402eb`, sonra gövde.

### Hikâye 12: tohum sakir-0046 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0046
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sırayla oynamak
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'zincir', fiil 'seslenmek', sıfat 'temkinli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: tek bir zincir vardı ve ikisi de saklamak istedi | sırayla oynamayı önerdi ve ilk sırayı annesine verdi
@tohum: sakir-0046
@degisim: temkinli -> yavaş
Ormanda, kamp yerinde serin bir sabahtı. Şakir ile annesi Kadriye bir macera oyunu oynuyordu. Ama tek bir parlak zincir vardı ve ikisi de onu saklamak istedi. Şakir biraz düşündü. "Anneciğim, sırayla oynayalım, önce sen sakla," dedi Şakir. Kadriye gülümsedi ve zinciri büyük bir taşın altına koydu. "Bul bakalım, Şakir!" diye seslendi Kadriye. Şakir yavaş adımlarla yürüdü ve taşları tek tek kaldırdı. Zincir üçüncü taşın altındaydı. "Buldum!" dedi Şakir sevinçle. Sonra sıra Şakir'e geldi ve o, zinciri çalıların arasına bıraktı. Kadriye de etrafa baktı ve onu kısa sürede buldu. Şakir ile annesi oyunlarına sırayla, mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir ile annesi Kadriye bir macera oyunu"
   - Cümle 2: «Şakir ile annesi Kadriye bir macera oyunu oynuyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız oyunun adı olarak geçiyor, sıra sorununun çözümünde işe yaramıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ikisi de onu saklamak istedi"
   - Cümle 3: «Ama tek bir parlak zincir vardı ve ikisi de onu saklamak istedi.»
   - Açıklama: Annenin çocuğuyla zinciri saklamak için yarışmasının sebebi söylenmiyor ve sorun zayıf.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0046` birebir aynı, `@degisim: temkinli -> yavaş` (tutuyorsan), ardından `@onarim: 357ed60771aee77e3319ecda7d8966982595333a`, sonra gövde.
