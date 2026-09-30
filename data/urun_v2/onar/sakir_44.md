# Editör görevi (onarım): Şakir, onarım partisi 44

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar44.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar44.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0238 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0238
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'şort', fiil 'döndürmek', sıfat 'peynirli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: şemsiyeyi oyun için döndürdü ve şemsiyenin sapı kırıldı | babasından özür diledi ve ona şapkasını taktı
@tohum: sakir-0238
@degisim: şort -> gölge
Kumsalda sıcak bir rüzgar esiyordu. Şakir, babası Remzi'nin şemsiyesini oyun için döndürdü. Şemsiye kuma devrildi ve sapı kırıldı. Kırık şemsiye artık gölge yapmıyordu. Remzi peynirli sandviçini yiyordu ve güneş yüzüne vuruyordu. Şakir hemen babasının yanına gitti ve ondan özür diledi. Sonra kendi geniş şapkasını çıkardı. Şapkayı babasının başına taktı. Şapka Remzi'nin yüzünü güneşten korudu. Remzi gülümsedi ve Şakir'e teşekkür etti. Sonra sandviçini rahatça yedi. Şakir bundan sonra şemsiyeyle hiç oynamadı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ona şapkasını taktı"
   - Cümle 0 (plan satırı): «şemsiyeyi oyun için döndürdü ve şemsiyenin sapı kırıldı | babasından özür diledi ve ona şapkasını taktı»
   - Açıklama: 'Şapkasını' Şakir'in mi babanın mı şapkası olduğu belli değil.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "şemsiyesini oyun için döndürdü"
   - Cümle 2: «Şakir, babası Remzi'nin şemsiyesini oyun için döndürdü.»
   - Açıklama: Çocuğun taklit edebileceği biçimde ağır plaj şemsiyesi oyun için döndürülüp devriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0238` birebir aynı, `@degisim: şort -> gölge` (tutuyorsan), ardından `@onarim: 4ca398a3b2e595fdede7a0ac72c55ddaf9defa25`, sonra gövde.

### Hikâye 2: tohum sakir-0239 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0239
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'patlıcan', fiil 'yatırmak', sıfat 'kokulu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: kabuklar çoktu ama avucuna yalnız üç kabuk sığdı | kabukları şapkasına doldurup kaleye taşıdı
@tohum: sakir-0239
@degisim: patlıcan -> kabuk
Bir sabah dalgalar kumsala bir sürü beyaz kabuk getirmişti. Şakir onlarla kumdaki kalesini süslemek istedi. Ama küçük avucuna yalnız üç kabuk sığıyordu. Kale de kabuklardan biraz uzaktaydı. Şakir başındaki şapkayı çıkardı ve kuma koydu. Şapkanın içini kabuklarla doldurdu. Kabukların arasında kokulu yosunlar da vardı. Şakir yosunları ayırdı ve kenara bıraktı. Sonra şapkayı iki eliyle kaleye taşıdı. Kabukları kalenin çevresine tek tek yatırdı. Kale beyaz kabuklarla çok güzel oldu. Şakir bundan sonra çok şey taşırken elleri yerine bir kap kullandı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kabukların arasında kokulu yosunlar da vardı"
   - Cümle 7: «Kabukların arasında kokulu yosunlar da vardı.»
   - Açıklama: Yosunlar sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Yosunlar kuruluyor ama olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0239` birebir aynı, `@degisim: patlıcan -> kabuk` (tutuyorsan), ardından `@onarim: b5a49d2352d8c6a9d4d995c97b856b9d0220a120`, sonra gövde.

