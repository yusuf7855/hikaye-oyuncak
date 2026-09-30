# Editör görevi (onarım): Keloğlan, onarım partisi 48

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar48.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar48.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0183 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0183
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'mücevher', fiil 'kıpırdamak', sıfat 'huzurlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: top dedenin taş kutusunu devirdi ve taşlar döküldü | özür diledi ve taşları tek tek topladı
@tohum: keloglan-0183
@degisim: mücevher -> taş
Bir sabah Keloğlan ormanda top oynuyordu. Bilgecan Dede yakında oturmuş, kutusundaki parlak taşlara bakıyordu. Ama Keloğlan topa çok sert vurdu ve top dedenin kutusunu devirdi. Taşlar yerdeki yaprakların arasına döküldü. Keloğlan bir an hiç kıpırdamadı. Sonra dürüst davrandı ve dedenin yanına gitti. "Özür dilerim, Bilgecan Dede, topa ben vurdum," dedi Keloğlan. "Doğruyu söyledin, teşekkürler, Keloğlan," dedi Bilgecan Dede. Keloğlan yaprakların arasından taşları tek tek topladı. Bütün taşları yeniden kutuya koydu. Bilgecan Dede gülümsedi ve huzurlu oldu, çünkü hiçbir taş eksik değildi. Keloğlan bundan sonra topla dedenin kutusundan uzakta oynadı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gülümsedi ve huzurlu oldu"
   - Cümle 11: «Bilgecan Dede gülümsedi ve huzurlu oldu, çünkü hiçbir taş eksik değildi.»
   - Açıklama: 'Huzurlu' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
   - Açıklama: 'Huzurlu olmak' soyut ve çocuğa uygun olmayan bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0183` birebir aynı, `@degisim: mücevher -> taş` (tutuyorsan), ardından `@onarim: e45f97df68d515914c0228a08856d689f8129430`, sonra gövde.

### Hikâye 2: tohum keloglan-0184 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0184
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'portakal', fiil 'bozulmak', sıfat 'rüzgarlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: rüzgar hafif sepeti devirdi ve oyun bozuldu | portakalları sepete koyup sepeti ağır yaptı
@tohum: keloglan-0184
Bir sabah ormanda hava çok rüzgarlıydı. Keloğlan ile anası sırayla boş bir sepete kozalak atıyordu. Ama rüzgar hafif sepeti hep deviriyordu ve oyun bozuluyordu. "Şimdi kimin sırası, anne?" diye sordu Keloğlan. "Sıra sende, ama önce sepeti kaldır," dedi anası. Sakar Keloğlan sepeti kaldırırken anasının portakal torbasını düşürdü. Portakallar yere yuvarlandı. Sepet ağır olsun diye Keloğlan portakalları sepetin içine koydu. Rüzgar yine esti, ama ağır sepet bu kez devrilmedi. Keloğlan ile anası birbirine bakıp güldü. Keloğlan bir kozalak attı. Kozalak sepete girdi ve anası alkışladı. "Şimdi sıra sende, anneciğim, bu oyun çok eğlenceli!" dedi Keloğlan.
```

