# Editör görevi (onarım): Hayri, onarım partisi 32

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar32.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar32.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0080 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Kamil
@tohum: hayri-0080
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yüzük', fiil 'bitmek', sıfat 'masmavi'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Kamil
@plan: ağacın arkasından garip bir ses geliyordu | ağacın arkasına bakıp uyuyan arkadaşını buldu
@tohum: hayri-0080
@degisim: yüzük -> simit
Parkta hafif bir rüzgar esiyordu ve gökyüzü masmaviydi. Hayri, Kamil ile simit yemek için parka gelmişti. Kamil'i göremedi ama büyük ağacın arkasından garip bir ses geldi. Hayri bu sesi çok merak etti. Ağaca yürüdü ve arkasına baktı. Kamil ağacın dibinde uyuyordu. Garip ses Kamil'in burnundan geliyordu. Hayri çok acıkmıştı ama simidi yalnız yemek istemedi. Simidi Kamil'in burnuna yaklaştırdı. Kamil kokuyu aldı ve gözlerini açtı. "Hayri, simit mi getirdin?" diye sordu Kamil. "Evet, gel, birlikte yiyelim, Kamil," dedi Hayri. İkisi simidi yedi ve simit çabucak bitti. Hayri çok sevindi, çünkü garip sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri, Kamil ile simit yemek için parka gelmişti"
   - Cümle 2: «Hayri, Kamil ile simit yemek için parka gelmişti.»
   - Açıklama: Hayri parka Kamil ile birlikte gelmişken Kamil'i göremiyor ve onu ağacın dibinde uyurken buluyor; Kamil de simit getirildiğine şaşırıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0080` birebir aynı, `@degisim: yüzük -> simit` (tutuyorsan), ardından `@onarim: 6497700a44dc647626037a3195734f9f0474b95c`, sonra gövde.

### Hikâye 2: tohum hayri-0081 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0081
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'top', fiil 'saklamak', sıfat 'nazik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: dalga geldi ve topun yeri belli olmadı | kumun yüksek kalan yerini kazdı ve topu buldu
@tohum: hayri-0081
@degisim: nazik -> sarı
Dalgaların sesi kıyıdan geliyordu. Hayri hazine oyunu oynuyordu ve sarı topunu kumun altına sakladı. Ama bir dalga kumun üstünden geçti ve Hayri topun yerini bulamadı. Hayri eğildi ve kuma dikkatle baktı. Hayri topu saklarken abarttı ve üstüne çok fazla kum koydu. Bu yüzden bir yerde kum biraz yüksek kalmıştı. Hayri orayı elleriyle kazdı. Kumun altından sarı top çıktı. Hayri topu iki eliyle havaya kaldırdı ve güldü. Sonra topu dalgalardan uzağa, kuru kuma gömdü. Hayri oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri topu saklarken abarttı"
   - Cümle 5: «Hayri topu saklarken abarttı ve üstüne çok fazla kum koydu.»
   - Açıklama: 'Abarttı' soyut bir kelime ve 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri topu saklarken abarttı"
   - Cümle 5: «Hayri topu saklarken abarttı ve üstüne çok fazla kum koydu.»
   - Açıklama: Karttaki özellik olayları abartmaktır; burada abartma fazla kum koymak anlamında, karttaki gibi kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri topu saklarken abarttı ve üstüne çok fazla kum koydu"
   - Cümle 5: «Hayri topu saklarken abarttı ve üstüne çok fazla kum koydu.»
   - Açıklama: Karttaki özellik olayları abartmak; burada abartma fazla kum koymak anlamında, karttaki özellikten farklı kullanılmış.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri topu saklarken abarttı"
   - Cümle 5: «Hayri topu saklarken abarttı ve üstüne çok fazla kum koydu.»
   - Açıklama: Çözümü getiren yüksek kum bilgisi olaydan çıkmıyor, çözüm anında geriye dönük olarak ekleniyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri topu saklarken abarttı ve üstüne çok fazla kum koydu"
   - Cümle 5: «Hayri topu saklarken abarttı ve üstüne çok fazla kum koydu.»
   - Açıklama: Çözümü getiren fazla kum ayrıntısı sonradan sebepsizce ekleniyor ve dalganın kumu düzleştirmesiyle de uyuşmuyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bu yüzden bir yerde kum biraz yüksek kalmıştı"
   - Cümle 6: «Bu yüzden bir yerde kum biraz yüksek kalmıştı.»
   - Açıklama: Dalga kumun üstünden geçip yeri belirsizleştirdiği halde kumun yüksek kalan yeri hâlâ duruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0081` birebir aynı, `@degisim: nazik -> sarı` (tutuyorsan), ardından `@onarim: 15dad0579db5cb0c3dbf5d7ac941397566675a96`, sonra gövde.

### Hikâye 3: tohum hayri-0084 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0084
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ay', fiil 'vermek', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: koşarken arkadaşına çarptı ve onun sütü döküldü | özür diledi ve bardağını yeniden doldurdu
@tohum: hayri-0084
Bir akşam kamp masasında ılık süt vardı. Hayri gökyüzünde büyük bir ay gördü. Hayri, Mert'e gökyüzünü göstermek için koşarken ona çarptı ve Mert'in sütü döküldü. Mert boş bardağına üzgün üzgün baktı. Hayri hemen durdu ve Mert'in yanına gitti. "Özür dilerim, Mert, koşmamalıydım," dedi Hayri. Sonra masadaki sütten Mert'in bardağını yeniden doldurdu. Çalıştığı dükkandan getirdiği baklavayı da Mert'e verdi. Mert sütünü içti, baklavayı yedi ve gülümsedi. "Teşekkür ederim, Hayri," dedi Mert. "Hadi, Mert, şimdi aya birlikte bakalım!" dedi Hayri.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çalıştığı dükkandan getirdiği baklavayı"
   - Cümle 8: «Çalıştığı dükkandan getirdiği baklavayı da Mert'e verdi.»
   - Açıklama: Baklava daha önce kurulmadan sebepsizce beliriyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çalıştığı dükkandan getirdiği baklavayı da Mert'e verdi"
   - Cümle 8: «Çalıştığı dükkandan getirdiği baklavayı da Mert'e verdi.»
   - Açıklama: Baklava sebepsiz beliriyor ve sorunun çözümüne hiçbir katkısı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0084` birebir aynı, ardından `@onarim: fb7454cb0215b48f3d43210562d63e4652c1a1d3`, sonra gövde.

