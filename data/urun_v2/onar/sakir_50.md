# Editör görevi (onarım): Şakir, onarım partisi 50

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar50.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar50.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0155 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0155
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kemer', fiil 'almak', sıfat 'ekşi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: sürpriz daha bitmemişti ama fil erken geri geliyordu | şapkasıyla erikleri örttü ve sonra açtı
@tohum: sakir-0155
@degisim: kemer -> erik
Şakir, Fil Necati için kumsalda bir sürpriz hazırlıyordu. Çantasından Necati'nin en sevdiği ekşi erikleri aldı ve havluya dizdi. Ama Necati su kenarından erken geri geliyordu. Şakir erikleri saklamak istedi. Şakir geniş şapkasını hemen çıkardı. Şapkayla erikleri örttü. Necati geldi ve yerdeki şapkaya baktı. "Şakir, şapkan neden yerde?" diye sordu Necati. "Çünkü altında sana bir sürpriz var," dedi Şakir. Şakir şapkayı yavaşça kaldırdı. "Erikler mi, onları çok severim!" dedi Necati sevinçle. İkisi erikleri paylaştı ve mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama Necati su kenarından erken geri geliyordu"
   - Cümle 3: «Ama Necati su kenarından erken geri geliyordu.»
   - Açıklama: Necati'nin neden erken döndüğü, yani sorunun sebebi hiç söylenmiyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şapkayla erikleri örttü"
   - Cümle 6: «Şapkayla erikleri örttü.»
   - Açıklama: Plandaki sorun sürprizin bitmemesiyken sürpriz hiç tamamlanmıyor; erikler örtülüp hemen açılıyor, çözüm sebebe yönelmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0155` birebir aynı, `@degisim: kemer -> erik` (tutuyorsan), ardından `@onarim: 080fe8b7c73035ee7580df801070225b6adac5c7`, sonra gövde.

### Hikâye 2: tohum sakir-0156 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0156
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kızartma', fiil 'ödemek', sıfat 'umutlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: kabuklar küçük elinden hep düşüyordu | kabukları şapkasına doldurup taşıdı
@tohum: sakir-0156
@degisim: ödemek -> taşımak
Kumsalda Şakir annesi için kabuklardan bir kalp yapmak istedi. Kadriye biraz ileride örtüye patates kızartması koyuyordu. Ama kabuklar çoktu ve Şakir'in küçük elinden hep düşüyordu. Şakir şapkasını çıkardı. Kabukları tek tek şapkanın içine koydu. Şapka doldu ve hiçbir kabuk düşmedi. Şakir şapkayı örtünün yanına taşıdı. Kabuklarla kumun üstüne büyük bir kalp yaptı. "Anne, sana bir sürprizim var!" dedi Şakir ve umutlu bir yüzle bekledi. Kadriye döndü ve kumdaki kalbi görünce gülümsedi. "Teşekkürler, Şakir, gel şimdi birlikte kızartma yiyelim!" dedi Kadriye.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kadriye biraz ileride örtüye"
   - Cümle 2: «Kadriye biraz ileride örtüye patates kızartması koyuyordu.»
   - Açıklama: Kadriye'nin Şakir'in annesi olduğu söylenmeden adıyla giriyor, 'annesi' ile 'Kadriye'nin aynı kişi olduğu belli değil.
   - Açıklama: Kadriye'nin Şakir'in annesi olduğu söylenmeden ad olarak geçiyor; 'annesi' ile aynı kişi olduğu belli değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "umutlu bir yüzle bekledi"
   - Cümle 9: «"Anne, sana bir sürprizim var!" dedi Şakir ve umutlu bir yüzle bekledi.»
   - Açıklama: 'Umutlu bir yüz' soyut bir anlatım, 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Umutlu bir yüzle' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0156` birebir aynı, `@degisim: ödemek -> taşımak` (tutuyorsan), ardından `@onarim: c639d7bfb385963733f1d86729dbb77bc711553f`, sonra gövde.

