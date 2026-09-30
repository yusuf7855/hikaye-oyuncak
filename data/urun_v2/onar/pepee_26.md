# Editör görevi (onarım): Pepee, onarım partisi 26

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/pepee_onar26.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Pepee | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/pepee_onar26.txt --ad urun_v2`
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

## Kart: Pepee (kaynaklı, kapalı dünya)

- Ad: Pepee (okunuş: pepe; kesme eki okunuşa uyar)
- Kimlik: Pepee, mavi tulum ve mavi şapka giyen, dört yaşında meraklı bir oğlandır.
- Tür: oğlan
- Güvenli özellik kullanımı: Pepee yeni şeyleri bir büyüğün yanında dener; derin suya girmez, yüksek yere çıkmaz.
- Özellikler:
  - öğren: Yeni şeyler öğrenmeyi ve denemeyi sever. (örnek biçimler: öğrendi, öğrenmeyi)
  - kahvaltı: Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer. (örnek biçimler: kahvaltı, kahvaltıda)
  - dans: Oyun oynamayı ve dans etmeyi sever. (örnek biçimler: dans, dansı)
- Yerler:
  - orman: Ağaçlarla ve çiçeklerle dolu bir orman.
  - deniz: Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.
  - park: Salıncağı ve kaydırağı olan bir çocuk parkı.
  - ev: Pepee'nin ailesiyle yaşadığı ev.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Bebee: Pepee'nin küçük kız kardeşi; annesine hayrandır, Pepee ile oynamak için büyümek ister. Tür: kız; konuşur. Yüzey biçimleri: Bebee, kardeş, kardeşi
  - Şila: Pepee'nin kuzeni ve en yakın arkadaşı; çok güzel dans eder. Tür: kız; konuşur. Yüzey biçimleri: Şila, kuzen, kuzeni
  - Dedee: Pepee'nin dedesi; en az Pepee kadar hareketli bir oyun arkadaşı. Tür: dede; konuşur. Yüzey biçimleri: Dedee, dede, dedesi, dedeciğim
  - Nenee: Pepee'nin ninesi; komik ve eğlencelidir, yemek pişirmeyi sever. Tür: nine; konuşur. Yüzey biçimleri: Nenee, Ninee, nine, ninesi, nineciğim
  - Annee: Pepee'nin ve Bebee'nin annesi. Tür: anne; konuşur. Yüzey biçimleri: Annee, anne, annesi, anneciğim
- Dünya kuralları:
  - Bebee Pepee'nin küçük kız kardeşidir; Şila kuzenidir, kardeşi değildir.
  - Dizinin görünmeyen anlatıcısı hikayeye girmez; hikaye olayları kendisi anlatır.
- Yasak adlar: Şuşu, Şuşuu, Pisi, Zulu, Köpüş, Maymuş, Kaliş, Möcük, Zezee, Bibii, Kekee, Mimi, Mimii, Duduu, Tutuu, Ekee, Babaa, Zuku
- Yasak: Pepee'nin ve Bebee'nin konuşma zorluğu hikayeye konmaz; kimse konuşmasıyla alay etmez.
- Yasak: Dedee'nin uçan balonu hikayeye girmez (yükseklik).
- İzinli dünya kelimeleri: tulum, kahvaltı, pekmez, tahin, dans

## Onarılacak hikâyeler

### Hikâye 1: tohum pepee-0089 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Dedee
@tohum: pepee-0089
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Dedee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'poşet', fiil 'dikmek', sıfat 'eskimiş'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | Dedee
@plan: koşarken dedesinin ekmeğine kum sıçrattı | özür dileyip dedesine yeni ekmek verdi
@tohum: pepee-0089
Deniz kıyısında Pepee ile Dedee kahvaltı yapacaktı. Dedee şemsiyeyi kuma dikti ve eskimiş poşetten ekmek çıkardı. Pepee sevinçle koştu ve kumlar dedesinin ekmeğine sıçradı. Ekmek artık yenmezdi. Pepee durdu ve çok üzüldü. Hemen Dedee'den özür diledi. Sonra yeni bir ekmek ve tahin pekmez aldı. Ekmeğin üstüne en sevdiği tahin pekmezi dikkatle sürdü. Ekmeği gülümseyerek dedesine uzattı. Dedee Pepee'ye sıkıca sarıldı ve ekmeği ısırdı. Sonra Pepee ile Dedee şemsiyenin gölgesinde mutlu mutlu yemeğe başladı.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "eskimiş poşetten ekmek çıkardı"
   - Cümle 2: «Dedee şemsiyeyi kuma dikti ve eskimiş poşetten ekmek çıkardı.»
   - Açıklama: Eskimiş poşet ayrıntısı hiçbir işe yaramıyor.
   - Açıklama: Eskimiş poşet işlevsiz bir ayrıntı olarak kuruluyor ve kullanılmıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yeni bir ekmek ve tahin pekmez aldı"
   - Cümle 7: «Sonra yeni bir ekmek ve tahin pekmez aldı.»
   - Açıklama: Tamlama eksik ve sonraki cümleyle tutarsız; 'tahin pekmezi' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ekmek ve tahin pekmez aldı"
   - Cümle 7: «Sonra yeni bir ekmek ve tahin pekmez aldı.»
   - Açıklama: Tamlama eki eksik; sonraki cümledeki gibi 'tahin pekmezi' olmalı.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra yeni bir ekmek ve tahin pekmez aldı"
   - Cümle 7: «Sonra yeni bir ekmek ve tahin pekmez aldı.»
   - Açıklama: Yeni ekmek ve tahin pekmezin nereden geldiği söylenmeden sebepsizce beliriyor.
   - Açıklama: Yeni ekmek ve tahin pekmez nereden geldiği söylenmeden sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0089` birebir aynı, ardından `@onarim: 619480862f6e24681f12f37408e2a79a40580422`, sonra gövde.

