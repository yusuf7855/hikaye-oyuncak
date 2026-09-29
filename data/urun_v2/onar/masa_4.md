# Editör görevi (onarım): Maşa, onarım partisi 4

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 7 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar4.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar4.txt --ad urun_v2`
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

### Hikâye 1: tohum masa-0002 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, kirpi
@tohum: masa-0002
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı, kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'silgi', fiil 'hazırlamak', sıfat 'gizemli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, kirpi
@plan: sepet dala takıldı ve reçel kavanozu kayboldu | yerdeki kırmızı damlaları takip edip kavanozu buldu
@tohum: masa-0002
@degisim: silgi -> kavanoz
Ormanda Koca Ayı, Maşa ile kirpi için kahvaltı hazırlıyordu. Ama sepet bir dala takıldı ve reçel kavanozu düşüp yuvarlandı. Koca Ayı her yere baktı ama kavanozu bulamadı. Maşa, Koca Ayı'ya yardım etmek istedi. Yerde gizemli kırmızı damlalar gördü. Maşa reçeli çok severdi ve bu damlaları hemen tanıdı. Kavanozun kapağı açılmıştı ve reçel yere dökülmüştü. Maşa damlaları takip etti ve çalılara vardı. Kavanoz orada, çimenlerin üstünde duruyordu. "Buldum, Koca Ayı, işte reçel!" dedi Maşa. Koca Ayı sevinçle kavanozu aldı ve ekmeklere reçel sürdü. Kirpi de burnunu kavanoza uzattı. "Kahvaltı hazır, hadi hep birlikte yiyelim!" dedi Maşa.
```

**Hakem bulguları (3):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Yerde gizemli kırmızı damlalar gördü"
   - Cümle 5: «Yerde gizemli kırmızı damlalar gördü.»
   - Açıklama: Yerdeki gizemli kırmızı damlalar küçük çocuğa kan izi gibi korkutucu gelebilir.
   - Açıklama: Ormanda gizemli kırmızı damlalar kan izi gibi okunup küçük çocuğu korkutabilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yerde gizemli kırmızı damlalar"
   - Cümle 5: «Yerde gizemli kırmızı damlalar gördü.»
   - Açıklama: 'Gizemli' soyut bir kelimedir ve 3 yaşındaki bir çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yerde gizemli kırmızı"
   - Cümle 5: «Yerde gizemli kırmızı damlalar gördü.»
   - Açıklama: 'Gizemli' soyut bir kelime ve 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0002` birebir aynı, `@degisim: silgi -> kavanoz` (tutuyorsan), ardından `@onarim: f9d3625584db42e3c7f650ee97ecbe12580dfd6d`, sonra gövde.

### Hikâye 2: tohum masa-0003 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0003
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'inci', fiil 'barışmak', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: ip kısa olduğu için bilezik kapanmadı | ipin ucuna uzun bir ot bağladı
@tohum: masa-0003
@degisim: barışmak -> bağlamak
Rüzgar esiyordu. Maşa ormanda kuzeni Daşa için küçük beyaz incilerden bir bilezik hazırlıyordu. Ama ip çok kısaydı ve bilezik kapanmadı. Daşa biraz ileride gözlerini kapatmış bekliyordu. Maşa hemen yeni bir şey denedi. Yerden uzun ve ince bir ot kopardı. Otu ipin ucuna sıkıca bağladı. Bu kez bilezik kapandı. Maşa bileziği kalp işaretli küçük bir kutuya koydu. Sonra kutuyu Daşa'ya götürdü. Daşa gözlerini açtı ve kutunun içine baktı. Bileziği hemen koluna taktı ve Maşa'ya sarıldı. Maşa bundan sonra ip kısa kalınca ucuna bir ot bağladı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kalp işaretli küçük bir kutuya koydu"
   - Cümle 9: «Maşa bileziği kalp işaretli küçük bir kutuya koydu.»
   - Açıklama: Kalp işaretli kutu hiçbir hazırlık olmadan sebepsizce beliriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kalp işaretli küçük bir kutuya"
   - Cümle 9: «Maşa bileziği kalp işaretli küçük bir kutuya koydu.»
   - Açıklama: Kutu hiçbir sebep gösterilmeden ortaya çıkıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bileziği kalp işaretli küçük bir kutuya koydu"
   - Cümle 9: «Maşa bileziği kalp işaretli küçük bir kutuya koydu.»
   - Açıklama: Kalp işaretli kutu hiç kurulmadan sebepsizce beliriyor.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa bundan sonra ip kısa kalınca ucuna bir ot bağladı"
   - Cümle 13: «Maşa bundan sonra ip kısa kalınca ucuna bir ot bağladı.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılırken tek seferlik -dı kullanılmış; 'bağlardı' olmalı.
   - Açıklama: 'Bundan sonra' süreklilik bildirdiği için fiil 'bağlardı' olmalı; tek seferlik '-dı' ile uyumsuz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0003` birebir aynı, `@degisim: barışmak -> bağlamak` (tutuyorsan), ardından `@onarim: 3ecdde84fe12faf8c2ff3c7aa8e8b7fe9e4ee2fb`, sonra gövde.

