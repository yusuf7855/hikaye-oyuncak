# Editör görevi (onarım): Keloğlan, onarım partisi 37

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar37.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar37.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0137 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0137
- yer: dağ (Köyün yakınındaki tepe.)
- tema: bir şey yapmak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'takvim', fiil 'anlatmak', sıfat 'büyük'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: uçurtma kuyruğu olmadığı için düşüyordu | düşen kurdeleyi uçurtmaya kuyruk olarak bağladı
@tohum: keloglan-0137
@degisim: takvim -> kurdele
Tepede güçlü bir rüzgar esiyordu. Keloğlan ile Balkız büyük bir uçurtma yapmıştı. Ama uçurtma kuyruğu olmadığı için havada dönüyor ve yere düşüyordu. Keloğlan süs için getirdikleri uzun kurdeleyi eline aldı. Ama sakarlık yaptı ve kurdeleyi elinden düşürdü. Kurdele uçurtmanın alt ucuna dolandı. "Bak, bu tam bir kuyruk oldu!" dedi Balkız. Keloğlan kurdeleyi uçurtmanın ucuna sıkıca bağladı. Balkız ipi tuttu ve Keloğlan uçurtmayı havaya bıraktı. Uçurtma bu kez dönmedi ve dümdüz yükseldi. "Kuyruk uçurtmayı dik tutar," diye anlattı Balkız. "Ne güzel uçuyor, Balkız, onu birlikte yaptık!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama sakarlık yaptı"
   - Cümle 5: «Ama sakarlık yaptı ve kurdeleyi elinden düşürdü.»
   - Açıklama: 'Sakarlık' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ama sakarlık yaptı ve kurdeleyi elinden düşürdü"
   - Cümle 5: «Ama sakarlık yaptı ve kurdeleyi elinden düşürdü.»
   - Açıklama: Çözüm figürün düşüncesinden değil, kurdelenin tesadüfen uçurtmaya dolanmasından geliyor.
   - Açıklama: Çözüm Keloğlan'ın düşünmesinden değil, kurdelenin tesadüfen uçurtmaya dolanmasından sebepsizce geliyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bak, bu tam bir kuyruk oldu!"
   - Cümle 7: «"Bak, bu tam bir kuyruk oldu!" dedi Balkız.»
   - Açıklama: Kurdelenin kuyruk olabileceğini Keloğlan değil Balkız fark ediyor.
   - Açıklama: Kuyruk fikrini Keloğlan değil Balkız buluyor; çözümü yan karakter getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0137` birebir aynı, `@degisim: takvim -> kurdele` (tutuyorsan), ardından `@onarim: 2da1f0db3a0353b549fd98f00ed87c3993a67a86`, sonra gövde.

### Hikâye 2: tohum keloglan-0138 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0138
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: kaybolan eşya
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'tutkal', fiil 'dinlemek', sıfat 'harika'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: tutkal masadan düşüp kaybolmuştu | sepeti düşürdü sesi dinledi ve tutkalı buldu
@tohum: keloglan-0138
Evde her yer sessizdi. Keloğlan anasının kırık tahta kaşığını tutkalla yapıştırmak istedi. Ama tutkal masadan düşmüş ve kaybolmuştu. "Anneciğim, tutkalı gördün mü?" diye sordu Keloğlan. "Görmedim, belki yere düştü," dedi anası. Keloğlan etrafa bakarken sakarlık yaptı ve elma sepetini düşürdü. Elmalar yere döküldü. Keloğlan durdu ve dikkatle dinledi. Dolabın altından küçük bir ses geldi. Bir elma oradaki tutkala çarpmıştı. Keloğlan tutkalı dolabın altından çıkardı ve kaşığı yapıştırdı. "Harika olmuş, Keloğlan!" dedi anası. Sonra Keloğlan ile anası elmaları gülerek birlikte topladı.
```

