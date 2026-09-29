# Editör görevi (onarım): Keloğlan, onarım partisi 16

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar16.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar16.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0055 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0055
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kilit', fiil 'oynatmak', sıfat 'çekingen'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: kolyenin kilidi açıldı ve boncuklar çimenlere döküldü | boncukları tek tek bulup hepsini arkadaşına verdi
@tohum: keloglan-0055
@degisim: çekingen -> parlak
Şatonun geniş bahçesinde Balkız ile Keloğlan oturuyordu. Balkız kolyesinin kilidini parmaklarıyla oynatıyordu. Birden kilit açıldı ve boncuklar çimenlere döküldü. "Ah, kolyem!" dedi Balkız. Keloğlan hemen çimenlere eğildi. Boncukları tek tek topladı ve saydı. Bir boncuk eksikti ama Keloğlan aramayı bırakmadı. Sonunda bir çiçeğin dibinde son boncuğu buldu. Bu boncuk hepsinden daha parlaktı. Keloğlan onu çok beğendi ama dürüst davrandı ve hepsini Balkız'a verdi. Balkız boncukları ipe dizdi ve kilidi sıkıca kapattı. "Teşekkür ederim, Keloğlan, kolyem yine tamam!" dedi Balkız. Keloğlan çok mutlu oldu, çünkü arkadaşına yardım etmişti.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Keloğlan onu çok beğendi ama dürüst davrandı"
   - Cümle 10: «Keloğlan onu çok beğendi ama dürüst davrandı ve hepsini Balkız'a verdi.»
   - Açıklama: Boncuk toplama sorununa boncuğu saklama isteği gibi ikinci bir sorun ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0055` birebir aynı, `@degisim: çekingen -> parlak` (tutuyorsan), ardından `@onarim: 8fd06da75b8eb4abdaf463889ee3480d378d2069`, sonra gövde.

### Hikâye 2: tohum keloglan-0056 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0056
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kavanoz', fiil 'şakalaşmak', sıfat 'nefis'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: kavanozun kapağı dikenli bir çalının altına yuvarlandı | uzun bir sopayla kapağı çalının altından çekti
@tohum: keloglan-0056
Keloğlan anasıyla ormanda böğürtlen topluyordu. Anası böğürtlenleri büyük bir kavanoza koyuyordu. Birden kavanozun kapağı elinden kaydı ve dikenli bir çalının altına yuvarlandı. "Kapak olmadan böğürtlenler yere düşer," dedi anası. Keloğlan yerden uzun bir sopa aldı. Sopayı çalının altına uzattı ama ilk seferde kapağı çıkaramadı. Keloğlan bırakmadı ve bir kez daha denedi. Sonunda kapağı yavaşça dışarı çekti. Annesi kavanoza baktı ve Keloğlan ile şakalaştı. "Böğürtlenler azalmış, yoksa sen mi yedin?" dedi anası. "Evet, üç tane yedim, hepsi çok nefis!" dedi Keloğlan. Annesi güldü ve kapağı sıkıca kapattı. "Dürüst olduğun ve kapağı bulduğun için teşekkürler, Keloğlan!" dedi anası.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan bırakmadı ve bir kez daha denedi"
   - Cümle 7: «Keloğlan bırakmadı ve bir kez daha denedi.»
   - Açıklama: Nesnesiz 'bırakmadı' neyi bırakmadığı belli olmayan, 'vazgeçmedi' anlamında yanlış kullanılmış bir fiil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan bırakmadı ve bir kez daha denedi"
   - Cümle 7: «Keloğlan bırakmadı ve bir kez daha denedi.»
   - Açıklama: Nesnesiz 'bırakmadı' 'vazgeçmedi' anlamında deyimsel bir kullanım ve küçük çocuğa açık değil.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Böğürtlenler azalmış, yoksa sen mi yedin"
   - Cümle 10: «"Böğürtlenler azalmış, yoksa sen mi yedin?" dedi anası.»
   - Açıklama: Kapak sorunu çözüldükten sonra böğürtlenlerin azalması ikinci bir mesele olarak açılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Böğürtlenler azalmış, yoksa sen"
   - Cümle 10: «"Böğürtlenler azalmış, yoksa sen mi yedin?" dedi anası.»
   - Açıklama: Kapak bulunduktan sonra böğürtlen yeme ve dürüstlük olayı önceki olaydan çıkmadan sebepsizce ekleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Evet, üç tane yedim"
   - Cümle 11: «"Evet, üç tane yedim, hepsi çok nefis!" dedi Keloğlan.»
   - Açıklama: Keloğlan'ın böğürtlen yediği hiç gösterilmeden sonradan beliriyor ve kapak olayıyla bağı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0056` birebir aynı, ardından `@onarim: 7ea566f61c25e862ac05a622316d05a3f3ff840a`, sonra gövde.

