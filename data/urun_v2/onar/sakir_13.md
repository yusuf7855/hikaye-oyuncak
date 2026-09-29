# Editör görevi (onarım): Şakir, onarım partisi 13

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar13.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar13.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0035 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0035
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'mürekkep', fiil 'bağlamak', sıfat 'üzgün'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: filin kaleminin mürekkebi birden bitti | kendi kalemini verip sırayla çizdiler
@tohum: sakir-0035
@degisim: bağlamak -> paylaşmak
Şakir, Necati ile kamp yerinde bir orman haritası çiziyordu. Necati büyük ağaçları çizecekti. Ama Necati'nin kaleminin mürekkebi birden bitti. Necati üzgün bir yüzle kalemine baktı. "Kalemim artık çizmiyor," dedi Necati. Şakir bu haritayla bir macera gezisi yapmak istiyordu. Onun tek bir kırmızı kalemi vardı. Şakir kalemi hemen Necati'ye uzattı. "Kalemimi seninle paylaşırım, sırayla çizelim," dedi Şakir. Önce Necati ağaçları çizdi. Sonra Şakir çadırı ve yolu çizdi. Harita bitince Şakir ile Necati onu alıp kamp yerini mutlu mutlu gezdi.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kendi kalemini verip sırayla çizdiler"
   - Cümle 0 (plan satırı): «filin kaleminin mürekkebi birden bitti | kendi kalemini verip sırayla çizdiler»
   - Açıklama: Zarf-fiilin öznesi (kalemi veren tek kişi) ana fiilin çoğul öznesiyle uyuşmuyor ve 'kendi' kimi gösterdiği belirsiz.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir bu haritayla bir macera gezisi yapmak istiyordu"
   - Cümle 6: «Şakir bu haritayla bir macera gezisi yapmak istiyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenmiş, paylaşma çözümünde işe yaramıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onun tek bir kırmızı"
   - Cümle 7: «Onun tek bir kırmızı kalemi vardı.»
   - Açıklama: 'Onun' zamirinin Şakir'i mi Necati'yi mi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0035` birebir aynı, `@degisim: bağlamak -> paylaşmak` (tutuyorsan), ardından `@onarim: 51ccad88ae45fa1370b422fc1eb55b939a799f83`, sonra gövde.

### Hikâye 2: tohum sakir-0036 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0036
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'mobilya', fiil 'kaybetmek', sıfat 'sıcak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: aynı anda atıp kabukları karıştırdılar | sırayla atmayı önerdi ve birlikte saydılar
@tohum: sakir-0036
@degisim: mobilya -> kabuk
Kumsalda güneş çok sıcaktı ama Şakir'in geniş şapkası başını koruyordu. Şakir ile annesi Kadriye kovaya kabuk atıp yarışıyordu. Ama ikisi aynı anda attı ve hangi kabuğun kimin olduğunu bilemediler. "Anne, sırayla atalım mı?" diye sordu Şakir. "Olur, önce sen at," dedi Kadriye. Şakir bir kabuk attı ve kabuk kovaya girdi. Sonra Kadriye attı ama onun kabuğu kuma düştü. Her seferinde kovadaki kabukları birlikte saydılar. Sonunda kovada Kadriye'nin bir kabuğu daha fazlaydı. Şakir yarışı kaybetti ama güldü. "Tebrikler, anneciğim, sen kazandın!" dedi Şakir. Şakir yine de çok sevindi, çünkü sırayla oynayınca kabuklar hiç karışmamıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "geniş şapkası başını koruyordu"
   - Cümle 1: «Kumsalda güneş çok sıcaktı ama Şakir'in geniş şapkası başını koruyordu.»
   - Açıklama: Şapka ayrıntısı olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0036` birebir aynı, `@degisim: mobilya -> kabuk` (tutuyorsan), ardından `@onarim: c231a97fdfe34ba724a5fcc5ee068d842d56f5c1`, sonra gövde.

