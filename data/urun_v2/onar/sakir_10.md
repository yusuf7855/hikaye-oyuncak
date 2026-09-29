# Editör görevi (onarım): Şakir, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar10.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0032 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0032
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'yelkenli', fiil 'uzaklaşmak', sıfat 'bilgili'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: oyunda geminin yelkeni yoktu | annesinden havlu isteyip bir dala bağladı
@tohum: sakir-0032
@degisim: bilgili -> büyük
Şakir, kamp yerinde yere düşmüş kalın bir ağaca oturdu. Oyunda bu ağaç bir gemi oldu ve annesi Kadriye de arkasına oturdu. Ama geminin yelkeni yoktu ve yola çıkamıyordu. Şakir macerayı çok severdi ve hemen bir yelken aradı. "Anneciğim, büyük mavi havluyu alabilir miyim?" diye sordu Şakir. "Tabii, al," dedi Kadriye ve havluyu ona verdi. Şakir havluyu uzun bir dala bağladı. Sonra dalı iki eliyle havaya kaldırdı. Rüzgar esti ve havlu bir yelken gibi şişti. "Bak, anneciğim, yelkenlimiz limandan uzaklaşıyor!" dedi Şakir. Kadriye güldü ve ellerini çırptı. Şakir çok mutlu oldu, çünkü gemisi sonunda yola çıkmıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi ve hemen bir yelken aradı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0032` birebir aynı, `@degisim: bilgili -> büyük` (tutuyorsan), ardından `@onarim: 61e263ac04d22e0c64d61f02a04300ae4c4d24bb`, sonra gövde.

### Hikâye 2: tohum sakir-0033 (deneme 2 -> 3)

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
Kumsalda Şakir ile Canan ahşap oyuncak kutusunu açtı. İçinden havası inmiş mavi bir deniz topu çıktı. Şakir topa üfledi, ama nefes alırken hava hep geri kaçtı. Şakir macerayı çok severdi ve hemen yeni bir yol düşündü. "Canan, ben nefes alırken topun ağzını tutar mısın?" diye sordu Şakir. "Tabii, tutarım," dedi Canan. Şakir yine üfledi. Şakir nefes alırken Canan topun ağzını parmağıyla kapattı. Böylece hava hiç kaçmadı. Top yavaş yavaş büyüdü ve yuvarlak oldu. Sonunda Şakir topun ağzını sıkıca kapattı. "Teşekkürler, Canan, şimdi birlikte oynayabiliriz!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hemen yeni bir yol düşündü"
   - Cümle 4: «Şakir macerayı çok severdi ve hemen yeni bir yol düşündü.»
   - Açıklama: 'Yeni bir yol düşünmek' mecazlı bir anlatım; çocuk için soyut.
   - Açıklama: 'Yol' burada 'çare' anlamında mecazdır ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Yol' burada mecazi olarak 'çare' anlamında kullanılmış, küçük çocuğa soyut.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve hemen yeni bir yol düşündü"
   - Cümle 4: «Şakir macerayı çok severdi ve hemen yeni bir yol düşündü.»
   - Açıklama: Tohumdaki macera özelliği yalnız söyleniyor, top şişirme çözümünde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki macera özelliği topu şişirme çözümünde işe yarar biçimde kullanılmıyor, yalnız eklenmiş.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi ve hemen yeni bir yol düşündü"
   - Cümle 4: «Şakir macerayı çok severdi ve hemen yeni bir yol düşündü.»
   - Açıklama: Macerayı sevmek çözüm bulmanın sebebi gibi sunuluyor ama olaya bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0033` birebir aynı, `@degisim: pota -> top` (tutuyorsan), ardından `@onarim: 09e1e6d182ea3e53510376ac659c756c3b254eed`, sonra gövde.

