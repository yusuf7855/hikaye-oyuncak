# Editör görevi (onarım): Keloğlan, onarım partisi 26

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar26.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar26.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0010 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0010
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'odun', fiil 'süpürmek', sıfat 'kırık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: kule kuru yaprakların üstünde kayıp yıkıldı | kırık bir dalla yaprakları süpürüp kuleyi yeniden yaptı
@tohum: keloglan-0010
Bir sabah Keloğlan ile eşeği Karakaçan ormanda küçük bir odun kulesi yapıyordu. Karakaçan sırtında odunlar getirdi, Keloğlan onları üst üste dizdi. Ama yer kuru yapraklarla doluydu ve kule onların üstünde kayıp yıkıldı. Keloğlan yaprakların altında ne olduğunu öğrenmek istedi. Bir yaprağı kaldırdı ve altında düz, sert toprak gördü. Keloğlan hemen kırık bir dal aldı ve yaprakları sağa sola süpürdü. Sonra kuleyi bu düz toprağın üstüne yeniden yaptı. "Bak, Karakaçan, kulemiz bu kez hiç kaymadı!" dedi Keloğlan. Karakaçan başını salladı. Keloğlan çok sevindi, çünkü kuleyi birlikte bitirmişlerdi.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kulemiz bu kez hiç kaymadı"
   - Cümle 8: «"Bak, Karakaçan, kulemiz bu kez hiç kaymadı!" dedi Keloğlan.»
   - Açıklama: Kule kaymaz, devrilir ya da yıkılır; fiil öznesine uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0010` birebir aynı, ardından `@onarim: 0de576eda45d6fab870d4c0b534b151d4308e4df`, sonra gövde.

### Hikâye 2: tohum keloglan-0031 (deneme 5 -> 6)

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
Keloğlan şatonun bahçesinde ilk kez boyayla resim yapmayı denedi. Karakaçan resim çantasını sırtında taşıyordu. Ama kağıda iri bir boya damlası düştü ve kağıt kirlendi. "Ah, resmim bozuldu!" dedi Keloğlan. Keloğlan fırçaya dikkatle baktı. Fırça boyayla doluydu. Fırçayı kabın kenarına hafifçe sildi. Böylece boyayı az almayı öğrendi. Sonra kirli kağıdı bir yana koydu. Karakaçan'ın çantasından temiz bir kağıt aldı. Kağıda şatonun yüksek kapısını çizdi ve resmi boyadı. Bu kez kağıda hiç damla düşmedi. Karakaçan başını salladı. "Karakaçan, bak, ilk resmim ne güzel oldu!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Karakaçan'ın çantasından temiz bir kağıt aldı"
   - Cümle 10: «Karakaçan'ın çantasından temiz bir kağıt aldı.»
   - Açıklama: Çözüm fırçayı silme, yeni kağıt alma ve yeniden boyama olmak üzere iki adımı aşıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0031` birebir aynı, `@degisim: işaretlemek -> boyamak` (tutuyorsan), ardından `@onarim: 2b306985e6b6916b4f1e739a83a85d18c3bb0e32`, sonra gövde.