### Hikâye 3: tohum masa-0005 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | kirpi
@tohum: masa-0005
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni bir şeyi denemek
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'mermer', fiil 'uyutmak', sıfat 'değerli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | kirpi
@plan: kirpi sert taşın üstünde uyuyamadı | yapraktan yumuşak bir yatak yaptı
@tohum: masa-0005
@degisim: değerli -> yumuşak
Bir sabah Maşa ormanda bir kirpi gördü. Kirpi büyük, beyaz bir mermer taşın üstünde uyumaya çalışıyordu. Ama taş çok sertti ve kirpi uyuyamadı. Maşa daha önce hiç yapraktan yatak yapmamıştı. Ama bu yeni işi hemen denedi. Ağaçların altından yumuşak yapraklar topladı. Yaprakları taşın yanına koydu ve küçük bir yatak yaptı. Kirpi taştan indi ve yaprakları kokladı. "Bu senin yeni yatağın, kirpi," dedi Maşa. Kirpi yumuşak yatağa kıvrıldı ve hemen uyudu. Maşa çok sevindi, çünkü yaptığı ilk yatakla kirpiyi uyutmuştu.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "beyaz bir mermer taşın"
   - Cümle 2: «Kirpi büyük, beyaz bir mermer taşın üstünde uyumaya çalışıyordu.»
   - Açıklama: 'Mermer' kelimesini 3 yaşındaki bir çocuk bilmeyebilir.
   - Açıklama: 'Mermer' kelimesini 3 yaşındaki bir çocuk büyük olasılıkla bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0005` birebir aynı, `@degisim: değerli -> yumuşak` (tutuyorsan), ardından `@onarim: f2d84306daf37e4e7bfdd355f212c941354a0975`, sonra gövde.

### Hikâye 4: tohum masa-0007 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, kirpi
@tohum: masa-0007
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yeni bir şeyi denemek
- yan: Koca Ayı, kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kurabiye', fiil 'görünmek', sıfat 'çevik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, kirpi
@plan: büyük sesten kirpi kıvrıldı ve burnu görünmedi | yanına oturup yavaşça konuştu ve kurabiye verdi
@tohum: masa-0007
@degisim: çevik -> hızlı
Bir sabah Maşa, Koca Ayı ve kirpi tepede kurabiye yiyordu. Koca Ayı kurabiyeleri çok beğendi ve ellerini hızlı hızlı çırptı. Bu büyük sesten kirpi top gibi kıvrıldı ve burnu hiç görünmedi. Kirpi artık kurabiyesini yiyemiyordu. Maşa kirpiye yardım etmek istedi. Maşa hiç sessiz durmazdı, ama bu kez yeni bir şey denedi. Kirpinin yanına oturdu ve çok yavaş konuştu. "Kirpi, gel, sana bir kurabiye ayırdım," dedi Maşa. Sonra kurabiyeyi kirpiye uzattı. Kirpi biraz açıldı ve önce küçük burnu göründü. Sonra kurabiyeyi aldı ve yemeye başladı. Sonra üçü tepede kurabiyelerini mutlu mutlu yemeye devam etti.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra üçü tepede kurabiyelerini"
   - Cümle 12: «Sonra üçü tepede kurabiyelerini mutlu mutlu yemeye devam etti.»
   - Açıklama: 'Sonra' dört cümle içinde üç kez tekrarlanıyor (9, 11 ve 12. cümleler).
   - Açıklama: 9, 11 ve 12. cümleler art arda 'Sonra' ile başlıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0007` birebir aynı, `@degisim: çevik -> hızlı` (tutuyorsan), ardından `@onarim: 8db662deb12172f5fbbd2398aa51b201790af875`, sonra gövde.