### Hikâye 3: tohum sakir-0034 (deneme 1 -> 2)

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
@plan: böcekler soğuk tartıya ters düştü ve dönemedi | yaprak uzatıp böcekleri güneşe taşıdı
@tohum: sakir-0034
@degisim: şekerli -> yeşil
Şakir mutfakta kardeşi Canan ile oynuyordu. Birden tartının üstünde minik uğur böcekleri gördü. Böcekler soğuk tartıya ters düşmüştü ve dönemiyordu. Şakir macerayı çok severdi ve onları hemen kurtarmak istedi. "Canan, onlara nasıl yardım ederiz?" diye sordu Şakir. "Onlara bir yaprak uzat, yaprağı tutarlar," dedi Canan. Şakir pencerenin önündeki çiçekten yeşil bir yaprak kopardı. Yaprağı böceklerin ayaklarına yavaşça yaklaştırdı. Böcekler yaprağa tutundu ve döndü. Şakir yaprağı güneşli pencerenin önüne koydu. Uğur böcekleri güneşte ısındı ve kanatlarını açtı. Sonra uçup çiçeğin üstüne kondular. "Teşekkürler, Canan, böcekleri birlikte kurtardık!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Böcekler soğuk tartıya ters düşmüştü"
   - Cümle 3: «Böcekler soğuk tartıya ters düşmüştü ve dönemiyordu.»
   - Açıklama: Uğur böceklerinin mutfaktaki tartıya nasıl ve neden düştüğü söylenmiyor.
   - Açıklama: Uğur böceklerinin mutfaktaki tartıya neden ve nasıl ters düştüğü söylenmiyor, sebep akla yatkın biçimde kurulmuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi ve onları hemen kurtarmak istedi.»
   - Açıklama: Böcekleri kurtarmak istemek macera sevgisiyle ilgili değil; özellik kelimesi yanlış yerde kullanılmış.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Böcekler yaprağa tutundu ve döndü"
   - Cümle 9: «Böcekler yaprağa tutundu ve döndü.»
   - Açıklama: Notlanan çoğul canlı uğur böcekleri arka planda kalmıyor, olayın merkezine katılıyor.
   - Açıklama: Notlanan çoğul canlı böcekler arka planda kalmıyor, olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0034` birebir aynı, `@degisim: şekerli -> yeşil` (tutuyorsan), ardından `@onarim: c07ff6d32a807a4d16405f33538399c99fae628f`, sonra gövde.

### Hikâye 4: tohum sakir-0035 (deneme 1 -> 2)

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
@plan: filin kaleminin mürekkebi birden bitti | kendi kalemini verip sırayla çizdiler
@tohum: sakir-0035
Şakir, Necati ile kamp yerinde bir orman haritası çiziyordu. Necati büyük ağaçları çizecekti. Ama Necati'nin kaleminin mürekkebi birden bitti. Necati üzgün bir yüzle kalemine baktı. "Kalemim artık çizmiyor," dedi Necati. Şakir macerayı çok severdi ve bu haritayı bitirmek istiyordu. Onun tek bir kırmızı kalemi vardı. Şakir kalemini kaybolmasın diye çantasına bir iple bağlamıştı. İpi çözdü ve kalemi Necati'ye uzattı. "Kalemimi seninle paylaşırım, sırayla çizelim," dedi Şakir. Önce Necati ağaçları çizdi. Sonra Şakir çadırı ve yolu çizdi. Harita bitince Şakir ile Necati onu alıp kamp yerini mutlu mutlu gezdi.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve bu haritayı bitirmek istiyordu"
   - Cümle 6: «Şakir macerayı çok severdi ve bu haritayı bitirmek istiyordu.»
   - Açıklama: Tohumdaki macera özelliği kartın özellik cümlesi olarak söylenip geçiliyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir kalemini kaybolmasın diye çantasına bir iple bağlamıştı"
   - Cümle 8: «Şakir kalemini kaybolmasın diye çantasına bir iple bağlamıştı.»
   - Açıklama: İple bağlı kalem ayrıntısı olaya hiçbir şey katmayan işlevsiz bir ek adım kuruyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kalemini kaybolmasın diye çantasına bir iple bağlamıştı"
   - Cümle 8: «Şakir kalemini kaybolmasın diye çantasına bir iple bağlamıştı.»
   - Açıklama: Kalemin iple bağlı olması olayda hiçbir işe yaramayan, yalnız fazladan adım ekleyen bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0035` birebir aynı, ardından `@onarim: 69c6bee9c113dc08f9da8122abed000d16cb72fc`, sonra gövde.

