# Editör görevi (onarım): Maşa, onarım partisi 3

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar3.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Maşa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar3.txt --ad urun_v2`
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

## Kart: Maşa (kaynaklı, kapalı dünya)

- Ad: Maşa (okunuş: maşa; kesme eki okunuşa uyar)
- Kimlik: Maşa, ormanın yakınındaki evinde yaşayan, çok enerjik ve oyun seven küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Maşa'nın denemeleri kimseyi incitmez; kimse düşmez, bir şey kırılıp kimseyi yaralamaz. Yüksek yere çıkmaz, ateşe ve derin suya yaklaşmaz.
- Özellikler:
  - dene: Çok enerjiktir; her şeyi dener. (örnek biçimler: denedi, denemek, deniyordu)
  - reçel: Tatlıları ve reçeli çok sever. (örnek biçimler: reçel, reçeli)
- Yerler:
  - orman: Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.
  - dağ: Ormanın yanındaki tepe.
  - ev: Maşa'nın evi ve önündeki bahçe.
    - yan Koca Ayı ise: Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Koca Ayı: Maşa'nın eski dostu; iyi kalpli ve her işi bilen bir ayı. Tür: ayı; KONUŞMAZ. Yüzey biçimleri: Koca Ayı, ayı
  - kirpi: Ormanda yaşayan, elmayı seven dost canlısı bir kirpi. Tür: kirpi; KONUŞMAZ. Yüzey biçimleri: kirpi
  - sincap: Ormanda küçük bir yuvada yaşayan hızlı sincap; fındık ve meşe palamudu sever. Tür: sincap; KONUŞMAZ. Yüzey biçimleri: sincap
  - Daşa: Maşa'nın şehirde yaşayan kuzeni; düşünceli, ciddi ve akıllı bir kız. Tür: kız; konuşur. Yüzey biçimleri: Daşa, kuzen, kuzeni
- Dünya kuralları:
  - Koca Ayı, kirpi ve sincap konuşmaz; sesle, hareketle ve yüzüyle anlatır. Yalnız Maşa ve Daşa konuşur.
  - Daşa şehirde yaşar; Maşa'yı ziyarete gelir.
- Yasak adlar: Rosie, Panda, Kaplan, Ayı Hanım, Siyah Ayı, Kurnaz Kurt, Aptal Kurt, Penguen
- Yasak: Kurtlar, sirk gösterisi ve ambulans hikayeye girmez.
- İzinli dünya kelimeleri: reçel, ayı, sincap, kirpi, patika

## Onarılacak hikâyeler

### Hikâye 1: tohum masa-0001 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | sincap, Daşa
@tohum: masa-0001
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kadife', fiil 'çevirmek', sıfat 'dikkatli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | sincap, Daşa
@plan: torbayı sormadan çevirdi ve fındıklar döküldü | kuzeninden özür diledi ve fındıkları topladı
@tohum: masa-0001
@degisim: kadife -> bez
Maşa'nın evinin önünde Daşa, sincap için bez bir torbada fındık tutuyordu. Maşa torbayı sormadan aldı ve havada çevirmeyi denedi. Torbanın ağzı açıldı ve bütün fındıklar çimenlere döküldü. Sincap ağaçtan indi ve dökülen fındıklara baktı. Daşa üzüldü. Maşa hemen durdu ve Daşa'ya baktı. "Özür dilerim, Daşa, torbanı sormadan aldım," dedi Maşa. "Tamam, ama bundan sonra bana sor," dedi Daşa. Maşa fındıkları dikkatli bir şekilde topladı. Hepsini yeniden bez torbaya koydu ve torbayı Daşa'ya verdi. Daşa fındıkları sincabın önüne koydu. Sincap bir fındık aldı ve hızlı hızlı yedi. Maşa çok sevindi, çünkü hem Daşa hem de sincap artık mutluydu.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kuzeninden özür diledi ve fındıkları topladı"
   - Cümle 0 (plan satırı): «torbayı sormadan çevirdi ve fındıklar döküldü | kuzeninden özür diledi ve fındıkları topladı»
   - Açıklama: Plan fındıkları Maşa'nın topladığını söylüyor ama gövdede fındıkları sincap topluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0001` birebir aynı, `@degisim: kadife -> bez` (tutuyorsan), ardından `@onarim: 9497fa1e9e3fb81f770c3ec7fcbac21388f2e1f7`, sonra gövde.