### Hikâye 4: tohum hayri-0089 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0089
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kırıntı', fiil 'yeşermek', sıfat 'hazırlıklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: köpek çok hızlıydı ve kırıntılar çabuk bitti | çantadan ikinci simidi çıkarıp oyuna devam etti
@tohum: hayri-0089
@degisim: hazırlıklı -> dolu
Hayri parkta Yumak ile koku oyunu oynuyordu. Hayri simit kırıntılarını yeşermiş çimlere saklıyor, Yumak da onları buluyordu. Ama Yumak çok hızlıydı ve kırıntılar çabuk bitti. Yumak kuyruğunu salladı ve Hayri'ye baktı. Hayri sık sık acıkırdı, bu yüzden çantası hep doluydu. Çantasında bir simit daha vardı. Simidi ikiye ayırdı ve yarısını kendisi yedi. Öbür yarısını küçük küçük kırıntı yaptı ve çimlere serpti. "Hadi, Yumak, bul bakalım!" dedi Hayri. Yumak burnunu yere yaklaştırdı ve çimlerde koştu. Her kırıntıyı buldukça sevinçle zıpladı ve havladı. Hayri çok sevindi, çünkü oyunları yarım kalmamıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "simit kırıntılarını yeşermiş çimlere"
   - Cümle 2: «Hayri simit kırıntılarını yeşermiş çimlere saklıyor, Yumak da onları buluyordu.»
   - Açıklama: 'Yeşermiş' çimlere uymayan, çocuğa yabancı bir sıfat; 'yeşil çimlere' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kırıntılarını yeşermiş çimlere saklıyor"
   - Cümle 2: «Hayri simit kırıntılarını yeşermiş çimlere saklıyor, Yumak da onları buluyordu.»
   - Açıklama: 'Yeşermiş' 3 yaşındaki çocuğun bilmeyeceği edebi bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0089` birebir aynı, `@degisim: hazırlıklı -> dolu` (tutuyorsan), ardından `@onarim: 8d786d8f5b27a2f2d20fb10cef2d84771171b32a`, sonra gövde.

### Hikâye 5: tohum hayri-0090 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0090
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'saman', fiil 'birleştirmek', sıfat 'tuhaf'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: kabuğun öbür yarısı yoktu çünkü dalgalar onu kırmıştı | kıyıda dolaşıp öbür yarısını buldu ve birleştirdi
@tohum: hayri-0090
@degisim: saman -> kabuk
Deniz kıyısında ıslak kumun üstünde tuhaf bir kabuk vardı. Hayri kabuğu eline aldı. Ama kabuğun öbür yarısı yoktu, çünkü dalgalar onu kırmıştı. Kabuğun üstünde pembe ve mavi çizgiler vardı. Hayri öbür yarısını bulmak için kıyıda yavaş yavaş yürüdü. Yine abarttı ve kumdaki bütün kabuklara tek tek baktı. Sonunda taşların arasında aynı çizgileri olan bir parça gördü. Hayri iki parçayı yan yana koydu ve birleştirdi. İki parça birbirine tam uydu ve çizgiler bir yıldız şekli yaptı. Hayri kabuğu iki eliyle tuttu ve ona güneşte uzun uzun baktı. Hayri çok sevindi, çünkü tuhaf kabuğun öbür yarısını bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yine abarttı ve kumdaki"
   - Cümle 6: «Yine abarttı ve kumdaki bütün kabuklara tek tek baktı.»
   - Açıklama: Kabuklara tek tek bakmak abartmak değildir ve 'yine' önceki bir abartıya dayanmıyor; kelime yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yine abarttı ve kumdaki"
   - Cümle 6: «Yine abarttı ve kumdaki bütün kabuklara tek tek baktı.»
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmez ve burada anlamı da belirsiz.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yine abarttı ve kumdaki bütün kabuklara"
   - Cümle 6: «Yine abarttı ve kumdaki bütün kabuklara tek tek baktı.»
   - Açıklama: Karttaki 'olayları abartmayı sever' özelliği yerine dikkatle arama abartma diye adlandırılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yine abarttı ve kumdaki bütün kabuklara tek tek baktı"
   - Cümle 6: «Yine abarttı ve kumdaki bütün kabuklara tek tek baktı.»
   - Açıklama: Karttaki özellik olayları abartmak; kabuklara tek tek bakmak abartma değil titizlik olarak kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0090` birebir aynı, `@degisim: saman -> kabuk` (tutuyorsan), ardından `@onarim: 6d76fa07bd30c8a5a802cebcd0c09ecec422828a`, sonra gövde.

