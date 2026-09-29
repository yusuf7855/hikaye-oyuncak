# Editör görevi (onarım): Hayri, onarım partisi 20

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar20.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar20.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0043 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0043
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yelpaze', fiil 'götürmek', sıfat 'ferah'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpek gelip kumdan kemiği bozdu | topu uzağa götürdü ve kuma gömdü
@tohum: hayri-0043
@degisim: ferah -> geniş
Kumsal geniş ve serindi. Hayri, Yumak için kumdan kocaman bir kemik yapıyordu. Bu bir sürprizdi ama Yumak topunu bırakıp geldi ve kemiği bozdu. Hayri biraz düşündü. Sonra Yumak'ın kırmızı topunu kayaların yanına götürdü ve kuma gömdü. Topun üstüne küçük bir kum tepesi de yaptı. Yumak topun kokusunu aldı ve orada uzun uzun kumu eşeledi. Hayri hemen işine döndü ve kum kemiğini bitirdi. Kemiğin ucuna beyaz kabuklardan bir yelpaze yaptı. "Yumak, gel, sana ev kadar büyük bir kemik yaptım!" dedi Hayri. Hayri biraz abartmıştı, ama Yumak koşup geldi ve kuyruğunu salladı. Hayri bundan sonra sürpriz hazırlarken önce Yumak'ın topunu saklardı.
```

**Hakem bulguları (5):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kemiğin ucuna beyaz kabuklardan bir yelpaze yaptı"
   - Cümle 9: «Kemiğin ucuna beyaz kabuklardan bir yelpaze yaptı.»
   - Açıklama: Kabuk yelpaze olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sana ev kadar büyük bir kemik"
   - Cümle 10: «"Yumak, gel, sana ev kadar büyük bir kemik yaptım!" dedi Hayri.»
   - Açıklama: Tohumdaki abartma özelliği sorun çözüldükten sonra süs olarak geçiyor, çözümde işe yaramıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı, ama"
   - Cümle 11: «Hayri biraz abartmıştı, ama Yumak koşup geldi ve kuyruğunu salladı.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 11: «Hayri biraz abartmıştı, ama Yumak koşup geldi ve kuyruğunu salladı.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
5. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "önce Yumak'ın topunu saklardı"
   - Cümle 12: «Hayri bundan sonra sürpriz hazırlarken önce Yumak'ın topunu saklardı.»
   - Açıklama: Anlatım -dı'lı geçmişten geniş zamanın hikayesine kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0043` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: 230fbd320ec1332b6fd315b8b03cf2265c941401`, sonra gövde.

### Hikâye 2: tohum hayri-0046 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0046
- yer: park (Mahallenin çocuk parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'mıknatıs', fiil 'ölçmek', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kum çok kuruydu ve pasta hep dağıldı | kumu ıslattı ve eski kovayla pasta yaptı
@tohum: hayri-0046
@degisim: mıknatıs -> kova
Parkın kum havuzunda Hayri pasta yapma oyunu oynuyordu. Hayri biraz abartıp kule kadar yüksek bir pasta yapmak istedi. Ama kum çok kuruydu ve pasta hep dağıldı. Hayri biraz düşündü ve su şişesini açtı. Suyu oyuncak bardağıyla ölçtü ve iki bardak kuma döktü. Islak kumu eski kovasına sıkıca bastırdı. Sonra kovayı ters çevirdi ve yavaşça kaldırdı. Kumdan pasta bu kez hiç yıkılmadı. Hayri onun üstüne iki kat daha yaptı. Pasta bir kule gibi yükseldi. Hayri onu yapraklarla süsledi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartıp kule"
   - Cümle 2: «Hayri biraz abartıp kule kadar yüksek bir pasta yapmak istedi.»
   - Açıklama: 'Abartmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz abartıp kule kadar yüksek bir pasta yapmak istedi"
   - Cümle 2: «Hayri biraz abartıp kule kadar yüksek bir pasta yapmak istedi.»
   - Açıklama: Karttaki özellik olayları abartmak (sözle büyütmek) iken burada abartı büyük bir şey yapmak isteme anlamında kullanılıyor ve çözüme katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0046` birebir aynı, `@degisim: mıknatıs -> kova` (tutuyorsan), ardından `@onarim: 9ce2dc00dc1f7aed941e6da1a18ee0cc7b2902ae`, sonra gövde.

