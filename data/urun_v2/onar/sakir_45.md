# Editör görevi (onarım): Şakir, onarım partisi 45

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar45.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar45.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0261 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0261
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bezelye', fiil 'satmak', sıfat 'ahşap'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: hızlı koşarken masaya çarptı ve bezelye döküldü | özür diledi ve taneleri şapkasıyla topladı
@tohum: sakir-0261
Rüzgar hafif hafif esiyordu. Canan, Şakir için ahşap bir masaya bezelye koymuştu. "Bezelye satıyorum, kim alır?" dedi Canan. Şakir hemen masaya koştu. Ama durmadı ve masaya çarptı. Bütün bezelye taneleri otların arasına döküldü. Canan buna çok üzüldü. "Özür dilerim, Canan, çok hızlı koştum," dedi Şakir. Sonra şapkasını çıkarıp ters çevirdi. Taneleri tek tek toplayıp içine koydu. Hepsini masanın üstüne yavaşça boşalttı. "Teşekkürler, Şakir," dedi Canan ve güldü. Sonra Canan ona bir avuç bezelye sattı. İkisi de çok sevindi, çünkü kamp yerindeki oyunları yeniden başlamıştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «"Bezelye satıyorum, kim alır?" dedi Canan.»
   - Açıklama: Sorun ilk üç cümlede söylenmiyor; bezelyeler ancak altıncı cümlede dökülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0261` birebir aynı, ardından `@onarim: abdcd3311dd6b5d5b72f281ca2b6c9ca3003b6e4`, sonra gövde.

### Hikâye 2: tohum sakir-0267 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0267
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kebap', fiil 'yakalamak', sıfat 'heyecanlı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: güneş gözlerine geldiği için fil topu yakalayamadı | şapkasını paylaştı ve filin başına taktı
@tohum: sakir-0267
@degisim: kebap -> top
Ormanda kamp yerinin yanında Şakir ile Necati heyecanlı bir top oyunu oynuyordu. Ama güneş tam Necati'nin gözlerine geliyordu. Bu yüzden Necati gelen topu yakalayamadı. "Güneşten topu hiç göremiyorum," dedi Necati. Şakir biraz düşündü. Sonra geniş şapkasını çıkarıp Necati'nin başına taktı. Artık Necati'nin gözleri gölgede kalıyordu. Şakir topu yavaşça yeniden attı. Necati onu hortumuyla hemen yakaladı. "Oldu, Şakir, şimdi her şeyi görüyorum!" dedi Necati. "Oyun bitene kadar şapkam sende kalsın," dedi Şakir. İkisi de çok sevindi, çünkü oyunları yine eğlenceli olmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkasını paylaştı ve filin"
   - Cümle 0 (plan satırı): «güneş gözlerine geldiği için fil topu yakalayamadı | şapkasını paylaştı ve filin başına taktı»
   - Açıklama: Tek şapkayı arkadaşına vermek 'paylaşmak' değildir; fiil yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0267` birebir aynı, `@degisim: kebap -> top` (tutuyorsan), ardından `@onarim: 45208bc8e3516549a12286716efd4b852cac7d89`, sonra gövde.