### Hikâye 3: tohum sakir-0037 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Remzi
@tohum: sakir-0037
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: bir şey yapmak
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'spagetti', fiil 'kokmak', sıfat 'rahat'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Remzi
@plan: spagetti çok uzundu ve tencereye sığmadı | spagettiyi ikiye kırmayı söyledi ve kendisi kırdı
@tohum: sakir-0037
Bir akşam Şakir babası Remzi ile mutfakta spagetti yapıyordu. Ama spagetti çok uzundu ve tencereye sığmadı. Remzi spagettiye şaşkın şaşkın baktı. "Baba, onları ikiye bölelim mi?" diye sordu Şakir. "Güzel fikir, Şakir," dedi Remzi. Şakir önce beyaz şapkasını taktı, böylece tüyleri yemeğe düşmeyecekti. Sonra spagettileri tabağın üstünde ikiye kırdı. Remzi kısa parçaları tencereye koydu. Bu kez hepsi tencereye sığdı. Biraz sonra mutfak çok güzel kokmaya başladı. Remzi yemeği iki tabağa koydu. Şakir ile Remzi rahat sandalyelere oturup yediler. Şakir çok mutluydu, çünkü yemeği babasıyla birlikte yapmıştı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kırmayı söyledi ve kendisi kırdı"
   - Cümle 0 (plan satırı): «spagetti çok uzundu ve tencereye sığmadı | spagettiyi ikiye kırmayı söyledi ve kendisi kırdı»
   - Açıklama: Planda söyleyenle kıranın kim olduğu belli değil; gövdede öneriyi Şakir yapıyor, kıran ise Remzi.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir önce beyaz şapkasını taktı"
   - Cümle 6: «Şakir önce beyaz şapkasını taktı, böylece tüyleri yemeğe düşmeyecekti.»
   - Açıklama: Şapka takma adımı çözüme hiçbir katkı yapmadan araya giren işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0037` birebir aynı, ardından `@onarim: 6453b163a8755c876a543bf6935238b56fbcc898`, sonra gövde.

### Hikâye 4: tohum sakir-0039 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0039
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'fide', fiil 'çekinmek', sıfat 'dolu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: su dolu kova çok ağırdı ve kaldıramadı | annesinden yardım isteyip kovayı birlikte taşıdı
@tohum: sakir-0039
@degisim: fide -> fidan
Bir sabah Şakir kamp yerinde küçük bir fidan dikti. Bu Şakir'in macera oyunuydu ve fidanı kendisi sulamak istedi. Ama su dolu kova çok ağırdı ve Şakir onu kaldıramadı. Annesi Kadriye çadırın önünde oturuyordu. Şakir ondan yardım istemekten biraz çekindi. Sonra annesinin yanına gitti. "Anne, kovayı birlikte taşır mıyız?" diye sordu Şakir. "Tabii, hemen geliyorum," dedi Kadriye. İkisi kovayı iki yanından tuttu ve fidanın yanına taşıdı. Şakir suyu fidana yavaş yavaş döktü. Kuru toprak ıslandı ve fidanın yaprakları parladı. "Teşekkürler, anneciğim, fidan artık susuz değil!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bu Şakir'in macera oyunuydu"
   - Cümle 2: «Bu Şakir'in macera oyunuydu ve fidanı kendisi sulamak istedi.»
   - Açıklama: 'Bu' zamirinin neyi gösterdiği belli değil; fidan dikmek bir macera oyunu olarak anlaşılmıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu Şakir'in macera oyunuydu"
   - Cümle 2: «Bu Şakir'in macera oyunuydu ve fidanı kendisi sulamak istedi.»
   - Açıklama: Fidan sulamaya macera oyunu denmesi özelliği yalnız anıyor; çözüm (anneden yardım istemek) özelliğe dayanmıyor.
   - Açıklama: Fidan sulamak macera değil; tohumdaki özellik işe yaramadan etiket olarak kullanılıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yardım istemekten biraz çekindi"
   - Cümle 5: «Şakir ondan yardım istemekten biraz çekindi.»
   - Açıklama: 'Çekinmek' soyut bir duygu kelimesi, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0039` birebir aynı, `@degisim: fide -> fidan` (tutuyorsan), ardından `@onarim: f3bc9375f4036ab22f7fba289c71e0ade9ddf582`, sonra gövde.

