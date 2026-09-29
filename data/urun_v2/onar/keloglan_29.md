# Editör görevi (onarım): Keloğlan, onarım partisi 29

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar29.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar29.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0064 (deneme 5 -> 6)

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
@plan: rüzgar ipi çekti ve önlük uçtu | aramayı bırakmadı ve önlüğü çalıda buldu
@tohum: keloglan-0064
@degisim: ışıltılı -> parlak
Rüzgar tepede sert esiyordu. Keloğlan'ın belinde mavi bir önlük vardı, cebine çiçek topluyordu. Birden rüzgar önlüğü çekti, ipi çözüldü ve önlük uçtu. Çiçekler de yere döküldü. Keloğlan etrafa baktı ama önlüğü göremedi. Keloğlan dürüst bir çocuktu ve işini hiç bırakmazdı. Bu yüzden aramaya devam etti. Sonra bir çalının dibinde parlak mavi bir şey gördü. Keloğlan bunu merak etti ve oraya yürüdü. Önlük çalıya takılmıştı. Keloğlan önlüğü aldı ve ipini beline sıkıca bağladı. Sonra çiçekleri yeniden cebine topladı. Keloğlan çok sevindi, çünkü önlüğü sonunda bulmuştu.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "cebine çiçek topluyordu"
   - Cümle 2: «Keloğlan'ın belinde mavi bir önlük vardı, cebine çiçek topluyordu.»
   - Açıklama: 'Cebine' kelimesinin önlüğün mü Keloğlan'ın mı cebi olduğu belli değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu ve işini hiç bırakmazdı"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini hiç bırakmazdı.»
   - Açıklama: 'Dürüst' kelimesi işini bırakmamakla (sebat) ilgili değil, yanlış anlamda kullanılmış.
   - Açıklama: 'Dürüst' yanlış anlamda kullanılmış; işini bırakmamak dürüstlük değil sebatlılıktır.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 6: «Keloğlan dürüst bir çocuktu ve işini hiç bırakmazdı.»
   - Açıklama: Dürüstlük olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
   - Açıklama: Dürüstlük olayla ilgisiz bir ayrıntı ve aramaya devam etmenin sebebi gibi sunuluyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan bunu merak etti"
   - Cümle 9: «Keloğlan bunu merak etti ve oraya yürüdü.»
   - Açıklama: Tohumdaki özellik dürüst/azimli; merak ikinci bir özellik olarak ekleniyor, bu kartın özellik kullanımına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0064` birebir aynı, `@degisim: ışıltılı -> parlak` (tutuyorsan), ardından `@onarim: 2f3ed8bf09f0f9c3e5509c87b7ed8b2b25c91630`, sonra gövde.

### Hikâye 2: tohum keloglan-0065 (deneme 5 -> 6)

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
Ormanda kuşlar ötüyordu ve Keloğlan ile anası elma topluyordu. "En kırmızı elmaları ben toplarım," dedi Keloğlan. Ama o elmalar yüksek bir dalda duruyordu ve Keloğlan onlara yetişemedi. Keloğlan bunu anasına söylemekten çekindi. Ama sonra dürüst davrandı. "Anneciğim, dal çok yüksek, yardım eder misin?" diye sordu Keloğlan. "Tabii ki," dedi anası. Anası temkinliydi ve dalı yavaşça aşağı eğdi. Keloğlan kırmızı elmaları tek tek sepete koydu. Sepet kısa sürede doldu. Sonra ikisi bir ağacın gölgesinde oturdu ve elmaları mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bunu anasına söylemekten çekindi"
   - Cümle 4: «Keloğlan bunu anasına söylemekten çekindi.»
   - Açıklama: 'çekinmek' soyut bir duygu kelimesi, 3 yaşındaki çocuk için zor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "anasına söylemekten çekindi"
   - Cümle 4: «Keloğlan bunu anasına söylemekten çekindi.»
   - Açıklama: 'Çekinmek' soyut bir duygu kelimesi, küçük çocuk için zor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Anası temkinliydi ve"
   - Cümle 8: «Anası temkinliydi ve dalı yavaşça aşağı eğdi.»
   - Açıklama: 'temkinli' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Temkinli' soyut ve 3 yaşındaki çocuğun bilmediği bir kelime; figürün özellik kelimesi de değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0065` birebir aynı, `@degisim: tuğla -> elma` (tutuyorsan), ardından `@onarim: 1f532b88bab43bd5b200fe9d6ad4823c401b1bbc`, sonra gövde.

