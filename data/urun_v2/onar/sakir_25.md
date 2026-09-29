# Editör görevi (onarım): Şakir, onarım partisi 25

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar25.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Şakir | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar25.txt --ad urun_v2`
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

## Kart: Şakir (kaynaklı, kapalı dünya)

- Ad: Şakir (okunuş: şakir; kesme eki okunuşa uyar)
- Kimlik: Şakir, ailesiyle bir apartmanda yaşayan, okula giden yavru bir aslandır.
- Tür: aslan
- Güvenli özellik kullanımı: Şakir'in macerası güvenli bir oyun olarak kalır; yüksekten atlamaz, ateşle oynamaz, tek başına uzağa gitmez.
- Özellikler:
  - şapka: Hep şapka takar; şapkası yerden yere değişir. (örnek biçimler: şapka, şapkasını)
  - macera: Macerayı çok sever. (örnek biçimler: macera, macerayı)
- Yerler:
  - deniz: Deniz kıyısı ve kumsal.
  - orman: Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.
  - park: Şehirdeki park.
  - ev: Şakir'in ailesiyle yaşadığı apartman dairesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Remzi: Şakir'in ve Canan'ın babası; kırmızı kazak giyer, bankada çalışır, çocuk gibi eğlenir. Tür: aslan; konuşur. Yüzey biçimleri: Remzi, baba, babası, babacığım
  - Kadriye: Şakir'in ve Canan'ın annesi. Tür: kedi; konuşur. Yüzey biçimleri: Kadriye, anne, annesi, anneciğim
  - Canan: Şakir'in kız kardeşi; çok akıllıdır, kitap okumayı sever. Tür: kedi; konuşur. Yüzey biçimleri: Canan, kardeş, kardeşi
  - Necati: Remzi'nin en iyi arkadaşı; sık sık Şakir'lerin evine gelir, yemek yer ve oyun oynar. Tür: fil; konuşur. Yüzey biçimleri: Necati, Fil Necati, fil
- Dünya kuralları:
  - Remzi ve Şakir aslandır; Kadriye ve Canan beyaz kedidir; Necati mor bir fildir.
  - Necati Şakir'in akrabası değil, babasının arkadaşıdır; Şakir'in dedesi ve başka akrabası kartta yoktur.
- Yasak adlar: Peyami, Filsu, Tanju, Mirket, Kürşat, Ercan, Necmi, Cüneyt, Polat, Kumpir, Cemşit, Arif, Vedat, Refik
- Yasak: Video oyunu ve ekran başında oyun hikayeye girmez.
- İzinli dünya kelimeleri: şapka, aslan, apartman, macera, fil

## Onarılacak hikâyeler

### Hikâye 1: tohum sakir-0073 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0073
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'başörtüsü', fiil 'buluşmak', sıfat 'güneşli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: çiçek eğilmişti çünkü toprağı çok kuruydu | çeşmeden su getirip çiçeği suladı
@tohum: sakir-0073
@degisim: başörtüsü -> çiçek
Güneşli bir sabah Şakir parkta macera oyunu oynuyordu. Oyunda yere ve çalılara dikkatle bakıyordu. Birden bankın yanında küçük, sarı bir çiçek gördü. Çiçek yere doğru eğilmişti, çünkü toprağı çok kuruydu. Şakir çiçeğe su vermek istedi. Hemen yakında, iki yolun buluştuğu yerde bir çeşme vardı. Şakir çeşmeye gitti ve ellerine su doldurdu. Yavaşça yürüdü ve suyu çiçeğin dibine boşalttı. Sonra bir kez daha gidip su getirdi. Toprak ıslandı ve çiçek yavaş yavaş doğruldu. Sarı yaprakları güneşte parladı. Şakir bundan sonra parkta kuru bir çiçek görünce ona su getirirdi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "parkta macera oyunu oynuyordu"
   - Cümle 1: «Güneşli bir sabah Şakir parkta macera oyunu oynuyordu.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmeyebilir.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Çiçek yere doğru eğilmişti"
   - Cümle 4: «Çiçek yere doğru eğilmişti, çünkü toprağı çok kuruydu.»
   - Açıklama: Sorun ancak 4. cümlede söyleniyor, ilk 3 cümlede açıkça yok.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parkta kuru bir çiçek"
   - Cümle 12: «Şakir bundan sonra parkta kuru bir çiçek görünce ona su getirirdi.»
   - Açıklama: Kuru olan toprak idi; 'kuru çiçek' ölmüş çiçek anlamına gelir ve kastedilen susuz çiçek değildir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0073` birebir aynı, `@degisim: başörtüsü -> çiçek` (tutuyorsan), ardından `@onarim: 8af8a894ade56288d46e0128f8226af13b9f17db`, sonra gövde.