### Hikâye 3: tohum sakir-0241 (deneme 1 -> 2)

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
@plan: tek tren vardı ve ikisi de onu itmek istedi | şapkayı takan treni itti ve şapka sırayla dolaştı
@tohum: sakir-0241
@degisim: dürüst -> kısa
Bir sabah Şakir ile Canan kumsalda oyuncak trenle oynuyordu. Kumda uzun bir tren yolu yapmışlardı. Ama tek bir tren vardı ve ikisi de onu itmek istedi. Şakir şapkasını çıkardı ve Canan'ın başına taktı. Artık treni yalnız şapkayı takan itiyordu. Canan treni yolda kısa bir süre itti. Sonra başını eğdi, şapkayı çıkardı ve Şakir'e verdi. Şakir de şapkayı taktı ve treni yolun sonuna kadar götürdü. Böylece ikisi de sırayla oynadı ve kimse üzülmedi. Şakir ile Canan oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "şapkayı takan treni itti"
   - Cümle 0 (plan satırı): «tek tren vardı ve ikisi de onu itmek istedi | şapkayı takan treni itti ve şapka sırayla dolaştı»
   - Açıklama: Plan satırı 'şapkayı takan tren' diye okunabiliyor; özne belirsiz kuruluş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0241` birebir aynı, `@degisim: dürüst -> kısa` (tutuyorsan), ardından `@onarim: d13ee8e7b622130b2fb7c248dcb4dbe1441357fb`, sonra gövde.

### Hikâye 4: tohum sakir-0242 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Remzi
@tohum: sakir-0242
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'nota', fiil 'örmek', sıfat 'puantiyeli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Remzi
@plan: ince ipleri örmeye çalıştı ama ipler karıştı | babasından yardım isteyip ipleri birlikte ördü
@tohum: sakir-0242
@degisim: nota -> ip
Dışarıda rüzgar hızlı hızlı esiyordu. Şakir, puantiyeli şapkasına bağlamak için üç ince ipi örmek istedi. Ama ipler hep karıştı. Şakir babası Remzi'nin yanına gitti ve ondan yardım istedi. Remzi iplerin bir ucunu sıkıca tuttu. Şakir de ipleri sırayla üst üste geçirdi. Bu kez ipler düzgün kaldı. Sonunda uzun ve sağlam bir ip oldu. Şakir ipi şapkasının iki yanına bağladı. Sonra şapkayı taktı ve ipi sıkıca çekti. Remzi gülerek ellerini çırptı. Şakir çok sevindi, çünkü şapkası artık rüzgarda başında kalacaktı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "puantiyeli şapkasına bağlamak için"
   - Cümle 2: «Şakir, puantiyeli şapkasına bağlamak için üç ince ipi örmek istedi.»
   - Açıklama: 'Puantiyeli' kelimesini 3 yaşındaki bir çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "puantiyeli şapkasına bağlamak"
   - Cümle 2: «Şakir, puantiyeli şapkasına bağlamak için üç ince ipi örmek istedi.»
   - Açıklama: 'Puantiyeli' kelimesini 3 yaşındaki bir çocuk bilmez.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama ipler hep karıştı"
   - Cümle 3: «Ama ipler hep karıştı.»
   - Açıklama: İplerin neden karıştığı söylenmiyor; sorunun sebebi yok.
   - Açıklama: İplerin neden karıştığı söylenmiyor; sorunun sebebi eksik.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0242` birebir aynı, `@degisim: nota -> ip` (tutuyorsan), ardından `@onarim: 75c497ecca972efde587f4d2d077ca730baa421a`, sonra gövde.

