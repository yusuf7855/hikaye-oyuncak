# Editör görevi (onarım): Keloğlan, onarım partisi 17

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar17.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar17.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0022 (deneme 5 -> 6)

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
@plan: kese uzun otların arasında görünmüyordu | yardım isteyip otları ayırdı ve keseyi buldu
@tohum: keloglan-0022
@degisim: gıdıklamak -> ayırmak
Ormanda kıvrımlı bir yolda Keloğlan hazine arama oyunu oynuyordu. Bilgecan Dede hazine olarak küçük bir keseyi otların arasına saklamıştı. Otlar çok uzundu ve Keloğlan keseyi hiç göremiyordu. "Dede, hazine hangi tarafta?" diye sordu Keloğlan. "Büyük ağacın yanına bak," dedi Bilgecan Dede. Keloğlan büyük ağacın yanına gitti. Orada otları bir sopayla ayırdı. Ama biraz sakardı ve sopa elinden otlara düştü. Sopayı alırken otların dibinde kahverengi keseyi gördü. İçinde üç tane ceviz vardı. Bilgecan Dede gülümsedi ve başını salladı. "Gel, cevizleri birlikte yiyelim, Dede!" dedi Keloğlan.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir keseyi otların"
   - Cümle 2: «Bilgecan Dede hazine olarak küçük bir keseyi otların arasına saklamıştı.»
   - Açıklama: 'Kese' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama biraz sakardı ve"
   - Cümle 8: «Ama biraz sakardı ve sopa elinden otlara düştü.»
   - Açıklama: 'Sakar' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği soyut bir özellik kelimesidir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sopa elinden otlara düştü"
   - Cümle 8: «Ama biraz sakardı ve sopa elinden otlara düştü.»
   - Açıklama: Kese, figürün çabasıyla değil sopanın kazayla düşmesiyle sebepsizce bulunuyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sopayı alırken otların dibinde kahverengi keseyi gördü"
   - Cümle 9: «Sopayı alırken otların dibinde kahverengi keseyi gördü.»
   - Açıklama: Kese Keloğlan'ın çabasıyla değil, sopayı düşürme kazasıyla sebepsizce bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0022` birebir aynı, `@degisim: gıdıklamak -> ayırmak` (tutuyorsan), ardından `@onarim: 9cca0f5199663f0d3ea288ec2a493a4f7ce01604`, sonra gövde.

### Hikâye 2: tohum keloglan-0023 (deneme 5 -> 6)

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
@degisim: alet -> sepet
Evin mutfağında Keloğlan ile Balkız çorba oyunu oynuyordu. Keloğlan çorbayı yapacaktı ve Balkız'ı eski masaya oturttu. Ama masanın bir ayağı kısaydı ve masa sallanıyordu. "Böyle yemek yiyemem, Keloğlan," dedi Balkız gülerek. Keloğlan masa için küçük bir tahta aradı. Odun sepetini kaldırdı. Keloğlan biraz sakardı ve sepet elinden düştü. Odunların arasında küçük düz bir tahta vardı. Tahtayı kısa ayağın altına koydu ve odunları sepete topladı. Masa artık hiç sallanmadı. "Buyur, sıcak çorban hazır," dedi Keloğlan. Balkız boş tabaktan çorba içer gibi yaptı ve güldü. Keloğlan bundan sonra oyuna başlamadan önce masanın ayaklarına bakardı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sepet elinden düştü"
   - Cümle 7: «Keloğlan biraz sakardı ve sepet elinden düştü.»
   - Açıklama: Sepetin düşmesi olaya hiçbir şey katmıyor ve tahta rastlantıyla, sebepsizce beliriyor.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "masanın ayaklarına bakardı"
   - Cümle 13: «Keloğlan bundan sonra oyuna başlamadan önce masanın ayaklarına bakardı.»
   - Açıklama: Anlatım son cümlede -dı'lı geçmişten -ardı biçimine kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0023` birebir aynı, `@degisim: alet -> sepet` (tutuyorsan), ardından `@onarim: 8933f6deb00ec66da47e835da781211cbc95299c`, sonra gövde.

