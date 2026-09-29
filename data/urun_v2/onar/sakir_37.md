# Editör görevi (onarım): Şakir, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar37.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0013 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0013
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'mermer', fiil 'sallanmak', sıfat 'minicik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: kova sallanınca kabuklar kuma düşüyordu | kovayı iki eliyle tuttu ve yavaşça yürüdü
@tohum: sakir-0013
@degisim: mermer -> kova
Şakir kumsalda hazine oyunu oynuyordu. Minicik deniz kabuklarını kovayla kumdaki çukura taşıyordu. Ama kova elinde sallanınca kabuklar kuma düşüyordu. Şakir eğildi ve düşen kabukları tek tek topladı. Macera oyunlarını çok seven Şakir yeni bir şey denedi. Kovayı iki eliyle önünde tuttu. Yavaş yavaş yürüdü ve kova hiç sallanmadı. Çukura vardığında bütün hazinesi kovanın içindeydi. Şakir kabukları çukura döktü ve üstlerini kumla örttü. Yerini unutmamak için üstüne büyük bir taş koydu. Hazine oyunu tam istediği gibi olmuştu. Şakir bundan sonra dolu kovayı hep iki eliyle taşıdı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macera oyunlarını çok seven Şakir yeni bir şey denedi"
   - Cümle 5: «Macera oyunlarını çok seven Şakir yeni bir şey denedi.»
   - Açıklama: Macera özelliği yalnız anılıyor; kovayı iki elle taşıma çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0013` birebir aynı, `@degisim: mermer -> kova` (tutuyorsan), ardından `@onarim: a99c456c5d0991a967b0337e128c7b5511c04678`, sonra gövde.

### Hikâye 2: tohum sakir-0108 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0108
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'erik', fiil 'kabarmak', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: kum kaydı ve eriği örttü | şapkasıyla kabarık kumu itip eriği buldu
@tohum: sakir-0108
Şakir kumsalda oturuyordu ve elinde son bir erik vardı. Ama erik elinden düştü ve kumdaki küçük bir çukura yuvarlandı. Çukurun kenarından kum kaydı ve eriği örttü. Artık erik görünmüyordu. Şakir hemen çukurun yanına eğildi. Kumun bir yeri küçük bir tepe gibi kabarmıştı. Şakir düşünceli bir yüzle kabarık yere baktı. Erik bu kumun altında olabilirdi. Şakir şapkasını çıkardı ve onu küçük bir kürek gibi tuttu. Şapkayla kumu yavaş yavaş kenara itti. Kumun altından mor erik çıktı. Şakir eriği deniz suyunda iyice yıkadı. Sonra şapkasını yeniden taktı ve eriği mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir düşünceli bir yüzle"
   - Cümle 7: «Şakir düşünceli bir yüzle kabarık yere baktı.»
   - Açıklama: 'Düşünceli bir yüzle' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Düşünceli bir yüzle' soyut bir anlatım, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0108` birebir aynı, ardından `@onarim: 652b3a7469b9b08cff80432dde54e2395696e432`, sonra gövde.