### Hikâye 5: tohum sakir-0041 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0041
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'muz', fiil 'uzaklaştırmak', sıfat 'yapışkan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: rüzgar esince tabaktaki muzlara kum uçmaya başladı | tabağı oradan uzaklaştırıp büyük taşın arkasına koydu
@tohum: sakir-0041
Bir sabah Canan kumsalda kitabını bitirdi ve kabuk toplamaya gitti. Şakir bunu kutlamak için ona gizlice bir tabak muz hazırladı. Ama rüzgar esti ve tabağa kum uçmaya başladı. Kumlu muzları kimse yiyemezdi. Şakir tabağı hemen oradan uzaklaştırdı. Onu büyük bir taşın arkasına koydu. Sonra kuma, taşa kadar giden oklar çizdi. Canan geri gelince Şakir onu bekliyordu. "Canan, bir macera oyunu oynayalım, okları izle!" dedi Şakir. Canan okları izledi ve taşın arkasında tabağı buldu. "Sürpriz, bu kutlama senin için!" dedi Şakir. "Ne güzel, çok teşekkür ederim!" dedi Canan. Sonra Şakir ile Canan taşın arkasına oturup yapışkan muzları mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yapışkan muzları mutlu mutlu"
   - Cümle 13: «Sonra Şakir ile Canan taşın arkasına oturup yapışkan muzları mutlu mutlu yedi.»
   - Açıklama: Muzun yapışkan olduğu hiçbir yerde kurulmadı; sıfat bağlama uymuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yapışkan muzları mutlu mutlu yedi"
   - Cümle 13: «Sonra Şakir ile Canan taşın arkasına oturup yapışkan muzları mutlu mutlu yedi.»
   - Açıklama: Muzların yapışkan olması için bir neden yok; kelime yanlış anlamda kullanılmış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "taşın arkasına oturup yapışkan muzları mutlu mutlu yedi"
   - Cümle 13: «Sonra Şakir ile Canan taşın arkasına oturup yapışkan muzları mutlu mutlu yedi.»
   - Açıklama: Muzların yapışkan olması sebepsiz beliriyor ve olaya bağlanmıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "yapışkan muzları mutlu mutlu yedi"
   - Cümle 13: «Sonra Şakir ile Canan taşın arkasına oturup yapışkan muzları mutlu mutlu yedi.»
   - Açıklama: Tabağa kum uçmuşken ve kumlu muzları kimse yiyemezken muzlar sonunda sorunsuz yeniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0041` birebir aynı, ardından `@onarim: 18c160b2e7bd4d3ca55039e60710019f385f1259`, sonra gövde.

### Hikâye 6: tohum sakir-0042 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0042
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kamyon', fiil 'yollamak', sıfat 'taze'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: oyuncak kamyon kumdaki çukura girdi ve takıldı | kamyonu çıkarıp çukuru kumla doldurdu
@tohum: sakir-0042
Parkta Şakir ile Necati kamyon oyunu oynuyordu. Şakir taze bir elmayı oyuncak kamyona koydu ve kamyonu Necati'ye yolladı. Ama kamyon kumdaki bir çukura girdi ve tekerlekleri takıldı. "Kamyon çukurdan çıkamıyor!" dedi Şakir. Şakir macera oyunlarında hiç vazgeçmezdi ve hemen çukurun başına koştu. Kamyonu çukurdan çıkardı. Sonra çukuru avuç avuç kumla doldurdu ve düzeltti. Kamyonu yeniden itip Necati'ye yolladı. Bu kez kamyon düz kumdan geçti ve Necati'nin önünde durdu. Necati elmayı hortumuyla aldı ve güldü. "Elma geldi, teşekkürler, Şakir!" dedi Necati. Sonra Şakir ile Necati oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "macera oyunlarında hiç vazgeçmezdi"
   - Cümle 5: «Şakir macera oyunlarında hiç vazgeçmezdi ve hemen çukurun başına koştu.»
   - Açıklama: 'Vazgeçmek' ayrılma eki ister; cümle dilbilgisel değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macera oyunlarında hiç vazgeçmezdi"
   - Cümle 5: «Şakir macera oyunlarında hiç vazgeçmezdi ve hemen çukurun başına koştu.»
   - Açıklama: 'Macera' ve 'vazgeçmek' soyut kavramlar, küçük çocuğa uygun değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "macera oyunlarında hiç vazgeçmezdi"
   - Cümle 5: «Şakir macera oyunlarında hiç vazgeçmezdi ve hemen çukurun başına koştu.»
   - Açıklama: 'Vazgeçmemek' soyut bir kavram ve küçük çocuğa uygun değil.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macera oyunlarında hiç vazgeçmezdi"
   - Cümle 5: «Şakir macera oyunlarında hiç vazgeçmezdi ve hemen çukurun başına koştu.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenmiş, çözümde işe yarar biçimde kullanılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0042` birebir aynı, ardından `@onarim: d693f5cfc07debb4c95a454c29d6fdceabaa69ea`, sonra gövde.

