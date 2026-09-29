# Editör görevi (onarım): Şakir, onarım partisi 19

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar19.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar19.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0047 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0047
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: paylaşmak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'bulaşık', fiil 'yaklaştırmak', sıfat 'bulutlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kardeşi de oynamak istedi ama tek bir kova vardı | kovasını kardeşine yaklaştırıp birlikte kullandılar
@tohum: sakir-0047
@degisim: bulaşık -> kova
Bulutlu bir sabah Şakir ile kardeşi Canan kumsalda oynuyordu. Şakir kovasıyla kumdan büyük bir kale yapmaya başladı. Canan da oynamak istedi ama yanlarında tek bir kova vardı. Canan kumun üstüne oturdu ve üzgün üzgün baktı. Şakir bunu gördü ve kovayı kardeşine yaklaştırdı. "Canan, kovayı birlikte kullanalım, sonra kalede macera oyunu oynarız," dedi Şakir. Canan kovaya ıslak kum doldurdu ve ters çevirdi. Şakir de kumu eliyle düzeltti. Böylece ikisi sırayla yeni kuleler yaptı. "Bu bizim kalemiz olsun!" dedi Şakir. "Ben de kapısını yapayım," dedi Canan ve güldü. Şakir çok mutluydu, çünkü kovasını paylaşınca kale daha büyük ve güzel olmuştu.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kovasını kardeşine yaklaştırıp birlikte kullandılar"
   - Cümle 0 (plan satırı): «kardeşi de oynamak istedi ama tek bir kova vardı | kovasını kardeşine yaklaştırıp birlikte kullandılar»
   - Açıklama: '-ıp' ulacının öznesi tekil, ana fiil çoğul; özne uyumu bozuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kalede macera oyunu oynarız"
   - Cümle 6: «"Canan, kovayı birlikte kullanalım, sonra kalede macera oyunu oynarız," dedi Şakir.»
   - Açıklama: 'Macera' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Macera' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sonra kalede macera oyunu oynarız"
   - Cümle 6: «"Canan, kovayı birlikte kullanalım, sonra kalede macera oyunu oynarız," dedi Şakir.»
   - Açıklama: Tohumdaki macera özelliği yalnız süs olarak anılıyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki macera özelliği sorunu çözmede işe yaramıyor, yalnız süs olarak anılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "sonra kalede macera oyunu oynarız"
   - Cümle 6: «"Canan, kovayı birlikte kullanalım, sonra kalede macera oyunu oynarız," dedi Şakir.»
   - Açıklama: Söz verilen macera oyunu hiç oynanmıyor; kurulan ayrıntı kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0047` birebir aynı, `@degisim: bulaşık -> kova` (tutuyorsan), ardından `@onarim: 9c49b6c410a33fab211a9c413ea519088922d1c6`, sonra gövde.

### Hikâye 2: tohum sakir-0048 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0048
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'havuç', fiil 'yatmak', sıfat 'kırık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: havuç kırık bir kütüğün içine yuvarlandı | filden yardım istedi ve fil havucu hortumuyla çıkardı
@tohum: sakir-0048
Şakir ormandaki kamp yerinde Necati ile oturuyordu. Elinde Necati için büyük bir havuç vardı. Ama havuç elinden kaydı ve kırık bir kütüğün içine yuvarlandı. Kütük yerde yatıyordu, Şakir eğildi ve içine baktı. Havuç oradaydı, ama Şakir'in kolu ona yetişmedi. "Necati, bir macera oyunu oynayalım, havucu birlikte çıkarır mıyız?" diye sordu Şakir. Necati hortumunu kütüğün içine uzattı ve havucu çıkardı. "Buyur, bu senin için," dedi Şakir. Necati havucu yedi ve kulaklarını salladı. "Teşekkürler, Şakir, çok tatlıymış!" dedi Necati. Şakir çok sevindi, çünkü yardım isteyince havuç kütükten çıkmıştı.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bir macera oyunu oynayalım"
   - Cümle 6: «"Necati, bir macera oyunu oynayalım, havucu birlikte çıkarır mıyız?" diye sordu Şakir.»
   - Açıklama: Havucu çıkarmak için yardım isterken 'macera oyunu' sözü bağlama uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir macera oyunu oynayalım"
   - Cümle 6: «"Necati, bir macera oyunu oynayalım, havucu birlikte çıkarır mıyız?" diye sordu Şakir.»
   - Açıklama: 'Macera' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bir macera oyunu oynayalım"
   - Cümle 6: «"Necati, bir macera oyunu oynayalım, havucu birlikte çıkarır mıyız?" diye sordu Şakir.»
   - Açıklama: Tohumdaki macera özelliği yalnız bir etiket olarak ekleniyor; sorunu yardım istemek çözüyor, macera işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki macera özelliği çözüme katkı vermiyor; havucu Necati'nin hortumu çıkarıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir macera oyunu oynayalım"
   - Cümle 6: «"Necati, bir macera oyunu oynayalım, havucu birlikte çıkarır mıyız?" diye sordu Şakir.»
   - Açıklama: Önerilen macera oyunu hiç oynanmıyor ve olayda işlevsiz kalıyor.
5. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: ""Buyur, bu senin için," dedi Şakir"
   - Cümle 8: «"Buyur, bu senin için," dedi Şakir.»
   - Açıklama: Havucu hortumuyla çıkaran Necati olduğu halde 'Buyur' diyen kişi Şakir gösterilmiş; konuşan kişi tutarsız.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0048` birebir aynı, ardından `@onarim: 99f8374d41ad3bf88079ffe6212d2222a8e30d46`, sonra gövde.