### Hikâye 3: tohum hayri-0047 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0047
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'pizza', fiil 'ıslatmak', sıfat 'çamurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar şapkayı uçurdu ve şapka kayboldu | kıyıda dikkatle aradı ve taşların arkasında buldu
@tohum: hayri-0047
@degisim: pizza -> şapka
Rüzgar kıyıda hızlı esiyordu. Hayri denizin kenarında yürüyor ve dalgaları izliyordu. Birden rüzgar mavi şapkasını başından kaptı ve uçurdu. Hayri önce dalgaların ıslattığı çamurlu kumda aradı, ama şapka orada yoktu. Hayri biraz abartıp şapkanın çok uzağa uçtuğunu düşündü. Bu yüzden en uzaktaki büyük taşlara kadar yürüdü. Rüzgar da o taşlara doğru esiyordu. Hayri taşların arkasına dikkatle baktı. Şapka orada, kuru bir taşın üstündeydi. Hayri şapkayı aldı ve başına sıkıca taktı. Hayri çok sevindi, çünkü kaybolan şapkasını bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartıp şapkanın"
   - Cümle 5: «Hayri biraz abartıp şapkanın çok uzağa uçtuğunu düşündü.»
   - Açıklama: 'Abartmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "en uzaktaki büyük taşlara kadar yürüdü"
   - Cümle 6: «Bu yüzden en uzaktaki büyük taşlara kadar yürüdü.»
   - Açıklama: Çocuğun deniz kıyısında tek başına en uzaktaki taşlara kadar gitmesi taklit edilince tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0047` birebir aynı, `@degisim: pizza -> şapka` (tutuyorsan), ardından `@onarim: dacdd48b3cac466d173467c641713ddf68fba270`, sonra gövde.

### Hikâye 4: tohum hayri-0048 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0048
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kürek', fiil 'ilerlemek', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: çukur sudan uzaktı ve içine su gelmedi | çukurdan denize doğru üç ince yol kazdı
@tohum: hayri-0048
Hayri deniz kıyısında küreğiyle yumuşak kumda bir çukur kazıyordu. Orada küçük bir havuz yapmak istiyordu. Ama çukur sudan uzaktı ve içine hiç su gelmedi. Hayri durdu ve denize dikkatle baktı. Dalgaların kıyıya gelip geri gittiğini fark etti. Hayri abarttı ve çukurdan denize bir değil, üç ince yol kazdı. Az sonra bir dalga geldi. Su yolların içinde yavaş yavaş ilerledi ve çukura aktı. Üç yoldan gelen su havuzu çabucak doldurdu. Hayri sevinçle zıpladı ve ellerini çırptı. Hayri bundan sonra havuzuna suyu hep böyle yollardan getirdi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abarttı ve çukurdan"
   - Cümle 6: «Hayri abarttı ve çukurdan denize bir değil, üç ince yol kazdı.»
   - Açıklama: 'Abartmak' burada yanlış anlamda kullanılmış; üç yol kazmak akıllıca bir çözüm, abartı değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve çukurdan"
   - Cümle 6: «Hayri abarttı ve çukurdan denize bir değil, üç ince yol kazdı.»
   - Açıklama: 'Abarttı' soyut bir kelime ve 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abarttı ve çukurdan denize bir değil, üç ince yol kazdı"
   - Cümle 6: «Hayri abarttı ve çukurdan denize bir değil, üç ince yol kazdı.»
   - Açıklama: Karttaki özellik olayları sözle abartmaktır; burada abartma fazladan iş yapmak olarak yanlış kullanılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abarttı ve çukurdan denize"
   - Cümle 6: «Hayri abarttı ve çukurdan denize bir değil, üç ince yol kazdı.»
   - Açıklama: Karttaki özellik olayları abartmak (sözle büyütmek) iken burada abartma fazladan iş yapmak olarak yanlış kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0048` birebir aynı, ardından `@onarim: ef74c3196cc0d316d6fac577be00f566b2acfd87`, sonra gövde.

