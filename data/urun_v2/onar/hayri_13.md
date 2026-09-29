# Editör görevi (onarım): Hayri, onarım partisi 13

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar13.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar13.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0042 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0042
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'portakal', fiil 'sokulmak', sıfat 'iyi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar kumu portakalın üstüne savurdu | tabağı kayanın arkasına götürdü ve oraya sokuldu
@tohum: hayri-0042
Rüzgar denizden sert sert esiyordu. Hayri kumda baklava dükkanı oyunu oynuyordu. Portakalını baklava gibi parçalara bölüp bir tabağa koymuştu. Ama rüzgar kumu portakalın üstüne savurdu. Hayri kumlu portakal yemek istemiyordu. Etrafına baktı ve büyük bir kaya gördü. Kayanın arkasında rüzgar yoktu. Hayri baklava dükkanında tepsi taşımayı iyi öğrenmişti. Tabağı iki eliyle dikkatle kaldırdı ve kayaya götürdü. Sonra kayanın dibine sokuldu ve tabağı kucağına koydu. Burada portakalın üstüne hiç kum gelmedi. Sonra tatlı bir parça yedi ve güldü. Hayri bundan sonra rüzgarlı günlerde kayanın arkasında oynadı.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar kumu portakalın üstüne savurdu"
   - Cümle 4: «Ama rüzgar kumu portakalın üstüne savurdu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
   - Açıklama: Sorun ilk 3 cümlede değil, ancak 4. cümlede söyleniyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra tatlı bir parça yedi"
   - Cümle 12: «Sonra tatlı bir parça yedi ve güldü.»
   - Açıklama: Portakalın üstüne zaten kum gelmişken ve Hayri kumlu portakal yemek istemezken aynı parçaları temizlemeden yiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0042` birebir aynı, ardından `@onarim: 784580a5485dc3bea29af16c9651f6ab55d29532`, sonra gövde.

### Hikâye 2: tohum hayri-0043 (deneme 2 -> 3)

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
@degisim: yelpaze -> kabuk
Kumsal geniş ve ferahtı, orada başka kimse yoktu. Hayri, Yumak için kumdan kocaman bir kemik yapıyordu. Bu bir sürprizdi ama Yumak topunu bırakıp geldi ve kemiği bozdu. Hayri biraz düşündü. Sonra Yumak'ın kırmızı topunu kayaların yanına götürdü ve kuma gömdü. Hayri işi abarttı ve topun üstüne kocaman bir kum tepesi yaptı. Yumak topun kokusunu aldı ve orada uzun uzun kumu eşeledi. Hayri hemen işine döndü ve kum kemiğini bitirdi. Üstüne beyaz kabuklar dizdi. "Yumak, gel, sana bir kemik yaptım!" dedi Hayri. Yumak topuyla koşup geldi ve kuyruğunu salladı. Hayri bundan sonra sürpriz hazırlarken önce Yumak'ın topunu sakladı.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "orada başka kimse yoktu"
   - Cümle 1: «Kumsal geniş ve ferahtı, orada başka kimse yoktu.»
   - Açıklama: Çocuk deniz kıyısında yanında hiçbir büyük olmadan yalnız bırakılıyor; taklit edilirse tehlikeli olabilir.
   - Açıklama: Küçük bir çocuk büyük olmadan, yalnız başına deniz kıyısında oynuyor; taklit edilirse tehlikeli.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kumsal geniş ve ferahtı"
   - Cümle 1: «Kumsal geniş ve ferahtı, orada başka kimse yoktu.»
   - Açıklama: 'Ferah' kelimesi 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Ferah' kelimesini 3 yaşındaki çocuk bilmez.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri işi abarttı"
   - Cümle 6: «Hayri işi abarttı ve topun üstüne kocaman bir kum tepesi yaptı.»
   - Açıklama: 'İşi abartmak' soyut bir anlatım, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'İşi abartmak' soyut bir anlatım, 3 yaşındaki çocuk anlamaz.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri işi abarttı ve topun"
   - Cümle 6: «Hayri işi abarttı ve topun üstüne kocaman bir kum tepesi yaptı.»
   - Açıklama: Karttaki özellik olayları abartmak (anlatırken) iken burada iş abartılıyor ve çözüme katkısı olmayan süs olarak kullanılıyor.
   - Açıklama: Tohumdaki özellik olayları abartmak (anlatırken), burada iş abartılıyor; özellik karttaki anlamıyla kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0043` birebir aynı, `@degisim: yelpaze -> kabuk` (tutuyorsan), ardından `@onarim: 1e149649cc099faa58472656c1cdd467665b116c`, sonra gövde.