### Hikâye 3: tohum sakir-0268 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0268
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'halka', fiil 'kurulamak', sıfat 'simsiyah'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: rüzgar esti ve halka sopası kırıldı | şapkasını yere koyup halkaları ona attı
@tohum: sakir-0268
Bir sabah Şakir parkta halkaları ince bir sopaya atıyordu. Ama rüzgar esti ve sopa ikiye kırıldı. Artık halkaları atacak bir yer yoktu. Şakir başındaki simsiyah uzun şapkaya baktı. Çimler ıslaktı, bu yüzden çantasındaki havluyla küçük bir yeri kuruladı. Sonra şapkasını çıkarıp oraya dik koydu. İlk halka yanına düştü. İkinci halka tam tepesinden geçti ve aşağı indi. Şakir sevinçle zıpladı. Sonra bütün halkaları tek tek attı. Şakir bundan sonra oyunda bir şey bozulunca başka bir hedef buldu.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar esti ve sopa ikiye kırıldı"
   - Cümle 2: «Ama rüzgar esti ve sopa ikiye kırıldı.»
   - Açıklama: Rüzgarın bir sopayı ikiye kırması akla yatkın bir sebep değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "çantasındaki havluyla küçük bir yeri kuruladı"
   - Cümle 5: «Çimler ıslaktı, bu yüzden çantasındaki havluyla küçük bir yeri kuruladı.»
   - Açıklama: Havlu ve ıslak çim sebepsiz beliriyor ve çözüme bir katkısı yok.
   - Açıklama: Islak çim ve havlu sebepsiz beliriyor ve sorunun çözümüne hiçbir katkı yapmıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "İlk halka yanına düştü"
   - Cümle 7: «İlk halka yanına düştü.»
   - Açıklama: 'Yanına' zamirinin neyi (şapkayı) gösterdiği belli değil.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şakir bundan sonra oyunda bir şey bozulunca başka bir hedef buldu"
   - Cümle 11: «Şakir bundan sonra oyunda bir şey bozulunca başka bir hedef buldu.»
   - Açıklama: 'Bundan sonra' ile süregelen bir alışkanlık anlatılıyor ama fiil tek seferlik 'buldu' olmuş; 'bulurdu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0268` birebir aynı, ardından `@onarim: 2a0072c71416d5b4141e0a41b1444f859808e702`, sonra gövde.

### Hikâye 4: tohum sakir-0270 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0270
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'tabak', fiil 'gizlenmek', sıfat 'çamurlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: yağmur başladı ve kurabiyeler ıslanıyordu | şapkasını tabağın üstüne tuttu ve çadıra yürüdü
@tohum: sakir-0270
@degisim: gizlenmek -> ıslanmak
Ormanda kamp yerinde Canan bir tabak kurabiyeyi çadıra götürüyordu. Şakir de onun yanında yürüyordu. Birden ince bir yağmur başladı ve damlalar tabağa düştü. "Kurabiyeler ıslanıyor!" dedi Canan. Şakir hemen geniş şapkasını çıkardı. Onu tabağın üstüne tuttu. Damlalar artık kurabiyelere değil, şapkaya düşüyordu. Yol çamurluydu, bu yüzden ikisi yavaş yavaş yürüdü. Sonunda çadıra vardılar. Canan tabağa baktı ve güldü. "Teşekkürler, Şakir," dedi Canan. İkisi de çok sevindi, çünkü kurabiyeler kuru kalmıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yol çamurluydu, bu yüzden ikisi yavaş yavaş yürüdü"
   - Cümle 8: «Yol çamurluydu, bu yüzden ikisi yavaş yavaş yürüdü.»
   - Açıklama: Çamurlu yol kuruluyor ama olaya hiçbir etkisi olmuyor, işlevsiz bir ayrıntı.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Yol çamurluydu, bu yüzden"
   - Cümle 8: «Yol çamurluydu, bu yüzden ikisi yavaş yavaş yürüdü.»
   - Açıklama: Çamurlu yol bir engel gibi kuruluyor ama olayda hiçbir sonucu olmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0270` birebir aynı, `@degisim: gizlenmek -> ıslanmak` (tutuyorsan), ardından `@onarim: 17e44bba4db9de25f93b607611358937bc92b484`, sonra gövde.

### Hikâye 5: tohum sakir-0271 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0271
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'blok', fiil 'korunmak', sıfat 'zeki'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: rüzgar kumu kaldırıp sandviçin üstüne getirdi | şapkasıyla kumdan bloklar yapıp duvar kurdu
@tohum: sakir-0271
Rüzgar esiyordu. Şakir ile Kadriye kumsalda oturmuş, sandviç yiyordu. Ama rüzgar kumu kaldırıp Kadriye'nin sandviçine getirdi. "Sandviçimde kum var," dedi Kadriye. Şakir biraz düşündü. Sonra şapkasını ıslak kumla doldurup yere ters çevirdi. Yerde kumdan küçük bir blok kaldı. Şakir böyle beş blok daha yaptı ve annesinin önüne dizdi. Bloklar küçük bir duvar oldu. Artık sandviçler rüzgardan korunuyordu. Kadriye yemeğini rahatça bitirdi ve Şakir'e sarıldı. "Çok zeki bir fikir, teşekkürler, Şakir!" dedi Kadriye.
```