**Hakem bulguları (7):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "sepeti düşürdü sesi dinledi"
   - Cümle 0 (plan satırı): «tutkal masadan düşüp kaybolmuştu | sepeti düşürdü sesi dinledi ve tutkalı buldu»
   - Açıklama: Plan satırında sıralı yan cümleler arasında virgül eksik: 'sepeti düşürdü, sesi dinledi'.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "etrafa bakarken sakarlık yaptı"
   - Cümle 6: «Keloğlan etrafa bakarken sakarlık yaptı ve elma sepetini düşürdü.»
   - Açıklama: 'Sakarlık yaptı' soyut bir kavram, 3 yaşındaki çocuk bu kelimeyi bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bakarken sakarlık yaptı"
   - Cümle 6: «Keloğlan etrafa bakarken sakarlık yaptı ve elma sepetini düşürdü.»
   - Açıklama: 'Sakarlık' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sakarlık yaptı ve elma sepetini düşürdü"
   - Cümle 6: «Keloğlan etrafa bakarken sakarlık yaptı ve elma sepetini düşürdü.»
   - Açıklama: Çözüm sebebe yönelmiyor; tutkal kaza sonucu bulunuyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sakarlık yaptı ve elma sepetini düşürdü"
   - Cümle 6: «Keloğlan etrafa bakarken sakarlık yaptı ve elma sepetini düşürdü.»
   - Açıklama: Çözümü bir kaza sebepsizce getiriyor; tutkal tesadüfen bulunuyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bir elma oradaki tutkala çarpmıştı"
   - Cümle 10: «Bir elma oradaki tutkala çarpmıştı.»
   - Açıklama: Çözüm figürün bilinçli bir adımı değil, tesadüfen yuvarlanan bir elmayla geliyor ve sebebe doğrudan yönelmiyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir elma oradaki tutkala çarpmıştı"
   - Cümle 10: «Bir elma oradaki tutkala çarpmıştı.»
   - Açıklama: Tutkalın bulunması rastlantıyla, sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0138` birebir aynı, ardından `@onarim: d688dec1cbf3a476ce643204bafeff8328c1be50`, sonra gövde.

### Hikâye 3: tohum keloglan-0139 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0139
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yastık', fiil 'tamamlanmak', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: yağmurda kulübenin çatısı bitmemişti | düşürdüğü dallar çatıdaki deliği kapattı
@tohum: keloglan-0139
@degisim: yastık -> dal
Yağmur yavaş yavaş yağmaya başladı. Keloğlan ile Balkız ormanda dallardan küçük bir kulübe yapıyordu. Ama kulübenin çatısı bitmemişti ve içeri yağmur damlıyordu. "Keloğlan, çabuk, biraz daha dal getir!" dedi Balkız. Keloğlan kucağına kocaman bir yığın dal aldı. Kulübenin yanına gelince sakarlık yaptı ve dalları elinden düşürdü. Dallar tam çatıdaki deliğin üstüne düştü. Keloğlan onları eliyle düzeltti ve çatı tamamlandı. İçeri artık hiç su girmedi. Dışarıda otlar sırılsıklam oldu, ama ikisi hiç ıslanmadı. "Teşekkürler, Keloğlan, kulübemiz bitti!" dedi Balkız. Keloğlan çok sevindi, çünkü yaptıkları kulübe ikisini de yağmurdan korumuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gelince sakarlık yaptı ve"
   - Cümle 6: «Kulübenin yanına gelince sakarlık yaptı ve dalları elinden düşürdü.»
   - Açıklama: 'Sakarlık yaptı' soyut bir ad, küçük çocuğa uygun değil.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "sakarlık yaptı ve dalları elinden düşürdü"
   - Cümle 6: «Kulübenin yanına gelince sakarlık yaptı ve dalları elinden düşürdü.»
   - Açıklama: Deliği Keloğlan bilerek kapatmıyor; sorun şans eseri çözülüyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sakarlık yaptı ve dalları elinden düşürdü"
   - Cümle 6: «Kulübenin yanına gelince sakarlık yaptı ve dalları elinden düşürdü.»
   - Açıklama: Çözüm sebebe bilerek yönelmiyor, bir kaza ile geliyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dallar tam çatıdaki deliğin üstüne düştü"
   - Cümle 7: «Dallar tam çatıdaki deliğin üstüne düştü.»
   - Açıklama: Çözüm tesadüfle, sebepsizce geliyor.
   - Açıklama: Çözüm figürün eyleminden değil bir sakarlık tesadüfünden sebepsizce geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0139` birebir aynı, `@degisim: yastık -> dal` (tutuyorsan), ardından `@onarim: 6ab0d9ee4985cc8d26a6eafa16aeb6872e360167`, sonra gövde.