### Hikâye 7: tohum sakir-0043 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0043
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'yelek', fiil 'sevmek', sıfat 'cesur'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kırmızı yelek bir taneydi ve ikisi de istedi | sırayla giymeyi söyleyip önce kardeşine verdi
@tohum: sakir-0043
Bir sabah Şakir ile Canan kumsalda kumdan bir gemi yaptılar. Kırmızı yeleği giyen gemiyi sürecekti ama yelek bir taneydi. Şakir macera oyunlarını çok severdi ve gemiyi sürmek istedi, Canan da. "Canan, sırayla sürelim, önce sen giy," dedi Şakir. Canan yeleği giydi ve geminin önüne oturdu. "Çok cesuruz, gemimiz yola çıktı!" dedi Canan. Şakir onun arkasında iki eliyle kürek çekti. Sonra Canan yeleği çıkarıp Şakir'e verdi. Bu kez gemiyi Şakir sürdü ve Canan kürek çekti. Kardeşler bol bol güldü. Şakir çok sevindi, çünkü sırayla oynayınca ikisi de gemiyi sürmüştü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macera oyunlarını çok"
   - Cümle 3: «Şakir macera oyunlarını çok severdi ve gemiyi sürmek istedi, Canan da.»
   - Açıklama: 'Macera' soyut bir kelime, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0043` birebir aynı, ardından `@onarim: f24d2c7ba3200fc587636c9a86c2732569add5b3`, sonra gövde.

### Hikâye 8: tohum sakir-0045 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0045
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: kaybolan eşya
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'sabun', fiil 'çalıştırmak', sıfat 'şaşkın'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: rüzgar çantayı devirdi ve sabun kayboldu | şapkasıyla gözlerini güneşten korudu ve sabunu buldu
@tohum: sakir-0045
@degisim: çalıştırmak -> aramak
Ormandaki kamp yerinde hava sıcaktı. Şakir ile babası Remzi sabunla köpük yapmak istiyordu. Ama rüzgar çantayı devirmişti ve sabun kaybolmuştu. Şakir şaşkın bir yüzle boş çantaya baktı. Sonra çadırın önündeki otların arasında sabunu aramaya başladı. Güneş çok parlaktı ve Şakir iyi göremiyordu. Hemen kamp şapkasını gözlerinin üstüne doğru çekti. O zaman bir çalının dibinde beyaz bir şey gördü. Sabun oradaydı! Şakir onu aldı ve koşarak babasına götürdü. İkisi ellerini ovdu ve bol köpük yaptı. Remzi biraz köpüğü Şakir'in burnuna sürdü ve ikisi de güldü. Şakir çok sevindi, çünkü kaybolan sabunu kendisi bulmuştu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "köpüğü Şakir'in burnuna sürdü"
   - Cümle 12: «Remzi biraz köpüğü Şakir'in burnuna sürdü ve ikisi de güldü.»
   - Açıklama: Yüze ve buruna sabun köpüğü sürmek çocuğun taklit edebileceği, göze kaçma riski taşıyan bir davranış.
   - Açıklama: Sabun köpüğünü yüze sürmek çocuğun taklit edebileceği, göze kaçma riski taşıyan bir davranıştır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0045` birebir aynı, `@degisim: çalıştırmak -> aramak` (tutuyorsan), ardından `@onarim: ac1be10c662bf31eac53822d6f27980df5d04a22`, sonra gövde.

