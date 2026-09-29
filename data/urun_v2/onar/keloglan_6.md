# Editör görevi (onarım): Keloğlan, onarım partisi 6

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar6.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar6.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0003 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0003
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'sepet', fiil 'oturmak', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: otlar hep dağıldı ve sepet olmadı | arkadaşından yardım istedi ve otları örmeyi öğrendi
@tohum: keloglan-0003
Keloğlan ile Balkız tepede yumuşak otların üstüne oturdu. Keloğlan yeni şeyler öğrenmeyi severdi ve otlardan küçük bir sepet yapmak istedi. Uzun otları üst üste koydu, ama otlar hep dağıldı. Keloğlan bir daha denedi, yine olmadı. Sonra Balkız'a döndü ve ondan yardım istedi. Balkız bir otu alıp öbür otların arasından geçirdi. Keloğlan onun gibi yaptı ve otları sıkıca ördü. Otlar artık dağılmıyordu. Az sonra Keloğlan'ın elinde küçük bir sepet vardı. Balkız sepete sarı çiçekler koydu ve güldü. Keloğlan çok sevindi, çünkü Balkız'ın yardımıyla ilk sepetini yapmıştı.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "arkadaşından yardım istedi ve otları örmeyi öğrendi"
   - Cümle 0 (plan satırı): «otlar hep dağıldı ve sepet olmadı | arkadaşından yardım istedi ve otları örmeyi öğrendi»
   - Açıklama: Gövdede Keloğlan'ın örmeyi öğrendiği ya da kendisinin ördüğü gösterilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0003` birebir aynı, ardından `@onarim: de167d9ad8a89e7c0e05dc971761a1d24910b1df`, sonra gövde.

### Hikâye 2: tohum keloglan-0006 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0006
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: paylaşmak
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'jöle', fiil 'çoğalmak', sıfat 'yırtık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: tek küçük bir kek vardı ve annesine hiç kalmadı | annesinden kesmeyi öğrendi ve keki paylaştı
@tohum: keloglan-0006
@degisim: jöle -> kek
Bir sabah Keloğlan ile anası evde bir kek yaptı. Un torbası yırtıktı ve içinde az un kalmıştı. Bu yüzden kek çok küçük çıktı. Anası keki Keloğlan'a verdi ama kendine hiç kalmadı. Keloğlan keki annesiyle paylaşmak istedi. "Anneciğim, bunu nasıl keserim?" diye sordu Keloğlan. "Kaşıkla önce ortadan, sonra yandan kes," dedi anası. Keloğlan bunu hemen öğrendi. Kek yumuşaktı ve kaşık kolayca girdi. Keloğlan kestikçe parçalar çoğaldı ve tabakta dört küçük kare oldu. Keloğlan iki kareyi annesine verdi. Anası bir kare yedi ve gülümsedi. "Seninle yemek çok güzel, anneciğim!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Anası keki Keloğlan'a verdi ama kendine hiç kalmadı"
   - Cümle 4: «Anası keki Keloğlan'a verdi ama kendine hiç kalmadı.»
   - Açıklama: Annesine kek kalmaması sorunu ilk üç cümlede değil dördüncü cümlede söyleniyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Anneciğim, bunu nasıl keserim?"
   - Cümle 6: «"Anneciğim, bunu nasıl keserim?" diye sordu Keloğlan.»
   - Açıklama: Sorun annesine kek kalmaması, ama çözüm doğrudan paylaşmak yerine kek kesmeyi öğrenmek gibi dolambaçlı bir yoldan gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0006` birebir aynı, `@degisim: jöle -> kek` (tutuyorsan), ardından `@onarim: f348e0ff12ab32805cdd5779bc527dd491b2f3dc`, sonra gövde.

### Hikâye 3: tohum keloglan-0007 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0007
- yer: dağ (Köyün yakınındaki tepe.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'kartopu', fiil 'kaplamak', sıfat 'düzenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: kartopu pasta için çok küçüktü | düşen topu karda iterek büyüttü
@tohum: keloglan-0007
Keloğlan dağda Bilgecan Dede'ye kardan bir pasta yapmak istedi. Kar bütün tepeyi kaplamıştı ve Dede ağacın altında kitap okuyordu. Ama Keloğlan'ın kartopu çok küçüktü, pasta için büyük bir top gerekiyordu. Keloğlan sakar davrandı ve topu elinden düşürdü. Top karda yuvarlandı ve üstüne kar yapıştı. Keloğlan topun biraz büyüdüğünü gördü ve düşündü. Sonra topu karda uzun uzun itti. Top büyüdü ve kocaman bir pasta oldu. Keloğlan pastanın üstüne düzenli bir sırayla küçük taşlar dizdi. "Dede, bak, sana bir sürprizim var!" dedi Keloğlan. Bilgecan Dede kitabını kapattı ve pastayı gördü. "Ne güzel bir pasta, çok teşekkür ederim, Keloğlan!" dedi Bilgecan Dede.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Keloğlan'ın kartopu çok küçüktü"
   - Cümle 3: «Ama Keloğlan'ın kartopu çok küçüktü, pasta için büyük bir top gerekiyordu.»
   - Açıklama: Kartopunun neden küçük olduğu söylenmiyor; sorun yalnızca işin henüz bitmemiş olması.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan sakar davrandı"
   - Cümle 4: «Keloğlan sakar davrandı ve topu elinden düşürdü.»
   - Açıklama: 'Sakar davranmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir nitelendirme.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan sakar davrandı ve topu elinden düşürdü"
   - Cümle 4: «Keloğlan sakar davrandı ve topu elinden düşürdü.»
   - Açıklama: Çözüm figürün düşüncesinden değil, rastlantı bir düşürmeden sebepsizce doğuyor.
   - Açıklama: Çözüm figürün düşüncesinden değil sebepsiz bir kazadan çıkıyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "düzenli bir sırayla küçük taşlar dizdi"
   - Cümle 9: «Keloğlan pastanın üstüne düzenli bir sırayla küçük taşlar dizdi.»
   - Açıklama: 'Düzenli bir sırayla' soyut bir anlatım ve 3 yaşındaki çocuğa ağır.
   - Açıklama: 'Düzenli bir sırayla' küçük çocuk için soyut ve gereksiz bir ifade.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0007` birebir aynı, ardından `@onarim: 2606b0dc9a6e34e4b33cf5036bbef77336a39e82`, sonra gövde.

