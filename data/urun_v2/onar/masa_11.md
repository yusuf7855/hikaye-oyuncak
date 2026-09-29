# Editör görevi (onarım): Maşa, onarım partisi 11

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar11.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar11.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0011 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | -
@tohum: masa-0011
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'beşik', fiil 'öğrenmek', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | -
@plan: çilekler büyük yaprakların altında görünmüyordu | yaprakları yavaşça kaldırıp çilekleri buldu
@tohum: masa-0011
@degisim: beşik -> sepet
Bir sabah Maşa evinin önündeki bahçede tek bir kırmızı çilek fark etti. Maşa reçeli çok severdi, bu yüzden sepetini çilekle doldurmak istedi. Ama öteki çilekler görünmüyordu, çünkü büyük yaprakların altındaydı. Maşa yere eğildi ve bir yaprağı kaldırdı. Altında kıpkırmızı bir çilek duruyordu! Ama narin yaprak Maşa'nın elinde biraz yırtıldı. Maşa yaprakları yavaşça kaldırmayı çabucak öğrendi. Her seferinde yeni bir çilek buldu ve sepete koydu. Sonunda sepet çileklerle doldu. Maşa dolu sepeti eve götürdü ve mutlu mutlu çilek reçeli yaptı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama narin yaprak"
   - Cümle 6: «Ama narin yaprak Maşa'nın elinde biraz yırtıldı.»
   - Açıklama: 'Narin' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama narin yaprak Maşa'nın"
   - Cümle 6: «Ama narin yaprak Maşa'nın elinde biraz yırtıldı.»
   - Açıklama: 'Narin' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "mutlu mutlu çilek reçeli yaptı"
   - Cümle 10: «Maşa dolu sepeti eve götürdü ve mutlu mutlu çilek reçeli yaptı.»
   - Açıklama: Reçel yapmak ocak ve kaynar tencere gerektirir; küçük çocuk tek başına taklit edebilir, güvenli kullanım satırı ateşe yaklaşmamayı söyler.
   - Açıklama: Küçük bir çocuk yetişkinsiz reçel pişiriyor; ocak ve ateş kullanımı taklit edilince tehlikelidir ve güvenli kullanım satırı ateşe yaklaşmamayı söyler.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "dolu sepeti eve götürdü ve mutlu mutlu çilek reçeli yaptı"
   - Cümle 10: «Maşa dolu sepeti eve götürdü ve mutlu mutlu çilek reçeli yaptı.»
   - Açıklama: Reçel yapmak uzun sürer; son cümle bahçedeki sahneden zaman atlatarak eve geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0011` birebir aynı, `@degisim: beşik -> sepet` (tutuyorsan), ardından `@onarim: fb6ab1011bd1ed1a2cd64fbcc8e657f02529fea3`, sonra gövde.

### Hikâye 2: tohum masa-0012 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap, Daşa
@tohum: masa-0012
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tabure', fiil 'ölçmek', sıfat 'mutsuz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | sincap, Daşa
@plan: kaşık ağacın yanındaki küçük bir deliğe düştü | sincaptan yardım istedi ve sincap kaşığı getirdi
@tohum: masa-0012
@degisim: tabure -> kaşık
Bir sabah Maşa ile Daşa ormanda büyük bir ağacın altında oturuyordu. Maşa reçeli çok severdi ve kavanozdan küçük bir kaşıkla yiyordu. Birden kaşık elinden kaydı ve ağacın yanındaki bir deliğe düştü. Delik Maşa'nın elinden çok daha küçüktü. Maşa çok mutsuz oldu. Daşa deliği iki parmağıyla ölçtü. "Benim elim de sığmaz, Maşa," dedi Daşa. Dalda küçük bir sincap onlara bakıyordu. "Sincap, kaşığımı bana getirir misin?" diye sordu Maşa. Sincap hızla indi ve deliğe girdi. Biraz sonra kaşığı ağzında tutarak dışarı çıktı. "Teşekkürler, sincap!" dedi Maşa. Maşa çok sevindi, çünkü kavanozdan yine kaşığıyla yiyebilecekti.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçeli çok severdi"
   - Cümle 2: «Maşa reçeli çok severdi ve kavanozdan küçük bir kaşıkla yiyordu.»
   - Açıklama: Tohumdaki reçel sevgisi yalnız söyleniyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Özellik doğrudan söylenip sayılıyor ve sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0012` birebir aynı, `@degisim: tabure -> kaşık` (tutuyorsan), ardından `@onarim: cb9aa2c6d6c8c7a7083a44b3eb6a4503092c5899`, sonra gövde.