### Hikâye 2: tohum sakir-0075 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0075
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'cüzdan', fiil 'köpürmek', sıfat 'yeni'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: fil çok hızlı üfledi ve köpükler uçtu | ondan yavaşça üflemesini istedi ve kova köpükle doldu
@tohum: sakir-0075
@degisim: cüzdan -> kova
Ormanda kamp yerinde Şakir ile Fil Necati bir kova sabunlu suyla oynuyordu. Bu, Şakir'in yeni macera oyunuydu ve kova köpükle dolacaktı. Ama Necati hortumuyla suya çok hızlı üfledi ve köpükler havaya uçtu. Köpükler Necati'nin başına kondu ve kovada hiç köpük kalmadı. Şakir buna çok güldü. "Necati, bu kez hafifçe üfle," dedi Şakir. Necati hortumunu suya soktu ve öyle yaptı. Su yavaş yavaş köpürdü. Beyaz köpük kovanın ağzına kadar çıktı. "Bak, Şakir, kova doldu!" dedi Necati. İkisi köpüklerle oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yeni macera oyunuydu"
   - Cümle 2: «Bu, Şakir'in yeni macera oyunuydu ve kova köpükle dolacaktı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu, Şakir'in yeni macera oyunuydu"
   - Cümle 2: «Bu, Şakir'in yeni macera oyunuydu ve kova köpükle dolacaktı.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak geçiyor, olayda işe yarar biçimde kullanılmıyor.
3. **C4** (K merceği) — Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
   - Alıntı: "Şakir buna çok güldü"
   - Cümle 5: «Şakir buna çok güldü.»
   - Açıklama: Şakir arkadaşının başına gelen aksiliğe gülüyor; bu alay örnek alınabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0075` birebir aynı, `@degisim: cüzdan -> kova` (tutuyorsan), ardından `@onarim: d3bc1dc8db3b6b06b1c5a5b055246100add15299`, sonra gövde.

### Hikâye 3: tohum sakir-0076 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0076
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tost', fiil 'koşuşturmak', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: kumda büyük pati izleri vardı | izleri takip edip şemsiyenin arkasında babasını buldu
@tohum: sakir-0076
@degisim: sevecen -> neşeli
Şakir kumsalda kumdan bir kale yapıyordu. Kaleyi bitirince başını kaldırdı ve kumda büyük pati izleri gördü. Şakir bu izleri kimin yaptığını çok merak etti. Bu, onun için yeni bir macera oyunuydu ve izleri takip etti. İzler yakındaki büyük bir şemsiyenin arkasına gidiyordu. Şakir yavaşça şemsiyenin arkasına baktı. Orada babası Remzi oturuyordu ve elinde iki tost vardı. "Tost almaya gittim, o pati izleri benim," dedi Remzi neşeli bir sesle. "Demek izleri sen yaptın, baba!" dedi Şakir ve güldü. Sonra ikisi tostlarını yedi ve kumda koşuşturdu. Şakir çok sevindi, çünkü izleri kimin yaptığını bulmuştu.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kumda büyük pati izleri gördü"
   - Cümle 2: «Kaleyi bitirince başını kaldırdı ve kumda büyük pati izleri gördü.»
   - Açıklama: Pati izlerinin sebebi akla yatkın değil ve ortada çocuğun önemseyeceği gerçek bir sorun yok.
   - Açıklama: Pati izlerinin sebebi olarak bir insan gösteriliyor; sebep akla yatkın değil.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Bu, onun için yeni bir macera oyunuydu ve izleri takip etti"
   - Cümle 4: «Bu, onun için yeni bir macera oyunuydu ve izleri takip etti.»
   - Açıklama: Bağlanan iki cümlenin öznesi uyumsuz; 'Bu' izleri takip etmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "onun için yeni bir macera oyunuydu"
   - Cümle 4: «Bu, onun için yeni bir macera oyunuydu ve izleri takip etti.»
   - Açıklama: 'Macera oyunu' soyut bir kavram ve 3 yaşındaki çocuk için uygun değil.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "o pati izleri benim"
   - Cümle 8: «"Tost almaya gittim, o pati izleri benim," dedi Remzi neşeli bir sesle.»
   - Açıklama: İnsan olan babanın patisi yoktur; 'pati izi' kelimesi öznesine uymuyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "o pati izleri benim"
   - Cümle 8: «"Tost almaya gittim, o pati izleri benim," dedi Remzi neşeli bir sesle.»
   - Açıklama: Bir insan olan babanın büyük pati izleri bırakması çelişkili ve olanaksız.
   - Açıklama: Baba Remzi bir insan olarak pati izi bırakamaz; izlerin ona ait olması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0076` birebir aynı, `@degisim: sevecen -> neşeli` (tutuyorsan), ardından `@onarim: 7dd26793050ecd5cbe3412efc799392b405e9462`, sonra gövde.

