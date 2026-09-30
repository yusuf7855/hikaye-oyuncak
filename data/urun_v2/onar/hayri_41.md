# Editör görevi (onarım): Hayri, onarım partisi 41

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar41.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar41.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0138 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0138
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'hortum', fiil 'soğumak', sıfat 'esnek'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: tek kova vardı ve ikisi de aynı anda istedi | sırayı arkadaşına verip önce sandviçini yedi
@tohum: hayri-0138
@degisim: hortum -> kova
Hayri ile Akın deniz kıyısında kumda bir havuz kazdı. Kum güneşte çok sıcaktı. Ama yalnız bir kova vardı. İkisi de kovayı aynı anda çekti. Kovanın esnek kulpu iki yana büküldü. Hayri kulp kopmasın diye kovayı bıraktı. Hayri çok acıkmıştı ve çantasında sandviç vardı. "Akın, sen önce su taşı, ben de sandviçimi yerim," dedi Hayri. Akın sevindi ve kovayla denizden su getirdi. Hayri sandviçini yedi ve Akın'ı izledi. "Sıra sende, Hayri," dedi Akın ve kovayı ona verdi. Hayri de havuza su döktü. Havuz dolunca sıcak kum da soğudu. Sonra Hayri ile Akın sırayla su taşımaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kovanın esnek kulpu iki yana büküldü"
   - Cümle 5: «Kovanın esnek kulpu iki yana büküldü.»
   - Açıklama: 'Esnek' kelimesi 3 yaşındaki bir çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kovanın esnek kulpu iki"
   - Cümle 5: «Kovanın esnek kulpu iki yana büküldü.»
   - Açıklama: 'Esnek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Havuz dolunca sıcak kum da soğudu"
   - Cümle 13: «Havuz dolunca sıcak kum da soğudu.»
   - Açıklama: Kumun sıcaklığı sorunla ilgisiz kurulup sonunda sebepsizce çözülmüş gibi anılan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0138` birebir aynı, `@degisim: hortum -> kova` (tutuyorsan), ardından `@onarim: e875da78b539416989f59eeb99678f13ee79b341`, sonra gövde.

### Hikâye 2: tohum hayri-0140 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0140
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'erik', fiil 'sarılmak', sıfat 'değerli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: küçük kalp yukarıdaki banktan görünmüyordu | kumun üstüne kocaman bir kalp çizdi
@tohum: hayri-0140
Hayri deniz kıyısında Basri Amca'nın doğum günü için sürpriz hazırlıyordu. Kumun üstüne bir kalp çizmişti ama kalp çok küçüktü. Basri Amca yukarıdaki bankta oturuyordu ve küçük kalbi oradan göremezdi. "Bu kez denizden büyük bir kalp çizeceğim!" diye abarttı Hayri. Sonra kumun üstüne kocaman bir kalp çizdi. Ortasına da getirdiği bir sepet eriği koydu. "Basri Amca, aşağı bak!" diye seslendi Hayri. Basri Amca kocaman kalbi gördü ve Hayri'nin yanına geldi. Ona sıkıca sarıldı. "Bu sürpriz benim için çok değerli," dedi Basri Amca. Sonra Hayri ile Basri Amca kıyıya oturup erikleri mutlu mutlu yediler.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "diye abarttı Hayri"
   - Cümle 4: «"Bu kez denizden büyük bir kalp çizeceğim!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' konuşma fiili olarak yanlış ve soyut kullanılmış.
   - Açıklama: 'Abarttı' söyleme fiili yerine yanlış kullanılmış.
2. **D5** (D merceği) — Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 4: «"Bu kez denizden büyük bir kalp çizeceğim!" diye abarttı Hayri.»
   - Açıklama: Hayri yanında kimse yokken kendi kendine konuşuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 4: «"Bu kez denizden büyük bir kalp çizeceğim!" diye abarttı Hayri.»
   - Açıklama: 'Abarttı' konuşma fiili olarak soyut ve 3 yaşındaki çocuğun bileceği bir kelime değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "denizden büyük bir kalp"
   - Cümle 4: «"Bu kez denizden büyük bir kalp çizeceğim!" diye abarttı Hayri.»
   - Açıklama: 'Denizden büyük' abartılı bir mecaz, çocuğa uygun değil.
   - Açıklama: 'Denizden büyük' abartılı mecaz bir anlatım.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "benim için çok değerli"
   - Cümle 10: «"Bu sürpriz benim için çok değerli," dedi Basri Amca.»
   - Açıklama: 'Değerli' soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0140` birebir aynı, ardından `@onarim: f5da0b377b4a3b4cb1a7ed050666ec900c6b29fc`, sonra gövde.