### Hikâye 3: tohum masa-0014 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi, Daşa
@tohum: masa-0014
- yer: dağ (Ormanın yanındaki tepe.)
- tema: sırayla oynamak
- yan: kirpi, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kürek', fiil 'dokunmak', sıfat 'ucuz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi, Daşa
@plan: tek bir kürek vardı ve ikisi de kazmak istedi | sırayla kazdılar ve fidanı diktiler
@tohum: masa-0014
@degisim: ucuz -> küçük
Tepede serin bir rüzgar esiyordu. Maşa ile Daşa kirpi için küçük bir elma fidanı dikecekti. Ama tek bir kürek vardı ve ikisi de önce kazmak istedi. Küreği aynı anda çektiler ve kürek yere düştü. Maşa'nın yanında bir kavanoz reçel vardı. "Küreği önce sen al, Daşa, ben de reçelimi yiyeyim," dedi Maşa. Daşa kazarken Maşa reçelini yedi. Sonra küreği Maşa aldı ve biraz kazdı. Sonunda çukur hazır oldu. Fidanı çukura koyup etrafını toprakla doldurdular. Kirpi yaklaştı ve burnuyla fidana dokundu. Maşa ile Daşa çok sevindi, çünkü sırayla kazınca fidan çabucak dikilmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yanında bir kavanoz reçel vardı"
   - Cümle 5: «Maşa'nın yanında bir kavanoz reçel vardı.»
   - Açıklama: Reçel kavanozu sebepsiz beliriyor ve fidan dikme olayında işlevi olmayan bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa'nın yanında bir kavanoz reçel vardı"
   - Cümle 5: «Maşa'nın yanında bir kavanoz reçel vardı.»
   - Açıklama: Reçel kavanozu sebepsizce beliriyor ve sıra kavgasının çözümünü kendiliğinden getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0014` birebir aynı, `@degisim: ucuz -> küçük` (tutuyorsan), ardından `@onarim: dfe6b2832a1c7a5df5369724b9d4e3ba85339df8`, sonra gövde.

### Hikâye 4: tohum masa-0018 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0018
- yer: dağ (Ormanın yanındaki tepe.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'lamba', fiil 'sıkılmak', sıfat 'süslü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: uçurtma her seferinde yere düştü çünkü kuyruğu kısaydı | kavanozdaki kurdeleyi kuyruğa bağladı
@tohum: masa-0018
@degisim: lamba -> uçurtma
Tepede güçlü bir rüzgar esiyordu. Maşa süslü uçurtmasını ve kurdeleli reçel kavanozunu tepeye getirmişti. Ama uçurtma her seferinde dönüp yere düştü, çünkü kuyruğu çok kısaydı. Maşa hiç sıkılmadı ve uçurtmaya dikkatle baktı. Sonra kavanozun uzun, kırmızı kurdelesini gördü. Maşa kurdeleyi çözdü ve uçurtmanın kuyruğuna bağladı. Uçurtma bu kez dönmedi ve yavaş yavaş yükseldi. Maşa uçurtmanın ipini iki eliyle tuttu ve sevinçle güldü. Kırmızı kuyruk rüzgarda sallandı. Maşa uçurtmasını tepede mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kurdeleli reçel kavanozunu tepeye"
   - Cümle 2: «Maşa süslü uçurtmasını ve kurdeleli reçel kavanozunu tepeye getirmişti.»
   - Açıklama: Tohumdaki reçel sevgisi kullanılmıyor; yalnız kavanozun kurdelesi çözümde işe yarıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kurdeleli reçel kavanozunu tepeye getirmişti"
   - Cümle 2: «Maşa süslü uçurtmasını ve kurdeleli reçel kavanozunu tepeye getirmişti.»
   - Açıklama: Tohumdaki reçel sevgisi kullanılmıyor; çözümde yalnız kavanozun kurdelesi işe yarıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0018` birebir aynı, `@degisim: lamba -> uçurtma` (tutuyorsan), ardından `@onarim: f745b02c3ed1164606bc48a99ea102d6dd800d9b`, sonra gövde.