### Hikâye 3: tohum keloglan-0053 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0053
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'dolma', fiil 'esmek', sıfat 'parlak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşek sırasını bekleyemedi ve topu hep kendisi itti | bir sen bir ben diyerek sırayla oynamayı önerdi
@tohum: keloglan-0053
@degisim: dolma -> top
Bir sabah ormanda serin bir rüzgar esiyordu. Keloğlan ile eşeği Karakaçan parlak bir topu büyük bir ağaca doğru itiyordu. Ama Karakaçan sırasını bekleyemedi ve topu hep kendisi itti. Keloğlan Karakaçan'ın başını okşadı. "Karakaçan, bir sen, bir ben oynayalım," dedi Keloğlan. Karakaçan başını salladı. Keloğlan topa ayağıyla bir kez vurdu ve Karakaçan'ı bekledi. Karakaçan da topu burnuyla itti ve top ağaca değdi. "Aferin, Karakaçan, bu sefer sen yaptın!" dedi dürüst Keloğlan. Karakaçan sevinçle anırdı. Keloğlan çok mutluydu, çünkü sırayla oynamak çok eğlenceli olmuştu.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dedi dürüst Keloğlan"
   - Cümle 9: «"Aferin, Karakaçan, bu sefer sen yaptın!" dedi dürüst Keloğlan.»
   - Açıklama: 'Dürüst' sıfatı bu övgü cümlesinde olaya uymuyor, yersiz kullanılmış.
   - Açıklama: 'Dürüst' sıfatı bu övgü repliğiyle ilgisiz ve yersiz kullanılmış.
   - Açıklama: 'Dürüst' sıfatı bu replikle ve olayla ilgisiz, yersiz kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi dürüst Keloğlan"
   - Cümle 9: «"Aferin, Karakaçan, bu sefer sen yaptın!" dedi dürüst Keloğlan.»
   - Açıklama: Tohumdaki dürüstlük özelliği yalnız bir sıfat olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki dürüstlük yalnız sıfat olarak ekleniyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0053` birebir aynı, `@degisim: dolma -> top` (tutuyorsan), ardından `@onarim: 96cf177fa24805232f232024e7ef8f1516665849`, sonra gövde.

### Hikâye 4: tohum keloglan-0057 (deneme 5 -> 6)

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
@plan: tepede tuhaf bir ses duyuldu | sesin peşinden gidip kayada küçük bir delik buldu
@tohum: keloglan-0057
@degisim: bindirmek -> karıştırmak
Rüzgar esiyordu ve tepede tuhaf bir ses duyuluyordu. Keloğlan tozlu bir taşa oturmuş, kalemiyle resim çiziyordu. Bu sesi çok merak etti. Keloğlan sesi önce eşeği Karakaçan'ın sesiyle karıştırdı. "Karakaçan, bunu sen mi yapıyorsun?" diye sordu Keloğlan. Karakaçan başını iki yana salladı. Keloğlan sesin peşinden kayaların arasına yürüdü. Bir kayanın dibinde küçük bir delik gördü. Keloğlan biraz sakardı ve kalemini elinden düşürdü. Kalem yuvarlandı ve deliğin üstünde durdu. Ses hemen kesildi. Keloğlan kalemi aldı ve ses yeniden başladı. Rüzgar bu delikten geçerken ıslık gibi bir ses çıkarıyordu. "Buldum, Karakaçan, sesi bu küçük delik yapıyormuş!" dedi Keloğlan sevinçle.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kalemini elinden düşürdü"
   - Cümle 9: «Keloğlan biraz sakardı ve kalemini elinden düşürdü.»
   - Açıklama: Sesin sebebi Keloğlan'ın çabasıyla değil, rastlantıyla düşen kalemle ortaya çıkıyor.
   - Açıklama: Sesin delikten geldiği sebepsiz bir kazayla, düşen kalemle kanıtlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0057` birebir aynı, `@degisim: bindirmek -> karıştırmak` (tutuyorsan), ardından `@onarim: 8747c182afa08728bd50e32ad24c8f42a8e7cfbe`, sonra gövde.

### Hikâye 5: tohum keloglan-0058 (deneme 5 -> 6)

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
@plan: ikisi ipi aynı anda çekti ve topaç devrildi | düşen atkıyla sırayla oynamayı önerdi
@tohum: keloglan-0058
@degisim: yetenekli -> hızlı
Keloğlan ile Bilgecan Dede evde tahta bir topaçla oynuyordu. Ama yalnız bir ip vardı. İkisi de ipi aynı anda çekti ve topaç devrildi. Keloğlan biraz sakardı ve o sırada atkısını dedenin kucağına düşürdü. Keloğlan atkıyı görünce güldü. "Sırayla oynayalım, atkı sende olunca ipi sen çek," dedi Keloğlan. Dede ipi çekince topaç masada uzun uzun döndü. "Dede, topaç çok hızlı döndü!" dedi Keloğlan. Dede gülümsedi ve atkıyı Keloğlan'a geri verdi. Keloğlan ipi çekince topaç yine güzelce döndü. İkisi bunu el çırparak kutladı. Keloğlan çok sevindi, çünkü sırayla oynamak ikisini de mutlu etmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "o sırada atkısını dedenin kucağına düşürdü"
   - Cümle 4: «Keloğlan biraz sakardı ve o sırada atkısını dedenin kucağına düşürdü.»
   - Açıklama: Atkı tesadüfen düşüyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Atkı sebepsizce düşüyor ve çözümü rastlantıyla getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0058` birebir aynı, `@degisim: yetenekli -> hızlı` (tutuyorsan), ardından `@onarim: 5119805a4abc89b2cd12e8f4006105893065ebf5`, sonra gövde.

### Hikâye 6: tohum keloglan-0063 (deneme 5 -> 6)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar kağıt topu sepetten uzağa itti | rüzgarın durmasını bekledi ve topu yavaşça attı
@tohum: keloglan-0063
@degisim: kilitli -> beyaz
Rüzgar tepede hafif hafif esiyordu. Keloğlan beyaz kağıttan topunu eşeği Karakaçan'ın sırtındaki sepete atmak istiyordu. Ama rüzgar kağıt topu her seferinde sepetten uzağa itti. Bir kez top sepetin kenarına çarptı ve yere sıçradı. Keloğlan topu yerden aldı. Dürüst ve azimli bir çocuktu, atmayı bırakmadı. "Bekle, Karakaçan, topu yine atacağım," dedi Keloğlan. Sonra rüzgarın durmasını bekledi. Rüzgar durunca topu yavaşça attı. Kağıt top sepetin içine düştü. Karakaçan başını salladı ve neşeyle anırdı. Keloğlan çok sevindi, çünkü kağıt topu sonunda sepete sokmuştu.
```