### Hikâye 5: tohum hayri-0050 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0050
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'paspas', fiil 'konmak', sıfat 'yeterli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: rüzgar örtünün kenarlarını hep havaya kaldırdı | yardım istedi ve her köşeye bir taş koydu
@tohum: hayri-0050
@degisim: paspas -> örtü
Rüzgar ormanda hızlı hızlı esiyordu. Hayri, çalıştığı dükkanın baklavalarını yemek için yere büyük bir örtü yaymak istedi. Ama rüzgar örtünün kenarlarını hep havaya kaldırdı. Hayri örtüyü tek başına tutamadı. "Basri Amca, bana yardım eder misin?" diye sordu Hayri. "Tabii, hemen geliyorum," dedi Basri Amca. Basri Amca iki köşeyi sıkıca tuttu. Hayri de ağaçların dibinden dört büyük taş getirdi. Taşları örtünün dört köşesine koydu. Artık rüzgar örtüyü hiç kaldıramadı. Sonra Hayri tatlı kutusunu çıkardı. Kutu örtünün tam ortasına kondu. Kutudaki tatlılar ikisine de yeterliydi. Basri Amca bir dilim yedi ve gülümsedi. Hayri çok sevindi, çünkü örtü artık yerinde duruyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "çalıştığı dükkanın baklavalarını yemek"
   - Cümle 2: «Hayri, çalıştığı dükkanın baklavalarını yemek için yere büyük bir örtü yaymak istedi.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız anılıyor, sorunun çözümünde işe yarar biçimde kullanılmıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutudaki tatlılar ikisine de yeterliydi"
   - Cümle 13: «Kutudaki tatlılar ikisine de yeterliydi.»
   - Açıklama: Tatlıların yetmesi hiçbir soruna ya da olaya bağlanmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0050` birebir aynı, `@degisim: paspas -> örtü` (tutuyorsan), ardından `@onarim: 5d905b2bbf6e4b8febaf70ef45663f42f8b032b2`, sonra gövde.

### Hikâye 6: tohum hayri-0051 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0051
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yağmurluk', fiil 'yetişmek', sıfat 'patlak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: patlak kovadan kozalaklar yere düştü | yağmurluğunu katlayıp kovanın dibine koydu
@tohum: hayri-0051
Bir sabah Hayri kamp yerinde kozalakları bir kovaya atıp oynuyordu. Kova dolunca kahvaltı yapacaktı, çünkü çok acıkmıştı. Ama kova patlaktı ve kozalaklar delikten yere düştü. Bir kozalak otların arasına yuvarlandı. Hayri birkaç adımda ona yetişti. Sonra deliğe baktı ve biraz düşündü. Sarı yağmurluğunu çıkardı, katladı ve kovanın dibine koydu. Artık delik kapanmıştı. Hayri kozalağı yine kovaya attı. Bu kez kozalak yere düşmedi. Hayri hızlı hızlı attı ve kova çabucak doldu. Sonra ağacın altına oturdu ve kahvaltısını mutlu mutlu yaptı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kova dolunca kahvaltı yapacaktı"
   - Cümle 2: «Kova dolunca kahvaltı yapacaktı, çünkü çok acıkmıştı.»
   - Açıklama: Aç olan Hayri'nin kahvaltıyı kovanın dolmasına bağlaması sebepsiz ve mantıksız bir koşul.
   - Açıklama: Kahvaltının kovanın dolmasına bağlanması sebepsiz ve olay zincirinden çıkmıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama kova patlaktı"
   - Cümle 3: «Ama kova patlaktı ve kozalaklar delikten yere düştü.»
   - Açıklama: Kova için 'patlak' değil 'delik' denir; kelime yanlış anlamda.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0051` birebir aynı, ardından `@onarim: 81fa908dc7642ee5e8a37df3379250536e396399`, sonra gövde.

