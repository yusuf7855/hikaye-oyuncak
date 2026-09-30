# Editör görevi (onarım): Doru, onarım partisi 32

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/doru_onar32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Doru | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/doru_onar32.txt --ad urun_v2`
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

## Kart: Doru (kaynaklı, kapalı dünya)

- Ad: Doru (okunuş: doru; kesme eki okunuşa uyar)
- Kimlik: Doru, annesiyle birlikte özgür bir at sürüsünde yaşayan genç bir attır.
- Tür: at
- Güvenli özellik kullanımı: Doru'nun hızı açık ve düz yerde koşarken gösterilir; uçurumdan atlama, derin sudan geçme yoktur. Sürüyü yakalamak isteyen insanlar ve kovalamaca hikayeye girmez.
- Özellikler:
  - hız: Genç ama güçlü ve hızlıdır. (örnek biçimler: hızla, hızlı, hızlıca)
  - cesur: Cesurdur. (örnek biçimler: cesur, cesaretle)
  - yardım: Karşılaştığı her canlıya yardım eder. (örnek biçimler: yardım, yardımına)
- Yerler:
  - dağ: Sürünün dolaştığı yüksek dağlar ve vadi.
  - orman: Vadinin yakınında, ağaçlarla dolu bir orman.
  - park: Sürünün çimen yediği geniş bir çayır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - annesi: Doru'nun sevecen annesi. Tür: at; konuşur. Yüzey biçimleri: annesi, anne, anneciğim, Dorukısrak
  - Karatay: Doru'nun en yakın arkadaşı; simsiyah, neşeli ve heyecanlıdır, bazen yanlış karar verir. Tür: at; konuşur. Yüzey biçimleri: Karatay
  - Alaca: Sürünün en küçük üyesi; Doru ve Karatay'dan yeni şeyler öğrenir, onlar ona hep yardım eder. Tür: at; konuşur. Yüzey biçimleri: Alaca
  - Kırat: Sürünün en yaşlı üyesi; en çok o bilir, sürüdekiler ona danışır. Tür: at; konuşur. Yüzey biçimleri: Kırat
- Dünya kuralları:
  - Sürüdeki atlar konuşur; insanlar (çiftlik sahipleri) hikayeye girmez.
  - Kırat sürünün en yaşlısıdır; Doru'nun babası ya da dedesi değildir.
  - Doru'nun annesi Dorukısrak'tır; Doru'nun babası kartta yoktur.
- Yasak adlar: Alkız, Demirkır, Gelincik, Alfa Kurt, Moya, Muhtar, Yaman, Kaju, Hulusi
- Yasak: Kurt, tuzak ve çiftlik sahipleri hikayeye girmez.
- İzinli dünya kelimeleri: sürü, vadi, at, çimen

## Onarılacak hikâyeler

### Hikâye 1: tohum doru-0116 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0116
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'hediye', fiil 'beslemek', sıfat 'sulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: arkadaşı yüksekteki elmalara ulaşamadı | ağacı itip elmaları düşürdü ve ona verdi
@tohum: doru-0116
Rüzgar dağda serin serin esiyordu. Doru, arkadaşı Karatay'ı bir elma ağacının altında gördü. Karatay acıkmıştı ama sulu elmalar çok yüksekteydi. Karatay zıpladı ama elmalara ulaşamadı. Doru hemen arkadaşının yardımına geldi. Onu beslemek istiyordu. Doru ağacın gövdesini yavaşça itti. Dallar sallandı ve iki elma çimenlere düştü. Doru büyük elmayı Karatay'ın önüne koydu. Bu, arkadaşına küçük bir hediyeydi. Karatay elmayı yedi ve karnı doydu. Küçük elmayı da Doru yedi. Sonra iki arkadaş dağda mutlu mutlu oynamaya başladı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "arkadaşının yardımına geldi"
   - Cümle 5: «Doru hemen arkadaşının yardımına geldi.»
   - Açıklama: 'yardımına gelmek' kalıp bir anlatım, küçük çocuğa soyut kalıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Onu beslemek istiyordu"
   - Cümle 6: «Onu beslemek istiyordu.»
   - Açıklama: 'beslemek' arkadaş için uygun değil; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0116` birebir aynı, ardından `@onarim: 3360bcb177d468394e358b563cb6a980dc5d0e29`, sonra gövde.