### Hikâye 2: tohum pepee-0091 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Şila
@tohum: pepee-0091
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Şila
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'basamak', fiil 'çekilmek', sıfat 'iyi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | orman | Şila
@plan: sürpriz daha hazır değildi ama kuzeni geliyordu | kuzenini bekletip tabaklara en sevdiği yiyecekleri koydu
@tohum: pepee-0091
@degisim: basamak -> tabak
Pepee ormanda kuzeni Şila için bir sürpriz hazırlıyordu. Sepetinden tabakları çıkardı ve büyük bir kütüğün üstüne dizdi. Ama birden Şila'nın sesi geldi ve sürpriz daha hazır değildi. "Şila, orada bekle, daha gelme!" dedi Pepee. Şila güldü ve bir ağacın arkasına çekildi. Pepee hemen en sevdiği yiyecekleri sepetten aldı. Tabaklara yumurta, bal ve tahin pekmez koydu. "Şimdi gel, Şila!" dedi Pepee. Şila koşarak geldi ve tabakları gördü. Sevinçle zıpladı ve Pepee'ye sarıldı. "Ne iyi bir sürpriz! Teşekkürler, Pepee, bu en güzel kahvaltı!" dedi Şila.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "en sevdiği yiyecekleri sepetten"
   - Cümle 6: «Pepee hemen en sevdiği yiyecekleri sepetten aldı.»
   - Açıklama: Yiyeceklerin Pepee'nin mi Şila'nın mı en sevdiği olduğu belli değil.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bal ve tahin pekmez"
   - Cümle 7: «Tabaklara yumurta, bal ve tahin pekmez koydu.»
   - Açıklama: Tamlama eki eksik; 'tahin pekmezi' ya da 'tahin ve pekmez' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0091` birebir aynı, `@degisim: basamak -> tabak` (tutuyorsan), ardından `@onarim: e2a9b2b6437a8cbd7ba7d89c7835bacdced3a526`, sonra gövde.

### Hikâye 3: tohum pepee-0092 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0092
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bebee
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'terazi', fiil 'susmak', sıfat 'dürüst'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: koşarken kardeşinin terazisini devirdi ve kabuklar döküldü | özür dileyip kabukları topladı ve komik dans etti
@tohum: pepee-0092
Deniz kıyısında Bebee kabukları oyuncak bir teraziye koyuyordu. Pepee de onun yanında kumda koşuyordu. Birden Pepee teraziyi devirdi ve kabuklar yere döküldü. Bebee hemen sustu ve başını eğdi. Pepee dürüst davrandı ve kardeşinden hemen özür diledi. Sonra kabukları tek tek topladı ve teraziye geri koydu. Ama Bebee daha gülmüyordu. Pepee onun önünde komik bir dans yaptı. Kollarını salladı, zıpladı ve yavaşça döndü. Bebee önce baktı, sonra sesli sesli güldü. Pepee çok sevindi, çünkü kardeşi yine gülüyordu.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Pepee dürüst davrandı ve"
   - Cümle 5: «Pepee dürüst davrandı ve kardeşinden hemen özür diledi.»
   - Açıklama: Tohumdaki özellik dans; dürüstlük ikinci bir özellik olarak ekleniyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama Bebee daha gülmüyordu"
   - Cümle 7: «Ama Bebee daha gülmüyordu.»
   - Açıklama: 'daha' burada 'hâlâ/henüz' anlamında belirsiz kullanılmış ve Bebee daha önce gülmediği için 'gülmüyordu' yerinde değil.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Pepee onun önünde komik bir dans yaptı"
   - Cümle 8: «Pepee onun önünde komik bir dans yaptı.»
   - Açıklama: Çözüm özür, kabukları toplama ve dans olmak üzere üç adım sürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0092` birebir aynı, ardından `@onarim: e98c3ade916189ca84c9b2ee7fb66da636dfde97`, sonra gövde.