### Hikâye 4: tohum keloglan-0140 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0140
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'simit', fiil 'gezdirmek', sıfat 'basit'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: simit dalın ucundan kayıp düşüyordu | dalın ucunu yukarı kaldırıp simidi taşıdı
@tohum: keloglan-0140
Keloğlan ormanda komik bir oyun oynuyordu. Simidi ince bir dalın ucunda en büyük ağaca kadar gezdirmek istiyordu. Ama dalın ucu aşağı bakıyordu ve simit hep kayıp yapraklara düşüyordu. Keloğlan simidi yerden aldı ve dala yeniden taktı. Bu kez dalın ucunu biraz yukarı kaldırdı. Simit şimdi Keloğlan'ın eline doğru kaydı ve düşmedi. Keloğlan böylece basit ama yeni bir yol öğrendi. Simidini dalın üstünde en büyük ağaca kadar gezdirdi. Sonra ağacın dibine oturdu ve güldü. Keloğlan çok sevindi, çünkü simit artık hiç düşmüyordu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Simidi ince bir dalın ucunda en büyük ağaca kadar gezdirmek istiyordu"
   - Cümle 2: «Simidi ince bir dalın ucunda en büyük ağaca kadar gezdirmek istiyordu.»
   - Açıklama: Sorun kendi uydurduğu saçma bir oyundan doğuyor ve çocuğun önemseyeceği bir şey değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "basit ama yeni bir yol öğrendi"
   - Cümle 7: «Keloğlan böylece basit ama yeni bir yol öğrendi.»
   - Açıklama: 'Yol' burada yöntem anlamında mecazdır ve soyuttur.
   - Açıklama: 'yol öğrenmek' yöntem anlamında soyut ve mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0140` birebir aynı, ardından `@onarim: 293ab1414f6194a372dbfad4c30b77180246cd0f`, sonra gövde.

### Hikâye 5: tohum keloglan-0141 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0141
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'gözlük', fiil 'anlamak', sıfat 'taze'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ormanda bilinmeyen küçük bir ses geldi | oturup dinledi ve düşen elmayı gördü
@tohum: keloglan-0141
@degisim: gözlük -> elma
Ormanda büyük ağaçların altı serindi. Keloğlan yürürken yakınından gelen küçük bir ses duydu. Döndü ama orada hiçbir şey göremedi. Bu sesin ne olduğunu çok öğrenmek istedi. Keloğlan bir ağacın dibine oturdu ve sessizce dinledi. Rüzgar esti ve dallar sallandı. Tam o sırada yukarıdan taze, kırmızı bir elma düştü. Elma aynı sesi çıkararak yere çarptı. Keloğlan elmayı eline aldı ve yukarı baktı. Ağacın dallarında bir sürü elma vardı. Sesin nereden geldiğini şimdi anlamıştı. Keloğlan bundan sonra bir ses duyunca önce durup dikkatle dinledi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sesin ne olduğunu çok öğrenmek istedi"
   - Cümle 4: «Bu sesin ne olduğunu çok öğrenmek istedi.»
   - Açıklama: 'Çok öğrenmek istedi' kuruluşu doğal değil; 'çok merak etti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0141` birebir aynı, `@degisim: gözlük -> elma` (tutuyorsan), ardından `@onarim: 45b231108c4ad4017b7598c1176c20c820ea09aa`, sonra gövde.

