# Editör görevi (onarım): Keloğlan, onarım partisi 8

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar8.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar8.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0003 (deneme 3 -> 4)

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
@plan: otlar hep dağıldı ve sepet olmadı | arkadaşından yardım istedi ve otları onun gibi ördü
@tohum: keloglan-0003
Keloğlan ile Balkız tepede yumuşak otların üstüne oturdu. Keloğlan yeni şeyler öğrenmeyi severdi ve otlardan küçük bir sepet yapmak istedi. Uzun otları üst üste koydu, ama otlar hep dağıldı. Keloğlan bir daha denedi, yine olmadı. Sonra Balkız'a döndü ve ondan yardım istedi. Balkız bir otu alıp öbür otların arasından geçirdi. Keloğlan onu izledi ve otları kendisi sıkıca ördü. Otlar artık dağılmıyordu. Az sonra Keloğlan'ın elinde küçük bir sepet vardı. Balkız sepete sarı çiçekler koydu ve güldü. Keloğlan çok sevindi, çünkü Balkız'ın yardımıyla ilk sepetini yapmıştı.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Keloğlan onu izledi"
   - Cümle 7: «Keloğlan onu izledi ve otları kendisi sıkıca ördü.»
   - Açıklama: 'Onu' zamirinin Balkız'ı mı otu mu gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0003` birebir aynı, ardından `@onarim: 29b6080fb0977c1f23b8bd550e5f051fc2b5cfd5`, sonra gövde.

### Hikâye 2: tohum keloglan-0006 (deneme 4 -> 5)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
Bir sabah Keloğlan ile anası evde bir kek yaptı. Un torbası yırtıktı ve az un kalmıştı, bu yüzden kek küçük çıktı. Anası keki Keloğlan'a verdi ama kendine hiç kalmadı. Keloğlan keki annesiyle paylaşmak istedi. "Anneciğim, keki ikimiz için nasıl keserim?" diye sordu Keloğlan. "Kaşıkla önce ortadan, sonra yandan kes," dedi anası. Keloğlan bunu hemen öğrendi. Kek yumuşaktı ve kaşık kolayca girdi. Keloğlan kestikçe parçalar çoğaldı ve tabakta dört küçük kare oldu. Keloğlan iki kareyi annesine verdi. Anası bir kare yedi ve gülümsedi. "Seninle yemek çok güzel, anneciğim!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "keki ikimiz için nasıl keserim"
   - Cümle 5: «"Anneciğim, keki ikimiz için nasıl keserim?" diye sordu Keloğlan.»
   - Açıklama: Paylaşmak için kek kesmeyi bilmemek zorlama bir sorun; annesine kek kalmamasının asıl sebebi keki ona vermesi, yırtık torba değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0006` birebir aynı, `@degisim: jöle -> kek` (tutuyorsan), ardından `@onarim: e494c18648b9d11a22ee0ccb880abb9e984d3117`, sonra gövde.

### Hikâye 3: tohum keloglan-0007 (deneme 4 -> 5)

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
@plan: kartopu pasta için çok küçüktü | topu yere koyup karda iterek büyüttü
@tohum: keloglan-0007
Keloğlan dağda Bilgecan Dede'ye kardan bir pasta yapmak istedi. Kar bütün tepeyi kaplamıştı ve Dede ağacın altında kitap okuyordu. Ama Keloğlan'ın elleri küçüktü, bu yüzden kartopu da çok küçük oldu. Pasta için büyük bir top gerekiyordu. Keloğlan biraz sakardı ve kartoplarını hep elinden düşürürdü. Bu yüzden yerde yuvarlanan topun büyüdüğünü biliyordu. Topu yere koydu ve uzun uzun itti. Top kocaman oldu ve pastaya benzedi. Keloğlan pastanın üstüne küçük taşları yan yana, düzenli dizdi. "Dede, bak, sana bir sürprizim var!" dedi Keloğlan. Bilgecan Dede kitabını kapattı ve pastayı gördü. "Ne güzel bir pasta, çok teşekkür ederim, Keloğlan!" dedi Bilgecan Dede.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve kartoplarını hep elinden düşürürdü"
   - Cümle 5: «Keloğlan biraz sakardı ve kartoplarını hep elinden düşürürdü.»
   - Açıklama: Sakarlık özelliği çözümü getirmek için zorlama bir sebep olarak araya sokuluyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden yerde yuvarlanan topun büyüdüğünü biliyordu"
   - Cümle 6: «Bu yüzden yerde yuvarlanan topun büyüdüğünü biliyordu.»
   - Açıklama: Kartopunu elinden düşürmekle yuvarlanan topun büyüdüğünü bilmek arasındaki bağ zorlama; çözüm sakarlık özelliğinden sebepsizce çıkarılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0007` birebir aynı, ardından `@onarim: d24d6e759e8cdab6713acf0a2dcff229db5a41bd`, sonra gövde.

