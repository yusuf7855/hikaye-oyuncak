# Editör görevi (onarım): Pepee, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 11 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Pepee | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar9.txt --ad urun_v2`
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

## Kart: Pepee (kaynaklı, kapalı dünya)

- Ad: Pepee (okunuş: pepe; kesme eki okunuşa uyar)
- Kimlik: Pepee, mavi tulum ve mavi şapka giyen, dört yaşında meraklı bir oğlandır.
- Tür: oğlan
- Güvenli özellik kullanımı: Pepee yeni şeyleri bir büyüğün yanında dener; derin suya girmez, yüksek yere çıkmaz.
- Özellikler:
  - öğren: Yeni şeyler öğrenmeyi ve denemeyi sever. (örnek biçimler: öğrendi, öğrenmeyi)
  - kahvaltı: Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer. (örnek biçimler: kahvaltı, kahvaltıda)
  - dans: Oyun oynamayı ve dans etmeyi sever. (örnek biçimler: dans, dansı)
- Yerler:
  - orman: Ağaçlarla ve çiçeklerle dolu bir orman.
  - deniz: Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.
  - park: Salıncağı ve kaydırağı olan bir çocuk parkı.
  - ev: Pepee'nin ailesiyle yaşadığı ev.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Bebee: Pepee'nin küçük kız kardeşi; annesine hayrandır, Pepee ile oynamak için büyümek ister. Tür: kız; konuşur. Yüzey biçimleri: Bebee, kardeş, kardeşi
  - Şila: Pepee'nin kuzeni ve en yakın arkadaşı; çok güzel dans eder. Tür: kız; konuşur. Yüzey biçimleri: Şila, kuzen, kuzeni
  - Dedee: Pepee'nin dedesi; en az Pepee kadar hareketli bir oyun arkadaşı. Tür: dede; konuşur. Yüzey biçimleri: Dedee, dede, dedesi, dedeciğim
  - Nenee: Pepee'nin ninesi; komik ve eğlencelidir, yemek pişirmeyi sever. Tür: nine; konuşur. Yüzey biçimleri: Nenee, Ninee, nine, ninesi, nineciğim
  - Annee: Pepee'nin ve Bebee'nin annesi. Tür: anne; konuşur. Yüzey biçimleri: Annee, anne, annesi, anneciğim
- Dünya kuralları:
  - Bebee Pepee'nin küçük kız kardeşidir; Şila kuzenidir, kardeşi değildir.
  - Dizinin görünmeyen anlatıcısı hikayeye girmez; hikaye olayları kendisi anlatır.
- Yasak adlar: Şuşu, Şuşuu, Pisi, Zulu, Köpüş, Maymuş, Kaliş, Möcük, Zezee, Bibii, Kekee, Mimi, Mimii, Duduu, Tutuu, Ekee, Babaa, Zuku
- Yasak: Pepee'nin ve Bebee'nin konuşma zorluğu hikayeye konmaz; kimse konuşmasıyla alay etmez.
- Yasak: Dedee'nin uçan balonu hikayeye girmez (yükseklik).
- İzinli dünya kelimeleri: tulum, kahvaltı, pekmez, tahin, dans

## Onarılacak hikâyeler