### Hikâye 3: tohum sakir-0109 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0109
- yer: park (Şehirdeki park.)
- tema: kaybolan eşya
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'karpuz', fiil 'büyütmek', sıfat 'zarif'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | -
@plan: top bankın altına yuvarlandı ve çok uzaktaydı | şapkasını bankın altına uzatıp topu kendine çekti
@tohum: sakir-0109
@degisim: zarif -> geniş
Parkta güneşli bir gündü. Şakir karpuz desenli topuna hava üfledi ve onu büyüttü. Ama top elinden kaydı ve bankın altına yuvarlandı. Şakir eğildi ve topu bankın altında gördü. Kolunu uzattı ama top çok uzaktaydı. Sonra başındaki geniş, beyaz şapkayı çıkardı. Şapkayı bankın altına uzattı. Top büyük olduğu için şapkanın kenarı topun arkasına kolayca ulaştı. Şakir şapkayı yavaşça kendine doğru çekti. Top şapkanın önünden dışarı yuvarlandı. Şakir topu iki eliyle sıkıca tuttu. Şapkanın tozunu silkeledi ve onu yeniden taktı. Sonra Şakir büyük topuyla mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Top büyük olduğu için şapkanın kenarı topun arkasına kolayca ulaştı"
   - Cümle 8: «Top büyük olduğu için şapkanın kenarı topun arkasına kolayca ulaştı.»
   - Açıklama: Topun büyük olması şapkanın topun arkasına ulaşmasını açıklamıyor; çözüm sebepsiz bir bağlantıyla geliyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Top büyük olduğu için şapkanın kenarı topun arkasına kolayca ulaştı"
   - Cümle 8: «Top büyük olduğu için şapkanın kenarı topun arkasına kolayca ulaştı.»
   - Açıklama: Topun büyük olması şapkanın arkasına ulaşmasını kolaylaştırmaz, tersine zorlaştırır; gerekçe mantıksız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0109` birebir aynı, `@degisim: zarif -> geniş` (tutuyorsan), ardından `@onarim: 6d82255bb48e18275f35f5406dc8d83914488db1`, sonra gövde.

### Hikâye 4: tohum sakir-0126 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0126
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'balkabağı', fiil 'yapıştırmak', sıfat 'sarı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: rüzgar babasının tabağını devirdi ve çekirdekler döküldü | çekirdeklerini şapkasına koyup babasıyla paylaştı
@tohum: sakir-0126
@degisim: balkabağı -> kabak
Ağaçların arasında rüzgar esiyordu. Şakir ile babası Remzi kampta sarı kağıda kabak çekirdeği yapıştırıyordu. Birden rüzgar Remzi'nin tabağını devirdi ve çekirdekleri uzun otlarda kayboldu. "Resmim için hiç çekirdeğim kalmadı," dedi Remzi. Şakir'in tabağı ise doluydu. Ama rüzgar yine esiyordu ve tabak çok düzdü. Şakir şapkasını çıkardı ve ikisinin arasına koydu. Sonra bütün çekirdeklerini şapkanın içine döktü. "Baba, bunun içi derin, ikimiz de buradan alalım," dedi Şakir. Remzi güldü ve şapkadan çekirdek alıp kendi kağıdına dizdi. Şakir de kendi resmini bitirdi. Şakir ile Remzi çok sevindi, çünkü paylaşınca ikisinin de resmi bitmişti.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama rüzgar yine esiyordu ve tabak çok düzdü"
   - Cümle 6: «Ama rüzgar yine esiyordu ve tabak çok düzdü.»
   - Açıklama: Kayıp çekirdek sorununun yanına Şakir'in düz tabağının rüzgarda dökülme tehlikesi ikinci bir sorun olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0126` birebir aynı, `@degisim: balkabağı -> kabak` (tutuyorsan), ardından `@onarim: f926dda0d76c58cc15fe98a762760cfa714b66be`, sonra gövde.