### Hikâye 5: tohum masa-0019 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0019
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'çubuk', fiil 'utanmak', sıfat 'temkinli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: karda yıldız çizmek istedi ama ince çubuk kırıldı | kalın bir çubuk bulup yıldızı çizdi
@tohum: masa-0019
@degisim: utanmak -> çizmek
Ormanda her yer karla kaplıydı. Maşa kar tanelerinin küçük yıldızlara benzediğini fark etti. Karda bir yıldız çizmek istedi ve ince bir çubuk aldı. Ama çubuk karda hemen kırıldı. Maşa ağaçların altında yeni bir çubuk aradı. Orada kalın ve sağlam bir çubuk buldu. Maşa bu çubukla yeniden denedi. Bu kez temkinliydi ve çubuğu kara hafifçe bastırdı. Yıldızın beş ucunu tek tek çizdi. Çubuk hiç kırılmadı. Artık karda büyük bir yıldız vardı. Maşa çok sevindi, çünkü kocaman yıldızını sonunda çizmişti.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama çubuk karda hemen kırıldı"
   - Cümle 4: «Ama çubuk karda hemen kırıldı.»
   - Açıklama: Sorun ilk 3 cümlede değil, 4. cümlede söyleniyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu kez temkinliydi"
   - Cümle 8: «Bu kez temkinliydi ve çubuğu kara hafifçe bastırdı.»
   - Açıklama: 'Temkinli' kelimesi 3 yaşındaki bir çocuğun bileceği bir kelime değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez temkinliydi"
   - Cümle 8: «Bu kez temkinliydi ve çubuğu kara hafifçe bastırdı.»
   - Açıklama: Tohumdaki özellik denemek; temkinlilik ikinci bir özellik olarak ekleniyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu kez temkinliydi ve"
   - Cümle 8: «Bu kez temkinliydi ve çubuğu kara hafifçe bastırdı.»
   - Açıklama: Tohumdaki özellik denemek; kartın özellikler alanında olmayan temkinlilik ikinci bir özellik olarak ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0019` birebir aynı, `@degisim: utanmak -> çizmek` (tutuyorsan), ardından `@onarim: 92ecded08f1f14a7aa4fe86fb003b6a19baddaf8`, sonra gövde.

### Hikâye 6: tohum masa-0021 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, sincap
@tohum: masa-0021
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'ayakkabı', fiil 'sektirmek', sıfat 'devasa'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, sincap
@plan: top fındık sepetini devirdi ve fındıklar döküldü | özür diledi ve fındıkları yeniden topladı
@tohum: masa-0021
@degisim: devasa -> kocaman
Maşa bir kavanoz reçel almıştı ve kocaman bir ağacın yanında top sektiriyordu. Koca Ayı ile sincap da ağacın altında bir sepete fındık topluyordu. Maşa topa ayakkabısıyla çok sert vurdu ve top sepeti devirdi. Fındıklar yere döküldü ve sincap üzüldü. "Özür dilerim, sincap, dikkat etmedim," dedi Maşa. Sonra Maşa yere eğildi ve fındıkları tek tek topladı. Koca Ayı da ona yardım etti. Kısa sürede sepet yine fındıkla doldu. Sincap sevinçle kuyruğunu salladı. Maşa en sevdiği reçeli onlarla paylaştı ve üçü mutlu mutlu güldü.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa en sevdiği reçeli onlarla paylaştı"
   - Cümle 10: «Maşa en sevdiği reçeli onlarla paylaştı ve üçü mutlu mutlu güldü.»
   - Açıklama: Tohumdaki reçel özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0021` birebir aynı, `@degisim: devasa -> kocaman` (tutuyorsan), ardından `@onarim: 60694c955fa9151b827d30a5b2e086984997e6c7`, sonra gövde.

