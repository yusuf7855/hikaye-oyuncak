# Editör görevi (onarım): Hayri, onarım partisi 21

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar21.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0065 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0065
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'patik', fiil 'açılmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: amca beklemekten sıkıldı ve gitmek istedi | baklava paylaştı ve amcayla birlikte bekledi
@tohum: hayri-0065
@degisim: patik -> çiçek
Ormandaki kamp yerinde turuncu bir çiçek açılmak üzereydi. Hayri, Basri Amca ile çiçeğin yanında oturmuş bekliyordu. Ama Basri Amca beklemekten sıkıldı ve ayağa kalktı. "Çok uzun sürdü, ben gidiyorum," dedi Basri Amca. Hayri, çiçeği amcayla birlikte görmek istiyordu. Yanında, çalıştığı baklava dükkanından getirdiği bir kutu vardı. Hayri kutunun kapağını kaldırdı ve amcaya uzattı. "Beklerken birer baklava yiyelim mi, Basri Amca?" diye sordu Hayri. Amca gülümsedi ve yeniden oturdu. İkisi baklavalarını yerken çiçeğe baktı. Az sonra turuncu çiçek bütün yapraklarıyla açıldı. "Çok güzel, Hayri, iyi ki gitmemişim!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kapağını kaldırdı ve amcaya uzattı"
   - Cümle 7: «Hayri kutunun kapağını kaldırdı ve amcaya uzattı.»
   - Açıklama: Uzatılan nesne belli değil; cümle kapağın uzatıldığı gibi okunuyor, kutu kastediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0065` birebir aynı, `@degisim: patik -> çiçek` (tutuyorsan), ardından `@onarim: c4c77e954cb2d4d0acfef20826f875fa34a303e9`, sonra gövde.

### Hikâye 2: tohum hayri-0066 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0066
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'zil', fiil 'ödemek', sıfat 'sıcacık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek baklava kutusunu ağaçların arasına götürdü | köpekten yardım istedi ve havlama sesini izledi
@tohum: hayri-0066
@degisim: ödemek -> koklamak
Ormandaki kamp yerinde Hayri küçük bir zil çalıyor, Yumak da sese koşuyordu. Hayri'nin çalıştığı dükkandan getirdiği sıcacık baklava kutusu bir kütüğün üstündeydi. Ama Yumak kutuyu ağzına aldı, ağaçların arasına koştu ve kutusuz döndü. Hayri her yere baktı ama kutuyu bulamadı. "Yumak, kutuyu bulmama yardım eder misin?" diye sordu Hayri. Yumak yeri kokladı. Sonra havlayarak ağaçların arasına doğru koştu. Hayri havlama sesini izledi ve Yumak'ın peşinden yürüdü. Kutu büyük bir ağacın dibindeydi. Hayri kutuyu açtı ve baklavaların hepsinin orada olduğunu gördü. Sonra Hayri ile Yumak zil oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri havlama sesini izledi ve Yumak'ın peşinden yürüdü"
   - Cümle 8: «Hayri havlama sesini izledi ve Yumak'ın peşinden yürüdü.»
   - Açıklama: Çocuk yalnız başına ormanda ağaçların arasına bir köpeğin peşinden gidiyor; taklit edilince kaybolma tehlikesi var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0066` birebir aynı, `@degisim: ödemek -> koklamak` (tutuyorsan), ardından `@onarim: 32d14ff90881b1a037fcd460aa82197b61677320`, sonra gövde.