### Hikâye 6: tohum keloglan-0142 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0142
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'pelerin', fiil 'sıralamak', sıfat 'güvenli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: yaprakların arasında garip yeşil bir top vardı | dalla birkaç kez bastırdı ve cevizi buldu
@tohum: keloglan-0142
@degisim: pelerin -> kabuk
Keloğlan ormanda büyük bir ağacın altında yürüyordu. Yaprakların arasında yeşil, yuvarlak bir top gördü. Bu garip topun içinde ne olduğunu çok merak etti. Güvenli olsun diye ona eliyle dokunmadı ve uzun bir dal aldı. Dalla topa bastırdı ama yeşil kabuk açılmadı. Keloğlan dürüst bir çocuktu ve işini hiç yarım bırakmazdı. Birkaç kez daha bastırdı ve sonunda kabuk ikiye ayrıldı. İçinden kahverengi, sert bir ceviz çıktı! Keloğlan yerde iki ceviz daha buldu ve üçünü bir kütüğün üstüne sıraladı. Keloğlan çok sevindi, çünkü yeşil topun içinde ne olduğunu bulmuştu.
```

**Hakem bulguları (7):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yaprakların arasında garip yeşil bir top vardı"
   - Cümle 0 (plan satırı): «yaprakların arasında garip yeşil bir top vardı | dalla birkaç kez bastırdı ve cevizi buldu»
   - Açıklama: Yerde bir topun bulunması gerçek bir sorun değil ve bir sebebe dayanmıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Yaprakların arasında yeşil, yuvarlak bir top gördü"
   - Cümle 2: «Yaprakların arasında yeşil, yuvarlak bir top gördü.»
   - Açıklama: Ortada gerçek bir sorun yok, yalnız bir merak var ve sebebi söylenmiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini hiç yarım bırakmazdı.»
   - Açıklama: 'Dürüst' kelimesi işi yarım bırakmamayı anlatmaz; yanlış anlamda kullanılmış.
   - Açıklama: 'Dürüst' kelimesi işi yarım bırakmamakla ilgisiz, yanlış anlamda kullanılmış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "işini hiç yarım bırakmazdı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini hiç yarım bırakmazdı.»
   - Açıklama: 'İşini yarım bırakmamak' kalıplaşmış soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini hiç yarım bırakmazdı.»
   - Açıklama: Tohumdaki özelliğin dürüstlük yanı yalnız etiket olarak söyleniyor, hikayede bir işe yaramıyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yerde iki ceviz daha buldu ve üçünü bir kütüğün üstüne sıraladı"
   - Cümle 9: «Keloğlan yerde iki ceviz daha buldu ve üçünü bir kütüğün üstüne sıraladı.»
   - Açıklama: Yeni cevizler sebepsiz beliriyor ve sıralanmaları hiçbir işe yaramıyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan yerde iki ceviz daha buldu"
   - Cümle 9: «Keloğlan yerde iki ceviz daha buldu ve üçünü bir kütüğün üstüne sıraladı.»
   - Açıklama: Yerdeki iki ceviz sebepsiz beliriyor ve olaya hiçbir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0142` birebir aynı, `@degisim: pelerin -> kabuk` (tutuyorsan), ardından `@onarim: f9eca4128f6f7310a0dbd99e8ed0887335dfc8c4`, sonra gövde.