### Hikâye 4: tohum pepee-0093 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0093
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: bir şey yapmak
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'süpürge', fiil 'öğretmek', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: kumdaki çukurlar yüzünden bahçe düz olmadı | eski süpürgeyle kumu düzeltmeyi ilk kez denedi
@tohum: pepee-0093
@degisim: öğretmek -> düzeltmek
Bir sabah Pepee deniz kıyısında kumdan bir ev yapıyordu. Evin önüne düz bir bahçe yapmak istedi. Ama kumda bir sürü küçük çukur vardı ve eliyle düzeltemedi. Pepee kovasına baktı. İçinde eski bir oyuncak süpürge vardı. Pepee süpürgeyi kumda hiç kullanmamıştı ama denemek istedi. Süpürgeyi bahçenin üstünde ileri geri gezdirdi. Çukurlar yavaş yavaş doldu ve bahçe dümdüz oldu. Böylece Pepee yeni bir şey öğrendi. Sonra bahçeye kabuklardan küçük bir yol yaptı. Pepee kumdan evinin önünde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük çukur vardı ve eliyle düzeltemedi"
   - Cümle 3: «Ama kumda bir sürü küçük çukur vardı ve eliyle düzeltemedi.»
   - Açıklama: Kumdaki küçük çukurları elle düzeltememek akla yatkın bir sebep değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Pepee süpürgeyi kumda hiç kullanmamıştı ama denemek istedi"
   - Cümle 6: «Pepee süpürgeyi kumda hiç kullanmamıştı ama denemek istedi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada deniz kıyısında yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0093` birebir aynı, `@degisim: öğretmek -> düzeltmek` (tutuyorsan), ardından `@onarim: a2d6e719257442924342d7de28f4d440dd60690d`, sonra gövde.

### Hikâye 5: tohum pepee-0094 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | ev | Bebee
@tohum: pepee-0094
- yer: ev (Pepee'nin ailesiyle yaşadığı ev.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Bebee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'delik', fiil 'kazanmak', sıfat 'temkinli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | ev | Bebee
@plan: kazanmak için kardeşinin topunu elinden çekip aldı | özür diledi ve kardeşinden temkinli atmayı öğrendi
@tohum: pepee-0094
Pepee evde Bebee ile delikli bir kutuya top atıyordu. Bebee temkinli atıyordu ve topları kutuya sokuyordu, ama Pepee kaçırıyordu. Pepee kazanmak istedi ve kardeşinin elindeki topu çekip aldı. Bebee çok üzüldü ve ağlamaya başladı. Pepee durdu ve topu ona geri verdi. "Özür dilerim, Bebee. Bana nasıl attığını öğretir misin?" dedi Pepee. Bebee gözlerini sildi ve güldü. "Önce deliğe iyi bak, sonra yavaşça at," dedi Bebee. Pepee bunu hemen öğrendi ve denedi. Top tam içeri girdi. Bebee sevinçle zıpladı. "Teşekkürler, Bebee, şimdi ikimiz de kazanıyoruz!" dedi Pepee.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kardeşinden temkinli atmayı öğrendi"
   - Cümle 0 (plan satırı): «kazanmak için kardeşinin topunu elinden çekip aldı | özür diledi ve kardeşinden temkinli atmayı öğrendi»
   - Açıklama: Plandaki 'temkinli' kelimesi 3 yaş için soyut.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bebee temkinli atıyordu"
   - Cümle 2: «Bebee temkinli atıyordu ve topları kutuya sokuyordu, ama Pepee kaçırıyordu.»
   - Açıklama: 'Temkinli' 3 yaşındaki çocuğun bilmediği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0094` birebir aynı, ardından `@onarim: 40f49113e12b2efc161d4eaa44449b733fd87e27`, sonra gövde.