### Hikâye 5: tohum sakir-0036 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0036
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'mobilya', fiil 'kaybetmek', sıfat 'sıcak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: aynı anda atıp kabukları karıştırdılar | sırayla atmayı önerdi ve birlikte saydılar
@tohum: sakir-0036
@degisim: mobilya -> kabuk
Kumsalda hava çok sıcaktı. Şakir şapkasını kuma koydu, annesi Kadriye ile içine kabuk attılar. Ama ikisi aynı anda attı ve hangi kabuğun kimin olduğunu bilemediler. "Anne, sırayla atalım mı?" diye sordu Şakir. "Olur, önce sen at," dedi Kadriye. Şakir bir kabuk attı ve kabuk şapkaya girdi. Sonra Kadriye attı ama onun kabuğu kuma düştü. Her seferinde birlikte saydılar. Sonunda Kadriye'nin bir kabuğu daha fazla girmişti. Şakir oyunu kaybetti ama güldü. "Tebrikler, anneciğim, sen kazandın!" dedi Şakir. Şakir çok sevindi, çünkü sırayla oynamak çok eğlenceliydi.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kumsalda hava çok sıcaktı"
   - Cümle 1: «Kumsalda hava çok sıcaktı.»
   - Açıklama: Çok sıcak güneşte şapkayı çıkarıp kuma koymak taklit edilince güneş çarpmasına yol açabilir; güvenli özellik kullanımına aykırı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "annesi Kadriye ile içine kabuk attılar"
   - Cümle 2: «Şakir şapkasını kuma koydu, annesi Kadriye ile içine kabuk attılar.»
   - Açıklama: Tekil özne Şakir ile başlayan cümlede 'annesi Kadriye ile ... attılar' yapısı özne-yüklem uyumunu bozuyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir şapkasını kuma koydu"
   - Cümle 2: «Şakir şapkasını kuma koydu, annesi Kadriye ile içine kabuk attılar.»
   - Açıklama: Karttaki özellik 'hep şapka takar' diyor; şapka çıkarılıp sepet olarak kullanılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kadriye'nin bir kabuğu daha fazla girmişti"
   - Cümle 9: «Sonunda Kadriye'nin bir kabuğu daha fazla girmişti.»
   - Açıklama: Kazanma-kaybetme yarışı hiç kurulmadan sebepsizce ortaya çıkıyor ve sorunla (kabukların karışması) bağı kopuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0036` birebir aynı, `@degisim: mobilya -> kabuk` (tutuyorsan), ardından `@onarim: e57286a6c1431e4fc0d9d13cc08b25387962e2d8`, sonra gövde.

### Hikâye 6: tohum sakir-0037 (deneme 1 -> 2)

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
@plan: spagetti çok uzundu ve tencereye sığmadı | spagettiyi ikiye kırmayı söyledi ve kendisi kırdı
@tohum: sakir-0037
Bir akşam Şakir babasıyla mutfakta spagetti yapıyordu. Ama spagetti çok uzundu ve tencereye sığmadı. Remzi elindeki spagettiye şaşkın şaşkın baktı. "Baba, onları ikiye bölelim mi?" diye sordu Şakir. "Güzel fikir, Şakir," dedi Remzi. Şakir tüyleri yemeğe düşmesin diye beyaz şapkasını taktı. Sonra spagettileri tabağın üstünde ikiye kırdı. Remzi kısa parçaları tencereye koydu. Bu kez hepsi tencereye sığdı. Biraz sonra mutfak çok güzel kokmaya başladı. Remzi yemeği iki tabağa koydu. Şakir ile Remzi rahat sandalyelere oturup yediler. Şakir çok mutluydu, çünkü yemeği babasıyla birlikte yapmıştı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Remzi elindeki spagettiye"
   - Cümle 3: «Remzi elindeki spagettiye şaşkın şaşkın baktı.»
   - Açıklama: Remzi babası olarak tanıtılmadan birden ortaya çıkıyor; kimin olduğu belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Remzi elindeki spagettiye şaşkın"
   - Cümle 3: «Remzi elindeki spagettiye şaşkın şaşkın baktı.»
   - Açıklama: Remzi tanıtılmadan geçiyor; babası olduğu belirtilmediği için kimi gösterdiği belli değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir tüyleri yemeğe düşmesin diye beyaz şapkasını taktı"
   - Cümle 6: «Şakir tüyleri yemeğe düşmesin diye beyaz şapkasını taktı.»
   - Açıklama: Tohumdaki şapka özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0037` birebir aynı, ardından `@onarim: 6bb47994e6e9fb797466b0507158937096cbff61`, sonra gövde.

