# Editör görevi (onarım): Hayri, onarım partisi 2

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar2.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Hayri | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar2.txt --ad urun_v2`
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

## Kart: Hayri (kaynaklı, kapalı dünya)

- Ad: Hayri (okunuş: hayri; kesme eki okunuşa uyar)
- Kimlik: Hayri, mahallede arkadaşlarıyla maceralar yaşayan, yemek yemeyi çok seven bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Hayri'nin yemek sevgisi paylaşmak, beklemek ya da yemek hazırlamak olarak gösterilir; çok yiyip midesi ağrımaz, kimse onun yemesiyle ya da kilosuyla alay etmez, tanımadığı birinden yiyecek almaz.
- Özellikler:
  - acık: Yemek yemeyi çok sever; sık sık acıkır. (örnek biçimler: acıktı, acıkmıştı)
  - baklava: Mahalledeki baklava dükkanında çalışır. (örnek biçimler: baklava, baklavayı)
  - abart: Olayları abartmayı sever. (örnek biçimler: abarttı, abartarak)
- Yerler:
  - deniz: Mahallenin yakınındaki deniz kıyısı.
  - orman: Şehrin dışında, ağaçların arasındaki kamp yeri.
  - park: Mahallenin çocuk parkı.
  - ev: Mahalledeki evler, sokak ve bahçeler.
    - yan Basri Amca ise: Basri Amca'nın bahçesi; izinsiz girilmez.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Akın: Mert'in küçük kardeşi ve arkadaş grubunun en küçüğü; çok zekidir, hayvanları çok sever. Tür: oğlan; konuşur. Yüzey biçimleri: Akın
  - Mert: Akın'ın ağabeyi; sakin ve düzenlidir, tartışmaları o bitirir. Tür: oğlan; konuşur. Yüzey biçimleri: Mert
  - Kamil: Hayri'nin yakın arkadaşı; uyumayı ve kitap okumayı çok sever, mahalle bakkalına bakar. Sık sık tartışsalar da birbirlerini çok severler. Tür: oğlan; konuşur. Yüzey biçimleri: Kamil
  - Basri Amca: Mahallede yaşar; çabuk kızar ama iyi kalplidir. Bahçesine izin almadan kimsenin girmesini istemez. Tür: amca; konuşur. Yüzey biçimleri: Basri Amca, Basri, amca
  - Yumak: Basri Amca'nın köpeği; onu Akın bulmuş ve Basri Amca'ya vermiştir. Tür: köpek; KONUŞMAZ. Yüzey biçimleri: Yumak, köpek, köpeği
- Dünya kuralları:
  - Mert ile Akın kardeştir, ağabey Mert'tir; hiçbiri Hayri'nin kardeşi değildir.
  - Yumak Basri Amca'nın köpeğidir; Hayri'nin köpeği yoktur.
  - Yumak konuşmaz; havlar, koklar, kuyruğunu sallar.
- Yasak adlar: Hale, Sevim, Rüstem, Fatma Nine, Sadettin, Saadettin, Kuşçu Baba, Ozan, Nuri, Tamtam
- Yasak: Hayri'nin kız kardeşi kartta yoktur; ailesi hikayeye girmez.
- İzinli dünya kelimeleri: mahalle, baklava, bakkal, abart

## Onarılacak hikâyeler

### Hikâye 1: tohum hayri-0001 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0001
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'lamba', fiil 'zıplamak', sıfat 'neşeli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: ikisi de önce zıplamak istedi ve oyun başlamadı | sırayla zıplayıp yerlere çizgi çizdiler
@tohum: hayri-0001
Hafif bir rüzgar esiyordu. Hayri ile Mert deniz kıyısında zıplama oyunu oynuyordu. Lambaya daha yakın zıplayan kazanacaktı. Ama ikisi de önce zıplamak istiyordu ve oyun başlamadı. "Dükkanda baklavayı sırayla veririz, burada da öyle yapalım," dedi Hayri. "Tamam, önce sen zıpla," dedi Mert neşeli bir sesle. Hayri zıpladı ve Mert onun ayağının yanına bir çizgi çizdi. Sonra Mert zıpladı ve Hayri de bir çizgi çizdi. Mert'in çizgisi lambaya biraz daha yakındı. İkisi de güldü ve bir kez daha oynadı. Hayri ile Mert çok sevindi, çünkü sırayla oynamak çok eğlenceli olmuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Lambaya daha yakın zıplayan kazanacaktı"
   - Cümle 3: «Lambaya daha yakın zıplayan kazanacaktı.»
   - Açıklama: Deniz kıyısında bir lamba hiç kurulmadan sebepsizce beliriyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama ikisi de önce zıplamak istiyordu"
   - Cümle 4: «Ama ikisi de önce zıplamak istiyordu ve oyun başlamadı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0001` birebir aynı, ardından `@onarim: eb285b86296bdddc4a8583ad0255c22982de9872`, sonra gövde.