### Hikâye 3: tohum hayri-0141 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0141
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: kaybolan eşya
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'sofra', fiil 'durdurmak', sıfat 'konuşkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: baklava kutusu yolda sepetten düşüp kaybolmuştu | köpekten yardım isteyip kutuyu birlikte buldu
@tohum: hayri-0141
@degisim: konuşkan -> tatlı
Hayri kamp yerinde bir sofra kuruyordu. Çalıştığı baklava dükkanından bir kutu tatlı baklava getirmişti. Ama kutu yolda sepetten düşüp kaybolmuştu. Yumak da yanında zıplıyordu. Hayri onu nazikçe durdurdu. Dükkanda çalıştığı için Hayri'nin elleri baklava kokuyordu. Ellerini Yumak'ın burnuna uzattı. "Yumak, bu kokuyu bulabilir misin?" diye sordu Hayri. Yumak elleri kokladı ve ağaçların arasına koştu. Bir çalının yanında durdu ve havladı. Kutu çalının altındaydı! Hayri kutuyu alıp sofranın ortasına koydu. "Teşekkürler, Yumak, baklavayı birlikte bulduk!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Dükkanda çalıştığı için Hayri'nin"
   - Cümle 6: «Dükkanda çalıştığı için Hayri'nin elleri baklava kokuyordu.»
   - Açıklama: Hayri'nin dükkanda çalıştığı 2. cümlede söylendiği halde gereksizce tekrarlanıyor.
   - Açıklama: Hayri'nin dükkanda çalıştığı bilgisi 2. cümleden sonra gereksiz yere tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0141` birebir aynı, `@degisim: konuşkan -> tatlı` (tutuyorsan), ardından `@onarim: 3f4af4d34735f1762399ad7f6228b244605218d5`, sonra gövde.

### Hikâye 4: tohum hayri-0142 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0142
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'jöle', fiil 'ovuşturmak', sıfat 'uzun'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: soğuk parmaklarıyla arkadaşı kabın kapağını açamadı | ellerini hızlı hızlı ovuşturdu ve ona da gösterdi
@tohum: hayri-0142
Bir sabah Hayri ile Akın kamp yerindeydi ve hava çok serindi. Akın küçük bir jöle kabını açmak istedi. Ama parmakları soğuktu ve kapağı sıkıca tutamadı. Hayri bunu gördü ve arkadaşına yardım etmek istedi. "Akın, ellerini böyle ısıt," dedi Hayri. Hayri ellerini çok hızlı ve uzun uzun ovuşturdu. "Bak, ellerim güneş kadar sıcak oldu!" diye abarttı Hayri. Akın güldü ve o da aynısını yaptı. Parmakları hemen ısındı. Akın kapağı kolayca açtı. "Teşekkürler, Hayri, sen de biraz jöle ister misin?" diye sordu Akın. Hayri çok sevindi, çünkü arkadaşına yardım edebilmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ellerim güneş kadar sıcak oldu"
   - Cümle 7: «"Bak, ellerim güneş kadar sıcak oldu!" diye abarttı Hayri.»
   - Açıklama: Abartılı benzetme mecazdır ve küçük çocuk için uygun değil.
   - Açıklama: Benzetme ve 'abarttı' kelimesi 3 yaşındaki çocuk için soyut.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Akın kapağı kolayca açtı"
   - Cümle 10: «Akın kapağı kolayca açtı.»
   - Açıklama: Sorun yan karakter Akın'ın sorunu ve kapağı da Akın açıyor; figür Hayri yalnız yol gösteriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0142` birebir aynı, ardından `@onarim: 52d9e737cf5b5654b1ddb7975d02a1aed28ea053`, sonra gövde.