### Hikâye 7: tohum sakir-0038 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0038
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'beşik', fiil 'yeşillenmek', sıfat 'patlak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: koşarken kumdan kaleye bastı ve kule yıkıldı | özür dileyip şapkasıyla kum taşıyarak kuleyi yaptı
@tohum: sakir-0038
@degisim: beşik -> kova
Kumsalda Necati kumdan büyük bir kale yapmıştı. Şakir topunun peşinden koşarken kaleye bastı ve kulesi yıkıldı. Necati yıkılan kuleye üzgün üzgün baktı. "Özür dilerim, Necati, kuleyi hemen yeniden yaparım," dedi Şakir. Necati'nin patlak kovasından ıslak kum akıyordu. Şakir şapkasını çıkardı ve içini ıslak kumla doldurdu. Kumu kalenin yanına taşıdı ve yeni bir kule yaptı. Necati de kulenin kenarlarını düzeltti. Sonra kulenin tepesine yosun koydular ve kule yeşillendi. "Teşekkürler, Şakir, kale şimdi daha güzel," dedi Necati. Şakir ile Necati kalenin etrafına mutlu mutlu kabuk dizdiler.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Necati'nin patlak kovasından ıslak kum akıyordu"
   - Cümle 5: «Necati'nin patlak kovasından ıslak kum akıyordu.»
   - Açıklama: Patlak kova sebepsiz beliriyor ve olayda işe yarayacak biçimde kurulmuyor.
   - Açıklama: Patlak kova sebepsizce beliriyor ve yalnız şapkayla çözümü getirmek için kuruluyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Necati'nin patlak kovasından ıslak kum akıyordu"
   - Cümle 5: «Necati'nin patlak kovasından ıslak kum akıyordu.»
   - Açıklama: Kova kaybolmuşken birkaç cümle sonra orada ve patlak olarak görünüyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kulenin tepesine yosun koydular"
   - Cümle 9: «Sonra kulenin tepesine yosun koydular ve kule yeşillendi.»
   - Açıklama: Yosun sebepsiz beliriyor.
   - Açıklama: Yosun sebepsizce beliriyor ve olaya hiçbir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0038` birebir aynı, `@degisim: beşik -> kova` (tutuyorsan), ardından `@onarim: a6fde5fca26235a69d932969cd8199d1a88931ac`, sonra gövde.

### Hikâye 8: tohum sakir-0039 (deneme 1 -> 2)

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
Bir sabah Şakir kamp yerinde küçük bir fidan dikti. Macerayı çok severdi, fidanı da kendisi sulamak istedi. Ama su dolu kova çok ağırdı ve Şakir onu kaldıramadı. Annesi Kadriye çadırın önünde oturuyordu. Şakir ondan yardım istemekten biraz çekindi. Sonra annesinin yanına gitti. "Anne, kovayı birlikte taşır mıyız?" diye sordu Şakir. "Tabii, hemen geliyorum," dedi Kadriye. İkisi kovayı iki yanından tuttu ve fidanın yanına taşıdı. Şakir suyu fidana yavaş yavaş döktü. Kuru toprak ıslandı ve fidanın yaprakları parladı. "Teşekkürler, anneciğim, fidan artık susuz değil!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok severdi"
   - Cümle 2: «Macerayı çok severdi, fidanı da kendisi sulamak istedi.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok severdi, fidanı da kendisi sulamak istedi"
   - Cümle 2: «Macerayı çok severdi, fidanı da kendisi sulamak istedi.»
   - Açıklama: Tohumdaki macera özelliği fidan sulamayla ilişkisiz, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0039` birebir aynı, `@degisim: fide -> fidan` (tutuyorsan), ardından `@onarim: d73835fc348777eea71abfbae3b05f51e7eb2e58`, sonra gövde.