### Hikâye 1: tohum pepee-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Annee
@tohum: pepee-0031
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: paylaşmak
- yan: Annee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'boru', fiil 'ıslanmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | Annee
@plan: ağacın altındaki kuru yer küçüktü ve annesi ıslanıyordu | ağaca yaslanıp dans ederek annesini kuru yere çekti
@tohum: pepee-0031
@degisim: boru -> ağaç
Yağmur yapraklara hafifçe vuruyordu. Pepee ile Annee ormanda büyük bir ağacın altına koştu. Ama ağacın altındaki kuru yer küçüktü ve Annee'nin omzu ıslanıyordu. Pepee annesine yer açmak istedi. Hemen ağaca iyice yaslandı. Sonra annesinin elini tuttu ve dans ederek onu yanına çekti. Annee dönerek kuru yere geldi ve güldü. Şimdi ikisi de yaprakların altında kuruydu. Annee Pepee'nin başını okşadı. Ağacın altı sessiz ve huzurluydu. Yağmur bir süre daha yağdı, sonra durdu. Pepee çok mutluydu, çünkü kuru yerini annesiyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ağacın altı sessiz ve huzurluydu"
   - Cümle 10: «Ağacın altı sessiz ve huzurluydu.»
   - Açıklama: 'Huzurlu' soyut bir kelime; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "altı sessiz ve huzurluydu"
   - Cümle 10: «Ağacın altı sessiz ve huzurluydu.»
   - Açıklama: 'huzurlu' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0031` birebir aynı, `@degisim: boru -> ağaç` (tutuyorsan), ardından `@onarim: 82a05e8d5b99492ca7a1bbc47930698f251d3561`, sonra gövde.

### Hikâye 2: tohum pepee-0032 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | -
@tohum: pepee-0032
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'bambu', fiil 'katmak', sıfat 'vanilyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | -
@plan: bambu yaprakları camın yarısını kapatıyordu | tabağını aldı ve öbür sandalyeye geçti
@tohum: pepee-0032
@degisim: vanilyalı -> uzun
Evde, pencerenin önünde uzun bir bambu vardı. Pepee kahvaltı yaparken dışarıda kar yağdığını gördü. Ama bambu yaprakları camın yarısını kapatıyordu. Pepee karı iyice görmek istedi. Ama tabağındaki yumurtayı da bırakmak istemedi. Bambu saksısı ise çok ağırdı. Pepee tabağını aldı ve öbür sandalyeye geçti. Buradan bütün cam görünüyordu. Kocaman kar taneleri yavaşça yere iniyordu. Pepee kar tanelerini tek tek saydı. Sonra pekmezine biraz tahin kattı ve tadına baktı. Pepee çok mutlu oldu, çünkü artık bütün karı görüyordu.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra pekmezine biraz tahin kattı"
   - Cümle 11: «Sonra pekmezine biraz tahin kattı ve tadına baktı.»
   - Açıklama: Pekmeze tahin katma sorunla ilgisiz, işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra pekmezine biraz tahin kattı ve tadına baktı"
   - Cümle 11: «Sonra pekmezine biraz tahin kattı ve tadına baktı.»
   - Açıklama: Pekmez ve tahin olayla ilgisiz, işlevsiz bir ayrıntı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "artık bütün karı görüyordu"
   - Cümle 12: «Pepee çok mutlu oldu, çünkü artık bütün karı görüyordu.»
   - Açıklama: 'bütün karı' hem belirsiz ('karı' eş anlamı) hem de karı görmek için tuhaf bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0032` birebir aynı, `@degisim: vanilyalı -> uzun` (tutuyorsan), ardından `@onarim: 1c9dc2b76ad17e7b56a38c72294ecdff541d3f51`, sonra gövde.