### Hikâye 3: tohum sakir-0184 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0184
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'top', fiil 'tamamlamak', sıfat 'çamurlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: küçük bir kedi kaygan çamurdan çıkamıyordu | şapkasını çamurun kenarına koyup kediyi dışarı aldı
@tohum: sakir-0184
@degisim: tamamlamak -> bitirmek
Şakir kamp yerinde annesi Kadriye ile top oynuyordu. Top çamurlu bir su birikintisinin yanına yuvarlandı. Orada küçük bir kedi kaygan çamurda kayıyordu ve dışarı çıkamıyordu. "Anne, kedi çamurdan çıkamıyor!" dedi Şakir. Kadriye çamura baktı. "Çamur çok kaygan, içine basma, Şakir," dedi Kadriye. Şakir şapkasını çıkardı ve çamurun kenarına koydu. Kedi şapkaya tutundu ve üstüne çıktı. Şakir şapkayı kaldırdı ve kediyi kuru otların üstüne bıraktı. Kedi ağaçlara doğru koşup gitti. Sonra Şakir ve annesi top oyununu mutlu mutlu bitirdi.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Orada küçük bir kedi kaygan çamurda kayıyordu"
   - Cümle 3: «Orada küçük bir kedi kaygan çamurda kayıyordu ve dışarı çıkamıyordu.»
   - Açıklama: Başlıktaki Yan alanında yalnız Kadriye var; kartın yanlar bölümünde olmayan bir kedi olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0184` birebir aynı, `@degisim: tamamlamak -> bitirmek` (tutuyorsan), ardından `@onarim: c79857c3be6056c73f333413f13a148d0c12762a`, sonra gövde.

### Hikâye 4: tohum sakir-0194 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0194
- yer: park (Şehirdeki park.)
- tema: kaybolan eşya
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kitap', fiil 'gerinmek', sıfat 'sisli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: fil gerinince kitap dallara kalktı ve sisin içinde kayboldu | kitabı dalda bulup şapkasını atarak düşürdü
@tohum: sakir-0194
Şakir sisli bir sabah Necati ile parktaydı. Necati bir ağacın altında durmuş, hortumuyla bir kitap tutuyordu. Birden Necati gerindi, hortumu dallara kalktı ve kitap sisin içinde kayboldu. "Kitabım nereye gitti?" diye sordu Necati. Şakir etrafa dikkatle baktı. Yukarıda bir dalın ucunda beyaz bir şey gördü. Bu, Necati'nin kitabıydı. Necati hortumunu uzattı ama dalın ucuna yetişemedi. Şakir şapkasını kitaba doğru attı. Kitap ve şapka daldan kaydı ve aşağı düştü. Necati kitabı hortumuyla havada yakaladı. "Teşekkürler, Şakir, sen olmasan kitabı bulamazdım!" dedi Necati. Şakir ile Necati banka oturdu ve kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kitap dallara kalktı"
   - Cümle 0 (plan satırı): «fil gerinince kitap dallara kalktı ve sisin içinde kayboldu | kitabı dalda bulup şapkasını atarak düşürdü»
   - Açıklama: Kitap kendiliğinden kalkmaz; 'kalkmak' fiili bu özneye uymuyor, 'dallara fırladı/uçtu' olmalı.
   - Açıklama: Kitap kendiliğinden kalkmaz; fiil öznesine uymuyor, kalkan fil'in hortumudur.
   - Açıklama: Kitap 'kalkmaz'; plan satırında fiil öznesine uymuyor, 'dallara fırladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0194` birebir aynı, ardından `@onarim: c67790e7c08198768b602422b31be3bd471f9dc2`, sonra gövde.

