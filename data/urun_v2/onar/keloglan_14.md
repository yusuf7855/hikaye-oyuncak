# Editör görevi (onarım): Keloğlan, onarım partisi 14

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar14.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar14.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0013 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0013
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'askı', fiil 'dökmek', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: yerde ıslak bir iz vardı ama yağmur yoktu | çantayı açtı ve kapağı açık şişeyi buldu
@tohum: keloglan-0013
@degisim: işaretli -> boş
Tepede sıcak bir rüzgar esiyordu. Keloğlan çantasının askısını omzuna takmış, yürüyordu. Birden yerde ıslak bir iz gördü. Ama hiç yağmur yoktu ve Keloğlan çok susamıştı. Keloğlan izin nereden geldiğini öğrenmek istedi. İz, tam onun ayaklarının arkasından başlıyordu. Keloğlan çantasına baktı, çanta da ıslaktı. Hemen çantayı yere koydu ve açtı. Çantada kapağı açık bir şişe vardı. Şişe suyu damla damla yere döküyordu. İzi Keloğlan'ın kendi suyu yapmıştı. Keloğlan kapağı sıkıca kapattı. Şişe yarı boştu, ama içinde biraz su kalmıştı. Keloğlan suyundan içti ve tepede mutlu mutlu yürüdü.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "İzi Keloğlan'ın kendi suyu yapmıştı"
   - Cümle 11: «İzi Keloğlan'ın kendi suyu yapmıştı.»
   - Açıklama: Suyun izi 'yapması' fiil-özne uyumu açısından yanlış ve bozuk bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0013` birebir aynı, `@degisim: işaretli -> boş` (tutuyorsan), ardından `@onarim: dfed08a89aa6fd4533924181d24d948a64b34f74`, sonra gövde.

### Hikâye 2: tohum keloglan-0015 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0015
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'maske', fiil 'okumak', sıfat 'ekşi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: eşeğe verilecek elmalar çok ekşiydi | sepetlere bakıp tatlı elmalar buldu
@tohum: keloglan-0015
@degisim: okumak -> aramak
Bir sabah Keloğlan evin önünde eşeği Karakaçan için sürpriz hazırladı. Onu sevindirmek için komik bir maske takıp tatlı elmalar verecekti. Ama sepetteki elmalar yeşildi ve çok ekşiydi. Keloğlan dürüsttü, ekşi elmayı tatlı diye vermek istemedi. Evdeki sepetlere tek tek bakıp tatlı elma aradı. Kapının yanındaki küçük sepette kırmızı elmalar buldu. Bir elmayı tattı ve elma çok tatlıydı. Keloğlan bu elmaları büyük bir tabağa dizdi. Sonra kağıttan yaptığı eşek maskesini yüzüne taktı. Islık çaldı ve Karakaçan hemen geldi. Eşek maskeyi görünce sevinçle anırdı. Karakaçan elmaları bir bir yedi ve başını salladı. Sonra Keloğlan ile Karakaçan mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "komik bir maske takıp"
   - Cümle 2: «Onu sevindirmek için komik bir maske takıp tatlı elmalar verecekti.»
   - Açıklama: Maske ekşi elma sorunuyla ilgisiz ikinci bir iplik açıyor ve olayda işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0015` birebir aynı, `@degisim: okumak -> aramak` (tutuyorsan), ardından `@onarim: b55ff5ea0510d065b9e0c494942cb9bc0997bc39`, sonra gövde.