### Hikâye 3: tohum sakir-0054 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0054
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'gölge', fiil 'somurtmak', sıfat 'kırmızı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: ipi sıkı tutunca uçurtma hep yere düştü | yeniden koştu ve ipi yavaş yavaş bıraktı
@tohum: sakir-0054
Şakir kumsalda ilk kez kırmızı bir uçurtma uçurmayı denedi. Ama uçurtma hep yere düştü, çünkü Şakir ipi hiç bırakmıyordu. Sonra şemsiyenin gölgesine oturdu ve biraz somurttu. Yine de bu yeni macera oyununu bir daha denemek istedi. Uçurtmaya ve ipe uzun uzun baktı. Denizden hafif bir rüzgar esiyordu. Şakir kalktı ve kumda yeniden koştu. Bu kez ipi yavaş yavaş bıraktı. Kırmızı uçurtma rüzgarla yükseldi ve havada kaldı. Şakir sevinçle zıpladı ve ipi sıkıca tuttu. Sonra kumsalda uçurtmasını mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "bu yeni macera oyununu"
   - Cümle 4: «Yine de bu yeni macera oyununu bir daha denemek istedi.»
   - Açıklama: Uçurtma uçurmak 'macera oyunu' değildir; kelime yanlış anlamda kullanılmış.
   - Açıklama: Uçurtma uçurmak 'macera oyunu' değil; kelime yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bu yeni macera oyununu"
   - Cümle 4: «Yine de bu yeni macera oyununu bir daha denemek istedi.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Macera' soyut bir kavram, küçük çocuk için ağır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0054` birebir aynı, ardından `@onarim: fd06c88099995ca65f52fe9c0079686cd6f1427c`, sonra gövde.