### Hikâye 3: tohum hayri-0044 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0044
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'basamak', fiil 'buruşturmak', sıfat 'çabuk'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: kalp gibi bir bulut çıktı ama arkadaşı uyuyordu | sandviçi burnuna yaklaştırdı ve arkadaşını uyandırdı
@tohum: hayri-0044
Hayri kamp yerinde çok acıkmıştı ve iki sandviç yapıyordu. Birden gökyüzünde kalp şeklinde büyük bir bulut gördü. Hayri bulutu Kamil'e göstermek istedi ama Kamil basamakta uyuyordu. Hayri çabuk olmalıydı, çünkü bulut yavaş yavaş dağılıyordu. "Kamil, uyan, bak!" diye seslendi Hayri. Ama Kamil uyanmadı. Hayri sandviçi kağıdından çıkardı ve kağıdı buruşturup cebine koydu. Sonra sandviçi Kamil'in burnuna yaklaştırdı. Kamil sandviçi kokladı ve gözlerini açtı. "Kamil, yukarı bak, bulut kalp gibi!" dedi Hayri. Kamil başını kaldırdı ve bulutu gördü. İkisi basamağa oturdu, sandviç yedi ve buluta baktı. Hayri çok sevindi, çünkü bulutu Kamil ile birlikte görmüştü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kağıdı buruşturup cebine koydu"
   - Cümle 7: «Hayri sandviçi kağıdından çıkardı ve kağıdı buruşturup cebine koydu.»
   - Açıklama: Kağıdı buruşturup cebe koymak işlevsiz bir ayrıntı.
   - Açıklama: Kağıdın buruşturulup cebe konması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0044` birebir aynı, ardından `@onarim: 8d6b8ecbd7fbafb6db14dd1716ee81c8bc70d1b5`, sonra gövde.

### Hikâye 4: tohum hayri-0045 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0045
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'flüt', fiil 'belirmek', sıfat 'yapışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: iki çocuk da tek flütü ilk çalmak istedi | sırayla çalmayı ve baklava yemeyi buldu
@tohum: hayri-0045
Rüzgar ağaçların arasında esiyordu. Akın kamp yerinde küçük bir flüt çıkardı ve Hayri'ye gösterdi. İkisi de onu ilk çalmak istedi, ama tek flüt vardı. Hayri biraz düşündü ve çantasını açtı. İçinde, çalıştığı baklava dükkanından getirdiği tatlılar vardı. Hayri sırayla oynamayı söyledi. Bir çocuk çalarken öteki baklava yiyecekti. Önce Akın yavaş bir şarkı çaldı. Hayri onu dinlerken bir baklava yedi. Sonra sıra Hayri'ye geldi. Parmakları yapışkandı, bu yüzden önce ellerini suyla yıkadı. Hayri neşeli bir şarkı çaldı ve Akın da tatlısını yedi. Akın'ın yüzünde kocaman bir gülümseme belirdi. Hayri bundan sonra flütü hep Akın ile sırayla çaldı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "baklava dükkanından getirdiği tatlılar"
   - Cümle 5: «İçinde, çalıştığı baklava dükkanından getirdiği tatlılar vardı.»
   - Açıklama: Baklava sorunu çözmek için gerekmeden beliriyor; sırayla çalmak tek başına yeterliyken çözüme sebepsiz bir öğe ekleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri sırayla oynamayı söyledi"
   - Cümle 6: «Hayri sırayla oynamayı söyledi.»
   - Açıklama: Flüt çalınır, oynanmaz; 'sırayla çalmayı' olmalı.
   - Açıklama: Flüt oynanmaz, çalınır; 'sırayla çalmayı' olmalı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "önce ellerini suyla yıkadı"
   - Cümle 11: «Parmakları yapışkandı, bu yüzden önce ellerini suyla yıkadı.»
   - Açıklama: El yıkama ve suyun sebepsizce belirmesi sıra sorununun çözümüne hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0045` birebir aynı, ardından `@onarim: 1cf4c43b3905e846f5bc8363a9ece78f1a02adfe`, sonra gövde.