### Hikâye 2: tohum doru-0118 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | park | annesi
@tohum: doru-0118
- yer: park (Sürünün çimen yediği geniş bir çayır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'top', fiil 'yakalanmak', sıfat 'ferah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | park | annesi
@plan: annesi durmadan kuyruğunu sallıyordu | kuyruğa takılan dikenli topu dişleriyle çıkardı
@tohum: doru-0118
@degisim: yakalanmak -> takılmak
Çayırda hava ferah ve serindi. Doru ile annesi çimen yiyordu. Annesi birden durmadan kuyruğunu sallamaya başladı. Doru bunu çok merak etti ve annesine yaklaştı. "Anne, neden kuyruğunu sallıyorsun?" diye sordu Doru. "Bir şey var ama göremiyorum," dedi annesi. Doru dikkatle baktı ve küçük, dikenli bir ot topu gördü. Top, uzun kuyruğa sıkıca takılmıştı. "Dur anneciğim, sana yardım edeyim," dedi Doru. Doru topu dişleriyle yavaşça tuttu ve çekti. Dikenli top çıktı ve çimenlere düştü. "Teşekkürler, Doru," dedi annesi. Doru çok sevindi, çünkü annesinin neden kuyruğunu salladığını bulmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hava ferah ve serindi"
   - Cümle 1: «Çayırda hava ferah ve serindi.»
   - Açıklama: 'Ferah' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Çayırda hava ferah ve serindi"
   - Cümle 1: «Çayırda hava ferah ve serindi.»
   - Açıklama: Başlıktaki yer park ama hikaye çayırda geçiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor ve bitiyor.
   - Açıklama: Başlıktaki yer park ama hikaye çayırda başlıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru topu dişleriyle yavaşça tuttu"
   - Cümle 10: «Doru topu dişleriyle yavaşça tuttu ve çekti.»
   - Açıklama: Dikenli bir ot topunu ağızla tutmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0118` birebir aynı, `@degisim: yakalanmak -> takılmak` (tutuyorsan), ardından `@onarim: 8edd2c25235e08d1ea1f779934413c45e550910a`, sonra gövde.

### Hikâye 3: tohum doru-0119 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Alaca
@tohum: doru-0119
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: paylaşmak
- yan: Alaca
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'buket', fiil 'toplanmak', sıfat 'tertemiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Alaca
@plan: yakında hiç çiçek kalmamıştı | hızla koşup çiçek getirdi ve paylaştı
@tohum: doru-0119
Bir sabah Doru ile Alaca vadide çimen yiyordu. Sürü yola çıkmak için toplanıyordu. Alaca üzgündü, çünkü yakında hiç çiçek kalmamıştı. "Ben daha hiç çiçek yemedim," dedi Alaca. Doru vadinin öbür ucundaki sarı çiçekleri gördü. "Bekle, Alaca, hemen dönerim!" dedi Doru. Doru düz vadide hızla koştu. Ağzıyla bir buket çiçek kopardı ve geri döndü. Sürü daha yola çıkmamıştı. Doru çiçekleri Alaca'nın önüne, tertemiz çimenin üstüne koydu. "Gel, bunları birlikte yiyelim," dedi Doru. İkisi çiçekleri yan yana yedi. Doru çok mutluydu, çünkü çiçeklerini Alaca ile paylaşmıştı.
```

**Hakem bulguları (4):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Doru ile Alaca vadide çimen yiyordu"
   - Cümle 1: «Bir sabah Doru ile Alaca vadide çimen yiyordu.»
   - Açıklama: Başlıktaki yer dağ, ama hikaye vadide geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yakında hiç çiçek kalmamıştı"
   - Cümle 3: «Alaca üzgündü, çünkü yakında hiç çiçek kalmamıştı.»
   - Açıklama: 'Yakında' hem 'yakın yerde' hem 'birazdan' anlamına gelir; burada anlam belirsiz kalıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yakında hiç çiçek kalmamıştı"
   - Cümle 3: «Alaca üzgündü, çünkü yakında hiç çiçek kalmamıştı.»
   - Açıklama: Yakında neden hiç çiçek kalmadığı söylenmiyor; sorunun sebebi yok.
   - Açıklama: Çiçeklerin neden kalmadığı söylenmiyor; sorunun sebebi yok.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir buket çiçek kopardı"
   - Cümle 8: «Ağzıyla bir buket çiçek kopardı ve geri döndü.»
   - Açıklama: 'Buket' 3 yaşındaki çocuğun bilmeyebileceği bir kelime ve koparılan çiçeğe uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0119` birebir aynı, ardından `@onarim: 4ca0c9c6c2bddb40650f281c70109a0d8a7d398c`, sonra gövde.

### Hikâye 4: tohum doru-0120 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0120
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: annesi
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'palmiye', fiil 'başlamak', sıfat 'cömert'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: kuru bir ot topu annesine doğru yuvarlandı | cesaretle ot topunun yanına gidip onu uzağa itti
@tohum: doru-0120
@degisim: palmiye -> çalı
Bir sabah dağda rüzgar esmeye başladı. Doru'nun annesi bir çalının yanında çimen yiyordu. Birden kocaman, kuru bir ot topu annesine doğru yuvarlandı. Annesi şaşırdı ve geri çekildi. "Doru, bu da ne?" dedi annesi. Doru biraz korktu ama cesaretle ot topuna yaklaştı. Burnuyla ona dokundu ve kokladı. "Korkma, anne, bu yalnız kuru ot," dedi Doru. Sonra ot topunu burnuyla itti ve uzağa yuvarladı. Annesi rahatladı ve yeniden çimen yedi. Cömert annesi en taze çimenleri Doru'ya bıraktı. Doru çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ot topu annesine doğru yuvarlandı"
   - Cümle 3: «Birden kocaman, kuru bir ot topu annesine doğru yuvarlandı.»
   - Açıklama: Özne 'Doru'nun annesi' iken 'annesine' zamirinin kimin annesini gösterdiği belirsiz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Cömert annesi en taze"
   - Cümle 11: «Cömert annesi en taze çimenleri Doru'ya bıraktı.»
   - Açıklama: 'Cömert' soyut bir kavram, küçük çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çünkü annesine yardım etmişti"
   - Cümle 12: «Doru çok sevindi, çünkü annesine yardım etmişti.»
   - Açıklama: Tohumdaki özellik cesaret; kartın özellikler listesindeki yardım ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0120` birebir aynı, `@degisim: palmiye -> çalı` (tutuyorsan), ardından `@onarim: 39b7379262fbe9ebb78e5675bad6e1b38afae6ea`, sonra gövde.

### Hikâye 5: tohum doru-0121 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0121
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'şeftali', fiil 'izlemek', sıfat 'beyaz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yaşlı at şeftaliyi severdi ama yakında şeftali yoktu | cesaretle karanlık yere girip şeftali getirdi
@tohum: doru-0121
Kuşlar ormanda neşeyle ötüyordu. Doru, Kırat'a bir sürpriz hazırlamak istedi. Kırat şeftaliyi çok severdi ama yakında hiç şeftali yoktu. Şeftali ağacı ormanın karanlık ve sık yerindeydi. Doru önce durdu, sonra cesaretle ağaçların arasına girdi. Ağacın altında yere düşmüş iki olgun şeftali buldu. Doru şeftalileri ağzıyla tek tek taşıdı. Onları Kırat'ın dinlendiği ağacın dibine, beyaz çiçeklerin yanına koydu. Sonra bir çalının arkasına saklandı ve izledi. Kırat başını kaldırdı ve şeftalileri gördü. Yaşlı at şeftalileri keyifle yedi. Doru çok sevindi, çünkü sürprizi Kırat'ı mutlu etmişti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "cesaretle ağaçların arasına girdi"
   - Cümle 5: «Doru önce durdu, sonra cesaretle ağaçların arasına girdi.»
   - Açıklama: Doru ormanın karanlık ve sık yerine tek başına ve gizlice giriyor; bu çocuğun taklit edebileceği tehlikeli bir davranış.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "sonra cesaretle ağaçların arasına girdi"
   - Cümle 5: «Doru önce durdu, sonra cesaretle ağaçların arasına girdi.»
   - Açıklama: Tek başına ormanın karanlık ve sık yerine girmek taklit edilebilecek riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0121` birebir aynı, ardından `@onarim: 12def4587ff00cde05848144c0475ad72501d07c`, sonra gövde.

### Hikâye 6: tohum doru-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Karatay
@tohum: doru-0122
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'yağmur', fiil 'seçmek', sıfat 'gururlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Karatay
@plan: saklambaçta arkadaşının kuyruğu çalıya takıldı | dalları dişleriyle çekip kuyruğu kurtardı
@tohum: doru-0122
Doru ile Karatay yağmurdan sonra ormanda saklambaç oynuyordu. Karatay saklanmak için sık bir çalıyı seçti. Ama çalıya girince kuyruğu dallara takıldı. "Doru, çıkamıyorum, yardım et!" diye seslendi Karatay. Doru sesi duydu ve hemen çalıya koştu. Karatay'ın uzun kuyruğu dallara dolanmıştı. Doru dalları dişleriyle tek tek tuttu ve yavaşça çekti. Kuyruk dallardan kurtuldu ve Karatay çalıdan çıktı. "Bu çalı çok sık, başka bir yer bul," dedi Doru gülerek. Karatay bu kez büyük bir kayanın arkasına saklandı. Doru onu uzun uzun aradı. Sonunda Karatay gururlu bir sesle "Buradayım!" diye bağırdı. İki arkadaş oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karatay bu kez büyük bir kayanın arkasına saklandı"
   - Cümle 10: «Karatay bu kez büyük bir kayanın arkasına saklandı.»
   - Açıklama: Sorun çözüldükten sonra sorunla ilgisi olmayan yeni bir saklambaç turu anlatılıyor.
   - Açıklama: Sorun çözüldükten sonra ikinci bir saklambaç bölümü ekleniyor ve olay akışı dağılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Karatay gururlu bir sesle"
   - Cümle 12: «Sonunda Karatay gururlu bir sesle "Buradayım!" diye bağırdı.»
   - Açıklama: 'Gururlu bir sesle' küçük çocuk için soyut bir ifade.
   - Açıklama: 'Gururlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0122` birebir aynı, ardından `@onarim: 7517f535a5c39f6cec528f1e150eba20563b0326`, sonra gövde.

### Hikâye 7: tohum doru-0124 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0124
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'avokado', fiil 'koklamak', sıfat 'kahverengi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: elmalar çok yüksekteydi ve uzanamadı | yaşlı attan yol sordu ve alçak dalı buldu
@tohum: doru-0124
@degisim: avokado -> elma
Ormanda ağaçların arasından tatlı bir koku geliyordu. Doru havayı kokladı ve bir elma ağacı buldu. Ama kırmızı elmalar çok yüksekteydi ve Doru onlara uzanamadı. Yaşlı Kırat yakında, kahverengi bir kütüğün yanında dinleniyordu. "Kırat, elmalar çok yüksek, bana bir yol gösterir misin?" diye sordu Doru. "Orada alçak bir dal var, ama o yan karanlık," dedi Kırat. Doru cesaretle karanlık yana yürüdü. Gerçekten de alçak bir dalda elmalar vardı. Doru bir elmayı dişleriyle koparıp yedi. Sonra bir tane de Kırat'a getirdi. Doru çok mutlu oldu, çünkü Kırat'a sormuş ve elmalara ulaşmıştı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bana bir yol gösterir misin"
   - Cümle 5: «"Kırat, elmalar çok yüksek, bana bir yol gösterir misin?" diye sordu Doru.»
   - Açıklama: 'Yol göstermek' burada mecazlı bir deyim olarak kullanılmış.
   - Açıklama: 'Yol göstermek' burada 'yardım etmek' anlamında mecazlı bir deyim.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama o yan karanlık"
   - Cümle 6: «"Orada alçak bir dal var, ama o yan karanlık," dedi Kırat.»
   - Açıklama: 'Yan' burada yanlış anlamda kullanılmış; 'o taraf karanlık' olmalı.
   - Açıklama: 'Yan' burada 'taraf' anlamında yanlış kullanılmış; 'o taraf karanlık' olmalı.
3. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Doru cesaretle karanlık yana yürüdü"
   - Cümle 7: «Doru cesaretle karanlık yana yürüdü.»
   - Açıklama: Ormanın karanlık tarafı cesaret gerektiren korkutucu bir öğe olarak sunuluyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Doru cesaretle karanlık yana"
   - Cümle 7: «Doru cesaretle karanlık yana yürüdü.»
   - Açıklama: 'Karanlık yana' yanlış kelime seçimi; 'karanlık tarafa' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0124` birebir aynı, `@degisim: avokado -> elma` (tutuyorsan), ardından `@onarim: bbdc79413fa630e384e53620d32ed9c4af21a929`, sonra gövde.

### Hikâye 8: tohum doru-0125 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0125
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Karatay
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'papatya', fiil 'işaretlemek', sıfat 'yorgun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: kuru bir dal papatyaların üstüne düştü | arkadaşını çağırdı ve dalı birlikte ittiler
@tohum: doru-0125
@degisim: işaretlemek -> dayamak
Bir sabah Doru ile Karatay dağda koşuyordu. Birden Doru durdu ve yere baktı. Rüzgar kuru bir dalı kırmış, dal papatyaların üstüne düşmüştü. Beyaz papatyalar dalın altında eğilmişti. Doru onlara yardım etmek istedi ve dalı burnuyla itti. Ama dal çok ağırdı ve yerinden oynamadı. Doru yüksek sesle Karatay'ı çağırdı ve ona dalı gösterdi. Karatay biraz yorgundu ama hemen geldi. İkisi başlarını dala dayadı ve birlikte itti. Dal sonunda yana düştü. Papatyalar artık dalın altında değildi. Doru çok sevindi, çünkü arkadaşıyla birlikte papatyaları kurtarmıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karatay biraz yorgundu ama hemen geldi"
   - Cümle 8: «Karatay biraz yorgundu ama hemen geldi.»
   - Açıklama: Karatay'ın yorgunluğu işe yarayacakmış gibi kuruluyor ama olayda hiçbir rolü yok.
   - Açıklama: Karatay'ın yorgunluğu kurulup hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0125` birebir aynı, `@degisim: işaretlemek -> dayamak` (tutuyorsan), ardından `@onarim: e1ce687384e5734774f0c67cd929b0e99f3eda06`, sonra gövde.

### Hikâye 9: tohum doru-0127 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Doru | dağ | -
@tohum: doru-0127
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: cesur (Cesurdur.)
- kelimeler: isim 'yem', fiil 'dikmek', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | -
@plan: çalının arkasından garip bir ses geldi | başını dalların arasına soktu ve sıcak suyu buldu
@tohum: doru-0127
@degisim: dikmek -> dinlemek
Doru soğuk bir sabah dağda yem arıyordu. Birden büyük bir çalının arkasından garip bir ses geldi. Doru bu sesin ne olduğunu çok merak etti. Çalının arkası karanlık görünüyordu. Doru cesaretle başını sık dalların arasına soktu. Orada küçük ve sığ bir su vardı. Su yerin altından çıkıyordu ve ses buradan geliyordu. Doru burnunu suya değdirdi. Su sıcacıktı ve üstünden ince bir buhar çıkıyordu. Doru suyun yanında durdu ve güzelce ısındı. Sonra suyun kenarındaki taze otları yedi. Doru bundan sonra garip bir ses duyunca önce dikkatle dinledi.
```

**Hakem bulguları (9):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çalının arkasından garip bir ses geldi"
   - Cümle 2: «Birden büyük bir çalının arkasından garip bir ses geldi.»
   - Açıklama: Garip bir sesin gelmesi gerçek bir sorun değil, yalnız merak.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "başını sık dalların arasına soktu"
   - Cümle 5: «Doru cesaretle başını sık dalların arasına soktu.»
   - Açıklama: Karanlık görünen bilinmeyen çalıya baş sokmak taklit edilebilir tehlikeli davranış.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Orada küçük ve sığ bir su vardı"
   - Cümle 6: «Orada küçük ve sığ bir su vardı.»
   - Açıklama: 'Bir su vardı' yanlış; birikinti ya da gölet gibi bir ad gerekir.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük ve sığ bir su"
   - Cümle 6: «Orada küçük ve sığ bir su vardı.»
   - Açıklama: 'Sığ' kelimesini 3 yaşındaki çocuk bilmez ve 'bir su' ifadesi belirsiz kalıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük ve sığ"
   - Cümle 6: «Orada küçük ve sığ bir su vardı.»
   - Açıklama: 'Sığ' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Doru burnunu suya değdirdi"
   - Cümle 8: «Doru burnunu suya değdirdi.»
   - Açıklama: Buhar çıkan bilinmeyen sıcak suya dokunmak taklit edilince tehlikelidir.
   - Açıklama: Buhar çıkan sıcak suya ve karanlık çalıdaki bilinmeyen sese dokunmak/yaklaşmak çocuğun taklit edebileceği tehlikeli bir davranış.
7. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "garip bir ses duyunca önce dikkatle dinledi"
   - Cümle 12: «Doru bundan sonra garip bir ses duyunca önce dikkatle dinledi.»
   - Açıklama: 'Bundan sonra' ile süregiden alışkanlık anlatılıyor, fiil 'dinlerdi' olmalı.
8. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "önce dikkatle dinledi"
   - Cümle 12: «Doru bundan sonra garip bir ses duyunca önce dikkatle dinledi.»
   - Açıklama: Ders yaşanan olaydan çıkmıyor; Doru hikayede önce dinlemiyor, doğrudan başını çalıya sokuyor.
9. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Doru bundan sonra garip bir ses duyunca önce dikkatle dinledi"
   - Cümle 12: «Doru bundan sonra garip bir ses duyunca önce dikkatle dinledi.»
   - Açıklama: Ders olaydan çıkmıyor; Doru dinlemek yerine başını doğrudan çalıya sokmuştu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0127` birebir aynı, `@degisim: dikmek -> dinlemek` (tutuyorsan), ardından `@onarim: 5fea391c08ec54313447b5b669aaaaa739a10569`, sonra gövde.

### Hikâye 10: tohum doru-0128 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | annesi
@tohum: doru-0128
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: annesi
- özellik: yardım (Karşılaştığı her canlıya yardım eder.)
- kelimeler: isim 'düğüm', fiil 'yazmak', sıfat 'yeterli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Doru | dağ | annesi
@plan: annesini dinlemedi ve annesinin kuyruğu dallara takıldı | özür diledi ve düğümü dişleriyle açtı
@tohum: doru-0128
@degisim: yazmak -> çekmek
Doru annesini dinlemedi ve dağda sık çalıların arasına koştu. Annesi arkasından geldi ve uzun kuyruğu dallara takıldı. Kuyruğunda sıkı bir düğüm oldu ve annesi çıkamadı. Doru geri döndü ve annesine baktı. "Özür dilerim, anneciğim, seni dinlemeliydim," dedi Doru. "Seni affettim, ama önce bu düğümü çözelim," dedi annesi. Doru yardım etmek için dişleriyle dalları tek tek çekti. Sonra düğümü de yavaşça açtı. Annesinin kuyruğu dallardan kurtuldu. Annesi Doru'yu burnuyla okşadı. "Bu kadar yeterli, artık çok rahatım," dedi annesi. "Bundan sonra seni hep dinleyeceğim, anneciğim," dedi Doru.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Kuyruğunda sıkı bir düğüm oldu ve annesi çıkamadı"
   - Cümle 3: «Kuyruğunda sıkı bir düğüm oldu ve annesi çıkamadı.»
   - Açıklama: Annenin dallara takılıp çıkamaması küçük çocuk için korkutucu bir sıkışma anı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""Seni affettim, ama önce"
   - Cümle 6: «"Seni affettim, ama önce bu düğümü çözelim," dedi annesi.»
   - Açıklama: 'Affetmek' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Bu kadar yeterli, artık çok rahatım"
   - Cümle 11: «"Bu kadar yeterli, artık çok rahatım," dedi annesi.»
   - Açıklama: 'Bu kadar yeterli' sözü bağlamda neyi kastettiği belli olmadan kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0128` birebir aynı, `@degisim: yazmak -> çekmek` (tutuyorsan), ardından `@onarim: a19bd6fe4e0c816156d3567d52d783bfd8d77ed5`, sonra gövde.

### Hikâye 11: tohum doru-0129 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | dağ | Karatay
@tohum: doru-0129
- yer: dağ (Sürünün dolaştığı yüksek dağlar ve vadi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Karatay
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'bitki', fiil 'boşaltmak', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Doru | dağ | Karatay
@plan: arkadaşının sevdiği bitki vadinin öbür yanında büyüyordu | düz vadide koşup bitkileri getirdi
@tohum: doru-0129
Rüzgar vadide serin serin esiyordu. Doru, Karatay'a küçük bir sürpriz hazırlamak istedi. Ama Karatay'ın sevdiği tatlı bitki vadinin öbür yanında büyüyordu. Karatay dereden su içiyordu ve hiç sabırlı değildi. Az sonra geri gelecekti. Doru düz vadide hızla koştu. Orada yeşil bitkileri ağzına doldurdu. Sonra aynı yoldan geri döndü. Ağzındaki bitkileri düz bir taşın üstüne boşalttı. Tam o sırada Karatay geldi ve taşa baktı. Karatay sevinçle zıpladı ve hepsini yedi. Doru bundan sonra arkadaşlarını küçük sürprizlerle sevindirdi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hiç sabırlı değildi"
   - Cümle 4: «Karatay dereden su içiyordu ve hiç sabırlı değildi.»
   - Açıklama: 'Sabırlı' soyut bir kavram ve Karatay için olaya bağlanmadan kullanılmış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "hiç sabırlı değildi"
   - Cümle 4: «Karatay dereden su içiyordu ve hiç sabırlı değildi.»
   - Açıklama: Karatay'ın sabırsızlığı kuruluyor ama olayda hiçbir işe yaramıyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Doru bundan sonra arkadaşlarını küçük"
   - Cümle 12: «Doru bundan sonra arkadaşlarını küçük sürprizlerle sevindirdi.»
   - Açıklama: Notlanan çoğul canlı arkadaşlarını olayın alıcısı olarak olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0129` birebir aynı, ardından `@onarim: 423c3812934d832e04d9c49e350327a4f71580cf`, sonra gövde.

### Hikâye 12: tohum doru-0131 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Doru | orman | Kırat
@tohum: doru-0131
- yer: orman (Vadinin yakınında, ağaçlarla dolu bir orman.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kırat
- özellik: hız (Genç ama güçlü ve hızlıdır.)
- kelimeler: isim 'çubuk', fiil 'gezdirmek', sıfat 'temkinli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Doru | orman | Kırat
@plan: yağmur yaklaşıyordu ve kuru yerin yolunu bilmiyordu | yaşlı attan yol istedi ve düz yoldan koştu
@tohum: doru-0131
@degisim: gezdirmek -> göstermek
Doru ormanda Kırat'la birlikte yürüyordu. Birden gökte kara bulutlar toplandı ve yağmur yaklaştı. Doru kuru bir yere gitmek istedi ama yolu bilmiyordu. Temkinli Kırat ormanı çok iyi tanıyordu. Doru ondan yolu göstermesini istedi. Kırat, kırık çubuklarla dolu yolu değil, yanındaki düz yolu gösterdi. Doru o düz yolda hızla koştu. Yağmur başlamadan büyük ağaçların altına ulaştı. Kırat da yavaş yavaş arkasından geldi. Sonra yağmur başladı ama ikisi de kuru kaldı. Doru ile Kırat, sık dalların altında yağmuru mutlu mutlu seyretti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yaşlı attan yol istedi"
   - Cümle 0 (plan satırı): «yağmur yaklaşıyordu ve kuru yerin yolunu bilmiyordu | yaşlı attan yol istedi ve düz yoldan koştu»
   - Açıklama: Yol istenmez; 'yolu sordu' ya da 'yolu göstermesini istedi' olmalı.
   - Açıklama: Yol bilinmeyince 'yol sorulur'; 'yol istemek' geçit istemek anlamına gelir.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "büyük ağaçların altına ulaştı"
   - Cümle 8: «Yağmur başlamadan büyük ağaçların altına ulaştı.»
   - Açıklama: Kara bulutlu yağmurda büyük ağaçların altına sığınmak taklit edilince tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: doru-0131` birebir aynı, `@degisim: gezdirmek -> göstermek` (tutuyorsan), ardından `@onarim: 87d50cb168624c2e925d3be8e2cea32ee130e56f`, sonra gövde.