### Hikâye 3: tohum keloglan-0025 (deneme 5 -> 6)

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
@plan: tepeden ıslık sesi geldi ama ıslık çalan yoktu | otların altında sesi çıkaran içi boş bir dal buldu
@tohum: keloglan-0025
Keloğlan tepede güzel sarı yapraklar topluyordu. Birden rüzgar esti ve ince bir ıslık sesi duyuldu. Ama tepede ıslık çalan kimse yoktu. Keloğlan çok heyecanlandı ve bu sesi merak etti. Sesin geldiği yere doğru yürüdü. Ses yerden, kuru otların altından geliyordu. Keloğlan sakar olduğu için yaprakları otların üstüne düşürdü. Yaprakları toplamak için otları eliyle ayırınca küçük bir dal buldu. Dalın içi boştu ve ucunda bir delik vardı. Keloğlan deliği parmağıyla kapattı ve ıslık kesildi. Parmağını çekince ıslık yeniden başladı. Ses, dalın içinden geçen rüzgardan çıkıyordu. Keloğlan dalı rüzgara doğru tuttu ve ıslığı mutlu mutlu dinledi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan sakar olduğu için yaprakları otların üstüne düşürdü"
   - Cümle 7: «Keloğlan sakar olduğu için yaprakları otların üstüne düşürdü.»
   - Açıklama: Dal, sesi araştırmanın sonucu olarak değil sebepsiz bir kazayla bulunuyor; çözüm tesadüfle geliyor.
   - Açıklama: Dal, yaprakların sebepsizce düşürülmesiyle rastlantı sonucu bulunuyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yaprakları toplamak için otları eliyle ayırınca"
   - Cümle 8: «Yaprakları toplamak için otları eliyle ayırınca küçük bir dal buldu.»
   - Açıklama: Dal sesi aramakla değil yaprakları düşürme kazasıyla tesadüfen bulunuyor, çözüm sebebe doğrudan yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0025` birebir aynı, ardından `@onarim: 21f19df2a99a612b6ee75b135a307ca76be23ae4`, sonra gövde.

### Hikâye 4: tohum keloglan-0027 (deneme 5 -> 6)

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
Keloğlan anasıyla ormanda çilek topluyordu. İkisi de çilekleri yemek için sabırsızdı. Keloğlan dolu sepeti hemen kaldırdı, ama biraz sakardı ve sepet elinden düştü. Bütün çilekler otlara döküldü. Keloğlan anasına üzgün üzgün baktı. "Özür dilerim, anne, sepeti düşürdüm," dedi Keloğlan. "Üzülme, gel birlikte toplayalım," dedi anası. Keloğlan çilekleri otlardan tek tek topladı. Sonra onları sepette güzelce düzenledi. Bu kez sepeti iki eliyle sıkıca tuttu. Anası gülümsedi ve onun başını okşadı. "Teşekkürler, anneciğim, çilekleri birlikte yiyelim!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "çilekleri yemek için sabırsızdı"
   - Cümle 2: «İkisi de çilekleri yemek için sabırsızdı.»
   - Açıklama: 'Sabırsız' soyut bir kavram.
   - Açıklama: 'Sabırsız' soyut bir kelime ve 3 yaşındaki çocuk için zor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama biraz sakardı ve"
   - Cümle 3: «Keloğlan dolu sepeti hemen kaldırdı, ama biraz sakardı ve sepet elinden düştü.»
   - Açıklama: 'Sakar' 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0027` birebir aynı, `@degisim: gümüş -> çilek` (tutuyorsan), ardından `@onarim: 3e1a47f8ee82c61404e479de3fdff221a7fdd831`, sonra gövde.

### Hikâye 5: tohum keloglan-0031 (deneme 4 -> 5)

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
Keloğlan şatonun bahçesinde ilk kez boyayla resim yapmayı denedi. Karakaçan resim çantasını sırtında taşımıştı. Ama kağıda iri bir boya damlası düştü ve kağıt kirlendi. "Ah, resmim bozuldu!" dedi Keloğlan. Keloğlan fırçaya dikkatle baktı. Fırça boyayla doluydu. Fırçayı kabın kenarına hafifçe sildi. Böylece boyayı az almayı öğrendi. Sonra kirli kağıdı bir yana koydu. Temiz bir kağıda şatonun yüksek kapısını boyadı. Bu kez kağıda hiç damla düşmedi. Karakaçan başını salladı. "Karakaçan, bak, ilk resmim ne güzel oldu!" dedi Keloğlan.
```

**Hakem bulguları (3):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "resim çantasını sırtında taşımıştı"
   - Cümle 2: «Karakaçan resim çantasını sırtında taşımıştı.»
   - Açıklama: Anlatım -mıştı'lı geçmişe kayıyor ve çantayı artık taşımıyormuş gibi okunuyor; 'taşıyordu' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Karakaçan resim çantasını sırtında taşımıştı"
   - Cümle 2: «Karakaçan resim çantasını sırtında taşımıştı.»
   - Açıklama: Resim çantası işe yarayacakmış gibi kuruluyor ama hikayede hiç kullanılmıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Temiz bir kağıda şatonun yüksek kapısını boyadı"
   - Cümle 10: «Temiz bir kağıda şatonun yüksek kapısını boyadı.»
   - Açıklama: Kağıda kapının resmi yapılır; 'kapısını boyadı' kapının kendisini boyamak anlamına geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0031` birebir aynı, `@degisim: işaretlemek -> boyamak` (tutuyorsan), ardından `@onarim: 0cbd65742f76f27c7a1feea5983984f69016328c`, sonra gövde.