### Hikâye 9: tohum sakir-0047 (deneme 1 -> 2)

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
Bulutlu bir sabah Şakir ile kardeşi Canan kumsala geldi. Şakir kovasıyla kumdan bir kale yapmaya başladı. Canan da oynamak istedi ama yanlarında tek bir kova vardı. Canan kumun üstüne oturdu ve üzgün üzgün baktı. Şakir bunu gördü ve kovayı kardeşine yaklaştırdı. "Canan, kovayı birlikte kullanalım," dedi Şakir. Canan kovaya ıslak kum doldurdu ve ters çevirdi. Şakir de kumu eliyle düzeltti. Böylece ikisi sırayla yeni kuleler yaptı. "Bu bizim macera kalemiz olsun!" dedi Şakir. "Ben de kapısını yapayım," dedi Canan ve güldü. Şakir çok mutluydu, çünkü kovasını paylaşınca kale daha güzel olmuştu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bu bizim macera kalemiz"
   - Cümle 10: «"Bu bizim macera kalemiz olsun!" dedi Şakir.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bizim macera kalemiz olsun"
   - Cümle 10: «"Bu bizim macera kalemiz olsun!" dedi Şakir.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu bizim macera kalemiz"
   - Cümle 10: «"Bu bizim macera kalemiz olsun!" dedi Şakir.»
   - Açıklama: Tohumdaki macera özelliği yalnız süs olarak anılıyor, kovayı paylaşma çözümünde işe yaramıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Bu bizim macera kalemiz olsun!"
   - Cümle 10: «"Bu bizim macera kalemiz olsun!" dedi Şakir.»
   - Açıklama: Tohumdaki macera özelliği yalnız kaleye ad olarak geçiyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0047` birebir aynı, `@degisim: bulaşık -> kova` (tutuyorsan), ardından `@onarim: d4129f15c5dcd6010c1908fb1f12b850cc000f19`, sonra gövde.

### Hikâye 10: tohum sakir-0050 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0050
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yağ', fiil 'selamlamak', sıfat 'yakın'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: babası kule yapamadı çünkü kova yoktu ve kum dağıldı | şapkasına ıslak kum doldurup kule yaptı
@tohum: sakir-0050
@degisim: yağ -> kova
Şakir ile babası Remzi denize yakın bir yerde kumdan kale yapıyordu. Remzi kaleye bir kule eklemek istedi ama kovayı evde unutmuştu. Remzi kuru kumla denedi ama kum hep dağıldı. Şakir babasına yardım etmek istedi. Su kenarındaki ıslak kumu şapkasına doldurdu. Sonra onu kalenin üstüne ters çevirdi. Yavaşça kaldırınca kumdan bir kule çıktı. "Baba, bak, yuvarlak bir kule!" dedi Şakir. Remzi elini kaldırdı ve kuleyi selamladı. "Teşekkürler, Şakir, kalemiz çok güzel oldu," dedi Remzi. Şakir bundan sonra kuleleri hep ıslak kumla yaptı.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra onu kalenin üstüne ters çevirdi"
   - Cümle 6: «Sonra onu kalenin üstüne ters çevirdi.»
   - Açıklama: Önceki cümlede hem kum hem şapka geçtiği için 'onu' zamirinin şapkayı mı kumu mu gösterdiği belirsiz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "elini kaldırdı ve kuleyi selamladı"
   - Cümle 9: «Remzi elini kaldırdı ve kuleyi selamladı.»
   - Açıklama: Kumdan kuleyi selamlamak bağlama uymayan, yanlış seçilmiş bir fiil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0050` birebir aynı, `@degisim: yağ -> kova` (tutuyorsan), ardından `@onarim: e7736215a8391f3f6ed02cc7b0325168fcdbd4b7`, sonra gövde.

