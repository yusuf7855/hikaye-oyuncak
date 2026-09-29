# Editör görevi (onarım): Şakir, onarım partisi 7

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar7.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar7.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0001 (deneme 4 -> 5)

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
Şakir babası Remzi ile salonda bilye oynuyordu. Remzi'nin kocaman mavi bilyesi yuvarlandı ve dolabın altına girdi. Remzi eğildi ama kalın kolu oraya sığmadı. "Bilyemi alamıyorum, Şakir," dedi Remzi. "Ben alırım, baba," dedi Şakir. Dolabın altına bakmak Şakir için küçük bir maceraydı. Hemen yere uzandı ve orayı dikkatle inceledi. Mavi bilye en arkada duruyordu. Şakir'in küçük eli içeri rahatça girdi. Bilyeyi parmaklarıyla tuttu ve yavaşça dışarı çekti. Sonra onu babasına verdi. Remzi sevinçle güldü ve Şakir'e sarıldı. "Teşekkürler, Şakir, şimdi oyunumuza devam edelim!" dedi Remzi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "için küçük bir maceraydı"
   - Cümle 6: «Dolabın altına bakmak Şakir için küçük bir maceraydı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir maceraydı"
   - Cümle 6: «Dolabın altına bakmak Şakir için küçük bir maceraydı.»
   - Açıklama: 'Macera' 3 yaşındaki çocuk için soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0001` birebir aynı, ardından `@onarim: b67d84d7e079065afffd11181280028fc90e9eed`, sonra gövde.

### Hikâye 2: tohum sakir-0003 (deneme 4 -> 5)

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
Şakir eski bir ayakkabı kutusundan davul yapmak istedi. Kutuya eliyle vurdu ama sesi zor duydu. Kutunun içi kağıtlarla dolu olduğu için davul iyi ses çıkarmıyordu. Kutunun içine bakmak Şakir için küçük bir maceraydı. Kapağı hemen açtı ve içine baktı. Kağıtları tek tek çıkardı ve bir kenara koydu. Sonra kapağı sıkıca kapattı. Davuluna yeniden vurdu. Bu kez yüksek ve güzel bir ses çıktı. Şakir masasından iki kalem aldı. Onlarla davulu hızlı hızlı çaldı. Şakir bu sesi çok beğendi ve güldü. Yeni davulunu mutlu mutlu çalmaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir maceraydı"
   - Cümle 4: «Kutunun içine bakmak Şakir için küçük bir maceraydı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir için küçük bir maceraydı"
   - Cümle 4: «Kutunun içine bakmak Şakir için küçük bir maceraydı.»
   - Açıklama: Kutuya bakmayı 'macera' diye anlatmak soyut ve mecazlı bir kullanım, 3 yaşındaki çocuğa uygun değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutunun içine bakmak Şakir için küçük bir maceraydı"
   - Cümle 4: «Kutunun içine bakmak Şakir için küçük bir maceraydı.»
   - Açıklama: Macera cümlesi olaya hiçbir şey katmayan, özelliği zorla sokan işlevsiz bir ayrıntı.
   - Açıklama: Bu cümle olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0003` birebir aynı, `@degisim: kütük -> kutu` (tutuyorsan), ardından `@onarim: 9e361bdbc5d04a5288aedc9afcc7d6fe640613ab`, sonra gövde.