### Hikâye 3: tohum keloglan-0072 (deneme 5 -> 6)

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
@plan: düşen beyaz taşlardan biri kırıldı | köklerin altında beyaz yuvarlak bir taş buldu
@tohum: keloglan-0072
@degisim: büyülü -> yuvarlak
Rüzgar ağaçların arasında hafifçe esiyordu. Keloğlan ormanda yere çubukla kareler çizdi ve satranç taşlarını dizdi. Ama biraz sakardı, beyaz bir taşı düşürdü ve taş ikiye kırıldı. Oyun için yeni bir beyaz taş lazımdı. Keloğlan ağaçların dibine tek tek baktı ama yalnız koyu taşlar gördü. Sonra büyük bir ağacın kökleri arasındaki yaprakları eliyle kenara itti. Orada küçük, beyaz ve yuvarlak bir taş vardı. Keloğlan bu taşı çok sevdi. Taşı silip karelerin üstüne koydu. Keloğlan çok mutlu oldu, çünkü satranç taşları yine tamamdı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "beyaz bir taşı düşürdü ve taş ikiye kırıldı"
   - Cümle 3: «Ama biraz sakardı, beyaz bir taşı düşürdü ve taş ikiye kırıldı.»
   - Açıklama: Yere düşen bir satranç taşının ikiye kırılması akla yatkın bir sebep değil.
   - Açıklama: Yere, toprağa düşen bir satranç taşının ikiye kırılması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0072` birebir aynı, `@degisim: büyülü -> yuvarlak` (tutuyorsan), ardından `@onarim: 2d3c75569c4074a5cc30620884e726f61320b438`, sonra gövde.

### Hikâye 4: tohum keloglan-0073 (deneme 5 -> 6)

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
Tepede kuşlar ötüyordu. Keloğlan kısa bir uykudan uyandı, anası yanında siyah bir atkı örüyordu. Birden rüzgar esti ve anasının yumağı yokuştan aşağı yuvarlandı. Yumak dikenli bir çalının altında durdu. "Anneciğim, ben getiririm!" dedi Keloğlan. Keloğlan yerden uzun bir dal aldı ve çalıya yürüdü. Elini dikenlere değdirmedi, dalla yumağı dışarı itti. Keloğlan biraz sakardı, bu yüzden yumağı iki eliyle tuttu ve anasına getirdi. "Teşekkür ederim, Keloğlan," dedi anası ve gülümsedi. Sonra Keloğlan yumağı tuttu, anası da atkısını mutlu mutlu ördü.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan kısa bir uykudan uyandı"
   - Cümle 2: «Keloğlan kısa bir uykudan uyandı, anası yanında siyah bir atkı örüyordu.»
   - Açıklama: Keloğlan'ın uykudan uyanması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı, bu yüzden yumağı iki eliyle tuttu"
   - Cümle 8: «Keloğlan biraz sakardı, bu yüzden yumağı iki eliyle tuttu ve anasına getirdi.»
   - Açıklama: Tohumdaki sakarlık özelliği kartın güvenli kullanım satırındaki gibi bir şeyi düşürmek ya da karıştırmak olarak işe yaramıyor, yalnız gerekçe olarak anılıyor.
   - Açıklama: Kartın güvenli özellik kullanımı satırı sakarlığı düşürmek ya da karıştırmak olarak gösterir; burada sakarlık işe yaramayan bir gerekçe olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0073` birebir aynı, `@degisim: flüt -> dal` (tutuyorsan), ardından `@onarim: 03ceca358fb380a60e2a6603639d04037d72522f`, sonra gövde.