### Hikâye 5: tohum hayri-0143 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0143
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çember', fiil 'yaklaştırmak', sıfat 'güçlü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: çember belinde dönmüyordu ve hemen yere düşüyordu | belini güçlü ve hızlı hareketlerle salladı
@tohum: hayri-0143
Deniz kıyısında güneş parlıyordu. Hayri kumda ilk kez çember çevirmeyi deniyordu. Ama çember her seferinde düştü, çünkü Hayri belini çok yavaş sallıyordu. Hayri çemberi yerden aldı. Hayri abarttı ve çember yüz kez dönecek diye düşündü. Çemberi iki eliyle beline yaklaştırdı. Sonra belini güçlü ve hızlı hareketlerle salladı. Çember belinde bir kez, iki kez, üç kez döndü! Hayri durmadı ve saymaya devam etti. Çember tam on kez dönüp kuma indi. Hayri güldü ve ellerini çırptı. Hayri çok sevindi, çünkü yeni oyunu sonunda öğrenmişti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve çember"
   - Cümle 5: «Hayri abarttı ve çember yüz kez dönecek diye düşündü.»
   - Açıklama: 'Abartmak' soyut bir kavram ve burada anlamı belirsiz kullanılmış.
   - Açıklama: 'Abarttı' soyut ve burada anlamı belirsiz, 3 yaşındaki çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abarttı ve çember yüz kez dönecek diye düşündü"
   - Cümle 5: «Hayri abarttı ve çember yüz kez dönecek diye düşündü.»
   - Açıklama: Tohumdaki abartma özelliği çözüme hiçbir katkı yapmıyor, sorunu belini hızlı sallamak çözüyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abarttı ve çember yüz kez dönecek"
   - Cümle 5: «Hayri abarttı ve çember yüz kez dönecek diye düşündü.»
   - Açıklama: Abartma özelliği yalnız bir düşünce olarak geçiyor, çemberin dönmesine işe yarar bir katkısı yok.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abarttı ve çember yüz kez dönecek diye düşündü"
   - Cümle 5: «Hayri abarttı ve çember yüz kez dönecek diye düşündü.»
   - Açıklama: Abartma düşüncesi olaya hiçbir şey katmayan, sonra kullanılmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0143` birebir aynı, ardından `@onarim: 27db159ac772fdd2e28a2462b5eacabef8a361de`, sonra gövde.

### Hikâye 6: tohum hayri-0144 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0144
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'araba', fiil 'çözülmek', sıfat 'havalı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: tozlu yolda nereden geldiği bilinmeyen ince izler vardı | çalıya gitti ve altında arabasını buldu
@tohum: hayri-0144
@degisim: havalı -> mavi
Bir sabah Hayri çok acıkmıştı ve çantasını bıraktığı banka döndü. Bankın yanındaki tozlu yolda ince izler gördü. İzler yokuş aşağı bir çalıya gidiyordu. Hayri bu izleri neyin yaptığını çok merak etti. Sandviçini hemen yemedi ve çalıya doğru yürüdü. Çalının altında mavi oyuncak arabasını buldu. Arabanın ipi boştu, çünkü düğüm çözülmüştü. Araba tekerlekleriyle yokuş aşağı inmiş ve izleri yapmıştı. Hayri arabayı çantasına sıkıca yeniden bağladı. Sonra banka oturdu ve sandviçini yedi. Hayri çok sevindi, çünkü izleri neyin yaptığını bulmuştu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bankın yanındaki tozlu yolda ince izler gördü"
   - Cümle 2: «Bankın yanındaki tozlu yolda ince izler gördü.»
   - Açıklama: Sorun yalnız bir merak; Hayri arabasının kaybolduğunu bilmiyor, çocuğun önemseyeceği açık bir sorun kurulmuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sandviçini hemen yemedi ve çalıya doğru yürüdü"
   - Cümle 5: «Sandviçini hemen yemedi ve çalıya doğru yürüdü.»
   - Açıklama: Tohumdaki acıkma özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0144` birebir aynı, `@degisim: havalı -> mavi` (tutuyorsan), ardından `@onarim: bfc8cc4bb70db3ee6545cf7e8ab58139c684ca65`, sonra gövde.