### Hikâye 3: tohum keloglan-0016 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0016
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'testi', fiil 'oynamak', sıfat 'minik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: top ağacın dibinde dar bir deliğe düştü | arkadaşından yardım isteyip deliğe su döktü
@tohum: keloglan-0016
Ormanda büyük ağaçların altında Keloğlan ile Balkız top oynuyordu. Yanlarında içmek için su dolu bir testi vardı. Birden minik top yuvarlandı ve ağacın dibinde dar bir deliğe düştü. Keloğlan eğilip baktı, top deliğin dibindeydi. Keloğlan deliğe su dökmeyi düşündü ve testiyi kaldırdı. Ama testi çok ağırdı, Keloğlan da biraz sakardı. Testi elinden kaydı ve biraz su otlara aktı. "Balkız, testiyi benimle tutar mısın?" diye sordu Keloğlan. Balkız testinin bir yanından tuttu. İkisi testiyi yavaşça deliğe eğdi. Minik top suyla yukarı çıktı ve Keloğlan onu aldı. Keloğlan çok sevindi, çünkü minik topunu geri almıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan da biraz sakardı"
   - Cümle 6: «Ama testi çok ağırdı, Keloğlan da biraz sakardı.»
   - Açıklama: 'Sakar' 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0016` birebir aynı, ardından `@onarim: 0b5f3323fb08d306e243a2d2285b36b40f0a9208`, sonra gövde.

### Hikâye 4: tohum keloglan-0018 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0018
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'vanilya', fiil 'küçülmek', sıfat 'sıkı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: bir kurabiye yolda kırılmış ve küçülmüştü | iki kurabiyeyi de ikiye böldü ve paylaştı
@tohum: keloglan-0018
Keloğlan ile anası dağda bir kayanın üstüne oturdu. Anası çantasından iki vanilyalı kurabiye çıkardı. Ama bir kurabiye yolda kırılmış ve küçülmüştü. "Büyük kurabiyeyi sen al, Keloğlan," dedi anası. Keloğlan dürüst bir çocuktu. "Anneciğim, büyük kurabiyeyi ben de istiyorum, sen de istersin," dedi Keloğlan. Sonra iki kurabiyeyi de ikiye böldü. Bir büyük ve bir küçük parçayı annesine verdi. Öteki iki parçayı da kendisi aldı. Böylece ikisi de aynı kadar kurabiye aldı. Anası gülümsedi ve Keloğlan'a sıkı sıkı sarıldı. "Ne güzel bir fikir, Keloğlan, çok teşekkür ederim!" dedi anası.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 5: «Keloğlan dürüst bir çocuktu.»
   - Açıklama: Dürüstlük olaya bağlanmıyor; paylaşma dürüstlükten çıkmıyor, cümle işlevsiz.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "aynı kadar kurabiye aldı"
   - Cümle 10: «Böylece ikisi de aynı kadar kurabiye aldı.»
   - Açıklama: 'Aynı kadar' dilbilgisel değil; 'aynı miktarda' ya da 'eşit' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ikisi de aynı kadar kurabiye aldı"
   - Cümle 10: «Böylece ikisi de aynı kadar kurabiye aldı.»
   - Açıklama: 'aynı kadar' dilbilgisel olarak yanlış; 'aynı miktarda' ya da 'eşit' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0018` birebir aynı, ardından `@onarim: df1f10475e1e26084379c9c9b2f0910c08c2d522`, sonra gövde.

### Hikâye 5: tohum keloglan-0019 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0019
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çember', fiil 'eğlenmek', sıfat 'uykulu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: odunları tutan eski ip koptu ve odunlar döküldü | odunları toplayıp çemberin içine dizdi
@tohum: keloglan-0019
Bir sabah Keloğlan ormanda tahta çemberini yuvarlayıp eğleniyordu. Uykulu eşeği Karakaçan da sırtında odunlarla yanında yürüyordu. Birden odunları tutan eski ip koptu ve odunlar yere döküldü. Karakaçan durdu ve üzgün üzgün başını eğdi. "Üzülme, Karakaçan, odunları ben toplarım," dedi Keloğlan. Karakaçan başını kaldırdı. Odunlar çoktu, ama Keloğlan dürüsttü ve dediğini yaptı. Bütün odunları tek tek topladı. Sonra odunları çemberin içine sıkıca dizdi. Çember bütün odunları bir arada tuttu. Keloğlan yükü eşeğinin sırtına koydu. Karakaçan esnedi, başını salladı ve yavaşça yürüdü. Keloğlan bundan sonra yola çıkmadan önce ipleri hep kontrol etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama Keloğlan dürüsttü ve"
   - Cümle 7: «Odunlar çoktu, ama Keloğlan dürüsttü ve dediğini yaptı.»
   - Açıklama: Odunları toplamak dürüstlükle ilgili değil; özellik kelimesi yanlış yerde kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0019` birebir aynı, ardından `@onarim: 53ee0937ba0a064ac3f5477c1e6a4bf3c3d7f53e`, sonra gövde.

### Hikâye 6: tohum keloglan-0022 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0022
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kese', fiil 'gıdıklamak', sıfat 'kıvrımlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: saklanan küçük kese bulunamadı | yardım isteyip uzun otların arasında keseyi buldu
@tohum: keloglan-0022
@degisim: gıdıklamak -> ayırmak
Ormanda büyük ağaçların altında kıvrımlı bir yol vardı. Keloğlan bu yolda hazine arama oyunu oynuyordu, ama hazineyi bulamıyordu. Bilgecan Dede hazine olarak yolun bir yanına küçük bir kese saklamıştı. Keloğlan biraz sakardı ve baktığı yerleri hep karıştırdı. "Dede, bana biraz yardım eder misin?" diye sordu Keloğlan. "Hazine uzun otların arasında," dedi Bilgecan Dede. Keloğlan hemen uzun otlara doğru yürüdü. Otları eliyle ayırdı ve kahverengi keseyi gördü. Kesenin içinde üç tane ceviz vardı. "Gel, cevizleri birlikte yiyelim, Dede!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "baktığı yerleri hep karıştırdı"
   - Cümle 4: «Keloğlan biraz sakardı ve baktığı yerleri hep karıştırdı.»
   - Açıklama: 'Karıştırmak' burada hem dağıtmak hem de şaşırmak anlamına gelebiliyor; anlam belirsiz.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "baktığı yerleri hep karıştırdı"
   - Cümle 4: «Keloğlan biraz sakardı ve baktığı yerleri hep karıştırdı.»
   - Açıklama: Hazinenin bulunamamasının sebebi belirsiz ve akla yatkın biçimde kurulmuyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Keloğlan biraz sakardı ve baktığı yerleri hep karıştırdı"
   - Cümle 4: «Keloğlan biraz sakardı ve baktığı yerleri hep karıştırdı.»
   - Açıklama: Hazinenin bulunamamasının sebebi belirsiz ve zayıf; baktığı yerleri karıştırmak somut bir sebep vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0022` birebir aynı, `@degisim: gıdıklamak -> ayırmak` (tutuyorsan), ardından `@onarim: dad15a1bd78cadcf0404ccd543888fc418229c23`, sonra gövde.