### Hikâye 5: tohum sakir-0243 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: filin yiyeceği yoktu ve rüzgar çok sertti | cipsi şapkaya koyup filin önüne bıraktı
@tohum: sakir-0243
Bir sabah ormandaki kamp yerinde hava çok rüzgarlıydı. Şakir ile Necati bir ağacın altında oturuyordu. Şakir'in bir paket cipsi vardı, ama Necati'nin yanında hiç yiyecek yoktu. Şakir yiyeceğini Necati ile paylaşmak istedi. Paketin ipini çekti ve ip hemen çözüldü. Ama rüzgar çok sertti ve ilk parçalar hemen uçtu. Şakir şapkasını çıkardı ve paketin yarısını içine boşalttı. Şapkayı Necati'nin önüne bıraktı. Necati hortumuyla parçaları tek tek aldı ve yedi. Şapkanın içindekiler hiç uçmadı. Şakir de kendi yarısını yedi. Şakir çok sevindi, çünkü Necati'nin de karnı doymuştu.
```

**Hakem bulguları (4):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "filin yiyeceği yoktu ve rüzgar çok sertti"
   - Cümle 0 (plan satırı): «filin yiyeceği yoktu ve rüzgar çok sertti | cipsi şapkaya koyup filin önüne bıraktı»
   - Açıklama: Hikayede Necati'nin yiyeceğinin olmaması ve rüzgarın cipsleri uçurması olmak üzere iki ayrı sorun var.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ve ilk parçalar hemen uçtu"
   - Cümle 6: «Ama rüzgar çok sertti ve ilk parçalar hemen uçtu.»
   - Açıklama: 'ilk parçalar' anlamca belirsiz; cipsten söz edildiği belli değil.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar çok sertti"
   - Cümle 6: «Ama rüzgar çok sertti ve ilk parçalar hemen uçtu.»
   - Açıklama: Çözülen asıl sorun olan rüzgarın cipsleri uçurması ancak 6. cümlede ortaya çıkıyor.
4. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama rüzgar çok sertti ve ilk parçalar hemen uçtu"
   - Cümle 6: «Ama rüzgar çok sertti ve ilk parçalar hemen uçtu.»
   - Açıklama: Necati'nin yiyeceğinin olmaması ve rüzgarın cipsi uçurması iki ayrı sorun olarak işleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0243` birebir aynı, ardından `@onarim: a3b1ac9aa5f152e38f9f3dc10727ec419b814c02`, sonra gövde.

### Hikâye 6: tohum sakir-0244 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0244
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'zarf', fiil 'unutmak', sıfat 'bilgili'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: sürpriz zarfı havluya koymak istedi ama rüzgar zarfı uçuruyordu | zarfın üstüne şapkasını koydu
@tohum: sakir-0244
@degisim: bilgili -> sarı
Bir sabah Şakir ile annesi Kadriye kumsaldaydı. Kadriye'nin doğum günüydü, ama annesi bunu unutmuştu. Şakir sarı bir zarfı havluya bırakmak istedi, ama rüzgar zarfı hep uçuruyordu. Zarfın içinde annesi için yaptığı bir resim vardı. Kadriye suyun kenarında kabuk topluyordu. Şakir zarfı havluya koydu ve üstüne şapkasını bıraktı. Zarf artık hiç kıpırdamadı. Kadriye dönünce şapkayı gördü. "Bu şapka neden burada?" diye sordu Kadriye. "Kaldır da bak, anneciğim," dedi Şakir. Kadriye şapkayı kaldırdı ve zarfı açtı. "Ne güzel bir resim, teşekkürler, Şakir!" dedi Kadriye. Sonra ikisi kumda mutlu mutlu kale yaptı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ama annesi bunu unutmuştu"
   - Cümle 2: «Kadriye'nin doğum günüydü, ama annesi bunu unutmuştu.»
   - Açıklama: 'Annesi' Kadriye'nin annesini mi Şakir'in annesini mi gösterdiği belli değil.
   - Açıklama: 'Annesi' Kadriye'nin annesini gösteriyor gibi okunuyor; kastedilen Kadriye'nin kendisi.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kadriye'nin doğum günüydü, ama annesi bunu unutmuştu"
   - Cümle 2: «Kadriye'nin doğum günüydü, ama annesi bunu unutmuştu.»
   - Açıklama: Doğum günü ve unutulma ayrıntısı kuruluyor ama sonda hiç kullanılmıyor.
   - Açıklama: Doğum günü ve unutulması kuruluyor ama olayda hiç kullanılmıyor, ayrıca annesi Kadriye'nin kendisi olduğu için karışık.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0244` birebir aynı, `@degisim: bilgili -> sarı` (tutuyorsan), ardından `@onarim: 26b5f834d4dc2648cf996e6d1d6eb34bd89a0d18`, sonra gövde.