### Hikâye 7: tohum hayri-0146 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0146
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: paylaşmak
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'küpe', fiil 'seçmek', sıfat 'kırılgan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: arkadaşının kovası boştu ve kabuk almak istemedi | kovada yüz kabuk var dedi ve paylaştı
@tohum: hayri-0146
@degisim: küpe -> kabuk
Bir sabah Hayri ile Kamil deniz kıyısında oturuyordu. Hayri kumdan renkli kabuklar toplamış ve kovasını doldurmuştu. Kamil ise kitap okumuştu ve hiç kabuk toplamadı. Kamil boş kovasına üzgün üzgün baktı. Hayri kendi kovasını Kamil'e uzattı ve istediğini almasını söyledi. Ama Kamil almak istemedi, çünkü o zaman Hayri'nin kabukları az kalacaktı. Hayri abartarak kovada tam yüz kabuk olduğunu söyledi. Kamil buna çok güldü ve kovaya elini uzattı. Kabuklar ince ve kırılgandı. Kamil onları yavaşça tuttu ve en güzel üç tanesini seçti. Sonra onları kendi kovasına dikkatle koydu. Hayri de Kamil de çok sevindi, çünkü ikisinin de kabukları vardı.
```

**Hakem bulguları (7):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "kovada yüz kabuk var dedi"
   - Cümle 0 (plan satırı): «arkadaşının kovası boştu ve kabuk almak istemedi | kovada yüz kabuk var dedi ve paylaştı»
   - Açıklama: Aktarılan söz tırnaksız ve noktalamasız yazılmış.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kitap okumuştu ve hiç kabuk toplamadı"
   - Cümle 3: «Kamil ise kitap okumuştu ve hiç kabuk toplamadı.»
   - Açıklama: Bağlanan fiillerin kipi uyumsuz; 'toplamamıştı' olmalı.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "okumuştu ve hiç kabuk toplamadı"
   - Cümle 3: «Kamil ise kitap okumuştu ve hiç kabuk toplamadı.»
   - Açıklama: 'okumuştu' ile 'toplamadı' arasında zaman kayıyor; 'toplamamıştı' olmalı.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Kamil ise kitap okumuştu ve hiç kabuk toplamadı.»
   - Açıklama: Asıl sorun olan Kamil'in kabuk almak istememesi ilk üç cümlede değil ancak altıncı cümlede söyleniyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kovada tam"
   - Cümle 7: «Hayri abartarak kovada tam yüz kabuk olduğunu söyledi.»
   - Açıklama: 'abartarak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
6. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak kovada"
   - Cümle 7: «Hayri abartarak kovada tam yüz kabuk olduğunu söyledi.»
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri abartarak kovada tam yüz kabuk olduğunu söyledi"
   - Cümle 7: «Hayri abartarak kovada tam yüz kabuk olduğunu söyledi.»
   - Açıklama: Abartılı bir sayı söylemek Kamil'in kabukların azalacağı kaygısını gerçekten gidermiyor; çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0146` birebir aynı, `@degisim: küpe -> kabuk` (tutuyorsan), ardından `@onarim: c412a62e24a108caa7f6459e37e3cc55ed8b7af5`, sonra gövde.