### Hikâye 9: tohum sakir-0040 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0040
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'gümüş', fiil 'yankılanmak', sıfat 'yamuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: yer eğikti ve kozalak pasta devrildi | düz bir taş bulup pastayı yeniden dizdi
@tohum: sakir-0040
Bir sabah Şakir kamp yerinde babasına bir sürpriz hazırlıyordu. Şapkasıyla kozalak topladı ve onlardan bir pasta yaptı. Ama yer eğikti, pasta yamuk durdu ve devrildi. O gün Remzi'nin doğum günüydü ve o çadırda uyuyordu. Şakir etrafına baktı ve büyük, düz bir taş buldu. Kozalakları taşın üstüne yeniden dizdi. Bu kez pasta dik durdu. Tepesine parlak, gümüş renkli küçük bir taş koydu. Sonra Remzi çadırdan çıktı. "Sürpriz, babacığım, iyi ki doğdun!" diye bağırdı Şakir. Şakir'in sesi dağda yankılandı. Remzi sevinçle zıpladı ve Şakir'e sarıldı. "Teşekkürler, Şakir, bu en güzel pasta!" dedi Remzi.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve kozalak pasta devrildi"
   - Cümle 0 (plan satırı): «yer eğikti ve kozalak pasta devrildi | düz bir taş bulup pastayı yeniden dizdi»
   - Açıklama: Tamlama eki eksik; 'kozalak pastası' ya da 'kozalaklı pasta' olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve o çadırda uyuyordu"
   - Cümle 4: «O gün Remzi'nin doğum günüydü ve o çadırda uyuyordu.»
   - Açıklama: 'o' zamiri Remzi'yi mi yoksa 'o çadır' mı gösterdiği belirsiz, ayrıca Remzi'nin baba olduğu bağlanmadan yeni biri gibi tanıtılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "O gün Remzi'nin doğum günüydü"
   - Cümle 4: «O gün Remzi'nin doğum günüydü ve o çadırda uyuyordu.»
   - Açıklama: Baba önce 'babasına' diye anılıp sonra açıklamasız Remzi adıyla ikinci kez tanıtılıyor ve 'o çadırda' zamiri belirsiz.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir'in sesi dağda yankılandı"
   - Cümle 11: «Şakir'in sesi dağda yankılandı.»
   - Açıklama: Ormandaki kamp yerinde dağdan yankı işlevsiz ve sebepsiz bir ayrıntı olarak ekleniyor.
   - Açıklama: Yankı işlevsiz bir ayrıntı ve hikaye dağda değil ormanda geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0040` birebir aynı, ardından `@onarim: c095314f67e5e2511197b307ec10a8aa15b9de05`, sonra gövde.

### Hikâye 10: tohum sakir-0041 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0041
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'muz', fiil 'uzaklaştırmak', sıfat 'yapışkan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: dalga geldi ve sürpriz örtünün ucunu ıslattı | örtüyü tabakla birlikte sudan uzaklaştırdı
@tohum: sakir-0041
Bir sabah Canan kumsalda kitabını bitirmek üzereydi. Şakir bunu kutlamak için örtüyü kuma serdi ve tabağa muz dizdi. Ama birden büyük bir dalga geldi ve örtünün ucunu ıslattı. Macerayı çok seven Şakir, örtüyü tabakla birlikte hemen sudan uzaklaştırdı. Onları büyük bir taşın yanına, kuru kuma taşıdı. Sonra muz dilimlerini tabakta gülen bir yüz gibi dizdi. Canan kitabını kapatıp yanına geldi. "Sürpriz, Canan, kitabın bitti, kutlayalım!" dedi Şakir. "Ne güzel, çok teşekkür ederim!" dedi Canan. Sonra Şakir ile Canan muzları yapışkan parmaklarıyla mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sürpriz örtünün ucunu ıslattı"
   - Cümle 0 (plan satırı): «dalga geldi ve sürpriz örtünün ucunu ıslattı | örtüyü tabakla birlikte sudan uzaklaştırdı»
   - Açıklama: 'sürpriz örtü' tamlaması bozuk; örtünün sürpriz için serildiği anlaşılmıyor.
   - Açıklama: 'Sürpriz örtü' tamlaması bozuk ve anlamsız; 'örtünün ucunu' ya da 'sürpriz için serilen örtünün' olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "birden büyük bir dalga geldi"
   - Cümle 3: «Ama birden büyük bir dalga geldi ve örtünün ucunu ıslattı.»
   - Açıklama: Çocuklar büyük dalgaların ulaşabileceği kadar suya yakın oturuyor; taklit edilince su kenarında tehlike doğurabilir.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "büyük bir dalga geldi ve örtünün ucunu ıslattı"
   - Cümle 3: «Ama birden büyük bir dalga geldi ve örtünün ucunu ıslattı.»
   - Açıklama: Örtünün yalnız ucunun ıslanması önemsiz bir sorun; örtü taşınınca hemen bitiyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 4: «Macerayı çok seven Şakir, örtüyü tabakla birlikte hemen sudan uzaklaştırdı.»
   - Açıklama: Tohumdaki macera özelliği kartın özellik cümlesi olarak sıfatlaştırılmış, çözümde işe yarar biçimde kullanılmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 4: «Macerayı çok seven Şakir, örtüyü tabakla birlikte hemen sudan uzaklaştırdı.»
   - Açıklama: Macera sevgisi olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0041` birebir aynı, ardından `@onarim: 24678c4e59f8da3ee3be771f8c17c608c5518a13`, sonra gövde.

