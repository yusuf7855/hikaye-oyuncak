# Editör görevi (onarım): Hayri, onarım partisi 10

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar10.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar10.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0040 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0040
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kek', fiil 'homurdanmak', sıfat 'utangaç'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: kayaların yanından homurdanır gibi bir ses geldi | kayalara gidip kuma gömülü boş şişeyi buldu
@tohum: hayri-0040
Rüzgar denizden sert sert esiyordu. Hayri ile Akın kumda oturmuş, kek yiyordu. Birden kayaların yanından homurdanır gibi garip bir ses geldi. "Bu ses bütün kumsalı sallıyor!" dedi Hayri abartarak. Akın güldü ve sesi dinledi. Hayri sesi merak etti ve kayalara doğru yürüdü. Kumda yarısı gömülü boş bir şişe vardı. Rüzgar şişenin ağzına esince bu ses çıkıyordu. Hayri şişeyi kumdan çekip aldı ve ses durdu. "Bak, o büyük ses bu küçük şişeden çıkıyormuş!" dedi Akın gülerek. Hayri utangaç utangaç güldü. Şişeyi çantasına koydu ve Akın'ın yanına döndü. Sonra ikisi keklerini mutlu mutlu yemeye devam etti.
```

**Hakem bulguları (5):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "homurdanır gibi garip bir ses"
   - Cümle 3: «Birden kayaların yanından homurdanır gibi garip bir ses geldi.»
   - Açıklama: Kayaların yanından gelen homurtuya benzer garip ses 3-6 yaş için korkutucu bir gerilim öğesi.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 4: «"Bu ses bütün kumsalı sallıyor!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğa uygun olmayan soyut bir kelime.
3. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "dedi Akın gülerek"
   - Cümle 10: «"Bak, o büyük ses bu küçük şişeden çıkıyormuş!" dedi Akın gülerek.»
   - Açıklama: Şişenin yanında yalnız Hayri var, Akın geride kaldığı için bu repliği Akın söyleyemez.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Hayri utangaç utangaç güldü"
   - Cümle 11: «Hayri utangaç utangaç güldü.»
   - Açıklama: 'Utangaç utangaç' dilbilgisel bir ikileme değil; 'utana utana' olmalı.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şişeyi çantasına koydu ve Akın'ın yanına döndü"
   - Cümle 12: «Şişeyi çantasına koydu ve Akın'ın yanına döndü.»
   - Açıklama: Akın kayaların yanında Hayri'yle konuşuyor ama sonra Hayri onun yanına geri dönüyor; Akın'ın yeri çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0040` birebir aynı, ardından `@onarim: dd74f704009c8c04ab2e8ec012e3ae6c0da1567b`, sonra gövde.

### Hikâye 2: tohum hayri-0041 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0041
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'oyuncak', fiil 'büyütmek', sıfat 'limonlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: kumdan pasta kuru kum yüzünden hep dağıldı | kovayla ıslak kum getirip pastayı büyüttü
@tohum: hayri-0041
Hayri deniz kıyısında kumdan pasta yapma oyunu oynuyordu. Çok acıkmıştı ama önce kocaman bir kum pastası yapmak istedi. Ama kum kuruydu ve pasta hemen dağıldı. Hayri oyuncak kovasını aldı ve su kenarına yürüdü. Kovayı ıslak kumla doldurdu ve geri döndü. Islak kumu kuru kuma karıştırdı ve pastayı büyüttü. Bu kez pasta sağlam durdu. Hayri pastanın üstüne beyaz kabuklar dizdi. Sonra çantasından limonlu bir kurabiye çıkardı. Hayri kocaman pastanın yanına oturdu. Kurabiyesini yedi ve pastasına mutlu mutlu baktı.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Ama kum kuruydu ve"
   - Cümle 3: «Ama kum kuruydu ve pasta hemen dağıldı.»
   - Açıklama: Bir önceki cümledeki 'ama'nın hemen ardından yeni cümle yine 'Ama' ile başlıyor; gereksiz tekrar.
   - Açıklama: Art arda iki cümlede 'ama' bağlacı gereksiz tekrarlanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra çantasından limonlu bir kurabiye çıkardı"
   - Cümle 9: «Sonra çantasından limonlu bir kurabiye çıkardı.»
   - Açıklama: Açlık ve kurabiye sorunla ilgisiz, pasta olayından çıkmayan işlevsiz bir yan iplik.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0041` birebir aynı, ardından `@onarim: e6e56488ccbb5ce55711ecd463f98c1467c77707`, sonra gövde.

### Hikâye 3: tohum hayri-0042 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

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
@plan: rüzgar kumu savurdu ve baklavanın çizgileri kayboldu | kayanın arkasına geçip çizgileri yeniden çizdi
@tohum: hayri-0042
Rüzgar denizden serin serin esiyordu. Hayri kumda baklava dükkanı oyunu oynuyordu ve kumdan bir tepsi baklava yapmıştı. Ama rüzgar kumu savurdu ve baklavanın çizgileri kayboldu. Hayri etrafına baktı ve büyük bir kaya gördü. Kayanın arkasında rüzgar yoktu. Hayri kayanın dibine sokuldu ve kumu orada düzeltti. Hayri dükkanda baklava kesmeyi iyi öğrenmişti. Bir çubukla kuma düzgün kareler çizdi. Sonra çantasından bir portakal çıkardı, soydu ve yedi. Portakalın kabuğunu küçük parçalara böldü. Her karenin ortasına bir parça koydu. Kum baklavası şimdi gerçek baklava gibi görünüyordu. Hayri bundan sonra rüzgarlı günlerde kayanın arkasında oynadı.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar kumu savurdu ve baklavanın çizgileri kayboldu"
   - Cümle 3: «Ama rüzgar kumu savurdu ve baklavanın çizgileri kayboldu.»
   - Açıklama: Kumdaki çizgilerin silinip yeniden çizilmesi önemsiz bir sorun.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra çantasından bir portakal çıkardı"
   - Cümle 9: «Sonra çantasından bir portakal çıkardı, soydu ve yedi.»
   - Açıklama: Portakal sebepsiz beliriyor ve sorunun çözümüyle ilgisiz bir süslemeye yarıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasından bir portakal çıkardı"
   - Cümle 9: «Sonra çantasından bir portakal çıkardı, soydu ve yedi.»
   - Açıklama: Portakal sebepsiz beliriyor ve rüzgarın çizgileri silme sorunuyla ilgisi yok.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Portakalın kabuğunu küçük parçalara böldü"
   - Cümle 10: «Portakalın kabuğunu küçük parçalara böldü.»
   - Açıklama: Çizgiler yeniden çizildikten sonra portakal kabuğuyla süsleme gibi fazladan adımlar ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0042` birebir aynı, ardından `@onarim: 9a9dd66d2049ae5c9dd261a7dc35af98c89347e7`, sonra gövde.