### Hikâye 3: tohum hayri-0068 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0068
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'zincir', fiil 'olgunlaşmak', sıfat 'tertemiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: erikler olgunlaşmıştı ama çok yüksek bir daldaydı | arkadaşından yardım istedi ve erikleri topladı
@tohum: hayri-0068
@degisim: zincir -> dal
Güneş evlerin üstünde parlıyordu. Hayri ile Mert bahçedeki erik ağacının altında oturuyordu. Hayri acıkmıştı ama olgunlaşmış erikler çok yüksek bir daldaydı. Hayri zıpladı ama erikleri tutamadı. "Mert, sen benden uzunsun, bana yardım eder misin?" diye sordu Hayri. Mert ayağa kalktı ve dalın ucunu tuttu. Dalı yavaşça aşağı çekti. Hayri erikleri tek tek topladı. Sonra erikleri çeşmede yıkadı ve erikler tertemiz oldu. "Teşekkürler, Mert!" dedi Hayri. Hayri ile Mert erikleri paylaştı ve mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "erikleri çeşmede yıkadı ve erikler tertemiz oldu"
   - Cümle 9: «Sonra erikleri çeşmede yıkadı ve erikler tertemiz oldu.»
   - Açıklama: Aynı cümlede 'erikler' gereksiz yere tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0068` birebir aynı, `@degisim: zincir -> dal` (tutuyorsan), ardından `@onarim: 7b71aead75e6a5f76748d447cd330c44c8bfa091`, sonra gövde.

### Hikâye 4: tohum hayri-0069 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0069
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yağmur ya da kar günü
- yan: Mert
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'ekmek', fiil 'yakalanmak', sıfat 'çilekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: yağmur başladı ve masadaki kurabiyeler ıslanıyordu | tabağı alıp çadıra koştu
@tohum: hayri-0069
@degisim: ekmek -> kurabiye
Hayri ile Mert kamp yerinde çilekli kurabiye yiyordu. Birden yağmur başladı ve ikisi yağmura yakalandı. Masadaki kurabiyeler ıslanıyordu. "Mert, bu dünyanın en büyük yağmuru!" dedi Hayri abartarak. Mert güldü ve ayağa kalktı. "O kadar büyük değil, ama çabuk olalım," dedi Mert. Hayri tabağı iki eliyle tuttu ve çadıra koştu. Mert de çadırın kapısını açtı. İçerisi kuru ve sıcaktı. Hayri tabağı yere koydu ve kurabiyelere baktı. Yalnız bir kurabiyenin ucu biraz ıslanmıştı. Yağmur çadırın üstüne tıp tıp vuruyordu. İki arkadaş kurabiyelerini çadırda afiyetle yedi. "Mert, çadırda yağmuru dinleyerek yemek çok güzelmiş!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 4: «"Mert, bu dünyanın en büyük yağmuru!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kelime ve 'dünyanın en büyük yağmuru' abartı mecazı 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Abartarak' ve 'dünyanın en büyük yağmuru' abartması 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0069` birebir aynı, `@degisim: ekmek -> kurabiye` (tutuyorsan), ardından `@onarim: 6850cb68f6a6932f4fe71007c10fdb79e394265c`, sonra gövde.

### Hikâye 5: tohum hayri-0071 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0071
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'scooter', fiil 'sormak', sıfat 'tüylü'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: kütük çok sertti ve arkadaşı rahat oturamadı | çadırdan tüylü battaniyesini getirip kütüğe serdi
@tohum: hayri-0071
@degisim: scooter -> kitap
Bir sabah Hayri kamp yerinde Kamil ile oturuyordu. Kamil bir kütüğün üstünde kitap okumak istedi. Ama kütük çok sertti ve Kamil hemen ayağa kalktı. Hayri ona ne olduğunu sordu. Kamil kütüğün çok sert olduğunu söyledi. Hayri hemen çadıra koştu ve tüylü battaniyesini getirdi. Battaniyeyi ikiye katladı ve kütüğün üstüne serdi. Hayri abartarak bunun ormandaki en yumuşak yer olduğunu söyledi. Kamil güldü ve battaniyenin üstüne oturdu. Kütük artık hiç sert değildi. Hayri de Kamil'in yanına oturdu. İki arkadaş kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak bunun ormandaki"
   - Cümle 8: «Hayri abartarak bunun ormandaki en yumuşak yer olduğunu söyledi.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0071` birebir aynı, `@degisim: scooter -> kitap` (tutuyorsan), ardından `@onarim: 9973aadd8d6d0cb192d055548b806ee0184af202`, sonra gövde.

### Hikâye 6: tohum hayri-0072 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0072
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamyonet', fiil 'ayırmak', sıfat 'özel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı | kumu elleriyle iki yana ayırıp kamyoneti çekti
@tohum: hayri-0072
Dalgalar kıyıya yavaşça vuruyordu. Hayri ile Akın, oyuncak kamyoneti kumla doldurup bir tepe yapıyordu. Birden büyük bir dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı. "Kamyonet denizin dibine gidiyor!" dedi Hayri abartarak. Akın güldü. "Hayır, yalnız tekerlekleri battı," dedi Akın. Hayri tekerleklerin önündeki kumu elleriyle iki yana ayırdı. Sonra kamyoneti yavaşça çekti ve kumdan çıkardı. "Teşekkürler, Hayri, bu kamyonet benim için çok özel!" dedi Akın. İki arkadaş kamyoneti dalgalardan uzağa, kuru kuma götürdü. Orada tepeyi büyütmeye mutlu mutlu devam ettiler.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 4: «"Kamyonet denizin dibine gidiyor!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartarak' soyut bir kavram; 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0072` birebir aynı, ardından `@onarim: 748f117f266addec1f150f82309225aa6c90593a`, sonra gövde.