### Hikâye 7: tohum keloglan-0143 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0143
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kavun', fiil 'asılmak', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kelebekler yaklaşınca hep uçup gidiyordu | düşen kavunun kokusuyla kelebekler yanına kondu
@tohum: keloglan-0143
@degisim: cömert -> tatlı
Güneş ormanın üstünde sıcacık parlıyordu. Keloğlan büyük bir ağacın altında renkli kelebekler gördü. Onlara yakından bakmak istedi, ama yaklaşınca kelebekler hep uçup gidiyordu. Keloğlan'ın yanında tatlı bir kavun vardı. Kavun serin kalsın diye bir torbanın içinde dala asılmıştı. Keloğlan kavunu yemek için torbayı aşağı indirdi. Ama sakarlık yaptı ve kavunu elinden düşürdü. Kavun yumuşak otların üstünde ikiye ayrıldı. Kokusu hemen etrafa yayıldı. Kelebekler uçup kavunun üstüne kondu. Keloğlan hiç kıpırdamadan oturdu ve onlara yakından baktı. Sonra Keloğlan kavunun öbür yarısını yedi ve kelebekleri mutlu mutlu izledi.
```

**Hakem bulguları (9):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kelebekler yaklaşınca hep"
   - Cümle 0 (plan satırı): «kelebekler yaklaşınca hep uçup gidiyordu | düşen kavunun kokusuyla kelebekler yanına kondu»
   - Açıklama: Plan satırında 'kelebekler yaklaşınca' yaklaşanı kelebekler yapıyor; yaklaşan Keloğlan olmalı.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kelebekler yaklaşınca hep uçup gidiyordu"
   - Cümle 0 (plan satırı): «kelebekler yaklaşınca hep uçup gidiyordu | düşen kavunun kokusuyla kelebekler yanına kondu»
   - Açıklama: Kimin yaklaştığı belli değil; cümle kelebeklerin yaklaştığı anlamına kayıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan'ın yanında tatlı bir kavun vardı"
   - Cümle 4: «Keloğlan'ın yanında tatlı bir kavun vardı.»
   - Açıklama: Kavun sorunla bağı olmadan kuruluyor ve çözümü tesadüfen getiriyor.
   - Açıklama: Kavun sorundan bağımsız beliriyor ve çözümü sebepsizce getiriyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan kavunu yemek için torbayı aşağı indirdi"
   - Cümle 6: «Keloğlan kavunu yemek için torbayı aşağı indirdi.»
   - Açıklama: Keloğlan kelebeklere yaklaşmak için bir şey yapmıyor; çözüm sebebe yönelmiyor, tesadüfle geliyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama sakarlık yaptı"
   - Cümle 7: «Ama sakarlık yaptı ve kavunu elinden düşürdü.»
   - Açıklama: 'Sakarlık' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
6. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Ama sakarlık yaptı ve kavunu elinden düşürdü"
   - Cümle 7: «Ama sakarlık yaptı ve kavunu elinden düşürdü.»
   - Açıklama: Kelebekleri yaklaştıran Keloğlan'ın çözümü değil, kazara düşen kavun.
   - Açıklama: Sorunu Keloğlan bilerek çözmüyor; kelebekler bir kaza sonucu geliyor.
7. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "sakarlık yaptı ve kavunu elinden düşürdü"
   - Cümle 7: «Ama sakarlık yaptı ve kavunu elinden düşürdü.»
   - Açıklama: Sorunu Keloğlan'ın bir çabası değil, kavunun kazara düşmesi çözüyor.
8. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Kelebekler uçup kavunun üstüne kondu"
   - Cümle 10: «Kelebekler uçup kavunun üstüne kondu.»
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor, sorunun ve çözümün parçası olarak olaya katılıyor.
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor, çözümün parçası olarak olaya katılıyor.
9. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kelebekler uçup kavunun üstüne kondu"
   - Cümle 10: «Kelebekler uçup kavunun üstüne kondu.»
   - Açıklama: Çözüm kelebeklerin ürkekliğine yönelmiyor, tesadüfen düşen kavundan çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0143` birebir aynı, `@degisim: cömert -> tatlı` (tutuyorsan), ardından `@onarim: 82e02f7144a8f7ea18d4834accaed89acafec77e`, sonra gövde.