### Hikâye 3: tohum pepee-0033 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0033
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'tabak', fiil 'sevmek', sıfat 'düzenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: tabağı eğri tutuyordu ve tabak çiçeklere düşüyordu | dedesine sordu ve tabağı düz tuttu
@tohum: pepee-0033
@degisim: düzenli -> düz
Pepee ile Dedee ormanda uçan tabak oynuyordu. Dedee kırmızı tabağı attı ve Pepee zıplayıp yakaladı. Ama Pepee tabağı eğri tuttuğu için tabak hep çiçeklere düşüyordu. Bir kez tabak Dedee'nin ayağının dibine yuvarlandı ve ikisi de güldü. "Dedeciğim, sen nasıl bu kadar güzel atıyorsun?" diye sordu Pepee. "Tabağı yere düz tut ve kolunu hızlıca aç," dedi Dedee. Dedee yine attı ve Pepee dikkatle baktı. Pepee bunu hemen öğrenmek istedi. Tabağı düz tuttu ve kolunu hızlıca açtı. Kırmızı tabak dümdüz uçtu ve Dedee onu havada yakaladı. "Bu oyunu çok sevdim, Dedee!" dedi Pepee.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tabak Dedee'nin ayağının dibine yuvarlandı"
   - Cümle 4: «Bir kez tabak Dedee'nin ayağının dibine yuvarlandı ve ikisi de güldü.»
   - Açıklama: Bu olay hiçbir şeye yol açmıyor; işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir kez tabak Dedee'nin ayağının dibine yuvarlandı"
   - Cümle 4: «Bir kez tabak Dedee'nin ayağının dibine yuvarlandı ve ikisi de güldü.»
   - Açıklama: Bu olay sorunla ya da çözümle bağlantısız, işlevsiz bir ayrıntı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Tabağı yere düz tut"
   - Cümle 6: «"Tabağı yere düz tut ve kolunu hızlıca aç," dedi Dedee.»
   - Açıklama: 'Yere düz tutmak' yanlış anlamda; 'yere paralel tut' kastediliyor.
   - Açıklama: 'Yere düz tutmak' yanlış anlatım; 'yere paralel, düz tut' kastediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0033` birebir aynı, `@degisim: düzenli -> düz` (tutuyorsan), ardından `@onarim: 3fbe00c2ba90e1d1ed837170f46173c1136ec723`, sonra gövde.

### Hikâye 4: tohum pepee-0034 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | -
@tohum: pepee-0034
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'fermuar', fiil 'şişirmek', sıfat 'patlak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | ev | -
@plan: balon delik olduğu için hava hemen kaçtı | çantadan yeni bir balon çıkarıp kavanoza bağladı
@tohum: pepee-0034
Evde, mutfağın penceresi açıktı ve rüzgar esiyordu. Rüzgar beyaz perdeyi şişiriyordu ve Pepee buna gülüyordu. Pepee bir balonu da rüzgarda sallamak istedi, ama balonu patlak çıktı. Pepee balona üfledi, ama hava hemen küçük bir delikten kaçtı. Sonra Pepee oyuncak çantasını getirdi. Çantanın fermuarını açtı ve içinden kırmızı bir balon ile bir ip çıkardı. Balonu üfledi ve ipi ucuna bağladı. Masada kahvaltıdan kalan ağır bir pekmez kavanozu vardı. Pepee ipin öbür ucunu bu kavanoza sardı. Rüzgar esince kırmızı balon pencerenin önünde sallandı. Pepee çok sevindi, çünkü balonu da perde gibi rüzgarda sallanıyordu.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee balona üfledi"
   - Cümle 4: «Pepee balona üfledi, ama hava hemen küçük bir delikten kaçtı.»
   - Açıklama: Küçük çocuğun büyük olmadan delik balonu ağzıyla şişirmesi taklit edilince boğulma tehlikesi taşır ve güvenli kullanım satırındaki bir büyüğün yanında deneme kuralına aykırı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Balonu üfledi ve ipi"
   - Cümle 7: «Balonu üfledi ve ipi ucuna bağladı.»
   - Açıklama: Balon üflenmez, şişirilir; 'balonu şişirdi' olmalı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Masada kahvaltıdan kalan ağır bir pekmez kavanozu vardı"
   - Cümle 8: «Masada kahvaltıdan kalan ağır bir pekmez kavanozu vardı.»
   - Açıklama: Tohumdaki özellik kahvaltıyı sevmek, ama yalnız kahvaltıdan kalan bir kavanoz olarak anılıyor ve özellik işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kahvaltı sevgisi özelliği kullanılmıyor, kahvaltı yalnız kalan kavanoz olarak anılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Masada kahvaltıdan kalan ağır bir pekmez kavanozu"
   - Cümle 8: «Masada kahvaltıdan kalan ağır bir pekmez kavanozu vardı.»
   - Açıklama: Kavanoz tam gerektiği anda sebepsizce beliriyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pepee ipin öbür ucunu bu kavanoza sardı"
   - Cümle 9: «Pepee ipin öbür ucunu bu kavanoza sardı.»
   - Açıklama: Sorun delik balondu; kavanoza bağlama sebebe yönelmeyen fazladan bir adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0034` birebir aynı, ardından `@onarim: 0c9715dc075dda83f802a7903eaa118830cb8aa9`, sonra gövde.