### Hikâye 7: tohum masa-0024 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0024
- yer: dağ (Ormanın yanındaki tepe.)
- tema: kaybolan eşya
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kızak', fiil 'kazanmak', sıfat 'güvenli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: kızak yağan karın altında kalmıştı | karı iki yerde kazdı ve kızağı buldu
@tohum: masa-0024
Bir kış sabahı Maşa ile Koca Ayı kızak yarışı için tepedeydi. Ama Maşa'nın kırmızı kızağı yağan karın altında kalmıştı. Kirpi de yarışı izlemek için gelmişti. "Kızak nerede?" diye sordu Maşa. Önce ağacın önündeki karı kazmayı denedi. Orada yalnız bir taş vardı. Sonra ağacın arkasını kazdı ve bir ip gördü. Maşa ipi çekti ve kızak karın içinden çıktı. Kirpi sevinçle etrafta koştu. Koca Ayı yarış için tepenin alçak ve güvenli bir yerini gösterdi. "Hadi, yarışalım!" dedi Maşa. Orada yarışı Maşa kazandı ve üçü mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kirpi de yarışı izlemek için gelmişti"
   - Cümle 3: «Kirpi de yarışı izlemek için gelmişti.»
   - Açıklama: Kirpi olayda hiçbir işe yaramıyor; Koca Ayı'nın güvenli yer göstermesi de işlevsiz ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Koca Ayı yarış için tepenin alçak ve güvenli bir yerini gösterdi"
   - Cümle 10: «Koca Ayı yarış için tepenin alçak ve güvenli bir yerini gösterdi.»
   - Açıklama: Güvenli yer arama olayı öncekinden çıkmıyor ve sebepsiz ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0024` birebir aynı, ardından `@onarim: 7610cc4b057f434a46163726ce0f959f001a00f9`, sonra gövde.

### Hikâye 8: tohum masa-0026 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0026
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'pelerin', fiil 'inanmak', sıfat 'yapraklı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: çilekleri koyacak bir sepet yoktu | pelerinini bağlayıp küçük bir çanta yaptı
@tohum: masa-0026
@degisim: inanmak -> bağlamak
Ormanda patikanın kenarında yapraklı bitkiler vardı. Maşa yaprakların altında kırmızı çilekler gördü. Onlardan reçel yapmak istedi, ama çilekleri koyacak sepeti yoktu. Maşa önce çilekleri avuçlarına doldurdu. Ama ellerine yalnız birkaç çilek sığdı. Maşa pelerinini çıkardı ve yere serdi. Çilekleri tek tek onun üstüne koydu. Pelerinini sıkıca bağladı ve küçük bir çanta yaptı. Çanta çileklerle doldu. Maşa dolu çantaya baktı ve güldü. Sonra çantayı sırtına aldı ve reçel için çileklerini mutlu mutlu taşıdı.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Maşa pelerinini çıkardı ve yere serdi"
   - Cümle 6: «Maşa pelerinini çıkardı ve yere serdi.»
   - Açıklama: Kartta Maşa'nın pelerini yok; çözüm kartta olmayan bir eşyaya dayanıyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Maşa pelerinini çıkardı"
   - Cümle 6: «Maşa pelerinini çıkardı ve yere serdi.»
   - Açıklama: Maşa dizide başörtüsü ve elbiseyle tanınır; pelerin kartta ve dizide olmayan yanlış bir görünüş bilgisi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0026` birebir aynı, `@degisim: inanmak -> bağlamak` (tutuyorsan), ardından `@onarim: 174ecfd23f4190c198106b9e979c6f90027126c2`, sonra gövde.

### Hikâye 9: tohum masa-0027 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0027
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tutkal', fiil 'katlamak', sıfat 'peynirli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: tutkal bitti ve yapraklar kağıtta durmadı | yaprakların arkasına yapışkan reçel sürdü
@tohum: masa-0027
@degisim: peynirli -> yapışkan
Ormanda Maşa kendine bir taç yapıyordu. Bir kağıdı katladı ve üstüne renkli yapraklar koymak istedi. Ama tutkal bitmişti ve yapraklar kağıtta durmuyordu. Maşa piknik sepetini açtı. İçinde bir kavanoz çilek reçeli vardı. Reçel çok yapışkandı. Maşa parmağıyla yaprakların arkasına ondan biraz sürdü. Sonra yaprakları kağıda bastırdı. Bu sefer hepsi sıkıca yapıştı. Taç çok güzel oldu ve çilek gibi kokuyordu. Maşa tacı başına taktı ve güldü. Sonra reçelli parmaklarını yaladı ve tacıyla oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Maşa piknik sepetini açtı"
   - Cümle 4: «Maşa piknik sepetini açtı.»
   - Açıklama: Daha önce hiç kurulmamış piknik sepeti çözümü getiren reçeli sebepsizce ortaya çıkarıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0027` birebir aynı, `@degisim: peynirli -> yapışkan` (tutuyorsan), ardından `@onarim: b9232da6d7e9da284dcc85dd51dd89853762ee5c`, sonra gövde.

### Hikâye 10: tohum masa-0028 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı
@tohum: masa-0028
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kova', fiil 'seyretmek', sıfat 'şaşkın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı
@plan: kovadaki fındıklar hep azalıyordu | kovayı seyretti ve küçük bir delik buldu
@tohum: masa-0028
Tepede serin bir rüzgar esiyordu. Maşa ile Koca Ayı kovaya fındık topluyordu. Ama Maşa'nın kovasında fındıklar hep azalıyordu. Maşa şaşkın bir yüzle kovasına baktı. "Fındıklarım nereye gidiyor, Koca Ayı?" diye sordu Maşa. Koca Ayı omuzlarını kaldırdı. Maşa arkasına döndü ve patikada tek tek fındıklar gördü. Sonra biraz yürüdü ve kovasını dikkatle seyretti. Kovanın altındaki küçük bir delikten bir fındık düştü! "Fındıklar bu delikten düşüyor!" dedi Maşa. Maşa deliği bir yaprakla kapatmayı denedi. Bu kez hiç fındık düşmedi. Koca Ayı yerdeki fındıkları topladı ve kovaya koydu. Maşa çok sevindi, çünkü kaybolan fındıkları bulmuştu.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kovayı seyretti ve küçük bir delik buldu"
   - Cümle 0 (plan satırı): «kovadaki fındıklar hep azalıyordu | kovayı seyretti ve küçük bir delik buldu»
   - Açıklama: Plan çözümü yalnız deliği bulmak olarak söylüyor; gövdede delik yaprakla kapatılıyor.
   - Açıklama: Plan çözümü deliği bulmak olarak veriyor ama sorunu deliği yaprakla kapatmak çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0028` birebir aynı, ardından `@onarim: 3a3c983e09d56f310e69484dc808f6cd01a66972`, sonra gövde.