**Hakem bulguları (5):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Rüzgar tepede hafif hafif esiyordu"
   - Cümle 1: «Rüzgar tepede hafif hafif esiyordu.»
   - Açıklama: Rüzgar hafif deniyor ama topu her seferinde uzağa itiyor, üstelik bir kez top sepetin kenarına kadar gidiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "sırtındaki sepete atmak istiyordu"
   - Cümle 2: «Keloğlan beyaz kağıttan topunu eşeği Karakaçan'ın sırtındaki sepete atmak istiyordu.»
   - Açıklama: Kağıt topu eşeğin sepetine atmak kendi uydurduğu önemsiz bir oyun; sorun çocuğun önemseyeceği bir derde dayanmıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Dürüst ve azimli bir çocuktu"
   - Cümle 6: «Dürüst ve azimli bir çocuktu, atmayı bırakmadı.»
   - Açıklama: 'Azimli' soyut bir kavram, 3 yaşındaki çocuk bu kelimeyi bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Dürüst ve azimli bir çocuktu"
   - Cümle 6: «Dürüst ve azimli bir çocuktu, atmayı bırakmadı.»
   - Açıklama: Tohum özelliğinin dürüstlük kısmı yalnız etiket olarak sayılıyor, olayda işe yaramıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Dürüst ve azimli bir çocuktu"
   - Cümle 6: «Dürüst ve azimli bir çocuktu, atmayı bırakmadı.»
   - Açıklama: Dürüstlük olayda hiçbir işe yaramayan, karttan aktarılmış işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0063` birebir aynı, `@degisim: kilitli -> beyaz` (tutuyorsan), ardından `@onarim: 1a1a20e4557ca4c781aa5016eea3be706b8b843e`, sonra gövde.

### Hikâye 7: tohum keloglan-0064 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0064
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'önlük', fiil 'çözülmek', sıfat 'ışıltılı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: ip çözüldü ve rüzgar önlüğü uçurdu | aramayı bırakmadı ve önlüğü çalıda buldu
@tohum: keloglan-0064
@degisim: ışıltılı -> parlak
Rüzgar tepede sert esiyordu. Keloğlan'ın belinde mavi bir önlük vardı. Keloğlan onun cebine çiçek topluyordu. Birden ipi çözüldü ve rüzgar önlüğü uçurdu. Çiçekler de yere döküldü. Keloğlan önlüğü her yerde aradı ama göremedi. Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı. Sonra bir çalının dibinde parlak mavi bir şey gördü. Keloğlan bunu merak etti ve oraya yürüdü. Önlük çalıya takılmıştı. Keloğlan onu çalıdan aldı ve yine beline bağladı. Sonra çiçekleri yeniden cebine topladı. Keloğlan çok sevindi, çünkü önlüğü sonunda bulmuştu.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Keloğlan onun cebine çiçek topluyordu.»
   - Açıklama: Önlüğün uçması ancak 4. cümlede söyleniyor; ilk üç cümlede sorun yok.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Birden ipi çözüldü"
   - Cümle 4: «Birden ipi çözüldü ve rüzgar önlüğü uçurdu.»
   - Açıklama: Daha önce ip anılmadığı için 'ipi' ekinin neyin ipini gösterdiği belli değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Birden ipi çözüldü ve rüzgar önlüğü uçurdu"
   - Cümle 4: «Birden ipi çözüldü ve rüzgar önlüğü uçurdu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden ipi çözüldü"
   - Cümle 4: «Birden ipi çözüldü ve rüzgar önlüğü uçurdu.»
   - Açıklama: İpin neden çözüldüğü söylenmiyor; sorunun sebebi sebepsiz bir olaya dayanıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan dürüst ve azimli bir çocuktu"
   - Cümle 7: «Keloğlan dürüst ve azimli bir çocuktu, aramayı bırakmadı.»
   - Açıklama: Olayla ilgisiz 'dürüst' soyut özelliği ek olarak verilmiş; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0064` birebir aynı, `@degisim: ışıltılı -> parlak` (tutuyorsan), ardından `@onarim: 6d7b50159dceade38753fbd550f6cac780d9f332`, sonra gövde.