### Hikâye 8: tohum hayri-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0147
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fıskiye', fiil 'parlamak', sıfat 'gizemli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: sormadan amcanın kutusunu açtı ve amca kızdı | özür diledi ve dükkandan getirdiği baklavayı paylaştı
@tohum: hayri-0147
@degisim: fıskiye -> kutu
Rüzgar ağaçların arasında serin serin esiyordu. Hayri ile Basri Amca ormandaki kamp yerindeydi. Basri Amca'nın çantasının yanında küçük, gizemli bir kutu duruyordu. Hayri çok merak etti ve kutuyu sormadan açtı. İçinde güneşte parlayan renkli taşlar vardı. Basri Amca bunu görünce kızdı, çünkü Hayri izin istememişti. Hayri kutuyu hemen kapattı ve Basri Amca'dan özür diledi. Sonra çantasından bir paket baklava çıkardı. Hayri bu baklavayı sabah çalıştığı dükkandan getirmişti. Hayri baklavayı Basri Amca ile paylaştı. Basri Amca bir dilim yedi ve gülümsedi. Sonra kutuyu kendisi açtı ve taşları Hayri'ye tek tek gösterdi. Hayri çok rahatladı, çünkü Basri Amca artık ona kızgın değildi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "küçük, gizemli bir kutu"
   - Cümle 3: «Basri Amca'nın çantasının yanında küçük, gizemli bir kutu duruyordu.»
   - Açıklama: 'Gizemli' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Gizemli' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Basri Amca'nın çantasının yanında küçük, gizemli bir kutu duruyordu.»
   - Açıklama: Kutunun izinsiz açılıp amcanın kızması ilk üç cümlede değil, 4. ve 6. cümlelerde geliyor.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Hayri çok merak etti ve kutuyu sormadan açtı"
   - Cümle 4: «Hayri çok merak etti ve kutuyu sormadan açtı.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak 4. ve 6. cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0147` birebir aynı, `@degisim: fıskiye -> kutu` (tutuyorsan), ardından `@onarim: 93804a694a8d30bc0f774bbe5a029905927f3720`, sonra gövde.

### Hikâye 9: tohum hayri-0149 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0149
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'patates', fiil 'dolaşmak', sıfat 'kibar'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar kumu savurdu ve küçük patates resmi kayboldu | kocaman ve derin bir patates çizdi
@tohum: hayri-0149
@degisim: kibar -> kocaman
Bir sabah Hayri deniz kıyısında bir çubukla kuma bıyıklı bir patates çizdi. Patates küçüktü ve çizgileri çok inceydi. Ama rüzgar kumu savurdu ve ince çizgiler kapandı. Komik patates hemen kayboldu. Hayri elindeki çubuğa baktı ve biraz düşündü. Sonra bu kez her şeyi abartarak yeniden başladı. Kumda ayaklarıyla büyük bir daire çizerek dolaştı. Daireye iki kocaman göz ve çok uzun bir bıyık ekledi. Çizgiler bu kez hem geniş hem de derindi. Rüzgar yine esti ama büyük patates kaybolmadı. Hayri patatesin ortasına oturdu ve mutlu mutlu güldü.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kocaman ve derin bir patates çizdi"
   - Cümle 0 (plan satırı): «rüzgar kumu savurdu ve küçük patates resmi kayboldu | kocaman ve derin bir patates çizdi»
   - Açıklama: Patates derin olmaz; 'derin' kelimesi nesnesine uymuyor.
   - Açıklama: Derin olan çizgilerdir, patates resmi 'derin' olamaz; sıfat yanlış ada bağlanmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "her şeyi abartarak yeniden"
   - Cümle 6: «Sonra bu kez her şeyi abartarak yeniden başladı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "her şeyi abartarak yeniden başladı"
   - Cümle 6: «Sonra bu kez her şeyi abartarak yeniden başladı.»
   - Açıklama: 'Abartarak' soyut bir kelimedir ve 3 yaşındaki çocuk bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "her şeyi abartarak yeniden başladı"
   - Cümle 6: «Sonra bu kez her şeyi abartarak yeniden başladı.»
   - Açıklama: Kartta özellik olayları abartmak iken burada yalnız resmi büyük çizmek olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0149` birebir aynı, `@degisim: kibar -> kocaman` (tutuyorsan), ardından `@onarim: abd8a3e30a9e189d1ca9c0fc082a377361c72f67`, sonra gövde.