### Hikâye 5: tohum pepee-0035 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Bebee
@tohum: pepee-0035
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'krem', fiil 'uzamak', sıfat 'sabunlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Bebee
@plan: baloncuk uçurmak istedi ama halka yoktu | ince bir ottan yeni bir halka yaptı
@tohum: pepee-0035
@degisim: krem -> halka
Bir sabah Pepee ile Bebee ormanda yumurta ve bal yiyordu. "Bak, Pepee, ben uzadım!" dedi Bebee ve çiçekli bir dala dokundu. Pepee bunu kutlamak için baloncuk uçurmak istedi, ama çantada halka yoktu. Çantada yalnız bir şişe sabunlu su vardı. Pepee yerde ince ve uzun bir ot buldu. Otun ucunu kıvırdı ve küçük bir halka yaptı. Halkayı suya batırdı ve yavaşça üfledi. Ağaçların arasına bir sürü baloncuk uçtu. Bebee onların arkasından koştu ve ellerini çırptı. "Bunlar senin için, Bebee!" dedi Pepee. Sonra Pepee ile Bebee kahvaltılarına mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ormanda yumurta ve bal yiyordu"
   - Cümle 1: «Bir sabah Pepee ile Bebee ormanda yumurta ve bal yiyordu.»
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız sahne olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bak, Pepee, ben uzadım!"
   - Cümle 2: «"Bak, Pepee, ben uzadım!" dedi Bebee ve çiçekli bir dala dokundu.»
   - Açıklama: Kişi için 'uzadım' yerine 'büyüdüm' ya da 'boyum uzadı' denmeli.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bak, Pepee, ben uzadım"
   - Cümle 2: «"Bak, Pepee, ben uzadım!" dedi Bebee ve çiçekli bir dala dokundu.»
   - Açıklama: Bebee'nin bir dala dokununca uzadığını söylemesi sebepsiz ve olaya bağlanmayan bir ayrıntı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kahvaltılarına mutlu mutlu devam etti"
   - Cümle 11: «Sonra Pepee ile Bebee kahvaltılarına mutlu mutlu devam etti.»
   - Açıklama: Tohumdaki kahvaltı özelliği sorunun çözümünde işe yaramıyor, yalnız anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0035` birebir aynı, `@degisim: krem -> halka` (tutuyorsan), ardından `@onarim: 60e11f5e54dbd73de9ad9ff4829af981f17f5e25`, sonra gövde.

### Hikâye 6: tohum pepee-0036 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Nenee
@tohum: pepee-0036
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Nenee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'çekmece', fiil 'yapıştırmak', sıfat 'akıllı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Nenee
@plan: koşarken ninesinin kumdan pastasına bastı | özür diledi ve kabukları yeniden yapıştırdı
@tohum: pepee-0036
@degisim: çekmece -> kabuk
Pepee deniz kıyısında kahvaltıya koşuyordu. Koşarken Nenee'nin kumdan yaptığı pastaya bastı. Pasta dağıldı ve üstündeki deniz kabukları kuma saçıldı. Nenee buna çok üzüldü. Pepee durdu ve hemen ninesinden özür diledi. Sonra pastayı Nenee ile birlikte yeniden yaptı. Kabukları ıslak kumla pastanın üstüne tek tek yapıştırdı. Kabuklar gülen bir yüz gibi duruyordu. Nenee yüzü görünce kahkaha attı. Sonra Pepee'ye sarıldı ve onun akıllı bir çocuk olduğunu söyledi. Pepee çok sevindi, çünkü ninesi artık üzgün değildi ve pasta yine güzeldi.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee deniz kıyısında kahvaltıya koşuyordu"
   - Cümle 1: «Pepee deniz kıyısında kahvaltıya koşuyordu.»
   - Açıklama: Tohumdaki kahvaltı özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kabuklar gülen bir yüz gibi duruyordu"
   - Cümle 8: «Kabuklar gülen bir yüz gibi duruyordu.»
   - Açıklama: Benzetme/mecaz içeriyor; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0036` birebir aynı, `@degisim: çekmece -> kabuk` (tutuyorsan), ardından `@onarim: 1e25f74ac06a84449a22f774eaebb33212a3ae98`, sonra gövde.

### Hikâye 7: tohum pepee-0037 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0037
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'bulmaca', fiil 'tanıştırmak', sıfat 'tuzlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: bulmacanın son sorusunu bilmiyordu | dedesinden yardım istedi ve cevabı buldu
@tohum: pepee-0037
@degisim: tanıştırmak -> sormak
Deniz kıyısında hava güzeldi. Pepee ile Dedee kumda oturmuş, resimli bir bulmaca yapıyordu. Son soru deniz suyunun tadını soruyordu, ama Pepee bunu bilmiyordu. "Dedeciğim, bana yardım eder misin?" diye sordu Pepee. Dedee onu su kenarındaki büyük bir taşa götürdü. Taşın üstünde ince, beyaz bir tuz vardı. "Bu tuz denizden geldi. Deniz suyu tuzlu," dedi Dedee. Pepee böylece yeni bir kelime öğrendi. Kelimeyi dedesiyle birlikte bulmacaya yazdı. Sonra Pepee ile Dedee kumda mutlu mutlu kale yaptı.
```

**Hakem bulguları (1):**

1. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Sonra Pepee ile Dedee kumda mutlu mutlu kale yaptı"
   - Cümle 11: «Sonra Pepee ile Dedee kumda mutlu mutlu kale yaptı.»
   - Açıklama: Son cümle bulmaca hedefine dönmüyor, ilgisiz bir kale oyunuyla kapanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0037` birebir aynı, `@degisim: tanıştırmak -> sormak` (tutuyorsan), ardından `@onarim: 8e1a05fa3e7ed0f65a4192922f4eda1d472bb3de`, sonra gövde.