### Hikâye 8: tohum keloglan-0065 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0065
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'tuğla', fiil 'çekinmek', sıfat 'temkinli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: kırmızı elmalar yüksek bir dalda duruyordu | doğruyu söyleyip anasından yardım istedi
@tohum: keloglan-0065
@degisim: tuğla -> elma
Ormanda kuşlar ötüyordu. Keloğlan ile anası büyük bir ağacın altında elma topluyordu. Ama en kırmızı elmalar yüksek bir dalda duruyordu ve Keloğlan onlara yetişemedi. Keloğlan bunu anasına söylemekten önce çekindi. Sonra dürüst davrandı ve anasına doğruyu söyledi. "Anneciğim, elim dala yetişmiyor, yardım eder misin?" diye sordu Keloğlan. "Tabii ki," dedi anası. Anası temkinli davrandı ve dalı kırmadan yavaşça aşağı eğdi. Keloğlan kırmızı elmaları tek tek sepete koydu. Sepet kısa sürede doldu. Sonra ikisi ağacın gölgesinde oturdu ve elmaları mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "anasına söylemekten önce çekindi"
   - Cümle 4: «Keloğlan bunu anasına söylemekten önce çekindi.»
   - Açıklama: 'söylemekten önce çekindi' dilbilgisel değil; 'önce söylemekten çekindi' olmalı.
   - Açıklama: 'söylemekten önce' bozuk; 'söylemekten çekindi' ya da 'söylemeden önce' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan bunu anasına söylemekten önce çekindi"
   - Cümle 4: «Keloğlan bunu anasına söylemekten önce çekindi.»
   - Açıklama: Keloğlan'ın yetişemediğini söylemekten çekinmesi için hiçbir sebep yok; dürüstlük ayrıntısı olaydan çıkmıyor.
   - Açıklama: Saklanacak bir şey yokken çekinme ve 'doğruyu söyleme' sebepsiz kuruluyor ve olaya bir şey katmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra dürüst davrandı ve anasına doğruyu söyledi"
   - Cümle 5: «Sonra dürüst davrandı ve anasına doğruyu söyledi.»
   - Açıklama: Yardım istemek dürüstlük gerektiren bir durum değil; tohum özelliği zorlama ve işe yaramayan biçimde kullanılmış.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Anası temkinli davrandı"
   - Cümle 8: «Anası temkinli davrandı ve dalı kırmadan yavaşça aşağı eğdi.»
   - Açıklama: 'Temkinli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0065` birebir aynı, `@degisim: tuğla -> elma` (tutuyorsan), ardından `@onarim: 9e0acc3500003f9f14c205a6536f0875c377915c`, sonra gövde.