### Hikâye 10: tohum hayri-0151 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0151
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tüy', fiil 'güzelleşmek', sıfat 'güvenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: arkadaşı çok iyi saklandı ve bulunamadı | acıktı ve bisküvi paketini açınca arkadaşı ortaya çıktı
@tohum: hayri-0151
@degisim: tüy -> bisküvi
Hayri ile Akın bahçede saklanma oyunu oynuyordu. Akın güvenli bir yere, çalıların arkasına saklandı. Hayri her yere baktı ama Akın'ı bulamadı, çünkü Akın çok iyi saklanmıştı. "Neredesin, Akın?" diye seslendi Hayri. Ama Akın hiç ses çıkarmadı. Hayri bu arada çok acıkmıştı. Çimlere oturdu ve cebindeki bisküvi paketini açtı. Paket hışır hışır ses çıkardı. Birden çalıların arkasından Akın'ın başı göründü. "Bana da bisküvi var mı?" diye sordu Akın. "Seni buldum, Akın!" dedi Hayri ve güldü. Bisküvileri paylaşınca oyun daha da güzelleşti. Sonra Hayri ile Akın oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri ile Akın bahçede saklanma"
   - Cümle 1: «Hayri ile Akın bahçede saklanma oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri ile Akın bahçede saklanma oyunu oynuyordu"
   - Cümle 1: «Hayri ile Akın bahçede saklanma oyunu oynuyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye bahçede geçiyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Akın güvenli bir yere"
   - Cümle 2: «Akın güvenli bir yere, çalıların arkasına saklandı.»
   - Açıklama: Saklanmak için 'güvenli' yer sözü bağlama uymuyor; 'iyi bir yere' ya da 'gizli bir yere' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri bu arada çok acıkmıştı"
   - Cümle 6: «Hayri bu arada çok acıkmıştı.»
   - Açıklama: Acıkma olaydan çıkmıyor ve çözümü sebepsizce getiriyor.
   - Açıklama: Acıkma ansızın beliriyor ve çözümü sebepsizce getiriyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "cebindeki bisküvi paketini açtı"
   - Cümle 7: «Çimlere oturdu ve cebindeki bisküvi paketini açtı.»
   - Açıklama: Çözüm sorunun sebebine (iyi saklanma) yönelmiyor, Akın tesadüfen ortaya çıkıyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Çimlere oturdu ve cebindeki bisküvi paketini açtı"
   - Cümle 7: «Çimlere oturdu ve cebindeki bisküvi paketini açtı.»
   - Açıklama: Çözüm arkadaşı bulmaya yönelmiyor; Akın tesadüfen ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0151` birebir aynı, `@degisim: tüy -> bisküvi` (tutuyorsan), ardından `@onarim: 6feeade4dee28da91620beb4fb71158e50f7b700`, sonra gövde.

### Hikâye 11: tohum hayri-0152 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0152
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tahta', fiil 'güldürmek', sıfat 'biberli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: dalga kaleyi yıktı ve arkadaşı üzüldü | acıkınca yiyeceklerle tahtaya gülen bir yüz yaptı
@tohum: hayri-0152
Deniz kıyısında Hayri ile Mert kumdan bir kale yapmıştı. Ama küçük bir dalga geldi ve kaleyi yıktı. Mert buna çok üzüldü. Hayri o sırada çok acıkmıştı ve bir sürpriz düşündü. Çantasından iki biberli sandviç ve iki elma çıkardı. Kıyıda düz bir tahta buldu ve yiyecekleri üstüne koydu. Mert'i güldürmek için tahtada gülen bir yüz yaptı. Elmalar iki göz, sandviçler de kocaman bir ağız oldu. "Sürpriz, Mert, gel bak!" dedi Hayri. Mert tahtaya baktı ve kahkahayla güldü. İkisi yan yana oturup yiyecekleri paylaştı. "Teşekkürler, Hayri, bu en güzel sürpriz!" dedi Mert.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri o sırada çok acıkmıştı"
   - Cümle 4: «Hayri o sırada çok acıkmıştı ve bir sürpriz düşündü.»
   - Açıklama: Çözüm yıkılan kaleye yönelmiyor, açlıkla ilgisiz bir yemek sürprizine dönüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri o sırada çok acıkmıştı ve bir sürpriz düşündü"
   - Cümle 4: «Hayri o sırada çok acıkmıştı ve bir sürpriz düşündü.»
   - Açıklama: Açlık sürpriz fikrini sebepsizce getiriyor ve olaylar birbirinden çıkmıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Mert'i güldürmek için tahtada gülen bir yüz yaptı"
   - Cümle 7: «Mert'i güldürmek için tahtada gülen bir yüz yaptı.»
   - Açıklama: Sorunun sebebi yıkılan kale ama çözüm kaleye hiç yönelmiyor, yalnız Mert'i yemekle oyalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0152` birebir aynı, ardından `@onarim: 0cfb5ef2b45c4a3724f8e31344df91e4f8506b14`, sonra gövde.