### Hikâye 4: tohum keloglan-0013 (deneme 2 -> 3)

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
@plan: tepede ince bir sesin nereden geldiği belli değildi | suyu yere döktü ve sesin şişeden geldiğini buldu
@tohum: keloglan-0013
Tepede serin bir rüzgar esiyordu. Keloğlan bir kayanın yanında oturmuş dinleniyordu. Birden ağaçtan ince bir ses geldi. Keloğlan bu sesi çok merak etti. Önce kayaların arkasına baktı ama bir şey bulamadı. Sonra ağaca yürüdü ve askıda duran çantasına baktı. Çantada su şişesi vardı ve rüzgar şişenin ağzına esiyordu. Keloğlan sesin şişeden gelip gelmediğini öğrenmek istedi. Suyu şişenin işaretli yerine kadar yere döktü. Rüzgar yine esti ve bu kez kalın bir ses çıktı. Ses gerçekten şişeden geliyordu! Sonra Keloğlan şişeyle ince ve kalın sesler çıkarıp mutlu mutlu oynadı.
```

**Hakem bulguları (5):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Önce kayaların arkasına baktı"
   - Cümle 5: «Önce kayaların arkasına baktı ama bir şey bulamadı.»
   - Açıklama: Ses açıkça ağaçtan geldiği halde Keloğlan önce kayaların arkasına bakıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Suyu şişenin işaretli yerine kadar yere döktü"
   - Cümle 9: «Suyu şişenin işaretli yerine kadar yere döktü.»
   - Açıklama: Cümle bozuk kurulmuş; 'yerine kadar yere' anlamı bulanıklaştırıyor ve işaretli yer hiç tanıtılmamış.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Suyu şişenin işaretli yerine kadar yere döktü."
   - Cümle 9: «Suyu şişenin işaretli yerine kadar yere döktü.»
   - Açıklama: 'Suyu' bütün suyu anlatıyor ve 'işaretli yerine kadar yere döktü' anlamca karışık; 'suyun bir kısmını' olmalı.
4. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "şişenin işaretli yerine kadar"
   - Cümle 9: «Suyu şişenin işaretli yerine kadar yere döktü.»
   - Açıklama: Kartın masal köyü dünyasında ('tohum_yasak_kategoriler': çağdaş) üzerinde ölçü işareti olan çağdaş bir su şişesi yok.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Suyu şişenin işaretli yerine kadar"
   - Cümle 9: «Suyu şişenin işaretli yerine kadar yere döktü.»
   - Açıklama: Şişedeki işaret daha önce hiç kurulmadan sebepsizce beliriyor.
   - Açıklama: Şişedeki işaret sebepsiz beliriyor ve hiç kurulmadan kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0013` birebir aynı, ardından `@onarim: 0c2c48441cdfcdb7bcaded5c8c8269716bbbc30e`, sonra gövde.