**Hakem bulguları (4):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "portakalları sepete koyup sepeti ağır yaptı"
   - Cümle 0 (plan satırı): «rüzgar hafif sepeti devirdi ve oyun bozuldu | portakalları sepete koyup sepeti ağır yaptı»
   - Açıklama: Gövdede portakallar sepete konmuyor, yere yuvarlanıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "anasının portakal torbasını düşürdü"
   - Cümle 6: «Sakar Keloğlan sepeti kaldırırken anasının portakal torbasını düşürdü.»
   - Açıklama: Sepet Keloğlan'ın bilinçli bir çözümüyle değil, sakarlıkla düşen torbayla tesadüfen ağırlaşıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "anasının portakal torbasını düşürdü"
   - Cümle 6: «Sakar Keloğlan sepeti kaldırırken anasının portakal torbasını düşürdü.»
   - Açıklama: Portakal torbası sebepsiz beliriyor ve çözümü tesadüfle getiriyor.
   - Açıklama: Portakal torbası daha önce kurulmadan sakarlık kazasıyla beliriyor ve çözümü sebepsizce getiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan sepeti kaldırırken anasının portakal torbasını düşürdü"
   - Cümle 6: «Sakar Keloğlan sepeti kaldırırken anasının portakal torbasını düşürdü.»
   - Açıklama: Sepeti ağırlaştıracak portakallar daha önce kurulmadan, sakarlıkla tesadüfen beliriyor ve çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0184` birebir aynı, ardından `@onarim: 7745274c26dcb8063b318bf192a36c5cd747c6b1`, sonra gövde.

### Hikâye 3: tohum keloglan-0185 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0185
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sırayla oynamak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'çimen', fiil 'ovuşturmak', sıfat 'keyifli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: ikisi aynı anda gözlerini kapadı ve oyun durdu | sırayla oynamayı söyledi ve yeni bir koku öğrendi
@tohum: keloglan-0185
Ormanda Keloğlan ile Balkız keyifli bir koku oyunu oynuyordu. Gözü kapalı olan, bir yaprağın kokusunu bulacaktı. Ama ikisi de aynı anda gözlerini kapadı ve kimse yaprak vermedi. "Balkız, sırayla oynayalım, önce sen yaprak ver," dedi Keloğlan. Keloğlan yeni kokular öğrenmek istiyordu. Balkız ona bir avuç çimen verdi. Keloğlan çimeni parmaklarıyla ovuşturdu ve kokladı, ama bilemedi. "Bu çimen," dedi Balkız. Sonra sıra Balkız'a geldi ve Keloğlan ona bir çam dalı verdi. "Bu çam!" dedi Balkız. Bir sonraki turda Keloğlan çimeni hemen bildi. Keloğlan çok sevindi, çünkü sırayla oynamak ona yeni bir koku öğretmişti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir yaprağın kokusunu bulacaktı"
   - Cümle 2: «Gözü kapalı olan, bir yaprağın kokusunu bulacaktı.»
   - Açıklama: Koku bulunmaz; kastedilen yaprağı kokusundan bilmek, fiil yanlış seçilmiş.
   - Açıklama: Koku bulunmaz; yaprağın ne olduğunu kokusundan bulmak kastediliyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ikisi de aynı anda gözlerini kapadı"
   - Cümle 3: «Ama ikisi de aynı anda gözlerini kapadı ve kimse yaprak vermedi.»
   - Açıklama: İkisinin aynı anda göz kapaması zorlama ve önemsiz bir sorun.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sırayla oynamak ona yeni bir koku öğretmişti"
   - Cümle 12: «Keloğlan çok sevindi, çünkü sırayla oynamak ona yeni bir koku öğretmişti.»
   - Açıklama: Soyut bir eylem özne yapılıp öğretme işi ona verilmiş; mecazlı anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0185` birebir aynı, ardından `@onarim: ccba1828ea2d6a44077a86fc638db345b2ff6eac`, sonra gövde.