### Hikâye 6: tohum pepee-0095 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Annee
@tohum: pepee-0095
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Annee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'yulaf', fiil 'izlemek', sıfat 'limonlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | park | Annee
@plan: kurabiye saklıydı ve nereye bakacağını bilmiyordu | sıcak soğuk oyununu öğrendi ve kurabiyeyi buldu
@tohum: pepee-0095
Pepee parkta annesiyle yeni bir oyun oynuyordu. Annee limonlu bir yulaf kurabiyesini kaydırağın altına sakladı. Ama Pepee nereye bakacağını bilmiyordu ve onu bulamadı. "Anneciğim, kurabiye nerede?" diye sordu Pepee. "Yakına gelince 'sıcak', uzağa gidince 'soğuk' derim," dedi Annee. Sonra Annee oturdu ve onu izledi. Pepee kuralı hemen öğrendi ve salıncağa doğru yürüdü. "Soğuk!" dedi Annee. Pepee geri döndü ve kaydırağa koştu. "Sıcak, çok sıcak!" dedi Annee. Pepee kaydırağın altına eğildi ve kurabiyeyi buldu. Onu ikiye böldü ve yarısını annesine verdi. "Anneciğim, bu oyun çok güzel, bir daha oynayalım!" dedi Pepee.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Pepee kuralı hemen öğrendi"
   - Cümle 7: «Pepee kuralı hemen öğrendi ve salıncağa doğru yürüdü.»
   - Açıklama: 'Kural' 3 yaşındaki çocuk için soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0095` birebir aynı, ardından `@onarim: cfb4ec1ef3cabde98ab82d6da227e93995103112`, sonra gövde.

### Hikâye 7: tohum pepee-0096 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | -
@tohum: pepee-0096
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'flüt', fiil 'düzenlemek', sıfat 'sisli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | -
@plan: çok güçlü üfledi ve flütten kötü ses çıktı | yavaşça üflemeyi denedi ve güzel ses çıkardı
@tohum: pepee-0096
@degisim: düzenlemek -> üflemek
Pepee sisli bir sabah deniz kıyısına yeni flütünü getirdi. Kuma oturdu ve flütü ilk kez çalmayı denedi. Ama çok güçlü üfledi ve flütten kötü bir ses çıktı. Pepee kulaklarını kapattı ve güldü. Sonra biraz düşündü. Bu kez az bir nefesle, yavaşça üfledi. Flütten ince ve güzel bir ses geldi. Pepee parmaklarını deliklere tek tek koydu. Her delikte flüt başka türlü öttü. Böylece küçük bir şarkı çalmayı öğrendi. Pepee bundan sonra flüte hep yavaşça üfledi.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sabah deniz kıyısına yeni flütünü getirdi"
   - Cümle 1: «Pepee sisli bir sabah deniz kıyısına yeni flütünü getirdi.»
   - Açıklama: İyelik eki yanlış; 'flütünü' değil 'flütü' olmalı.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "flütü ilk kez çalmayı denedi"
   - Cümle 2: «Kuma oturdu ve flütü ilk kez çalmayı denedi.»
   - Açıklama: Güvenli kullanım satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, ama deniz kıyısında yalnız deniyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Kuma oturdu ve flütü ilk kez çalmayı denedi"
   - Cümle 2: «Kuma oturdu ve flütü ilk kez çalmayı denedi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Pepee yeni şeyleri bir büyüğün yanında dener, burada deniz kıyısında yalnız deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0096` birebir aynı, `@degisim: düzenlemek -> üflemek` (tutuyorsan), ardından `@onarim: 14f33e63b43c344c3a50034b0ec33b01eb5b83c6`, sonra gövde.