### Hikâye 3: tohum sakir-0017 (deneme 2 -> 3)

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
Bir sabah Şakir ile Canan kumsalda peynirli poğaça ve fındık yiyordu. Birden kayaların arasından tık tık diye bir ses geldi. Şakir bu sesin ne olduğunu anlamak istedi. "Canan, bu ses nereden geliyor?" diye sordu Şakir. "Şu küçük delikten geliyor," dedi Canan. Şakir deliğe baktı, ama güneş gözlerine geliyordu ve içini göremedi. Hemen geniş şapkasını öne doğru çekti. Şapka gözlerine gölge yaptı ve deliğin içi göründü. İçeride bir fındık vardı ve küçük dalgalar onu taşa vuruyordu. Bu, onların düşürdüğü bir fındıktı. "Demek o sesi fındık yapıyormuş!" dedi Canan gülerek. "Yaşasın, Canan, sesin nereden geldiğini birlikte bulduk!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bu, onların düşürdüğü bir fındıktı"
   - Cümle 10: «Bu, onların düşürdüğü bir fındıktı.»
   - Açıklama: Kumsalda düşürülen fındığın kayaların arasındaki deliğe dalgaların içine nasıl girdiği açıklanmıyor, sesin sebebi akla yatkın değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu, onların düşürdüğü bir fındıktı"
   - Cümle 10: «Bu, onların düşürdüğü bir fındıktı.»
   - Açıklama: Kumsalda yenen fındığın kayalardaki dalgalı deliğe nasıl girdiği ve onların fındığı olduğunun nasıl bilindiği sebepsiz kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0017` birebir aynı, ardından `@onarim: bc7661a17097bbf5c0d991688b3a7f5bd7041665`, sonra gövde.

### Hikâye 4: tohum sakir-0018 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: ikisi aynı anda boncuk taktı ve renkler karıştı | sırayla takmayı önerdi ve şapkasını annesine verdi
@tohum: sakir-0018
@degisim: pürüzsüz -> renkli
Şakir parkta annesi Kadriye ile bir bileklik yapıyordu. İpe bir kırmızı, bir sarı boncuk takıyorlardı. Ama aynı anda boncuk taktılar ve renkleri karıştırdılar. İki sarı boncuk yan yana gelmişti. Şakir fazla sarı boncuğu ipten çıkardı. "Anne, şapkayı giyen boncuk takar, olur mu?" diye sordu Şakir. "Olur, önce sen tak," dedi Kadriye. Şakir bir kırmızı boncuk taktı. Sonra şapkasını annesinin başına koydu. Kadriye bir sarı boncuk taktı ve şapkayı geri verdi. İkisi sırayla devam etti. Sonunda renkli bileklik bitti ve Kadriye onu Şakir'in koluna geçirdi. Şakir çok sevindi, çünkü bilekliği sırayla güzelce yapmışlardı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkayı giyen boncuk takar"
   - Cümle 6: «"Anne, şapkayı giyen boncuk takar, olur mu?" diye sordu Şakir.»
   - Açıklama: Şapka giyilmez takılır, ayrıca şapka daha önce tanıtılmadan belirli olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0018` birebir aynı, `@degisim: pürüzsüz -> renkli` (tutuyorsan), ardından `@onarim: f3a26b7ce66d31cfbe7c69dced72aa8dec3f208b`, sonra gövde.