### Hikâye 11: tohum sakir-0053 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0053
- yer: park (Şehirdeki park.)
- tema: yağmur ya da kar günü
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'böğürtlen', fiil 'okşamak', sıfat 'vanilyalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: yağmur başladı ve damlalar kekin üstüne düştü | şapkasını kekin üstüne tuttu ve ağacın altına koştular
@tohum: sakir-0053
Bir sabah Şakir ile annesi Kadriye parkta bir bankta oturuyordu. Kadriye vanilyalı bir kek getirmişti ve üstünde böğürtlenler vardı. Birden yağmur başladı ve damlalar kekin üstüne düştü. Şakir hemen şapkasını çıkardı ve onun üstüne tuttu. Sonra ikisi büyük bir ağacın altına koştu. Yağmur yaprakların üstüne tıp tıp damlıyordu ama kek kuru kaldı. "Aferin, Şakir, kekimiz ıslanmadı," dedi Kadriye ve Şakir'in başını okşadı. Kadriye keki ikiye böldü. Şakir önce bir böğürtlen yedi. "Çok tatlı, anneciğim!" dedi Şakir. İkisi ağacın altında keklerini mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "çıkardı ve onun üstüne tuttu"
   - Cümle 4: «Şakir hemen şapkasını çıkardı ve onun üstüne tuttu.»
   - Açıklama: 'Onun' zamirinin keki mi Kadriye'yi mi gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve onun üstüne tuttu"
   - Cümle 4: «Şakir hemen şapkasını çıkardı ve onun üstüne tuttu.»
   - Açıklama: 'Onun' zamirinin keki mi Kadriye'yi mi gösterdiği belli değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "ama kek kuru kaldı"
   - Cümle 6: «Yağmur yaprakların üstüne tıp tıp damlıyordu ama kek kuru kaldı.»
   - Açıklama: Damlalar kekin üstüne zaten düşmüşken kekin kuru kaldığı ve ıslanmadığı söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0053` birebir aynı, ardından `@onarim: e7e07ff3ded671676e523f7bd1abe31fe094e1ed`, sonra gövde.

### Hikâye 12: tohum sakir-0054 (deneme 1 -> 2)

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
@plan: uçurtma hep yere düştü çünkü ipi bırakmıyordu | yeniden koştu ve ipi yavaş yavaş bıraktı
@tohum: sakir-0054
Şakir kumsalda ilk kez kırmızı bir uçurtma uçurmayı denedi. Macerayı çok severdi ve bu yeni oyunu merak ediyordu. Ama uçurtma hep yere düştü, çünkü Şakir ipi hiç bırakmıyordu. Şakir şemsiyenin gölgesine oturdu ve biraz somurttu. Sonra uçurtmaya ve ipe uzun uzun baktı. Denizden hafif bir rüzgar esiyordu. Şakir kalktı ve kumda yeniden koştu. Bu kez ipi yavaş yavaş bıraktı. Kırmızı uçurtma rüzgarla yükseldi ve havada kaldı. Şakir sevinçle zıpladı ve ipi sıkıca tuttu. Sonra kumsalda uçurtmasını mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "düştü çünkü ipi bırakmıyordu"
   - Cümle 0 (plan satırı): «uçurtma hep yere düştü çünkü ipi bırakmıyordu | yeniden koştu ve ipi yavaş yavaş bıraktı»
   - Açıklama: Plan satırında 'bırakmıyordu' fiilinin öznesi belirsiz, uçurtma gibi okunuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok severdi"
   - Cümle 2: «Macerayı çok severdi ve bu yeni oyunu merak ediyordu.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0054` birebir aynı, ardından `@onarim: f73e4922d44c449ef85ef7a229df3bf907c4b2c4`, sonra gövde.
