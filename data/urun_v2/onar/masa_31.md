# Editör görevi (onarım): Maşa, onarım partisi 31

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar31.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar31.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0093 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0093
- yer: dağ (Ormanın yanındaki tepe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kutu', fiil 'üflemek', sıfat 'yeni'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: beyaz çiçek küçüktü ve az tohum uçtu | çiçekleri kutuya koyup kutunun içine üfledi
@tohum: masa-0093
Maşa tepede yeni kutusuna çiçek topluyordu. Birden otların arasında beyaz, top gibi çiçekler fark etti. Bir tanesine üfledi ama çiçek küçüktü ve yalnız birkaç tohum uçtu. Maşa tohumların kar gibi uçmasını istedi. Önce daha güçlü üfledi, yine az tohum uçtu. Sonra beyaz çiçekleri tek tek toplayıp kutusuna koymayı denedi. Kutuyu yüzüne yaklaştırdı ve içine kuvvetle üfledi. Bir anda kutudan havaya bir sürü tohum uçtu. Tohumlar tepenin üstünde kar taneleri gibi dönüyordu. Maşa tohumların arasında mutlu mutlu koşup zıpladı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "içine kuvvetle üfledi"
   - Cümle 7: «Kutuyu yüzüne yaklaştırdı ve içine kuvvetle üfledi.»
   - Açıklama: 'Kuvvetle' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime; 'güçlü' ya da 'çok' yeterli.
   - Açıklama: 'Kuvvetle' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime; 'güçlü' ya da 'çok' yeterliydi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0093` birebir aynı, ardından `@onarim: 2becc6b12b15044bf01f64866ecf75b36aaede74`, sonra gövde.

### Hikâye 2: tohum masa-0094 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi, Daşa
@tohum: masa-0094
- yer: dağ (Ormanın yanındaki tepe.)
- tema: sırayla oynamak
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kök', fiil 'okşamak', sıfat 'sakin'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi, Daşa
@plan: üçü de aynı anda topa uzandı ve oyun durdu | bekleyen reçel yesin dedi ve önce kuzeni attı
@tohum: masa-0094
Tepede Maşa, Daşa ve kirpi, eğri bir kökün üstünden top yuvarlıyordu. Top kökün üstünden kayıp çimenlere iniyordu ve herkes buna gülüyordu. Ama üçü de aynı anda topa uzandı ve oyun durdu. "Hepimiz ilk olmak istiyoruz," dedi Daşa. Maşa sepetinden reçel kavanozunu çıkardı. "Bekleyen reçel yesin, Daşa," dedi Maşa. Artık kimse acele etmedi. Önce Daşa attı, Maşa da reçel yedi. Sonra sakin kirpi topu burnuyla itti, Daşa da reçel yedi. En son Maşa attı ve iki kız sevinçle güldü. Daşa, Maşa'nın başını okşadı. "Sırayla oynamak çok eğlenceli, Daşa!" dedi Maşa.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "önce kuzeni attı"
   - Cümle 0 (plan satırı): «üçü de aynı anda topa uzandı ve oyun durdu | bekleyen reçel yesin dedi ve önce kuzeni attı»
   - Açıklama: 'kuzeni attı' kuzenini fırlattı diye okunuyor; 'önce kuzeni topu attı' gibi olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve önce kuzeni attı"
   - Cümle 0 (plan satırı): «üçü de aynı anda topa uzandı ve oyun durdu | bekleyen reçel yesin dedi ve önce kuzeni attı»
   - Açıklama: Nesnesiz 'kuzeni attı' kuzenin atıldığı anlamına geliyor; 'önce kuzeni topu attı' ya da 'önce kuzeni atsın' olmalı.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "bekleyen reçel yesin dedi"
   - Cümle 0 (plan satırı): «üçü de aynı anda topa uzandı ve oyun durdu | bekleyen reçel yesin dedi ve önce kuzeni attı»
   - Açıklama: Aktarılan söz tırnak ve virgül olmadan yazılmış.
   - Açıklama: Aktarılan söz tırnak ya da virgülle ayrılmamış.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra sakin kirpi topu burnuyla itti, Daşa da reçel yedi"
   - Cümle 9: «Sonra sakin kirpi topu burnuyla itti, Daşa da reçel yedi.»
   - Açıklama: Kural bekleyenin reçel yemesi ama bekleyen Maşa değil yalnız Daşa yiyor ve kirpi hiç reçel yemiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0094` birebir aynı, ardından `@onarim: 853f25d7dfdaf970f2999b2a6d54693269a9cb40`, sonra gövde.

### Hikâye 3: tohum masa-0095 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi, Daşa
@tohum: masa-0095
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'paket', fiil 'süpürmek', sıfat 'berrak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | kirpi, Daşa
@plan: zıplarken paketi düşürdü ve kurabiyeler kırıldı | özür diledi ve kırık parçaları reçelle yapıştırdı
@tohum: masa-0095
@degisim: berrak -> mavi
Bir sabah ormanda gökyüzü maviydi. Daşa, Maşa'ya şehirden bir paket kurabiye getirmişti. Maşa sevinçle zıplarken paketi düşürdü ve içindeki kurabiyeler ikiye kırıldı. "Hepsi kırıldı," dedi Daşa üzgün bir sesle. "Özür dilerim, Daşa, çok acele ettim," dedi Maşa. Sonra sepetinden reçel kavanozunu çıkardı. Kırık parçaların arasına reçel sürüp onları birbirine yapıştırdı. Kurabiyeler yine bütün ve reçelli oldu. Patikadan bir kirpi geliyordu, Maşa dökülen kırıntıları bir dalla kenara süpürdü. Kirpi temiz patikadan geçti ve çalıların arasına girdi. Daşa reçelli bir kurabiye tattı ve gülümsedi. "Teşekkürler, Maşa, bunlar çok güzel olmuş!" dedi Daşa.
```

**Hakem bulguları (3):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "bir kirpi geliyordu, Maşa dökülen"
   - Cümle 9: «Patikadan bir kirpi geliyordu, Maşa dökülen kırıntıları bir dalla kenara süpürdü.»
   - Açıklama: İki bağımsız cümle virgülle birleştirilmiş; araya nokta gelmeli.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Patikadan bir kirpi geliyordu, Maşa dökülen"
   - Cümle 9: «Patikadan bir kirpi geliyordu, Maşa dökülen kırıntıları bir dalla kenara süpürdü.»
   - Açıklama: İki bağımsız cümle yalnız virgülle bağlanmış; nokta ya da bağlaç gerekir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Patikadan bir kirpi geliyordu"
   - Cümle 9: «Patikadan bir kirpi geliyordu, Maşa dökülen kırıntıları bir dalla kenara süpürdü.»
   - Açıklama: Kirpi ve kırıntı süpürme sebepsiz beliriyor ve kurabiye sorunuyla ilgisiz işlevsiz bir ayrıntı.
   - Açıklama: Kirpi ve kırıntı süpürme olayı sorunla ilgisiz, işlevsiz bir ara olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0095` birebir aynı, `@degisim: berrak -> mavi` (tutuyorsan), ardından `@onarim: f4d22afb89014c73013b7d44f2c9b1f614270645`, sonra gövde.

### Hikâye 4: tohum masa-0096 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı, sincap
@tohum: masa-0096
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'boya', fiil 'sararmak', sıfat 'heyecanlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı, sincap
@plan: sincap kovanın kenarından kaydı ve kovaya düştü | kovaya uzun bir dal koydu ve sincap tırmandı
@tohum: masa-0096
Bir sabah Koca Ayı'nın bahçesinde yapraklar sararmış, yere dallar düşmüştü. Koca Ayı ağaç evinin kapısını boyuyordu, Maşa da ona bakıyordu. Kovanın kenarında zıplayan bir sincap kaydı ve boş boya kovasına düştü. Sincap kovanın dibinde döndü ama kovanın içi kaygandı. Maşa heyecanlı heyecanlı kovanın yanına koştu. Önce elini uzattı ama kova çok derindi. Sonra yerdeki uzun bir dalı kovanın içine koymayı denedi. Sincap dala tutundu ve hızla yukarı tırmandı. Kovadan atladı ve kuyruğunu sallayarak ağaca koştu. Koca Ayı Maşa'ya bakıp gülümsedi. Maşa bundan sonra boş kovaları hep ters çevirip koydu.
```

**Hakem bulguları (4):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "kaydı ve boş boya kovasına düştü"
   - Cümle 3: «Kovanın kenarında zıplayan bir sincap kaydı ve boş boya kovasına düştü.»
   - Açıklama: Sincabın derin kovaya düşüp içinde mahsur kalması küçük çocuk için ürkütücü bir tehlike anı oluşturuyor.
2. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "kaydı ve boş boya kovasına düştü"
   - Cümle 3: «Kovanın kenarında zıplayan bir sincap kaydı ve boş boya kovasına düştü.»
   - Açıklama: Sincap düşüp kovada mahsur kalıyor; kartın güvenli kullanım satırı kimsenin düşmemesini istiyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "boş boya kovasına düştü"
   - Cümle 3: «Kovanın kenarında zıplayan bir sincap kaydı ve boş boya kovasına düştü.»
   - Açıklama: Koca Ayı kapıyı boyarken boya kovasının boş olması çelişkili.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kovanın dibinde döndü ama kovanın içi"
   - Cümle 4: «Sincap kovanın dibinde döndü ama kovanın içi kaygandı.»
   - Açıklama: 'Kovanın' kelimesi aynı cümlede ve art arda cümlelerde gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0096` birebir aynı, ardından `@onarim: 4b6837bd5047684a5e0e25995d63dbf9bde8082f`, sonra gövde.

### Hikâye 5: tohum masa-0098 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0098
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'biber', fiil 'doğmak', sıfat 'şekerli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: sepetteki fındıklar azalmıştı ve kim aldı bilinmiyordu | yaprağa reçel sürdü ve reçelli izleri takip etti
@tohum: masa-0098
Ormanda güneş yeni doğmuştu. Maşa sepetini bir ağacın altına bırakıp biraz uzakta çiçek topladı. Döndüğünde kırmızı biberin yanındaki fındıklar azalmıştı. Maşa fındıkları kimin aldığını çok merak etti. Sepetin önüne bir yaprak koydu ve üstüne şekerli reçelinden sürdü. Sonra yine çiçek toplamaya gitti. Döndüğünde reçelin üstünde küçük ayak izleri vardı. Reçelli izler yerde bir ağaca kadar gidiyordu. Maşa ağaca baktı ve dalda bir sincap gördü. Sincabın ağzında bir fındık vardı. "Demek fındıkları sen aldın, sincap!" dedi Maşa. Sonra Maşa ile sincap ağacın altında mutlu mutlu oynadı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kim aldı bilinmiyordu"
   - Cümle 0 (plan satırı): «sepetteki fındıklar azalmıştı ve kim aldı bilinmiyordu | yaprağa reçel sürdü ve reçelli izleri takip etti»
   - Açıklama: Yan cümle eksik çekimli; 'kimin aldığı bilinmiyordu' olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve kim aldı bilinmiyordu"
   - Cümle 0 (plan satırı): «sepetteki fındıklar azalmıştı ve kim aldı bilinmiyordu | yaprağa reçel sürdü ve reçelli izleri takip etti»
   - Açıklama: Plan satırında yan cümle yapısı bozuk; 'kimin aldığı bilinmiyordu' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kırmızı biberin yanındaki fındıklar"
   - Cümle 3: «Döndüğünde kırmızı biberin yanındaki fındıklar azalmıştı.»
   - Açıklama: Kırmızı biber sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0098` birebir aynı, ardından `@onarim: 17c7df267552a4b0875518256eb6d3e3d115d644`, sonra gövde.

### Hikâye 6: tohum masa-0099 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı
@tohum: masa-0099
- yer: dağ (Ormanın yanındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'şişe', fiil 'sabırsızlanmak', sıfat 'sevimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı
@plan: sabırsızlandı ve şişeyi çekti, su döküldü | özür diledi ve kalan suyla baloncuk yaptı
@tohum: masa-0099
Maşa, Koca Ayı ile tepede baloncuk yapıyordu. Koca Ayı şişedeki sabunlu suya bir halka koyup üfledi. Maşa sabırsızlandı, şişeyi hızla çekti ve su çimenlere döküldü. Koca Ayı üzgün üzgün şişeye baktı. "Özür dilerim, Koca Ayı, çok acele ettim," dedi Maşa. Şişenin dibinde birazcık sabunlu su kalmıştı. Maşa şişeyi eğdi ve halkayı kalan suya koymayı denedi. Sonra halkaya yavaşça üfledi. Halkadan kocaman bir baloncuk çıktı ve havada süzüldü. Sevimli Koca Ayı güldü ve ellerini çırptı. Bu kez Maşa halkayı Koca Ayı'ya verdi ve sırasını bekledi. Maşa çok sevindi, çünkü Koca Ayı yeniden gülüyordu.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "verdi ve sırasını bekledi"
   - Cümle 11: «Bu kez Maşa halkayı Koca Ayı'ya verdi ve sırasını bekledi.»
   - Açıklama: Tohumdaki özellik denemek; sıra bekleme sabrı ikinci bir özellik gibi ekleniyor, bu yüzden tereddütle işaretlendi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0099` birebir aynı, ardından `@onarim: 3bef211007497776ac818734c66e2b7be934dcc6`, sonra gövde.

### Hikâye 7: tohum masa-0102 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0102
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kanepe', fiil 'fışkırmak', sıfat 'umutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: zıplarken ayakkabısı yumuşak çamura takıldı | ayağını sağa sola küçük küçük salladı
@tohum: masa-0102
@degisim: kanepe -> çamur
Bir sabah ormanda yağmur yeni dinmişti. Maşa patikadaki su birikintilerine zıplıyor, sular havaya fışkırıyordu. Ama bir anda Maşa'nın ayakkabısı yumuşak bir çamura takıldı. Maşa ayağını hızla çekti ama ayağı yerinden çıkmadı. Maşa durmadı ve başka bir yol denedi. Ayağını sağa ve sola küçük küçük salladı. Ayakkabı biraz oynayınca Maşa umutlu oldu ve daha çok salladı. Sonunda ayağı ayakkabısıyla birlikte çamurdan çıktı. Maşa çamurlu ayakkabısına baktı ve güldü. Sonra yine su birikintilerine zıpladı ama bu kez çamurdan uzak durdu. Maşa bundan sonra çamurda ayağını çekmedi, yavaşça salladı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ayakkabısı yumuşak çamura takıldı"
   - Cümle 0 (plan satırı): «zıplarken ayakkabısı yumuşak çamura takıldı | ayağını sağa sola küçük küçük salladı»
   - Açıklama: Plan satırında da ayakkabı çamura 'takıldı' deniyor; 'battı' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ayakkabısı yumuşak bir çamura takıldı"
   - Cümle 3: «Ama bir anda Maşa'nın ayakkabısı yumuşak bir çamura takıldı.»
   - Açıklama: Ayakkabı çamura takılmaz, saplanır ya da batar.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yumuşak bir çamura takıldı"
   - Cümle 3: «Ama bir anda Maşa'nın ayakkabısı yumuşak bir çamura takıldı.»
   - Açıklama: Ayakkabı çamura takılmaz, saplanır; fiil yanlış anlamda kullanılmış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "başka bir yol denedi"
   - Cümle 5: «Maşa durmadı ve başka bir yol denedi.»
   - Açıklama: 'Yol' burada yöntem anlamında mecaz kullanılmış.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa umutlu oldu"
   - Cümle 7: «Ayakkabı biraz oynayınca Maşa umutlu oldu ve daha çok salladı.»
   - Açıklama: 'Umutlu' soyut bir kavram.
   - Açıklama: 'Umutlu' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0102` birebir aynı, `@degisim: kanepe -> çamur` (tutuyorsan), ardından `@onarim: a47d158e907d581462527c1a56f8714004f93e5f`, sonra gövde.

### Hikâye 8: tohum masa-0103 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0103
- yer: dağ (Ormanın yanındaki tepe.)
- tema: kaybolan eşya
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'şerit', fiil 'kaçmak', sıfat 'elmalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: reçel kavanozu yokuştan aşağı yuvarlandı ve kayboldu | kavanozdaki kırmızı şeridi otların arasında aradı
@tohum: masa-0103
@degisim: kaçmak -> yuvarlanmak
Rüzgar hafif hafif esiyordu. Maşa tepede elmalı reçel kavanozunu kucağında tutuyordu. Kavanozun kapağına kırmızı bir şerit bağlıydı. Birden kavanoz elinden kaydı ve yokuştan aşağı yuvarlandı. Kavanoz uzun otların arasında kayboldu. Maşa aşağıya yavaşça indi ve otlara baktı. Ama otlar çok sıktı ve kavanoz görünmüyordu. Maşa otların arasında o kırmızı şeridi aradı. Sonunda bir çalının dibinde kırmızı şerit göründü. Maşa kavanozu aldı ve ona sevinçle sarıldı. Sonra tepeye geri çıktı ve reçelinden mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "elmalı reçel kavanozunu"
   - Cümle 2: «Maşa tepede elmalı reçel kavanozunu kucağında tutuyordu.»
   - Açıklama: Reçel türü tamlamayla söylenir; 'elma reçeli kavanozunu' olmalı.
   - Açıklama: 'Elmalı reçel' doğal bir tamlama değil; 'elma reçeli kavanozunu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0103` birebir aynı, `@degisim: kaçmak -> yuvarlanmak` (tutuyorsan), ardından `@onarim: 271be2cf5d56fcab173aeaa84753d1ed7e32e128`, sonra gövde.

### Hikâye 9: tohum masa-0105 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0105
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'simit', fiil 'boyamak', sıfat 'nazik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi simidi yemedi çünkü elmayı severdi | simidi alıp üstüne elma reçeli sürdü
@tohum: masa-0105
@degisim: boyamak -> sürmek
Bir sabah Maşa ormanda yemek oyunu oynuyordu. Koca Ayı bir kütüğe iki simit ve bir kavanoz elma reçeli koydu. Ama kirpi simidi kokladı ve yemedi, çünkü o elmayı severdi. Maşa bir an düşündü. Sonra reçel kavanozunu açtı. Bir simidi alıp üstüne kalın kalın elma reçeli sürdü. "Buyur, kirpi, bu simit artık elmalı!" dedi Maşa nazik bir sesle. Kirpi hemen bir ısırık aldı ve burnunu oynattı. Koca Ayı sevinçle ellerini çırptı. Maşa da güldü ve üçü oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "çünkü o elmayı severdi"
   - Cümle 3: «Ama kirpi simidi kokladı ve yemedi, çünkü o elmayı severdi.»
   - Açıklama: Elmayı sevmek kirpinin simidi reddetmesi için akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0105` birebir aynı, `@degisim: boyamak -> sürmek` (tutuyorsan), ardından `@onarim: 60b0cac712edfa1f86cc865f78df66213a00773b`, sonra gövde.

### Hikâye 10: tohum masa-0106 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0106
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'saat', fiil 'tamamlamak', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: sincap yapbozun son parçasını fındık sandı ve kaçtı | yardım isteyip sincaba bir fındık verdi
@tohum: masa-0106
@degisim: saat -> yapboz
Tepede serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa orada meyveli bir ağacın yapbozunu yapıyordu. Ama bir sincap son parçayı fındık sandı ve kapıp kaçtı. Sincap sonra bir taşın üstüne oturdu. Parça olmadan yapboz bitmiyordu ve Maşa üzüldü. Maşa'nın cebinde hiç fındık yoktu, bu yüzden Daşa'dan yardım istedi. Daşa cebinden bir fındık çıkarıp Maşa'ya verdi. Maşa parçayı fındıkla değiştirmeyi denedi. Fındığı taşın yanına koydu. Sincap taştan indi, parçayı bıraktı ve fındığı aldı. Maşa son parçayı hemen yerine koydu ve yapbozu tamamladı. Daşa ile Maşa meyveli ağaca bakıp güldüler. Maşa bundan sonra zor bir işte hemen yardım istedi.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bir sincap son parçayı fındık sandı"
   - Cümle 3: «Ama bir sincap son parçayı fındık sandı ve kapıp kaçtı.»
   - Açıklama: Sincabın bir yapboz parçasını fındık sanması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0106` birebir aynı, `@degisim: saat -> yapboz` (tutuyorsan), ardından `@onarim: a552d4f57546025b53ca31c6c14bb5cae071571d`, sonra gövde.

### Hikâye 11: tohum masa-0112 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0112
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'buz', fiil 'tamamlanmak', sıfat 'uykulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: ağaç evin dışından tık tık diye bir ses geldi | sesi dinleyip pencereden damlayan suyu gördü
@tohum: masa-0112
@degisim: tamamlanmak -> damlamak
Dışarıdan tık tık diye bir ses geliyordu. Maşa, Koca Ayı'nın ağaç evindeydi ve bu sesi çok merak etti. Uykulu Koca Ayı da başını kaldırıp dinledi. Maşa önce kapıyı açıp baktı, ama orada bir şey yoktu. Sonra sesi dinleyerek pencereye doğru yürüdü. Maşa pencereden dışarı baktı. Çatıdaki buzlar eriyordu ve su boş bir kovaya damlıyordu. Her damla kovada tık diye ses çıkarıyordu. Koca Ayı da pencereye geldi ve gülümsedi. "Koca Ayı, sesi buldum, şimdi birlikte reçel yiyelim!" dedi Maşa.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Dışarıdan tık tık diye bir ses geliyordu"
   - Cümle 1: «Dışarıdan tık tık diye bir ses geliyordu.»
   - Açıklama: Yalnız merak uyandıran bir ses var, ortada çözülmesi gereken gerçek bir sorun yok.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "şimdi birlikte reçel yiyelim"
   - Cümle 10: «"Koca Ayı, sesi buldum, şimdi birlikte reçel yiyelim!" dedi Maşa.»
   - Açıklama: Tohumdaki reçel özelliği sona eklenmiş, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yaramıyor, yalnız son cümlede anılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şimdi birlikte reçel yiyelim"
   - Cümle 10: «"Koca Ayı, sesi buldum, şimdi birlikte reçel yiyelim!" dedi Maşa.»
   - Açıklama: Reçel olaydan çıkmıyor, son replikte sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0112` birebir aynı, `@degisim: tamamlanmak -> damlamak` (tutuyorsan), ardından `@onarim: bd3a3c0c06540712dd388c44a71246b79be967db`, sonra gövde.

### Hikâye 12: tohum masa-0114 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0114
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'zambak', fiil 'çizmek', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: rüzgar esti ve resim kağıdı uçtu | kağıdın köşesine reçel kavanozunu koydu
@tohum: masa-0114
Maşa ormanda resim oyunu oynuyordu ve bir zambak çizmek istiyordu. Kalemlerini ve sepetini beyaz bir zambağın yanına koydu, kağıdını da çimenlere serdi. Ama rüzgar esti ve kağıt havalanıp çalılara doğru uçtu. Maşa koştu ve kağıdı çalının dibinden aldı. Sonra sepetine baktı. Sepette en sevdiği yiyecek, bir kavanoz çilek reçeli vardı. Maşa reçel kavanozunu kağıdın bir köşesine koydu. Artık rüzgar esse de kağıt yerinden kıpırdamadı. Maşa zambağın uzun sapını ve açık yapraklarını dikkatle çizdi. Resim çok güzel oldu ve tıpkı çiçeğe benzedi. Maşa oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Artık rüzgar esse de kağıt yerinden kıpırdamadı"
   - Cümle 8: «Artık rüzgar esse de kağıt yerinden kıpırdamadı.»
   - Açıklama: Şart kipi ile belirli geçmiş uyumsuz; 'rüzgar esince bile kağıt kıpırdamadı' ya da 'kıpırdamıyordu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0114` birebir aynı, ardından `@onarim: 070620cddd93300a9ccea9807caa09d086136d0c`, sonra gövde.
