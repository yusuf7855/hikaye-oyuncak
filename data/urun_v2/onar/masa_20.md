# Editör görevi (onarım): Maşa, onarım partisi 20

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar20.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar20.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0016 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0016
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'direk', fiil 'yerleştirmek', sıfat 'düz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: örtü hep kayıyordu çünkü çadırın direği çok inceydi | kalın ve düz bir dalı toprağa yerleştirdi
@tohum: masa-0016
Serin bir rüzgar esiyordu. Maşa ile kirpi ormanda çadır kurup içinde reçel yiyecekti. Ama örtü hep yere kayıyordu, çünkü çadırın direği çok ince bir daldı. Maşa ince dalı yere bıraktı ve etrafa baktı. Çalıların yanında kalın ve düz bir dal buldu. Maşa dalı toprağa sıkıca yerleştirdi ve örtüyü üstüne serdi. Bu kez örtü hiç kaymadı. Güzel bir çadır olmuştu. Kirpi hemen çadırın içine girdi. Maşa da onun yanına oturdu. "Bak, kirpi, çadırımız hazır, hadi reçel yiyelim!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çadır kurup içinde reçel yiyecekti"
   - Cümle 2: «Maşa ile kirpi ormanda çadır kurup içinde reçel yiyecekti.»
   - Açıklama: Tohumdaki reçel özelliği yalnız anılıyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yarar biçimde kullanılmıyor, yalnız süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0016` birebir aynı, ardından `@onarim: 413e83922e3bbbf1d9ddfb2e2e6a357700870ab3`, sonra gövde.

### Hikâye 2: tohum masa-0037 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0037
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'fıskiye', fiil 'güvenmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: top ağaca çarpıp iki taşın arasına düştü | dalın ucuna reçel sürdü ve topu çıkardı
@tohum: masa-0037
@degisim: fıskiye -> top
Maşa ormanda piknik yapıyor ve küçük sarı topuyla oynuyordu. Topu havaya atıyor ve yakalıyordu. Ama top bir ağaca çarptı ve iki taşın arasına düştü. Taşların arası çok dardı ve Maşa'nın eli oraya sığmadı. Maşa sepetteki en sevdiği tatlı reçele baktı. Sarı top çok hafifti, reçel de yapışkandı. Maşa yapışkan reçele güvendi. Uzun bir dalın ucuna biraz reçel sürdü. Dalı taşların arasına uzattı ve top reçele yapıştı. Maşa dalı yavaşça çekti ve top dışarı çıktı. Top yapış yapış olmuştu. Maşa güldü ve onu otlara silip temizledi. Maşa bundan sonra topuyla ağaçlardan uzakta, açık bir yerde oynadı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Maşa yapışkan reçele güvendi"
   - Cümle 7: «Maşa yapışkan reçele güvendi.»
   - Açıklama: 'Reçele güvenmek' kelimeyi yanlış ve soyut anlamda kullanıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa yapışkan reçele güvendi"
   - Cümle 7: «Maşa yapışkan reçele güvendi.»
   - Açıklama: Reçele güvenmek soyut bir kullanım; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0037` birebir aynı, `@degisim: fıskiye -> top` (tutuyorsan), ardından `@onarim: f3d105792a5edd9f816b76d59bab2e7b0a743dab`, sonra gövde.