### Hikâye 5: tohum sakir-0207 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0207
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kova', fiil 'alışmak', sıfat 'karışık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: aç sincaplar korkup fındık kovasına yaklaşamadı | şapkaya fındık koyup ağacın dibine bıraktı
@tohum: sakir-0207
Şakir, Necati ile ormandaki kamp yerinde oturuyordu. Necati'nin önünde fındık ve ceviz karışık dolu bir kova vardı. Ağaçtan aç sincaplar indi, ama Necati'den korkup kovaya yaklaşamadılar. Sincaplar fındıklara uzaktan bakıyordu. "Onlara nasıl yardım ederiz?" diye sordu Necati. Şakir şapkasını çıkardı ve kovadan şapkanın içine biraz fındık koydu. Şapkayı ağacın dibine bıraktı ve Necati ile biraz geri çekildi. Sincaplar önce durdu ve kulaklarını oynattı. Sonra yavaş yavaş Şakir ile Necati'ye alıştılar ve şapkaya geldiler. Fındıkları tek tek kemirdiler. "Bak, Necati, sincapların karnı doydu!" dedi Şakir. Şakir ile Necati de kalan fındıkları mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "fındık ve ceviz karışık dolu bir kova"
   - Cümle 2: «Necati'nin önünde fındık ve ceviz karışık dolu bir kova vardı.»
   - Açıklama: Tamlama bozuk; 'fındık ve cevizle dolu bir kova' olmalı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "fındık ve ceviz karışık dolu bir kova"
   - Cümle 2: «Necati'nin önünde fındık ve ceviz karışık dolu bir kova vardı.»
   - Açıklama: Ceviz kuruluyor ama hikayede hiç kullanılmıyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Ağaçtan aç sincaplar indi"
   - Cümle 3: «Ağaçtan aç sincaplar indi, ama Necati'den korkup kovaya yaklaşamadılar.»
   - Açıklama: Arka planda kalması gereken çoğul sincaplar şapkaya gelip fındık yiyerek olaya katılıyor.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Sonra yavaş yavaş Şakir ile Necati'ye alıştılar ve şapkaya geldiler"
   - Cümle 9: «Sonra yavaş yavaş Şakir ile Necati'ye alıştılar ve şapkaya geldiler.»
   - Açıklama: Arka plandaki çoğul canlılar (sincaplar) olaya katılıyor; en çok 1 isimsiz yan kuralına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0207` birebir aynı, ardından `@onarim: ad547a242a0ff1fd8f721998cbba9ac43ebc7bba`, sonra gövde.

### Hikâye 6: tohum sakir-0212 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0212
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'halat', fiil 'doğmak', sıfat 'sağlıklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: kız kardeşi de sallanmak istedi ama tek halat vardı | şapkasını kardeşine verdi ve sırayla sallandılar
@tohum: sakir-0212
@degisim: sağlıklı -> uzun
Şakir ormanda alçak bir dala bağlı uzun bir halatla sallanıyordu. Güneş yeni doğmuştu. Kardeşi Canan da sallanmak istedi, ama orada tek bir halat vardı. "Ben de sallanabilir miyim, Şakir?" diye sordu Canan. Şakir durdu ve biraz düşündü. Sonra şapkasını çıkardı ve Canan'ın başına taktı. "Şapkayı kim takarsa o sallanır," dedi Şakir. Canan on kez sallandı, sonra şapkayı Şakir'e geri verdi. Bu kez Şakir şapkayı taktı ve sallandı. Şakir ile Canan sırayla sallanıp mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "alçak bir dala bağlı uzun bir halatla sallanıyordu"
   - Cümle 1: «Şakir ormanda alçak bir dala bağlı uzun bir halatla sallanıyordu.»
   - Açıklama: Çocukların ormanda ağaç dalına bağlı halatla yetişkinsiz sallanması taklit edilince tehlikeli olabilir ve güvenli kullanım satırının güvenli oyun sınırını zorlar.
   - Açıklama: Yetişkinsiz çocukların ağaç dalına bağlı halatla sallanması taklit edilince tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0212` birebir aynı, `@degisim: sağlıklı -> uzun` (tutuyorsan), ardından `@onarim: ead05e61d45bf905b20575933129ffdf2864e75b`, sonra gövde.