### Hikâye 7: tohum hayri-0073 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0073
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'saat', fiil 'hoplamak', sıfat 'sisli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: masadan garip bir ses geldi | masaya gidip sesi yapan damlaları buldu
@tohum: hayri-0073
Sabah orman çok sisliydi. Kahvaltı saati gelmişti ve Hayri çok acıkmıştı. Birden masadan tık tık diye bir ses geldi. Hayri sisin içinde masayı iyi göremedi. Sesi çok merak etti. Yerdeki köklerin üstünden hopladı ve masaya yaklaştı. Masada kapaklı bir tencere vardı. Dallardan düşen büyük damlalar tencerenin kapağına vuruyordu. Tık tık sesini bu damlalar yapıyordu. Hayri güldü ve kapağı kaldırdı. İçindeki yumurtalar hiç ıslanmamıştı. Tencereyi çadıra götürdü ve kahvaltısını afiyetle yaptı. Hayri bundan sonra dışarıdaki yemeğin üstünü hep kapattı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kahvaltı saati gelmişti ve Hayri çok acıkmıştı"
   - Cümle 2: «Kahvaltı saati gelmişti ve Hayri çok acıkmıştı.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız anılıyor, sorunun çözümüne bir katkısı yok.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden masadan tık tık diye bir ses geldi"
   - Cümle 3: «Birden masadan tık tık diye bir ses geldi.»
   - Açıklama: Sorun zararsız bir sesten ibaret; gerçek bir sorun yok.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hayri bundan sonra dışarıdaki yemeğin üstünü hep kapattı"
   - Cümle 13: «Hayri bundan sonra dışarıdaki yemeğin üstünü hep kapattı.»
   - Açıklama: Tencere zaten kapalıydı; ders yaşanan olaydan çıkmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0073` birebir aynı, ardından `@onarim: 289f47677bfe5cc3bbc40065436d3175354e0f88`, sonra gövde.

### Hikâye 8: tohum hayri-0074 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0074
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kumbara', fiil 'yankılanmak', sıfat 'kaygan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: yüksek sesle bağırdı ve uyuyan köpeği korkuttu | özür diledi ve ona simit verdi
@tohum: hayri-0074
@degisim: kumbara -> simit
Bir sabah Hayri kamp yerinde çok acıkmıştı. "Kahvaltı hazır!" diye yüksek sesle bağırdı Hayri. Sesi ağaçların arasında yankılandı ve uyuyan Yumak birden uyandı. Yumak korktu ve çadırın arkasına koştu. Hayri masadan bir simit aldı. Kaygan toprakta yavaş yavaş çadırın arkasına yürüdü. Yumak orada yerde yatıyor ve ona bakıyordu. "Özür dilerim, Yumak, seni korkuttum," dedi Hayri yavaşça. Sonra simidi ikiye böldü ve küçük parçayı Yumak'a uzattı. Yumak simidi kokladı ve yedi. Sonra kuyruğunu sallayarak Hayri'nin yanına geldi. Hayri bundan sonra Yumak uyurken hep alçak sesle konuştu.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kaygan toprakta yavaş yavaş"
   - Cümle 6: «Kaygan toprakta yavaş yavaş çadırın arkasına yürüdü.»
   - Açıklama: Kaygan toprak işe yarayacakmış gibi kuruluyor ama olayda hiçbir rol oynamıyor.
   - Açıklama: Kaygan toprak bir şey olacakmış gibi kuruluyor ama olayda hiçbir işe yaramıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "küçük parçayı Yumak'a uzattı"
   - Cümle 9: «Sonra simidi ikiye böldü ve küçük parçayı Yumak'a uzattı.»
   - Açıklama: Korkmuş bir köpeğe yaklaşıp elden simit vermek çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0074` birebir aynı, `@degisim: kumbara -> simit` (tutuyorsan), ardından `@onarim: a7a00d83228eb832e777dd5ff4140cadfb60e84c`, sonra gövde.