### Hikâye 9: tohum keloglan-0072 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0072
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'satranç', fiil 'sevmek', sıfat 'büyülü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: beyaz taşlardan biri kırılmıştı | köklerin altında beyaz yuvarlak bir taş buldu
@tohum: keloglan-0072
@degisim: büyülü -> yuvarlak
Rüzgar ağaçların arasında hafifçe esiyordu. Keloğlan ormanda yere çubukla bir satranç tahtası çizdi. Tahtaya küçük taşlar dizdi, ama beyaz taşlardan biri kırılmıştı. Oyun için yeni bir beyaz taş lazımdı. Keloğlan ağaçların dibine tek tek baktı ama yalnız koyu taşlar gördü. Sonra büyük bir ağacın kökleri arasındaki yaprakları eliyle kenara itti. Orada küçük, beyaz ve yuvarlak bir taş vardı. Keloğlan biraz sakardı ve taşı alırken yere düşürdü. Ama taş hiç kırılmadı, çok sağlamdı. Keloğlan bu taşı çok sevdi. Taşı silip tahtanın üstüne koydu. Keloğlan çok mutlu oldu, çünkü satranç taşları yine tamamdı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çubukla bir satranç tahtası"
   - Cümle 2: «Keloğlan ormanda yere çubukla bir satranç tahtası çizdi.»
   - Açıklama: 'Satranç tahtası' 3 yaşındaki bir çocuğun bilmediği bir kavram.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "beyaz taşlardan biri kırılmıştı"
   - Cümle 3: «Tahtaya küçük taşlar dizdi, ama beyaz taşlardan biri kırılmıştı.»
   - Açıklama: Taşın neden kırıldığı söylenmiyor.
   - Açıklama: Taşın neden kırıldığı hiç söylenmiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "taşı alırken yere düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve taşı alırken yere düşürdü.»
   - Açıklama: Tohumdaki sakarlık özelliği sorunun çözümüne hiçbir katkı yapmayan süs olarak kalıyor, karttaki özellik işe yarar biçimde kullanılmamış.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve taşı alırken yere düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve taşı alırken yere düşürdü.»
   - Açıklama: Tohumdaki sakarlık özelliği sorunun çözümünde işe yaramıyor, süs olarak ekleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "taşı alırken yere düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve taşı alırken yere düşürdü.»
   - Açıklama: Taşın düşürülmesi olaya hiçbir şey katmayan, yalnız özelliği göstermek için eklenmiş işlevsiz bir ayrıntı.
   - Açıklama: Taşın düşüp kırılmaması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0072` birebir aynı, `@degisim: büyülü -> yuvarlak` (tutuyorsan), ardından `@onarim: 4ebd0d79f88f66e356602b23a1a93377b30559fc`, sonra gövde.

### Hikâye 10: tohum keloglan-0073 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0073
- yer: dağ (Köyün yakınındaki tepe.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'flüt', fiil 'uyanmak', sıfat 'siyah'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: rüzgar yumağı yokuştan aşağı çalıya yuvarladı | dalla yumağı dışarı itip anasına getirdi
@tohum: keloglan-0073
@degisim: flüt -> dal
Tepede kuşlar ötüyordu. Keloğlan kısa bir uykudan uyandı, anası yanında siyah bir atkı örüyordu. Birden rüzgar esti ve anasının yumağı yokuştan aşağı yuvarlandı. Yumak dikenli bir çalının altında durdu. "Anneciğim, ben getiririm!" dedi Keloğlan. Keloğlan yerden uzun bir dal aldı ve çalıya yürüdü. Elini dikenlere değdirmedi, dalla yumağı dışarı itti. Keloğlan biraz sakardı ve yumağı anasının kucağına düşürdü. "Teşekkür ederim, Keloğlan," dedi anası ve gülümsedi. Sonra Keloğlan yumağı tuttu, anası da atkısını mutlu mutlu ördü.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve yumağı anasının kucağına düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve yumağı anasının kucağına düşürdü.»
   - Açıklama: Tohumdaki sakarlık özelliği çözüme katkı vermeyen süs olarak eklenmiş; özellik işe yarar biçimde kullanılmamış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve yumağı anasının kucağına düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve yumağı anasının kucağına düşürdü.»
   - Açıklama: Sakarlık olaydan çıkmıyor ve yumak çalıdan anasının kucağına sebepsizce ulaşıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yumağı anasının kucağına düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve yumağı anasının kucağına düşürdü.»
   - Açıklama: Yumak çalının altından birden ananın kucağına geçiyor; aradaki geri dönüş atlanıyor ve sakarlık olaya bağlanmıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Keloğlan biraz sakardı ve yumağı anasının kucağına düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı ve yumağı anasının kucağına düşürdü.»
   - Açıklama: Sakarlık bir aksilik olarak sunuluyor ama yumak tam yerine, ananın kucağına düşüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0073` birebir aynı, `@degisim: flüt -> dal` (tutuyorsan), ardından `@onarim: b1295dfff6dd050a3a823a38139004889881e028`, sonra gövde.