### Hikâye 7: tohum hayri-0052 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0052
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'dondurma', fiil 'boşaltmak', sıfat 'tedbirli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: çantanın altından pembe damlalar düşüyordu | çantayı boşalttı ve eriyen dondurmayı buldu
@tohum: hayri-0052
Hayri ile Mert kamp yerinde ağaçların altında oturuyordu. Hayri çok acıkmıştı ve çantasındaki dondurmayı Mert ile paylaşmak istedi. Ama çantanın altından yere pembe damlalar düşüyordu. İkisi de bu damlaları çok merak etti. Hayri çantayı açtı ve içini yavaşça yere boşalttı. İçinden ekmek, iki kaşık ve bir dondurma kutusu çıktı. Kutunun kapağı biraz açılmıştı ve çilekli dondurma eriyordu. Pembe damlalar dondurmadan geliyordu! Tedbirli Mert, ekmekler ıslanmasın diye onları hemen kenara aldı. Hayri dondurma daha fazla erimeden bir kaşığı Mert'e verdi. Hayri ile Mert dondurmayı ağaçların altında mutlu mutlu bitirdi.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çantasındaki dondurmayı Mert ile paylaşmak istedi"
   - Cümle 2: «Hayri çok acıkmıştı ve çantasındaki dondurmayı Mert ile paylaşmak istedi.»
   - Açıklama: Hayri çantada dondurma olduğunu biliyor ama sonra pembe damlaların kaynağını bilmiyormuş gibi merak ediyorlar.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İkisi de bu damlaları çok merak etti"
   - Cümle 4: «İkisi de bu damlaları çok merak etti.»
   - Açıklama: Hayri çantasında dondurma olduğunu biliyor ama pembe damlaların kaynağı ona bir sır gibi anlatılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0052` birebir aynı, ardından `@onarim: 0594e901ddd26727d3c518bc033642e79eac2991`, sonra gövde.

### Hikâye 8: tohum hayri-0054 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0054
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: bir şey yapmak
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'bez', fiil 'yarışmak', sıfat 'cesur'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: teknenin yelkeni yoktu ve tekne suda gitmedi | bezin hepsini açıp çubuğa takarak büyük bir yelken yaptı
@tohum: hayri-0054
@degisim: cesur -> büyük
Rüzgar deniz kıyısında hafif hafif esiyordu. Hayri kumda bir tahta, bir çubuk ve bir bez buldu. Tahtadan küçük bir tekne yaptı ama yelkeni olmadığı için tekne suda gitmedi. Hayri abarttı ve bezin hepsini iyice açtı. Bezi çubuğa geçirdi ve büyük bir yelken yaptı. Çubuğu teknedeki bir deliğe taktı. Sonra tekneyi sığ suya bıraktı. Büyük yelken rüzgarla şişti ve tekne hızla yüzmeye başladı. Hayri kıyıda koşarak tekneyle yarıştı. Hayri çok mutluydu, çünkü kendi yaptığı tekne sonunda suda ilerliyordu.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri kumda bir tahta, bir çubuk ve bir bez buldu"
   - Cümle 2: «Hayri kumda bir tahta, bir çubuk ve bir bez buldu.»
   - Açıklama: Çözümün bütün malzemeleri sebepsizce aynı anda kumda beliriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve bezin"
   - Cümle 4: «Hayri abarttı ve bezin hepsini iyice açtı.»
   - Açıklama: 'Abarttı' soyut bir kelime; 3 yaşındaki çocuk bilmez ve burada anlamı da yerine oturmuyor.
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abarttı ve bezin hepsini iyice açtı"
   - Cümle 4: «Hayri abarttı ve bezin hepsini iyice açtı.»
   - Açıklama: Karttaki özellik olayları sözle abartmaktır; burada abartma bezi büyük açmak olarak yanlış kullanılıyor.
   - Açıklama: Karttaki özellik olayları abartmak (anlatmak) iken burada bezi fazla açmak anlamında kullanılmış.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonra tekneyi sığ suya bıraktı"
   - Cümle 7: «Sonra tekneyi sığ suya bıraktı.»
   - Açıklama: Çocuğun tek başına suya tekne bırakıp kıyıda onunla yarışması suya yaklaşmayı örnekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0054` birebir aynı, `@degisim: cesur -> büyük` (tutuyorsan), ardından `@onarim: 0fe13878b0fc7b062d53d8a41a7abf3f5f861b60`, sonra gövde.