### Hikâye 4: tohum keloglan-0013 (deneme 3 -> 4)

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
@degisim: işaretli -> boş
Tepede serin bir rüzgar esiyordu. Keloğlan bir kayanın yanında oturmuş dinleniyordu. Birden ağaçtan ince bir ses geldi. Keloğlan bu sesi çok merak etti. Önce ağacın dallarına baktı ama bir şey göremedi. Sonra ağaca yürüdü ve askıda duran çantasına baktı. Çantada su şişesi vardı ve rüzgar şişenin ağzına esiyordu. Keloğlan sesin şişeden gelip gelmediğini öğrenmek istedi. Şişedeki suyun hepsini yere döktü. Rüzgar yine esti ve boş şişeden kalın bir ses çıktı. Ses gerçekten şişeden geliyordu! Sonra Keloğlan şişeyle mutlu mutlu oynadı.
```

**Hakem bulguları (5):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce ağacın dallarına baktı ama bir şey göremedi"
   - Cümle 5: «Önce ağacın dallarına baktı ama bir şey göremedi.»
   - Açıklama: Çözüm dallara bakma, çantaya bakma ve suyu dökme gibi ikiden fazla adıma yayılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "askıda duran çantasına baktı"
   - Cümle 6: «Sonra ağaca yürüdü ve askıda duran çantasına baktı.»
   - Açıklama: Ağaçta askı yoktur; 'dala asılı duran çantası' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "askıda duran çantasına"
   - Cümle 6: «Sonra ağaca yürüdü ve askıda duran çantasına baktı.»
   - Açıklama: 'Askıda' elbise askısını çağrıştırır; ağaç dalında asılı çanta için uygun değil.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şişedeki suyun hepsini yere döktü"
   - Cümle 9: «Şişedeki suyun hepsini yere döktü.»
   - Açıklama: Sesin kaynağı 7. cümlede zaten görülmüşken suyu dökmek soruya doğrudan yönelmeyen gereksiz bir adım.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "boş şişeden kalın bir ses çıktı"
   - Cümle 10: «Rüzgar yine esti ve boş şişeden kalın bir ses çıktı.»
   - Açıklama: Duyulan ses inceydi ama deneyde kalın bir ses çıkıyor, yine de sesin gerçekten şişeden geldiği sonucuna varılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0013` birebir aynı, `@degisim: işaretli -> boş` (tutuyorsan), ardından `@onarim: 0548dc676584e381f69ab8a3d609a1020d1b94d3`, sonra gövde.