### Hikâye 7: tohum sakir-0246 (deneme 1 -> 2)

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
Bir sabah Şakir kumsalda ilk kez kumdan bir kule yapmayı denedi. Ama kule hep yıkıldı, çünkü kum çok kuruydu. Kuru kum elinden hep dökülüyordu. Şakir suyun kenarına yürüdü ve ıslak kuma dokundu. Islak kum yumuşaktı ve hiç dökülmüyordu. Şakir şapkasını çıkardı ve ıslak kumla doldurdu. Şapkayı çevirip kuma bastırdı ve yavaşça kaldırdı. Kumda yuvarlak ve yüksek bir kule duruyordu. Şakir yanına iki kule daha yaptı. Tam o sırada karnı guruldadı. Çantasından meyveli kekini çıkardı ve yedi. Sonra Şakir mutlu mutlu yeni kuleler yapmaya devam etti.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir suyun kenarına yürüdü"
   - Cümle 4: «Şakir suyun kenarına yürüdü ve ıslak kuma dokundu.»
   - Açıklama: Güvenli kullanım satırına aykırı biçimde Şakir kumsalda yanında büyük olmadan tek başına su kenarına gidiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Tam o sırada karnı guruldadı"
   - Cümle 10: «Tam o sırada karnı guruldadı.»
   - Açıklama: Karnın guruldaması ve kek yemek olayla ilgisiz, işlevsiz bir ayrıntı.
   - Açıklama: Acıkma ve kek yeme olayı kule sorunuyla ilgisiz, işlevsiz bir ek olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0246` birebir aynı, `@degisim: vazo -> kum` (tutuyorsan), ardından `@onarim: 71bf1f46d14081272e9c2618b41481659f5ea00d`, sonra gövde.

### Hikâye 8: tohum sakir-0251 (deneme 1 -> 2)

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
@plan: kitabı hızla çekince bir sayfa koptu | sayfayı şapkasıyla yakalayıp bantla yapıştırdı ve özür diledi
@tohum: sakir-0251
Kumsalda Canan bir havlunun üstünde kitap okuyordu. Şakir resimlere bakmak için kitabı hızla kendine çekti. Bir sayfa koptu ve rüzgar onu kumun üstünde uçurdu. Canan şaşkın şaşkın Şakir'e baktı. Şakir kağıdın arkasından koştu. Şapkasını kağıdın üstüne attı ve kağıt olduğu yerde kaldı. Kağıdı alıp Canan'a geri getirdi. "Özür dilerim, Canan, kitabını hızla çektim," dedi Şakir. "Çantada bant var," dedi Canan. Şakir sayfayı bantla kitaba dikkatle yapıştırdı. Canan gülümsedi ve Şakir'e resimleri gösterdi. Şakir çok sevindi, çünkü kardeşinin kitabı yeniden tamamdı.
```

**Hakem bulguları (3):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "sayfayı şapkasıyla yakalayıp bantla yapıştırdı ve özür diledi"
   - Cümle 0 (plan satırı): «kitabı hızla çekince bir sayfa koptu | sayfayı şapkasıyla yakalayıp bantla yapıştırdı ve özür diledi»
   - Açıklama: Çözüm kovalama, şapkayla yakalama, özür ve bantlama olmak üzere ikiden fazla adım sürüyor.
2. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "rüzgar onu kumun üstünde uçurdu"
   - Cümle 3: «Bir sayfa koptu ve rüzgar onu kumun üstünde uçurdu.»
   - Açıklama: Sayfanın kopmasının yanına sayfanın rüzgarla uçması ikinci bir sorun olarak ekleniyor.
   - Açıklama: Sayfanın kopmasına bir de rüzgarın sayfayı uçurması ekleniyor ve hikaye iki ayrı sorunla uğraşıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çünkü kardeşinin kitabı yeniden tamamdı"
   - Cümle 12: «Şakir çok sevindi, çünkü kardeşinin kitabı yeniden tamamdı.»
   - Açıklama: Canan'ın Şakir'in kardeşi olduğu hiç kurulmadan son cümlede birden ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0251` birebir aynı, ardından `@onarim: e2ebe76c5485435ba92c70a38b0dcf2c75e056c3`, sonra gövde.

### Hikâye 9: tohum sakir-0252 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0252
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'masa', fiil 'barışmak', sıfat 'koyu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: hafif kutu devrildi ve kenarı yırtıldı | şapkasını masaya koyup topları onun içine attı
@tohum: sakir-0252
@degisim: barışmak -> zıplamak
Bir sabah Şakir evde komik bir oyun oynuyordu. Kağıttan toplar yapıp masadaki koyu mavi kutuya atıyordu. Ama kutu çok hafifti ve bir top çarpınca yere düştü. Kutunun bir yanı yırtıldı ve toplar oradan dışarı yuvarlandı. Şakir başındaki şapkayı çıkardı ve masanın ortasına koydu. Şapka geniş ve sağlamdı. Şakir ilk topu attı ve top şapkanın içine girdi. Şakir sevinçle zıpladı. Sonra bir top daha attı ve bu kez kükredi. Her top girince sesi biraz daha yükseldi. Sonunda beş topun hepsi şapkanın içindeydi. Şakir oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "bir top çarpınca yere düştü"
   - Cümle 3: «Ama kutu çok hafifti ve bir top çarpınca yere düştü.»
   - Açıklama: Yere düşenin kutu mu top mu olduğu belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bu kez kükredi"
   - Cümle 9: «Sonra bir top daha attı ve bu kez kükredi.»
   - Açıklama: Kükreme hiçbir hazırlık olmadan beliriyor ve olayda işlevi olmayan bir ayrıntı olarak kalıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir top daha attı ve bu kez kükredi"
   - Cümle 9: «Sonra bir top daha attı ve bu kez kükredi.»
   - Açıklama: Şakir'in kükremesi sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0252` birebir aynı, `@degisim: barışmak -> zıplamak` (tutuyorsan), ardından `@onarim: 3d273479d9bb8d014289d5b43dafe67571f85090`, sonra gövde.