### Hikâye 5: tohum keloglan-0014 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0014
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Bilgecan Dede
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'küpe', fiil 'giyinmek', sıfat 'kalın'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: çalıda sallanan pembe şeylerin ne olduğu belli değildi | yakından bakıp onların çiçek olduğunu buldu
@tohum: keloglan-0014
Bir sabah Keloğlan ile Bilgecan Dede tepeye çıktı. Hava soğuktu, bu yüzden ikisi de kalın giyinmişti. Keloğlan bir çalıda sallanan pembe, küçük şeyler gördü. Bunların ne olduğunu çok merak etti. "Dede, bunlar meyve mi?" diye sordu Keloğlan. "Yakından bak, belki sen bulursun," dedi Bilgecan Dede. Keloğlan eğildi ve dikkatle baktı. "Bunlar çiçek, yaprakları var!" dedi Keloğlan. "Evet, adı küpe çiçeği, çünkü küpe gibi sallanır," dedi Bilgecan Dede. Keloğlan yere düşmüş bir çiçeği aldı ve ceketinin üstüne taktı. Bilgecan Dede bunu görünce gülümsedi. "Teşekkürler, Dede, bugün yeni bir çiçek öğrendim!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bunların ne olduğunu çok merak etti"
   - Cümle 4: «Bunların ne olduğunu çok merak etti.»
   - Açıklama: Sorun yalnızca bir merak; ortada sebebi söylenen gerçek bir sorun yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0014` birebir aynı, ardından `@onarim: 6ab47355f36c72387361c7c8421971be2347b3e0`, sonra gövde.

### Hikâye 6: tohum keloglan-0015 (deneme 2 -> 3)

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
@plan: sürpriz için elmalar çok ekşiydi | bütün sepetlere baktı ve tatlı elmalar buldu
@tohum: keloglan-0015
@degisim: okumak -> aramak
Bir sabah Keloğlan evin önünde eşeği Karakaçan için sürpriz hazırladı. Kağıttan komik bir eşek maskesi yaptı ve yüzüne taktı. Ama sepetteki elmalar yeşildi ve çok ekşiydi. Karakaçan böyle elmaları hiç sevmezdi. Keloğlan dürüst bir çocuktu ve işini bırakmadı. Evdeki bütün sepetleri tek tek aradı. Kapının yanındaki küçük sepette kırmızı elmalar buldu. Bir elmayı tattı ve elma çok tatlıydı. Keloğlan bu elmaları büyük bir tabağa dizdi. Sonra ıslık çaldı ve Karakaçan hemen geldi. Eşek komik maskeyi görünce yüksek sesle anırdı. Keloğlan tabağı ona uzattı. Karakaçan elmaları bir bir yedi ve başını salladı. Sonra Keloğlan ile Karakaçan mutlu mutlu oynadı.
```