### Hikâye 4: tohum keloglan-0186 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | Bilgecan Dede
@tohum: keloglan-0186
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Bilgecan Dede
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'etek', fiil 'özlemek', sıfat 'devasa'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | şato | Bilgecan Dede
@plan: sürpriz çiçekler yüksek kapıya ulaşmadı | sepeti düşürdü ve çiçeklerle yolu süsledi
@tohum: keloglan-0186
@degisim: etek -> çiçek
Şatonun bahçesinde devasa bir taş kapı vardı. Keloğlan, Bilgecan Dede için kapıyı çiçeklerle süslemek istedi. Ama kapı çok yüksekti ve Keloğlan'ın eli yukarı uzanamadı. Dede şatonun çiçekli bahçesini çok özlemişti ve biraz sonra gelecekti. Keloğlan çiçek sepetini kucakladı ve kapıya doğru yürüdü. Sakar Keloğlan acele etti ve sepeti elinden düşürdü. Çiçekler kapıya giden taş yola döküldü. Keloğlan yola baktı ve güldü, çünkü yol rengarenk olmuştu. Kalan çiçekleri de yolun iki yanına dizdi. Biraz sonra Bilgecan Dede kapıdan içeri girdi. Çiçekli yolu görünce "Ne güzel bir sürpriz, Keloğlan!" dedi Dede. Keloğlan çok sevindi, çünkü Dede çiçekli yolu çok sevmişti.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sürpriz çiçekler yüksek kapıya ulaşmadı"
   - Cümle 0 (plan satırı): «sürpriz çiçekler yüksek kapıya ulaşmadı | sepeti düşürdü ve çiçeklerle yolu süsledi»
   - Açıklama: Çiçekler kendi başına bir yere ulaşmaya çalışmaz; kapıya uzanamayan Keloğlan'dır, fiil öznesine uymuyor.
   - Açıklama: Çiçekler kendi ulaşmaz; fiil öznesine uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "devasa bir taş kapı"
   - Cümle 1: «Şatonun bahçesinde devasa bir taş kapı vardı.»
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki bir çocuk bilmez; 'çok büyük' denmeli.
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki çocuk bilmez.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "eli yukarı uzanamadı"
   - Cümle 3: «Ama kapı çok yüksekti ve Keloğlan'ın eli yukarı uzanamadı.»
   - Açıklama: 'Eli uzanamadı' yanlış; 'eli yetişmedi' olmalı.
4. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Dede şatonun çiçekli bahçesini çok özlemişti"
   - Cümle 4: «Dede şatonun çiçekli bahçesini çok özlemişti ve biraz sonra gelecekti.»
   - Açıklama: Kartın şato kararında sahibi yazılmıyor ve Bilgecan Dede köyün bilgesi; Dede'ye şatoyla kartta olmayan bir bağ ekleniyor.
   - Açıklama: Kartın Bilgecan Dede ilişkisi onu köyün bilgesi olarak verir ve şato kararı sahibi yazılmayan uzak bir saray der; Dede'yi şatoya bağlamak kartta olmayan bir bilgi ekliyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sepeti elinden düşürdü"
   - Cümle 6: «Sakar Keloğlan acele etti ve sepeti elinden düşürdü.»
   - Açıklama: Çözüm kapının yüksekliği sebebine yönelmiyor, kazayla başka bir süslemeye dönüşüyor.
   - Açıklama: Çözüm kapının yüksekliğine yönelmiyor; sorun bir kaza ile başka bir şeye dönüşerek kendiliğinden çözülüyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sakar Keloğlan acele etti ve sepeti elinden düşürdü"
   - Cümle 6: «Sakar Keloğlan acele etti ve sepeti elinden düşürdü.»
   - Açıklama: Çözümü figürün düşüncesi değil tesadüfi bir kaza getiriyor.
   - Açıklama: Çözümü getiren olay önceki olaydan çıkmıyor, sebepsiz bir kazayla geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0186` birebir aynı, `@degisim: etek -> çiçek` (tutuyorsan), ardından `@onarim: 1cf77aac395fb07d25c3eff8ac78a843eede8738`, sonra gövde.

### Hikâye 5: tohum keloglan-0187 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0187
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'sünger', fiil 'gelmek', sıfat 'esnek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: sünger çok hafifti ve kovaya girmedi | süngeri sıkıp küçük bir top yaptı
@tohum: keloglan-0187
Keloğlan evin önünde süngerle bir atma oyunu oynuyordu. Kovayı duvarın dibine koymuş, süngeri içine atıyordu. Ama sünger çok hafifti ve hep kovanın yanına düşüyordu. Karakaçan her seferinde gelip süngeri ağzıyla getiriyordu. Keloğlan dürüst davrandı ve "Bu atış olmadı, yine deneyeceğim," dedi. Sonra süngere baktı. Sünger esnekti, sıkılınca küçülüyordu. Keloğlan süngeri avucunda iyice sıktı ve küçük bir top yaptı. Sünger bu kez kovanın içine düştü! Karakaçan başını salladı ve kulaklarını oynattı. "Oldu, Karakaçan, sen de bana çok iyi yardım ettin!" dedi Keloğlan.
```