### Hikâye 8: tohum pepee-0097 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Pepee | deniz | Şila
@tohum: pepee-0097
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Şila
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'havlu', fiil 'gezinmek', sıfat 'kısa'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Şila
@plan: kıyıda nereden geldiği belli olmayan tatlı bir koku vardı | kokuyu tanıdı, izledi ve kutuyu buldu
@tohum: pepee-0097
Bir sabah Pepee ile Şila deniz kıyısında gezindi. Birden Pepee tatlı bir koku aldı. Bunun nereden geldiğini çok merak etti. "Bil bakalım, bu ne?" diye sordu Şila ve güldü. Pepee durdu ve havayı kokladı. "Bu bal ve tahin pekmez, en sevdiğim yiyecekler!" dedi Pepee. Kokuyu izleyerek kısa bir yol yürüdü. Kumda Şila'nın havlusu vardı ve üstünde küçük bir kutu duruyordu. Pepee kutuyu açtı ve içinde bal, tahin pekmez ve ekmek gördü. "Buldun! Bunları kahvaltı için getirdim," dedi Şila. Pepee çok sevindi, çünkü ekmekleri kendi burnuyla bulmuştu.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "nereden geldiği belli olmayan tatlı bir koku"
   - Cümle 0 (plan satırı): «kıyıda nereden geldiği belli olmayan tatlı bir koku vardı | kokuyu tanıdı, izledi ve kutuyu buldu»
   - Açıklama: Tatlı bir koku almak çocuğun önemseyeceği gerçek bir sorun değil ve kapalı kutudaki bal ile tahin pekmezin uzaktan kokması akla yatkın değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bunun nereden geldiğini çok merak etti"
   - Cümle 3: «Bunun nereden geldiğini çok merak etti.»
   - Açıklama: Tatlı bir kokunun kaynağını merak etmek gerçek bir sorun değil, önemsiz bir merak olayı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Bu bal ve tahin pekmez"
   - Cümle 6: «"Bu bal ve tahin pekmez, en sevdiğim yiyecekler!" dedi Pepee.»
   - Açıklama: Tamlama eki eksik; 'tahin pekmezi' olmalı.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çünkü ekmekleri kendi burnuyla bulmuştu"
   - Cümle 12: «Pepee çok sevindi, çünkü ekmekleri kendi burnuyla bulmuştu.»
   - Açıklama: Pepee bal ve tahin pekmez kokusunu izledi ama son cümle ekmekleri kokuyla bulduğunu söylüyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ekmekleri kendi burnuyla bulmuştu"
   - Cümle 12: «Pepee çok sevindi, çünkü ekmekleri kendi burnuyla bulmuştu.»
   - Açıklama: Pepee bal ve tahin pekmez kokusunu izledi, ekmeği kokuyla bulmadı; son cümle öncekilerle çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0097` birebir aynı, ardından `@onarim: a0c84224779afb6d19c63afeceeab5cf7d84e9c4`, sonra gövde.

### Hikâye 9: tohum pepee-0099 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Dedee
@tohum: pepee-0099
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: kaybolan eşya
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'fırça', fiil 'çekmek', sıfat 'boyalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Dedee
@plan: rüzgar esince fırça çiçeklerin arasında kayboldu | boya lekelerini izleyip fırçayı buldu
@tohum: pepee-0099
Ormanda hafif bir rüzgar esiyordu. Pepee ile Dedee bir kütüğün üstünde taşları kırmızıya boyuyordu. Bu rüzgarla Pepee'nin fırçası kütükten yuvarlandı ve çiçeklerin arasında kayboldu. "Dedeciğim, fırçam nerede?" diye sordu Pepee. "Boyalı fırça nereye düşerse orada boya izi olur," dedi Dedee. Pepee bunu hemen öğrendi ve yere dikkatle baktı. Bir yaprakta kırmızı bir leke gördü. Biraz ileride bir leke daha vardı. Pepee lekeleri izledi ve bir çiçeğin dibine geldi. Fırçayı yaprakların altından çekip aldı. "Buldum!" dedi Pepee. Pepee ile Dedee taşları boyamaya mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Pepee bunu hemen öğrendi"
   - Cümle 6: «Pepee bunu hemen öğrendi ve yere dikkatle baktı.»
   - Açıklama: Burada 'öğrendi' yerine 'anladı' olmalı; kelime yanlış anlamda.
   - Açıklama: Burada 'öğrendi' yanlış anlamda; 'anladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0099` birebir aynı, ardından `@onarim: 50173569f643cf1bf74058c3eaa8182172a1c234`, sonra gövde.