**Hakem bulguları (7):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sürpriz için elmalar çok ekşiydi"
   - Cümle 0 (plan satırı): «sürpriz için elmalar çok ekşiydi | bütün sepetlere baktı ve tatlı elmalar buldu»
   - Açıklama: Plan cümlesi eksik kurulmuş; 'sürpriz için ayrılan elmalar' gibi bir tamlama gerekiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kağıttan komik bir eşek maskesi yaptı ve yüzüne taktı"
   - Cümle 2: «Kağıttan komik bir eşek maskesi yaptı ve yüzüne taktı.»
   - Açıklama: Maske ekşi elma sorunuyla hiç ilgisi olmayan ayrı bir iş olarak kuruluyor ve olayın akışına bir şey katmıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kağıttan komik bir eşek maskesi yaptı"
   - Cümle 2: «Kağıttan komik bir eşek maskesi yaptı ve yüzüne taktı.»
   - Açıklama: Maske sorunla ilgisiz ayrı bir iplik olarak kuruluyor ve çözüme hiçbir katkısı yok.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini bırakmadı"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve işini bırakmadı.»
   - Açıklama: Vazgeçmemek dürüstlük değildir; 'dürüst' yanlış anlamda kullanılmış.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve işini bırakmadı.»
   - Açıklama: 'Dürüst' kelimesi işini bırakmamakla ilgisiz, yanlış anlamda kullanılmış.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini bırakmadı"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve işini bırakmadı.»
   - Açıklama: Tohumdaki dürüstlük yalnız etiket olarak sayılıyor, hikayede işe yarar biçimde kullanılmıyor.
7. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Evdeki bütün sepetleri tek tek aradı"
   - Cümle 6: «Evdeki bütün sepetleri tek tek aradı.»
   - Açıklama: 'Sepetleri aradı' sepetleri bulmaya çalışmak demektir; 'sepetlere baktı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0015` birebir aynı, `@degisim: okumak -> aramak` (tutuyorsan), ardından `@onarim: 539d2c46f60a19e490a897cc847f584c9630746c`, sonra gövde.

### Hikâye 7: tohum keloglan-0016 (deneme 2 -> 3)

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
Ormanda büyük ağaçların altında Keloğlan ile Balkız top oynuyordu. Yanlarında içmek için su dolu bir testi vardı. Birden minik top yuvarlandı ve ağacın dibinde dar bir deliğe düştü. Keloğlan eğilip baktı ama deliğe eli sığmadı. Keloğlan deliğe su dökmeyi düşündü, ama testi çok ağırdı. "Balkız, testiyi benimle tutar mısın?" diye sordu Keloğlan. Balkız testinin bir yanından tuttu. Keloğlan biraz sakardı ve suyun yarısı ayağına döküldü. İkisi de buna güldü. Bu kez ikisi testiyi yavaşça deliğe eğdi. Minik top suyla yukarı çıktı ve Keloğlan onu aldı. Keloğlan çok sevindi, çünkü minik topunu geri almıştı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Keloğlan eğilip baktı ama deliğe eli sığmadı"
   - Cümle 4: «Keloğlan eğilip baktı ama deliğe eli sığmadı.»
   - Açıklama: Ormanda ağaç dibindeki bir deliğe el sokmaya çalışmak çocuğun taklit edebileceği riskli bir davranış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve suyun yarısı ayağına döküldü"
   - Cümle 8: «Keloğlan biraz sakardı ve suyun yarısı ayağına döküldü.»
   - Açıklama: Tohumdaki sakarlık özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "suyun yarısı ayağına döküldü"
   - Cümle 8: «Keloğlan biraz sakardı ve suyun yarısı ayağına döküldü.»
   - Açıklama: Çözüm testiyi tutma, suyu dökme ve yeniden eğme olarak ikiden fazla adıma yayılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve suyun yarısı ayağına döküldü"
   - Cümle 8: «Keloğlan biraz sakardı ve suyun yarısı ayağına döküldü.»
   - Açıklama: Suyun dökülmesi olayı ilerletmiyor ve çözüme hiçbir katkısı olmayan işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0016` birebir aynı, ardından `@onarim: afc34ea716a77f5edb319b98cf065bc865522f07`, sonra gövde.

### Hikâye 8: tohum keloglan-0018 (deneme 2 -> 3)

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
@plan: üç kurabiye ikiye eşit bölünmüyordu | evde bir kurabiye yediğini söyleyip ikisini annesine verdi
@tohum: keloglan-0018
@degisim: küçülmek -> bölmek
Keloğlan ile anası dağda bir kayanın üstüne oturdu. Anası çantasını açtı ve üç vanilyalı kurabiye çıkardı. Dördüncü kurabiyeyi Keloğlan sabah evde yemişti. Ama üç kurabiyeyi ikiye eşit bölmek zordu. "Sen iki tane ye, Keloğlan," dedi anası. Keloğlan dürüst bir çocuktu ve başını iki yana salladı. "Hayır, anneciğim, ben evde bir kurabiye yedim," dedi Keloğlan. Sonra iki kurabiyeyi annesine verdi ve kendisi bir tane aldı. Böylece ikisi de iki kurabiye yedi. Kurabiyeler çok güzel vanilya kokuyordu. Anası kurabiyelerini yedi ve Keloğlan'a sıkı sıkı sarıldı. "Çok teşekkürler, Keloğlan, seninle burada olmak çok güzel!" dedi anası.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "üç kurabiyeyi ikiye eşit bölmek zordu"
   - Cümle 4: «Ama üç kurabiyeyi ikiye eşit bölmek zordu.»
   - Açıklama: 'Eşit bölmek' soyut bir kavram, 3 yaşındaki çocuk anlamaz.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama üç kurabiyeyi ikiye eşit bölmek zordu"
   - Cümle 4: «Ama üç kurabiyeyi ikiye eşit bölmek zordu.»
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede söyleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kurabiyeler çok güzel vanilya kokuyordu"
   - Cümle 10: «Kurabiyeler çok güzel vanilya kokuyordu.»
   - Açıklama: Koku ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0018` birebir aynı, `@degisim: küçülmek -> bölmek` (tutuyorsan), ardından `@onarim: 379f5889974becb073a18d444ba9a06e79b61968`, sonra gövde.