### Hikâye 5: tohum sakir-0019 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0019
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'saksı', fiil 'yıkamak', sıfat 'yeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: aç sincaplar yanlarına gelmeye korkuyordu | şapkasına elma koyup ağacın dibine bıraktı
@tohum: sakir-0019
@degisim: saksı -> kova
Ormandaki kamp yerinde Şakir ile annesi Kadriye kovada yeşil elmalar yıkıyordu. Birden ağacın dibinde küçük sincaplar göründü. Sincapların karnı açtı, ama yanlarına gelmeye korkuyorlardı. Şakir onlara yardım etmek istedi. Kadriye bir elmayı küçük parçalara ayırdı. Şakir şapkasını çıkarıp ters çevirdi ve parçaları içine koydu. Sonra şapkayı ağacın dibine bıraktı ve annesiyle biraz geri çekildi. Sincaplar önce durdu ve baktı. Sonra yavaşça şapkaya yaklaştılar. Elma parçalarını tek tek yediler ve ağaca geri koştular. Şakir boş şapkasını alıp yeniden taktı. Şakir çok sevindi, çünkü aç sincaplara yardım etmişti.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ama yanlarına gelmeye korkuyorlardı"
   - Cümle 3: «Sincapların karnı açtı, ama yanlarına gelmeye korkuyorlardı.»
   - Açıklama: 'yanlarına' zamirinin Şakir ile Kadriye'yi mi sincapları mı gösterdiği belli değil.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kadriye bir elmayı küçük parçalara ayırdı"
   - Cümle 5: «Kadriye bir elmayı küçük parçalara ayırdı.»
   - Açıklama: Çözümün ilk adımını Şakir istemeden annesi Kadriye kendiliğinden başlatıyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Sonra yavaşça şapkaya yaklaştılar"
   - Cümle 9: «Sonra yavaşça şapkaya yaklaştılar.»
   - Açıklama: Arka plandaki çoğul canlı sincaplar olaya katılıp elmaları yiyor.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Elma parçalarını tek tek yediler"
   - Cümle 10: «Elma parçalarını tek tek yediler ve ağaca geri koştular.»
   - Açıklama: Çoğul canlı sincaplar arka planda kalmıyor, korkuyor, yaklaşıyor ve yiyerek olaya katılıyor.
   - Açıklama: Çoğul sincaplar olayın çözümünde etkin rol alıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0019` birebir aynı, `@degisim: saksı -> kova` (tutuyorsan), ardından `@onarim: 9e4a47efdebbc2470425750a4002afb31d8fe5ee`, sonra gövde.

### Hikâye 6: tohum sakir-0021 (deneme 2 -> 3)

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
Bir sabah Şakir ile Necati kamp yerinde yürüyordu. Ama Necati'nin karnı acıkmıştı ve yanında hiç yiyecek yoktu. Şakir'in macera çantasında, bir beze sardığı ılık bir simit vardı. Şakir simidi çıkardı ve bezi açtı. Sonra simidi iki eşit parçaya böldü. "Necati, yarısı senin," dedi Şakir. Necati simidi hortumuyla aldı. "Teşekkür ederim, Şakir, çok acıkmıştım," dedi Necati. İkisi bir kütüğün üstüne oturdu ve simidi birlikte yedi. Necati her lokmada hortumunu salladı. Şakir buna güldü. Şakir çok sevindi, çünkü simidini Necati ile paylaşmıştı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Şakir ile Necati kamp yerinde yürüyordu"
   - Cümle 1: «Bir sabah Şakir ile Necati kamp yerinde yürüyordu.»
   - Açıklama: Başlıktaki yer orman ama hikaye ormanı hiç kurmuyor, yalnız bir kamp yerinde geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir'in macera çantasında, bir beze"
   - Cümle 3: «Şakir'in macera çantasında, bir beze sardığı ılık bir simit vardı.»
   - Açıklama: Tohum özelliği 'Macerayı çok sever' karttaki gibi kullanılmıyor, yalnız çantanın adı olarak geçiyor ve çözüme katkısı yok.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir'in macera çantasında"
   - Cümle 3: «Şakir'in macera çantasında, bir beze sardığı ılık bir simit vardı.»
   - Açıklama: Kartın 'özellikler' alanındaki macera sevgisi yalnız çanta adı olarak geçiyor ve sorunun çözümünde işe yaramıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Necati simidi hortumuyla aldı"
   - Cümle 7: «Necati simidi hortumuyla aldı.»
   - Açıklama: Necati simidin yarısını aldı; 'simidi' bütün simidi anlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0021` birebir aynı, ardından `@onarim: ec1dc0c15b62189339ffda1c4829e8d771fbd657`, sonra gövde.