### Hikâye 5: tohum keloglan-0014 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: rüzgar esti ve atkı uçup gitti | otlara bakıp atkıyı buldu
@tohum: keloglan-0014
@degisim: küpe -> atkı
Bir sabah Keloğlan ile Bilgecan Dede tepeye çıktı. Hava soğuktu, bu yüzden ikisi de sıcak giyinmişti. Ama birden rüzgar esti ve Keloğlan'ın kalın atkısı uçup gitti. Keloğlan etrafa baktı ama atkıyı göremedi. "Dede, onu nerede bulurum?" diye sordu Keloğlan. "Otlara bak, rüzgar onları bir yana itiyor," dedi Bilgecan Dede. Keloğlan yeni şeyler öğrenmeyi severdi ve hemen denedi. Otlara baktı, hepsi aynı yana dönmüştü. Keloğlan o yana yürüdü. Bir çalıda kırmızı atkı sallanıyordu! "Teşekkürler, Dede, bugün rüzgara bakmayı öğrendim!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bugün rüzgara bakmayı öğrendim"
   - Cümle 11: «"Teşekkürler, Dede, bugün rüzgara bakmayı öğrendim!" dedi Keloğlan.»
   - Açıklama: Rüzgara bakılmaz; otlara bakarak rüzgarın yönünü anlamak kastediliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bugün rüzgara bakmayı öğrendim"
   - Cümle 11: «"Teşekkürler, Dede, bugün rüzgara bakmayı öğrendim!" dedi Keloğlan.»
   - Açıklama: Rüzgar görülmez; 'rüzgara bakmak' mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0014` birebir aynı, `@degisim: küpe -> atkı` (tutuyorsan), ardından `@onarim: 66ecb879d2f954eb0ea4056ef0b54a423a9578ca`, sonra gövde.

### Hikâye 6: tohum keloglan-0015 (deneme 3 -> 4)

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
Bir sabah Keloğlan evin önünde eşeği Karakaçan için sürpriz hazırladı. Ona tatlı elmalar verecek ve komik bir maske takacaktı. Ama sepetteki elmalar yeşildi ve çok ekşiydi. Keloğlan dürüst bir çocuktu ve Karakaçan'ı kandırmak istemedi. Evdeki sepetlere tek tek bakıp tatlı elma aradı. Kapının yanındaki küçük sepette kırmızı elmalar buldu. Bir elmayı tattı ve elma çok tatlıydı. Keloğlan bu elmaları büyük bir tabağa dizdi. Sonra kağıttan yaptığı eşek maskesini yüzüne taktı. Islık çaldı ve Karakaçan hemen geldi. Eşek komik maskeyi görünce anırdı. Karakaçan elmaları bir bir yedi ve başını salladı. Sonra Keloğlan ile Karakaçan mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "komik bir maske takacaktı"
   - Cümle 2: «Ona tatlı elmalar verecek ve komik bir maske takacaktı.»
   - Açıklama: Maske sorunla ve çözümle ilgisiz ikinci bir iş olarak kuruluyor ve olayı dağıtıyor.
   - Açıklama: Maske sorunla ve çözümle ilgisi olmayan ikinci bir iş olarak ekleniyor.
   - Açıklama: Maske sorunla ve çözümle ilgisi olmayan ikinci bir hedef olarak kuruluyor ve olaya hiçbir katkı yapmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karakaçan'ı kandırmak istemedi"
   - Cümle 4: «Keloğlan dürüst bir çocuktu ve Karakaçan'ı kandırmak istemedi.»
   - Açıklama: Ekşi elma vermek kandırmak değildir; dürüstlük gerekçesi olaydan çıkmıyor.
   - Açıklama: Ekşi elma vermek kandırmak sayılmadığı için dürüstlük gerekçesi olaya bağlanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0015` birebir aynı, `@degisim: okumak -> aramak` (tutuyorsan), ardından `@onarim: 6d7ed8e91bef88f2e0152a045f9b6214d9ed2c11`, sonra gövde.

### Hikâye 7: tohum keloglan-0016 (deneme 3 -> 4)

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
Ormanda büyük ağaçların altında Keloğlan ile Balkız top oynuyordu. Yanlarında içmek için su dolu bir testi vardı. Birden minik top yuvarlandı ve ağacın dibinde dar bir deliğe düştü. Keloğlan eğilip baktı, top deliğin dibindeydi. Keloğlan deliğe su dökmeyi düşündü, ama testi çok ağırdı. Biraz sakar olduğu için ağır testiyi tek başına düşürebilirdi. "Balkız, testiyi benimle tutar mısın?" diye sordu Keloğlan. Balkız testinin bir yanından tuttu. İkisi testiyi yavaşça deliğe eğdi. Minik top suyla yukarı çıktı ve Keloğlan onu aldı. Keloğlan çok sevindi, çünkü minik topunu geri almıştı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Biraz sakar olduğu için"
   - Cümle 6: «Biraz sakar olduğu için ağır testiyi tek başına düşürebilirdi.»
   - Açıklama: 'Sakar' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0016` birebir aynı, ardından `@onarim: e8c008e4cfcc91dad9269cf5fff26ebcabe4be65`, sonra gövde.

### Hikâye 8: tohum keloglan-0018 (deneme 3 -> 4)

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
@plan: üç kurabiyeyi ikisine bölmek zordu | evde bir kurabiye yediğini söyleyip ikisini annesine verdi
@tohum: keloglan-0018
@degisim: küçülmek -> bölmek
Keloğlan ile anası dağda bir kayanın üstüne oturdu. Anası çantasını açtı ve üç vanilyalı kurabiye çıkardı. Ama üç kurabiyeyi ikisine bölmek zordu, bir tane fazlaydı. Dördüncü kurabiyeyi Keloğlan sabah evde yemişti. "Sen iki tane ye, Keloğlan," dedi anası. Keloğlan dürüst bir çocuktu ve başını iki yana salladı. "Hayır, anneciğim, ben evde bir kurabiye yedim," dedi Keloğlan. Sonra iki kurabiyeyi annesine verdi ve kendisi bir tane aldı. Böylece ikisi de iki kurabiye yedi. Anası gülümsedi ve Keloğlan'a sıkı sıkı sarıldı. "Çok teşekkürler, Keloğlan, seninle burada olmak çok güzel!" dedi anası.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dördüncü kurabiyeyi Keloğlan sabah evde yemişti"
   - Cümle 4: «Dördüncü kurabiyeyi Keloğlan sabah evde yemişti.»
   - Açıklama: Daha önce hiç kurulmamış bir dördüncü kurabiye çözümü getirmek için sebepsizce ortaya çıkarılıyor.
   - Açıklama: Evde yenen kurabiye sebepsizce anlatılıp çözümü hazır getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0018` birebir aynı, `@degisim: küçülmek -> bölmek` (tutuyorsan), ardından `@onarim: e5828c7530681493ab79d9dc3ce16079eb1dd29a`, sonra gövde.