### Hikâye 11: tohum masa-0030 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0030
- yer: dağ (Ormanın yanındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'gözlük', fiil 'köpürmek', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: çimenlerde bir şey parladı ama yakından görünmedi | ilk durduğu yere dönüp oradan baktı ve yürüdü
@tohum: masa-0030
@degisim: köpürmek -> parlamak
Maşa tepede kayıp pembe oyuncak gözlüğünü arıyordu. Birden uzun çimenlerin arasında bir şey parladı. Maşa hemen oraya koştu ama çimenler çok sıktı ve hiçbir şey göremedi. Maşa ilk durduğu yere döndü ve oradan bakmayı denedi. Işık yine parladı. Maşa bu kez ışığa bakarak yavaş yavaş yürüdü. Çimenlerin arasında Maşa'nın pembe gözlüğü vardı. Gözlüğün camları güneşte parlıyordu. Maşa gözlüğü eline aldı ve güldü. Maşa çok sevindi, çünkü artık oyuncaklarından hiçbiri eksik değildi.
```

**Hakem bulguları (2):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "çimenlerde bir şey parladı ama yakından görünmedi"
   - Cümle 0 (plan satırı): «çimenlerde bir şey parladı ama yakından görünmedi | ilk durduğu yere dönüp oradan baktı ve yürüdü»
   - Açıklama: Hikayenin asıl sorunu kayıp gözlük; plan bunu söylemiyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Maşa tepede kayıp pembe oyuncak gözlüğünü arıyordu"
   - Cümle 1: «Maşa tepede kayıp pembe oyuncak gözlüğünü arıyordu.»
   - Açıklama: Gözlüğün neden kaybolduğu hiç söylenmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0030` birebir aynı, `@degisim: köpürmek -> parlamak` (tutuyorsan), ardından `@onarim: 15beeb33e580d7a757fc323a9ba3dcabd59764bd`, sonra gövde.

### Hikâye 12: tohum masa-0033 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0033
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'çuval', fiil 'giydirmek', sıfat 'masmavi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: patikada nereden geldiği bilinmeyen mor lekeler vardı | çuvalın altına baktı ve delikli köşesini bağladı
@tohum: masa-0033
@degisim: giydirmek -> bağlamak
Gökyüzü masmaviydi ve ormanda kuşlar ötüyordu. Maşa patikada böğürtlen dolu bir çuval taşıyordu. Birden arkasına baktı ve patikada mor lekeler gördü. Maşa bu lekelerin nereden geldiğini çok merak etti. Önce başını kaldırıp dallara baktı. Ama dallarda mor bir şey yoktu. Maşa eğilip lekeyi kokladı. Böğürtlen reçelini çok sevdiği için bu kokuyu hemen tanıdı. Sonra çuvalını yere koydu ve altına baktı. Orada küçük bir delik vardı. Böğürtlenler bu delikten tek tek düşüp eziliyordu. Maşa çuvalın delikli köşesini sıkıca bağladı. Bu kez yere tek bir tane bile düşmedi. Maşa çok sevindi, çünkü böğürtlenlerini kurtarmıştı.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Önce başını kaldırıp dallara baktı"
   - Cümle 5: «Önce başını kaldırıp dallara baktı.»
   - Açıklama: Çözüm dallara bakma, koklama, çuvalın altına bakma ve bağlama gibi ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0033` birebir aynı, `@degisim: giydirmek -> bağlamak` (tutuyorsan), ardından `@onarim: 014202ba950de54797279d1227a93fcdf56d6f4f`, sonra gövde.