**Hakem bulguları (4):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "Kovayı duvarın dibine koymuş"
   - Cümle 2: «Kovayı duvarın dibine koymuş, süngeri içine atıyordu.»
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı biçime kayıyor; 'koymuştu' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sünger esnekti, sıkılınca"
   - Cümle 7: «Sünger esnekti, sıkılınca küçülüyordu.»
   - Açıklama: 'Esnek' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Esnek' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "süngeri avucunda iyice sıktı"
   - Cümle 8: «Keloğlan süngeri avucunda iyice sıktı ve küçük bir top yaptı.»
   - Açıklama: Sorunun sebebi süngerin hafifliği ama sıkmak süngeri ağırlaştırmıyor, çözüm sebebe doğrudan yönelmiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan süngeri avucunda iyice sıktı ve küçük bir top yaptı"
   - Cümle 8: «Keloğlan süngeri avucunda iyice sıktı ve küçük bir top yaptı.»
   - Açıklama: Sorunun sebebi süngerin hafifliği ama sıkmak ağırlığı değiştirmiyor, üstelik esnek sünger bırakılınca yeniden açılır; çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0187` birebir aynı, ardından `@onarim: 120661e08eb5eae7759e6f78951f256d30b04173`, sonra gövde.

### Hikâye 6: tohum keloglan-0188 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | anası
@tohum: keloglan-0188
- yer: dağ (Köyün yakınındaki tepe.)
- tema: sırayla oynamak
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'börek', fiil 'affetmek', sıfat 'garip'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | anası
@plan: ilk sırayı kimin alacağını bilemediler | düşen kozalak ilk sırayı anneye verdi
@tohum: keloglan-0188
@degisim: affetmek -> seçmek
Tepede serin bir rüzgar esiyordu. Keloğlan ile anası çimenlere oturmuş, börek yiyordu. Börekler bitince boş sepeti önlerine koydular. İkisi yerdeki kozalakları sırayla sepete atmak istedi. Ama ilk sırayı kimin alacağını bilemediler. "Önce sen at, anne," dedi Keloğlan. "Hayır, önce sen," dedi anası. Keloğlan biraz sakardı, gülerken kozalağı elinden düşürdü. Kozalak garip bir şekilde yuvarlandı ve anasının önünde durdu. "Kozalak seni seçti, ilk sıra senin, anne," dedi Keloğlan. Anası güldü ve kozalağı sepete attı. Sonra sıra Keloğlan'a geçti. "Sırayla oynamak çok güzel, anneciğim!" dedi Keloğlan.
```