### Hikâye 11: tohum sakir-0042 (deneme 1 -> 2)

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
Parkta Şakir ile Necati kamyon oyunu oynuyordu. Şakir taze bir elmayı oyuncak kamyona koydu ve kamyonu Necati'ye yolladı. Ama kamyon kumdaki bir çukura girdi ve tekerlekleri takıldı. "Kamyon çukurdan çıkamıyor!" dedi Şakir. Şakir macerayı çok severdi ve hemen çukurun başına koştu. Kamyonu çukurdan çıkardı. Sonra çukuru avuç avuç kumla doldurdu ve düzeltti. Kamyonu yeniden itip Necati'ye yolladı. Bu kez kamyon düz kumdan geçti ve Necati'nin önünde durdu. Necati elmayı hortumuyla aldı ve güldü. "Elma geldi, teşekkürler, Şakir!" dedi Necati. Sonra Şakir ile Necati oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi ve hemen çukurun başına koştu.»
   - Açıklama: 'Macera' soyut bir kelime; 3 yaşındaki çocuk için uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve hemen çukurun başına koştu"
   - Cümle 5: «Şakir macerayı çok severdi ve hemen çukurun başına koştu.»
   - Açıklama: Tohumdaki macera özelliği yalnız kartın özellik cümlesi olarak anılıyor, çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0042` birebir aynı, ardından `@onarim: 855a73e3be116288e9903490405f4941e94753b2`, sonra gövde.

### Hikâye 12: tohum sakir-0043 (deneme 1 -> 2)

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
Bir sabah Şakir ile Canan kumsalda kumdan bir gemi yaptılar. Kırmızı yeleği giyen gemiyi sürecekti ama yelek bir taneydi. Şakir macerayı çok severdi, Canan da gemiyi sürmek istiyordu. "Canan, sırayla sürelim, önce sen giy," dedi Şakir. Canan yeleği giydi ve geminin önüne oturdu. "Çok cesuruz, gemimiz yola çıktı!" dedi Canan. Şakir onun arkasında iki eliyle kürek çekti. Sonra Canan yeleği çıkarıp Şakir'e verdi. Bu kez gemiyi Şakir sürdü ve Canan kürek çekti. Kardeşler bol bol güldü. Şakir çok sevindi, çünkü sırayla oynayınca ikisi de gemiyi sürmüştü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 3: «Şakir macerayı çok severdi, Canan da gemiyi sürmek istiyordu.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0043` birebir aynı, ardından `@onarim: 4e300497a99b7682542d0cb9f3646b86e070a9f9`, sonra gövde.