### Hikâye 6: tohum keloglan-0033 (deneme 4 -> 5)

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
Keloğlan benekli eldivenleriyle ormanda odun topluyordu. Eşeği Karakaçan odunları sırtında taşıyordu. Birden Karakaçan durdu ve yürümedi, çünkü çok acıkmıştı. Ama büyük ağaçların altında hiç ot yoktu. "Bekle, Karakaçan, çantamda havuç var," dedi Keloğlan. Hemen çantasını açtı ve havuçları çıkardı. Keloğlan biraz sakardı ve havuçlar kalın eldivenlerinden kayıp düştü. Eldivenlerini çıkardı ve havuçları yerden topladı. Sonra onları Karakaçan'a tek tek verdi. Eşek hepsini yedi ve mutlu mutlu kuyruğunu oynattı. "Karnın doydu mu, Karakaçan?" diye sordu Keloğlan. Karakaçan başını iki kez salladı. Keloğlan çok sevindi, çünkü eşeği artık aç değildi.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "havuçlar kalın eldivenlerinden kayıp düştü"
   - Cümle 7: «Keloğlan biraz sakardı ve havuçlar kalın eldivenlerinden kayıp düştü.»
   - Açıklama: Açlık sorununa ek olarak havuçların düşmesiyle ikinci bir sorun açılıyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "havuçlar kalın eldivenlerinden kayıp düştü"
   - Cümle 7: «Keloğlan biraz sakardı ve havuçlar kalın eldivenlerinden kayıp düştü.»
   - Açıklama: Çözüm havuçların düşüp eldivenlerin çıkarılıp yeniden toplanmasıyla ikiden fazla adıma uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0033` birebir aynı, `@degisim: puantiyeli -> benekli` (tutuyorsan), ardından `@onarim: 0c586bbc2c4f33bc3171c4e24fc89b751520f759`, sonra gövde.

### Hikâye 7: tohum keloglan-0034 (deneme 4 -> 5)

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
Tepede serin bir rüzgar esiyordu. Keloğlan ile Balkız tekerlekli sepeti tepeye çekiyordu. Sepet bir taşa çarptı ve Balkız'ın keki yere düşüp ezildi. Balkız yerdeki keke üzgün üzgün baktı. Keloğlan'ın kremalı keki ise sepette duruyordu. Keloğlan kekini Balkız ile paylaşmak istedi. Keki yavaşça ikiye böldü. Sonra büyük parçayı Balkız'a verdi. İkisi tepede çimenlere oturdu ve parçalarını yedi. Keloğlan biraz sakardı ve kremayı burnuna bulaştırdı. Balkız ona bakıp güldü. Keloğlan çok mutluydu, çünkü kekini arkadaşıyla paylaşmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve kremayı burnuna bulaştırdı"
   - Cümle 10: «Keloğlan biraz sakardı ve kremayı burnuna bulaştırdı.»
   - Açıklama: Tohumdaki sakarlık özelliği sorun çözüldükten sonra süs olarak ekleniyor, işe yarar biçimde kullanılmıyor.
   - Açıklama: Sakarlık kartın güvenli kullanım satırındaki gibi düşürme ya da karıştırma olarak değil, soruna katkısı olmayan bir süs olarak kullanılmış.
2. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "Balkız ona bakıp güldü"
   - Cümle 11: «Balkız ona bakıp güldü.»
   - Açıklama: Balkız'ın Keloğlan'ın sakarlığına gülmesi alay olarak örnek alınabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0034` birebir aynı, `@degisim: güvenmek -> bölmek` (tutuyorsan), ardından `@onarim: 604e62327467d8ccb192e777aa9bb2f9b5993323`, sonra gövde.