### Hikâye 12: tohum hayri-0153 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0153
- yer: park (Mahallenin çocuk parkı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'heykel', fiil 'aydınlanmak', sıfat 'sırılsıklam'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: doğum gününde yağmur yağdı ve arkadaşı üzüldü | acıkınca bile yemediği kurabiyelerle ona sürpriz yaptı
@tohum: hayri-0153
@degisim: heykel -> kurabiye
Bir sabah Hayri ile Akın parktaydı ve o gün Akın'ın doğum günüydü. Birden kısa bir yağmur yağdı ve Akın sırılsıklam oldu. Akın, doğum günü bozuldu diye çok üzüldü. Hayri çok acıkmıştı ama çantasındaki kurabiyeleri yememişti. Onları Akın'a sürpriz yapmak için saklamıştı. Sonra yağmur durdu ve güneş çıktı. Park güneşle aydınlandı ve Akın'ı ısıttı. Hayri çantasından kurabiye kutusunu çıkardı ve açtı. Kutunun içinde küçük kurabiyeler vardı. "İyi ki doğdun, Akın!" dedi Hayri. Akın kurabiyelere baktı ve sevinçle güldü. "Hepsi benim için mi?" diye sordu Akın. "Hayır, ikimiz için," dedi Hayri. Sonra Hayri ile Akın kurabiyeleri paylaştı ve mutlu mutlu oynadı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "doğum günü bozuldu diye"
   - Cümle 3: «Akın, doğum günü bozuldu diye çok üzüldü.»
   - Açıklama: 'Doğum günü bozuldu' soyut ve mecazlı bir anlatım.
   - Açıklama: Doğum gününün bozulması soyut ve mecazlı bir anlatım.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra yağmur durdu ve güneş çıktı"
   - Cümle 6: «Sonra yağmur durdu ve güneş çıktı.»
   - Açıklama: Islaklık sorunu figürün hiçbir eylemi olmadan kendiliğinden çözülüyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Park güneşle aydınlandı ve Akın'ı ısıttı"
   - Cümle 7: «Park güneşle aydınlandı ve Akın'ı ısıttı.»
   - Açıklama: Akın'ı ısıtan park değil güneştir; fiil öznesine uymuyor.
4. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Park güneşle aydınlandı ve Akın'ı ısıttı"
   - Cümle 7: «Park güneşle aydınlandı ve Akın'ı ısıttı.»
   - Açıklama: Akın'ın ıslanma sorununu Hayri değil kendiliğinden çıkan güneş çözüyor.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri çantasından kurabiye kutusunu çıkardı"
   - Cümle 8: «Hayri çantasından kurabiye kutusunu çıkardı ve açtı.»
   - Açıklama: Çözüm sorunun sebebi olan yağmura ve ıslaklığa yönelmiyor, önceden saklanmış kurabiyelerle üzüntüyü dağıtıyor.
   - Açıklama: Kurabiye sürprizi sorunun sebebi olan yağmura ve ıslanmaya yönelmiyor, önceden hazırlanmış ayrı bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0153` birebir aynı, `@degisim: heykel -> kurabiye` (tutuyorsan), ardından `@onarim: 5a3087cf40f407df4f3a374918b0697321cf78e3`, sonra gövde.