### Hikâye 5: tohum masa-0008 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0008
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: sırayla oynamak
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'bulut', fiil 'solmak', sıfat 'sevinçli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: iki kız aynı anda bağırdı ve birbirini duymadı | sırayla söyleme kuralı koydu
@tohum: masa-0008
@degisim: solmak -> söylemek
Bir sabah Maşa ile Daşa ormanda çimenlere uzanmış, bulutlara bakıyordu. İkisi de bulutlarda şekil bulmak istiyordu. Ama ikisi aynı anda bağırıyordu ve birbirlerini duymuyorlardı. Maşa biraz düşündü ve yeni bir oyun kuralı denedi. "Sırayla söyleyelim, Daşa, önce sen," dedi Maşa. Daşa gökyüzüne dikkatle baktı. "Şu bulut bir kaşığa benziyor," dedi Daşa. Maşa da baktı ve kaşığı gördü. Sonra sıra Maşa'ya geldi. "Şu bulut da kocaman bir elmaya benziyor!" dedi Maşa. Daşa elmayı görünce sevinçli bir sesle güldü. İki kız sırayla bulutlara baktı ve oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yeni bir oyun kuralı denedi"
   - Cümle 4: «Maşa biraz düşündü ve yeni bir oyun kuralı denedi.»
   - Açıklama: Kural denenmez, konur; fiil yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0008` birebir aynı, `@degisim: solmak -> söylemek` (tutuyorsan), ardından `@onarim: 82eee31662aa1728b4bf519df11e12690a609426`, sonra gövde.

### Hikâye 6: tohum masa-0009 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | sincap
@tohum: masa-0009
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: paylaşmak
- yan: sincap
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'ay', fiil 'buruşturmak', sıfat 'kararlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | orman | sincap
@plan: kurabiye çok sertti ve paylaşmak için kırılmadı | kurabiyeyi kağıda sarıp kağıdı buruşturdu
@tohum: masa-0009
@degisim: kararlı -> yuvarlak
Maşa ormanda bir kütüğe oturdu ve kağıda sarılı kurabiyesini açtı. Bir sincap kütüğe zıpladı ve ay gibi yuvarlak kurabiyeye baktı. Maşa kurabiyeyi sincapla paylaşmak istedi, ama kurabiye çok sertti ve kırılmadı. Maşa hemen yeni bir şey denedi. Kurabiyeyi yeniden kağıda sardı. Sonra kağıdı iki eliyle sıkıca buruşturdu. Kağıdın içinde kurabiye çıt diye kırıldı. Maşa kağıdı açtı ve parçaların yarısını sincaba verdi. Sincap parçaları patileriyle tuttu ve hızlı hızlı yedi. Maşa da kendi parçalarını yedi. "Birlikte yemek daha güzel, sincap!" dedi Maşa.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "paylaşmak için kırılmadı"
   - Cümle 0 (plan satırı): «kurabiye çok sertti ve paylaşmak için kırılmadı | kurabiyeyi kağıda sarıp kağıdı buruşturdu»
   - Açıklama: Plan satırında 'paylaşmak için' kurabiyeye bağlanıyor; kurabiye paylaşmak amacı taşıyamaz.
   - Açıklama: Amaç bildiren 'paylaşmak için' kurabiyeye uymuyor; paylaşmak isteyen Maşa, kurabiye değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ay gibi yuvarlak kurabiyeye"
   - Cümle 2: «Bir sincap kütüğe zıpladı ve ay gibi yuvarlak kurabiyeye baktı.»
   - Açıklama: 'Ay gibi' benzetmesi mecazlı bir anlatım.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kağıdı iki eliyle sıkıca buruşturdu"
   - Cümle 6: «Sonra kağıdı iki eliyle sıkıca buruşturdu.»
   - Açıklama: Elle kırılamayacak kadar sert kurabiyenin kağıt buruşturunca kırılması sebebe akla yatkın biçimde yönelmiyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kağıdın içinde kurabiye çıt diye kırıldı"
   - Cümle 7: «Kağıdın içinde kurabiye çıt diye kırıldı.»
   - Açıklama: Kurabiye elle kırılamayacak kadar sert denmişken yalnız kağıdı buruşturmakla kolayca kırılması çelişkili görünüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0009` birebir aynı, `@degisim: kararlı -> yuvarlak` (tutuyorsan), ardından `@onarim: 3557c8728a9d87656216ceda46630ed06625d8a9`, sonra gövde.