### Hikâye 7: tohum sakir-0241 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0241
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'tren', fiil 'eğmek', sıfat 'dürüst'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: tek tren vardı ve ikisi de onu itmek istedi | treni yalnız şapkayı takan itti
@tohum: sakir-0241
@degisim: dürüst -> kısa
Bir sabah Şakir ile Canan kumsalda oyuncak trenle oynuyordu. Kumda uzun bir tren yolu yapmışlardı. Ama tek bir tren vardı ve ikisi de onu itmek istedi. Şakir sıra için bir oyun buldu. Treni yalnız şapkayı takan itecekti. Şakir şapkasını çıkardı ve Canan'ın başına taktı. Canan treni yolda kısa bir süre itti. Sonra başını eğdi, şapkayı çıkardı ve Şakir'e verdi. Şakir de şapkayı taktı ve treni yolun sonuna kadar götürdü. Böylece ikisi de sırayla oynadı ve kimse üzülmedi. Şakir ile Canan oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Canan treni yolda kısa bir süre itti"
   - Cümle 7: «Canan treni yolda kısa bir süre itti.»
   - Açıklama: Canan treni yalnız kısa bir süre itip Şakir yolun sonuna kadar götürürken hikaye ikisinin de eşit sırayla oynadığını ve kimsenin üzülmediğini söylüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0241` birebir aynı, `@degisim: dürüst -> kısa` (tutuyorsan), ardından `@onarim: 263a4aa049ff287b300c69138409e9971da08064`, sonra gövde.

### Hikâye 8: tohum sakir-0243 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0243
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'cips', fiil 'çözülmek', sıfat 'rüzgarlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: cipsleri paylaşmak istedi ama rüzgar onları uçurdu | şapkasını rüzgara karşı tuttu ve cipsleri korudu
@tohum: sakir-0243
Bir sabah Şakir ile Necati ormandaki rüzgarlı kamp yerinde oturuyordu. Şakir ağzı düğümlü cips paketini Necati ile paylaşmak istedi. Düğüm kolayca çözüldü, ama rüzgar birkaç cipsi paketten uçurdu. Şakir hemen şapkasını çıkardı ve rüzgarın geldiği yana tuttu. Şapkanın arkasında kalan cipsler artık uçmadı. Şakir paketi Necati'ye uzattı. Necati uzun hortumuyla cipsleri tek tek aldı ve yedi. Sonra Şakir de cips yedi. Şakir çok sevindi, çünkü cipsleri Necati ile birlikte yemişlerdi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar birkaç cipsi paketten uçurdu"
   - Cümle 3: «Düğüm kolayca çözüldü, ama rüzgar birkaç cipsi paketten uçurdu.»
   - Açıklama: Rüzgarın birkaç cipsi uçurması önemsiz bir olay; sorun çocuğun önemseyeceği bir şey değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Düğüm kolayca çözüldü"
   - Cümle 3: «Düğüm kolayca çözüldü, ama rüzgar birkaç cipsi paketten uçurdu.»
   - Açıklama: Paketin düğümlü ağzı bir engel gibi kuruluyor ama hemen çözülüyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Düğümlü paket bir engel gibi kuruluyor ama hiçbir işe yaramadan hemen çözülüyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "cipsleri Necati ile birlikte yemişlerdi"
   - Cümle 9: «Şakir çok sevindi, çünkü cipsleri Necati ile birlikte yemişlerdi.»
   - Açıklama: Özne Şakir tekil ve 'ile birlikte' kullanılmış, fiil çoğul çekimlenmiş; 'yemişti' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0243` birebir aynı, ardından `@onarim: 2b3fa6f3eccdaf5576c648b37d12bf75754f4b45`, sonra gövde.

### Hikâye 9: tohum sakir-0246 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0246
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'vazo', fiil 'guruldamak', sıfat 'meyveli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: kuru kumdan yaptığı kule hep yıkıldı | şapkasını ıslak kumla doldurup çevirdi
@tohum: sakir-0246
@degisim: vazo -> kum
Bir sabah Şakir kumsalda ilk kez kumdan bir kule yapmayı denedi. Ama kule hep yıkıldı, çünkü kum çok kuruydu. Kuru kum elinden hep dökülüyordu. Şakir kumu biraz kazdı ve çukurun dibinde su guruldadı. Oradaki kum ıslaktı ve hiç dökülmüyordu. Şakir meyveli şapkasını çıkardı ve ıslak kumla doldurdu. Şapkayı çevirip kuma bastırdı ve yavaşça kaldırdı. Kumda yuvarlak ve yüksek bir kule duruyordu. Kule kocaman bir keke benziyordu. Şakir buna çok güldü ve yanına iki kule daha yaptı. Sonra Şakir mutlu mutlu yeni kuleler yapmaya devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dibinde su guruldadı"
   - Cümle 4: «Şakir kumu biraz kazdı ve çukurun dibinde su guruldadı.»
   - Açıklama: Su guruldamaz; kelime öznesine uygun değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çukurun dibinde su guruldadı"
   - Cümle 4: «Şakir kumu biraz kazdı ve çukurun dibinde su guruldadı.»
   - Açıklama: Su guruldamaz; fiil öznesine uymuyor, 'su göründü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0246` birebir aynı, `@degisim: vazo -> kum` (tutuyorsan), ardından `@onarim: 725ce622027d6e0bdea60532b7cea58f0165c06e`, sonra gövde.