### Hikâye 5: tohum sakir-0133 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0133
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bisküvi', fiil 'uzatmak', sıfat 'kolay'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: annesi parlak güneş yüzünden bulutu göremedi | şapkasını annesine uzattı ve gözlerine gölge yaptı
@tohum: sakir-0133
Deniz kıyısında güneşli bir öğle vaktiydi. Şakir kumda bisküvi yerken denizin üstünde bir bulut gördü. Bulut tıpkı bisküvisine benziyordu ama annesi Kadriye parlak güneş yüzünden bulutu göremedi. "Ben de o bisküviyi görmek istiyorum, Şakir," dedi Kadriye. Şakir başından geniş şapkasını çıkardı ve annesine uzattı. Kadriye şapkayı taktı ve gözleri gölgede kaldı. Şimdi bulutu görmek çok kolaydı. Kadriye denizin üstündeki bulutu gördü ve güldü. Şakir de sevinçle ellerini çırptı. "Teşekkürler, Şakir, bu gerçekten kocaman bir bisküvi!" dedi Kadriye.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "o bisküviyi görmek istiyorum"
   - Cümle 4: «"Ben de o bisküviyi görmek istiyorum, Şakir," dedi Kadriye.»
   - Açıklama: Bulut mecazla 'bisküvi' diye anılıyor; üstelik bulutu görmeyen anne onu bisküvi diye adlandırıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu gerçekten kocaman bir bisküvi"
   - Cümle 10: «"Teşekkürler, Şakir, bu gerçekten kocaman bir bisküvi!" dedi Kadriye.»
   - Açıklama: Buluta bisküvi denmesi mecazdır; küçük çocuk için kafa karıştırıcı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0133` birebir aynı, ardından `@onarim: c9be97c14f96f9b5552abd66fe0dc14e232ee98b`, sonra gövde.

### Hikâye 6: tohum sakir-0136 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0136
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: paylaşmak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'biber', fiil 'dinmek', sıfat 'hareketsiz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: rüzgar dinmişti ve güneş filin başını ısıttı | şapkasını ona verdi ve onun gölgesinde oturdu
@tohum: sakir-0136
@degisim: biber -> gölge
Şakir ile Necati kumsalda oturuyordu. Rüzgar dinmişti ve güneş Necati'nin büyük başını ısıttı. Kumsalda hiç ağaç yoktu. "Şakir, başım çok sıcak," dedi Necati. Şakir başındaki geniş şapkasını hemen çıkardı. Şapkayı Necati'nin başına koydu. Necati şapka düşmesin diye başını hareketsiz tuttu. Şapka, Necati'nin başını güneşten korudu. Sonra Necati güldü ve Şakir'i yanına çağırdı. "Gel, benim gölgemde otur," dedi Necati. Şakir, Necati'nin gölgesinde oturdu. Artık ikisi de serindi. "Teşekkürler, Şakir, iyi ki bana şapkanı verdin!" dedi Necati.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "şapkasını ona verdi ve onun gölgesinde"
   - Cümle 0 (plan satırı): «rüzgar dinmişti ve güneş filin başını ısıttı | şapkasını ona verdi ve onun gölgesinde oturdu»
   - Açıklama: Plan satırında 'ona' ve 'onun' zamirlerinin kimi gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Necati şapka düşmesin diye başını hareketsiz tuttu"
   - Cümle 7: «Necati şapka düşmesin diye başını hareketsiz tuttu.»
   - Açıklama: Başı hareketsiz tutma ayrıntısı olayda hiçbir işe yaramıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Gel, benim gölgemde otur"
   - Cümle 10: «"Gel, benim gölgemde otur," dedi Necati.»
   - Açıklama: Şapkayla sorun çözülmüşken gölgede oturma sebebe yönelmeyen ek bir adım olarak ekleniyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Artık ikisi de serindi"
   - Cümle 12: «Artık ikisi de serindi.»
   - Açıklama: İnsanlar için 'serindi' uygun değil; 'serinledi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0136` birebir aynı, `@degisim: biber -> gölge` (tutuyorsan), ardından `@onarim: f2c27376d5ed8013ef8a84fbda5c6e5ed81baeed`, sonra gövde.