### Hikâye 4: tohum sakir-0078 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0078
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'karton', fiil 'çağırmak', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: kozalaklar yolda yere döküldü ve oyun durdu | şapkasını ters çevirip kozalakları içinde taşıdı
@tohum: sakir-0078
@degisim: çağırmak -> taşımak
Şakir kamp yerinde komik bir oyun oynuyordu. Büyük bir kartona ağzı kocaman bir aslan yüzü çizmişti. Yüzün ağzı delikti ve Şakir oraya kozalak atıyordu. Ama kozalakları kucağında getirdi ve yolda hepsi yere döküldü. Şakir bir daha denedi ama kozalaklar yine düştü. Oyun durdu ve Şakir üzüldü. Sonra şapkasını çıkardı ve ters çevirdi. Kozalakları tek tek şapkanın içine koydu. Dolu şapkayı hiç düşürmeden kartonun yanına taşıdı. Şakir cömert davrandı ve en büyük kozalakları da yüzün ağzına attı. Şakir çok eğlendi, çünkü oyununa yeniden devam edebilmişti.
```

**Hakem bulguları (6):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "yolda hepsi yere döküldü"
   - Cümle 4: «Ama kozalakları kucağında getirdi ve yolda hepsi yere döküldü.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama kozalakları kucağında getirdi ve yolda hepsi yere döküldü"
   - Cümle 4: «Ama kozalakları kucağında getirdi ve yolda hepsi yere döküldü.»
   - Açıklama: Sorun ancak dördüncü cümlede söyleniyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir cömert davrandı"
   - Cümle 10: «Şakir cömert davrandı ve en büyük kozalakları da yüzün ağzına attı.»
   - Açıklama: Kozalakları kartonun ağzına atmak cömertlik değil; 'cömert' yanlış anlamda kullanılmış.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir cömert davrandı ve en büyük kozalakları"
   - Cümle 10: «Şakir cömert davrandı ve en büyük kozalakları da yüzün ağzına attı.»
   - Açıklama: Kozalakları kendi oyununda deliğe atmak cömertlik değildir; 'cömert' kelimesi yanlış anlamda kullanılmış.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir cömert davrandı"
   - Cümle 10: «Şakir cömert davrandı ve en büyük kozalakları da yüzün ağzına attı.»
   - Açıklama: Tohumdaki özellik şapka; cömertlik ikinci bir özellik olarak ekleniyor.
   - Açıklama: Tohumdaki özellik şapka; cömertlik kartın ozellikler alanında olmayan ikinci bir özellik olarak ekleniyor.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir cömert davrandı ve en büyük kozalakları"
   - Cümle 10: «Şakir cömert davrandı ve en büyük kozalakları da yüzün ağzına attı.»
   - Açıklama: Kimseyle paylaşım olmadan kozalak atmak cömertlik olarak sunuluyor; ayrıntı olaydan çıkmıyor ve anlamsız.
   - Açıklama: Tek başına oynarken kozalak atmak cömertlik değil; özellik olaydan çıkmadan eklenmiş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0078` birebir aynı, `@degisim: çağırmak -> taşımak` (tutuyorsan), ardından `@onarim: 868f303584f43549fa629ae154bf8dac605dcac5`, sonra gövde.

