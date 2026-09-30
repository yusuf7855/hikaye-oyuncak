# Editör görevi (onarım): Keloğlan, onarım partisi 38

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar38.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar38.txt --ad urun_v2`
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

### Hikâye 1: tohum keloglan-0151 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | -
@tohum: keloglan-0151
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: kaybolan eşya
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'turşu', fiil 'gizlenmek', sıfat 'turuncu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | -
@plan: turuncu top yuvarlandı ve mutfakta kayboldu | düşürdüğü sepeti almaya gidince topu kavanozun arkasında buldu
@tohum: keloglan-0151
Evin mutfağında Keloğlan turuncu topuyla oynuyordu. Top zıpladı, yuvarlandı ve gözden kayboldu. Keloğlan topunu masanın altında aradı ama bulamadı. Dolabın yanına da baktı, top orada da yoktu. Sepetin altına bakmak için sepeti kaldırdı ama sakarlık yapıp onu düşürdü. Sepet yuvarlandı ve köşedeki büyük turşu kavanozunun arkasına gitti. Keloğlan sepeti almak için köşeye yürüdü. Kavanozun arkasında turuncu bir şey vardı. Top orada gizlenmiş gibi duruyordu. Keloğlan topu ve sepeti aldı. Sepeti yerine koydu, topu da sıkıca tuttu. Keloğlan çok sevindi, çünkü kaybolan topunu sonunda bulmuştu.
```

**Hakem bulguları (7):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yuvarlandı ve gözden kayboldu"
   - Cümle 2: «Top zıpladı, yuvarlandı ve gözden kayboldu.»
   - Açıklama: 'Gözden kaybolmak' deyimdir, küçük çocuk için uygun değil.
   - Açıklama: 'Gözden kaybolmak' deyimdir; 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sakarlık yapıp onu düşürdü"
   - Cümle 5: «Sepetin altına bakmak için sepeti kaldırdı ama sakarlık yapıp onu düşürdü.»
   - Açıklama: 'Sakarlık' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sakarlık yapıp onu düşürdü"
   - Cümle 5: «Sepetin altına bakmak için sepeti kaldırdı ama sakarlık yapıp onu düşürdü.»
   - Açıklama: Top aramaya yönelik bir çözüm yok; top sepet kazayla düşünce tesadüfen bulunuyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sepet yuvarlandı ve köşedeki büyük turşu kavanozunun arkasına gitti"
   - Cümle 6: «Sepet yuvarlandı ve köşedeki büyük turşu kavanozunun arkasına gitti.»
   - Açıklama: Sepetin tam topun saklandığı yere yuvarlanması çözümü sebepsizce getiriyor.
   - Açıklama: Çözümü sebepsiz bir tesadüf getiriyor; sepet tam da topun saklandığı yere yuvarlanıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Keloğlan sepeti almak için köşeye yürüdü"
   - Cümle 7: «Keloğlan sepeti almak için köşeye yürüdü.»
   - Açıklama: Top aranarak değil düşen sepetin peşinden gidilirken rastlantıyla bulunuyor.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Top orada gizlenmiş gibi"
   - Cümle 9: «Top orada gizlenmiş gibi duruyordu.»
   - Açıklama: Top gizlenemez; fiil öznesine uymuyor.
7. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "orada gizlenmiş gibi duruyordu"
   - Cümle 9: «Top orada gizlenmiş gibi duruyordu.»
   - Açıklama: Top gizlenmez; benzetme/mecaz 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0151` birebir aynı, ardından `@onarim: 55ca93ea394ebc347e76b5a24d22c8c1514887d6`, sonra gövde.

### Hikâye 2: tohum keloglan-0152 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0152
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: sırayla oynamak
- yan: anası
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'şeftali', fiil 'cevaplamak', sıfat 'rengarenk'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: annesi tüylü meyveyi sordu ama cevabı bilmiyordu | sepetteki meyvelere tek tek dokundu ve şeftaliyi buldu
@tohum: keloglan-0152
Bir sabah Keloğlan ile anası evde sırayla soru soruyordu. "Hangi meyvenin kabuğu tüylü?" diye sordu anası. Keloğlan cevabı bilmiyordu ama öğrenmek istedi. Masada rengarenk meyvelerle dolu bir sepet vardı. Keloğlan meyveleri tek tek eline aldı ve kabuklarına dokundu. Elma ile armut kaygandı. Ama şeftalinin kabuğu yumuşak ve tüylüydü. "Şeftali, anneciğim!" dedi Keloğlan. "Aferin, doğru cevapladın, şimdi sıra sende," dedi anası. "Hangi meyvenin içinde büyük bir çekirdek var?" diye sordu Keloğlan. "Şeftalinin," dedi anası gülerek. Keloğlan çok sevindi, çünkü tüylü meyveyi kendi bulmuştu.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ama cevabı bilmiyordu"
   - Cümle 3: «Keloğlan cevabı bilmiyordu ama öğrenmek istedi.»
   - Açıklama: Plan satırında cevabı bilmeyenin annesi mi Keloğlan mı olduğu belli değil.
   - Açıklama: Plan satırında cevabı bilmeyenin kim olduğu belli değil; özne annesi gibi okunuyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "meyveyi kendi bulmuştu"
   - Cümle 12: «Keloğlan çok sevindi, çünkü tüylü meyveyi kendi bulmuştu.»
   - Açıklama: 'kendi' yerine 'kendisi' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "tüylü meyveyi kendi bulmuştu"
   - Cümle 12: «Keloğlan çok sevindi, çünkü tüylü meyveyi kendi bulmuştu.»
   - Açıklama: 'Kendi' zamiri eksik; 'kendisi bulmuştu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0152` birebir aynı, ardından `@onarim: 79ab3dffb995800596b15d25dae79b4d32609409`, sonra gövde.