### Hikâye 5: tohum keloglan-0078 (deneme 4 -> 5)

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
@degisim: tomurcuk -> çiçek
Bir sabah Keloğlan ile Balkız tepede oturuyordu. Ağaçlarda küçük çiçekler vardı ve gökyüzü berraktı. Balkız'ın karnı acıkmıştı ama çantasında ekmek yoktu. Çantasında yalnız küçük bir kavanoz bal vardı. Keloğlan'ın çantasında ise bir ekmek vardı. "Balkız, bu ekmeği seninle paylaşayım mı?" diye sordu Keloğlan. "Olur, ben de balımı seninle paylaşırım," dedi Balkız. Keloğlan ekmeği iki eşit parçaya böldü. Balkız kavanozu açtı ve iki parçaya da kaşıkla biraz bal sürdü. İkisi ekmeklerini yan yana oturup yedi. "Teşekkürler, Balkız, ekmeğin balla ne güzel olduğunu öğrendim!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve gökyüzü berraktı"
   - Cümle 2: «Ağaçlarda küçük çiçekler vardı ve gökyüzü berraktı.»
   - Açıklama: 'Berrak' kelimesi 3 yaşındaki bir çocuğun bildiği bir kelime değil.
   - Açıklama: 'Berrak' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "ekmeğin balla ne güzel olduğunu öğrendim"
   - Cümle 11: «"Teşekkürler, Balkız, ekmeğin balla ne güzel olduğunu öğrendim!" dedi Keloğlan.»
   - Açıklama: Tohumdaki öğrenme özelliği sorunu çözmüyor, yalnız son repliğe eklenmiş; kartın özellik alanındaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki öğrenme özelliği sorunu çözmekte işe yaramıyor, yalnız sona eklenmiş bir söz olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0078` birebir aynı, `@degisim: tomurcuk -> çiçek` (tutuyorsan), ardından `@onarim: d6e5a0bfb3c3ea971c5f61590832a51d6bc229f6`, sonra gövde.

### Hikâye 6: tohum keloglan-0079 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0079
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'eşarp', fiil 'beğenmek', sıfat 'kocaman'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: rüzgar annesinin eşarbını pencerenin önünden düşürdü | aramayı bırakmadı ve eşarbı sepette buldu
@tohum: keloglan-0079
Köy evinin içi sıcak ve aydınlıktı. Keloğlan'ın anası kocaman kırmızı eşarbını arıyordu. Rüzgar eşarbı pencerenin önünden bir yere düşürmüştü. Anası bu eşarbı çok beğeniyordu ve biraz üzüldü. "Anneciğim, ben sana yardım ederim," dedi Keloğlan. Önce pencerenin önünde yere baktı ama eşarp orada yoktu. "Bırak, sonra buluruz," dedi anası. Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı. Sonra pencerenin altındaki sepete baktı. Kırmızı eşarp sepetin içindeydi! Keloğlan eşarbı çıkarıp annesine verdi. Anası eşarbını boynuna sardı ve Keloğlan'a sarıldı. Keloğlan çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 8: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Aramayı bırakmamak dürüstlükle ilgili değil; 'dürüst' kelimesi yanlış anlamda kullanılmış.
   - Açıklama: 'Dürüst' aramayı bırakmamakla ilgili değil; kelime yanlış anlamda kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 8: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Özellik alanındaki dürüstlük aramayı sürdürmenin nedeni olarak yanlış kullanılmış; dürüstlüğün olayla ilgisi yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan dürüst bir çocuktu ve aramayı bırakmadı"
   - Cümle 8: «Ama Keloğlan dürüst bir çocuktu ve aramayı bırakmadı.»
   - Açıklama: Aramayı bırakmamanın sebebi olarak dürüstlük gösteriliyor, oysa dürüstlük azimle ilgisiz.
   - Açıklama: Dürüstlük aramayı sürdürmenin sebebi değil; olay bir öncekinden mantıkla çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0079` birebir aynı, ardından `@onarim: 53c2a348739a4d40fec30835968d7dfff9034131`, sonra gövde.