**Hakem bulguları (6):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "annesinin önüne dizdi"
   - Cümle 8: «Şakir böyle beş blok daha yaptı ve annesinin önüne dizdi.»
   - Açıklama: Kadriye adıyla tanıtılan kişi birden 'annesi' diye anılıyor ve kimi gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ve annesinin önüne dizdi"
   - Cümle 8: «Şakir böyle beş blok daha yaptı ve annesinin önüne dizdi.»
   - Açıklama: 'Annesi' kimi gösteriyor belli değil; Kadriye'nin anne olduğu söylenmedi.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şakir böyle beş blok daha yaptı"
   - Cümle 8: «Şakir böyle beş blok daha yaptı ve annesinin önüne dizdi.»
   - Açıklama: Çözüm çok sayıda tekrarlanan adım sürüyor ve zaten kumlanmış sandviçi düzeltmiyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "annesinin önüne dizdi"
   - Cümle 8: «Şakir böyle beş blok daha yaptı ve annesinin önüne dizdi.»
   - Açıklama: Anne sebepsiz beliriyor; Kadriye'nin anne olduğu hiç söylenmediği için blokların kimin önüne dizildiği belirsiz.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Kadriye yemeğini rahatça bitirdi"
   - Cümle 11: «Kadriye yemeğini rahatça bitirdi ve Şakir'e sarıldı.»
   - Açıklama: Sandviçine kum girmiş olmasına rağmen Kadriye aynı yemeği rahatça bitiriyor; kumlu sandviç hiç çözülmüyor.
6. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çok zeki bir fikir"
   - Cümle 12: «"Çok zeki bir fikir, teşekkürler, Şakir!" dedi Kadriye.»
   - Açıklama: Fikir zeki olmaz; 'akıllıca bir fikir' olmalı.
   - Açıklama: 'Zeki' insan için kullanılır, fikir için 'akıllıca' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0271` birebir aynı, ardından `@onarim: 25806aaf6ef4d9404b2c2e5f3b868654ff6040c9`, sonra gövde.

### Hikâye 6: tohum sakir-0272 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0272
- yer: park (Şehirdeki park.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'inci', fiil 'katmak', sıfat 'kırılgan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: inciler çimenlere döküldü ve patileri onları tutamadı | filden yardım istedi ve incileri şapkasına topladı
@tohum: sakir-0272
Şakir parkta bir bankta oturmuş, inci bir kolye yapıyordu. Necati de bankın öbür ucunda oturuyordu. Ama rüzgar esti, kutu devrildi ve kırılgan inciler çimenlere döküldü. Şakir'in patileri bu minik incileri tutmak için çok büyüktü. Onları ezmek de istemedi. "Necati, incileri toplar mısın?" diye sordu Şakir. Necati hortumuyla onları tek tek kaldırdı. Şakir de şapkasını ters tuttu ve Necati hepsini içine bıraktı. Hiçbiri yeniden kaybolmadı. Sonra Şakir incileri ipe yavaş yavaş kattı. Kolye çok güzel oldu. "Teşekkürler, Necati, sen olmasan bunu bitiremezdim!" dedi Şakir.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "oturmuş, inci bir kolye"
   - Cümle 1: «Şakir parkta bir bankta oturmuş, inci bir kolye yapıyordu.»
   - Açıklama: 'inci bir kolye' yanlış kuruluş; 'inci bir kolye' yerine 'incili bir kolye' ya da 'bir inci kolye' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve kırılgan inciler çimenlere"
   - Cümle 3: «Ama rüzgar esti, kutu devrildi ve kırılgan inciler çimenlere döküldü.»
   - Açıklama: 'kırılgan' 3 yaşındaki çocuğa uygun olmayan soyut bir kelime ve incilere de uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kırılgan inciler çimenlere döküldü"
   - Cümle 3: «Ama rüzgar esti, kutu devrildi ve kırılgan inciler çimenlere döküldü.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "incileri ipe yavaş yavaş kattı"
   - Cümle 10: «Sonra Şakir incileri ipe yavaş yavaş kattı.»
   - Açıklama: İnciler ipe katılmaz, dizilir; fiil yanlış anlamda.
   - Açıklama: İnciler ipe 'katılmaz', ipe dizilir ya da geçirilir; fiil yanlış anlamda.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra Şakir incileri ipe yavaş yavaş kattı"
   - Cümle 10: «Sonra Şakir incileri ipe yavaş yavaş kattı.»
   - Açıklama: Patileri minik incileri tutamayacak kadar büyük denmişken Şakir incileri tek tek ipe dizebiliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0272` birebir aynı, ardından `@onarim: c3e3a2e88382de0032387f539fc1a2055cd03e75`, sonra gövde.