### Hikâye 7: tohum keloglan-0023 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | Balkız
@tohum: keloglan-0023
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'alet', fiil 'oturtmak', sıfat 'eski'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | Balkız
@plan: masanın bir ayağı kısaydı ve masa sallandı | kısa ayağın altına küçük bir tahta koydu
@tohum: keloglan-0023
Evin mutfağında Keloğlan ile Balkız çorba oyunu oynuyordu. Keloğlan çorbayı yapacaktı ve Balkız'ı eski masaya oturttu. Ama masanın bir ayağı kısaydı ve masa sallanıyordu. "Böyle yemek yiyemem, Keloğlan," dedi Balkız gülerek. Keloğlan masa için küçük bir tahta aradı. Alet kutusunu getirdi ve aletleri tek tek çıkardı. Kutunun dibinde küçük bir tahta buldu. Keloğlan biraz sakardı ve tahta elinden düştü. Tahtayı aldı ve kısa ayağın altına koydu. Masa artık hiç sallanmadı. "Buyur, sıcak çorban hazır," dedi Keloğlan. Balkız boş tabaktan çorba içer gibi yaptı ve güldü. Keloğlan bundan sonra oyuna başlamadan önce masanın ayaklarına bakardı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Alet kutusunu getirdi ve aletleri tek tek çıkardı"
   - Cümle 6: «Alet kutusunu getirdi ve aletleri tek tek çıkardı.»
   - Açıklama: Çocuğun alet kutusunu karıştırması taklit edildiğinde tehlikeli olabilecek bir davranış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve tahta elinden düştü"
   - Cümle 8: «Keloğlan biraz sakardı ve tahta elinden düştü.»
   - Açıklama: Tohumdaki sakarlık özelliği çözüme katkı yapmıyor, yalnız araya eklenmiş.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve tahta elinden düştü"
   - Cümle 8: «Keloğlan biraz sakardı ve tahta elinden düştü.»
   - Açıklama: Tahtanın elinden düşmesi hiçbir sonuç doğurmayan işlevsiz bir ayrıntı.
   - Açıklama: Tahtanın düşmesi hiçbir sonuç doğurmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0023` birebir aynı, ardından `@onarim: 7ab65da9c79e7cab459ef96a9166795317005661`, sonra gövde.

### Hikâye 8: tohum keloglan-0025 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0025
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yaprak', fiil 'heyecanlanmak', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: tepeden ıslık sesi geldi ama ıslık çalan yoktu | otların altında sesi yapan içi boş bir dal buldu
@tohum: keloglan-0025
Keloğlan tepede güzel sarı yapraklar topluyordu. Birden rüzgar esti ve ince bir ıslık sesi duyuldu. Ama tepede ıslık çalan kimse yoktu. Keloğlan çok heyecanlandı ve bu sesi merak etti. Sesin geldiği yere doğru yürüdü. Ses yerden, kuru otların altından geliyordu. Keloğlan eğildi, ama biraz sakardı ve yapraklar elinden düştü. Keloğlan otları eliyle ayırdı ve küçük bir dal buldu. Dalın içi boştu ve ucunda bir delik vardı. Keloğlan deliği parmağıyla kapattı ve ıslık kesildi. Parmağını çekince ıslık yeniden başladı. Ses, dalın içinden geçen rüzgardan çıkıyordu. Keloğlan dalı rüzgara doğru tuttu ve ıslığı mutlu mutlu dinledi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesi yapan içi boş"
   - Cümle 0 (plan satırı): «tepeden ıslık sesi geldi ama ıslık çalan yoktu | otların altında sesi yapan içi boş bir dal buldu»
   - Açıklama: Ses 'yapılmaz', 'çıkarılır'; 'sesi çıkaran' olmalı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "biraz sakardı ve yapraklar elinden düştü"
   - Cümle 7: «Keloğlan eğildi, ama biraz sakardı ve yapraklar elinden düştü.»
   - Açıklama: Tohumdaki sakarlık özelliği sorunun çözümüne hiçbir katkı yapmadan araya sıkıştırılmış, işe yarar biçimde kullanılmamış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "biraz sakardı ve yapraklar elinden düştü"
   - Cümle 7: «Keloğlan eğildi, ama biraz sakardı ve yapraklar elinden düştü.»
   - Açıklama: Toplanan yaprakların düşmesi olayda hiçbir işe yaramıyor ve yapraklara bir daha dönülmüyor.
   - Açıklama: Yaprakların düşmesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0025` birebir aynı, ardından `@onarim: 36a08cf49813d2f5a4a730c9593e4c8495fe8799`, sonra gövde.