### Hikâye 7: tohum masa-0010 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | kirpi
@tohum: masa-0010
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: kirpi
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'vazo', fiil 'durdurmak', sıfat 'şık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | ev | kirpi
@plan: vazoya giren kirpi dışarı çıkamadı | vazoyu yavaşça eğdi ve kirpi dışarı kaydı
@tohum: masa-0010
@degisim: şık -> boş
Rüzgar hızlı hızlı esiyordu. Maşa evinin önünde zıplarken rüzgarın devirdiği boş vazodan bir ses duydu. Rüzgardan saklanan bir kirpi kaygan vazoya girmişti ve çıkamıyordu. Maşa hemen zıplamayı durdurdu ve vazonun yanına koştu. "Bekle, kirpi, sana yardım edeceğim," dedi Maşa. Maşa vazonun dibini yavaşça yukarı kaldırmayı denedi. Vazonun ağzı çimenlere doğru eğildi. Kirpi yavaş yavaş kaydı ve çimenlerin üstüne çıktı. Kirpi küçük burnunu kıpırdattı ve Maşa'ya baktı. "Oldu, kirpi, artık çıktın!" dedi Maşa. Sonra boş vazoyu dikkatle yerine koydu. Kirpi de çimenlerde mutlu mutlu dolaştı. Maşa çok sevindi, çünkü kirpiyi vazodan çıkarmıştı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgarın devirdiği boş vazodan"
   - Cümle 2: «Maşa evinin önünde zıplarken rüzgarın devirdiği boş vazodan bir ses duydu.»
   - Açıklama: Vazo rüzgarla yan yatmışken kirpinin yatay ağızdan çıkamaması akla yatkın bir sebep değil.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Rüzgardan saklanan bir kirpi"
   - Cümle 3: «Rüzgardan saklanan bir kirpi kaygan vazoya girmişti ve çıkamıyordu.»
   - Açıklama: 'Rüzgar' kelimesi art arda üç cümlede (1, 2, 3) gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0010` birebir aynı, `@degisim: şık -> boş` (tutuyorsan), ardından `@onarim: 10a385c47d3004ef2908958546e10facdd9efcea`, sonra gövde.