### Hikâye 4: tohum sakir-0055 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0055
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'pilav', fiil 'sararmak', sıfat 'iyi'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: yapraklar tencerenin altındaki delikten yere düştü | şapkasını ters çevirip yaprakları içine doldurdu
@tohum: sakir-0055
Şakir kamp yerinde, çadırın hemen önünde yemek oyunu oynuyordu. Sararmış yaprakları pilav yerine oyuncak tencereye koydu. Ama yapraklar tencerenin altındaki bir delikten yere düştü. Şakir üzüldü, çünkü delikli tencereyle pilav yapamazdı. Sonra başındaki şapkasına baktı. Şapkasını çıkardı ve ters çevirdi. Yaprakları yerden toplayıp şapkanın içine doldurdu. Bu kez hiçbir yaprak düşmedi. Şakir onları bir çubukla karıştırdı. Şimdi pilav çok iyi görünüyordu. Pilavı şapkadan oyuncak bir tabağa döktü. Şakir yemek oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Pilavı şapkadan oyuncak bir tabağa döktü"
   - Cümle 11: «Pilavı şapkadan oyuncak bir tabağa döktü.»
   - Açıklama: Oyuncak tabak sebepsiz beliriyor; tabak varken şapkaya gerek kalmaması çözümün mantığını zayıflatıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0055` birebir aynı, ardından `@onarim: a91ddae81ffc6421f3ba2b2b3ed9916f5f6fcfeb`, sonra gövde.

### Hikâye 5: tohum sakir-0056 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0056
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'taç', fiil 'düşürmek', sıfat 'ufak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: koşarken babasına çarptı ve tacı yere düşürdü | özür diledi ve yaprakları toplayıp tacı düzeltti
@tohum: sakir-0056
Şakir ormandaki kamp yerinde ağaçların arasında koşuyordu. Babası Remzi bir taşın üstünde oturmuş, yapraklardan ufak bir taç yapıyordu. Şakir koşarken babasının koluna çarptı ve tacı yere düşürdü. Tacın yaprakları otların arasına dağıldı. Şakir hemen durdu ve dağılan yapraklara baktı. "Özür dilerim, baba, seni görmedim," dedi Şakir. "Tamam, Şakir, birlikte düzeltelim," dedi Remzi ve gülümsedi. Macerayı çok seven Şakir otların arasındaki bütün yaprakları tek tek buldu. Sonra babasıyla birlikte onları taca taktı. Remzi tacı Şakir'in başına koydu ve ikisi de güldü. Şakir çok sevindi, çünkü özür dilemiş ve tacı babasıyla yeniden yapmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 8: «Macerayı çok seven Şakir otların arasındaki bütün yaprakları tek tek buldu.»
   - Açıklama: 'Macera' soyut bir kavram ve yaprak toplama sahnesine uymuyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir otların arasındaki"
   - Cümle 8: «Macerayı çok seven Şakir otların arasındaki bütün yaprakları tek tek buldu.»
   - Açıklama: Tohumdaki macera özelliği süs olarak anılıyor, tacı düzeltme çözümünde işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0056` birebir aynı, ardından `@onarim: f172de711402b6a1282331df10ff3d03f53e8db5`, sonra gövde.

### Hikâye 6: tohum sakir-0057 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0057
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'pirinç', fiil 'giydirmek', sıfat 'karmakarışık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: koşarken örtüye bastı ve elbise rüzgarla uçtu | özür diledi ve çalılarda elbiseyi bulup getirdi
@tohum: sakir-0057
@degisim: pirinç -> elbise
Rüzgar esiyordu ve Şakir kamp yerinde koşuyordu. Kardeşi Canan örtüde oyuncak bebeğine bir elbise hazırlıyordu. Şakir koşarken örtüye bastı ve elbise rüzgarla uçup kayboldu. Canan çok üzüldü, çünkü oyuncak bebeğinin başka elbisesi yoktu. Şakir hemen durdu ve kardeşinden özür diledi. Macerayı çok seven Şakir yakındaki karmakarışık çalılara eğilip baktı. Küçük elbise bir dala takılmıştı. Şakir elbiseyi dikkatle aldı ve Canan'a götürdü. İkisi oyuncak bebeğe elbiseyi birlikte giydirdi. Canan gülümsedi ve Şakir'e sarıldı. Şakir ile Canan oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şakir koşarken örtüye bastı ve elbise rüzgarla uçup kayboldu"
   - Cümle 3: «Şakir koşarken örtüye bastı ve elbise rüzgarla uçup kayboldu.»
   - Açıklama: Örtüye basmanın elbiseyi uçurması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0057` birebir aynı, `@degisim: pirinç -> elbise` (tutuyorsan), ardından `@onarim: 4df067abd957825411c212db10ac03ddc12ab898`, sonra gövde.

### Hikâye 7: tohum sakir-0059 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0059
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'giysi', fiil 'soğumak', sıfat 'sabırlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: rüzgarla birlikte ıslık gibi bir ses geldi | şapkasıyla büyük kabuğu kapatıp sesin yerini buldu
@tohum: sakir-0059
Deniz kıyısında hava biraz soğumuştu. Şakir ile Canan kalın giysiler içinde kumda oturuyordu. Birden rüzgarla birlikte ıslık gibi ince bir ses geldi. "Bu ses nereden geliyor?" diye sordu Şakir. "Sabırlı olalım ve dikkatle dinleyelim," dedi Canan. İkisi sessizce bekledi. Rüzgar yine esti ve ses büyük bir kabuğun yanından geldi. Şakir şapkasını çıkardı ve kabuğun üstüne kapattı. Islık hemen kesildi. Şakir şapkayı kaldırınca ıslık tekrar başladı. "Rüzgar kabuğun içine esince bu ses çıkıyor!" dedi Şakir. Şakir kabuğu kulağına tuttu ve güldü. Şakir çok sevindi, çünkü ıslık sesinin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şakir çok sevindi, çünkü"
   - Cümle 13: «Şakir çok sevindi, çünkü ıslık sesinin nereden geldiğini bulmuştu.»
   - Açıklama: Art arda cümleler gereksiz yere hep 'Şakir' adıyla başlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0059` birebir aynı, ardından `@onarim: 97636ac28f09f9cc6075d64f0036b4113a7225a2`, sonra gövde.