### Hikâye 5: tohum sakir-0079 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0079
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'yonca', fiil 'mırıldanmak', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: top kayboldu ve otların arasından ince bir ses geldi | sesin geldiği yere yürüyüp topu otların arasında buldu
@tohum: sakir-0079
Bir sabah Şakir kamp yerinde bir şarkı mırıldanıyordu. Birden durdu, çünkü küçük zilli topunu bulamadı. Şakir topunu çok seviyordu ve üzüldü. O sırada yakındaki otların arasından ince bir ses geldi. Şakir bu sesi çok merak etti. Şakir macerayı çok severdi, bu yüzden hemen otlara yürüdü. Rüzgar esti ve ses yine geldi. Şakir otları kibarca iki yana açtı. Top orada, yeşil yonca yapraklarının arasında duruyordu. Rüzgar esince top sallanıyor ve zili çalıyordu. Şakir çok sevindi, çünkü hem sesi hem de topunu bulmuştu.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük zilli topunu bulamadı"
   - Cümle 2: «Birden durdu, çünkü küçük zilli topunu bulamadı.»
   - Açıklama: Topun nasıl kaybolduğu, yani sorunun sebebi hiç söylenmiyor.
   - Açıklama: Topun neden otların arasında kaybolduğu hiç söylenmiyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bu yüzden hemen otlara yürüdü"
   - Cümle 6: «Şakir macerayı çok severdi, bu yüzden hemen otlara yürüdü.»
   - Açıklama: Şakir yanında büyük olmadan kamp yerinde bilinmeyen bir sese doğru yürüyor; güvenli kullanım satırı tek başına gitmeyi yasaklıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 6: «Şakir macerayı çok severdi, bu yüzden hemen otlara yürüdü.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir otları kibarca iki"
   - Cümle 8: «Şakir otları kibarca iki yana açtı.»
   - Açıklama: Otlara karşı kibar olunmaz; 'kibarca' kelimesi nesnesine uymuyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir otları kibarca iki yana açtı"
   - Cümle 8: «Şakir otları kibarca iki yana açtı.»
   - Açıklama: 'Kibarca' insanlara davranış için kullanılır, otları açmaya uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0079` birebir aynı, ardından `@onarim: 7ad15377eb5cd3d54edd5e4be8bac7c7490a08b2`, sonra gövde.

### Hikâye 6: tohum sakir-0080 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0080
- yer: park (Şehirdeki park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'odun', fiil 'sevinmek', sıfat 'ışıltılı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: annesinin anahtarı düştü ve güneş gözüne geliyordu | şapkasını öne çekip anahtarı odunların arasında buldu
@tohum: sakir-0080
Parkta Şakir ile annesi Kadriye yürüyordu. Kadriye bir odun yığınının yanında ev anahtarını düşürmüştü. Şakir odunların arasında ışıltılı bir şey gördü. Ama güneş gözüne geliyordu ve Şakir onu iyi göremedi. "Anneciğim, odunların arasında bir şey parlıyor," dedi Şakir. "Bir bakalım, Şakir, belki anahtarımdır," dedi Kadriye. Şakir şapkasını gözlerinin üstüne doğru çekti. Artık güneş gözüne gelmiyordu. Şakir odunlara yaklaştı ve baktı. Parlayan şey annesinin anahtarıydı! Şakir anahtarı aldı ve annesine verdi. Kadriye anahtarını görünce çok sevindi. Sonra ikisi el ele mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "annesinin anahtarı düştü ve güneş gözüne geliyordu"
   - Cümle 0 (plan satırı): «annesinin anahtarı düştü ve güneş gözüne geliyordu | şapkasını öne çekip anahtarı odunların arasında buldu»
   - Açıklama: Plan ve gövde iki ayrı sorun taşıyor: düşen anahtar ve göze gelen güneş.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ev anahtarını düşürmüştü"
   - Cümle 2: «Kadriye bir odun yığınının yanında ev anahtarını düşürmüştü.»
   - Açıklama: Anahtarın neden düştüğü söylenmiyor ve Kadriye kaybını fark etmemiş görünüyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ışıltılı bir şey gördü"
   - Cümle 3: «Şakir odunların arasında ışıltılı bir şey gördü.»
   - Açıklama: 'Işıltılı' kelimesi 3 yaşındaki bir çocuğun bildiği bir kelime değil; 'parlak' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0080` birebir aynı, ardından `@onarim: 23d14556a0c079ad132cef70553b9ce67f4c48c8`, sonra gövde.