### Hikâye 7: tohum sakir-0024 (deneme 2 -> 3)

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
Evde Şakir ile Canan mutfaktaydı. Şakir hızlı hızlı yürürken önüne bakmadı. Canan'ın masadaki dolu sebze sepetine çarptı ve sebzeler yere döküldü. Canan onları az önce sepete koymuştu. Kardeşi üzüldü ve yere baktı. Şakir hemen durdu. "Özür dilerim, Canan, dikkat etmedim," dedi Şakir. Bazı domatesler masanın altındaydı. Oraya girmek Şakir için küçük bir maceraydı. Masanın altına girdi ve havuçları, domatesleri tek tek topladı. Canan da ona yardım etti. Kısa sürede sepet yine doldu. "Tamam, Şakir, birlikte hepsini topladık," dedi Canan ve gülümsedi. Şakir çok rahatladı, çünkü kardeşi artık üzgün değildi.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kardeşinden özür dileyip sebzeleri topladı"
   - Cümle 0 (plan satırı): «koşarken sebze sepetine çarptı ve sebzeler döküldü | kardeşinden özür dileyip sebzeleri topladı»
   - Açıklama: Gövdede Şakir kardeşinden hiç özür dilemiyor; plan çözümü yanlış söylüyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "koşarken sebze sepetine çarptı"
   - Cümle 0 (plan satırı): «koşarken sebze sepetine çarptı ve sebzeler döküldü | kardeşinden özür dileyip sebzeleri topladı»
   - Açıklama: Gövdede Şakir koşmuyor, hızlı hızlı yürürken sepete çarpıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kardeşi üzüldü ve yere baktı"
   - Cümle 5: «Kardeşi üzüldü ve yere baktı.»
   - Açıklama: Önceki cümlenin öznesi Canan olduğu için 'kardeşi' kelimesinin Canan'ı mı Şakir'i mi gösterdiği belirsiz.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir için küçük bir maceraydı"
   - Cümle 9: «Oraya girmek Şakir için küçük bir maceraydı.»
   - Açıklama: 'Macera' 3 yaşındaki çocuk için soyut bir kelime.
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oraya girmek Şakir için küçük bir maceraydı"
   - Cümle 9: «Oraya girmek Şakir için küçük bir maceraydı.»
   - Açıklama: Macera cümlesi olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0024` birebir aynı, `@degisim: pahalı -> dolu` (tutuyorsan), ardından `@onarim: 6a6e6f0c651076b35a82fb49844ba3327b85de6a`, sonra gövde.

### Hikâye 8: tohum sakir-0025 (deneme 2 -> 3)

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
Şakir, kamp yerinde annesi Kadriye için bir sürpriz hazırlıyordu. Şakir şanslıydı, orada çok çiçek vardı ve onlardan bir taç yaptı. Ama fazla çiçek koyduğu için taç çok büyük oldu. Şakir tacı şapkasına taktı ama taç aşağı düştü. Üç çiçek çıkardı ve tacı küçülttü. Bu kez taç şapkada kaldı. Sonra tacı arkasına sakladı ve annesinin yanına koştu. "Anne, gözlerini kapar mısın?" diye sordu Şakir. Kadriye gülümsedi ve gözlerini kapadı. Şakir tacı annesinin başına yavaşça koydu. Taç tam oldu, hiç kaymadı. Kadriye gözlerini açtı ve tacı eliyle tuttu. "Ne güzel bir sürpriz, Şakir, çok teşekkür ederim!" dedi Kadriye.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir şanslıydı, orada çok"
   - Cümle 2: «Şakir şanslıydı, orada çok çiçek vardı ve onlardan bir taç yaptı.»
   - Açıklama: 'Şanslı' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Taç tam oldu"
   - Cümle 11: «Taç tam oldu, hiç kaymadı.»
   - Açıklama: Doğru söyleyiş 'taç tam geldi'; 'tam oldu' yanlış anlamda.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Taç tam oldu, hiç kaymadı"
   - Cümle 11: «Taç tam oldu, hiç kaymadı.»
   - Açıklama: Taç Şakir'in şapkasına göre küçültülmüşken annesinin başına da tam oturuyor, bu çelişkili.
   - Açıklama: Taç Şakir'in şapkasına göre küçültüldü ama annesinin başına tam oluyor; ölçü çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0025` birebir aynı, `@degisim: piyano -> çiçek` (tutuyorsan), ardından `@onarim: 0858a179249cec603a94c682179fb53dabf36414`, sonra gövde.