### Hikâye 7: tohum sakir-0141 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0141
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'delik', fiil 'düzelmek', sıfat 'harika'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: top büyük bir taşın arkasına gidip kayboldu | delikteki kumu şapkasıyla alıp topu buldu
@tohum: sakir-0141
Bir sabah Şakir kumsalda harika kırmızı topuyla oynuyordu. Top yuvarlandı ve büyük bir taşın arkasına gitti. Şakir oraya gitti ama topu göremedi. Kumda yalnız topun bıraktığı ince bir iz vardı. Şakir izin yanından yavaşça yürüdü. İz bir deliğin başında bitiyordu. Deliğin içi yumuşak kumla doluydu. Şakir başından şapkasını çıkardı. Şapkayla bu kumu yavaş yavaş dışarı aldı. Altında kırmızı bir şey göründü. Bu, Şakir'in topuydu! Şakir topu delikten çıkardı. Sonra kumu deliğe geri döktü ve yer düzeldi. Şakir şapkasını taktı ve topuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Top yuvarlandı ve büyük bir taşın arkasına gitti"
   - Cümle 2: «Top yuvarlandı ve büyük bir taşın arkasına gitti.»
   - Açıklama: Topun nasıl kumun altına gömüldüğünün sebebi söylenmiyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Deliğin içi yumuşak kumla doluydu"
   - Cümle 7: «Deliğin içi yumuşak kumla doluydu.»
   - Açıklama: Deliğin içi kumla doluyken topun deliğe girip kumun altında kalması çelişiyor.
   - Açıklama: Top az önce yuvarlanıp deliğe girmişken deliğin kumla dolu olması ve topun kumun altında kalması akla yatkın değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kumu yavaş yavaş dışarı aldı"
   - Cümle 9: «Şapkayla bu kumu yavaş yavaş dışarı aldı.»
   - Açıklama: Kum şapkayla 'dışarı alınmaz'; 'dışarı çıkardı' olmalı.
   - Açıklama: Kum dışarı alınmaz, çıkarılır; fiil yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0141` birebir aynı, ardından `@onarim: fecabd962af39124e1005d0a04ef2e2f4cc7f019`, sonra gövde.

### Hikâye 8: tohum sakir-0145 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0145
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'zeytin', fiil 'öğrenmek', sıfat 'meraklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: annesinin düğmesi koptu ve kumda kayboldu | şapkasını yuvarlanan şeyin üstüne koydu
@tohum: sakir-0145
Şakir annesi Kadriye ile kumsalda zeytin yiyordu. Birden annesinin siyah bir düğmesi koptu. "Düğmem kuma düştü," dedi Kadriye. Şakir yakında zeytin gibi küçük bir şey gördü. Rüzgar esti ve o şey kumda yuvarlanmaya başladı. Şakir hemen şapkasını çıkardı ve onun üstüne koydu. Onun ne olduğunu öğrenmek istedi. Kadriye de meraklıydı ve yanına eğildi. Şakir şapkayı yavaşça kaldırdı. Altında düz ve siyah bir düğme vardı. "Anne, bu zeytin değil, düğme!" dedi Şakir. Kadriye düğmeyi aldı ve Şakir'e sarıldı. "Teşekkürler, Şakir, düğmeyi sen buldun!" dedi Kadriye.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden annesinin siyah bir düğmesi koptu"
   - Cümle 2: «Birden annesinin siyah bir düğmesi koptu.»
   - Açıklama: Düğmenin neden koptuğu söylenmiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir yakında zeytin gibi"
   - Cümle 4: «Şakir yakında zeytin gibi küçük bir şey gördü.»
   - Açıklama: 'Yakında' çoğunlukla 'az sonra' anlamındadır; burada 'yakınında' kastediliyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun ne olduğunu öğrenmek"
   - Cümle 7: «Onun ne olduğunu öğrenmek istedi.»
   - Açıklama: Cümle başındaki 'Onun' zamirinin neyi gösterdiği belli değil.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Onun ne olduğunu öğrenmek istedi"
   - Cümle 7: «Onun ne olduğunu öğrenmek istedi.»
   - Açıklama: Annesi düğmenin kuma düştüğünü söylemişken Şakir'in yuvarlanan şeyin ne olduğunu bilmemesi ve düz bir düğmenin rüzgarda yuvarlanması çelişiyor.
   - Açıklama: Annesi düğmenin kuma düştüğünü az önce söylemişken Şakir ve Kadriye yuvarlanan şeyin ne olduğunu bilmiyormuş gibi davranıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0145` birebir aynı, ardından `@onarim: d3be37f4ef56ac7b1e395132525a0ff6ecf2bbba`, sonra gövde.