### Hikâye 7: tohum sakir-0081 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0081
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kazak', fiil 'ilgilenmek', sıfat 'gizli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: rüzgar kuru kumu savurdu ve kule yıkıldı | kardeşinden yardım isteyip ıslak kumla kule yaptı
@tohum: sakir-0081
Rüzgar esiyordu. Şakir ile kardeşi Canan kazaklarını giymiş, kumsalda oturuyordu. Şakir kuru kumdan bir kule yaptı ama rüzgar onu yıktı. Canan yanında kitap okuyordu. "Canan, bana yardım eder misin?" diye sordu Şakir. Canan kitabını kapattı ve kardeşiyle ilgilendi. "Sana gizli bir şey söyleyeyim, ıslak kum rüzgarda yıkılmaz," dedi Canan. Şakir su kenarına gitti ve şapkasını ıslak kumla doldurdu. Sonra şapkayı kulenin olduğu yere taşıdı ve kumu sıkıca bastırdı. Bu kez rüzgar kuleyi yıkamadı. "Teşekkürler, Canan, kulem artık çok sağlam!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve kardeşiyle ilgilendi"
   - Cümle 6: «Canan kitabını kapattı ve kardeşiyle ilgilendi.»
   - Açıklama: 'İlgilenmek' soyut, 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sana gizli bir şey söyleyeyim"
   - Cümle 7: «"Sana gizli bir şey söyleyeyim, ıslak kum rüzgarda yıkılmaz," dedi Canan.»
   - Açıklama: Söylenen bilgi gizli değil; 'gizli' yanlış anlamda.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir su kenarına gitti"
   - Cümle 8: «Şakir su kenarına gitti ve şapkasını ıslak kumla doldurdu.»
   - Açıklama: Kartın güvenli kullanım satırına aykırı olarak iki küçük çocuk yetişkinsiz kumsalda ve Şakir tek başına su kenarına gidiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0081` birebir aynı, ardından `@onarim: d3bad016a09c3b7c6067b334db397d996b20e765`, sonra gövde.

### Hikâye 8: tohum sakir-0082 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0082
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bilezik', fiil 'saçmak', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: yuvarlak boncuklar masadan yere yuvarlandı | boncukları ters çevrilmiş şapkasının içine koydu
@tohum: sakir-0082
@degisim: gizemli -> yuvarlak
Şakir evde ilk kez bir bilezik yapmayı denedi. Renklerini görmek için boncukları masaya saçtı ve uzun bir ip aldı. Ama yuvarlak boncuklar masanın kenarına kaydı ve yere düştü. Şakir boncukları yerden tek tek topladı. Sonra biraz düşündü. Başındaki şapkayı çıkardı ve ters çevirdi. Bütün boncukları şapkanın içine koydu. Artık hiçbir boncuk yere düşmedi. Şakir şapkadan birer boncuk aldı ve ipe geçirdi. Önce kırmızı, sonra sarı, sonra mavi boncuk seçti. Bilezik yavaş yavaş uzadı. Şakir ipin iki ucunu sıkıca bağladı. Sonra yeni bileziğini koluna taktı ve sevinçle odada dans etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir şapkadan birer boncuk aldı"
   - Cümle 9: «Şakir şapkadan birer boncuk aldı ve ipe geçirdi.»
   - Açıklama: 'Birer' her birine bir anlamına gelir; burada 'teker teker' ya da 'bir bir' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0082` birebir aynı, `@degisim: gizemli -> yuvarlak` (tutuyorsan), ardından `@onarim: c5b8534a56fd4b0fee0ddfcf38dea010109885d6`, sonra gövde.