### Hikâye 8: tohum sakir-0060 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0060
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'altın', fiil 'birleşmek', sıfat 'turuncu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: tek bir turuncu kova vardı ve ikisi de istedi | kovayı sırayla kullanmayı önerdi
@tohum: sakir-0060
Şakir kumsalda Necati ile oyun oynuyordu. Oyuncak altın için kumdan büyük bir kale yapacaklardı. Ama tek bir turuncu kova vardı ve ikisi de onu istedi. "Necati, kovayı sırayla dolduralım mı?" diye sordu Şakir. "Olur, önce sen başla," dedi Necati. Şakir kovayı kumla doldurdu ve sol yanda bir kule yaptı. Sonra Necati kovayı aldı ve sağ yana ikinci bir kule dikti. Macerayı çok seven Şakir beklerken kaleye bir yol çizdi. Kuleler büyüdükçe duvarları ortada birleşti. Şakir oyuncak altını bu yoldan kalenin ortasına götürdü. "Ne güzel bir kale oldu, Şakir!" dedi Necati. Şakir çok sevindi, çünkü birlikte kocaman bir kale yapmışlardı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 8: «Macerayı çok seven Şakir beklerken kaleye bir yol çizdi.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 8: «Macerayı çok seven Şakir beklerken kaleye bir yol çizdi.»
   - Açıklama: Hikayenin ortasında Şakir sıfatla yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı çok seven Şakir beklerken"
   - Cümle 8: «Macerayı çok seven Şakir beklerken kaleye bir yol çizdi.»
   - Açıklama: Tohumdaki macera özelliği yalnız anılıyor, kovayı paylaşma sorununun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0060` birebir aynı, ardından `@onarim: cb47f7aaa47cd8174c2e306b8dd85b6fdf3db5d2`, sonra gövde.

### Hikâye 9: tohum sakir-0061 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0061
- yer: park (Şehirdeki park.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'buz', fiil 'güneşlenmek', sıfat 'yağmurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: rüzgar olmadığı için gemi suyun ortasında durdu | şapkasını salladı, rüzgar yaptı ve gemiyi getirdi
@tohum: sakir-0061
@degisim: buz -> gemi
Şakir yağmurlu bir sabahın sonunda evinin önündeki parkta güneşleniyordu. Oyuncak gemisini büyük bir su birikintisine bıraktı. Ama gemi suyun ortasında durdu, çünkü hiç rüzgar yoktu. Şakir suya girmek istemedi, çünkü ayakkabıları kuru kalmalıydı. Biraz düşündü ve sarı yağmur şapkasını başından çıkardı. Şapkayı suyun üstünde hızlı hızlı salladı. Şapkadan hafif bir rüzgar çıktı ve su kıpırdadı. Gemi yavaş yavaş Şakir'e doğru yüzdü. Şakir gemiyi aldı ve şapkasını başına taktı. Şakir çok mutluydu, çünkü gemisini suya girmeden kurtarmıştı.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Gemi yavaş yavaş Şakir'e doğru yüzdü"
   - Cümle 8: «Gemi yavaş yavaş Şakir'e doğru yüzdü.»
   - Açıklama: Şakir'in salladığı şapkanın rüzgarı gemiyi ondan uzağa itmeli, ama gemi ona doğru geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0061` birebir aynı, `@degisim: buz -> gemi` (tutuyorsan), ardından `@onarim: 40335233fcf602167dfb7ca95c0d216714c2ae50`, sonra gövde.