### Hikâye 3: tohum keloglan-0057 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0057
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kalem', fiil 'bindirmek', sıfat 'tozlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: tepeden tuhaf bir ses geldi ve merak etti | sesin peşinden gidip kayada bir delik buldu
@tohum: keloglan-0057
@degisim: bindirmek -> karıştırmak
Rüzgar esiyordu ve tepeden tuhaf bir ses geliyordu. Keloğlan tozlu bir taşa oturmuş, kalemiyle resim çiziyordu. Bu sesi çok merak etti. Eşeği Karakaçan da yanında otluyordu. Keloğlan biraz sakardı ve önce bunu eşeğinin sesiyle karıştırdı. "Karakaçan, bunu sen mi yapıyorsun?" diye sordu Keloğlan. Karakaçan başını iki yana salladı. Keloğlan sesin peşinden kayaların arasına yürüdü. Karakaçan da arkasından geldi. Büyük bir kayada küçük bir delik vardı. Rüzgar bu delikten geçerken ıslık gibi bir ses çıkıyordu. Keloğlan kalemiyle deliği de resmine çizdi. "Bak, Karakaçan, sesi yapan bu küçük delik!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan biraz sakardı ve"
   - Cümle 5: «Keloğlan biraz sakardı ve önce bunu eşeğinin sesiyle karıştırdı.»
   - Açıklama: Sesleri karıştırmak sakarlık değildir; 'sakar' yanlış anlamda kullanılmış.
   - Açıklama: 'Sakar' beceriksiz demektir; sesi karıştırmayı anlatmak için yanlış anlamda kullanılmış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve önce bunu eşeğinin sesiyle karıştırdı"
   - Cümle 5: «Keloğlan biraz sakardı ve önce bunu eşeğinin sesiyle karıştırdı.»
   - Açıklama: Sakarlık sesi karıştırmaya sebep olmuyor ve tepeden gelen ses yanındaki eşekle karıştırılıyor, bu ayrıntı olaydan çıkmıyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "önce bunu eşeğinin sesiyle karıştırdı"
   - Cümle 5: «Keloğlan biraz sakardı ve önce bunu eşeğinin sesiyle karıştırdı.»
   - Açıklama: Ses tepeden geliyor ama Keloğlan onu hemen yanında otlayan eşeğin sesiyle karıştırıyor, bu çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0057` birebir aynı, `@degisim: bindirmek -> karıştırmak` (tutuyorsan), ardından `@onarim: 874a33a657de1e3edc48a05cad70c65143e5171e`, sonra gövde.

### Hikâye 4: tohum keloglan-0058 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Bilgecan Dede
@tohum: keloglan-0058
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'atkı', fiil 'kutlamak', sıfat 'yetenekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | Bilgecan Dede
@plan: ikisi ipi aynı anda çekti ve topaç devrildi | sırayla oynamayı önerdi ve ipi düzgünce sardı
@tohum: keloglan-0058
@degisim: atkı -> topaç
Keloğlan ile Bilgecan Dede evde tahta bir topaçla oynuyordu. Topaç dedenin yeni icadıydı ve yalnız bir ipi vardı. İkisi de ipi aynı anda çekti ve topaç devrildi. "Sırayla oynayalım, önce sen çevir, dede," dedi Keloğlan. Dede ipi çekti ve topaç masada uzun uzun döndü. "Sen çok yeteneklisin, dede!" dedi Keloğlan. Sonra sıra Keloğlan'a geldi. Keloğlan sakar davrandı, ipi karıştırdı ve topaç masadan düştü. Keloğlan ipi bu kez düzgünce sardı ve çekti. Topaç da dedeninki kadar uzun döndü. İkisi bu güzel dönüşü el çırparak kutladı. Keloğlan çok sevindi, çünkü sırayla oynamak ikisini de mutlu etmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedenin yeni icadıydı"
   - Cümle 2: «Topaç dedenin yeni icadıydı ve yalnız bir ipi vardı.»
   - Açıklama: 'İcat' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: ""Sen çok yeteneklisin, dede!""
   - Cümle 6: «"Sen çok yeteneklisin, dede!" dedi Keloğlan.»
   - Açıklama: 'Yetenekli' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
3. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Keloğlan sakar davrandı, ipi karıştırdı ve topaç masadan düştü"
   - Cümle 8: «Keloğlan sakar davrandı, ipi karıştırdı ve topaç masadan düştü.»
   - Açıklama: İlk sorun sırayla oynayarak çözüldükten sonra topacın düşmesiyle ikinci bir sorun çıkıyor.
   - Açıklama: İlk sorun çözüldükten sonra topacın yeniden düşmesiyle ikinci bir sorun açılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0058` birebir aynı, `@degisim: atkı -> topaç` (tutuyorsan), ardından `@onarim: a3ea7d14c2520263c89802b463ecf1c5a5137df5`, sonra gövde.