### Hikâye 9: tohum keloglan-0027 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0027
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'gümüş', fiil 'düzenlemek', sıfat 'sabırsız'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: sepet düştü ve çilekler otlara döküldü | özür diledi ve çilekleri toplayıp düzenledi
@tohum: keloglan-0027
@degisim: gümüş -> çilek
Keloğlan anasıyla ormanda çilek topluyordu. Keloğlan çilekleri hemen yemek için sabırsızlandı. Dolu sepeti hızla kaptı, ama biraz sakardı ve sepet elinden düştü. Bütün çilekler otlara döküldü. Keloğlan anasına üzgün üzgün baktı. "Özür dilerim, anne, acele ettim," dedi Keloğlan. "Üzülme, gel birlikte toplayalım," dedi anası. Keloğlan çilekleri otlardan tek tek topladı. Sonra onları sepette güzelce düzenledi. Bu kez sepeti iki eliyle sıkıca tuttu. Anası gülümsedi ve onun başını okşadı. "Teşekkürler, anneciğim, çilekleri birlikte yiyelim!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan çilekleri hemen yemek için sabırsızlandı"
   - Cümle 2: «Keloğlan çilekleri hemen yemek için sabırsızlandı.»
   - Açıklama: Tohumdaki özellik sakarlık; sabırsızlık ve acele kartın özellikler alanında olmayan ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0027` birebir aynı, `@degisim: gümüş -> çilek` (tutuyorsan), ardından `@onarim: 352aec340ca02a69a7e1a2b1c2b327a383025340`, sonra gövde.

### Hikâye 10: tohum keloglan-0031 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | eşeği
@tohum: keloglan-0031
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: yeni bir şeyi denemek
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'damla', fiil 'işaretlemek', sıfat 'kirli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | şato | eşeği
@plan: kağıda boya damladı ve kağıt kirlendi | fırçayı kabın kenarına silip yeniden boyadı
@tohum: keloglan-0031
@degisim: işaretlemek -> boyamak
Keloğlan şatonun bahçesinde ilk kez boyayla resim yapmayı denedi. Karakaçan resim çantasını sırtında taşımıştı. Ama kağıda iri bir boya damlası düştü ve kağıt kirli oldu. "Ah, resmim bozuldu!" dedi Keloğlan. Keloğlan fırçaya dikkatle baktı. Fırça boyayla doluydu. Fırçayı kabın kenarına hafifçe sildi. Böylece boyayı az almayı öğrendi. Sonra temiz bir kağıda şatonun yüksek kapısını boyadı. Bu kez kağıda hiç damla düşmedi. Karakaçan başını salladı. "Karakaçan, bak, ilk resmim ne güzel oldu!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ve kağıt kirli oldu"
   - Cümle 3: «Ama kağıda iri bir boya damlası düştü ve kağıt kirli oldu.»
   - Açıklama: Doğal kullanım 'kağıt kirlendi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0031` birebir aynı, `@degisim: işaretlemek -> boyamak` (tutuyorsan), ardından `@onarim: f946d17fc43f490377d9f6627e733a81eabf5017`, sonra gövde.