### Hikâye 7: tohum keloglan-0083 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0083
- yer: dağ (Köyün yakınındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'çöp', fiil 'çıkmak', sıfat 'rahat'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: taç yapmak istedi ama çiçekler hep koptu | arkadaşından yardım istedi ve çiçekleri yavaşça bağladı
@tohum: keloglan-0083
@degisim: çöp -> papatya
Keloğlan ile Balkız tepeye çıktı. Tepede bir sürü beyaz papatya vardı. Keloğlan papatyalardan taç yapmak istedi, ama sert çekince çiçekler koptu. Sonra Balkız'dan yardım istedi. Balkız ona çiçekleri yavaşça bağlamayı gösterdi. Keloğlan dikkatle baktı ve çiçekleri yavaşça bağlamayı öğrendi. Sonra papatyaları tek tek ekledi. Bu kez hiçbir çiçek kopmadı. Keloğlan'ın tacı çok güzel oldu. Keloğlan tacı Balkız'ın sarı saçlarına taktı. Balkız da ona hızlıca bir taç yaptı. Keloğlan ile Balkız çimenlere rahatça oturdu ve mutlu mutlu güldü.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çiçekleri yavaşça bağlamayı öğrendi"
   - Cümle 6: «Keloğlan dikkatle baktı ve çiçekleri yavaşça bağlamayı öğrendi.»
   - Açıklama: 'Çiçekleri yavaşça bağlamayı' bir önceki cümlede aynen geçiyor; gereksiz tekrar.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Keloğlan dikkatle baktı ve çiçekleri yavaşça bağlamayı öğrendi"
   - Cümle 6: «Keloğlan dikkatle baktı ve çiçekleri yavaşça bağlamayı öğrendi.»
   - Açıklama: 'Çiçekleri yavaşça bağlamayı' bir önceki cümlede geçmişti; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0083` birebir aynı, `@degisim: çöp -> papatya` (tutuyorsan), ardından `@onarim: 641d355372e34c3b178a306a89a82a3cde9fba91`, sonra gövde.

### Hikâye 8: tohum keloglan-0086 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0086
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Balkız
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'uçurtma', fiil 'sığmak', sıfat 'değişik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: sürpriz uçurtma çantaya sığmadı | uçurtmayı kalın bir ağacın arkasına sakladı
@tohum: keloglan-0086
Rüzgar ormanın ağaçları arasında hafifçe esiyordu. Keloğlan, Balkız'ın doğum günü için değişik bir uçurtma yapmıştı. Uçurtmayı Balkız gelmeden saklamak istedi ama uçurtma çantasına sığmadı. Keloğlan etrafına baktı ve büyük bir ağaç gördü. Uçurtmayı ağacın arkasına dikkatlice koydu. Ağacın gövdesi çok kalındı ve uçurtma hiç görünmedi. Biraz sonra Balkız geldi ve Keloğlan'ın yanına oturdu. Balkız, Keloğlan'ın ağaca baktığını gördü ve ne olduğunu sordu. Keloğlan dürüst bir çocuktu ve ona bir sürprizi olduğunu söyledi. Sonra uçurtmayı ağacın arkasından çıkarıp Balkız'a verdi. Balkız uçurtmayı görünce ellerini çırptı. İkisi uçurtmayı birlikte uçurdu. Keloğlan çok sevindi, çünkü sürprizi Balkız'ı mutlu etmişti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 9: «Keloğlan dürüst bir çocuktu ve ona bir sürprizi olduğunu söyledi.»
   - Açıklama: Tohumdaki dürüstlük özelliği sorunu çözmüyor; sorun uçurtmayı ağacın arkasına saklayarak çözülüyor, özellik süs olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0086` birebir aynı, ardından `@onarim: 552477cb8d520a4080eeacb49666e24765d5f5ba`, sonra gövde.

### Hikâye 9: tohum keloglan-0087 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0087
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'salata', fiil 'soğumak', sıfat 'dalgalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: ikisi aynı anda koyunca tabaktaki yüz bozuldu | sırayla koymayı istedi ve yüzü birlikte yaptılar
@tohum: keloglan-0087
Köy evinde sıcak bir çorba soğuyordu. Keloğlan ile anası salatadan komik bir yüz yapıyordu. Ama ikisi aynı anda parça koyunca sakar Keloğlan hepsini karıştırdı. Yüz bozuldu ve Keloğlan üzüldü. "Anne, sırayla koyalım mı?" diye sordu Keloğlan. "Olur, önce sen koy," dedi anası. Keloğlan iki salatalıkla gözleri yaptı. Sonra anası domates parçalarını dalgalı bir ağız gibi dizdi. Keloğlan da burun için ortaya bir zeytin koydu. Bu kez yüz hiç bozulmadı. Anası yüze baktı ve güldü. Çorba da artık soğumuştu. "Bak, anneciğim, yüz çok güzel oldu, hadi yiyelim!" dedi Keloğlan.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sıcak bir çorba soğuyordu"
   - Cümle 1: «Köy evinde sıcak bir çorba soğuyordu.»
   - Açıklama: Soğuyan çorba kuruluyor ama olaya hiçbir katkısı olmayan işlevsiz bir ayrıntı olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0087` birebir aynı, ardından `@onarim: 80968215c2bd06fe7d06c33b587cc7d2ff67cf76`, sonra gövde.

### Hikâye 10: tohum keloglan-0089 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Bilgecan Dede
@tohum: keloglan-0089
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: paylaşmak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'marul', fiil 'toplamak', sıfat 'eskimiş'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Bilgecan Dede
@plan: dedenin eskimiş torbası yırtıldı ve marullar döküldü | marulları toplayıp kendi torbasını dedeyle paylaştı
@tohum: keloglan-0089
Şatonun büyük bahçesi serin ve sessizdi. Keloğlan torbası elinde yürürken Bilgecan Dede'yi gördü ve ona el salladı. Birden dedenin eskimiş torbası yırtıldı ve marullar çimenlere döküldü. Keloğlan hemen koştu ve marulları topladı. Keloğlan biraz sakardı ve marulları elinden düşürmek istemedi. Bu yüzden torbasını hemen açtı. "Gel, Dede, torbamı seninle paylaşayım," dedi Keloğlan. Keloğlan marulları kendi torbasına koydu. Sonra torbanın bir ucunu kendisi, öbür ucunu dede tuttu. Birlikte bahçenin kapısına kadar yürüdüler. "Teşekkür ederim, Keloğlan, bana çok yardım ettin," dedi Bilgecan Dede. Keloğlan çok sevindi, çünkü torbasını dedeyle paylaşmıştı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan biraz sakardı ve marulları elinden düşürmek istemedi"
   - Cümle 5: «Keloğlan biraz sakardı ve marulları elinden düşürmek istemedi.»
   - Açıklama: Sorunu sakarlık yaratmıyor; özellik kartın güvenli kullanım satırındaki gibi işe yarar biçimde kullanılmıyor, yalnız anılıyor.
   - Açıklama: Güvenli özellik kullanımı satırına göre sakarlık bir şeyi düşürmek ya da karıştırmak olarak gösterilmeli; burada yalnız söylenmiş, işe yarar biçimde kullanılmamış.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Keloğlan marulları kendi torbasına koydu"
   - Cümle 8: «Keloğlan marulları kendi torbasına koydu.»
   - Açıklama: Keloğlan ardışık cümlelerde gereksiz yere tekrar tekrar özne olarak yazılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0089` birebir aynı, ardından `@onarim: e2efb6b4a3cfdb2aba9d5624ed43fc6857958d6e`, sonra gövde.

### Hikâye 11: tohum keloglan-0092 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0092
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'bayrak', fiil 'yatmak', sıfat 'şeffaf'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: ıslak dal demeti çok ağırdı ve onu kaldıramadı | ıslık çalıp eşeğinden yardım istedi
@tohum: keloglan-0092
@degisim: bayrak -> dal
Yağmur yeni dinmişti ve yapraklarda şeffaf su damlaları vardı. Keloğlan ormanda büyük bir demet dal toplamıştı. Ama ıslak dallar çok ağırdı ve Keloğlan demeti kaldıramadı. Eşeği Karakaçan biraz uzakta, bir ağacın altında yatıyordu. Keloğlan ıslık çaldı. Eşek hemen kalktı ve yanına geldi. "Karakaçan, bu dalları taşımama yardım eder misin?" diye sordu Keloğlan. Eşek başını salladı. Keloğlan dalları tek tek eşeğin sırtına koydu. Karakaçan yükü kolayca taşıdı. Keloğlan böylece ağır yük için yardım istemeyi öğrendi. Keloğlan ile Karakaçan dalları köye götürmek için yan yana, mutlu mutlu yürüdü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yapraklarda şeffaf su damlaları"
   - Cümle 1: «Yağmur yeni dinmişti ve yapraklarda şeffaf su damlaları vardı.»
   - Açıklama: 'Şeffaf' kelimesi 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki bir çocuk bilmez; 'parlak' ya da 'küçük' gibi basit bir kelime gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0092` birebir aynı, `@degisim: bayrak -> dal` (tutuyorsan), ardından `@onarim: 5e51ff365cedcb25c2b39a087de0f88e315db000`, sonra gövde.

### Hikâye 12: tohum keloglan-0097 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0097
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çim', fiil 'karıştırmak', sıfat 'yeni'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: acele edip çiçekleri bakmadan attı ve karıştırdı | doğruyu söyleyip özür diledi ve çiçekleri yeniden ayırdı
@tohum: keloglan-0097
Bir sabah Keloğlan ile anası ormanda çiçek topluyordu. Anası yeni bir buket için çimlere sarı ve mor yığınlar yapmıştı. Keloğlan acele etti, çiçeklerini bakmadan attı ve iki yığını karıştırdı. Anası yığınlara baktı ve şaşırdı. "Bu çiçekler neden karışık?" diye sordu anası. "Ben yaptım, anneciğim, özür dilerim," dedi Keloğlan. Sonra çimlere oturdu ve çiçekleri tek tek ayırdı. Anası gülümsedi ve Keloğlan'ın başını okşadı. "Dürüst davrandın, Keloğlan, teşekkür ederim," dedi anası. Sonra ikisi güzel bir buket bağladı. Keloğlan ile anası çiçek toplamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "iki yığını karıştırdı"
   - Cümle 3: «Keloğlan acele etti, çiçeklerini bakmadan attı ve iki yığını karıştırdı.»
   - Açıklama: Sarı ve mor çiçek yığınlarının karışması çocuğun önemseyeceği ciddi bir sorun değil, önemsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0097` birebir aynı, ardından `@onarim: f3b2b4aeee1c35a5eb027955d8a014f2a0af42de`, sonra gövde.