### Hikâye 2: tohum masa-0002 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0002
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'silgi', fiil 'hazırlamak', sıfat 'gizemli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: sepet dala takıldı ve reçel kavanozu kayboldu | reçelin kokusuna doğru gidip kavanozu buldu
@tohum: masa-0002
@degisim: silgi -> kavanoz
Ormanda Koca Ayı, Maşa ile kirpi için kahvaltı hazırlıyordu. Ama sepet bir dala takıldı ve reçel kavanozu düşüp yuvarlandı. Koca Ayı her yere baktı ama kavanozu bulamadı. Maşa, Koca Ayı'ya yardım etmek istedi. Maşa reçeli çok sevdiği için onun kokusunu iyi biliyordu. Burnunu havaya kaldırdı ve derin derin kokladı. Çalıların arkasından gizemli bir koku geliyordu. Maşa onu tanıdı, bu reçelin tatlı kokusuydu. Maşa hemen çalılara koştu. Kavanoz orada, çimenlerin üstünde duruyordu. "Buldum, Koca Ayı, işte reçel!" dedi Maşa. Koca Ayı sevinçle kavanozu aldı ve ekmeklere reçel sürdü. Kirpi de burnunu kavanoza uzattı. "Kahvaltı hazır, hadi hep birlikte yiyelim!" dedi Maşa.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçeli çok sevdiği için onun kokusunu iyi biliyordu"
   - Cümle 5: «Maşa reçeli çok sevdiği için onun kokusunu iyi biliyordu.»
   - Açıklama: Kartın özellikler alanındaki reçel sevgisi, kartta olmayan uzaktan koku alıp kavanozun izini sürme yeteneğine çevriliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "arkasından gizemli bir koku"
   - Cümle 7: «Çalıların arkasından gizemli bir koku geliyordu.»
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki bir çocuk bilmez.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çalıların arkasından gizemli bir koku geliyordu"
   - Cümle 7: «Çalıların arkasından gizemli bir koku geliyordu.»
   - Açıklama: Kavanozun açıldığı ya da kırıldığı söylenmediği halde kapalı kavanozdan koku gelmesi çözümü sebepsizce getiriyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Çalıların arkasından gizemli bir koku geliyordu"
   - Cümle 7: «Çalıların arkasından gizemli bir koku geliyordu.»
   - Açıklama: Kavanoz kırılmadan sağlam duruyor ve sonra reçeli ekmeğe sürülüyor, yine de kapalı kavanozdan çalıların arkasına kadar koku geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0002` birebir aynı, `@degisim: silgi -> kavanoz` (tutuyorsan), ardından `@onarim: f9b6798ebb1a84a44817b5662d5ae78f0fc3c9a9`, sonra gövde.

### Hikâye 3: tohum masa-0003 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0003
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'inci', fiil 'barışmak', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: rüzgar ağaçtaki kurdeleyi uçurdu ve ağaç bulunamadı | ağaçların dibine bakıp sepeti buldu
@tohum: masa-0003
@degisim: barışmak -> bağlamak
Rüzgar hızlı hızlı esiyordu. Maşa, kuzeni Daşa için işaretli bir ağacın dibine küçük bir sepet koymuştu. Sepette inci gibi beyaz çiçekler vardı. Ama rüzgar ağaçtaki kırmızı kurdeleyi uçurdu ve Maşa ağacı bulamadı. Daşa biraz ileride gözlerini kapatmış bekliyordu. Maşa sepeti aramayı denedi. Her ağacın dibine dikkatle baktı. Sonunda bir ağacın dibinde küçük sepeti gördü. Maşa sepeti aldı ve Daşa'nın yanına koştu. Daşa gözlerini açtı ve çiçekleri görünce çok sevindi. Maşa bir çiçeği Daşa'nın saçına taktı ve iki kız birlikte güldü. Maşa, kurdeleyi dala sıkıca bağlamak gerektiğini öğrendi.
```