### Hikâye 10: tohum sakir-0251 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0251
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bant', fiil 'kopmak', sıfat 'şaşkın'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kitabı hızla çekince bir sayfa koptu | özür diledi ve sayfayı bantla yapıştırdı
@tohum: sakir-0251
Kumsalda Canan bir havlunun üstünde kitap okuyordu. Şakir resimlere bakmak için kardeşinin kitabını hızla kendine çekti. Bir sayfa koptu ve rüzgar onu uçurdu. Şakir koştu ve sayfayı şapkasıyla yakaladı. Canan şaşkın şaşkın önce kitaba, sonra Şakir'e baktı. "Özür dilerim, Canan, kitabını hızla çektim," dedi Şakir. "Çantada bant var," dedi Canan. Şakir sayfayı bantla kitaba dikkatle yapıştırdı. Canan gülümsedi ve Şakir'e resimleri gösterdi. Şakir çok sevindi, çünkü kardeşinin kitabı yeniden tamamdı.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "rüzgar onu uçurdu"
   - Cümle 3: «Bir sayfa koptu ve rüzgar onu uçurdu.»
   - Açıklama: Sayfanın kopmasına ek olarak rüzgarın sayfayı uçurması ikinci bir sorun açıyor.
   - Açıklama: Kopan sayfanın rüzgarla uçması ana sorunun yanına ikinci bir sorun ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0251` birebir aynı, ardından `@onarim: 2071b4e156dd3f70728a8c53a4535af9d2ef78b0`, sonra gövde.

### Hikâye 11: tohum sakir-0259 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0259
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: bir şey yapmak
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yosun', fiil 'tasarlamak', sıfat 'serin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: kuru kum aslanın başında hep dağıldı | yosunları şapkayla getirip başın çevresine dizdi
@tohum: sakir-0259
@degisim: tasarlamak -> yapmak
Serin bir rüzgar esiyordu. Şakir kumsalda kumdan bir aslan yapmak istedi. Aslanın gövdesini yaptı, ama başını yaparken kuru kum hep dağıldı. Biraz ileride kumun üstünde uzun yeşil yosunlar vardı. Şakir şapkasını çıkardı ve ıslak yosunları içine doldurdu. Şapkayı kumdan aslanın yanına yavaşça getirdi. Yosunları aslanın başının çevresine tek tek dizdi. Kumdan aslanın yeşil bir yelesi oldu. Şakir aslana bakıp çok güldü. Sonra Şakir kumda mutlu mutlu yeni aslanlar yapmaya devam etti.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yosunları aslanın başının çevresine tek tek dizdi"
   - Cümle 7: «Yosunları aslanın başının çevresine tek tek dizdi.»
   - Açıklama: Sorunun sebebi kumun kuru olması ama çözüm kumu tutturmuyor, yalnız yosundan yele ekliyor.
   - Açıklama: Sorunun sebebi kumun kuru olması ama çözüm kumu ıslatmıyor, başın çevresine yele ekliyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kumdan aslanın yeşil bir yelesi oldu"
   - Cümle 8: «Kumdan aslanın yeşil bir yelesi oldu.»
   - Açıklama: Aslanın başı kuru kum dağıldığı için yapılamamışken başın çevresine yele dizilmiş gibi anlatılıyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Kumdan aslanın yeşil bir yelesi oldu"
   - Cümle 8: «Kumdan aslanın yeşil bir yelesi oldu.»
   - Açıklama: Kuru kumdan başın dağılma sorununun çözüldüğü hiç görünmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0259` birebir aynı, `@degisim: tasarlamak -> yapmak` (tutuyorsan), ardından `@onarim: 2fbbeeebc1000c8fc1d604cdbe8e8e15eeac0624`, sonra gövde.

### Hikâye 12: tohum sakir-0260 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0260
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'valiz', fiil 'şişirmek', sıfat 'resimli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: top kayboldu ve kumda yalnız bir iz kaldı | izin yanından yürüdü ve şapkasıyla yosunları itti
@tohum: sakir-0260
Şakir kumsalda havlusunun yanında resimli valizini açtı ve bir top çıkardı. Topu iyice şişirdi ve yere koydu. Ama Şakir arkasını dönünce top yerinde yoktu. Kumda yalnız ince, uzun bir iz vardı. Şakir bu izi çok merak etti. İzin yanından birkaç adım yürüdü. İz, küçük bir yosun yığınında bitiyordu. Şakir şapkasını çıkardı ve onunla yosunları dikkatle kenara itti. Altından topun kırmızı rengi göründü. Top rüzgarla yuvarlanmış ve yosunların altına girmişti. Şakir topunu çıkarıp sıkıca tuttu. Şakir çok sevindi, çünkü izin yanından yürüyüp topunu bulmuştu.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Top rüzgarla yuvarlanmış ve yosunların altına girmişti"
   - Cümle 10: «Top rüzgarla yuvarlanmış ve yosunların altına girmişti.»
   - Açıklama: Şişirilmiş bir topun küçük bir yosun yığınının altına girip gizlenmesi akla yatkın değil.
   - Açıklama: Şişirilmiş bir topun rüzgarla küçük bir yosun yığınının altına girmesi akla yatkın değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0260` birebir aynı, ardından `@onarim: a6b77f072f944f55e95de052c61c10b26bb2f10f`, sonra gövde.