### Hikâye 3: tohum masa-0039 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0039
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'koni', fiil 'yıkamak', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: çamurdan pasta yaparken elleri çok kirlendi | kovadaki yağmur suyuyla ellerini yıkadı
@tohum: masa-0039
@degisim: koni -> kova
Maşa bulutlu bir günde ormanda çamurdan pasta yapıyordu. Pasta yapmak için yanındaki kovada yağmur suyu biriktirmişti. Birden karnı acıktı ama elleri çok kirliydi. Sepetinde en sevdiği reçelli ekmek vardı. Maşa onu temiz ellerle yemek istedi. Kovadaki su serin ve temizdi. Maşa bu suyla ellerini iyice yıkadı. Sonra ellerini salladı ve kuruttu. Büyük bir ağacın altına oturdu. Ekmeğini sepetten aldı ve afiyetle yedi. Maşa çok mutluydu, çünkü elleri temizdi ve karnı doymuştu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sepetinde en sevdiği reçelli ekmek vardı"
   - Cümle 4: «Sepetinde en sevdiği reçelli ekmek vardı.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sepetinde en sevdiği reçelli ekmek"
   - Cümle 4: «Sepetinde en sevdiği reçelli ekmek vardı.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yarar biçimde kullanılmıyor, yalnız anılıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Maşa bu suyla ellerini iyice yıkadı"
   - Cümle 7: «Maşa bu suyla ellerini iyice yıkadı.»
   - Açıklama: Kirli elleri hazır kovadaki suyla yıkamak önemsiz bir olay; sorun hiç zorluk çıkarmadan bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0039` birebir aynı, `@degisim: koni -> kova` (tutuyorsan), ardından `@onarim: 5e7b4dfb4ababb42f8cb6cca103e00d55036140f`, sonra gövde.

### Hikâye 4: tohum masa-0040 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Daşa
@tohum: masa-0040
- yer: dağ (Ormanın yanındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'boncuk', fiil 'kavuşmak', sıfat 'uyanık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Daşa
@plan: koşarken kutu elinden düştü ve boncuklar döküldü | özür diledi ve boncukları tek tek topladı
@tohum: masa-0040
@degisim: uyanık -> renkli
Rüzgar tepede hafif hafif esiyordu. Şehirden gelen Daşa, kolye yapmak için çimenlerde Maşa'yı bekliyordu. Maşa kuzenine kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü. Renkli boncuklar çimenlerin arasına döküldü. Daşa çok üzüldü. "Özür dilerim, Daşa, hepsini hemen toplayacağım," dedi Maşa. Maşa çimenlere eğildi ve boncukları tek tek toplamayı denedi. Daşa da kutuyu açık tuttu. Sonunda bütün boncuklar kutudaydı. Daşa kutuya baktı ve gülümsedi. "Teşekkürler, Maşa, hadi kolyeyi birlikte yapalım," dedi Daşa. Maşa çok sevindi, çünkü kuzeni yine gülüyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa kuzenine kavuşmak için"
   - Cümle 3: «Maşa kuzenine kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü.»
   - Açıklama: 'Kavuşmak' 3 yaşındaki bir çocuğun bilmeyeceği edebi bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kuzenine kavuşmak için"
   - Cümle 3: «Maşa kuzenine kavuşmak için boncuk kutusuyla koştu, ama kutu elinden düştü.»
   - Açıklama: 'Kavuşmak' 3 yaşındaki bir çocuğun bilmeyeceği edebi bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0040` birebir aynı, `@degisim: uyanık -> renkli` (tutuyorsan), ardından `@onarim: f0f7f053449b2a6c366a28ef58b0e5f225036fd5`, sonra gövde.