### Hikâye 8: tohum keloglan-0144 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0144
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'baloncuk', fiil 'ilerlemek', sıfat 'yamuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşeğiyle yemeğini paylaşmak istedi ama onun neyi sevdiğini bilmiyordu | ekmeği ve elmayı sırayla uzatıp elmayı sevdiğini öğrendi
@tohum: keloglan-0144
@degisim: baloncuk -> elma
Ormanda Keloğlan ile eşeği dar bir yolda ilerliyordu. Keloğlan bir ağacın altında durup sepetini açtı. Sepettekileri Karakaçan'la paylaşmak istedi ama eşeğin neyi sevdiğini bilmiyordu. Sepette bir ekmek ve yamuk bir elma vardı. Keloğlan bunu öğrenmek istedi. Önce ekmekten bir parça uzattı. Karakaçan ekmeği kokladı ve başını çevirdi. Sonra Keloğlan yamuk elmayı uzattı. Eşek elmayı hemen yedi ve kulaklarını oynattı. "Demek sen elmayı seviyorsun, Karakaçan!" dedi Keloğlan. Keloğlan çok sevindi, çünkü yemeğini eşeğiyle paylaşmıştı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sepettekileri Karakaçan'la paylaşmak istedi"
   - Cümle 3: «Sepettekileri Karakaçan'la paylaşmak istedi ama eşeğin neyi sevdiğini bilmiyordu.»
   - Açıklama: Karakaçan adı eşeğin adı olarak tanıtılmadan kullanılıyor, kimi gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepettekileri Karakaçan'la paylaşmak istedi"
   - Cümle 3: «Sepettekileri Karakaçan'la paylaşmak istedi ama eşeğin neyi sevdiğini bilmiyordu.»
   - Açıklama: Karakaçan adı eşeğe ait olduğu söylenmeden beliriyor ve okur yeni bir karakter sanabilir.
   - Açıklama: Karakaçan adı eşek olduğu söylenmeden sebepsizce beliriyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Keloğlan bunu öğrenmek istedi"
   - Cümle 5: «Keloğlan bunu öğrenmek istedi.»
   - Açıklama: 'Bunu' zamiri önceki cümledeki elmaya mı eşeğin sevdiğine mi gidiyor, belli değil.
   - Açıklama: 'bunu' zamirinin neyi gösterdiği belli değil; önceki cümle sepetteki yiyecekler hakkında.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0144` birebir aynı, `@degisim: baloncuk -> elma` (tutuyorsan), ardından `@onarim: 699834f257cef51c561142af9a8bec1bd9aebbcb`, sonra gövde.

### Hikâye 9: tohum keloglan-0145 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0145
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'sis', fiil 'koşmak', sıfat 'tertemiz'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: dağa sis indi ve koşma oyununda kaya görünmez oldu | adımlarını sayarak yürüdü ve kayayı sisin içinde buldu
@tohum: keloglan-0145
Dağda Keloğlan büyük bir ağaçtan gri bir kayaya koşuyordu. Koşarken adımlarını saymayı öğrenmişti ve kaya yirmi adım uzaktaydı. Ama birden tepeye beyaz bir sis indi ve kaya görünmez oldu. Keloğlan ağacın yanında durdu ama oyunu bırakmak istemedi. Bu kez acele etmedi, yavaş yavaş yürüdü. Bir, iki, üç diye adımlarını tek tek saydı. Yirmi adım sonra eli soğuk kayaya değdi. Keloğlan sevinçle zıpladı ve kayaya sarıldı. Biraz sonra rüzgar esti ve sis dağıldı. Hava yine tertemiz oldu ve oyun devam etti. Keloğlan çok mutluydu, çünkü kayayı sisin içinde bile bulmuştu.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Koşarken adımlarını saymayı öğrenmişti"
   - Cümle 2: «Koşarken adımlarını saymayı öğrenmişti ve kaya yirmi adım uzaktaydı.»
   - Açıklama: 'Koşarken' zarf-fiili 'öğrenmişti' ile uyumsuz; cümle bozuk kurulmuş.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Koşarken adımlarını saymayı öğrenmişti"
   - Cümle 2: «Koşarken adımlarını saymayı öğrenmişti ve kaya yirmi adım uzaktaydı.»
   - Açıklama: 'öğrenmişti' yanlış anlamda; Keloğlan'ın adımlarını saydığı kastediliyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Koşarken adımlarını saymayı öğrenmişti"
   - Cümle 2: «Koşarken adımlarını saymayı öğrenmişti ve kaya yirmi adım uzaktaydı.»
   - Açıklama: Yirmi adım koşarken sayılmış ama yavaş yürürken de aynı yirmi adımda kayaya varılıyor; koşu ve yürüyüş adımları aynı değil.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Keloğlan ağacın yanında durdu ama oyunu bırakmak istemedi"
   - Cümle 4: «Keloğlan ağacın yanında durdu ama oyunu bırakmak istemedi.»
   - Açıklama: Tepede ani siste yalnız başına yürümeyi sürdürmek çocuğun taklit edebileceği riskli bir davranış.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "oyunu bırakmak istemedi"
   - Cümle 4: «Keloğlan ağacın yanında durdu ama oyunu bırakmak istemedi.»
   - Açıklama: Tohumdaki özellik öğrenmeyi sevmek; karttaki azim özelliği ikinci bir özellik olarak ekleniyor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "acele etmedi, yavaş yavaş yürüdü"
   - Cümle 5: «Bu kez acele etmedi, yavaş yavaş yürüdü.»
   - Açıklama: Keloğlan tepede tek başına, göremediği sisin içinde yürümeyi sürdürüyor; çocuk bunu taklit edebilir.
7. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bu kez acele etmedi, yavaş yavaş yürüdü"
   - Cümle 5: «Bu kez acele etmedi, yavaş yavaş yürüdü.»
   - Açıklama: Yirmi adımı koşarken öğrenmişken yavaş yürüyüş adımlarıyla da tam yirmi adımda kayaya varması tutarsız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0145` birebir aynı, ardından `@onarim: 4ca76650f0a6f2b9fe4523d0bd488eba4bff07ba`, sonra gövde.