### Hikâye 6: tohum hayri-0092 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0092
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'ipek', fiil 'hızlanmak', sıfat 'resimli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: dar yolda sıra beklemek arkadaşına sıkıcı geldi | koşarken komik sözlerle bağırıp arkadaşını güldürdü
@tohum: hayri-0092
@degisim: ipek -> kitap
Hayri ile Kamil ormandaki kamp yerinde koşu oyunu oynuyordu. Kamil resimli kitabını bitiş yeri olarak bir kütüğe koydu. Yol çok dardı, sırayla koşacaklardı ama Kamil beklemek istemedi. "Beklemek çok sıkıcı, Hayri," dedi Kamil. "Ben koşarken sana her şeyi anlatırım, Kamil," dedi Hayri. Hayri koşmaya başladı ve yolun ortasında hızlandı. "Kamil, ormanın en hızlı çocuğu şimdi geçiyor!" diye bağırdı Hayri. Hayri yine abartıyordu ve Kamil beklerken çok güldü. Hayri kitaba vardı ve el salladı. "Sıra sende, Kamil!" dedi Hayri. Bu kez Kamil koştu ve Hayri onu neşeyle bekledi. İki arkadaş sırayla koşmaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri yine abartıyordu"
   - Cümle 8: «Hayri yine abartıyordu ve Kamil beklerken çok güldü.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0092` birebir aynı, `@degisim: ipek -> kitap` (tutuyorsan), ardından `@onarim: 8281462deb57c2dfe67727bc1f1d07480c6900fc`, sonra gövde.

### Hikâye 7: tohum hayri-0093 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0093
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'yastık', fiil 'ayrılmak', sıfat 'sevinçli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kum çok kuruydu ve kule hemen yıkıldı | büyük bir çukur açıp ıslak kumla kule yaptı
@tohum: hayri-0093
@degisim: yastık -> kova
Bir sabah Hayri parkta kumdan kule yapma oyunu oynuyordu. Kovayı kumla doldurdu ve kumun üstüne ters çevirdi. Ama kum çok kuruydu ve kovadan ayrıldı, kule hemen yıkıldı. Hayri bir kez daha denedi ama kule olmadı. Hayri aşağıdaki kumun ıslak olduğunu biliyordu. Yine abarttı ve kumda çok büyük bir çukur açtı. Kovayı çukurun dibindeki ıslak kumla doldurdu ve yavaşça kaldırdı. Bu kez kule dik durdu. Çukur büyük olduğu için içinde çok ıslak kum vardı. Hayri o kumla beş kule daha yaptı. Sevinçli Hayri oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yine abarttı ve kumda"
   - Cümle 6: «Yine abarttı ve kumda çok büyük bir çukur açtı.»
   - Açıklama: 'Abarttı' 3 yaşındaki çocuk için soyut bir kelime ve 'yine' daha önce anlatılmamış bir abartıya gönderme yapıyor.
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Yine abarttı ve kumda"
   - Cümle 6: «Yine abarttı ve kumda çok büyük bir çukur açtı.»
   - Açıklama: Karttaki özellik olayları abartmaktır; burada abartma büyük çukur kazmak anlamında, karttaki gibi kullanılmıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sevinçli Hayri oyununa mutlu mutlu"
   - Cümle 11: «Sevinçli Hayri oyununa mutlu mutlu devam etti.»
   - Açıklama: 'Sevinçli' ve 'mutlu mutlu' aynı duyguyu gereksiz yere tekrarlıyor.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sevinçli Hayri oyununa mutlu mutlu devam etti"
   - Cümle 11: «Sevinçli Hayri oyununa mutlu mutlu devam etti.»
   - Açıklama: 'Sevinçli' ve 'mutlu mutlu' aynı duyguyu gereksiz yere tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0093` birebir aynı, `@degisim: yastık -> kova` (tutuyorsan), ardından `@onarim: a9ac63d48dd44a6a184b851db13522629329b605`, sonra gövde.