### Hikâye 9: tohum hayri-0075 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0075
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'elmas', fiil 'saklanmak', sıfat 'sıcak'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: ikisi de saklanmak istedi ve oyun başlamadı | önce kendisi saydı ve sırayla oynadılar
@tohum: hayri-0075
@degisim: elmas -> simit
Bir sabah Hayri ile Kamil kamp yerinde saklambaç oynuyordu. İkisi de önce saklanmak istedi ve kimse saymak istemedi. Bu yüzden oyun hiç başlamadı. "Kamil, önce ben sayarım, sonra sıra sende," dedi Hayri. Hayri gözlerini kapadı ve ona kadar saydı. Kamil hemen koştu ve saklandı. Hayri çok acıkmıştı ve masadan sıcak simit kokusu geliyordu. Hayri kokuya doğru yürüdü ve masanın altına baktı. Kamil orada, simit sepetinin yanında gülüyordu. "Buldum seni, Kamil!" dedi Hayri. "Şimdi sıra bende, Hayri," dedi Kamil. İki arkadaş birer simit yedi ve sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bu yüzden oyun hiç başlamadı"
   - Cümle 3: «Bu yüzden oyun hiç başlamadı.»
   - Açıklama: İlk cümlede saklambaç oynuyorlar ama sonra oyunun hiç başlamadığı söyleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı ve masadan sıcak simit kokusu geliyordu"
   - Cümle 7: «Hayri çok acıkmıştı ve masadan sıcak simit kokusu geliyordu.»
   - Açıklama: Simit kokusu sebepsiz beliriyor ve Kamil'i bulmayı tesadüfen getiriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "masadan sıcak simit kokusu geliyordu"
   - Cümle 7: «Hayri çok acıkmıştı ve masadan sıcak simit kokusu geliyordu.»
   - Açıklama: Masa ve simit sebepsiz beliriyor ve Kamil'i bulmayı rastlantıyla getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0075` birebir aynı, `@degisim: elmas -> simit` (tutuyorsan), ardından `@onarim: 128686b4341241daf6a7a1642492457266d5e070`, sonra gövde.