### Hikâye 5: tohum hayri-0046 (deneme 1 -> 2)

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
Parkın kum havuzunda Hayri pasta yapma oyunu oynuyordu. Hayri abartarak bir kule kadar yüksek bir pasta yapmak istedi. Ama kum çok kuruydu ve pasta hep dağıldı. Hayri biraz düşündü ve su şişesini açtı. Suyu oyuncak bardağıyla ölçtü ve iki bardak kuma döktü. Islak kumu eski kovasına sıkıca bastırdı. Sonra kovayı ters çevirdi ve yavaşça kaldırdı. Kumdan pasta bu kez hiç yıkılmadı. Hayri onun üstüne iki kat daha yaptı. Pasta bir kule gibi yükseldi. Hayri onu yapraklarla süsledi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak bir kule"
   - Cümle 2: «Hayri abartarak bir kule kadar yüksek bir pasta yapmak istedi.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez ve burada yerinde de değil.
   - Açıklama: 'Abartarak' soyut ve küçük çocuğa uygun olmayan bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0046` birebir aynı, `@degisim: mıknatıs -> kova` (tutuyorsan), ardından `@onarim: 88fcefdf63cffd652040e69ee3232c1cd8a05fdc`, sonra gövde.

### Hikâye 6: tohum hayri-0047 (deneme 1 -> 2)

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
Rüzgar kıyıda hızlı esiyordu. Hayri denizin kenarında yürüyor ve dalgaları izliyordu. Birden rüzgar mavi şapkasını başından kaptı ve uçurdu. Hayri abartarak şapkanın denizin öbür ucuna gittiğini düşündü. Ama sonra durdu ve etrafa dikkatle baktı. Önce kumun üstünde aradı, orada yoktu. Sonra büyük taşların arkasına baktı. Şapka orada, çamurlu bir çukurun içindeydi. Hayri onu alıp suya götürdü. Şapkayı sığ suda ıslattı ve iyice yıkadı. Mavi şapka yine tertemiz oldu. Hayri çok sevindi, çünkü kaybolan şapkasını bulmuştu.
```

**Hakem bulguları (7):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak şapkanın denizin"
   - Cümle 4: «Hayri abartarak şapkanın denizin öbür ucuna gittiğini düşündü.»
   - Açıklama: 'Abartarak düşünmek' soyut bir anlatım, 3 yaşındaki çocuk anlamaz.
   - Açıklama: 'Abartarak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak şapkanın denizin öbür ucuna"
   - Cümle 4: «Hayri abartarak şapkanın denizin öbür ucuna gittiğini düşündü.»
   - Açıklama: Tohumdaki abartma özelliği anılıp hemen bırakılıyor ve sorunun çözümünde işe yaramıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak şapkanın denizin öbür ucuna gittiğini düşündü"
   - Cümle 4: «Hayri abartarak şapkanın denizin öbür ucuna gittiğini düşündü.»
   - Açıklama: Tohumdaki abartma özelliği çözüme hiç katkı vermiyor, yalnız anılıp bırakılıyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Şapka orada, çamurlu bir çukurun içindeydi"
   - Cümle 8: «Şapka orada, çamurlu bir çukurun içindeydi.»
   - Açıklama: Kayıp şapka sorununa bir de çamurlanan şapka sorunu ekleniyor, hikayede iki sorun oluyor.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "çamurlu bir çukurun içindeydi"
   - Cümle 8: «Şapka orada, çamurlu bir çukurun içindeydi.»
   - Açıklama: Şapkanın çamurlanıp yıkanması, bulma sorunundan sonra ikinci bir sorun açıyor.
6. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri onu alıp suya götürdü"
   - Cümle 9: «Hayri onu alıp suya götürdü.»
   - Açıklama: Tek başına bir çocuğun deniz suyuna gidip içinde şapka yıkaması taklit edilince tehlikeli olabilir.
7. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şapkayı sığ suda ıslattı ve iyice yıkadı"
   - Cümle 10: «Şapkayı sığ suda ıslattı ve iyice yıkadı.»
   - Açıklama: Çözüm şapkayı bulmakla bitmiyor, kumda arama, taşlara bakma ve yıkamayla ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0047` birebir aynı, `@degisim: pizza -> şapka` (tutuyorsan), ardından `@onarim: 58638234845985406c7d7a0e334351a2224ba274`, sonra gövde.

### Hikâye 7: tohum hayri-0048 (deneme 1 -> 2)

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
@plan: çukur sudan uzaktı ve içine su gelmedi | çukurdan denize doğru ince bir yol kazdı
@tohum: hayri-0048
Hayri deniz kıyısında küreğiyle yumuşak kumda bir çukur kazıyordu. Hayri abartarak kocaman bir havuz yapmak istedi. Ama çukur sudan uzaktı ve içine hiç su gelmedi. Hayri durdu ve denize dikkatle baktı. Dalgaların kıyıya gelip geri gittiğini fark etti. Sonra çukurdan denize doğru ince bir yol kazdı. Az sonra bir dalga geldi. Su yolun içinde yavaş yavaş ilerledi ve çukura aktı. Dalgalar geldi ve havuz biraz daha doldu. Hayri sevinçle zıpladı ve ellerini çırptı. Hayri bundan sonra havuzuna suyu hep böyle bir yoldan getirdi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak kocaman bir"
   - Cümle 2: «Hayri abartarak kocaman bir havuz yapmak istedi.»
   - Açıklama: 'abartarak' bir isteği niteleyemez; kelime yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak kocaman bir havuz yapmak istedi"
   - Cümle 2: «Hayri abartarak kocaman bir havuz yapmak istedi.»
   - Açıklama: 'Abartarak istemek' anlamca uygun değil ve soyut bir kelime kullanılmış.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak kocaman bir havuz"
   - Cümle 2: «Hayri abartarak kocaman bir havuz yapmak istedi.»
   - Açıklama: Tohumdaki abartma özelliği olayları abartmak olarak değil istek olarak geçiyor ve çözümde işe yaramıyor.
   - Açıklama: Karttaki özellik olayları abartmak; burada abartma yalnız süs olarak geçiyor ve sorunun çözümüne hiç katkı yapmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0048` birebir aynı, ardından `@onarim: c2a634caded9131c771a264eb762bb11dd35b7f8`, sonra gövde.