### Hikâye 7: tohum sakir-0273 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0273
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: bir şey yapmak
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'güneş', fiil 'binmek', sıfat 'sıcacık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: karton kutudan araba yapmak istedi ama direksiyon yoktu | şapkasını direksiyon gibi tuttu ve arabaya bindi
@tohum: sakir-0273
Güneş parlıyordu. Şakir kamp yerinde boş ve büyük bir karton kutu buldu. Ondan bir araba yapmak istedi ama arabanın direksiyonu yoktu. Şakir kutuya baktı ve biraz düşündü. Sonra yuvarlak şapkasını çıkardı. Onu iki eliyle direksiyon gibi tuttu. Şakir kutunun içine oturdu ve arabasına bindi. Hava sıcacıktı ve ağaçların arasında hafif bir rüzgar esiyordu. Şakir şapkayı sağa sola çevirdi. Ağzıyla araba sesi çıkardı. Şakir karton arabasıyla kamp yerinde mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hava sıcacıktı ve ağaçların arasında hafif bir rüzgar esiyordu"
   - Cümle 8: «Hava sıcacıktı ve ağaçların arasında hafif bir rüzgar esiyordu.»
   - Açıklama: Çözümden sonra araya giren hava betimi olaya hiçbir şey katmıyor.
   - Açıklama: Olayın ortasına işlevsiz ikinci bir hava betimi giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0273` birebir aynı, ardından `@onarim: 11ca2687d3844f07c0303cba96fdee12404d0ff3`, sonra gövde.

### Hikâye 8: tohum sakir-0274 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0274
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'nilüfer', fiil 'şakalaşmak', sıfat 'benekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: benekli kabuklar kumun içine karışmıştı | şapkasıyla kumu salladı ve kabukları ayırdı
@tohum: sakir-0274
@degisim: şakalaşmak -> sallamak
Dalgaların sesi geliyordu. Şakir benekli kabuklar gördü ve onlarla nilüfer çiçeği yapmak istedi. Ama kabuklar kumun içine karışmıştı ve patileriyle onları tutamadı. Şakir hasır şapkasını çıkardı. Onunla bir avuç kum aldı ve yavaşça salladı. Kum deliklerden aşağı aktı. Kabuklar ise içeride kaldı. Şakir onları yere tek tek koydu. Ortaya bir daire, etrafına da çiçek yaprakları yaptı. Sonunda güzel bir nilüfer çiçeği oldu. Şakir çiçeğinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir benekli kabuklar gördü"
   - Cümle 2: «Şakir benekli kabuklar gördü ve onlarla nilüfer çiçeği yapmak istedi.»
   - Açıklama: Güvenli kullanım satırına göre Şakir tek başına uzağa gitmez; deniz kıyısında yetişkinsiz yalnız.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "patileriyle onları tutamadı"
   - Cümle 3: «Ama kabuklar kumun içine karışmıştı ve patileriyle onları tutamadı.»
   - Açıklama: Cümlenin öznesi kabuklar iken fiil Şakir'e ait; özne uyumu bozuk.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Onunla bir avuç kum aldı"
   - Cümle 5: «Onunla bir avuç kum aldı ve yavaşça salladı.»
   - Açıklama: Şapkayla alınan kum 'avuç' olmaz; kelime yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0274` birebir aynı, `@degisim: şakalaşmak -> sallamak` (tutuyorsan), ardından `@onarim: ad5b8c86eddf140becbe7782cde72714b62c5d94`, sonra gövde.

