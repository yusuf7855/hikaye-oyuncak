# Editör görevi (onarım): Maşa, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar2.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0002 (deneme 2 -> 3)

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
Ormanda Koca Ayı, Maşa ile kirpi için kahvaltı hazırlıyordu. Ama reçel kavanozu sepetten düşmüş, kapağı açılmış ve bir yere yuvarlanmıştı. Koca Ayı her yere baktı ama kavanozu bulamadı. Maşa, Koca Ayı'ya yardım etmek istedi. Maşa reçeli çok sevdiği için onun kokusunu iyi biliyordu. Burnunu havaya kaldırdı ve derin derin kokladı. Çalıların arkasından gizemli bir koku geliyordu. Bu, reçelin tatlı kokusuydu. Maşa hemen çalılara koştu. Kavanoz orada, çimenlerin üstünde duruyordu. "Buldum, Koca Ayı, işte reçel!" dedi Maşa. Koca Ayı sevinçle kavanozu aldı ve ekmeklere reçel sürdü. Kirpi de burnunu kavanoza uzattı. "Kahvaltı hazır, hadi hep birlikte yiyelim!" dedi Maşa.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kokusunu takip edip kavanozu"
   - Cümle 0 (plan satırı): «reçel kavanozu sepetten düşüp kayboldu | reçelin kokusunu takip edip kavanozu buldu»
   - Açıklama: 'Takip etmek' küçük çocuk için zor bir kelime; 'kokunun peşinden gidip' daha uygun.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "reçel kavanozu sepetten düşmüş"
   - Cümle 2: «Ama reçel kavanozu sepetten düşmüş, kapağı açılmış ve bir yere yuvarlanmıştı.»
   - Açıklama: Kavanozun sepetten neden düştüğü hiç söylenmiyor; sorunun sebebi yok.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "arkasından gizemli bir koku"
   - Cümle 7: «Çalıların arkasından gizemli bir koku geliyordu.»
   - Açıklama: 'Gizemli' soyut bir kelime; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0002` birebir aynı, `@degisim: silgi -> kavanoz` (tutuyorsan), ardından `@onarim: ac70775502fc2941091740c002ee3131fce89245`, sonra gövde.

### Hikâye 2: tohum masa-0003 (deneme 2 -> 3)

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
@plan: rüzgar ağaçtaki kurdeleyi uçurdu ve ağaç bulunamadı | ağaçların dibinde parlayan incileri aradı
@tohum: masa-0003
@degisim: barışmak -> bağlamak
Rüzgar hızlı hızlı esiyordu. Maşa, kuzeni Daşa için işaretli bir ağacın dibine inci bir kolye koymuştu. Ama rüzgar ağaçtaki kırmızı kurdeleyi uçurdu ve Maşa ağacı bulamadı. Daşa biraz ileride gözlerini kapatmış bekliyordu. Maşa kolyenin parlak incilerini aramayı denedi. Ağaçların diplerine dikkatle baktı. Bir ağacın dibinde beyaz inciler güneşte parlıyordu. Maşa kolyeyi aldı ve Daşa'nın yanına koştu. Daşa gözlerini açtı ve kolyeyi görünce çok sevindi. Maşa kolyeyi Daşa'nın boynuna taktı ve iki kız birlikte güldü. Maşa, kurdeleyi dala sıkıca bağlamak gerektiğini öğrendi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "dibine inci bir kolye koymuştu"
   - Cümle 2: «Maşa, kuzeni Daşa için işaretli bir ağacın dibine inci bir kolye koymuştu.»
   - Açıklama: Sıfat sırası bozuk; 'bir inci kolye' ya da 'incili bir kolye' olmalı.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "ağacın dibine inci bir kolye koymuştu"
   - Cümle 2: «Maşa, kuzeni Daşa için işaretli bir ağacın dibine inci bir kolye koymuştu.»
   - Açıklama: Kartta Maşa'ya ait inci kolye gibi bir eşya yok; kapalı dünyaya dışarıdan eşya ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0003` birebir aynı, `@degisim: barışmak -> bağlamak` (tutuyorsan), ardından `@onarim: f94207088345d134dfb348233501f5c968e2d977`, sonra gövde.