### Hikâye 8: tohum keloglan-0040 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0040
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'mermer', fiil 'savurmak', sıfat 'süslü'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: ikisi de ipi aynı anda çekti | sırayla oynamayı söyledi ve önce arkadaşına verdi
@tohum: keloglan-0040
@degisim: mermer -> taş
Keloğlan ile Balkız şatonun bahçesinde taş bir yolda oynuyordu. Ellerinde tek bir süslü topaç vardı. İkisi de ipi aynı anda çekti ve ip karmakarışık oldu. "Balkız, sırayla oynayalım, önce sen çevir," dedi Keloğlan. Keloğlan ipi çözdü ve topacı Balkız'a verdi. Balkız ipi sardı ve topacı yere savurdu. Topaç taşın üstünde uzun uzun döndü. Sıra Keloğlan'a geldi. Keloğlan biraz sakardı ve topacı önce elinden düşürdü. Sonra topacı yerden aldı, ipi sardı ve yere attı. Topaç da güzelce döndü. İkisi de güldü. "Sırayla oynamak çok eğlenceli, Balkız!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve"
   - Cümle 9: «Keloğlan biraz sakardı ve topacı önce elinden düşürdü.»
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki çocuk bilmez.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "topacı önce elinden düşürdü"
   - Cümle 9: «Keloğlan biraz sakardı ve topacı önce elinden düşürdü.»
   - Açıklama: Topacın düşmesi hiçbir sonuca bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0040` birebir aynı, `@degisim: mermer -> taş` (tutuyorsan), ardından `@onarim: 4e441bc05d104ed4d9d33623991f523189cf621e`, sonra gövde.

### Hikâye 9: tohum keloglan-0042 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0042
- yer: dağ (Köyün yakınındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yağmurluk', fiil 'boyamak', sıfat 'yemyeşil'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: resmi boyamak için yeşil boya bitmişti | dededen yardım isteyip sarı ile maviyi karıştırdı
@tohum: keloglan-0042
@degisim: yağmurluk -> fırça
Keloğlan tepede resim yapma oyunu oynuyordu. Bilgecan Dede de yanına oturmuş, onu izliyordu. Keloğlan kağıttaki tepeyi boyamak istedi ama yeşil boyası bitmişti. Elinde yalnız sarı ile mavi boya vardı. "Dede, yeşil boyam bitti, ne yapayım?" diye sordu Keloğlan. "Sarı ile maviyi karıştır, yeşil olur," dedi Bilgecan Dede. Keloğlan biraz sakardı ve sarı boyayı birden mavi boyanın içine döktü. Sonra fırçasıyla iki rengi karıştırdı. Mavi renk yavaş yavaş yeşile döndü. Keloğlan resimdeki tepeyi yemyeşil boyadı. Bilgecan Dede resmi görünce ellerini çırptı. Keloğlan da mutlu mutlu yeni bir resme başladı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sarı boyayı birden mavi boyanın içine döktü"
   - Cümle 7: «Keloğlan biraz sakardı ve sarı boyayı birden mavi boyanın içine döktü.»
   - Açıklama: Sakarlıkla yapılan kaza sebepsizce istenen çözümü getiriyor; sakarlık ayrıntısı olayda kusur yaratmıyor ve işlevsiz kalıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan biraz sakardı ve sarı boyayı birden mavi boyanın içine döktü"
   - Cümle 7: «Keloğlan biraz sakardı ve sarı boyayı birden mavi boyanın içine döktü.»
   - Açıklama: Sakarlıkla boyanın dökülmesi bir aksilik gibi kuruluyor ama hiçbir sonucu olmuyor, işlevsiz bir ayrıntı kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0042` birebir aynı, `@degisim: yağmurluk -> fırça` (tutuyorsan), ardından `@onarim: 5f80be6d2ad90708608e582e6d1ee4978b563496`, sonra gövde.