### Hikâye 9: tohum sakir-0027 (deneme 1 -> 2)

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
@plan: kardeşi kitabını unuttuğu için boş oturuyordu | çantanın ipini çözdü ve ikinci küreği paylaştı
@tohum: sakir-0027
@degisim: süpürge -> kürek
Rüzgar hafif hafif esiyordu. Şakir kumsalda küreğiyle büyük bir kale yapıyordu. Kardeşi Canan ise kitabını evde unuttuğu için sessiz oturuyordu. Şakir, Canan'ın üzgün olduğunu gördü. Oyuncak çantasının ipini çözdü ve içinden ikinci bir kürek çıkardı. "Canan, bu kürek senin olsun, gel birlikte oynayalım!" dedi Şakir. "Ne oynayacağız?" diye sordu Canan. "Bir macera oyunu, kalenin etrafına uzun bir yol kazalım!" dedi Şakir. Canan küreği aldı ve gülümsedi. İkisi yan yana kumu kazdı. Sonunda yol kalenin etrafını tam sardı. Şakir ile Canan, kalelerinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "unuttuğu için boş oturuyordu"
   - Cümle 0 (plan satırı): «kardeşi kitabını unuttuğu için boş oturuyordu | çantanın ipini çözdü ve ikinci küreği paylaştı»
   - Açıklama: 'Boş oturmak' deyimsel bir anlatım; çocuk için somut değil.
   - Açıklama: 'Boş oturmak' deyimsel bir kullanım; çocuk için somut değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Oyuncak çantasının ipini çözdü"
   - Cümle 5: «Oyuncak çantasının ipini çözdü ve içinden ikinci bir kürek çıkardı.»
   - Açıklama: Oyuncak çantası ve ikinci kürek önceden kurulmadan çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0027` birebir aynı, `@degisim: süpürge -> kürek` (tutuyorsan), ardından `@onarim: 38cd4533b3e4dd939a0de5fdb91e096940e11d45`, sonra gövde.

### Hikâye 10: tohum sakir-0028 (deneme 1 -> 2)

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
@plan: kumdan pastanın mumu eksikti | yakında beyaz bir tüy bulup pastaya dikti
@tohum: sakir-0028
Kumsalda Fil Necati büyük bir şemsiyenin altında uyuyordu. Şakir ona sürpriz olarak kumdan bir pasta yaptı ve üstüne kabuklar dizdi. Ama pastanın mumu eksikti ve kumsalda hiç mum yoktu. Macerayı çok seven Şakir, şemsiyenin yanındaki kumda mum yerine bir şey aradı. Kumun üstünde uzun, beyaz bir tüy buldu. Tüyü pastanın tam ortasına dikti. Şimdi pasta tamamdı. Biraz sonra Necati uyandı ve pastayı gördü. Hortumuyla tüye yavaşça dokundu ve gülümsedi. Şakir de sevinçle ellerini çırptı. Şakir bundan sonra bir şey eksik olunca önce etrafına dikkatle baktı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yakında beyaz bir tüy"
   - Cümle 0 (plan satırı): «kumdan pastanın mumu eksikti | yakında beyaz bir tüy bulup pastaya dikti»
   - Açıklama: 'Yakında' burada 'az sonra' anlamında da okunuyor; 'yakınında' ya da 'yakınlarda' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 4: «Macerayı çok seven Şakir, şemsiyenin yanındaki kumda mum yerine bir şey aradı.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0028` birebir aynı, ardından `@onarim: 632ac94ddeb2d6b2ef58aa8963d3826e82080cd2`, sonra gövde.