### Hikâye 3: tohum masa-0005 (deneme 2 -> 3)

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
Bir sabah Maşa ormanda bir kirpi gördü. Kirpi büyük, beyaz bir mermer taşın üstünde uyumaya çalışıyordu. Ama taş çok sertti ve kirpi uyuyamadı. Maşa daha önce hiç yapraktan yatak yapmamıştı. Ama bu yeni işi hemen denedi. Ağaçların altından yumuşak yapraklar topladı. Yaprakları taşın yanına koydu ve küçük bir yatak yaptı. Kirpi taştan indi ve yaprakları kokladı. "Bu senin yeni yatağın, kirpi," dedi Maşa. Kirpi yumuşak yatağa kıvrıldı ve hemen uyudu. Maşa çok sevindi, çünkü yaptığı ilk yatak kirpiyi uyutmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "beyaz bir mermer taşın"
   - Cümle 2: «Kirpi büyük, beyaz bir mermer taşın üstünde uyumaya çalışıyordu.»
   - Açıklama: 'Mermer' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Mermer' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime ve hikayeye bir şey katmıyor.
   - Açıklama: 'Mermer' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0005` birebir aynı, `@degisim: değerli -> yumuşak` (tutuyorsan), ardından `@onarim: f5951301804b61dbb284e81d2bf92ae0259cb403`, sonra gövde.

### Hikâye 4: tohum masa-0006 (deneme 2 -> 3)

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
@plan: soğukta reçel buzlu oldu ve kaşık reçele girmedi | kavanozu elleriyle ısıttı ve reçel yumuşadı
@tohum: masa-0006
@degisim: asılmak -> sürmek
Maşa karlı ormanda ilk kez piknik yapıyordu. Kesesinden ekmeği ve reçel kavanozunu çıkardı. Ama soğukta reçel buzlu olmuştu ve kaşık içine girmedi. Maşa kaşıkla reçele tık tık vurdu. Reçel çok sertti. Maşa reçeli çok severdi ve onu hemen yemek istiyordu. Biraz düşündü ve kavanozu iki elinin arasına aldı. Elleri sıcacıktı ve kavanozu yavaş yavaş ısıttı. Maşa bir süre bekledi. Sonra kaşığı yeniden reçele soktu. Bu kez kaşık kolayca içine girdi. Maşa ekmeğine bol bol reçel sürdü. Sonra karların arasında oturdu ve ekmeğini mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "soğukta reçel buzlu olmuştu"
   - Cümle 3: «Ama soğukta reçel buzlu olmuştu ve kaşık içine girmedi.»
   - Açıklama: Reçel buzlu olmaz, donar ya da sertleşir; 'buzlu' kelimesi öznesine uymuyor.
   - Açıklama: Reçel için 'buzlu' yanlış kelime; 'donmuş' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "soğukta reçel buzlu oldu"
   - Cümle 3: «Ama soğukta reçel buzlu olmuştu ve kaşık içine girmedi.»
   - Açıklama: Reçel için 'buzlu' yanlış kelime; 'donmuş' olmalı.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Maşa ekmeğine bol bol reçel sürdü"
   - Cümle 12: «Maşa ekmeğine bol bol reçel sürdü.»
   - Açıklama: Yemek kayboldu denmesine rağmen Maşa sonunda ekmeğini yiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0006` birebir aynı, `@degisim: asılmak -> sürmek` (tutuyorsan), ardından `@onarim: 66d05699c51c2622d07eca83531a1a860e337625`, sonra gövde.