### Hikâye 10: tohum keloglan-0043 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0043
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'yelpaze', fiil 'karşılaşmak', sıfat 'küçücük'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: annesi küçücük yelpazesini yolda düşürmüştü | annesinin geldiği yola bakıp yelpazeyi geri verdi
@tohum: keloglan-0043
Keloğlan ormandaki yolda anasıyla karşılaştı. Anası üzgündü, çünkü küçücük yelpazesini yolda düşürmüştü. "Hava çok sıcak," dedi anası. "Anneciğim, ben onu senin için bulurum," dedi Keloğlan. Keloğlan anasının geldiği yoldan geri gitti ve yere dikkatle baktı. Sonunda büyük bir ağacın altında yelpazeyi buldu. Keloğlan dürüst bir çocuktu ve yelpazeyi hemen anasına götürdü. Anası yelpazeyi salladı ve önce Keloğlan'ı, sonra kendini serinletti. "Teşekkür ederim, Keloğlan, sen bana çok yardım ettin!" dedi anası.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "anasının geldiği yoldan geri gitti"
   - Cümle 5: «Keloğlan anasının geldiği yoldan geri gitti ve yere dikkatle baktı.»
   - Açıklama: Keloğlan o yoldan gelmediği için 'geri gitti' yanlış; 'o yoldan yürüdü' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 7: «Keloğlan dürüst bir çocuktu ve yelpazeyi hemen anasına götürdü.»
   - Açıklama: Yelpaze zaten anasının olduğundan dürüstlük ayrıntısı olayda işlevsiz kalıyor.
   - Açıklama: Dürüstlük ayrıntısı işlevsiz; annesinin yelpazesini geri vermek dürüstlük sınavı değil ve olayda bir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0043` birebir aynı, ardından `@onarim: 16d030e3cf58f732f0dd78467ad960295748e925`, sonra gövde.

### Hikâye 11: tohum keloglan-0045 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0045
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'boya', fiil 'duymak', sıfat 'hazırlıklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: boya kabını düşürdü ve boya yere döküldü | dededen özür diledi ve evi birlikte boyadılar
@tohum: keloglan-0045
@degisim: hazırlıklı -> kırmızı
Ormanda Bilgecan Dede kuşlar için tahta bir ev boyuyordu. Keloğlan ona çantasında iki kap kırmızı boya getirmişti. Keloğlan bir kabı tutarak dedeye yardım ediyordu. Ama Keloğlan biraz sakardı, kabı düşürdü ve boya yere döküldü. Bilgecan Dede sesi duydu ve arkasına döndü. Keloğlan yerdeki kırmızı lekeye baktı ve başını eğdi. "Özür dilerim, dede, boyayı ben düşürdüm," dedi Keloğlan. "Üzülme, Keloğlan," dedi Bilgecan Dede ve gülümsedi. Keloğlan çantasından ikinci kabı çıkardı ve onu iki eliyle sıkıca tuttu. İkisi evi birlikte boyadı ve bitirdi. Keloğlan çok sevindi, çünkü dede ona kızmamıştı ve kuşların evi hazırdı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Keloğlan bir kabı tutarak dedeye yardım ediyordu.»
   - Açıklama: Sorun (boyanın dökülmesi) ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0045` birebir aynı, `@degisim: hazırlıklı -> kırmızı` (tutuyorsan), ardından `@onarim: 036ad49eb39177632785f17f886514a61b048b97`, sonra gövde.

### Hikâye 12: tohum keloglan-0047 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Balkız
@tohum: keloglan-0047
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kiraz', fiil 'koklamak', sıfat 'meraklı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Balkız
@plan: bahçedeki tatlı kokunun nereden geldiğini bilmiyordu | gözlerini kapatıp kokladı ve kiraz ağacını buldu
@tohum: keloglan-0047
@degisim: meraklı -> tatlı
Şatonun büyük bahçesinde tatlı bir koku vardı. Keloğlan kokunun nereden geldiğini bulmak istedi. Ama bahçede bir sürü ağaç ve çiçek vardı. "Balkız, gözlerimi kapatıp kokuyu bulacağım," dedi Keloğlan. Keloğlan dürüsttü ve gözlerini kapalı tuttu. Sonra yavaşça döndü ve havayı kokladı. Sonunda eliyle kapının yanını gösterdi. "Koku oradan geliyor, Balkız!" dedi Keloğlan. Keloğlan gözlerini açtı ve ikisi o tarafa yürüdü. Kapının yanında beyaz çiçekli bir kiraz ağacı vardı. "İşte, kiraz çiçekleri!" dedi Balkız sevinçle. Keloğlan çok sevindi, çünkü kokuyu yalnız burnuyla bulmuştu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüsttü ve gözlerini kapalı tuttu"
   - Cümle 5: «Keloğlan dürüsttü ve gözlerini kapalı tuttu.»
   - Açıklama: Dürüstlük özelliği olaya katkı vermeden zorla eklenmiş işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0047` birebir aynı, `@degisim: meraklı -> tatlı` (tutuyorsan), ardından `@onarim: cc61988ee545551f26a20ab6db01eb1980ca881f`, sonra gövde.