**Hakem bulguları (8):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sepette inci gibi beyaz"
   - Cümle 3: «Sepette inci gibi beyaz çiçekler vardı.»
   - Açıklama: 'İnci gibi' benzetmesi mecazlı ve 3 yaşındaki çocuk için bilinmeyen bir kelime içeriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "inci gibi beyaz çiçekler"
   - Cümle 3: «Sepette inci gibi beyaz çiçekler vardı.»
   - Açıklama: 'İnci gibi' benzetmesi mecazdır ve 3 yaşındaki çocuk 'inci' kelimesini bilmeyebilir.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "rüzgar ağaçtaki kırmızı kurdeleyi uçurdu"
   - Cümle 4: «Ama rüzgar ağaçtaki kırmızı kurdeleyi uçurdu ve Maşa ağacı bulamadı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar ağaçtaki kırmızı kurdeleyi uçurdu ve Maşa ağacı bulamadı"
   - Cümle 4: «Ama rüzgar ağaçtaki kırmızı kurdeleyi uçurdu ve Maşa ağacı bulamadı.»
   - Açıklama: Sepet ağacın dibinde durduğu için kurdele gidince ağacın bulunamaması akla yatkın bir sebep değil.
5. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Maşa ağacı bulamadı"
   - Cümle 4: «Ama rüzgar ağaçtaki kırmızı kurdeleyi uçurdu ve Maşa ağacı bulamadı.»
   - Açıklama: Maşa'nın kendi koyduğu sepeti bulamaması zayıf bir sorun ve her ağaca bakınca hemen bitiyor; 'dağıttı, topladı, bitti' türünde önemsiz bir olay.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa sepeti aramayı denedi"
   - Cümle 6: «Maşa sepeti aramayı denedi.»
   - Açıklama: 'Aramayı denedi' anlamca uygun değil; 'aramaya başladı' olmalı.
   - Açıklama: 'Aramayı denedi' yanlış anlamda; Maşa sepeti aradı, aramayı denemedi.
7. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa sepeti aramayı denedi"
   - Cümle 6: «Maşa sepeti aramayı denedi.»
   - Açıklama: Tohumdaki özellik enerjiyle her şeyi denemek; sepeti aramak bu özelliği işe yarar biçimde göstermiyor, fiil yalnız kelime olarak eklenmiş.
   - Açıklama: Kartın özellikler alanındaki her şeyi deneme özelliği yalnız sıradan bir arama fiili olarak geçiyor, yeni bir şey denenmiyor.
8. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Her ağacın dibine dikkatle baktı"
   - Cümle 7: «Her ağacın dibine dikkatle baktı.»
   - Açıklama: Çözüm kaybolan işarete yönelmiyor, her ağaca tek tek bakan uzun bir aramaya dönüşüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0003` birebir aynı, `@degisim: barışmak -> bağlamak` (tutuyorsan), ardından `@onarim: 4cd00deb61ae73cf03cd8d7e170fe0ddf31a81e2`, sonra gövde.

### Hikâye 4: tohum masa-0005 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0005
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni bir şeyi denemek
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'mermer', fiil 'uyutmak', sıfat 'değerli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: kirpi sert taşın üstünde uyuyamadı | yapraktan yumuşak bir yatak yaptı
@tohum: masa-0005
@degisim: mermer -> taş
Bir sabah Maşa ormanda bir kirpi gördü. Kirpi büyük bir taşın üstünde uyumaya çalışıyordu. Ama taş çok sertti ve kirpi uyuyamadı. Maşa daha önce hiç yapraktan yatak yapmamıştı. Ama bu yeni işi hemen denedi. Ağaçların altından yumuşak yapraklar topladı. Yaprakları taşın yanına koydu ve küçük bir yatak yaptı. Kirpi taştan indi ve yaprakları kokladı. "Bu senin yeni yatağın, kirpi," dedi Maşa. Kirpi yumuşak yatağa kıvrıldı ve hemen uyudu. Maşa çok sevindi. Bu ilk yatak onun için çok değerliydi, çünkü kirpiyi uyutmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "onun için çok değerliydi"
   - Cümle 12: «Bu ilk yatak onun için çok değerliydi, çünkü kirpiyi uyutmuştu.»
   - Açıklama: 'Değerli' soyut bir kavram ve 3 yaşındaki bir çocuk için uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu ilk yatak onun için çok değerliydi"
   - Cümle 12: «Bu ilk yatak onun için çok değerliydi, çünkü kirpiyi uyutmuştu.»
   - Açıklama: 'Değerli' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bu ilk yatak onun için"
   - Cümle 12: «Bu ilk yatak onun için çok değerliydi, çünkü kirpiyi uyutmuştu.»
   - Açıklama: 'Onun' zamirinin Maşa'yı mı kirpiyi mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0005` birebir aynı, `@degisim: mermer -> taş` (tutuyorsan), ardından `@onarim: 8389a41b0692384b0008269a91725ca985acc117`, sonra gövde.