### Hikâye 5: tohum masa-0047 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Daşa
@tohum: masa-0047
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kereviz', fiil 'soğumak', sıfat 'konuşkan'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | Daşa
@plan: içecek güneşte kaldığı için ılık olmuştu | şişeyi soğuk sulu kovaya koyup gölgede bekledi
@tohum: masa-0047
@degisim: kereviz -> şişe
Hava çok sıcaktı. Maşa bahçede en sevdiği çilek reçelinden kuzeni Daşa için içecek hazırlamıştı. Ama şişe güneşte kaldığı için içecek ılık olmuştu. Maşa evden bir kova soğuk su getirdi. Şişeyi kovaya koydu ve kovayı ağacın gölgesine taşıdı. Maşa beklerken şişeye birkaç kez dokundu. Sonunda içecek iyice soğudu. Tam o sırada bahçe kapısından Daşa geldi. "Sürpriz, Daşa, bu içecek senin için!" dedi Maşa. Daşa bir yudum aldı ve gülümsedi. "Çok güzel olmuş, teşekkür ederim, Maşa," dedi Daşa. Ciddi Daşa bile sevinçten çok konuşkan oldu. Maşa ile Daşa ağacın altında oturup içeceklerini mutlu mutlu içti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ciddi Daşa bile sevinçten çok konuşkan oldu"
   - Cümle 12: «Ciddi Daşa bile sevinçten çok konuşkan oldu.»
   - Açıklama: 'Ciddi' ve 'konuşkan' soyut kişilik kelimeleri 3 yaşındaki çocuğa uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ciddi Daşa bile sevinçten çok konuşkan oldu"
   - Cümle 12: «Ciddi Daşa bile sevinçten çok konuşkan oldu.»
   - Açıklama: Daşa'nın çok konuşkan olduğu olaylarda görülmüyor; cümle işlevsiz ve temelsiz bir ayrıntı.
   - Açıklama: Daşa'nın konuşkanlaştığı gösterilmiyor; cümle olaydan çıkmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0047` birebir aynı, `@degisim: kereviz -> şişe` (tutuyorsan), ardından `@onarim: b8d88c026d77017bf77196ed5c7245896ae9ca31`, sonra gövde.

### Hikâye 6: tohum masa-0050 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0050
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tablo', fiil 'dikmek', sıfat 'kilitli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: resmin köşesinde yapışkan kırmızı izler vardı | kokudan reçeli tanıdı ve izleri takip edip sincabı buldu
@tohum: masa-0050
@degisim: kilitli -> yapışkan
Maşa tepede reçel kavanozunu yanına koymuş, Koca Ayı'yı izliyordu. Koca Ayı bir tahtayı yere dikmiş, üstüne bir tablo asmıştı. Birden Maşa resmin köşesinde küçük kırmızı izler gördü. Bunlar yapışkandı ve çok güzel kokuyordu. Maşa kokuyu hemen tanıdı, bu onun en sevdiği reçeldi! Kavanozun yanında da minik, kırmızı pati izleri vardı. Maşa bu izlere bakarak yürüdü ve ağacın arkasında bir sincap buldu. Sincabın patileri kırmızı reçelle kaplıydı. Koca Ayı sincabı görünce gülümsedi. Maşa çok sevindi, çünkü kırmızı izleri kimin yaptığını bulmuştu.
```

**Hakem bulguları (6):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "resmin köşesinde küçük kırmızı izler gördü"
   - Cümle 3: «Birden Maşa resmin köşesinde küçük kırmızı izler gördü.»
   - Açıklama: İzler görülüyor ama bunun neden bir sorun olduğu açıkça söylenmiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "resmin köşesinde küçük kırmızı izler gördü"
   - Cümle 3: «Birden Maşa resmin köşesinde küçük kırmızı izler gördü.»
   - Açıklama: Sorun yalnız resimde birkaç iz olması; çocuğun önemseyeceği gerçek bir sorun kurulmuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bunlar yapışkandı ve çok güzel kokuyordu"
   - Cümle 4: «Bunlar yapışkandı ve çok güzel kokuyordu.»
   - Açıklama: Resimdeki güzel kokulu izler çocuğun önemseyeceği net bir sorun olarak kurulmuyor.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "hemen tanıdı, bu onun en sevdiği reçeldi!"
   - Cümle 5: «Maşa kokuyu hemen tanıdı, bu onun en sevdiği reçeldi!»
   - Açıklama: İki bağımsız cümle virgülle birleştirilmiş; nokta ya da iki nokta gerekir.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "kırmızı izleri kimin yaptığını bulmuştu"
   - Cümle 10: «Maşa çok sevindi, çünkü kırmızı izleri kimin yaptığını bulmuştu.»
   - Açıklama: İzi yapan bulunuyor ama lekeli resim temizlenmiyor; sorunun çözüldüğü görünmüyor.
6. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Maşa çok sevindi, çünkü kırmızı izleri kimin yaptığını bulmuştu"
   - Cümle 10: «Maşa çok sevindi, çünkü kırmızı izleri kimin yaptığını bulmuştu.»
   - Açıklama: İzlerin sahibi bulunuyor ama resimdeki lekeler ve reçelin yenmesi çözülmeden hikaye bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0050` birebir aynı, `@degisim: kilitli -> yapışkan` (tutuyorsan), ardından `@onarim: e0c906d94d8ab3d8f64a18daa092d09c1ff4a599`, sonra gövde.