### Hikâye 8: tohum hayri-0094 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0094
- yer: park (Mahallenin çocuk parkı.)
- tema: kaybolan eşya
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'saksı', fiil 'gerinmek', sıfat 'uslu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: rüzgar esti ve şapka başından uçtu | rüzgarın estiği yöne yürüyüp şapkayı saksının yanında buldu
@tohum: hayri-0094
@degisim: uslu -> kırmızı
Hayri parktaki bankta oturdu ve keyifle gerindi. O anda rüzgar esti ve kırmızı şapkası başından uçtu. Hayri çevresine baktı ama şapkayı hiçbir yerde göremedi. Onu mutlaka bulmak istedi. Hayri biraz abarttı ve şapkanın rüzgarla çok uzağa uçtuğunu düşündü. Bu yüzden rüzgarın estiği yöne doğru yürüdü. Bankın arkasında büyük bir çiçek saksısı duruyordu. Hayri eğildi ve saksının yanına baktı. Şapka orada, çimenlerin üstündeydi. Şapkayı alıp başına sıkıca taktı. Hayri güldü ve çok sevindi, çünkü şapkasını bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri biraz abarttı ve şapkanın"
   - Cümle 5: «Hayri biraz abarttı ve şapkanın rüzgarla çok uzağa uçtuğunu düşündü.»
   - Açıklama: 'Abartmak' burada yanlış anlamda kullanılmış; şapkanın uzağa uçtuğunu düşünmek abartmak değildir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abarttı ve"
   - Cümle 5: «Hayri biraz abarttı ve şapkanın rüzgarla çok uzağa uçtuğunu düşündü.»
   - Açıklama: 'Abarttı' soyut bir kelime ve burada anlamı da oturmuyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri biraz abarttı ve şapkanın"
   - Cümle 5: «Hayri biraz abarttı ve şapkanın rüzgarla çok uzağa uçtuğunu düşündü.»
   - Açıklama: Tohumdaki abartma özelliği işe yaramıyor; şapka yakında bulunuyor ve abartma çözüme katkı vermiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şapkanın rüzgarla çok uzağa uçtuğunu düşündü"
   - Cümle 5: «Hayri biraz abarttı ve şapkanın rüzgarla çok uzağa uçtuğunu düşündü.»
   - Açıklama: Abartma ayrıntısı işe yarayacakmış gibi kuruluyor ama şapka hemen bankın arkasında çıkınca hiçbir işlevi kalmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0094` birebir aynı, `@degisim: uslu -> kırmızı` (tutuyorsan), ardından `@onarim: 65d710e8aff64ec9f24f6728e4a1e254ad9659ad`, sonra gövde.

### Hikâye 9: tohum hayri-0095 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0095
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'sandalye', fiil 'bükmek', sıfat 'yardımsever'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: köpeğin başı devrilen sandalyenin ayakları arasına sıkıştı | dizlerini büküp sandalyeyi yavaşça kaldırdı
@tohum: hayri-0095
@degisim: yardımsever -> boş
Deniz kıyısında Yumak durmadan havlıyordu. Hayri sese doğru yürüdü ve Yumak'ı gördü. Rüzgar boş bir sandalyeyi kuma devirmişti. Yumak koklarken başı sandalyenin ayakları arasına sıkışmıştı. Yumak çıkmak için çok uğraştı ama kurtulamadı. "Bekle, Yumak, mahallenin en güçlü çocuğu geldi!" dedi Hayri. Hayri biraz abartmıştı. Yumak kuyruğunu salladı ve kıpırdamadan bekledi. Hayri dizlerini büktü ve sandalyeyi iki eliyle sıkıca tuttu. Sonra sandalyeyi yavaşça yukarı kaldırdı. Yumak hemen başını çıkardı ve kumda zıpladı. Hayri sandalyeyi düz bir şekilde kuma koydu. Yumak koşup Hayri'nin elini yaladı. "Haydi, Yumak, şimdi birlikte oynayalım!" dedi Hayri.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Rüzgar boş bir sandalyeyi kuma devirmişti.»
   - Açıklama: Yumak'ın başının sıkışması ancak 4. cümlede söyleniyor, ilk 3 cümlede sorun açık değil.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "başı sandalyenin ayakları arasına sıkışmıştı"
   - Cümle 4: «Yumak koklarken başı sandalyenin ayakları arasına sıkışmıştı.»
   - Açıklama: Başı sıkışıp kurtulamayan köpek küçük çocuklar için tedirgin edici bir tehlike sahnesi.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "başı sandalyenin ayakları arasına sıkışmıştı"
   - Cümle 4: «Yumak koklarken başı sandalyenin ayakları arasına sıkışmıştı.»
   - Açıklama: Asıl sorun olan sıkışma ilk üç cümlede değil dördüncü cümlede söyleniyor.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 7: «Hayri biraz abartmıştı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kavram.
   - Açıklama: 'Abartmak' soyut bir kavram ve 'mahallenin en güçlü çocuğu' abartısı 3 yaşındaki çocuğa uygun değil.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri biraz abartmıştı"
   - Cümle 7: «Hayri biraz abartmıştı.»
   - Açıklama: Abartma notu olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Abartma ayrıntısı olaya hiçbir şey katmayan işlevsiz bir ek.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0095` birebir aynı, `@degisim: yardımsever -> boş` (tutuyorsan), ardından `@onarim: 0436ad39e613a080b629798119586df9b3e75449`, sonra gövde.