### Hikâye 8: tohum hayri-0049 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0049
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'güneş', fiil 'selamlamak', sıfat 'mutsuz'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: acıkınca köpeğe hiç bakmadı | köpekten özür diledi ve başını okşadı
@tohum: hayri-0049
Ormandaki kamp yerinde güneş yeni doğuyordu. Hayri çok acıkmıştı ve ekmeğine peynir koyuyordu. Yumak koşup onu selamladı, ama Hayri ona hiç bakmadı. Yumak kuyruğunu indirdi ve bir ağacın altına oturdu. Köpek çok mutsuz görünüyordu. Hayri bunu görünce üzüldü. Ekmeğini bıraktı ve Yumak'ın yanına gitti. "Özür dilerim, Yumak, sana günaydın demedim," dedi Hayri. Sonra onun başını yavaşça okşadı. Yumak havladı ve kuyruğunu yine salladı. "Günaydın, Yumak, gel birlikte oturalım," dedi Hayri. Sonra Hayri ile Yumak ağacın altında mutlu mutlu kahvaltı yaptı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "acıkınca köpeğe hiç bakmadı"
   - Cümle 0 (plan satırı): «acıkınca köpeğe hiç bakmadı | köpekten özür diledi ve başını okşadı»
   - Açıklama: Kartın güvenli özellik kullanımı satırı yemek sevgisini paylaşmak ya da beklemek olarak gösterir; burada açlık arkadaşını görmezden gelmenin nedeni oluyor.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "köpekten özür diledi ve başını okşadı"
   - Cümle 0 (plan satırı): «acıkınca köpeğe hiç bakmadı | köpekten özür diledi ve başını okşadı»
   - Açıklama: Planda Hayri köpeği okşuyor ama gövdede başı okşayan Yumak.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0049` birebir aynı, ardından `@onarim: 77aa83261985e9602b75971130ed59300ec99788`, sonra gövde.

### Hikâye 9: tohum hayri-0050 (deneme 1 -> 2)

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
Rüzgar ormanda hızlı hızlı esiyordu. Hayri kamp yerinde yere büyük bir örtü yaymak istedi. Ama rüzgar örtünün kenarlarını hep havaya kaldırdı. Hayri onu tek başına tutamadı. "Basri Amca, bana yardım eder misin?" diye sordu Hayri. "Tabii, hemen geliyorum," dedi Basri Amca. Basri Amca iki köşeyi sıkıca tuttu. Hayri de dört köşeye birer büyük taş koydu. Artık rüzgar örtüyü hiç kaldıramadı. Hayri, çalıştığı baklava dükkanından bir kutu baklava getirmişti. Kutu örtünün tam ortasına kondu. Kutudaki baklava ikisine de yeterliydi. Basri Amca bir dilim yedi ve gülümsedi. Hayri çok sevindi, çünkü örtü artık yerinde duruyordu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri, çalıştığı baklava dükkanından"
   - Cümle 10: «Hayri, çalıştığı baklava dükkanından bir kutu baklava getirmişti.»
   - Açıklama: Tohumdaki baklava özelliği sorunu çözmüyor, yalnız süs olarak ekleniyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çalıştığı baklava dükkanından bir kutu baklava getirmişti"
   - Cümle 10: «Hayri, çalıştığı baklava dükkanından bir kutu baklava getirmişti.»
   - Açıklama: Baklava kutusu sorun çözüldükten sonra sebepsizce beliriyor ve örtü sorunuyla ilgisi olmayan işlevsiz bir ayrıntı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir kutu baklava getirmişti"
   - Cümle 10: «Hayri, çalıştığı baklava dükkanından bir kutu baklava getirmişti.»
   - Açıklama: Baklava kutusu sorun çözüldükten sonra sebepsiz beliriyor ve olayla bağı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0050` birebir aynı, `@degisim: paspas -> örtü` (tutuyorsan), ardından `@onarim: b638cd090350d5ef98ce562a6a55d88d42fa0915`, sonra gövde.