**Hakem bulguları (9):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "düşen kozalak ilk sırayı anneye verdi"
   - Cümle 0 (plan satırı): «ilk sırayı kimin alacağını bilemediler | düşen kozalak ilk sırayı anneye verdi»
   - Açıklama: Kozalak bir şey veremez; fiil cansız özneye uymuyor.
   - Açıklama: Kozalak sıra veremez; fiil öznesine uymuyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 5: «Ama ilk sırayı kimin alacağını bilemediler.»
   - Açıklama: Sorun ancak 5. cümlede söyleniyor, ilk 3 cümlede yok.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ilk sırayı kimin alacağını bilemediler"
   - Cümle 5: «Ama ilk sırayı kimin alacağını bilemediler.»
   - Açıklama: İkisinin de nazikçe birbirine sıra vermesi çocuk için önemsiz, sorun sayılmayacak bir olay.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "gülerken kozalağı elinden düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı, gülerken kozalağı elinden düşürdü.»
   - Açıklama: Sorunu Keloğlan'ın bilinçli bir hareketi değil, rastlantısal bir sakarlık çözüyor.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "kozalağı elinden düşürdü"
   - Cümle 8: «Keloğlan biraz sakardı, gülerken kozalağı elinden düşürdü.»
   - Açıklama: Sorunu Keloğlan bilerek çözmüyor; sıra kazara düşen kozalakla belirleniyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Kozalak garip bir şekilde yuvarlandı"
   - Cümle 9: «Kozalak garip bir şekilde yuvarlandı ve anasının önünde durdu.»
   - Açıklama: Çözüm sebebe yönelen bir eylem değil, kozalağın rastgele yuvarlanması.
   - Açıklama: Çözüm sebebe yönelen bir eylem değil, şansa bağlı tuhaf bir olay.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kozalak garip bir şekilde yuvarlandı"
   - Cümle 9: «Kozalak garip bir şekilde yuvarlandı ve anasının önünde durdu.»
   - Açıklama: Çözümü getiren olay sebepsiz ve 'garip bir şekilde' rastlantıyla oluyor.
8. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kozalak seni seçti, ilk"
   - Cümle 10: «"Kozalak seni seçti, ilk sıra senin, anne," dedi Keloğlan.»
   - Açıklama: Kozalağın seçmesi mecazdır; cansız nesneye kişilik veriliyor.
9. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kozalak seni seçti"
   - Cümle 10: «"Kozalak seni seçti, ilk sıra senin, anne," dedi Keloğlan.»
   - Açıklama: Kozalağın seçmesi kişileştirme/mecaz, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0188` birebir aynı, `@degisim: affetmek -> seçmek` (tutuyorsan), ardından `@onarim: 962a4ebe682bd593f6634ba7b2fb47933d5a1c9c`, sonra gövde.

### Hikâye 7: tohum keloglan-0189 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0189
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'meşe', fiil 'kirletmek', sıfat 'hareketsiz'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: çamur küçük meşe ağacının yapraklarını kirletti | düşen testinin suyu çamuru yıkadı
@tohum: keloglan-0189
Bir sabah Keloğlan ormanda yürüyordu. Hafif bir rüzgar büyük ağaçların yapraklarını sallıyordu. Ama küçük bir meşe ağacının yaprakları hareketsizdi. Keloğlan eğilip ona baktı. Yağmurdan kalan çamur yaprakları kirletmişti. Yapraklar çamurla kaplıydı ve çok ağırdı. Keloğlan ağacı temizlemek istedi. Elinde içmek için bir testi su vardı. Suyu yapraklara yavaşça dökmek için testiyi kaldırdı. Ama Keloğlan biraz sakardı ve testiyi elinden düşürdü. Testi devrildi ve bütün su yaprakların üstüne aktı. Su çamuru bir anda yıkadı. Temiz yapraklar rüzgarda yeniden sallandı. Keloğlan çok sevindi, çünkü küçük meşe yine tertemizdi.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Ama küçük bir meşe ağacının yaprakları hareketsizdi.»
   - Açıklama: İlk üç cümlede yalnız yaprakların hareketsiz olduğu söyleniyor; asıl sorun olan çamur ancak 5. cümlede açıklanıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "testiyi elinden düşürdü"
   - Cümle 10: «Ama Keloğlan biraz sakardı ve testiyi elinden düşürdü.»
   - Açıklama: Sorunu Keloğlan'ın bilinçli eylemi değil, testinin kazara düşmesi çözüyor.
   - Açıklama: Sorunu Keloğlan'ın bilinçli eylemi değil, testiyi kazara düşürmesi çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0189` birebir aynı, ardından `@onarim: 9afb8a1aee08cfa6327b1bb9381bc81bbd03f9e5`, sonra gövde.