### Hikâye 11: tohum sakir-0029 (deneme 1 -> 2)

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
@plan: rüzgar hazine haritasını uçurdu | babasından sıcak soğuk demesini isteyip kutuyu buldu
@tohum: sakir-0029
@degisim: tuzlu -> sarı
Parkta Şakir ile babası Remzi bir hazine oyunu oynuyordu. Remzi sarı bir kutuya kek koyup saklamış, bir de harita çizmişti. Ama rüzgar esti ve harita uçup gitti. Macerayı çok seven Şakir hiç üzülmedi. "Baba, yaklaşınca 'sıcak', uzaklaşınca 'soğuk' der misin?" diye sordu Şakir. "Tamam, haydi başla!" dedi Remzi gülerek. Şakir parkta gezinmeye başladı. "Soğuk, çok soğuk!" dedi Remzi ve titriyormuş gibi yaptı. Şakir döndü ve banklara doğru yürüdü. "Sıcak, çok sıcak!" dedi Remzi. Şakir bankın altına baktı ve sarı kutuyu buldu. Sonra ikisi banka oturdu ve keki mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 4: «Macerayı çok seven Şakir hiç üzülmedi.»
   - Açıklama: 'Macera' 3 yaşındaki çocuk için soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0029` birebir aynı, `@degisim: tuzlu -> sarı` (tutuyorsan), ardından `@onarim: 730eebe06de8aba02d29cd4f71246c7673e8ec1d`, sonra gövde.

### Hikâye 12: tohum sakir-0030 (deneme 1 -> 2)

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
@plan: su kenarındaki parlak şeyi dalgalar kapatıyordu | şapkasıyla onu alıp bir kabuk olduğunu gördü
@tohum: sakir-0030
@degisim: hamur -> kabuk
Rüzgar hafifçe esiyordu. Şakir kumsalda yürürken su kenarında parlayan bir şey gördü. Ama küçük dalgalar gelip gidiyordu ve onu hep kapatıyordu. Şakir onun ne olduğunu çok merak etti. Suya girmeden kenarda durdu ve eğildi. Dalga gidince şapkasını çıkardı. Onu şapkasıyla yavaşça aldı. Şapkanın içinde pembe, ıslak bir deniz kabuğu vardı. Kabuk küçük ve çok tatlıydı. Şakir kabuğu avucuna aldı ve güneşe tuttu. Kabuk yine parladı. Şakir çok sevindi, çünkü parlayan şeyin ne olduğunu bulmuştu.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Suya girmeden kenarda durdu ve eğildi"
   - Cümle 5: «Suya girmeden kenarda durdu ve eğildi.»
   - Açıklama: Şakir yanında büyük olmadan dalgaların vurduğu su kenarına eğiliyor; güvenli özellik kullanımı satırı tek başına uzağa gitmemeyi ister ve çocuk için taklit edilebilir bir su kenarı davranışı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu şapkasıyla yavaşça aldı"
   - Cümle 7: «Onu şapkasıyla yavaşça aldı.»
   - Açıklama: Önceki cümlede şapka geçtiği için 'Onu' zamirinin parlak şeyi mi şapkayı mı gösterdiği belirsiz.
   - Açıklama: 'Onu' zamiri bir önceki cümledeki şapkayı da gösterebilir; neyi aldığı belli değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "küçük ve çok tatlıydı"
   - Cümle 9: «Kabuk küçük ve çok tatlıydı.»
   - Açıklama: 'Tatlı' kabuk için 'sevimli' anlamında kullanılmış; küçük çocuk bunu tat olarak anlar.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kabuk küçük ve çok tatlıydı"
   - Cümle 9: «Kabuk küçük ve çok tatlıydı.»
   - Açıklama: 'Tatlı' tat anlamıyla karışır; kabuk için belirsiz kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0030` birebir aynı, `@degisim: hamur -> kabuk` (tutuyorsan), ardından `@onarim: c182fcdf7492961b2e3b3a1815ee809b351ffc66`, sonra gövde.
