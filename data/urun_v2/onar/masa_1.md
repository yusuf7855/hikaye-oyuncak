# Editör görevi (onarım): Maşa, onarım partisi 1

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar1.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar1.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0001 (deneme 1 -> 2)

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
Bahçede Daşa, sincap için kadife bir torbada fındık getirmişti. Maşa torbayı sormadan aldı ve havada çevirmeyi denedi. Torbanın ağzı açıldı ve bütün fındıklar çimenlere döküldü. Sincap ağaçtan indi ve dökülen fındıklara baktı. Daşa üzüldü. Maşa hemen durdu ve kuzenine baktı. "Özür dilerim, Daşa, torbanı sormadan aldım," dedi Maşa. "Tamam, ama bundan sonra bana sor," dedi Daşa. Maşa çimenlere eğildi. Fındıkları dikkatli bir şekilde tek tek topladı. Hepsini yeniden kadife torbaya koydu ve torbayı Daşa'ya verdi. Daşa fındıkları sincabın önüne koydu. Sincap bir fındık aldı ve hızlı hızlı yedi. Maşa çok sevindi, çünkü hem kuzeni hem de sincap artık mutluydu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "kadife bir torbada fındık"
   - Cümle 1: «Bahçede Daşa, sincap için kadife bir torbada fındık getirmişti.»
   - Açıklama: 'Kadife' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede Daşa, sincap için"
   - Cümle 1: «Bahçede Daşa, sincap için kadife bir torbada fındık getirmişti.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor ve bahçede bitiyor.
   - Açıklama: Başlıktaki yer ev iken hikaye bahçede başlıyor ve bahçede bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0001` birebir aynı, ardından `@onarim: 9229349f297fb929c0b81cda9a39db9e7e40e2f3`, sonra gövde.

### Hikâye 2: tohum masa-0002 (deneme 1 -> 2)

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
@plan: reçel kavanozu sepetten düşüp kayboldu | reçelin kokusunu takip edip kavanozu buldu
@tohum: masa-0002
@degisim: silgi -> kavanoz
Ormanda Koca Ayı, Maşa ile kirpi için kahvaltı hazırlıyordu. Ama reçel kavanozu sepetten düşmüş ve bir yere yuvarlanmıştı. Koca Ayı her yere baktı ama kavanozu bulamadı. Maşa, Koca Ayı'ya yardım etmek istedi. Maşa reçeli çok sevdiği için onun kokusunu iyi biliyordu. Burnunu havaya kaldırdı ve derin derin kokladı. Çalıların arkasından gizemli, tatlı bir koku geliyordu. Maşa hemen çalılara koştu. Kavanoz orada, çimenlerin üstünde duruyordu. "Buldum, Koca Ayı, işte reçel!" dedi Maşa. Koca Ayı sevinçle kavanozu aldı ve ekmeklere reçel sürdü. Kirpi de burnunu kavanoza uzattı. "Kahvaltı hazır, hadi hep birlikte yiyelim!" dedi Maşa.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "gizemli, tatlı bir koku"
   - Cümle 7: «Çalıların arkasından gizemli, tatlı bir koku geliyordu.»
   - Açıklama: 'Gizemli' soyut bir kelime ve 3 yaşındaki çocuğun bilmeyeceği bir sözcük.
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Çalıların arkasından gizemli, tatlı bir koku geliyordu"
   - Cümle 7: «Çalıların arkasından gizemli, tatlı bir koku geliyordu.»
   - Açıklama: Sağlam duran, dökülmemiş bir kavanozun çalıların arkasından koku yayması çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0002` birebir aynı, `@degisim: silgi -> kavanoz` (tutuyorsan), ardından `@onarim: 59455b883bd7f533d729424de8118d197e91dc43`, sonra gövde.