### Hikâye 10: tohum hayri-0076 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0076
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'bilye', fiil 'kutlamak', sıfat 'sakar'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: bilye çarptı ve amcanın çayı kuma döküldü | özür dileyip simidini amcayla paylaştı
@tohum: hayri-0076
@degisim: kutlamak -> paylaşmak
Deniz kıyısında Hayri kumda bilye oynuyordu. Basri Amca yakındaki bir taşın üstünde oturmuş çay içiyordu. Hayri bilyeyi çok hızlı fırlattı ve bilye amcanın bardağına çarptı. Bardak devrildi ve çay kuma döküldü. Basri Amca kızdı. "Hayri, biraz dikkatli ol!" dedi Basri Amca. Hayri hemen koştu ve bardağı kumdan kaldırdı. "Özür dilerim, amca, sakar davrandım," dedi Hayri. Hayri acıkmıştı ve çantasında bir simit vardı. Ama simidi ikiye böldü ve yarısını amcaya verdi. "Çayın yerine bunu paylaşalım," dedi Hayri. Basri Amca gülümsedi. "Teşekkürler, Hayri, bundan sonra biraz uzakta oyna," dedi Basri Amca. İkisi kıyıda yan yana oturdu ve simidi mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "amca, sakar davrandım"
   - Cümle 8: «"Özür dilerim, amca, sakar davrandım," dedi Hayri.»
   - Açıklama: 'Sakar davranmak' küçük çocuğun bilmeyeceği soyut bir ifade.
   - Açıklama: 'Sakar' kelimesini 3 yaşındaki çocuk bilmeyebilir.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Çayın yerine bunu paylaşalım"
   - Cümle 11: «"Çayın yerine bunu paylaşalım," dedi Hayri.»
   - Açıklama: Dökülen çayın yerine simit vermek sebebe (dökülen çay) doğrudan yönelmiyor ve çözüm bardağı kaldırma, özür ve simit paylaşma olarak ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0076` birebir aynı, `@degisim: kutlamak -> paylaşmak` (tutuyorsan), ardından `@onarim: cb20cf838c3e88f34d1a55c4c3239795e66ffe89`, sonra gövde.

### Hikâye 11: tohum hayri-0077 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0077
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'zeytin', fiil 'somurtmak', sıfat 'sıkı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpek kapağı sıkı tuttu ve hiç bırakmadı | kuma oturup sessizce bekledi
@tohum: hayri-0077
@degisim: zeytin -> kapak
Hayri kıyıda Yumak ile kapak yakalama oyunu oynuyordu. Kapağı çalıştığı baklava dükkanından, boş bir kutudan getirmişti. Ama Yumak kapağı her yakalayınca dişleriyle sıkı tutuyor ve bırakmıyordu. Hayri'nin atma sırası hiç gelmiyordu ve Hayri somurttu. "Yumak, bırak!" dedi Hayri. Yumak kuyruğunu salladı ama kapağı bırakmadı. Hayri kuma oturdu ve sessizce bekledi. Biraz sonra Yumak geldi ve kapağı Hayri'nin önüne koydu. "Aferin, Yumak, şimdi sıra bende!" dedi Hayri. Kapağı uzağa attı ve Yumak koşup getirdi. Bu kez Yumak kapağı hemen verdi. Hayri çok sevindi, çünkü artık Yumak ile sırayla oynayabiliyordu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kapağı çalıştığı baklava dükkanından"
   - Cümle 2: «Kapağı çalıştığı baklava dükkanından, boş bir kutudan getirmişti.»
   - Açıklama: Baklava dükkanı özelliği yalnız geçerken anılıyor, sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kapağı çalıştığı baklava dükkanından, boş bir kutudan getirmişti"
   - Cümle 2: «Kapağı çalıştığı baklava dükkanından, boş bir kutudan getirmişti.»
   - Açıklama: Baklava dükkanı ayrıntısı olayda hiçbir işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı baklava dükkanından, boş bir kutudan"
   - Cümle 2: «Kapağı çalıştığı baklava dükkanından, boş bir kutudan getirmişti.»
   - Açıklama: Kapağın baklava dükkanından geldiği ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0077` birebir aynı, `@degisim: zeytin -> kapak` (tutuyorsan), ardından `@onarim: 19d25cd956d93fae362a5684623476b63e92f75e`, sonra gövde.

### Hikâye 12: tohum hayri-0079 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0079
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kanepe', fiil 'çırpmak', sıfat 'sevecen'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: rüzgar esti ve örtünün kenarları havaya kalktı | örtünün dört ucuna büyük taşlar koydu
@tohum: hayri-0079
@degisim: kanepe -> kurabiye
Bir sabah Hayri kıyıda Akın'ın doğum günü için bir sürpriz hazırlıyordu. Kumun üstüne bir örtü serdi ve kurabiyeleri dizdi. Ama rüzgar esti ve örtünün kenarları havaya kalktı. Kurabiyeler kuma kaymaya başladı. Hayri çevreye baktı ve dört büyük taş topladı. Taşları örtünün dört ucuna koydu. Örtü artık uçmadı ve kurabiyeler yerinde kaldı. Hayri çok acıkmıştı ama kurabiyelere dokunmadı ve Akın'ı bekledi. Biraz sonra Akın kıyıya geldi. Hayri ellerini çırptı. "İyi ki doğdun, Akın!" dedi Hayri. Akın sevecen bir gülümsemeyle Hayri'ye sarıldı. "Bu en güzel sürpriz," dedi Akın. Hayri bundan sonra rüzgarlı günlerde örtünün ucuna hep taş koydu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Akın sevecen bir gülümsemeyle"
   - Cümle 12: «Akın sevecen bir gülümsemeyle Hayri'ye sarıldı.»
   - Açıklama: 'Sevecen bir gülümseme' soyut bir ifade ve 3 yaşındaki çocuk için ağır.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sevecen bir gülümsemeyle Hayri'ye"
   - Cümle 12: «Akın sevecen bir gülümsemeyle Hayri'ye sarıldı.»
   - Açıklama: 'Sevecen' kelimesi 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0079` birebir aynı, `@degisim: kanepe -> kurabiye` (tutuyorsan), ardından `@onarim: 47adc4eb8b89b7ede8ffa330a9c3e5c7b0eb97cf`, sonra gövde.