### Hikâye 9: tohum keloglan-0019 (deneme 3 -> 4)

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
Bir sabah Keloğlan ormanda tahta çemberini yuvarlayıp eğleniyordu. Uykulu eşeği Karakaçan da sırtında odunlarla yanında yürüyordu. Birden odunları tutan eski ip koptu ve odunlar yere döküldü. Karakaçan durdu ve üzgün üzgün başını eğdi. Keloğlan dürüst bir çocuktu ve ona doğruyu söyledi. "Sen bir şey yapmadın, ip çok eskiydi, Karakaçan," dedi Keloğlan. Karakaçan başını kaldırdı. Keloğlan odunları topladı. Sonra odunları çemberin içine sıkıca dizdi. Çember bütün odunları bir arada tuttu. Keloğlan yükü eşeğinin sırtına koydu. Karakaçan esnedi, başını salladı ve yavaşça yürüdü. Keloğlan bundan sonra yola çıkmadan önce ipleri hep kontrol etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve ona doğruyu söyledi.»
   - Açıklama: Tohumdaki dürüstlük sorunu çözmüyor; çözüm çemberle geliyor, özellik işe yarar biçimde kullanılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve ona doğruyu söyledi"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve ona doğruyu söyledi.»
   - Açıklama: Dürüstlük özelliği olaya zorla ekleniyor; ortada söylenmesi zor bir doğru yok ve bu cümle olaydan çıkmıyor.
   - Açıklama: Dürüstlük ve doğruyu söyleme olayı sorunla bağlantısız, sebepsiz eklenmiş işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0019` birebir aynı, ardından `@onarim: 834c8b1743e0cab33884eb5da1813f5c890060cc`, sonra gövde.

### Hikâye 10: tohum keloglan-0022 (deneme 2 -> 3)

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
Ormanda büyük ağaçların altında kıvrımlı bir yol vardı. Keloğlan bu yolda hazine arama oyunu oynuyordu. Bilgecan Dede hazine olarak yolun bir yanına küçük bir kese saklamıştı. Keloğlan biraz sakardı ve yolun iki yanını karıştırdı. Hep öbür yana baktı ve keseyi bulamadı. "Dede, bana biraz yardım eder misin?" diye sordu Keloğlan. "Hazine, uzun otların olduğu kenarda," dedi Bilgecan Dede. Keloğlan hemen uzun otlara yürüdü. Otlar bacaklarını gıdıkladı ve Keloğlan kıkır kıkır güldü. Keloğlan otları eliyle ayırdı ve kahverengi keseyi gördü. Kesenin içinde üç tane ceviz vardı. "Gel, cevizleri birlikte yiyelim, Dede!" dedi Keloğlan.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yolun iki yanını karıştırdı"
   - Cümle 4: «Keloğlan biraz sakardı ve yolun iki yanını karıştırdı.»
   - Açıklama: 'Karıştırdı' burada hem 'ayırt edemedi' hem 'eşeledi' anlamına gelebiliyor; anlam belirsiz.
   - Açıklama: 'Karıştırmak' burada 'ayırt edememek' anlamında kullanılmış ve çocuk için 'eşelemek' anlamıyla karışıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "keseyi bulamadı"
   - Cümle 5: «Hep öbür yana baktı ve keseyi bulamadı.»
   - Açıklama: Sorun ancak 5. cümlede, keseyi bulamadığında söyleniyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Hep öbür yana baktı ve keseyi bulamadı"
   - Cümle 5: «Hep öbür yana baktı ve keseyi bulamadı.»
   - Açıklama: Kesenin bulunamaması sorunu ilk üç cümlede değil beşinci cümlede söyleniyor.
4. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: ""Hazine, uzun otların"
   - Cümle 7: «"Hazine, uzun otların olduğu kenarda," dedi Bilgecan Dede.»
   - Açıklama: Özne ile yüklem arasına gereksiz virgül konmuş.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Keloğlan hemen uzun otlara yürüdü"
   - Cümle 8: «Keloğlan hemen uzun otlara yürüdü.»
   - Açıklama: Yön eksik; 'uzun otlara doğru yürüdü' olmalı.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Otlar bacaklarını gıdıkladı"
   - Cümle 9: «Otlar bacaklarını gıdıkladı ve Keloğlan kıkır kıkır güldü.»
   - Açıklama: Gıdıklanma ayrıntısı olaya hiçbir şey katmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0022` birebir aynı, ardından `@onarim: d75d3fc4be734fd09ae08bd4c81d10d487ac76ae`, sonra gövde.