### Hikâye 3: tohum masa-0003 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar ağaçtaki kurdeleyi uçurdu ve ağaç bulunamadı | bütün ağaçların dibine tek tek baktı
@tohum: masa-0003
@degisim: barışmak -> bağlamak
Rüzgar hızlı hızlı esiyordu. Maşa, Daşa için işaretli bir ağacın dibine inci bir kolye saklamıştı. Ama rüzgar ağaçtaki kırmızı kurdeleyi uçurdu ve Maşa ağacı bulamadı. Daşa biraz ileride gözlerini kapatmış bekliyordu. Maşa ağaçların dibine tek tek bakmayı denedi. İlk ağacın dibinde yalnız yapraklar vardı. İkinci ağacın dibinde küçük taşlar vardı. Üçüncü ağacın dibinde beyaz inci kolye parlıyordu. Maşa kolyeyi aldı ve Daşa'nın yanına koştu. Daşa gözlerini açtı ve kolyeyi görünce çok sevindi. Maşa kolyeyi kuzeninin boynuna taktı ve iki kız birlikte güldü. Maşa bundan sonra sürpriz saklarken kurdeleyi dala sıkıca bağladı.
```

**Hakem bulguları (4):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa ağaçların dibine tek tek bakmayı denedi"
   - Cümle 5: «Maşa ağaçların dibine tek tek bakmayı denedi.»
   - Açıklama: Çözüm kurdelenin kaybına yönelmiyor, ağaçları tek tek aramak üç adımlık bir tarama oluyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kolyeyi kuzeninin boynuna"
   - Cümle 11: «Maşa kolyeyi kuzeninin boynuna taktı ve iki kız birlikte güldü.»
   - Açıklama: Daşa'nın kuzen olduğu daha önce söylenmediği için 'kuzeni' yeni biri gibi okunuyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa bundan sonra sürpriz saklarken kurdeleyi dala sıkıca bağladı"
   - Cümle 12: «Maşa bundan sonra sürpriz saklarken kurdeleyi dala sıkıca bağladı.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılırken tek seferlik '-dı' kullanılmış; 'bağlardı' olmalı.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Maşa bundan sonra sürpriz saklarken"
   - Cümle 12: «Maşa bundan sonra sürpriz saklarken kurdeleyi dala sıkıca bağladı.»
   - Açıklama: Son cümle hikayenin zamanından çıkıp ileriki günlere atlıyor.
   - Açıklama: Son cümle 'bundan sonra' diyerek sahneden çıkıp gelecekteki başka zamanlara atlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0003` birebir aynı, `@degisim: barışmak -> bağlamak` (tutuyorsan), ardından `@onarim: bb6185146b2d983711c9da83427eeed90f6c918a`, sonra gövde.