### Hikâye 11: tohum keloglan-0033 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0033
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'eldiven', fiil 'açmak', sıfat 'puantiyeli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşek acıktı ama ormanda hiç ot yoktu | çantasını açıp havuçları eşeğine yedirdi
@tohum: keloglan-0033
@degisim: puantiyeli -> benekli
Keloğlan benekli eldivenleriyle ormanda odun topluyordu. Eşeği Karakaçan odunları sırtında taşıyordu. Birden Karakaçan durdu ve yürümedi, çünkü çok acıkmıştı. Ama büyük ağaçların altında hiç ot yoktu. "Bekle, Karakaçan, çantamda havuç var," dedi Keloğlan. Keloğlan biraz sakardı, bu yüzden havuçları düşürmemek için eldivenlerini çıkardı. Sonra çantasını açtı ve havuçları Karakaçan'a tek tek verdi. Eşek havuçları yedi ve mutlu mutlu kuyruğunu oynattı. "Karnın doydu mu, Karakaçan?" diye sordu Keloğlan. Karakaçan başını iki kez salladı. Keloğlan çok sevindi, çünkü eşeği artık aç değildi.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Keloğlan benekli eldivenleriyle ormanda"
   - Cümle 1: «Keloğlan benekli eldivenleriyle ormanda odun topluyordu.»
   - Açıklama: Kartta Keloğlan'ın benekli eldivenleri gibi bir eşya yok; kapalı dünyaya aykırı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden havuçları"
   - Cümle 6: «Keloğlan biraz sakardı, bu yüzden havuçları düşürmemek için eldivenlerini çıkardı.»
   - Açıklama: Güvenli özellik kullanımı satırına göre sakarlık bir şeyi düşürmek ya da karıştırmak olarak gösterilmeli; burada yalnız gerekçe olarak anılıyor ve işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "havuçları düşürmemek için eldivenlerini çıkardı"
   - Cümle 6: «Keloğlan biraz sakardı, bu yüzden havuçları düşürmemek için eldivenlerini çıkardı.»
   - Açıklama: Güvenli özellik kullanımına göre sakarlık bir şeyi düşürmek ya da karıştırmak olarak gösterilmeli; burada sakarlık gösterilmiyor ve işe yaramıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "havuçları düşürmemek için eldivenlerini çıkardı"
   - Cümle 6: «Keloğlan biraz sakardı, bu yüzden havuçları düşürmemek için eldivenlerini çıkardı.»
   - Açıklama: Benekli eldivenler kurulup çözüme hiçbir katkı yapmayan işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0033` birebir aynı, `@degisim: puantiyeli -> benekli` (tutuyorsan), ardından `@onarim: 6562ace40b95e8f8ce0929488e3b548f2b526851`, sonra gövde.

### Hikâye 12: tohum keloglan-0034 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0034
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'krema', fiil 'güvenmek', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: sepet taşa çarptı ve arkadaşının keki ezildi | kekini ikiye bölüp arkadaşıyla paylaştı
@tohum: keloglan-0034
@degisim: güvenmek -> bölmek
Tepede serin bir rüzgar esiyordu. Keloğlan ile Balkız tekerlekli sepeti tepeye çekiyordu. Sepet bir taşa çarptı ve Balkız'ın keki yere düşüp ezildi. Balkız yerdeki keke üzgün üzgün baktı. Keloğlan'ın kremalı keki ise sepette duruyordu. Keloğlan kekini Balkız ile paylaşmak istedi. Keloğlan biraz sakardı, bu yüzden keki yavaşça ve dikkatle ikiye böldü. Sonra büyük parçayı Balkız'a verdi. İkisi tepede çimenlere oturdu ve parçalarını yedi. Keloğlan'ın burnuna biraz krema bulaştı ve Balkız güldü. Keloğlan çok mutluydu, çünkü kekini arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden keki yavaşça"
   - Cümle 7: «Keloğlan biraz sakardı, bu yüzden keki yavaşça ve dikkatle ikiye böldü.»
   - Açıklama: Güvenli özellik kullanımı satırına göre sakarlık bir şeyi düşürmek ya da karıştırmak olarak gösterilmeli; burada yalnız gerekçe olarak anılıyor ve işe yaramıyor.
   - Açıklama: Tohumdaki sakarlık özelliği güvenli kullanım satırındaki gibi bir şeyi düşürme ya da karıştırma olarak gösterilmiyor ve çözümde işe yaramıyor, yalnızca adı anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0034` birebir aynı, `@degisim: güvenmek -> bölmek` (tutuyorsan), ardından `@onarim: 637fe86c8df7986ce94deefb93acc0faf1d45ad8`, sonra gövde.