### Hikâye 10: tohum hayri-0096 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0096
- yer: park (Mahallenin çocuk parkı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'reçel', fiil 'ovmak', sıfat 'çiçekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: iki çocuk küçük salıncağa aynı anda binmek istedi | dükkandaki gibi ilk sırayı önce gelene verdi
@tohum: hayri-0096
@degisim: reçel -> salıncak
Bir sabah Akın parka koştu ve Hayri de arkasından geldi. İkisi de çiçekli salıncağa aynı anda binmek istedi. Ama salıncak küçüktü ve ikisi birden oturamıyordu. Akın üzüldü ve gözlerini ovdu. Hayri baklava dükkanında baklavayı hep ilk gelene verirdi. Parka ilk gelen de Akın'dı. Bu yüzden Hayri sırayı önce Akın'a verdi. Akın sallanırken Hayri salıncağı yavaşça itti. On kez itti ve sonra sırayı kendisi aldı. Bu kez Akın, Hayri'yi itti ve güldü. Hayri ile Akın çok sevindi, çünkü sırayla ikisi de salıncağa binmişti.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "ilk sırayı önce gelene"
   - Cümle 0 (plan satırı): «iki çocuk küçük salıncağa aynı anda binmek istedi | dükkandaki gibi ilk sırayı önce gelene verdi»
   - Açıklama: 'İlk sıra' ve 'önce' aynı şeyi söylüyor; plan satırında gereksiz tekrar var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0096` birebir aynı, `@degisim: reçel -> salıncak` (tutuyorsan), ardından `@onarim: d72e83e2826c8245e1bb1afabd9327897b9b5dd6`, sonra gövde.