### Hikâye 4: tohum masa-0004 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0004
- yer: dağ (Ormanın yanındaki tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kum', fiil 'sunmak', sıfat 'zor'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: en büyük fındık iki taşın arasına yuvarlandı | uzun bir dalla fındığı dışarı itti
@tohum: masa-0004
@degisim: kum -> dal
Bir sabah Maşa, Koca Ayı ve sincap ile tepede fındık topluyordu. Birden en büyük fındık yuvarlandı ve iki taşın arasına girdi. Sincap patisini uzattı ama fındığı çıkarmak ona çok zordu. Maşa sincaba yardım etmek istedi. Önce fındığı parmaklarıyla çekmeyi denedi. Ama fındık çok içerideydi. Sonra Maşa yerde uzun, ince bir dal buldu. Dalı taşların arasına soktu ve fındığı yavaşça itti. Fındık yuvarlandı ve dışarı çıktı. Sincap sevinçle zıpladı ve fındığı Maşa'ya sundu. Maşa gülerek fındığı Koca Ayı'nın sepetine koydu. Sonra üçü tepede oturdu ve fındıkları mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa, Koca Ayı ve sincap ile tepede"
   - Cümle 1: «Bir sabah Maşa, Koca Ayı ve sincap ile tepede fındık topluyordu.»
   - Açıklama: Sayma dizisinin sonunda 'ile' kullanılması cümleyi bozuyor; 'Maşa, Koca Ayı ve sincap tepede' olmalı.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Bir sabah Maşa, Koca Ayı ve sincap ile"
   - Cümle 1: «Bir sabah Maşa, Koca Ayı ve sincap ile tepede fındık topluyordu.»
   - Açıklama: Maşa'dan sonraki virgül cümleyi sıralama gibi gösteriyor; 'Maşa, Koca Ayı ve sincapla' ya da virgülsüz yazılmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fındığı çıkarmak ona çok zordu"
   - Cümle 3: «Sincap patisini uzattı ama fındığı çıkarmak ona çok zordu.»
   - Açıklama: Yapı bozuk; 'onun için çok zordu' ya da 'ona çok zor geldi' olmalı.
   - Açıklama: 'Ona zordu' yanlış; 'onun için çok zordu' olmalı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "fındığı Maşa'ya sundu"
   - Cümle 10: «Sincap sevinçle zıpladı ve fındığı Maşa'ya sundu.»
   - Açıklama: 'Sunmak' 3 yaşındaki çocuğun bilmeyeceği resmi bir kelime; 'verdi' olmalı.
   - Açıklama: 'Sundu' 3 yaşındaki çocuğun bilmeyeceği resmi bir kelime; 'verdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0004` birebir aynı, `@degisim: kum -> dal` (tutuyorsan), ardından `@onarim: 85cada989155e03cd7fbd3522ed73a74acc62cd3`, sonra gövde.

### Hikâye 5: tohum masa-0005 (deneme 1 -> 2)

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
@degisim: değerli -> yumuşak
Bir sabah Maşa ormanda bir kirpi gördü. Kirpi büyük bir mermer taşın üstünde uyumaya çalışıyordu. Ama taş çok sertti ve kirpi uyuyamadı. Maşa daha önce hiç yapraktan yatak yapmamıştı. Ama bu yeni işi hemen denedi. Ağaçların altından yumuşak yapraklar topladı ve taşın üstüne koydu. Maşa o kadar çok yaprak koydu ki kirpi yaprakların altında kayboldu. Sonra kirpi burnunu yaprakların arasından çıkardı. Maşa bunu görünce çok güldü. "Bu yatak biraz fazla büyük oldu, kirpi," dedi Maşa. Yaprakların yarısını aldı ve yatağı düzeltti. Kirpi yumuşak yatağa kıvrıldı ve hemen uyudu. Maşa çok sevindi, çünkü yaptığı ilk yatak kirpiyi uyutmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "büyük bir mermer taşın"
   - Cümle 2: «Kirpi büyük bir mermer taşın üstünde uyumaya çalışıyordu.»
   - Açıklama: 'Mermer' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Mermer' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Maşa o kadar çok yaprak koydu ki kirpi yaprakların altında kayboldu"
   - Cümle 7: «Maşa o kadar çok yaprak koydu ki kirpi yaprakların altında kayboldu.»
   - Açıklama: Çözüm fazla yaprak yüzünden ikinci bir düzeltme adımı gerektiriyor ve 2 adımı aşıyor.
   - Açıklama: Çözüm fazla yaprak koyma ve yarısını geri alma sapmasıyla iki adımı aşıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yaprakların yarısını aldı ve yatağı düzeltti"
   - Cümle 11: «Yaprakların yarısını aldı ve yatağı düzeltti.»
   - Açıklama: Çözüm Maşa'nın kendi yarattığı fazla yaprak sorunu yüzünden ek bir düzeltme adımıyla uzuyor ve iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0005` birebir aynı, `@degisim: değerli -> yumuşak` (tutuyorsan), ardından `@onarim: 238b97a8563c935ecf813443f298e2339386fc1d`, sonra gövde.

### Hikâye 6: tohum masa-0006 (deneme 1 -> 2)

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
@plan: soğukta reçel buzlu oldu ve kaşık girmedi | kavanozu elleriyle ısıttı ve reçel yumuşadı
@tohum: masa-0006
@degisim: asılmak -> sürmek
Maşa karlı ormanda ilk kez piknik yapıyordu. Kesesinden ekmeği ve reçel kavanozunu çıkardı. Ama soğukta reçel buzlu olmuştu ve kaşık içine girmedi. Maşa kaşıkla reçele tık tık vurdu. Reçel çok sertti. Maşa reçeli çok severdi ve onu hemen yemek istiyordu. Biraz düşündü ve kavanozu iki elinin arasına aldı. Elleri sıcacıktı ve kavanozu yavaş yavaş ısıttı. Maşa bir süre bekledi. Sonra kaşığı yeniden reçele soktu. Bu kez kaşık kolayca girdi. Maşa ekmeğine bol bol reçel sürdü. Sonra karların arasında oturdu ve ekmeğini mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "buzlu oldu ve kaşık girmedi"
   - Cümle 0 (plan satırı): «soğukta reçel buzlu oldu ve kaşık girmedi | kavanozu elleriyle ısıttı ve reçel yumuşadı»
   - Açıklama: Plan satırında 'girmedi' fiilinin yönelme tümleci eksik; 'kaşık içine girmedi' ya da 'kaşık reçele girmedi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0006` birebir aynı, `@degisim: asılmak -> sürmek` (tutuyorsan), ardından `@onarim: 96792ef00a245e8db565010340cb3b89c32a4030`, sonra gövde.

### Hikâye 7: tohum masa-0007 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Bir sabah Maşa, Koca Ayı ve kirpi tepede yeni bir oyun oynuyordu. Kirpi saklandı ve Maşa onu aramaya başladı. Ama kirpi yuvarlak taşların arasında top gibi kıvrılmıştı ve hiç görünmüyordu. Maşa her taşın arkasına baktı ama kirpiyi bulamadı. Sonra yeni bir yol denedi. Koca Ayı sepetini Maşa'ya uzattı. Maşa sepetten elmalı bir kurabiye aldı. Kurabiyeyi taşların yanına koydu ve sessizce bekledi. Az sonra taşların arasında küçük, dikenli bir şey kıpırdadı. Kirpi burnunu çıkardı ve çevik adımlarla kurabiyeye koştu. "Buldum seni, kirpi!" dedi Maşa. Sonra üçü kurabiyeleri paylaştı ve oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "Sonra yeni bir yol denedi."
   - Cümle 5: «Sonra yeni bir yol denedi.»
   - Açıklama: 'Yeni bir yol denemek' yöntem anlamında mecazlı bir kullanım.
   - Açıklama: 'Yol' burada yöntem anlamında mecaz kullanılmış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Koca Ayı sepetini Maşa'ya uzattı"
   - Cümle 6: «Koca Ayı sepetini Maşa'ya uzattı.»
   - Açıklama: Sepet ve içindeki kurabiye önceden kurulmadan beliriyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Daha önce hiç anılmayan sepet ve kurabiye sebepsizce beliriyor ve çözümü getiriyor.
   - Açıklama: Daha önce hiç kurulmamış sepet ve kurabiye çözümü sebepsizce getiriyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "ve çevik adımlarla kurabiyeye"
   - Cümle 10: «Kirpi burnunu çıkardı ve çevik adımlarla kurabiyeye koştu.»
   - Açıklama: 'Çevik' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "çevik adımlarla kurabiyeye koştu"
   - Cümle 10: «Kirpi burnunu çıkardı ve çevik adımlarla kurabiyeye koştu.»
   - Açıklama: 'Çevik' 3 yaşındaki çocuğun bileceği bir kelime değil.
   - Açıklama: 'Çevik' 3 yaşındaki çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0007` birebir aynı, ardından `@onarim: ad5afba21f3c77f3c95806293be446be1cf0c4d5`, sonra gövde.

### Hikâye 8: tohum masa-0008 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0008
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sırayla oynamak
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'bulut', fiil 'solmak', sıfat 'sevinçli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: iki kız aynı anda bağırdı ve birbirini duymadı | sırayla söyleme kuralı koydu
@tohum: masa-0008
@degisim: solmak -> söylemek
Bir sabah Maşa ile Daşa ormanda çimenlere uzanmış, bulutlara bakıyordu. İkisi de bulutlarda şekil bulmak istiyordu. Ama ikisi aynı anda bağırıyordu ve kimse ötekini duymuyordu. Maşa biraz düşündü ve yeni bir oyun kuralı denedi. "Sırayla söyleyelim, Daşa, önce sen," dedi Maşa. Daşa gökyüzüne dikkatle baktı. "Şu bulut bir kaşığa benziyor," dedi Daşa. Maşa da baktı ve kaşığı gördü. Sonra sıra Maşa'ya geldi. "Şu bulut da kocaman bir elmaya benziyor!" dedi Maşa. Daşa elmayı görünce sevinçli bir sesle güldü. İki kız sırayla bulutlara baktı ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kimse ötekini duymuyordu"
   - Cümle 3: «Ama ikisi aynı anda bağırıyordu ve kimse ötekini duymuyordu.»
   - Açıklama: İki kişi için 'kimse ötekini' uyumsuz; 'hiçbiri ötekini' ya da 'birbirlerini duymuyorlardı' olmalı.
   - Açıklama: 'Kimse' ile 'ötekini' uyumsuz; 'biri ötekini duymuyordu' ya da 'birbirlerini duymuyorlardı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kimse ötekini duymuyordu"
   - Cümle 3: «Ama ikisi aynı anda bağırıyordu ve kimse ötekini duymuyordu.»
   - Açıklama: İki kişi için 'kimse' uygun değil; 'hiçbiri ötekini duymuyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0008` birebir aynı, `@degisim: solmak -> söylemek` (tutuyorsan), ardından `@onarim: ede9bbc32408accb8d6802835b153bd1e1a1d32c`, sonra gövde.

### Hikâye 9: tohum masa-0009 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: sincap da kurabiye istedi ama kurabiye bir taneydi | kurabiyeyi ikiye kırdı ve sincapla paylaştı
@tohum: masa-0009
Maşa ormanda bir kütüğe oturdu ve kağıda sarılı kurabiyesini açtı. Kurabiye ay şeklindeydi. O sırada bir sincap kütüğe zıpladı ve kurabiyeye aç aç baktı. Ama kurabiye bir taneydi. Maşa kurabiyeyi sincapla paylaşmak istedi. Kurabiyeyi iki eliyle tuttu ve ikiye kırmayı denedi. Ama kurabiye çok sertti ve kırılmadı. Maşa kararlı bir şekilde bir kez daha bastırdı. Çıt diye bir ses geldi ve kurabiye ikiye ayrıldı. Maşa bir parçayı kağıdın üstüne koydu ve sincaba verdi. Sincap parçayı patileriyle tuttu ve hızlı hızlı yedi. Maşa da kendi parçasını yedi. Sonra boş kağıdı buruşturdu ve cebine koydu. "Birlikte yemek daha güzelmiş, sincap!" dedi Maşa.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "Kurabiye ay şeklindeydi"
   - Cümle 2: «Kurabiye ay şeklindeydi.»
   - Açıklama: Kurabiyenin ay şekli kuruluyor ama olayda hiçbir işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kurabiyeye aç aç baktı"
   - Cümle 3: «O sırada bir sincap kütüğe zıpladı ve kurabiyeye aç aç baktı.»
   - Açıklama: 'Aç aç' yerleşik bir ikileme değil, 'bakmak' fiiline anlamca uymuyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kurabiye bir taneydi"
   - Cümle 4: «Ama kurabiye bir taneydi.»
   - Açıklama: Kurabiyenin tek olduğu sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama kurabiye çok sertti ve kırılmadı"
   - Cümle 7: «Ama kurabiye çok sertti ve kırılmadı.»
   - Açıklama: Paylaşma sorununun yanına kurabiyenin sertliği ikinci bir sorun olarak ekleniyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa kararlı bir şekilde"
   - Cümle 8: «Maşa kararlı bir şekilde bir kez daha bastırdı.»
   - Açıklama: Tohumdaki özellik deneme; kararlılık karttaki özellik listesinde olmayan ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0009` birebir aynı, ardından `@onarim: f164ef8f568e8edc7d35c440ec5f302a6524db45`, sonra gövde.

### Hikâye 10: tohum masa-0010 (deneme 1 -> 2)

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
Rüzgar hızlı hızlı esiyordu. Maşa bahçede zıplarken yerde yatan şık vazodan bir ses duydu. Rüzgardan saklanan bir kirpi vazoya girmişti ama dışarı çıkamıyordu. Maşa hemen zıplamayı durdurdu ve vazonun yanına koştu. "Bekle, kirpi, sana yardım edeceğim," dedi Maşa. Maşa vazonun dibini yavaşça yukarı kaldırmayı denedi. Vazonun ağzı çimenlere doğru eğildi. Kirpi yavaş yavaş kaydı ve çimenlerin üstüne çıktı. Kirpi burnunu salladı ve Maşa'nın eline dokundu. "Oldu, kirpi, artık dışarıdasın!" dedi Maşa. Sonra şık vazoyu dikkatle yerine koydu. Kirpi de bahçede mutlu mutlu dolaştı. Maşa çok sevindi, çünkü kirpiyi vazodan çıkarmıştı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "yatan şık vazodan"
   - Cümle 2: «Maşa bahçede zıplarken yerde yatan şık vazodan bir ses duydu.»
   - Açıklama: 'Şık' kelimesi 3 yaşındaki bir çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır. Çocuğun bildiği yaygın kelimeler ('bulmak', 'merak etmek', 'sevinmek') ve basit benzetmeler ('top gibi yuvarlak', 'kar gibi beyaz') D6 değildir; D6 yalnız deyim ('burnunu sokmak'), gerçek mecaz ('kalbi eridi') ve soyut isimdir ('cesaret', 'mutluluk', 'hayal gücü'). 'Keşif' ve 'keşfetmek' sınırdadır: kılavuz 'bulmak' ister; tek başına geçtiğinde D6 sayılmaz.
   - Alıntı: "yerde yatan şık vazodan"
   - Cümle 2: «Maşa bahçede zıplarken yerde yatan şık vazodan bir ses duydu.»
   - Açıklama: 'Şık' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir sıfat.
   - Açıklama: 'Şık' kelimesi 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir niteliktir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır. Yere doğal olarak ait yaygın bir nesne (kumsalda şemsiye, deniz kıyısında kova, parkta bank) önceden kurulmadan kullanılabilir; sebepsiz beliren nesne sayılmaz.
   - Alıntı: "yerde yatan şık vazodan"
   - Cümle 2: «Maşa bahçede zıplarken yerde yatan şık vazodan bir ses duydu.»
   - Açıklama: Şık bir vazonun bahçede yerde yatması sebepsiz beliriyor.
   - Açıklama: Şık bir vazonun bahçede yerde yatması sebepsiz; vazo yalnızca sorunu kurmak için beliriyor.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Maşa bahçede zıplarken"
   - Cümle 2: «Maşa bahçede zıplarken yerde yatan şık vazodan bir ses duydu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
   - Açıklama: Başlıktaki yer ev olduğu halde hikaye bahçede geçiyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kirpi burnunu salladı"
   - Cümle 9: «Kirpi burnunu salladı ve Maşa'nın eline dokundu.»
   - Açıklama: Burun sallanmaz; fiil nesnesine uymuyor.
   - Açıklama: Burun sallanmaz; 'burnunu oynattı' gibi bir fiil gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0010` birebir aynı, ardından `@onarim: 1f54264e220d0637058d6eedf920deeebad6bae0`, sonra gövde.