### Hikâye 10: tohum sakir-0063 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0063
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'balon', fiil 'yaratmak', sıfat 'sulu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: rüzgar babasının balonunu uçurdu | mavi balonunu babasına verdi
@tohum: sakir-0063
@degisim: yaratmak -> uçurmak
Rüzgar kamp yerinde birden hızlı esti. Şakir ile babası Remzi bir taşın üstünde oturmuş, sulu karpuz yiyordu. Remzi karpuzu iki eliyle tutarken rüzgar balonunu uçurdu. Balon ağaçların arkasında kayboldu ve Remzi üzüldü. Şakir'in elinde kırmızı ve mavi iki balon vardı. "Baba, mavi balonu sen al, sonra birlikte macera yürüyüşüne çıkalım," dedi Şakir. Sonra mavi balonun ipini babasının eline verdi. "Çok teşekkür ederim, Şakir!" dedi Remzi ve güldü. İkisi karpuzu bitirdi ve balonlarıyla ormanda mutlu mutlu yürüdü.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir'in elinde kırmızı ve mavi iki balon vardı"
   - Cümle 5: «Şakir'in elinde kırmızı ve mavi iki balon vardı.»
   - Açıklama: Karpuz yerken Şakir'in elindeki iki balon daha önce kurulmadan çözümü getirmek için sebepsizce beliriyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "birlikte macera yürüyüşüne çıkalım"
   - Cümle 6: «"Baba, mavi balonu sen al, sonra birlikte macera yürüyüşüne çıkalım," dedi Şakir.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "birlikte macera yürüyüşüne çıkalım"
   - Cümle 6: «"Baba, mavi balonu sen al, sonra birlikte macera yürüyüşüne çıkalım," dedi Şakir.»
   - Açıklama: Tohumdaki macera özelliği sorunun çözümünde işe yaramıyor, yalnız süs olarak anılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sonra birlikte macera yürüyüşüne çıkalım"
   - Cümle 6: «"Baba, mavi balonu sen al, sonra birlikte macera yürüyüşüne çıkalım," dedi Şakir.»
   - Açıklama: Tohumdaki macera özelliği çözümden sonra süs olarak ekleniyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0063` birebir aynı, `@degisim: yaratmak -> uçurmak` (tutuyorsan), ardından `@onarim: a0699043d51779428b9d1be3949e037fc4caebf3`, sonra gövde.

### Hikâye 11: tohum sakir-0064 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0064
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'etek', fiil 'yoğurmak', sıfat 'dar'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: bardak çok dar olduğu için kumdan pasta çıkmadı | şapkasını kalıp yapıp büyük bir pasta yaptı
@tohum: sakir-0064
@degisim: etek -> bardak
Kumsalda dalgaların sesi duyuluyordu. Şakir ile Necati ıslak kumu yoğurdu ve pasta yapmaya başladı. Ama Şakir'in bardağı çok dardı ve pasta bardaktan çıkmadı. Şakir bardağı salladı, ama kum içeride kaldı. "Pasta bardağa yapıştı!" dedi Necati ve ikisi birlikte güldü. Şakir geniş şapkasına baktı. Şapkayı çıkardı ve içini kumla doldurdu. Sonra şapkayı kumun üstüne ters çevirdi ve yavaşça kaldırdı. Kumda kocaman, yuvarlak bir pasta duruyordu. "Ne büyük bir pasta bu, Şakir!" dedi Necati. Necati hortumuyla pastanın üstüne küçük bir kabuk koydu. Şakir bundan sonra kumdan pastaları şapkasıyla yaptı.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kalıp yapıp büyük bir pasta yaptı"
   - Cümle 0 (plan satırı): «bardak çok dar olduğu için kumdan pasta çıkmadı | şapkasını kalıp yapıp büyük bir pasta yaptı»
   - Açıklama: Plan satırında 'yapıp' ve 'yaptı' gereksizce tekrarlanıyor.
2. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Şakir bundan sonra kumdan pastaları şapkasıyla yaptı"
   - Cümle 12: «Şakir bundan sonra kumdan pastaları şapkasıyla yaptı.»
   - Açıklama: Son cümle his ya da sıcak bir sonuç vermeyen çıplak bir alışkanlık eylemiyle bitiyor.
   - Açıklama: Son cümle his ya da sıcak bir sonuç vermeyen çıplak bir alışkanlık cümlesi; sıcak kapanış yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0064` birebir aynı, `@degisim: etek -> bardak` (tutuyorsan), ardından `@onarim: 9dfbdcfbd3d62bf8db686af80421f8171ba35ca6`, sonra gövde.