### Hikâye 5: tohum keloglan-0060 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0060
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'süs', fiil 'beklemek', sıfat 'sarı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ağacın tepesinden bilinmeyen bir ses geldi | sepet düşünce yerdeki armutları gördü ve sesi buldu
@tohum: keloglan-0060
@degisim: süs -> armut
Keloğlan ormanda elinde boş bir sepetle yürüyordu. Birden büyük bir ağaçtan pıt pıt diye bir ses geldi. Keloğlan bu sesin ne olduğunu çok merak etti. Başını kaldırdı ama sık dalların arasında hiçbir şey göremedi. Ağacın dibinde sessizce bekledi ama ses bir daha gelmedi. Sonra ayağa kalktı ve sakarlıkla sepetini düşürdü. Sepet ağacın öbür yanına yuvarlandı. Keloğlan sepetin peşinden gitti ve yerde küçük sarı armutlar gördü. Tam o sırada daldan bir armut daha pıt diye düştü. Ses bu armutlardan geliyordu. Keloğlan armutları tek tek topladı ve sepetine koydu. Sonra dolu sepetiyle ağacın altında mutlu mutlu ıslık çaldı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ayağa kalktı ve sakarlıkla"
   - Cümle 6: «Sonra ayağa kalktı ve sakarlıkla sepetini düşürdü.»
   - Açıklama: 'Sakarlıkla' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sakarlıkla sepetini düşürdü"
   - Cümle 6: «Sonra ayağa kalktı ve sakarlıkla sepetini düşürdü.»
   - Açıklama: Çözüm Keloğlan'ın sese yönelmesiyle değil, rastgele bir kazayla geliyor.
   - Açıklama: Çözüm Keloğlan'ın sese yönelik bir eylemiyle değil, kazara sepetin düşmesiyle geliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepet ağacın öbür yanına yuvarlandı"
   - Cümle 7: «Sepet ağacın öbür yanına yuvarlandı.»
   - Açıklama: Armutlar sebebe yönelen bir eylemle değil, sebepsiz bir tesadüfle bulunuyor.
   - Açıklama: Sesin kaynağı sebepsiz bir tesadüfle, yuvarlanan sepetin peşinden gidilince bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0060` birebir aynı, `@degisim: süs -> armut` (tutuyorsan), ardından `@onarim: f6ff1d0fbffadf985db180dece5d11b923371696`, sonra gövde.

### Hikâye 6: tohum keloglan-0061 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0061
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'davul', fiil 'parıldamak', sıfat 'saygılı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: annesine sormadan tencereyi alıp davul gibi çaldı | özür dileyip tencereyi geri verdi
@tohum: keloglan-0061
Keloğlan davul çalmayı öğrenmek istiyordu ama evde davul yoktu. Anasına sormadan mutfaktan parıldayan büyük tencereyi aldı. Tencereyi ters çevirdi ve kaşıkla davul gibi çaldı. Tam o sırada anası mutfağa girdi. "Keloğlan, tencerem nerede, çorba pişirecektim," dedi anası. Keloğlan tencereyi hemen anasına geri verdi. "Sormadan aldım, özür dilerim, anneciğim," dedi Keloğlan saygılı bir sesle. Anası gülümsedi ve onu kucakladı. Sonra dolaptan eski bir tahta kova çıkardı. "Bu kova senin davulun olsun," dedi anası. Anası çorbayı pişirirken Keloğlan kovaya kaşıkla vurdu. İkisi mutfakta mutlu mutlu şarkı söyledi.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "davul çalmayı öğrenmek istiyordu ama evde davul yoktu"
   - Cümle 1: «Keloğlan davul çalmayı öğrenmek istiyordu ama evde davul yoktu.»
   - Açıklama: Tencereyi sormadan alma sorununun yanında davulsuzluk ayrı bir sorun olarak kuruluyor ve onu da anası kovayla çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0061` birebir aynı, ardından `@onarim: 05aafc0ea93b4cf76e58d0135fb64d69ce5f951f`, sonra gövde.