### Hikâye 11: tohum keloglan-0076 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0076
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'blok', fiil 'giymek', sıfat 'üzgün'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: tahta bloklardan yapılan kule her seferinde devrildi | büyük blokları alta koyup kuleyi sağlam yaptı
@tohum: keloglan-0076
Bir sabah Keloğlan annesine bir sürpriz yapmak istedi. Anası bahçedeyken tahta bloklardan ona bir kule yapmaya başladı. Ama kule her seferinde devrildi, çünkü en altta küçük bloklar vardı. Keloğlan yere oturdu ve üzgün bir yüzle bloklara baktı. Sonra büyük blokları alta, küçükleri üste koydu. Bu kez kule hiç devrilmedi. Keloğlan böylece büyük blokların altta sağlam durduğunu öğrendi. Keloğlan ayakkabılarını giydi ve annesini çağırmak için bahçeye çıktı. "Anneciğim, gel, sana bir sürprizim var!" dedi Keloğlan. Anası içeri geldi, kuleyi gördü ve güldü. "Ne güzel bir kule, teşekkür ederim!" dedi anası. Sonra ikisi bloklarla birlikte mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Anası bahçedeyken tahta bloklardan ona bir kule yapmaya başladı"
   - Cümle 2: «Anası bahçedeyken tahta bloklardan ona bir kule yapmaya başladı.»
   - Açıklama: Cümlede görünen tek özne Anası olduğu için kuleyi kimin yaptığı belli değil ve 'ona' zamiri belirsiz kalıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan ayakkabılarını giydi"
   - Cümle 8: «Keloğlan ayakkabılarını giydi ve annesini çağırmak için bahçeye çıktı.»
   - Açıklama: Ayakkabı giyme ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0076` birebir aynı, ardından `@onarim: 962d6d9495f34ee3bc1ac9a868d4d79ecd347294`, sonra gövde.

### Hikâye 12: tohum keloglan-0078 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0078
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'tomurcuk', fiil 'sürmek', sıfat 'berrak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: arkadaşının karnı acıkmıştı ama ekmeği yoktu | ekmeğini ikiye böldü ve onunla paylaştı
@tohum: keloglan-0078
@degisim: berrak -> mavi
Bir sabah Keloğlan ile Balkız tepede oturuyordu. Ağaçlarda küçük tomurcuklar vardı ve gökyüzü maviydi. Balkız'ın karnı acıkmıştı ama çantasında ekmek yoktu. Çantasında yalnız küçük bir kavanoz bal vardı. Keloğlan'ın çantasında ise bir ekmek vardı. "Balkız, bu ekmeği seninle paylaşayım mı?" diye sordu Keloğlan. "Olur, ben de balımı seninle paylaşırım," dedi Balkız. Keloğlan ekmeği iki eşit parçaya böldü. Balkız kavanozu açtı ve kaşıkla kendi parçasına biraz bal sürdü. İkisi ekmeklerini yan yana oturup yedi. "Teşekkürler, Balkız, paylaşmanın güzel olduğunu bugün öğrendim!" dedi Keloğlan.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ağaçlarda küçük tomurcuklar vardı"
   - Cümle 2: «Ağaçlarda küçük tomurcuklar vardı ve gökyüzü maviydi.»
   - Açıklama: 'Tomurcuk' 3 yaşındaki bir çocuğun büyük olasılıkla bilmediği bir kelime.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Ağaçlarda küçük tomurcuklar vardı"
   - Cümle 2: «Ağaçlarda küçük tomurcuklar vardı ve gökyüzü maviydi.»
   - Açıklama: Kartın yasaklar bölümündeki 'Tomurcuk' adı hikayede geçiyor.
   - Açıklama: Kartın 'yasaklar' bölümündeki 'Tomurcuk' adı hikayede geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ben de balımı seninle paylaşırım"
   - Cümle 7: «"Olur, ben de balımı seninle paylaşırım," dedi Balkız.»
   - Açıklama: Balkız balını paylaşacağını söylüyor ama balı yalnız kendi parçasına sürüyor; kurulan bal kullanılmıyor.
4. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: ""Teşekkürler, Balkız, paylaşmanın güzel olduğunu bugün öğrendim!" dedi Keloğlan"
   - Cümle 11: «"Teşekkürler, Balkız, paylaşmanın güzel olduğunu bugün öğrendim!" dedi Keloğlan.»
   - Açıklama: Ekmeği paylaşan Keloğlan olduğu halde teşekkür eden ve paylaşmayı öğrendiğini söyleyen de o; replik yanlış kişiye verilmiş.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Teşekkürler, Balkız, paylaşmanın güzel"
   - Cümle 11: «"Teşekkürler, Balkız, paylaşmanın güzel olduğunu bugün öğrendim!" dedi Keloğlan.»
   - Açıklama: Paylaşan Keloğlan olduğu halde Balkız'a teşekkür ediyor ve paylaşmayı yeni öğrendiğini söylüyor; bu olayla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0078` birebir aynı, `@degisim: berrak -> mavi` (tutuyorsan), ardından `@onarim: 3af65c5efc6507708d6402730b1dafdc40403c6b`, sonra gövde.