### Hikâye 5: tohum masa-0006 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0006
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kese', fiil 'asılmak', sıfat 'buzlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: soğukta reçel dondu ve kaşık reçele girmedi | kavanozu elleriyle ısıttı ve reçel yumuşadı
@tohum: masa-0006
@degisim: asılmak -> sürmek
Maşa karlı ormanda ilk kez piknik yapıyordu. Kesesinden ekmeği ve reçel kavanozunu çıkardı. Ama soğukta kavanoz buzlu olmuştu ve reçel donmuştu. Kaşık reçelin içine girmedi. Maşa kaşıkla reçele tık tık vurdu. Reçel çok sertti. Maşa reçeli çok severdi ve onu hemen yemek istiyordu. Biraz düşündü ve kavanozu iki elinin arasına aldı. Elleri sıcacıktı ve kavanozu yavaş yavaş ısıttı. Maşa bir süre bekledi. Sonra kaşığı yeniden reçele soktu. Bu kez kaşık kolayca içine girdi. Maşa reçeli ekmeğine sürdü. Sonra karların arasında oturdu ve ekmeğini mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kesesinden ekmeği ve"
   - Cümle 2: «Kesesinden ekmeği ve reçel kavanozunu çıkardı.»
   - Açıklama: 'Kese' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime; 'çanta' gibi bilinen bir kelime olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0006` birebir aynı, `@degisim: asılmak -> sürmek` (tutuyorsan), ardından `@onarim: 0b30986ca71aab526ce7ab348d5f932739dea7bc`, sonra gövde.

### Hikâye 6: tohum masa-0007 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0007
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kurabiye', fiil 'görünmek', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: saklanan kirpi taşların arasında hiç görünmüyordu | taşların yanına bir kurabiye koyup bekledi
@tohum: masa-0007
@degisim: çevik -> hızlı
Bir sabah Maşa, Koca Ayı ve kirpi tepede sepetten kurabiye yiyordu. Sonra yeni bir oyun oynadılar ve kirpi saklandı. Ama kirpi yuvarlak taşların arasında top gibi kıvrılmıştı ve hiç görünmüyordu. Maşa her taşın arkasına baktı ama kirpiyi bulamadı. Kirpi elmayı çok severdi. Maşa kirpiyi elmalı bir kurabiyeyle dışarı çıkarmayı denedi. Koca Ayı sepeti Maşa'ya uzattı. Maşa sepetten elmalı bir kurabiye aldı. Kurabiyeyi taşların yanına koydu ve sessizce bekledi. Az sonra taşların arasında küçük, dikenli bir şey kıpırdadı. Kirpi burnunu çıkardı ve hızlı adımlarla kurabiyeye koştu. "Buldum seni, kirpi!" dedi Maşa. Sonra üçü kurabiyeleri paylaştı ve oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sonra yeni bir oyun oynadılar ve kirpi saklandı"
   - Cümle 2: «Sonra yeni bir oyun oynadılar ve kirpi saklandı.»
   - Açıklama: Saklambaçta saklananın bulunamaması oyunun doğal parçası, gerçek bir sorun değil ve kurabiyeyle dışarı çekmek oyunu bozuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0007` birebir aynı, `@degisim: çevik -> hızlı` (tutuyorsan), ardından `@onarim: 1fd70c9eedaba48d5f29d643c07a909f7414b8af`, sonra gövde.