### Hikâye 9: tohum sakir-0083 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0083
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: sırayla oynamak
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'pul', fiil 'eşleştirmek', sıfat 'güzel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: ikisi de aynı anda aynı pulu tuttu | sırası gelenin önce tur attığı bir oyun kurdu
@tohum: sakir-0083
Yağmur cama vuruyordu. Şakir ile annesi Kadriye evde pul eşleştirme oyunu oynuyordu. Ama ikisi de aynı anda aynı pulu tuttu ve oyun durdu. Şakir oyunun devam etmesini istedi. Biraz düşündü. "Anneciğim, sırası gelen önce odada bir macera turu atsın," dedi Şakir. Kadriye güldü ve başını salladı. Önce Kadriye tur attı ve iki gemi pulunu buldu. Sonra sıra Şakir'e geçti. Şakir de tur attı ve iki güzel çiçek pulunu eşleştirdi. "Aferin, Şakir!" dedi Kadriye. İkisi sırayla oynadı ve bütün pullar eşini buldu. Şakir çok sevindi, çünkü oyun artık hiç durmadı.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "odada bir macera turu atsın"
   - Cümle 6: «"Anneciğim, sırası gelen önce odada bir macera turu atsın," dedi Şakir.»
   - Açıklama: 'Macera turu' soyut ve 3 yaşındaki çocuğun bilmeyeceği bir ifade.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sırası gelen önce odada bir macera turu atsın"
   - Cümle 6: «"Anneciğim, sırası gelen önce odada bir macera turu atsın," dedi Şakir.»
   - Açıklama: Aynı pulu tutma sorununa sıra yeterliyken çözüme sebeple ilgisiz bir oda turu adımı ekleniyor.
   - Açıklama: Çözüm sırayla oynamak olabilirken araya sebeple ilgisiz bir oda turu adımı ekleniyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Önce Kadriye tur attı ve iki gemi pulunu buldu"
   - Cümle 8: «Önce Kadriye tur attı ve iki gemi pulunu buldu.»
   - Açıklama: Macera turu pulların eşleşmesiyle bağlantısız, işlevsiz bir ayrıntı ve pulları sebepsizce bulduruyor.
   - Açıklama: Masadaki eşleştirme oyununda pulların oda turuyla bulunması sebepsiz ve olaydan çıkmıyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bütün pullar eşini buldu"
   - Cümle 12: «İkisi sırayla oynadı ve bütün pullar eşini buldu.»
   - Açıklama: Pullar bir şey bulamaz; fiil öznesine uymuyor, mecazlı kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0083` birebir aynı, ardından `@onarim: 4cd9a0446eac41a58b215da290ea0c0a6d464d5a`, sonra gövde.

### Hikâye 10: tohum sakir-0084 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0084
- yer: park (Şehirdeki park.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'küp', fiil 'koşmak', sıfat 'garip'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: kutlama için yanında hiç ödül yoktu | şapkasını ödül olarak filin başına koydu
@tohum: sakir-0084
Bir sabah Şakir ile Necati parktaydı. Necati parkta ilk kez hiç durmadan koştu. Şakir onun için küçük bir kutlama yapmak istedi. Ama yanında hiç ödül yoktu. Şakir etrafa baktı ve alçak bir taş küp gördü. "Necati, küpün üstüne otur," dedi Şakir. Necati şaşırdı ama küpün üstüne oturdu. Şakir şapkasını çıkardı. Şapkayı Necati'nin kocaman başına koydu. Küçük şapka filin başında çok garip durdu. İkisi de çok güldü. "Bu senin ödül şapkan, Necati!" dedi Şakir. "Teşekkürler, Şakir, bu çok güzel bir kutlama!" dedi Necati. Sonra ikisi yan yana parkta mutlu mutlu yürüdü.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Şakir onun için küçük bir kutlama yapmak istedi.»
   - Açıklama: Asıl sorun olan ödül yokluğu ancak 4. cümlede söyleniyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Küçük şapka filin başında"
   - Cümle 10: «Küçük şapka filin başında çok garip durdu.»
   - Açıklama: Necati'nin fil olduğu hiç söylenmeden 'filin' deniyor; kimi gösterdiği belli değil.
   - Açıklama: Necati'nin fil olduğu hiç söylenmeden 'filin' deniyor; kimi gösterdiği belirsiz.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Küçük şapka filin başında çok garip durdu"
   - Cümle 10: «Küçük şapka filin başında çok garip durdu.»
   - Açıklama: Necati'nin fil olduğu hiç kurulmadan 'fil' sebepsizce beliriyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Küçük şapka filin başında"
   - Cümle 10: «Küçük şapka filin başında çok garip durdu.»
   - Açıklama: Necati'nin fil olduğu hiç kurulmadan 'fil' sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0084` birebir aynı, ardından `@onarim: eab4eddf51ebfde18cf9490319ece0a223db0fcb`, sonra gövde.