### Hikâye 8: tohum keloglan-0192 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0192
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'dilim', fiil 'uyandırmak', sıfat 'saklı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kuru bir dal küçük çiçeklere güneşi kapattı | dalı kaldırıp çiçeklere güneş verdi
@tohum: keloglan-0192
@degisim: dilim -> dal
Bir sabah Keloğlan ormanda büyük bir ağacın altında uyuyordu. Güneş yüzüne geldi ve onu uyandırdı. Keloğlan kalktı ve çevresine baktı. Güneşin altındaki sarı çiçekler açıktı. Ama kuru bir dalın altında saklı küçük çiçekler kapalıydı. Keloğlan onların da açılmasını istedi. İki yere dikkatle baktı. Açık çiçeklerin üstünde güneş vardı, kapalı çiçekler gölgede kalmıştı. Böylece Keloğlan çiçeklerin güneşte açıldığını öğrendi. Kuru dalı kaldırdı ve kenara koydu. Güneş saklı çiçeklere de ulaştı. Biraz sonra küçük çiçekler yavaş yavaş açıldı. Keloğlan çok sevindi, çünkü bütün çiçekler artık açıktı.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dalı kaldırıp çiçeklere güneş verdi"
   - Cümle 0 (plan satırı): «kuru bir dal küçük çiçeklere güneşi kapattı | dalı kaldırıp çiçeklere güneş verdi»
   - Açıklama: Keloğlan güneş veremez; fiil öznesine uymuyor, güneşin çiçeklere ulaşmasını sağladı denmeli.
   - Açıklama: Keloğlan güneş veremez; fiil öznesine uymuyor, 'güneş çiçeklere ulaştı' gibi olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Keloğlan ormanda büyük bir ağacın altında uyuyordu"
   - Cümle 1: «Bir sabah Keloğlan ormanda büyük bir ağacın altında uyuyordu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde ormanda tek başına ağaç altında uyunuyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "kuru bir dalın altında saklı küçük çiçekler kapalıydı"
   - Cümle 5: «Ama kuru bir dalın altında saklı küçük çiçekler kapalıydı.»
   - Açıklama: Sorun ilk üç cümlede değil, uyanma sahnesinden sonra ancak beşinci cümlede söyleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kuru bir dalın altında saklı küçük çiçekler kapalıydı"
   - Cümle 5: «Ama kuru bir dalın altında saklı küçük çiçekler kapalıydı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak beşinci cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0192` birebir aynı, `@degisim: dilim -> dal` (tutuyorsan), ardından `@onarim: 73ee54ae235fa0c47f32649a4a7770f9a6587476`, sonra gövde.

### Hikâye 9: tohum keloglan-0193 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | -
@tohum: keloglan-0193
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'erik', fiil 'sıkmak', sıfat 'aydınlık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | şato | -
@plan: bahçeden pat diye bir ses geldi | erikleri sıkıp sesin düşen erikler olduğunu buldu
@tohum: keloglan-0193
Şatonun aydınlık bahçesinde Keloğlan yürüyordu. Birden yakından pat diye bir ses geldi. Keloğlan sesin nereden geldiğini merak etti. Biraz sonra aynı ses yine duyuldu. Keloğlan sesin geldiği yere, büyük bir erik ağacının altına gitti. Yerde mor erikler vardı. Tam o sırada bir erik daha pat diye yere düştü. Keloğlan yerdeki bir eriği hafifçe sıktı ve yumuşak buldu. Sonra dalda asılı bir erik tuttu, o sertti. Keloğlan böylece sesin olgun eriklerden geldiğini öğrendi. Keloğlan yerdeki olgun erikleri topladı ve mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "sesin düşen erikler olduğunu"
   - Cümle 0 (plan satırı): «bahçeden pat diye bir ses geldi | erikleri sıkıp sesin düşen erikler olduğunu buldu»
   - Açıklama: Ses erik olamaz; 'sesin düşen eriklerden geldiğini' olmalı.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan yerdeki bir eriği hafifçe sıktı"
   - Cümle 8: «Keloğlan yerdeki bir eriği hafifçe sıktı ve yumuşak buldu.»
   - Açıklama: Sesin kaynağı 7. cümlede erik düşerken zaten görülüyor; erikleri sıkma adımları gereksiz ve çözüm ikiden fazla adıma yayılıyor.
   - Açıklama: Erik düşerken ses zaten görülmüşken erikleri sıkmak sesin kaynağına doğrudan yönelmiyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yerdeki olgun erikleri topladı ve mutlu mutlu yedi"
   - Cümle 11: «Keloğlan yerdeki olgun erikleri topladı ve mutlu mutlu yedi.»
   - Açıklama: Çocuk başkasına ait bir bahçede yerden topladığı meyveyi izinsiz ve yıkamadan yiyor; taklit edilince riskli bir davranış.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Keloğlan yerdeki olgun erikleri topladı ve mutlu mutlu yedi"
   - Cümle 11: «Keloğlan yerdeki olgun erikleri topladı ve mutlu mutlu yedi.»
   - Açıklama: Çocuk yerden topladığı yıkanmamış meyveyi başkasının bahçesinde izinsiz yiyor; taklit edilebilir bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0193` birebir aynı, ardından `@onarim: a0ab750c1f799bed69ae85b49bbab2f31b57d3ae`, sonra gövde.