### Hikâye 11: tohum keloglan-0023 (deneme 2 -> 3)

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
Evin mutfağında Keloğlan ile Balkız çorba oyunu oynuyordu. Keloğlan çorbayı yapacaktı ve Balkız'ı eski masaya oturttu. Ama masanın bir ayağı kısaydı ve masa sallanıyordu. "Böyle yemek yiyemem, Keloğlan," dedi Balkız gülerek. Keloğlan evdeki alet kutusunu getirdi ve içinde küçük bir tahta aradı. Biraz sakar olduğu için kutuyu yere düşürdü. Keloğlan aletleri topladı ve aralarında tahtayı buldu. Tahtayı masanın kısa ayağının altına koydu. Masa artık hiç sallanmadı. "Buyur, sıcak çorban hazır," dedi Keloğlan. Balkız boş tabaktan çorba içer gibi yaptı ve güldü. Keloğlan bundan sonra oyuna başlamadan önce masanın ayaklarına baktı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Biraz sakar olduğu için kutuyu yere düşürdü"
   - Cümle 6: «Biraz sakar olduğu için kutuyu yere düşürdü.»
   - Açıklama: Kutunun düşmesi çözüme bir şey katmayan araya giren işlevsiz bir olay.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bundan sonra oyuna başlamadan önce masanın ayaklarına baktı"
   - Cümle 12: «Keloğlan bundan sonra oyuna başlamadan önce masanın ayaklarına baktı.»
   - Açıklama: 'Bundan sonra' alışkanlık bildirir; fiil 'bakardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0023` birebir aynı, ardından `@onarim: 94e23ca31574c3954e5fa887b3b127696b9a6de8`, sonra gövde.

### Hikâye 12: tohum keloglan-0024 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: kabak düştü ve çalıların arkasında kayboldu | yerdeki izi inceledi ve kabağı buldu
@tohum: keloglan-0024
@degisim: balkabağı -> kabak
Ormanda büyük ağaçların arasında dar bir yol vardı. Keloğlan elinde büyük bir kabakla bu yoldan eve dönüyordu. Keloğlan biraz sakardı ve kabak elinden düştü. Kabak hızla yuvarlandı ve çalıların arkasında kayboldu. Keloğlan çalıların arkasına baktı ama kabak orada yoktu. Kabağın nereye gittiğini çok merak etti. Keloğlan yere eğildi ve yaprakları dikkatle inceledi. Yapraklarda uzun bir iz vardı, kabak oradan geçmişti. Keloğlan izin yanından yavaşça yürüdü. İz büyük bir ağacın dibinde bitti. Kabak orada duruyordu. Keloğlan çok memnun oldu ve kabağı alıp eve doğru neşeyle yürüdü.
```

**Hakem bulguları (3):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Keloğlan biraz sakardı ve kabak elinden düştü.»
   - Açıklama: İlk üç cümlede yalnız kabağın düştüğü söyleniyor; asıl sorun olan kaybolma ancak 4. cümlede geliyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "çalıların arkasında kayboldu"
   - Cümle 4: «Kabak hızla yuvarlandı ve çalıların arkasında kayboldu.»
   - Açıklama: Asıl sorun olan kabağın kaybolması ancak 4. cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan çok memnun oldu"
   - Cümle 12: «Keloğlan çok memnun oldu ve kabağı alıp eve doğru neşeyle yürüdü.»
   - Açıklama: 'Memnun olmak' 3 yaşındaki çocuk için soyut; 'sevindi' yeterli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0024` birebir aynı, `@degisim: balkabağı -> kabak` (tutuyorsan), ardından `@onarim: 26c0dda54a3fdc7957d851437360505885cffa68`, sonra gövde.