### Hikâye 2: tohum hayri-0002 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0002
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'lokma', fiil 'tamamlanmak', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: amca yemeğini evde unuttu ve acıktı | sandviçini ikiye bölüp yarısını amcaya verdi
@tohum: hayri-0002
@degisim: işaretli -> peynirli
Bir sabah Hayri deniz kıyısında Basri Amca ile kumdan kale yapıyordu. Kale sonunda tamamlandı ve ikisi de çok acıktı. Hayri peynirli sandviçini çıkardı ama Basri Amca yemeğini evde unutmuştu. Basri Amca boş çantasına üzgün üzgün baktı. Hayri sandviçine baktı ve biraz düşündü. Amcanın aç kalmasını hiç istemedi. Sonra sandviçi tam ortasından ikiye böldü. Parçalardan birini Basri Amca'ya uzattı. Basri Amca önce şaşırdı, sonra gülümsedi. İkisi kalenin önüne oturdu. Hayri her lokmayı yavaş yavaş yedi. Basri Amca da kendi parçasını bitirdi. Karınları doyunca ikisi kumda yeni bir kale yapmaya mutlu mutlu başladı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Basri Amca boş çantasına üzgün üzgün baktı"
   - Cümle 4: «Basri Amca boş çantasına üzgün üzgün baktı.»
   - Açıklama: Çanta kayboldu denmişken hemen ardından Basri Amca çantasına bakıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0002` birebir aynı, `@degisim: işaretli -> peynirli` (tutuyorsan), ardından `@onarim: 8831a331fd1dfd11102af603f3e5dc753865685c`, sonra gövde.

### Hikâye 3: tohum hayri-0003 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0003
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yün', fiil 'güzelleştirmek', sıfat 'saygılı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: rüzgar arkadaşının sandviçini kuma düşürdü | kendi sandviçini ikiye bölüp yarısını verdi
@tohum: hayri-0003
@degisim: güzelleştirmek -> bölmek
Deniz kıyısında Hayri ile Kamil yün bir örtünün üstünde oturuyordu. Birden sert bir rüzgar esti ve Kamil'in sandviçi kuma düştü. Sandviçin her yerine kum yapıştı. Kamil üzgün üzgün sandviçine baktı. Hayri de çok acıkmıştı ve elinde tek bir sandviç vardı. Ama Hayri sandviçini hemen ikiye böldü. "Kamil, yarısı senin," dedi Hayri. "Çok teşekkür ederim, Hayri," dedi Kamil saygılı bir sesle. Kamil kumlu sandviçi alıp çantasına koydu. Sonra ikisi örtünün üstünde yan yana oturup sandviçlerini yedi. Hayri çok sevindi, çünkü arkadaşı artık aç değildi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Kamil saygılı bir sesle"
   - Cümle 8: «"Çok teşekkür ederim, Hayri," dedi Kamil saygılı bir sesle.»
   - Açıklama: 'Saygılı bir sesle' soyut bir nitelik; 3 yaşındaki bir çocuk bu kelimeyi bilmeyebilir.
   - Açıklama: 'Saygılı bir ses' soyut bir nitelik, 3 yaşındaki çocuğun bileceği bir anlatım değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0003` birebir aynı, `@degisim: güzelleştirmek -> bölmek` (tutuyorsan), ardından `@onarim: fdec9cfd16e80185ae08c9b35d11ae7abd0769d1`, sonra gövde.