### Hikâye 7: tohum masa-0054 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | Koca Ayı
@tohum: masa-0054
- yer: ev (Maşa'nın evi ve önündeki bahçe. Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'paspas', fiil 'boşaltmak', sıfat 'cömert'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | ev | Koca Ayı
@plan: sebzeleri sulamak istedi ama su dolu kova çok ağırdı | suyun yarısını boşalttı ve kovayı rahatça taşıdı
@tohum: masa-0054
@degisim: paspas -> kova
Ormandaki ağaç evin bahçesinde Koca Ayı bir ağacın altında uyuyordu. Maşa, cömert dostu Koca Ayı'ya sürpriz yapmak için sebzeleri sulamak istedi. Ama su dolu büyük kova çok ağırdı. Maşa kovayı iki eliyle çekti ama kova yerinden oynamadı. Maşa biraz düşündü ve suyun yarısını domateslere boşaltmayı denedi. Kova hafifledi ve Maşa onu rahatça taşıdı. Kalan suyu da havuçlara döktü. Sonra Koca Ayı uyandı ve ıslak bahçeyi gördü. Şaşırdı ve kocaman gülümsedi. Maşa'ya koştu ve ona sıkıca sarıldı. "Sürpriz, Koca Ayı! Bugün bahçeni ben suladım!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "suyun yarısını domateslere boşaltmayı denedi"
   - Cümle 5: «Maşa biraz düşündü ve suyun yarısını domateslere boşaltmayı denedi.»
   - Açıklama: Kova yerinden bile oynamayacak kadar ağırken Maşa suyunu domateslere boşaltabiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0054` birebir aynı, `@degisim: paspas -> kova` (tutuyorsan), ardından `@onarim: 13ceac213fc4bf060b1e51eb6d85f5ee580b6726`, sonra gövde.

### Hikâye 8: tohum masa-0056 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0056
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'yağ', fiil 'sakinleşmek', sıfat 'sabırsız'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: yaprakların arasından gelen sesi merak etti | sakinleşti ve yere elma koyunca kirpiyi gördü
@tohum: masa-0056
@degisim: yağ -> elma
Maşa ormanda elinde bir elmayla yürüyordu. Birden yaprakların arasından hışır hışır bir ses geldi. Maşa bu sesi çok merak etti. Hemen sesin geldiği yere koştu. Ama ses kesildi ve hiçbir şey kıpırdamadı. Maşa biraz bekledi ve sakinleşti. Sonra yeni bir şey denedi ve elmasını yere koydu. Yavaşça geri çekildi ve sessizce oturdu. Az sonra yaprakların arasından küçük bir burun çıktı. Ardından dikenli ve sabırsız bir kirpi göründü. Kirpi elmayı hemen kokladı ve mutlu mutlu yemeye başladı. Maşa çok sevindi, çünkü sesi yapan kirpiyi sonunda bulmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dikenli ve sabırsız bir kirpi"
   - Cümle 10: «Ardından dikenli ve sabırsız bir kirpi göründü.»
   - Açıklama: Saklanıp bekleyen kirpi için 'sabırsız' sıfatı bağlama uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dikenli ve sabırsız bir kirpi"
   - Cümle 10: «Ardından dikenli ve sabırsız bir kirpi göründü.»
   - Açıklama: 'Sabırsız' soyut bir özellik kelimesi ve 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0056` birebir aynı, `@degisim: yağ -> elma` (tutuyorsan), ardından `@onarim: 0a2853ba7dc5adb5d118e0bcabbb66313c883caa`, sonra gövde.

### Hikâye 9: tohum masa-0057 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0057
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yosun', fiil 'içmek', sıfat 'özel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: sincap şaka yapmak için kavanozun üstüne yosun koydu | sincabın ağzında yosun görüp yosunların altına baktı
@tohum: masa-0057
@degisim: içmek -> saklamak
Maşa tepede Koca Ayı ve sincapla bir arama oyunu oynuyordu. Koca Ayı, Maşa'nın özel reçel kavanozunu bir taşın arkasına sakladı. Ama sincap şaka yapmak için kavanozun üstüne yosun koydu. Maşa taşların arkasına baktı ama kavanozu göremedi. Sonra sincabın ağzında biraz yosun gördü. Maşa kavanozun yosunun altında olduğunu anladı. Büyük bir taşın yanında kabarık bir yosun yığını vardı. Maşa hemen o taşa koştu ve yosunları kaldırdı. Reçel kavanozu tam oradaydı! "Buldum, sincap, sen çok komiksin!" dedi Maşa. Koca Ayı güldü ve ellerini çırptı. Sincap da kuyruğunu salladı. Maşa çok sevindi, çünkü sevdiği reçeli oyunun sonunda bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa kavanozun yosunun altında olduğunu anladı"
   - Cümle 6: «Maşa kavanozun yosunun altında olduğunu anladı.»
   - Açıklama: Sincabın ağzındaki yosundan kavanozun yosun altında olduğu sonucuna sebepsiz bir sıçramayla varılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0057` birebir aynı, `@degisim: içmek -> saklamak` (tutuyorsan), ardından `@onarim: a8e37ae440f88bdc4870f74ec9ef374696ea3011`, sonra gövde.

### Hikâye 10: tohum masa-0058 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0058
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'basamak', fiil 'şişirmek', sıfat 'düzenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: parmakları reçelliydi ve balonun ucunu bağlayamadı | parmaklarını yaladı ve balonu sıkıca bağladı
@tohum: masa-0058
@degisim: düzenli -> sıkı
Güneş parlıyordu. Maşa tepede reçelli ekmeğini bitirdi ve kırmızı bir balon şişirdi. Ama parmakları reçelden yapış yapış olmuştu. Maşa balonun ucunu bağlayamadı ve balon elinden kaçtı. Balon komik bir sesle sağa sola uçtu. Sonra söndü ve taş bir basamağın üstüne düştü. Maşa balonuna baktı ve üzüldü. Maşa reçeli çok severdi ve parmaklarını tek tek yaladı. Artık parmakları temizdi. Balonu yeniden şişirdi ve ucuna sıkı bir düğüm attı. Bu kez balon hiç kaçmadı. Maşa balonu havaya attı ve yakaladı. Maşa balonuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama parmakları reçelden yapış yapış olmuştu"
   - Cümle 3: «Ama parmakları reçelden yapış yapış olmuştu.»
   - Açıklama: Yapışkan parmakların balonu bağlamayı neden engellediği akla yatkın değil; yapışkanlık tutmayı zorlaştırmaz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0058` birebir aynı, `@degisim: düzenli -> sıkı` (tutuyorsan), ardından `@onarim: 27eb134a17f27f762571b7f778900d5f5469cd18`, sonra gövde.

### Hikâye 11: tohum masa-0062 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0062
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'külah', fiil 'çırpmak', sıfat 'yamuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: tanımadığı sincap utandı ve yaprakların arasına saklandı | yapraktan külah yapıp içine fındık koydu
@tohum: masa-0062
Maşa ormanda reçel yiyerek yürüyordu. Bir ağacın dalında daha önce görmediği bir sincap gördü. Sincap onu görünce utandı ve yaprakların arasına saklandı. "Merhaba, sincap, benimle arkadaş olur musun?" diye sordu Maşa. Ama sincap saklandığı yerden çıkmadı. Maşa etrafına baktı ve yerde fındıklar gördü. Parmağındaki reçelle büyük bir yaprağı yapıştırıp yamuk bir külah yaptı. Külahı fındıkla doldurup ağacın dibine koydu. Sincap hemen aşağı indi ve bir fındık aldı. Sonra Maşa'nın yanına geldi ve kuyruğunu salladı. Maşa sevinçle ellerini yavaşça çırptı. Maşa çok mutluydu, çünkü yeni bir arkadaş bulmuştu.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Parmağındaki reçelle büyük bir yaprağı yapıştırıp"
   - Cümle 7: «Parmağındaki reçelle büyük bir yaprağı yapıştırıp yamuk bir külah yaptı.»
   - Açıklama: 'Yapıştırmak' neyin neye yapıştığını istiyor; cümle eksik ve bozuk kurulmuş.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bir yaprağı yapıştırıp yamuk"
   - Cümle 7: «Parmağındaki reçelle büyük bir yaprağı yapıştırıp yamuk bir külah yaptı.»
   - Açıklama: Yapıştırmanın neyi neye yapıştırdığı eksik; cümle dilbilgisel olarak tamamlanmamış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Parmağındaki reçelle büyük bir yaprağı yapıştırıp yamuk bir külah yaptı"
   - Cümle 7: «Parmağındaki reçelle büyük bir yaprağı yapıştırıp yamuk bir külah yaptı.»
   - Açıklama: Reçelle yapıştırılan külah akla yatkın değil ve işlevsiz, fındıklar doğrudan ağacın dibine konabilirdi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0062` birebir aynı, ardından `@onarim: c00cce640efc344a62d7bfce1bdd7f3f159bb03f`, sonra gövde.

### Hikâye 12: tohum masa-0064 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0064
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'mendil', fiil 'aydınlanmak', sıfat 'kuru'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: kirpi uzun otların arasından kelebekleri göremedi | kirpiye yakın bir taşa reçel sürdü ve kelebekler geldi
@tohum: masa-0064
Yağmur dindi ve orman birden aydınlandı. Maşa ile Koca Ayı reçelli ekmek yerken renkli kelebekler gördü. Ama küçük kirpi uzun otların arasından onları göremedi. "Kirpi, sen de görmelisin!" dedi Maşa. Maşa reçeli çok severdi ve kelebeklerin de tatlıyı sevdiğini biliyordu. Sonra kirpiye yakın düz bir taşa biraz reçel sürdü. Az sonra kelebekler gelip reçelin yanına kondu. Kirpi kelebekleri yakından görünce sevinçle burnunu oynattı. Maşa reçelli parmaklarını kuru mendiliyle sildi. Maşa, Koca Ayı ve kirpi yan yana oturup kelebekleri mutlu mutlu seyretti.
```

**Hakem bulguları (3):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Az sonra kelebekler gelip reçelin yanına kondu"
   - Cümle 7: «Az sonra kelebekler gelip reçelin yanına kondu.»
   - Açıklama: Çoğul canlı kelebekler arka planda kalmıyor, çözümün parçası olarak olaya katılıyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "kelebekler gelip reçelin yanına kondu"
   - Cümle 7: «Az sonra kelebekler gelip reçelin yanına kondu.»
   - Açıklama: Arka plandaki çoğul canlılar (kelebekler) çözüme katılıyor; K4 çoğul canlıların olaya katılmamasını ister.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa reçelli parmaklarını kuru mendiliyle sildi"
   - Cümle 9: «Maşa reçelli parmaklarını kuru mendiliyle sildi.»
   - Açıklama: Mendille parmak silme olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0064` birebir aynı, ardından `@onarim: 3ae6f19e74b13918b3afb613bf369191985d1a97`, sonra gövde.