### Hikâye 10: tohum keloglan-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0147
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'güneş', fiil 'erimek', sıfat 'çikolatalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: güneş vurdu ve çikolata erimeye başladı | tabağı düşürmemek için dededen yardım istedi ve gölgeye taşıdılar
@tohum: keloglan-0147
Güneş ormanda sıcacık parlıyordu. Keloğlan ile Bilgecan Dede çimende çikolatalı kurabiye yiyordu. Ama güneş tabağa vurdu ve çikolata erimeye başladı. Keloğlan tabağı gölgeye koymak için kaldırdı. Tabak elinde sallandı ve sakar Keloğlan bir kurabiye düşürdü. "Dede, tabağı birlikte taşır mıyız?" diye sordu Keloğlan. "Tabii, sen bir yanından tut, ben de öbür yanından," dedi Bilgecan Dede. İkisi tabağı yavaşça bir ağacın gölgesine götürdü. Gölge serindi ve çikolata artık erimedi. Sonra Keloğlan ile dede kurabiyeleri mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "sakar Keloğlan bir kurabiye düşürdü"
   - Cümle 5: «Tabak elinde sallandı ve sakar Keloğlan bir kurabiye düşürdü.»
   - Açıklama: Çikolatanın erimesinin yanına kurabiyenin düşmesi ikinci bir sorun olarak ekleniyor ve düşen kurabiye bir daha anılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0147` birebir aynı, ardından `@onarim: 940e5d487af2654feb6ac25af62f73f24631bd7a`, sonra gövde.

### Hikâye 11: tohum keloglan-0148 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0148
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'gömlek', fiil 'düzelmek', sıfat 'akıllı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: gömleğin düğmeleri açıktı ve gömlek rüzgarda uçuyordu | arkadaşından yardım istedi ve düğmeleri geçirmeyi öğrendi
@tohum: keloglan-0148
Serin bir rüzgar dağda esiyordu. Keloğlan'ın gömleğinin düğmeleri açıktı ve gömleği rüzgarda uçuyordu. Keloğlan düğmeleri deliklerine geçirmeyi daha bilmiyordu. "Balkız, bana bunu gösterir misin?" diye sordu Keloğlan. "Tabii, düğmeyi küçük deliğe it ve öbür yandan çek," dedi akıllı Balkız. Keloğlan onu dikkatle dinledi. Sonra düğmeleri kendisi tek tek deliklerine geçirdi. Gömleği düzeldi ve artık rüzgarda uçmadı. "Balkız, bak, oldu!" dedi Keloğlan. Balkız gülümsedi ve ellerini çırptı. Keloğlan çok sevindi, çünkü yeni bir şey öğrenmişti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gömleği rüzgarda uçuyordu"
   - Cümle 2: «Keloğlan'ın gömleğinin düğmeleri açıktı ve gömleği rüzgarda uçuyordu.»
   - Açıklama: Giyilen gömlek uçmaz, dalgalanır; fiil öznesine uymuyor.
   - Açıklama: Giyilen gömlek uçmaz; 'dalgalanıyordu' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "gömlek rüzgarda uçuyordu"
   - Cümle 2: «Keloğlan'ın gömleğinin düğmeleri açıktı ve gömleği rüzgarda uçuyordu.»
   - Açıklama: Plan satırında da gömlek için 'uçmak' yanlış anlamda kullanılmış.
   - Açıklama: Plan satırında da gömlek için 'uçuyordu' öznesine uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0148` birebir aynı, ardından `@onarim: a4f0aa1f584e279065abcdf17738754138ac841d`, sonra gövde.