### Hikâye 11: tohum sakir-0085 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0085
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kumbara', fiil 'geçmek', sıfat 'kirli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: hazineye giden yolda büyük bir çamur birikintisi vardı | düz taşları çamura koyup karşıya geçti
@tohum: sakir-0085
@degisim: kumbara -> kutu
Şakir ile babası Remzi ormandaki kamp yerinde hazine oyunu oynuyordu. Remzi büyük bir ağacın dibine bir hazine kutusu saklamıştı. Ama ağaca giden yolda büyük bir çamur birikintisi vardı. Şakir çamurdan geçerse ayakları kirli olacaktı. Çamurun kenarında düz taşlar gördü. Şakir bir macera yolu yapmak için taşları tek tek topladı. Sonra taşları çamurun içine sıra sıra dizdi. Taşların üstüne basarak karşıya geçti. Remzi de onun arkasından geldi. Şakir ağacın dibinde hazine kutusunu buldu. Kutuyu açtı ve içinde iki kurabiye gördü. Kurabiyelerden birini babasına verdi. Sonra ikisi ağacın dibine oturdu ve kurabiyelerini mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ağaca giden yolda büyük bir çamur birikintisi vardı"
   - Cümle 3: «Ama ağaca giden yolda büyük bir çamur birikintisi vardı.»
   - Açıklama: Çamur birikintisinin neden orada olduğu söylenmiyor; sorunun sebebi verilmiyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir macera yolu yapmak"
   - Cümle 6: «Şakir bir macera yolu yapmak için taşları tek tek topladı.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0085` birebir aynı, `@degisim: kumbara -> kutu` (tutuyorsan), ardından `@onarim: c754c7285e393435bccd0c27b4b146fb378b88ff`, sonra gövde.

### Hikâye 12: tohum sakir-0086 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0086
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kumaş', fiil 'çiğnemek', sıfat 'paslı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: güneş çok parlaktı ve kardeşi okuyamadı | kumaştan gölgeli küçük bir çadır kurdu
@tohum: sakir-0086
@degisim: çiğnemek -> okumak
Ormandaki kamp yerinde Şakir ile kardeşi Canan vardı. Canan paslı bir sandalyede kitap okumak istedi. Ama güneş çok parlaktı ve Canan yazıları göremedi. Şakir sırtına pelerin gibi geniş bir kumaş takmıştı. Şakir kumaşı kardeşiyle paylaşmak istedi. Kumaşı sırtından çıkardı. İki ucunu iki alçak dala sıkıca bağladı. Böylece sandalyenin üstüne küçük bir macera çadırı kurdu. Çadırın altı gölge ve serin oldu. Canan kitabını rahatça okudu. Şakir de gölgeye geldi ve kardeşinin yanına oturdu. İkisi kitaptaki resimlere birlikte baktı. Şakir bundan sonra pelerinini Canan'la hep paylaştı.
```

**Hakem bulguları (6):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Şakir sırtına pelerin gibi geniş bir kumaş takmıştı"
   - Cümle 4: «Şakir sırtına pelerin gibi geniş bir kumaş takmıştı.»
   - Açıklama: Kartta Şakir'in pelerini yok; kart yalnız şapkasını tanımlıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir sırtına pelerin gibi geniş bir kumaş takmıştı"
   - Cümle 4: «Şakir sırtına pelerin gibi geniş bir kumaş takmıştı.»
   - Açıklama: Kumaş daha önce kurulmadan tam çözüm gerektiğinde sebepsizce beliriyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük bir macera çadırı"
   - Cümle 8: «Böylece sandalyenin üstüne küçük bir macera çadırı kurdu.»
   - Açıklama: 'Macera' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "küçük bir macera çadırı kurdu"
   - Cümle 8: «Böylece sandalyenin üstüne küçük bir macera çadırı kurdu.»
   - Açıklama: Tohumdaki macera özelliği yalnız süs sıfatı olarak geçiyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Macera özelliği çadıra yapıştırılmış bir sözcük olarak geçiyor, çözümde işe yaramıyor.
5. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Şakir bundan sonra pelerinini Canan'la hep paylaştı"
   - Cümle 13: «Şakir bundan sonra pelerinini Canan'la hep paylaştı.»
   - Açıklama: Kartta olmayan pelerin Şakir'in kalıcı eşyası gibi sunuluyor.
6. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "pelerinini Canan'la hep paylaştı"
   - Cümle 13: «Şakir bundan sonra pelerinini Canan'la hep paylaştı.»
   - Açıklama: Kartın özelliklerinde Şakir'in şapkası var; pelerin kartta olmayan bir eşya olarak figüre ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0086` birebir aynı, `@degisim: çiğnemek -> okumak` (tutuyorsan), ardından `@onarim: 3d51698e2b43202863ed9b40825c36d4899b3afe`, sonra gövde.