### Hikâye 10: tohum keloglan-0196 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0196
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: eşeği
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'zeytin', fiil 'düzeltmek', sıfat 'sağlam'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: odun yığını tek başına taşımak için çok ağırdı | ıslık çalıp eşeğinden yardım istedi
@tohum: keloglan-0196
@degisim: zeytin -> odun
Rüzgar ormanın büyük ağaçları arasında esiyordu. Keloğlan eve götürmek için kuru ve sağlam odunlar toplamıştı. Ama odun yığını çok ağırdı. Keloğlan odunları kucağına aldı ve yürüdü. Ama biraz sakardı ve birkaç adım sonra odunları yere düşürdü. Keloğlan yardım gerektiğini anladı. Parmaklarını ağzına koyup uzun bir ıslık çaldı. Karakaçan ağaçların arasından koşarak geldi. "Bana yardım eder misin, Karakaçan?" diye sordu Keloğlan. Karakaçan başını salladı. Keloğlan odunları eşeğin sırtına yükledi. Yük biraz yana kaydı ve Keloğlan onu hemen düzeltti. Karakaçan odunları kolayca taşıdı. Keloğlan bundan sonra ağır yükler için hep Karakaçan'dan yardım istedi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama biraz sakardı"
   - Cümle 5: «Ama biraz sakardı ve birkaç adım sonra odunları yere düşürdü.»
   - Açıklama: 'sakar' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "biraz sakardı ve birkaç adım sonra odunları yere düşürdü"
   - Cümle 5: «Ama biraz sakardı ve birkaç adım sonra odunları yere düşürdü.»
   - Açıklama: Sorunun sebebi yükün ağırlığı diye kuruluyor ama odunlar sakarlık yüzünden düşüyor, sebep karışıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yük biraz yana kaydı ve Keloğlan onu hemen düzeltti"
   - Cümle 12: «Yük biraz yana kaydı ve Keloğlan onu hemen düzeltti.»
   - Açıklama: Yükün kayması olaydan çıkmayan ve hiçbir sonucu olmayan işlevsiz bir ayrıntı.
   - Açıklama: Yükün kayması hiçbir şeye bağlanmayan işlevsiz ek bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0196` birebir aynı, `@degisim: zeytin -> odun` (tutuyorsan), ardından `@onarim: 1fb2d029c470102dabbcd1eef86568fa701bac17`, sonra gövde.

### Hikâye 11: tohum keloglan-0198 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0198
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'külah', fiil 'bırakmak', sıfat 'bol'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: kağıt külah bol geldi ve gözlerinin üstüne kaydı | anasından kağıdı sarmayı öğrendi ve külahı küçülttü
@tohum: keloglan-0198
Köy evinin odasında Keloğlan ile anası komik bir oyun oynuyordu. İkisi kağıttan külah yapıp başlarına taktı. Sonra odada büyük adımlarla yürüyüp güldüler. Ama Keloğlan'ın külahı çok boldu ve gözlerinin üstüne kaydı. Keloğlan önünü göremedi. "Anne, bu külah bana çok büyük," dedi Keloğlan. "Kağıdı daha sıkı sar ve ucunu katla," dedi anası. Keloğlan dikkatle dinledi ve bunu hemen öğrendi. Külahı masaya bıraktı, kağıdı sıkıca sardı ve ucunu katladı. Bu kez külah başından hiç kaymadı. İkisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Keloğlan'ın külahı çok boldu"
   - Cümle 4: «Ama Keloğlan'ın külahı çok boldu ve gözlerinin üstüne kaydı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Keloğlan'ın külahı çok boldu ve gözlerinin üstüne kaydı"
   - Cümle 4: «Ama Keloğlan'ın külahı çok boldu ve gözlerinin üstüne kaydı.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor; ilk 3 cümle yalnız oyunu anlatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0198` birebir aynı, ardından `@onarim: 28eba25074c82ddb2edbe9c1517a83f1b1f24b9c`, sonra gövde.