### Hikâye 9: tohum hayri-0057 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0057
- yer: park (Mahallenin çocuk parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'çim', fiil 'gizlenmek', sıfat 'yuvarlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: saklambaçta sayarken gizlice gözlerini açtı | özür diledi ve gözlerini kapayıp yeniden saydı
@tohum: hayri-0057
Hayri ile Akın parkta saklambaç oynuyordu. Ama Hayri sayarken gizlice gözlerini açtı. Akın bunu gördü ve çok üzüldü. "Hayri, sen bana baktın, bu olmaz!" dedi Akın. Hayri yanlış yaptığını anladı. "Haklısın, Akın. Özür dilerim," dedi Hayri. Hayri, çalıştığı dükkandan getirdiği yuvarlak kutudaki baklavayı Akın ile paylaştı. Akın tatlıyı yedi ve yine gülümsedi. Sonra Hayri gözlerini sıkıca kapadı ve ona kadar saydı. Akın çimlerin üstünden koştu ve büyük ağacın arkasına gizlendi. Hayri parkı dolaştı ve sonunda Akın'ı buldu. İkisi birlikte güldü. "Çok güzel oynadık, Hayri, bir daha oynayalım!" dedi Akın.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "yuvarlak kutudaki baklavayı Akın ile paylaştı"
   - Cümle 8: «Hayri, çalıştığı dükkandan getirdiği yuvarlak kutudaki baklavayı Akın ile paylaştı.»
   - Açıklama: Özür ve yeniden saymaya ek olarak baklava ikramı çözümü sebebe yönelmeyen üçüncü bir adımla uzatıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı dükkandan getirdiği yuvarlak kutudaki baklavayı Akın ile paylaştı"
   - Cümle 8: «Hayri, çalıştığı dükkandan getirdiği yuvarlak kutudaki baklavayı Akın ile paylaştı.»
   - Açıklama: Baklava kutusu sebepsiz beliriyor ve sorunla ilgisi olmayan bir ayrıntı olarak çözüme sokuluyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı dükkandan getirdiği yuvarlak kutudaki baklavayı"
   - Cümle 8: «Hayri, çalıştığı dükkandan getirdiği yuvarlak kutudaki baklavayı Akın ile paylaştı.»
   - Açıklama: Baklava kutusu sebepsiz beliriyor ve saklambaç sorununun çözümüne hiçbir katkı yapmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0057` birebir aynı, ardından `@onarim: 3970e451fb8fdd3dddefa26080dd3cdaf69665fd`, sonra gövde.

### Hikâye 10: tohum hayri-0058 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0058
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'hamur', fiil 'kapamak', sıfat 'incecik'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: ekmek incecikti ve domates kenardan kaydı | ekmeği ikiye katlayıp kenarlarını kapadı
@tohum: hayri-0058
@degisim: hamur -> sandviç
Hayri parkta ilk kez kendi sandviçini yapmayı denedi. Çok acıkmıştı ve bir dilim ekmeğe peynirle domates koydu. Ama ekmek incecikti ve domates hemen kenardan dışarı kaydı. Hayri durdu ve sandviçe dikkatle baktı. Sonra domatesi ekmeğin ortasına geri koydu. Ekmeği ikiye katlayıp kenarlarını sıkıca kapadı. Bu kez hiçbir şey kaymadı. Hayri büyük bir ısırık aldı ve gülümsedi. Peynir de domates de içeride kalmıştı. Hayri çok sevindi, çünkü ilk sandviçini kendisi yapmıştı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ekmek incecikti ve domates hemen kenardan dışarı kaydı"
   - Cümle 3: «Ama ekmek incecikti ve domates hemen kenardan dışarı kaydı.»
   - Açıklama: Ekmeğin inceliği domatesin kaymasına akla yatkın bir sebep değil ve katlama çözümü inceliğe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0058` birebir aynı, `@degisim: hamur -> sandviç` (tutuyorsan), ardından `@onarim: aeb1d3dbadfcdb1c4e3a30bd9e580e910b5de5bd`, sonra gövde.

### Hikâye 11: tohum hayri-0059 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0059
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'limonata', fiil 'temizlemek', sıfat 'yırtık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: çantanın içi ıslaktı | çantayı boşalttı ve kapağı açık şişeyi buldu
@tohum: hayri-0059
Hayri deniz kıyısında Basri Amca ile kumda oturuyordu. Hayri acıkmıştı ve ekmeğini Basri Amca ile paylaşmak istedi. Ama çantasını açınca her şey ıslaktı. "Basri Amca, çantam neden ıslak?" diye sordu Hayri. "Bilmiyorum, Hayri, içine birlikte bakalım," dedi Basri Amca. Hayri her şeyi çantadan tek tek çıkardı. İçinden bir kutu ekmek, yırtık bir bez ve limonata şişesi çıktı. Şişenin kapağı açıktı, limonata oradan çantaya akıyordu! Hayri kapağı sıkıca kapattı. Sonra bezle çantanın içini güzelce temizledi. Kutudaki ekmek kuruydu. Hayri ekmeği ve kalan limonatayı Basri Amca ile paylaştı. Hayri çok sevindi, çünkü çantanın neden ıslak olduğunu bulmuştu.
```

**Hakem bulguları (3):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ekmeğini Basri Amca ile paylaşmak"
   - Cümle 2: «Hayri acıkmıştı ve ekmeğini Basri Amca ile paylaşmak istedi.»
   - Açıklama: 'Basri Amca ile' art arda iki cümlede gereksiz yere tekrarlanıyor; 'onunla' yeterdi.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra bezle çantanın içini güzelce temizledi"
   - Cümle 10: «Sonra bezle çantanın içini güzelce temizledi.»
   - Açıklama: Çözüm boşaltma, kapağı kapatma ve temizleme olarak ikiden fazla adım sürüyor.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kutudaki ekmek kuruydu"
   - Cümle 11: «Kutudaki ekmek kuruydu.»
   - Açıklama: Çantada her şeyin ıslak olduğu söylenmişken ekmek kuru çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0059` birebir aynı, ardından `@onarim: 2e456876eb235001c34122237a162bca117ca974`, sonra gövde.

### Hikâye 12: tohum hayri-0061 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0061
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'atkı', fiil 'yaymak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: uçurtmanın kuyruğu yoktu ve uçurtma dönüp düşüyordu | atkısını uçurtmaya uzun bir kuyruk olarak bağladı
@tohum: hayri-0061
Rüzgar esiyordu ve gökyüzü beyaz bulutlarla doluydu. Hayri parkta ilk kez uçurtma uçurmayı deniyordu. Ama uçurtmanın kuyruğu yoktu ve uçurtma havada dönüp düşüyordu. Hayri uçurtmayı çimlere yaydı ve dikkatle baktı. Sonra boynundaki uzun kırmızı atkıyı çıkardı. Hayri abarttı ve kuyruğu çok uzun yapmak istedi. Bütün atkıyı uçurtmanın alt ucuna sıkıca bağladı. Hayri ipi tuttu ve rüzgara karşı koştu. Bu kez uçurtma hiç dönmedi. Kırmızı kuyruğuyla yavaş yavaş yükseldi. Hayri çok sevindi, çünkü ilk uçurtmasını kendisi uçurmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve kuyruğu"
   - Cümle 6: «Hayri abarttı ve kuyruğu çok uzun yapmak istedi.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abarttı ve kuyruğu çok uzun yapmak istedi"
   - Cümle 6: «Hayri abarttı ve kuyruğu çok uzun yapmak istedi.»
   - Açıklama: Kartın özellikler alanında abartmak olayları abartarak anlatmaktır; burada özellik yanlış anlamda, işi aşırı yapmak olarak kullanılıyor.
   - Açıklama: Karttaki özellik olayları abartmaktır; burada kuyruğu uzun yapmak olarak zorlama ve karttan farklı kullanılıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri abarttı ve kuyruğu çok uzun yapmak istedi"
   - Cümle 6: «Hayri abarttı ve kuyruğu çok uzun yapmak istedi.»
   - Açıklama: Abartma bir sonuç doğuracakmış gibi kuruluyor ama hiçbir işe yaramıyor.
   - Açıklama: Abartma sanki bir sonuç doğuracakmış gibi kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0061` birebir aynı, ardından `@onarim: fca87b0c414f67d07f9f078bfbd05c11457df094`, sonra gövde.