### Hikâye 4: tohum hayri-0004 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0004
- yer: park (Mahallenin çocuk parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fotoğraf', fiil 'sevinmek', sıfat 'ahşap'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: kutu kaybolunca köpeğe kızdı | kutuyu bankın arkasında bulup köpekten özür diledi
@tohum: hayri-0004
@degisim: fotoğraf -> kutu
Hayri parkta Yumak ile top oynuyordu. Çalıştığı baklava dükkanından getirdiği kutu ahşap bankın üstündeydi. Hayri bankın yanına döndü ama kutu yerinde yoktu. "Yumak, kutuyu sen mi aldın?" dedi Hayri kızgın bir sesle. Yumak kulaklarını indirdi ve yere oturdu. O sırada Hayri dükkanı hatırladı. Dükkanda hafif kutular rüzgarla hep yere düşerdi. Hayri bankın arkasına baktı ve kutuyu çimenlerin üstünde buldu. Kutunun kapağı sıkıca kapalıydı. Hayri, Yumak'ın kutuyu almadığını anladı. "Özür dilerim, Yumak, kutuyu sen almadın," dedi Hayri. Yumak'ın başını okşadı. Yumak sevindi ve kuyruğunu salladı. Hayri kutuyu banka geri koydu. Sonra Hayri ile Yumak top oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "kutuyu bankın arkasında bulup köpekten özür diledi"
   - Cümle 0 (plan satırı): «kutu kaybolunca köpeğe kızdı | kutuyu bankın arkasında bulup köpekten özür diledi»
   - Açıklama: Planda kutuyu Hayri buluyor ama gövdede kutuyu Yumak buluyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Dükkanda hafif kutular rüzgarla hep yere düşerdi"
   - Cümle 7: «Dükkanda hafif kutular rüzgarla hep yere düşerdi.»
   - Açıklama: Parkta rüzgar hiç anlatılmıyor; kutunun neden bankın arkasına düştüğü yalnız dükkandaki bir anıdan tahmin ediliyor.
   - Açıklama: Kutunun parkta neden düştüğü söylenmiyor; parkta rüzgar hiç esmiyor, sebep yalnız dükkandaki bir anıdan çıkarılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutunun kapağı sıkıca kapalıydı"
   - Cümle 9: «Kutunun kapağı sıkıca kapalıydı.»
   - Açıklama: Kapağın kapalı olması Yumak'ın kutuyu almadığını göstermez; Hayri'nin çıkarımı önceki olaydan çıkmıyor.
   - Açıklama: Kapağın kapalı olması Yumak'ın kutuyu almadığını göstermez; sonuç sebepsizce bu ayrıntıdan çıkarılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0004` birebir aynı, `@degisim: fotoğraf -> kutu` (tutuyorsan), ardından `@onarim: b51555f5fec8cb3ba6a9d7e53b608a7f4e1777c0`, sonra gövde.

### Hikâye 5: tohum hayri-0006 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0006
- yer: park (Mahallenin çocuk parkı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamyon', fiil 'değişmek', sıfat 'pürüzsüz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: bulut kamyona benziyordu ama rüzgarla değişiyordu | amcaya hemen bağırıp bulutu birlikte gördüler
@tohum: hayri-0006
@degisim: pürüzsüz -> ıslak
Hayri parkta ıslak çimenlerde oyuncak kamyonunu sürüyordu. Birden gökyüzünde tıpkı onun kamyonu gibi bir bulut gördü. Hayri bulutu Basri Amca'ya göstermek istedi, ama rüzgar bulutun şeklini değiştirebilirdi. Basri Amca bankta oturmuş, yere bakıyordu. Hayri kamyonunu bıraktı ve banka koştu. "Amca, bak, gökyüzünde ev kadar büyük kamyon var!" diye abartarak bağırdı Hayri. Basri Amca hemen başını kaldırdı ve bulutu gördü. "Ev kadar değil, Hayri, ama gerçekten bir kamyon!" dedi Basri Amca gülerek. İkisi bulutun tekerleklerini birlikte saydı. Az sonra rüzgar esti ve bulutun şekli değişti. "İyi ki kamyonu birlikte gördük, amca!" dedi Hayri.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "amcaya hemen bağırıp bulutu birlikte gördüler"
   - Cümle 0 (plan satırı): «bulut kamyona benziyordu ama rüzgarla değişiyordu | amcaya hemen bağırıp bulutu birlikte gördüler»
   - Açıklama: Tekil özneli 'bağırıp' ile çoğul 'gördüler' arasında özne uyumu bozuk.
   - Açıklama: '-ıp' zarf-fiilinin öznesi tekil, ana fiil 'gördüler' çoğul; özne uyumu bozuk.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama rüzgar bulutun şeklini değiştirebilirdi"
   - Cümle 3: «Hayri bulutu Basri Amca'ya göstermek istedi, ama rüzgar bulutun şeklini değiştirebilirdi.»
   - Açıklama: Sorun gerçek bir engel değil, yalnız olası bir değişiklik; Hayri'nin önünde çözülecek somut bir güçlük yok.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak bağırdı"
   - Cümle 6: «"Amca, bak, gökyüzünde ev kadar büyük kamyon var!" diye abartarak bağırdı Hayri.»
   - Açıklama: 'Abartmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abartarak bağırdı Hayri"
   - Cümle 6: «"Amca, bak, gökyüzünde ev kadar büyük kamyon var!" diye abartarak bağırdı Hayri.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0006` birebir aynı, `@degisim: pürüzsüz -> ıslak` (tutuyorsan), ardından `@onarim: 99f4b7a84eb3258ceae27a66049ebeb55f53aa08`, sonra gövde.

### Hikâye 6: tohum hayri-0008 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0008
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'çömlek', fiil 'bırakmak', sıfat 'minicik'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpeğin ipi çömleğin etrafına dolandı | çömleği kuma bırakıp ipi yavaşça çözdü
@tohum: hayri-0008
Deniz kıyısında Hayri çok acıkmıştı ve köfte dolu çömleği açtı. Tam o sırada Yumak koşup geldi ve çömleğin etrafında döndü. Yumak'ın uzun ipi çömleğin etrafına dolandı ve Yumak artık koşamadı. "Bekle, Yumak, sana yardım edeceğim," dedi Hayri. Hayri yemeden önce çömleği kuma bıraktı. Sonra ipi çömleğin etrafından yavaşça çözdü. Yumak kurtuldu ve sevinçle havladı. Yumak kuyruğunu salladı ve Hayri'nin yanına oturdu. Hayri sonunda minicik bir köfte yedi. "Yumak, artık ikimiz de mutluyuz!" dedi Hayri gülerek.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ipi çömleğin etrafına dolandı ve Yumak artık koşamadı"
   - Cümle 3: «Yumak'ın uzun ipi çömleğin etrafına dolandı ve Yumak artık koşamadı.»
   - Açıklama: 'Çömleğin etrafı' üst üste üç cümlede ve 'Yumak' aynı cümlede iki kez gereksizce tekrarlanıyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri sonunda minicik bir köfte yedi"
   - Cümle 9: «Hayri sonunda minicik bir köfte yedi.»
   - Açıklama: Çok acıkmış ve köfte dolu çömleği olan Hayri'nin sebepsizce yalnız minicik bir köfte yemesi baştaki açlıkla çelişiyor.
   - Açıklama: Hayri çok acıkmış ve çömlek köfte doluyken yalnız minicik bir köfte yemesi kurulan açlıkla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0008` birebir aynı, ardından `@onarim: d7600dec7aedab3efe3f5b1877d44f468d16d6ed`, sonra gövde.

### Hikâye 7: tohum hayri-0009 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0009
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: paylaşmak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tabure', fiil 'sallamak', sıfat 'hazır'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: arkadaşı top oynamaktan çok acıkmıştı | tabaktaki karpuzu arkadaşıyla paylaştı
@tohum: hayri-0009
Bir sabah Hayri evin önündeki tabureye bir tabak karpuz koydu. Çok acıkmıştı ve iki dilim karpuz yemeye hazırdı. O sırada Akın sokaktan el salladı. Top oynamaktan o da çok acıkmıştı. Hayri tabağa baktı ve biraz düşündü. "Akın, gel, bir dilim senin!" dedi Hayri. Akın koşup geldi ve tabureye yakın oturdu. Hayri büyük dilimi Akın'a uzattı. İkisi yan yana oturup karpuz yedi. Sonra siyah çekirdekleri tabağa koyup gülen bir yüz yaptılar. "Teşekkürler, Hayri, birlikte yemek çok güzeldi!" dedi Akın.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Top oynamaktan o da çok acıkmıştı"
   - Cümle 4: «Top oynamaktan o da çok acıkmıştı.»
   - Açıklama: Plandaki sorun (arkadaşın acıkması) ilk üç cümlede değil ancak 4. cümlede söyleniyor.
   - Açıklama: Plandaki sorun olan arkadaşın acıkması ilk üç cümlede değil dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0009` birebir aynı, ardından `@onarim: 89d6377c3ff7ac73c28f8e86a700296c18714f3b`, sonra gövde.