### Hikâye 12: tohum keloglan-0199 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0199
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'sandalye', fiil 'sunmak', sıfat 'uzak'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: uzaktan adını söyleyen garip bir ses geldi | kayalara seslenip sesin geri döndüğünü öğrendi
@tohum: keloglan-0199
@degisim: sandalye -> kaya
Rüzgar hafif hafif esiyordu. Keloğlan ile Balkız tepede oturmuş, uzaktaki dağlara bakıyordu. Keloğlan çantasından iki elma çıkardı ve birini Balkız'a sundu. "Afiyet olsun, Balkız!" dedi Keloğlan yüksek sesle. Uzaktan "Balkız!" diye bir ses geldi. "Bu ses nereden geldi?" diye sordu Balkız. Keloğlan bunu bulmak istedi. Ellerini ağzına koydu ve karşıdaki büyük kayalara "Elma!" diye seslendi. Biraz sonra kayalardan yine "Elma!" sesi geldi. Böylece Keloğlan sesin kayalara çarpıp geri döndüğünü öğrendi. Balkız da kayalara seslendi ve güldü. Keloğlan bundan sonra bir sesi merak edince onu kendisi deneyip buldu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "birini Balkız'a sundu"
   - Cümle 3: «Keloğlan çantasından iki elma çıkardı ve birini Balkız'a sundu.»
   - Açıklama: 'sunmak' 3 yaşındaki çocuğun bilmeyeceği resmi bir kelime; 'verdi' olmalı.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Keloğlan çantasından iki elma çıkardı ve birini Balkız'a sundu.»
   - Açıklama: İlk üç cümle rüzgar, oturma ve elma ile geçiyor; garip ses sorunu ancak beşinci cümlede ortaya çıkıyor.
   - Açıklama: Garip ses sorunu ilk 3 cümlede değil ancak 5. cümlede ortaya çıkıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kayalardan yine "Elma!" sesi"
   - Cümle 9: «Biraz sonra kayalardan yine "Elma!" sesi geldi.»
   - Açıklama: 'Elma!' sesi ilk kez geliyor; 'yine' yanlış anlamda.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "onu kendisi deneyip buldu"
   - Cümle 12: «Keloğlan bundan sonra bir sesi merak edince onu kendisi deneyip buldu.»
   - Açıklama: Bir ses 'deneyip bulunmaz'; fiiller nesnesine uymuyor ve cümle anlamca bozuk.
   - Açıklama: 'sesi deneyip bulmak' anlamca bozuk bir söyleyiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0199` birebir aynı, `@degisim: sandalye -> kaya` (tutuyorsan), ardından `@onarim: 17d52f3d76f09f73d2f946a88e32af7eb222b1f9`, sonra gövde.