### Hikâye 7: tohum keloglan-0062 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0062
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'kurdele', fiil 'bakmak', sıfat 'yuvarlak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: çember hep devrildi çünkü yalnız değneğe bakıyordu | dedeye sordu ve ileriye bakarak itti
@tohum: keloglan-0062
@degisim: kurdele -> değnek
Bir sabah Bilgecan Dede tepede Keloğlan'a yuvarlak bir çember getirdi. Keloğlan çemberi kısa bir değnekle itti ama çember hep devrildi. Çünkü Keloğlan yalnız değneğin ucuna bakıyordu. Bir kez çember yuvarlandı ve bir çalının içine girdi. Keloğlan çemberi çalıdan çıkardı ve çok güldü. "Dede, çember neden hep düşüyor?" diye sordu Keloğlan. "Değneğe değil, ileriye bak," dedi Bilgecan Dede. Keloğlan bu kez başını kaldırdı ve önüne baktı. Çember düz bir yolda uzun uzun yuvarlandı. Keloğlan yeni bir oyun öğrendiği için çok sevindi. Sonra ikisi sırayla çember çevirip tepede mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çünkü yalnız değneğe bakıyordu"
   - Cümle 0 (plan satırı): «çember hep devrildi çünkü yalnız değneğe bakıyordu | dedeye sordu ve ileriye bakarak itti»
   - Açıklama: Plan satırında değneğe bakanın kim olduğu belli değil; dilbilgisel özne çember gibi okunuyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Keloğlan'a yuvarlak bir çember"
   - Cümle 1: «Bir sabah Bilgecan Dede tepede Keloğlan'a yuvarlak bir çember getirdi.»
   - Açıklama: Çember zaten yuvarlaktır; gereksiz tekrar.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir kez çember yuvarlandı ve bir çalının içine girdi"
   - Cümle 4: «Bir kez çember yuvarlandı ve bir çalının içine girdi.»
   - Açıklama: Çemberin çalıya girmesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Çalıya kaçma olayı sorunla ya da çözümle bağlantısız, işlevsiz bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0062` birebir aynı, `@degisim: kurdele -> değnek` (tutuyorsan), ardından `@onarim: 8b4a0ffafea6d30ae7f58a9cae0f5df0a28ef9d7`, sonra gövde.

### Hikâye 8: tohum keloglan-0063 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0063
- yer: dağ (Köyün yakınındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kağıt', fiil 'sıçramak', sıfat 'kilitli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: rüzgar kağıt uçağı sepetten uzağa itti | rüzgarın durmasını bekledi ve uçağı yavaşça attı
@tohum: keloglan-0063
@degisim: kilitli -> beyaz
Rüzgar tepede hafif hafif esiyordu. Keloğlan beyaz kağıttan uçağını Karakaçan'ın sırtındaki sepete atmak istiyordu. Ama rüzgar kağıt uçağı her seferinde sepetten uzağa itti. Bir kez uçak eşeğin kulağına kondu. Karakaçan şaşırdı ve yerinde sıçradı. Keloğlan buna çok güldü. Sonra uçak sepetin hemen yanına düştü. "Bu olmadı, uçak dışarıda kaldı," dedi Keloğlan. Dürüst davrandı ve bunu saymadı. Keloğlan bu kez rüzgarın durmasını bekledi. Rüzgar durunca uçağı yavaşça attı. Kağıt uçak süzüldü ve sepetin içine girdi. Karakaçan başını salladı ve neşeyle anırdı. Keloğlan çok sevindi, çünkü kağıt uçağı sonunda sepete sokmuştu.
```