### Hikâye 10: tohum sakir-0254 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0254
- yer: park (Şehirdeki park.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'baston', fiil 'güvenmek', sıfat 'sağlam'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: sürpriz için yaprak topladı ama rüzgar onları uçurdu | yaprakları şapkasının içinde topladı
@tohum: sakir-0254
@degisim: baston -> yaprak
Bir sabah Şakir ile annesi Kadriye parktaydı. Kadriye sağlam bir bankta oturuyordu ve Şakir ona sürpriz hazırlamak istedi. Sarı yapraklar topladı, ama rüzgar onları elinden uçurdu. Şakir başındaki şapkayı çıkardı ve yere koydu. Yaprakları tek tek şapkanın içine koydu. Bu kez yapraklar şapkanın içinde kaldı. Şakir bankın yanına gitti. "Gözlerini kapat, anneciğim," dedi Şakir. Kadriye Şakir'e güvendi ve gözlerini kapattı. Şakir şapkayı annesinin kucağına bıraktı. Kadriye gözlerini açınca sarı yaprakları gördü. "Ne güzel bir sürpriz, teşekkürler, Şakir!" dedi Kadriye. Sonra ikisi yapraklarla bankta mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar onları elinden uçurdu"
   - Cümle 3: «Sarı yapraklar topladı, ama rüzgar onları elinden uçurdu.»
   - Açıklama: Rüzgarın yaprakları dağıtıp yeniden toplanması önemsiz, örnekteki 'yaprakları dağıttı, topladı, bitti' türünde bir sorun.
   - Açıklama: Rüzgarın yaprakları uçurması ve yeniden toplanması önemsiz bir sorun; talimattaki örnekle aynı kalıp.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kadriye Şakir'e güvendi"
   - Cümle 9: «Kadriye Şakir'e güvendi ve gözlerini kapattı.»
   - Açıklama: 'Güvenmek' soyut bir kavram, 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Güvenmek' 3 yaşındaki çocuk için soyut bir kavram.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0254` birebir aynı, `@degisim: baston -> yaprak` (tutuyorsan), ardından `@onarim: 13bbcd1da9df9f66856cd4317698260fddbfa275`, sonra gövde.

### Hikâye 11: tohum sakir-0259 (deneme 1 -> 2)

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
@plan: kum hep dağıldı ve aslanın tüylerini yapamadı | yosunları şapkayla getirip tüy yaptı
@tohum: sakir-0259
Serin bir rüzgar esiyordu. Şakir kumsalda kumdan bir aslan yapmayı tasarladı. Aslanın gövdesini yaptı, ama kum hep dağıldı ve tüylerini yapamadı. Suyun kenarında uzun yeşil yosunlar vardı. Ama yosunlar ıslak ve kaygandı, elinden kayıp düşüyordu. Şakir şapkasını çıkardı ve yosunları içine doldurdu. Şapkayı kumdan aslanın yanına getirdi. Yosunları aslanın başının çevresine tek tek dizdi. Kumdan aslanın yeşil tüyleri oldu. Şakir aslana bakıp güldü. Sonra Şakir kumda mutlu mutlu yeni aslanlar yapmaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir aslan yapmayı tasarladı"
   - Cümle 2: «Şakir kumsalda kumdan bir aslan yapmayı tasarladı.»
   - Açıklama: 'Tasarlamak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime; 'yapmak istedi' olmalı.
   - Açıklama: 'Tasarlamak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Tasarlamak' 3 yaşındaki bir çocuğun bilmediği soyut bir kelime.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "kum hep dağıldı ve tüylerini yapamadı"
   - Cümle 3: «Aslanın gövdesini yaptı, ama kum hep dağıldı ve tüylerini yapamadı.»
   - Açıklama: Aynı kumla gövde yapılabiliyorken tüylerde kumun neden dağıldığı söylenmiyor, sebep belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0259` birebir aynı, ardından `@onarim: 499965606fab686b21475baaffffe603de5da7c9`, sonra gövde.

### Hikâye 12: tohum sakir-0260 (deneme 1 -> 2)

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
@plan: top kayboldu ve kumda yalnız bir iz kaldı | izin yanından yürüdü ve şapkasıyla kumu dağıttı
@tohum: sakir-0260
Şakir kumsalda resimli valizi açtı ve bir top çıkardı. Topu iyice şişirdi ve yere koydu. Ama Şakir arkasını dönünce top yerinde yoktu. Kumda yalnız ince, uzun bir iz vardı. Şakir bu izi çok merak etti. İzin yanından yavaş yavaş yürüdü. İz küçük bir çukurda bitiyordu. Çukurun içi kumla doluydu. Şakir şapkasını çıkardı ve onunla kumu dikkatle kenara itti. Altından topun kırmızı rengi göründü. Top rüzgarla yuvarlanmış ve çukura düşmüştü. Şakir topunu çıkarıp sıkıca tuttu. Şakir çok sevindi, çünkü iz onu topuna götürmüştü.
```

**Hakem bulguları (4):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir kumsalda resimli valizi"
   - Cümle 1: «Şakir kumsalda resimli valizi açtı ve bir top çıkardı.»
   - Açıklama: Şakir deniz kıyısında yanında bir büyük olmadan tek başına; güvenli özellik kullanımı satırı tek başına uzağa gitmemesini söylüyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "İzin yanından yavaş yavaş yürüdü"
   - Cümle 6: «İzin yanından yavaş yavaş yürüdü.»
   - Açıklama: Şakir kumsalda yanında bir büyük olmadan tek başına izi takip ederek yürüyor; güvenli özellik kullanımı satırı tek başına uzağa gitmemesini söylüyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Çukurun içi kumla doluydu"
   - Cümle 8: «Çukurun içi kumla doluydu.»
   - Açıklama: Rüzgarla yuvarlanan topun çukurda kumun altına gömülmesi akla yatkın değil.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Top rüzgarla yuvarlanmış ve çukura düşmüştü"
   - Cümle 11: «Top rüzgarla yuvarlanmış ve çukura düşmüştü.»
   - Açıklama: Rüzgarla yuvarlanan şişkin topun çukurda kumun altına gömülmesi akla yatkın biçimde açıklanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0260` birebir aynı, ardından `@onarim: 212a33996cfe3fab059aebd9520364a8dec756f2`, sonra gövde.