### Hikâye 12: tohum sakir-0070 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0070
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'ruj', fiil 'dokunmak', sıfat 'şirin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: şirin bir kabuk ağır bir kütüğün altında kaldı | yardım istedi ve fil kütüğü kenara itti
@tohum: sakir-0070
@degisim: ruj -> kütük
Denizden serin bir rüzgar esiyordu. Macerayı seven Şakir, Necati ile kumsalı geziyordu. Birden şirin, pembe bir kabuk gördü ama kabuk ağır bir kütüğün altındaydı. Şakir kütüğü iki eliyle çekti ama kütük hiç kıpırdamadı. "Necati, bana yardım eder misin?" diye sordu Şakir. Necati hortumuyla kütüğü kolayca kenara itti. Şakir kabuğu aldı ve parmağıyla yavaşça dokundu. Kabuğun içi parlak ve pürüzsüzdü. "Çok güzel bir kabuk buldun, Şakir," dedi Necati. "Teşekkürler, Necati, bu kabuğu hep saklayacağım!" dedi Şakir.
```

**Hakem bulguları (5):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı seven Şakir, Necati ile kumsalı geziyordu"
   - Cümle 2: «Macerayı seven Şakir, Necati ile kumsalı geziyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız sıfat olarak anılıyor; sorunu Necati'nin hortumu çözüyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Macerayı seven Şakir"
   - Cümle 2: «Macerayı seven Şakir, Necati ile kumsalı geziyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız sıfat olarak anılıyor, çözümde işe yaramıyor; kartın özellikler alanındaki gibi işlevsel kullanılmamış.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şakir kabuğu aldı ve parmağıyla yavaşça dokundu"
   - Cümle 7: «Şakir kabuğu aldı ve parmağıyla yavaşça dokundu.»
   - Açıklama: 'Dokundu' yönelme durumu ister; belirtme ekli 'kabuğu' ortak nesne olamaz, 'ona dokundu' gerekir.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kabuğu aldı ve parmağıyla yavaşça dokundu"
   - Cümle 7: «Şakir kabuğu aldı ve parmağıyla yavaşça dokundu.»
   - Açıklama: 'Dokundu' yönelme eki ister; ortak nesne 'kabuğu' ile uyumsuz, 'ona dokundu' olmalı.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "içi parlak ve pürüzsüzdü"
   - Cümle 8: «Kabuğun içi parlak ve pürüzsüzdü.»
   - Açıklama: 'Pürüzsüz' kelimesini 3 yaşındaki bir çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0070` birebir aynı, `@degisim: ruj -> kütük` (tutuyorsan), ardından `@onarim: 8873b869c2aac7b297dc16929f5ea3eac5289a4c`, sonra gövde.