### Hikâye 12: tohum keloglan-0150 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0150
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'tüy', fiil 'havalanmak', sıfat 'yardımsever'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: eşeği de oynamak istedi ama nasıl oynayacağını bilmiyordu | tüy elinden düşüp eşeğin burnuna kondu ve sırayla oynadılar
@tohum: keloglan-0150
@degisim: yardımsever -> beyaz
Evin önünde Keloğlan yerde beyaz bir tüy buldu. Tüye üfledi ve tüy havalandı. Eşeği Karakaçan da oynamak istedi ama nasıl oynayacağını bilmiyordu. Keloğlan sakarlık yaptı ve tüyü elinden düşürdü. Tüy yavaşça uçtu ve Karakaçan'ın burnuna kondu. Karakaçan burnundan hızla üfledi ve tüy yine havalandı. Keloğlan çok güldü ve ellerini çırptı. Böylece Karakaçan da oyuna katıldı. Önce Keloğlan tüye üfledi, sonra Karakaçan burnuyla üfledi. Keloğlan ile eşeği tüyle sırayla oynayarak çok eğlendi.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama nasıl oynayacağını bilmiyordu"
   - Cümle 3: «Eşeği Karakaçan da oynamak istedi ama nasıl oynayacağını bilmiyordu.»
   - Açıklama: Eşeğin neden oynamayı bilmediği söylenmiyor, sorunun sebebi belirsiz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan sakarlık yaptı"
   - Cümle 4: «Keloğlan sakarlık yaptı ve tüyü elinden düşürdü.»
   - Açıklama: 'Sakarlık' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Sakarlık' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Keloğlan sakarlık yaptı ve tüyü elinden düşürdü"
   - Cümle 4: «Keloğlan sakarlık yaptı ve tüyü elinden düşürdü.»
   - Açıklama: Sorun Keloğlan'ın bilinçli bir çözümüyle değil, bir kazayla çözülüyor.
   - Açıklama: Sorun Keloğlan'ın bilinçli bir eylemiyle değil bir kazayla çözülüyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Tüy yavaşça uçtu ve Karakaçan'ın burnuna kondu"
   - Cümle 5: «Tüy yavaşça uçtu ve Karakaçan'ın burnuna kondu.»
   - Açıklama: Çözüm eşeğin oyunu bilmemesine yönelmiyor, tesadüfen geliyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tüy yavaşça uçtu ve Karakaçan'ın burnuna kondu"
   - Cümle 5: «Tüy yavaşça uçtu ve Karakaçan'ın burnuna kondu.»
   - Açıklama: Çözüm tesadüfen, sebepsizce geliyor.
   - Açıklama: Çözümü sebepsiz bir rastlantı getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0150` birebir aynı, `@degisim: yardımsever -> beyaz` (tutuyorsan), ardından `@onarim: 02342489ebde3616374be9904500b5b240ea49a4`, sonra gövde.