### Hikâye 9: tohum sakir-0275 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0275
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'salatalık', fiil 'kaldırmak', sıfat 'şapkalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: salatalık suyun kenarına yuvarlandı ve dalga onu itti | şapkasıyla salatalığı sudan aldı ve kaldırdı
@tohum: sakir-0275
@degisim: şapkalı -> yeşil
Deniz kıyısında Şakir ile Canan yeşil salatalık yiyecekti. Canan çok acıkmıştı. Ama salatalık Canan'ın elinden kaydı ve suyun kenarına yuvarlandı. Küçük bir dalga geldi ve onu biraz uzağa itti. "Salatalığım gidiyor!" dedi Canan. Şakir suyun kenarında durdu ve şapkasını çıkardı. Şapkayı sığ suya soktu ve salatalığı içine aldı. Sonra onu yukarı kaldırdı, su deliklerden aktı. Şakir salatalığı Canan'a verdi. "Teşekkürler, Şakir," dedi Canan. İkisi kumda oturup salatalığı mutlu mutlu paylaştı.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şapkayı sığ suya soktu"
   - Cümle 7: «Şapkayı sığ suya soktu ve salatalığı içine aldı.»
   - Açıklama: Dalganın ittiği bir eşyanın peşinden suya uzanmak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Dalganın uzağa ittiği bir eşyayı sudan almaya uzanmak çocuğun taklit edebileceği riskli bir davranış.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Sonra onu yukarı kaldırdı"
   - Cümle 8: «Sonra onu yukarı kaldırdı, su deliklerden aktı.»
   - Açıklama: 'Onu' şapkayı mı salatalığı mı gösteriyor belli değil.
   - Açıklama: 'Onu' zamirinin şapkayı mı salatalığı mı gösterdiği belli değil ve 'delikler' daha önce tanıtılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0275` birebir aynı, `@degisim: şapkalı -> yeşil` (tutuyorsan), ardından `@onarim: 1fdf9caf3278da760efa8a5545c4400fba3054af`, sonra gövde.

### Hikâye 10: tohum sakir-0278 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0278
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'direk', fiil 'süslenmek', sıfat 'nazik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: rüzgar gemideki kağıt bayrağı uçurdu | şapkasını direğin tepesine bayrak olarak taktı
@tohum: sakir-0278
Şakir ile Necati kumsalda kumdan büyük bir gemi yapmıştı. Geminin ortasında uzun bir sopa direk olarak duruyordu. Ama rüzgar esti ve direğin ucundaki kağıt bayrak uçup gitti. "Bayrağımız gitti, şimdi ne yapacağız?" diye sordu Necati. Şakir şapkasını çıkardı. Onu direğin tepesine sıkıca taktı. Şapka rüzgarda sallandı ama düşmedi. "Harika bir bayrak oldu, Şakir," dedi Necati nazik bir sesle. Sonra Necati hortumuyla kabuklar topladı. Gemi bu kabuklarla güzelce süslendi. Şakir ile Necati gemide mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra Necati hortumuyla kabuklar topladı"
   - Cümle 9: «Sonra Necati hortumuyla kabuklar topladı.»
   - Açıklama: Kabuk toplama çözümden sonra sebepsiz eklenen ve sorunla ilgisi olmayan işlevsiz bir olay.
   - Açıklama: Sorun çözüldükten sonra kabuk toplama ve gemiyi süsleme olayı sorunla ilgisiz, işlevsiz bir ek olay olarak geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0278` birebir aynı, ardından `@onarim: 0609bde56affc01c881b674d32b43adc3be95e93`, sonra gövde.