### Hikâye 10: tohum hayri-0051 (deneme 1 -> 2)

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
Bir sabah Hayri kamp yerinde öğle yemeğini bekliyordu. Çok acıkmıştı, bu yüzden yemeğe kadar kozalakları bir kovaya attı. Ama kova patlaktı ve kozalaklar delikten yere düştü. Bir kozalak yokuştan aşağı yuvarlandı. Hayri arkasından koştu ve ona yetişti. Sonra deliğe baktı ve biraz düşündü. Sarı yağmurluğunu çıkardı, katladı ve kovanın dibine koydu. Artık delik kapanmıştı. Hayri kozalağı yine kovaya attı. Bu kez kozalak yere düşmedi. Hayri sevinçle zıpladı ve bir tane daha attı. Hayri yemek saatine kadar kozalak oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çok acıkmıştı, bu yüzden"
   - Cümle 2: «Çok acıkmıştı, bu yüzden yemeğe kadar kozalakları bir kovaya attı.»
   - Açıklama: 'Bu yüzden' bağlacı yanlış anlamda; acıkmak kozalak atmanın sebebi değil.
   - Açıklama: 'Bu yüzden' yanlış kullanılmış; acıkmak kozalak atmanın nedeni değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çok acıkmıştı, bu yüzden yemeğe"
   - Cümle 2: «Çok acıkmıştı, bu yüzden yemeğe kadar kozalakları bir kovaya attı.»
   - Açıklama: Tohumdaki acıkma özelliği patlak kova sorununun çözümünde işe yaramıyor, yalnız başlangıç süsü olarak geçiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çok acıkmıştı, bu yüzden yemeğe kadar kozalakları bir kovaya attı"
   - Cümle 2: «Çok acıkmıştı, bu yüzden yemeğe kadar kozalakları bir kovaya attı.»
   - Açıklama: Acıkmış olmak kozalakları kovaya atmanın sebebi olamaz; olay öncekinden çıkmıyor.
   - Açıklama: Acıkmak kozalakları kovaya atmanın sebebi olamaz; olaylar birbirinden çıkmıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri arkasından koştu ve ona yetişti"
   - Cümle 5: «Hayri arkasından koştu ve ona yetişti.»
   - Açıklama: Yokuştan yuvarlanan bir nesnenin arkasından koşmak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0051` birebir aynı, ardından `@onarim: 16a3b86f3a596bd4f0cdf8758ede63f9fe060269`, sonra gövde.

### Hikâye 11: tohum hayri-0052 (deneme 1 -> 2)

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
@plan: yerde pembe damlalar vardı ve çantaya gidiyordu | çantayı boşalttı ve eriyen dondurmayı buldu
@tohum: hayri-0052
Hayri ile Mert kamp yerinde ağaçların altında oturuyordu. Birden Hayri yerde küçük, pembe damlalar gördü. Damlalar sıra sıra çantaya doğru gidiyordu. İkisi de bunu çok merak etti. Tedbirli Mert çantaya hemen elini sokmadı. Hayri ise çantayı yavaşça yere boşalttı. İçinden ekmek, iki kaşık ve bir kutu çıktı. Kutunun kapağı açılmıştı ve çilekli dondurma eriyordu. Pembe damlalar ondan geliyordu! Hayri zaten çok acıkmıştı. Bir kaşığı Mert'e verdi ve kutuyu onunla paylaştı. Hayri ile Mert ağaçların altında dondurmayı mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "pembe damlalar vardı ve çantaya gidiyordu"
   - Cümle 0 (plan satırı): «yerde pembe damlalar vardı ve çantaya gidiyordu | çantayı boşalttı ve eriyen dondurmayı buldu»
   - Açıklama: Plan satırında damlalar için 'gidiyordu' fiili uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Damlalar sıra sıra çantaya doğru gidiyordu"
   - Cümle 3: «Damlalar sıra sıra çantaya doğru gidiyordu.»
   - Açıklama: Damlalar gitmez; fiil öznesine uymuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tedbirli Mert çantaya hemen elini sokmadı"
   - Cümle 5: «Tedbirli Mert çantaya hemen elini sokmadı.»
   - Açıklama: Mert'in tedbirliliği işe yarayacakmış gibi kuruluyor ama olayda hiçbir sonucu yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0052` birebir aynı, ardından `@onarim: d0411db96c48124c04de0440d526a843376e43c5`, sonra gövde.

### Hikâye 12: tohum hayri-0053 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0053
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: paylaşmak
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'plak', fiil 'birikmek', sıfat 'sessiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: arkadaşı yiyeceğini evde unutmuştu | sandviçini ikiye böldü ve arkadaşıyla paylaştı
@tohum: hayri-0053
@degisim: plak -> kitap
Bir sabah Hayri kamp yerinde çok acıkmıştı. Çantasından büyük bir sandviç çıkardı ve bir ağacın altına oturdu. Yanındaki Kamil'in ise hiç yiyeceği yoktu, çünkü onu evde unutmuştu. Kamil birikmiş yaprakların üstünde sessizce kitap okuyordu. Ama arada bir sandviçe bakıyordu. Hayri sandviçi ikiye böldü. "Al, Kamil, yarısı senin," dedi Hayri. "Teşekkür ederim, Hayri," dedi Kamil ve gülümsedi. Kamil yerken kitabından komik bir yer okudu. Hayri buna çok güldü. "Paylaşınca sandviç daha lezzetli oldu, Kamil!" dedi Hayri.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çünkü onu evde unutmuştu"
   - Cümle 3: «Yanındaki Kamil'in ise hiç yiyeceği yoktu, çünkü onu evde unutmuştu.»
   - Açıklama: 'Onu' zamiri hiç olmayan yiyeceği gösteriyor; neyi gösterdiği belirsiz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kitabından komik bir yer okudu"
   - Cümle 9: «Kamil yerken kitabından komik bir yer okudu.»
   - Açıklama: 'Yerken' ile yan yana 'yer' kelimesi kitap bölümü anlamında kullanılmış; çocuk için yanlış anlaşılır.
   - Açıklama: 'Yer' kelimesi 'bölüm' anlamında ve hemen önceki 'yerken' ile karışıyor; anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0053` birebir aynı, `@degisim: plak -> kitap` (tutuyorsan), ardından `@onarim: 6cf4a1835296e2690ab5e5b7057d881dfffc512f`, sonra gövde.