### Hikâye 4: tohum hayri-0043 (deneme 1 -> 2)

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
Deniz kıyısında hava ferah ve serindi. Hayri, Yumak için kumdan kocaman bir kemik yapıyordu. Bu bir sürprizdi ama Yumak sürekli gelip kemiği patileriyle bozuyordu. Hayri biraz düşündü. Kumda Yumak'ın kırmızı topu duruyordu. Hayri topu kayaların yanına götürdü ve biraz kuma gömdü. Yumak topun kokusunu aldı ve orada kumu eşeledi. Hayri hemen işine döndü ve kum kemiğini bitirdi. Üstüne beyaz kabuklar dizdi. "Yumak, gel, sana dünyanın en büyük kemiğini yaptım!" dedi Hayri abartarak. Yumak topuyla koşup geldi ve kuyruğunu salladı. Hayri bundan sonra sürpriz hazırlarken önce Yumak'a bir oyun verdi.
```

**Hakem bulguları (6):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hava ferah ve serindi"
   - Cümle 1: «Deniz kıyısında hava ferah ve serindi.»
   - Açıklama: 'Ferah' 3 yaşındaki çocuğun bilmediği bir kelime ve havaya uygun düşmüyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kumda Yumak'ın kırmızı topu duruyordu"
   - Cümle 5: «Kumda Yumak'ın kırmızı topu duruyordu.»
   - Açıklama: Top tam gerektiği anda önceden kurulmadan beliriyor ve çözümü sebepsizce getiriyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 10: «"Yumak, gel, sana dünyanın en büyük kemiğini yaptım!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut kelime ve 'dünyanın en büyük' abartısı küçük çocuğa uygun değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 10: «"Yumak, gel, sana dünyanın en büyük kemiğini yaptım!" dedi Hayri abartarak.»
   - Açıklama: Tohumdaki abartma özelliği yalnız süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
5. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yumak'a bir oyun verdi"
   - Cümle 12: «Hayri bundan sonra sürpriz hazırlarken önce Yumak'a bir oyun verdi.»
   - Açıklama: 'Oyun vermek' yanlış eşdizim; oyun verilmez.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "önce Yumak'a bir oyun verdi"
   - Cümle 12: «Hayri bundan sonra sürpriz hazırlarken önce Yumak'a bir oyun verdi.»
   - Açıklama: Oyun verilmez; 'oyuncak verdi' ya da 'oyun buldu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0043` birebir aynı, `@degisim: yelpaze -> kabuk` (tutuyorsan), ardından `@onarim: 264c2783ed84dccff4642a7e32ecb4fce461d27d`, sonra gövde.

### Hikâye 5: tohum hayri-0044 (deneme 1 -> 2)

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
Hayri kamp yerinde çok acıkmıştı ve iki sandviç yapıyordu. Birden gökyüzünde kalp şeklinde büyük bir bulut gördü. Hayri bulutu Kamil'e göstermek istedi ama Kamil basamakta uyuyordu. Hayri çabuk olmalıydı, çünkü bulut yavaş yavaş dağılıyordu. "Kamil, uyan, bak!" diye seslendi Hayri. Ama Kamil uyanmadı. Hayri sandviçin kağıdını buruşturdu. Sonra sandviçi Kamil'in burnuna yaklaştırdı. Kamil sandviçi kokladı ve gözlerini açtı. "Kamil, yukarı bak, bulut kalp gibi!" dedi Hayri. Kamil başını kaldırdı ve bulutu gördü. İkisi basamağa oturdu, sandviç yedi ve buluta baktı. Hayri çok sevindi, çünkü bulutu Kamil ile birlikte görmüştü.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri sandviçin kağıdını buruşturdu"
   - Cümle 7: «Hayri sandviçin kağıdını buruşturdu.»
   - Açıklama: Kağıdı buruşturmanın uyandırmada ne işe yaradığı belli değil; işlevsiz ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0044` birebir aynı, ardından `@onarim: 35746e7afd410f7f11b0aa2636e21cf1dcf96952`, sonra gövde.