### Hikâye 11: tohum sakir-0282 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0282
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'çekirdek', fiil 'keşfetmek', sıfat 'soslu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: oyuncak fırının kapağı sıkıştı ve açılmadı | şapkasını pizzanın üstüne kapatıp fırın yaptı
@tohum: sakir-0282
@degisim: keşfetmek -> bulmak
Şakir evde hamurla soslu bir oyun pizzası yapıyordu. Mutfakta bulduğu çekirdekleri pizzanın üstüne dizdi. Ama oyuncak fırının kapağı sıkıştı ve açılmadı. Şakir kapağı iki kez çekti, yine olmadı. Sonra büyük beyaz şapkasını çıkardı. Onu pizzanın üstüne ters kapattı. Bu, Şakir'in yeni fırını oldu. Şakir yavaşça bir, iki, üç diye saydı. Sonra şapkayı kaldırdı ve pizzayı bir tabağa koydu. Oyunda pizza artık pişmişti. Şakir çok sevindi, çünkü oyun pizzasını yine de pişirmişti.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "hamurla soslu bir oyun pizzası"
   - Cümle 1: «Şakir evde hamurla soslu bir oyun pizzası yapıyordu.»
   - Açıklama: 'Hamurla soslu' bağlaması dilbilgisel değil; 'hamurdan ve sostan' gibi olmalı.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "hamurla soslu bir oyun"
   - Cümle 1: «Şakir evde hamurla soslu bir oyun pizzası yapıyordu.»
   - Açıklama: 'Hamurla soslu' bağlaması bozuk; 'hamurdan ve sostan' gibi olmalı.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "fırının kapağı sıkıştı ve açılmadı"
   - Cümle 3: «Ama oyuncak fırının kapağı sıkıştı ve açılmadı.»
   - Açıklama: Kapağın neden sıkıştığı söylenmiyor.
   - Açıklama: Kapağın neden sıkıştığı hiç söylenmiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Onu pizzanın üstüne ters kapattı"
   - Cümle 6: «Onu pizzanın üstüne ters kapattı.»
   - Açıklama: Çözüm sıkışan kapağa yönelmiyor, şapkayla oyunda yeni bir fırın uyduruluyor.
   - Açıklama: Çözüm sıkışan kapağa yönelmiyor, fırını tamamen bir kenara bırakıp şapkayla dolanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0282` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 5ce9fbd70c486cef13b982308d6a5e9fcbbee1e3`, sonra gövde.

### Hikâye 12: tohum sakir-0284 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0284
- yer: park (Şehirdeki park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'tekne', fiil 'vermek', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: havuzdan garip bir tık tık sesi geldi | şapkasıyla gölge yaptı ve sesi yapan kabuğu gördü
@tohum: sakir-0284
Rüzgar esiyordu. Şakir parktaki havuzun yanından geçerken tık tık diye bir ses duydu. Ses suyun ortasından geliyordu. Şakir bu sesi çok merak etti. Ama güneş suda çok parlıyordu ve iyi göremedi. Hemen şapkasını gözlerinin üstüne indirdi. Şapka ona serin bir gölge verdi. Şimdi suyun ortasını iyice gördü. Orada küçük bir ağaç kabuğu yüzüyordu. Kabuk yamuk bir tekne gibi sallanıyordu. Rüzgar kabuğu itiyordu ve kabuk bir taşa vuruyordu. Sesi bu kabuk yapıyordu. Şakir her tık sesini tek tek saydı ve güldü. Şakir çok sevindi, çünkü tık tık sesini yapan kabuğu bulmuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "güneş suda çok parlıyordu ve iyi göremedi"
   - Cümle 5: «Ama güneş suda çok parlıyordu ve iyi göremedi.»
   - Açıklama: Bağlı cümlede özne güneşten Şakir'e habersiz kayıyor; 'göremedi' güneşe bağlanıyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "suda çok parlıyordu ve iyi göremedi"
   - Cümle 5: «Ama güneş suda çok parlıyordu ve iyi göremedi.»
   - Açıklama: Bağlı cümlelerde özne güneşten Şakir'e habersiz kayıyor; 'göremedi' güneşe bağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0284` birebir aynı, ardından `@onarim: ed67d389fca7896bc10771c51a4f3442a71282d3`, sonra gövde.