### Hikâye 9: tohum keloglan-0019 (deneme 2 -> 3)

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
Bir sabah Keloğlan ormanda tahta çemberini yuvarlayıp eğleniyordu. Uykulu eşeği Karakaçan da sırtında odunlarla yanında yürüyordu. Birden odunları tutan eski ip koptu ve odunlar yere döküldü. Karakaçan durdu ve üzgün üzgün başını eğdi. Keloğlan odunları tek tek topladı. Sonra odunları çemberin içine sıkıca dizdi. Çember bütün odunları bir arada tuttu. Keloğlan yükü eşeğinin sırtına dikkatle koydu. Keloğlan dürüst davrandı ve "Yük çok ağır, yavaş yürü, Karakaçan," dedi. Karakaçan esnedi, başını salladı ve yavaşça yürüdü. Keloğlan bundan sonra yola çıkmadan önce ipleri hep kontrol etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst davrandı"
   - Cümle 9: «Keloğlan dürüst davrandı ve "Yük çok ağır, yavaş yürü, Karakaçan," dedi.»
   - Açıklama: Eşeğe yavaş yürümesini söylemek dürüstlük değildir; 'dürüst' kelimesi yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst davrandı ve"
   - Cümle 9: «Keloğlan dürüst davrandı ve "Yük çok ağır, yavaş yürü, Karakaçan," dedi.»
   - Açıklama: Eşeğe yavaş yürümesini söylemek dürüstlük değil; özellik kelimesi yanlış anlamda kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst davrandı ve"
   - Cümle 9: «Keloğlan dürüst davrandı ve "Yük çok ağır, yavaş yürü, Karakaçan," dedi.»
   - Açıklama: Tohumdaki dürüstlük özelliği sorunu çözmeye hiç katkı vermeden, yükün ağır olduğunu söylemeye zorla yapıştırılmış; bu yüzden 'ozellikler' alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki dürüstlük özelliği yalnız etiket olarak söyleniyor, olayda dürüstlük gerektiren bir iş yok; kartın özellik alanı işe yarar biçimde kullanılmamış.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst davrandı ve"
   - Cümle 9: «Keloğlan dürüst davrandı ve "Yük çok ağır, yavaş yürü, Karakaçan," dedi.»
   - Açıklama: Dürüstlük olayla hiç ilgili değil; işlevsiz bir ayrıntı olarak ekleniyor.
   - Açıklama: Dürüstlük olaydan çıkmıyor; sebepsiz ve işlevsiz bir ayrıntı olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0019` birebir aynı, ardından `@onarim: 23a80f2f8e69cbf219474b61fb5c1300d0d4c977`, sonra gövde.

### Hikâye 10: tohum keloglan-0022 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
Ormanda büyük ağaçların altında kıvrımlı bir yol vardı. Keloğlan elinde bir sopayla bu yolda hazine arama oyunu oynuyordu. Bilgecan Dede küçük bir kese saklamıştı ama Keloğlan onu bir türlü bulamadı. "Dede, bana biraz yardım eder misin?" diye sordu Keloğlan. "Hazine, yolun kenarındaki uzun otların arasında," dedi Bilgecan Dede. Keloğlan hemen uzun otlara koştu. Otlar bacaklarını gıdıkladı ve Keloğlan kıkır kıkır güldü. Keloğlan biraz sakardı ve gülerken sopasını otların içine düşürdü. Sopayı almak için eğilince kahverengi keseyi gördü. Kesenin içinde üç tane ceviz vardı. "Gel, cevizleri birlikte yiyelim, dede!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "onu bir türlü bulamadı"
   - Cümle 3: «Bilgecan Dede küçük bir kese saklamıştı ama Keloğlan onu bir türlü bulamadı.»
   - Açıklama: 'Bir türlü' deyimsel bir kalıp; 3 yaşındaki çocuğa uygun değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Keloğlan hemen uzun otlara koştu"
   - Cümle 6: «Keloğlan hemen uzun otlara koştu.»
   - Açıklama: Elinde sopa taşıyan çocuğun koşması taklit edilince tehlikeli bir davranıştır.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "gülerken sopasını otların içine düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve gülerken sopasını otların içine düşürdü.»
   - Açıklama: Kese, Keloğlan'ın aramasıyla değil sopanın tesadüfen düşmesiyle bulunuyor; çözüm sebepsizce geliyor.
   - Açıklama: Kese, Keloğlan'ın yöneldiği çözümle değil sebepsiz bir sakarlık kazasıyla bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0022` birebir aynı, ardından `@onarim: ad22aae9d67978eb6566f3ddb734199ab2a55e74`, sonra gövde.