### Hikâye 3: tohum keloglan-0153 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0153
- yer: dağ (Köyün yakınındaki tepe.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'şemsiye', fiil 'ekmek', sıfat 'ilginç'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: rüzgar esti ve tohumlar elinden uçup gitti | tohumları toplayıp şemsiyenin arkasında ekti
@tohum: keloglan-0153
Dağda Keloğlan bahçe oyunu oynuyordu. Elinde ilginç, çizgili ayçiçeği tohumları vardı. Ama rüzgar esti ve tohumlar elinden uçup gitti. Keloğlan dürüst ve azimliydi, bu yüzden tohumları bir bir topladı. Yanında bir şemsiye vardı, çünkü hava bulutluydu. Şemsiyeyi açtı ve rüzgara karşı yere koydu. Şemsiyenin arkasında hiç rüzgar yoktu. Keloğlan toprağı parmağıyla kazdı ve tohumları tek tek ekti. Üstlerini toprakla örttü. Tohumlar artık uçmadı ve bahçe hazır oldu. Keloğlan bundan sonra rüzgarlı havada tohumlarını şemsiyenin arkasında ekti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Keloğlan dürüst ve azimliydi, bu yüzden"
   - Cümle 4: «Keloğlan dürüst ve azimliydi, bu yüzden tohumları bir bir topladı.»
   - Açıklama: Dürüstlük tohum toplamanın sebebi olamaz; özellik kelimesi yanlış yerde kullanılmış.
   - Açıklama: Tohumları toplamak dürüstlükten kaynaklanmaz; 'dürüst' yanlış anlamda.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "bu yüzden tohumları bir bir topladı"
   - Cümle 4: «Keloğlan dürüst ve azimliydi, bu yüzden tohumları bir bir topladı.»
   - Açıklama: Çözüm tohumları toplama, şemsiyeyi kurma ve ekme adımlarıyla iki adımı aşıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanında bir şemsiye vardı, çünkü hava bulutluydu"
   - Cümle 5: «Yanında bir şemsiye vardı, çünkü hava bulutluydu.»
   - Açıklama: Şemsiye daha önce kurulmadan tam çözüm için beliriyor ve çözümü sebepsizce getiriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yanında bir şemsiye vardı"
   - Cümle 5: «Yanında bir şemsiye vardı, çünkü hava bulutluydu.»
   - Açıklama: Çözümü getiren şemsiye sebepsizce hazır bulunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0153` birebir aynı, ardından `@onarim: 310f9fda1f4e63d01eb5d5883d8aa2537c5e30e2`, sonra gövde.

### Hikâye 4: tohum keloglan-0154 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0154
- yer: dağ (Köyün yakınındaki tepe.)
- tema: bir şey yapmak
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çubuk', fiil 'sarmak', sıfat 'meyveli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: uçurtmanın çubukları hep birbirinden kayıyordu | dede çubukları tuttu ve ipi ortalarına sıkıca sardı
@tohum: keloglan-0154
@degisim: meyveli -> uzun
Keloğlan ile Bilgecan Dede dağda bir uçurtma yapıyordu. İki ince çubuğu üst üste koydular. Ama çubuklar hep birbirinden kayıyordu, çünkü onları tutan bir şey yoktu. "Dede, çubukları sen tutar mısın?" diye sordu Keloğlan. "Tabii, sıkıca tutuyorum," dedi Bilgecan Dede. Keloğlan ipi çubukların ortasına sardı. Çubuklar yine kaydı ama dürüst ve azimli Keloğlan işini bırakmadı. Bu sefer ipi üç kere sıkı sıkı sardı. Çubuklar artık hiç kaymadı. Sonra uçurtmaya sarı bir kağıt ve uzun bir kuyruk taktılar. Rüzgar esti ve uçurtma havalandı. Keloğlan ile dede uçurtmayı tepede mutlu mutlu uçurdular.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "dede çubukları tuttu ve ipi ortalarına sıkıca sardı"
   - Cümle 0 (plan satırı): «uçurtmanın çubukları hep birbirinden kayıyordu | dede çubukları tuttu ve ipi ortalarına sıkıca sardı»
   - Açıklama: Plan ipi dedenin sardığını ima ediyor ama gövdede ipi Keloğlan sarıyor.
   - Açıklama: Gövdede ipi dede değil Keloğlan sarıyor; dede yalnız çubukları tutuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ama dürüst ve azimli Keloğlan"
   - Cümle 7: «Çubuklar yine kaydı ama dürüst ve azimli Keloğlan işini bırakmadı.»
   - Açıklama: İşi bırakmamakla dürüstlüğün ilgisi yok; 'dürüst' yanlış anlamda kullanılmış.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dürüst ve azimli Keloğlan"
   - Cümle 7: «Çubuklar yine kaydı ama dürüst ve azimli Keloğlan işini bırakmadı.»
   - Açıklama: 'Dürüst' kelimesi olayla ilgisiz, yanlış anlamda kullanılmış.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Çubuklar yine kaydı"
   - Cümle 7: «Çubuklar yine kaydı ama dürüst ve azimli Keloğlan işini bırakmadı.»
   - Açıklama: Dede çubukları sıkıca tuttuğunu söylemesine rağmen çubuklar yine kayıyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bu sefer ipi üç kere sıkı sıkı sardı"
   - Cümle 8: «Bu sefer ipi üç kere sıkı sıkı sardı.»
   - Açıklama: İlk sarma başarısız oluyor ve çözüm tekrar denemeyle ikiden fazla adıma uzuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0154` birebir aynı, `@degisim: meyveli -> uzun` (tutuyorsan), ardından `@onarim: e67f7dc692d1c58c2a1a24a7e4a5a1423cd53d33`, sonra gövde.

### Hikâye 5: tohum keloglan-0155 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | eşeği
@tohum: keloglan-0155
- yer: dağ (Köyün yakınındaki tepe.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'çuval', fiil 'yeşermek', sıfat 'ufak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | eşeği
@plan: eşeğine çok ağır çuvallar koydu ve eşek durdu | özür diledi ve ufak çuvalı kendi taşıdı
@tohum: keloglan-0155
Dağda serin bir rüzgar esiyordu. Keloğlan eşeğinin sırtına büyük bir çuval ve ufak bir çuval odun koymuştu. Karakaçan birkaç adım attı ve durdu, çünkü çuvallar çok ağırdı. Keloğlan eşeğine fazla odun koyduğunu hemen anladı. Keloğlan dürüst bir çocuktu ve eşeğinden hemen özür diledi. Eşeğinin başını okşadı. Sonra ufak çuvalı indirdi ve kendi sırtına aldı. Karakaçan başını salladı ve yeniden yürüdü. Keloğlan onu yeşeren otların yanına götürdü. Eşek otları keyifle yedi. Keloğlan çok sevindi, çünkü eşeği artık büyük çuvalı kolayca taşıyordu.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Karakaçan birkaç adım attı"
   - Cümle 3: «Karakaçan birkaç adım attı ve durdu, çünkü çuvallar çok ağırdı.»
   - Açıklama: Karakaçan'ın eşek olduğu söylenmeden adıyla anılıyor; kimi gösterdiği belli değil.
   - Açıklama: Karakaçan adı eşekle bağlanmadan birden geçiyor; kimi gösterdiği belli değil.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "eşeğinden hemen özür diledi"
   - Cümle 5: «Keloğlan dürüst bir çocuktu ve eşeğinden hemen özür diledi.»
   - Açıklama: 'Hemen' art arda iki cümlede gereksiz tekrar ediliyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "onu yeşeren otların yanına"
   - Cümle 9: «Keloğlan onu yeşeren otların yanına götürdü.»
   - Açıklama: 'Yeşeren' kelimesi 3 yaşındaki bir çocuk için zor.
   - Açıklama: 'Yeşeren' kelimesi 3 yaşındaki çocuğun bileceği bir kelime değil.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Keloğlan onu yeşeren otların yanına götürdü"
   - Cümle 9: «Keloğlan onu yeşeren otların yanına götürdü.»
   - Açıklama: Otlara gitme sorunla ilgisiz, işlevsiz bir ek olay.
   - Açıklama: Sorun çözüldükten sonra gelen ot sahnesi olaydan çıkmıyor ve işlevsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0155` birebir aynı, ardından `@onarim: a36a6010f81ec9ff04256ec5b8aed11e0f80fae4`, sonra gövde.