### Hikâye 10: tohum pepee-0100 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | orman | Şila
@tohum: pepee-0100
- yer: orman (Ağaçlarla ve çiçeklerle dolu bir orman.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Şila
- özellik: dans (Oyun oynamayı ve dans etmeyi sever.)
- kelimeler: isim 'mikroskop', fiil 'hazırlanmak', sıfat 'ferah'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Pepee | orman | Şila
@plan: gösteri için ormanda hiç müzik yoktu | ayaklarını yere vurarak dans edip ses çıkardı
@tohum: pepee-0100
@degisim: mikroskop -> çiçek
Rüzgar ağaçların arasında hafifçe esiyordu. Pepee ile Şila ferah bir açıklıkta gösteri oyununa hazırlanıyordu. Ama ormanda hiç müzik yoktu. "Pepee, müzik olmadan nasıl dans edeceğiz?" diye sordu Şila. Pepee biraz düşündü. Sonra ayaklarını yere vurarak dans etmeye başladı. Tap, tap, tap diye güzel bir ses çıktı. Pepee dönerken ellerini de çırptı. "Şila, işte müzik!" dedi Pepee. Şila bu sesle çiçeklerin arasında güzelce dans etti. Pepee ses çıkarmayı hiç bırakmadı. Gösterinin sonunda ikisi birbirini alkışladı. Sonra el ele tutuşup oyunlarına mutlu mutlu devam ettiler.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ferah bir açıklıkta"
   - Cümle 2: «Pepee ile Şila ferah bir açıklıkta gösteri oyununa hazırlanıyordu.»
   - Açıklama: 'Ferah' ve 'açıklık' 3 yaşındaki bir çocuğun bildiği kelimeler değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ferah bir açıklıkta gösteri"
   - Cümle 2: «Pepee ile Şila ferah bir açıklıkta gösteri oyununa hazırlanıyordu.»
   - Açıklama: 'Ferah' ve 'açıklık' 3 yaşındaki çocuğun bilmeyeceği kelimeler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0100` birebir aynı, `@degisim: mikroskop -> çiçek` (tutuyorsan), ardından `@onarim: 8faff1e6d02323543615a19caa9ab29584d5e84a`, sonra gövde.

### Hikâye 11: tohum pepee-0103 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | deniz | Bebee
@tohum: pepee-0103
- yer: deniz (Deniz kıyısı; kum ve küçük dalgalar. Herkes kumda ve su kenarında kalır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Bebee
- özellik: kahvaltı (Kahvaltıyı çok sever; en çok yumurta, bal ve tahin pekmez yer.)
- kelimeler: isim 'halka', fiil 'sormak', sıfat 'şeffaf'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Pepee | deniz | Bebee
@plan: yumurtanın kabuğu çok sertti ve kardeşi onu çıkaramadı | yumurtayı kapağa vurdu ve avucunda yuvarladı
@tohum: pepee-0103
@degisim: halka -> kabuk
Deniz kıyısında Pepee ile Bebee kumun üstünde kahvaltı yapıyordu. Bebee şeffaf kutusundan bir yumurta çıkardı. Ama yumurtanın kabuğu çok sertti ve Bebee onu çıkaramadı. "Pepee, bu kabuk nasıl çıkar?" diye sordu Bebee. Pepee yumurtayı aldı ve kahvaltıda hep yaptığı gibi kutunun kapağına hafifçe vurdu. Kabuk küçük küçük çatladı. Sonra Pepee yumurtayı avucunda yavaşça yuvarladı. "Şimdi sen dene, Bebee," dedi Pepee. Bebee kabuğun parçalarını tek tek aldı. Kabuğun altından bembeyaz yumurta göründü. Bebee yumurtasını mutlu mutlu yedi. Pepee çok sevindi, çünkü kardeşine yardım etmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bebee şeffaf kutusundan"
   - Cümle 2: «Bebee şeffaf kutusundan bir yumurta çıkardı.»
   - Açıklama: 'Şeffaf' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Şeffaf' 3 yaşındaki bir çocuğun bileceği bir kelime değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0103` birebir aynı, `@degisim: halka -> kabuk` (tutuyorsan), ardından `@onarim: d36907ebdb3449f885e24e99ccd231f596da57a5`, sonra gövde.

### Hikâye 12: tohum pepee-0107 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Pepee | park | Dedee
@tohum: pepee-0107
- yer: park (Salıncağı ve kaydırağı olan bir çocuk parkı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Dedee
- özellik: öğren (Yeni şeyler öğrenmeyi ve denemeyi sever.)
- kelimeler: isim 'boncuk', fiil 'çoğalmak', sıfat 'boş'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Pepee | park | Dedee
@plan: boncuklar ipin boş ucundan kayıp düştü | ipin ucuna düğüm atmayı denedi ve öğrendi
@tohum: pepee-0107
Pepee parkta, cebindeki boncuklarla dedesine sürpriz bir bileklik yapmak istedi. Dedee bankta oturdu ve gözlerini kapattı. Pepee boncukları ipe dizdi ama hepsi ipin boş ucundan kayıp düştü. Pepee boncukları çimenlerden tek tek topladı. Sonra ipin ucuna ilk kez bir düğüm atmayı denedi. İlk düğüm çok küçüktü ve bir boncuk yine kaydı. Pepee bir daha denedi ve büyük bir düğüm atmayı öğrendi. Boncuklar artık düşmedi ve ipte yavaş yavaş çoğaldı. "Dedeciğim, şimdi bakabilirsin!" dedi Pepee. Dedee gözlerini açtı ve bilekliği koluna taktı. "Teşekkür ederim, Pepee, bu çok güzel bir hediye!" dedi Dedee.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ipte yavaş yavaş çoğaldı"
   - Cümle 8: «Boncuklar artık düşmedi ve ipte yavaş yavaş çoğaldı.»
   - Açıklama: Boncuklar çoğalmaz; ipteki boncuk sayısı artıyordu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: pepee-0107` birebir aynı, ardından `@onarim: 161f248d2ca586b0d7932e8149d55896fc1e2819`, sonra gövde.