### Hikâye 11: tohum keloglan-0023 (deneme 1 -> 2)

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
Evin mutfağında Keloğlan ile Balkız çorba oyunu oynuyordu. Keloğlan çorbayı yapacaktı ve Balkız'ı eski masaya oturttu. Ama masanın bir ayağı kısaydı ve masa sallanıyordu. "Böyle yemek yiyemem, Keloğlan," dedi Balkız gülerek. Keloğlan evdeki alet kutusunu getirdi. Biraz sakar olduğu için kutuyu yere düşürdü. Aletler yere döküldü ve içinden küçük bir tahta çıktı. Keloğlan bu tahtayı masanın kısa ayağının altına koydu. Masa artık hiç sallanmadı. "Buyur, sıcak çorban hazır," dedi Keloğlan. Balkız boş tabaktan çorba içer gibi yaptı ve güldü. Keloğlan bundan sonra oyuna başlamadan önce masanın ayaklarına baktı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sakar olduğu için kutuyu yere düşürdü"
   - Cümle 6: «Biraz sakar olduğu için kutuyu yere düşürdü.»
   - Açıklama: Tahta Keloğlan'ın aramasıyla değil kutunun kazayla düşmesiyle ortaya çıkıyor; çözüm tesadüfle geliyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yere döküldü ve içinden küçük bir tahta"
   - Cümle 7: «Aletler yere döküldü ve içinden küçük bir tahta çıktı.»
   - Açıklama: 'İçinden' zamiri özne 'aletler' iken kutuyu gösteriyor; kimi gösterdiği belirsiz.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Aletler yere döküldü ve içinden"
   - Cümle 7: «Aletler yere döküldü ve içinden küçük bir tahta çıktı.»
   - Açıklama: 'İçinden' zamiri özne 'aletler' olduğu için kutuyu gösterdiği belli değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "içinden küçük bir tahta çıktı"
   - Cümle 7: «Aletler yere döküldü ve içinden küçük bir tahta çıktı.»
   - Açıklama: Çözümü sağlayan tahta, kutunun kazara düşmesiyle sebepsizce beliriyor.
   - Açıklama: Çözümü sağlayan tahta, kutunun sakarlıkla düşmesiyle sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0023` birebir aynı, ardından `@onarim: e3317834229e0831f119a3bf2c4e484b4f042373`, sonra gövde.

### Hikâye 12: tohum keloglan-0024 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0024
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'balkabağı', fiil 'incelemek', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: ormanda bilinmeyen bir tok sesi geldi | kütüğü inceledi ve düşen kozalakları gördü
@tohum: keloglan-0024
@degisim: balkabağı -> kabak
Ormanda büyük ağaçların arasından tok tok diye bir ses geliyordu. Keloğlan elinde bir kabakla eve dönüyordu. Sesi duyunca durdu ve bu sesin ne olduğunu çok merak etti. Sesin geldiği yere yavaşça yürüdü. Orada içi boş, eski bir ağaç kütüğü vardı. Keloğlan kütüğü dikkatle inceledi ama bir şey göremedi. Keloğlan biraz sakardı ve kabağı elinden düşürdü. Kabak kütüğe hafifçe değdi ve aynı tok sesi çıktı. Tam o sırada yukarıdan bir kozalak düştü ve kütüğe tok diye çarptı. Keloğlan yukarı baktı ve ağaçtaki kozalakları gördü. Sesi yapan, kütüğe düşen kozalaklardı. Keloğlan çok memnun oldu ve kabağı alıp eve doğru neşeyle yürüdü.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bilinmeyen bir tok sesi geldi"
   - Cümle 0 (plan satırı): «ormanda bilinmeyen bir tok sesi geldi | kütüğü inceledi ve düşen kozalakları gördü»
   - Açıklama: Sıfat tamlaması hatalı; 'tok bir ses' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "bu sesin ne olduğunu çok merak etti"
   - Cümle 3: «Sesi duyunca durdu ve bu sesin ne olduğunu çok merak etti.»
   - Açıklama: Bir sesin ne olduğunu merak etmek çocuğun önemseyeceği bir sorun değil, önemsiz bir olay.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve kabağı elinden düşürdü"
   - Cümle 7: «Keloğlan biraz sakardı ve kabağı elinden düşürdü.»
   - Açıklama: Kabağın düşmesi çözüme bir şey katmıyor ve olay sebepsizce araya giriyor.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Kabak kütüğe hafifçe değdi"
   - Cümle 8: «Kabak kütüğe hafifçe değdi ve aynı tok sesi çıktı.»
   - Açıklama: Sesin kaynağını Keloğlan'ın bilinçli çabası değil tesadüfler ortaya çıkarıyor.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Tam o sırada yukarıdan bir kozalak düştü"
   - Cümle 9: «Tam o sırada yukarıdan bir kozalak düştü ve kütüğe tok diye çarptı.»
   - Açıklama: Cevabı Keloğlan bulmuyor; kozalak tesadüfen düşünce sorun kendiliğinden çözülüyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada yukarıdan bir kozalak düştü"
   - Cümle 9: «Tam o sırada yukarıdan bir kozalak düştü ve kütüğe tok diye çarptı.»
   - Açıklama: Çözüm tesadüfen düşen bir kozalakla sebepsizce geliyor, kabağın düşmesi de çözüme bağlanmayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0024` birebir aynı, `@degisim: balkabağı -> kabak` (tutuyorsan), ardından `@onarim: a29ee17872395acaa297e8e530282f7f4dd81bfd`, sonra gövde.