### Hikâye 7: tohum masa-0009 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0009
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: paylaşmak
- yan: sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'ay', fiil 'buruşturmak', sıfat 'kararlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: sincap da fındık istedi ve kütükten inmedi | fındıkları saydı ve yarısını sincapla paylaştı
@tohum: masa-0009
@degisim: ay -> fındık
Maşa ormanda bir kütüğe oturdu ve kağıda sarılı fındıklarını açtı. O sırada bir sincap kütüğe zıpladı ve kağıda uzun uzun baktı. Sincap da fındık istiyordu. Sincap kararlıydı ve kütükten hiç inmedi. Maşa fındıkları sincapla paylaşmak istedi. Onları tek tek saymayı denedi ve on fındık buldu. Beş fındığı sincap için kütüğün üstüne koydu. Sincap onları patileriyle tuttu ve hızlı hızlı yedi. Maşa da kendi fındıklarını yedi. Sonra boş kağıdı buruşturdu ve cebine koydu. "Birlikte yemek daha güzelmiş, sincap!" dedi Maşa.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sincap da fındık istiyordu"
   - Cümle 3: «Sincap da fındık istiyordu.»
   - Açıklama: Sincabın fındık istemesi Maşa için gerçek bir sorun oluşturmuyor; Maşa hemen paylaşmak istiyor ve hikayede aşılacak bir güçlük yok.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sincap kararlıydı ve"
   - Cümle 4: «Sincap kararlıydı ve kütükten hiç inmedi.»
   - Açıklama: 'Kararlı' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sincap kararlıydı ve kütükten"
   - Cümle 4: «Sincap kararlıydı ve kütükten hiç inmedi.»
   - Açıklama: 'Kararlı' soyut bir kelime ve figürün kart özelliği değil, sincaba verilmiş.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "tek tek saymayı denedi"
   - Cümle 6: «Onları tek tek saymayı denedi ve on fındık buldu.»
   - Açıklama: Maşa fındıkları gerçekten saydığı halde 'denedi' ve 'on fındık buldu' sayma eylemine uymuyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Onları tek tek saymayı denedi"
   - Cümle 6: «Onları tek tek saymayı denedi ve on fındık buldu.»
   - Açıklama: Tohumdaki özellik enerjiyle her şeyi denemek; fındık saymak bu özelliği işe yarar biçimde göstermiyor, fiil yalnız kelime olarak eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0009` birebir aynı, `@degisim: ay -> fındık` (tutuyorsan), ardından `@onarim: d3b80bb81586048a7404a6817d7f72252b07bd30`, sonra gövde.

### Hikâye 8: tohum masa-0010 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0010
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'vazo', fiil 'durdurmak', sıfat 'şık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: vazoya giren kirpi dışarı çıkamadı | vazoyu yavaşça eğdi ve kirpi dışarı kaydı
@tohum: masa-0010
@degisim: şık -> boş
Rüzgar hızlı hızlı esiyordu. Maşa evinin önünde zıplarken rüzgarın devirdiği boş vazodan bir ses duydu. Rüzgardan saklanan bir kirpi vazoya girmişti. Ama vazonun içi kaygandı ve kirpi dışarı yürüyemiyordu. Maşa hemen zıplamayı durdurdu ve vazonun yanına koştu. "Bekle, kirpi, sana yardım edeceğim," dedi Maşa. Maşa vazonun dibini yavaşça yukarı kaldırmayı denedi. Vazonun ağzı çimenlere doğru eğildi. Kirpi yavaş yavaş kaydı ve çimenlerin üstüne çıktı. Kirpi küçük burnunu kıpırdattı ve Maşa'ya baktı. "Oldu, kirpi, artık çıktın!" dedi Maşa. Sonra boş vazoyu dikkatle yerine koydu. Kirpi de çimenlerde mutlu mutlu dolaştı. Maşa çok sevindi, çünkü kirpiyi vazodan çıkarmıştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "kirpi dışarı yürüyemiyordu"
   - Cümle 4: «Ama vazonun içi kaygandı ve kirpi dışarı yürüyemiyordu.»
   - Açıklama: Kirpinin vazodan çıkamaması ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0010` birebir aynı, `@degisim: şık -> boş` (tutuyorsan), ardından `@onarim: bd9b07bb6f31a81cd60314a168be97e223b842a0`, sonra gövde.