### Hikâye 5: tohum masa-0007 (deneme 2 -> 3)

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
@degisim: çevik -> hızlı
Bir sabah Maşa, Koca Ayı ve kirpi tepede sepetten kurabiye yiyordu. Sonra yeni bir oyun oynadılar ve kirpi saklandı. Ama kirpi yuvarlak taşların arasında top gibi kıvrılmıştı ve hiç görünmüyordu. Maşa her taşın arkasına baktı ama kirpiyi bulamadı. Kirpi elmayı çok severdi. Kirpiyi elmalı bir kurabiyeyle dışarı çıkarmayı denedi. Koca Ayı sepeti Maşa'ya uzattı. Maşa sepetten elmalı bir kurabiye aldı. Kurabiyeyi taşların yanına koydu ve sessizce bekledi. Az sonra taşların arasında küçük, dikenli bir şey kıpırdadı. Kirpi burnunu çıkardı ve hızlı adımlarla kurabiyeye koştu. "Buldum seni, kirpi!" dedi Maşa. Sonra üçü kurabiyeleri paylaştı ve oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kirpiyi elmalı bir kurabiyeyle dışarı çıkarmayı denedi"
   - Cümle 6: «Kirpiyi elmalı bir kurabiyeyle dışarı çıkarmayı denedi.»
   - Açıklama: Öznesiz cümlede bir önceki cümlenin öznesi kirpi olduğu için kimin denediği belli değil.
   - Açıklama: Önceki cümlenin öznesi kirpi olduğu için bu cümlede deneyenin Maşa olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0007` birebir aynı, `@degisim: çevik -> hızlı` (tutuyorsan), ardından `@onarim: 7a86e34ee52e71cc28f25d03c51bbf63c41cf27e`, sonra gövde.

### Hikâye 6: tohum masa-0009 (deneme 2 -> 3)

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
@degisim: kararlı -> yuvarlak
Maşa ormanda bir kütüğe oturdu ve kağıda sarılı kurabiyesini açtı. O sırada bir sincap kütüğe zıpladı ve kurabiyeye uzun uzun baktı. Sincap da kurabiye istiyordu ama kurabiye bir taneydi. Kurabiye ay gibi kocaman ve yuvarlaktı. Maşa kurabiyeyi sincapla paylaşmak istedi. Kurabiyeyi iki eliyle tuttu ve ikiye kırmayı denedi. Çıt diye bir ses geldi ve kurabiye ikiye ayrıldı. Şimdi Maşa'nın elinde iki yarım ay vardı. Maşa bir parçayı sincaba verdi. Sincap parçayı patileriyle tuttu ve hızlı hızlı yedi. Maşa da kendi parçasını yedi. Sonra boş kağıdı buruşturdu ve cebine koydu. "Birlikte yemek daha güzelmiş, sincap!" dedi Maşa.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kurabiye ay gibi kocaman"
   - Cümle 4: «Kurabiye ay gibi kocaman ve yuvarlaktı.»
   - Açıklama: Kurabiye ay benzetmesiyle anlatılıyor; mecaz küçük çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "elinde iki yarım ay vardı"
   - Cümle 8: «Şimdi Maşa'nın elinde iki yarım ay vardı.»
   - Açıklama: Kurabiye parçaları 'yarım ay' diye anılıyor; bu bir mecaz.
   - Açıklama: Kurabiye parçalarına 'yarım ay' demek mecazdır ve küçük çocuğu yanıltır.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa bir parçayı sincaba verdi"
   - Cümle 9: «Maşa bir parçayı sincaba verdi.»
   - Açıklama: Yabani bir sincaba elden insan yiyeceği vermek çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0009` birebir aynı, `@degisim: kararlı -> yuvarlak` (tutuyorsan), ardından `@onarim: 0566f94931fa86336577f3f1e9b6ee851ac038ec`, sonra gövde.

### Hikâye 7: tohum masa-0010 (deneme 2 -> 3)

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
Rüzgar hızlı hızlı esiyordu. Maşa evinin önünde zıplarken rüzgarın devirdiği boş vazodan bir ses duydu. Rüzgardan saklanan bir kirpi vazoya girmişti ama dışarı çıkamıyordu. Maşa hemen zıplamayı durdurdu ve vazonun yanına koştu. "Bekle, kirpi, sana yardım edeceğim," dedi Maşa. Maşa vazonun dibini yavaşça yukarı kaldırmayı denedi. Vazonun ağzı çimenlere doğru eğildi. Kirpi yavaş yavaş kaydı ve çimenlerin üstüne çıktı. Kirpi küçük burnunu kıpırdattı ve Maşa'ya baktı. "Oldu, kirpi, artık çıktın!" dedi Maşa. Sonra boş vazoyu dikkatle yerine koydu. Kirpi de çimenlerde mutlu mutlu dolaştı. Maşa çok sevindi, çünkü kirpiyi vazodan çıkarmıştı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "vazoya girmişti ama dışarı çıkamıyordu"
   - Cümle 3: «Rüzgardan saklanan bir kirpi vazoya girmişti ama dışarı çıkamıyordu.»
   - Açıklama: Vazo devrilmiş ve ağzı açık yatarken kirpinin neden dışarı çıkamadığı söylenmiyor.
   - Açıklama: Rüzgarın devirdiği yatık vazodan kirpinin neden çıkamadığı söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0010` birebir aynı, `@degisim: şık -> boş` (tutuyorsan), ardından `@onarim: 8fbb5fb643fb5b97d9e91191d2d9ca764403bb37`, sonra gövde.