**Hakem bulguları (6):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Keloğlan beyaz kağıttan uçağını"
   - Cümle 2: «Keloğlan beyaz kağıttan uçağını Karakaçan'ın sırtındaki sepete atmak istiyordu.»
   - Açıklama: Masal köyü dünyasında uçak çağdaş araç kategorisindedir ve kartta böyle bir eşya yok.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bir kez uçak eşeğin kulağına kondu"
   - Cümle 4: «Bir kez uçak eşeğin kulağına kondu.»
   - Açıklama: Karakaçan'ın eşek olduğu söylenmeden 'eşeğin' deniyor; kimin kastedildiği belli değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "uçak eşeğin kulağına kondu"
   - Cümle 4: «Bir kez uçak eşeğin kulağına kondu.»
   - Açıklama: Karakaçan'ın eşek olduğu söylenmeden 'eşeğin' deniyor; bunun Karakaçan mı başka bir eşek mi olduğu belirsiz.
4. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "Keloğlan buna çok güldü"
   - Cümle 6: «Keloğlan buna çok güldü.»
   - Açıklama: Keloğlan, kulağına uçak konup şaşıran eşeğine gülüyor; bu alay örnek alınacak biçimde gösteriliyor.
   - Açıklama: Keloğlan, kulağına uçak konup ürken eşeğe gülüyor; bu bir hayvanla alay etme örneği gibi okunabilir.
5. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: ""Bu olmadı, uçak dışarıda kaldı," dedi Keloğlan"
   - Cümle 8: «"Bu olmadı, uçak dışarıda kaldı," dedi Keloğlan.»
   - Açıklama: Keloğlan kimseye seslenmeden kendi kendine konuşuyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dürüst davrandı ve bunu saymadı"
   - Cümle 9: «Dürüst davrandı ve bunu saymadı.»
   - Açıklama: Sayılan bir skor ya da kural kurulmadığı için dürüstlük cümlesi işlevsiz bir ayrıntı olarak kalıyor.
   - Açıklama: Hiçbir sayı ya da puan kurulmamışken saymama ayrıntısı sebepsiz beliriyor ve olaya bir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0063` birebir aynı, `@degisim: kilitli -> beyaz` (tutuyorsan), ardından `@onarim: 1583d1ccbbcb6dbd4836e00da9e487b1d3478375`, sonra gövde.