### Hikâye 8: tohum pepee-0039 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Şila
@tohum: pepee-0039
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Şila
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'meşe', fiil 'büyütmek', sıfat 'yamuk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Şila
@plan: fidan yamuk duruyordu çünkü üstünde kuru dal vardı | dalı kaldırdı ve fidana su verdi
@tohum: pepee-0039
Bir sabah Pepee ile Şila ormanda büyük bir meşe ağacının altında oturuyordu. Pepee ağacın dibinde küçük bir meşe fidanı gördü. Fidan yamuk duruyordu, çünkü üstünde kuru bir dal vardı. "Şila, bu fidanı büyütmek istiyorum," dedi Pepee. Pepee kuru dalı fidanın üstünden yavaşça kaldırdı. Fidan hemen biraz doğruldu. "Pepee, ona biraz su verelim mi?" diye sordu Şila. Pepee kahvaltı çantasından su şişesini çıkardı. Fidanın dibine azar azar su döktü. Sonra Pepee ile Şila ağacın altında mutlu mutlu oyun oynadı.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee kahvaltı çantasından su şişesini çıkardı"
   - Cümle 8: «Pepee kahvaltı çantasından su şişesini çıkardı.»
   - Açıklama: Tohumdaki özellik kahvaltıyı sevmek, ama yalnız bir çantanın adında geçiyor ve işe yarar biçimde kullanılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee kahvaltı çantasından su şişesini"
   - Cümle 8: «Pepee kahvaltı çantasından su şişesini çıkardı.»
   - Açıklama: Tohumdaki özellik kahvaltıyı sevmek, ama yalnız 'kahvaltı çantası' kelimesiyle geçiyor ve işe yarar biçimde kullanılmıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Fidanın dibine azar azar su döktü"
   - Cümle 9: «Fidanın dibine azar azar su döktü.»
   - Açıklama: Su vermek fidanın yamuk durma sebebine, yani kuru dala yönelmiyor; fazladan bir adım.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "ağacın altında mutlu mutlu oyun oynadı"
   - Cümle 10: «Sonra Pepee ile Şila ağacın altında mutlu mutlu oyun oynadı.»
   - Açıklama: Son cümle fidanı büyütme hedefine dönmüyor ve fidan yalnız biraz doğruluyor; kapanış olaya bağlı değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0039` birebir aynı, ardından `@onarim: e360bd34f487ad385f96eff6384a250305773de8`, sonra gövde.

### Hikâye 9: tohum pepee-0040 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0040
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'kolye', fiil 'dinlemek', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: dudakları baldan yapış yapıştı ve ıslık çıkmadı | dudaklarını sildi ve sütünden bir yudum içti
@tohum: pepee-0040
@degisim: kolye -> peçete
Bir sabah Pepee ormanda ekmeğine bal sürüp yiyordu. Ağaçlarda kuşlar ötüyordu ve Pepee onları dikkatle dinledi. Pepee de kuşlar gibi ıslık çalmak istedi, ama dudakları baldan yapış yapıştı. Yalnız pıt diye komik bir ses çıktı. Pepee buna çok güldü. Sonra dudaklarını peçeteyle iyice sildi. Sıcacık sütünden de bir yudum içti. Dudaklarını büzdü ve yeniden üfledi. Bu kez ince ve güzel bir ıslık çıktı. Sonra Pepee kahvaltısına ıslık çalarak mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "dudakları baldan yapış yapıştı"
   - Cümle 3: «Pepee de kuşlar gibi ıslık çalmak istedi, ama dudakları baldan yapış yapıştı.»
   - Açıklama: 'Yapış yapıştı' bozuk bir yapı; 'yapış yapış oldu' olmalı.
   - Açıklama: Plan satırında da 'yapış yapıştı' bozuk; 'yapış yapış oldu' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Pepee buna çok güldü"
   - Cümle 5: «Pepee buna çok güldü.»
   - Açıklama: Figür sorunu komik bulup gülüyor; sorun önemsiz kalıyor ve çocuğun önemseyeceği bir dert kurulmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0040` birebir aynı, `@degisim: kolye -> peçete` (tutuyorsan), ardından `@onarim: 572c49fbb89e8c93deef306507bf95fb2fc1a3b8`, sonra gövde.

### Hikâye 10: tohum pepee-0041 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | -
@tohum: pepee-0041
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'kök', fiil 'ovuşturmak', sıfat 'bembeyaz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | orman | -
@plan: ağacın kökü dışarı çıkmıştı ve ayağı takıldı | köke dikkatle bakıp üstünden zıpladı
@tohum: pepee-0041
Bir sabah Pepee ormanda bembeyaz çiçeklerin arasında dans ediyordu. Pepee büyük bir ağacın etrafında dönerek bir tur atmak istedi. Ama ağacın kalın bir kökü dışarı çıkmıştı ve Pepee'nin ayağı ona takıldı. Pepee pıt diye yumuşak otların üstüne oturdu. Ellerine toprak bulaşmıştı. Pepee ellerini birbirine ovuşturdu ve toprağı temizledi. Sonra köke dikkatle baktı. Bu kez kökün yanına gelince üstünden zıpladı. Zıplamak dönmekten de eğlenceliydi. Pepee çok sevindi, çünkü turunu bu kez hiç durmadan bitirmişti.
```

**Hakem bulguları (2):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Pepee'nin ayağı ona takıldı"
   - Cümle 3: «Ama ağacın kalın bir kökü dışarı çıkmıştı ve Pepee'nin ayağı ona takıldı.»
   - Açıklama: Pepee köke takılıp düşüyor; bu bir kaza ve yaralanma riski taşıyor.
   - Açıklama: Pepee'nin ayağı köke takılıp düşüyor; yaralanma riski taşıyan bir düşme sahnesi var.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ellerine toprak bulaşmıştı"
   - Cümle 5: «Ellerine toprak bulaşmıştı.»
   - Açıklama: Ellerin kirlenip temizlenmesi soruna ve çözüme hizmet etmeyen işlevsiz bir yan olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0041` birebir aynı, ardından `@onarim: 761d704af245f196ed0cadeec8798df4a9a85147`, sonra gövde.

### Hikâye 11: tohum pepee-0042 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0042
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: bir şey yapmak
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'teneke', fiil 'yıkanmak', sıfat 'yorgun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kuru kum kovadan çıkınca hemen dağıldı | kumu suyla ıslattı ve kovaya bastırdı
@tohum: pepee-0042
@degisim: yıkanmak -> ıslatmak
Deniz kıyısında kumlar sıcak ve kuruydu. Pepee küçük teneke kovasıyla bir kum kulesi yapmak istiyordu. Ama kovayı ters çevirince kuru kum hemen dağıldı. Pepee bir kez daha denedi, ama kule yine olmadı. Sonra su kenarına gitti ve oradaki kumu suyla ıslattı. Kovayı ıslak kumla doldurdu ve elleriyle bastırdı. Kovayı yavaşça ters çevirip kaldırdı. Kumda dimdik bir kule duruyordu! Pepee yeni bir şey öğrenmişti: ıslak kum dağılmıyordu. Pepee yanına üç tane daha yaptı. Pepee yorgundu ama çok mutluydu, çünkü artık dört kulesi vardı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra su kenarına gitti ve oradaki kumu suyla ıslattı"
   - Cümle 5: «Sonra su kenarına gitti ve oradaki kumu suyla ıslattı.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada yanında büyük olmadan tek başına su kenarına gidip deniyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra su kenarına gitti"
   - Cümle 5: «Sonra su kenarına gitti ve oradaki kumu suyla ıslattı.»
   - Açıklama: Güvenli özellik kullanımı satırına aykırı olarak Pepee hiçbir büyük yanında yokken su kenarına gidip yeni bir şey deniyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Pepee yanına üç tane daha yaptı"
   - Cümle 10: «Pepee yanına üç tane daha yaptı.»
   - Açıklama: Art arda üç cümle 'Pepee' ile başlıyor; ad gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0042` birebir aynı, `@degisim: yıkanmak -> ıslatmak` (tutuyorsan), ardından `@onarim: d28bade161d15832bbb26f915eac3212fac37cc6`, sonra gövde.
