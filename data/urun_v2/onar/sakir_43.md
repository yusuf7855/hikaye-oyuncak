# Editör görevi (onarım): Şakir, onarım partisi 43

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar43.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar43.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0193 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0193
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: kaybolan eşya
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'takvim', fiil 'taşmak', sıfat 'uzun'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: mavi bilye uzun otların arasında kayboldu | şapkasıyla kuru yaprakları havaya uçurdu
@tohum: sakir-0193
@degisim: takvim -> bilye
Bir sabah Şakir kamp yerinde bilye oynuyordu. Küçük kutusu çok doluydu ve bilyeler kutudan taştı. Birden mavi bir bilye yere düştü ve uzun otların arasına yuvarlandı. Otların dibi kuru yapraklarla doluydu ve Şakir bilyeyi göremedi. Şakir şapkasını yaprakların üstünde hızlı hızlı salladı. Yapraklar havaya uçtu ve bir yana gitti. Yaprakların altında mavi bir şey parladı. Bu kayıp bilyeydi! Şakir bu bilyeyi ve kutudan iki bilye daha alıp cebine koydu. Artık kutu çok dolu değildi. Şakir oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Küçük kutusu çok doluydu ve bilyeler kutudan taştı"
   - Cümle 2: «Küçük kutusu çok doluydu ve bilyeler kutudan taştı.»
   - Açıklama: Kayıp bilyenin yanında taşan kutu ikinci bir sorun olarak kurulup ayrıca çözülüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0193` birebir aynı, `@degisim: takvim -> bilye` (tutuyorsan), ardından `@onarim: 888b2a21c265867e0e9a15159d5b2b4c159d3c00`, sonra gövde.

### Hikâye 2: tohum sakir-0194 (deneme 2 -> 3)

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
@plan: fil gerinince kitap sisin içinde kayboldu | kitabı dalda bulup şapkasını atarak düşürdü
@tohum: sakir-0194
Şakir sisli bir sabah Necati ile parktaydı. Necati bankta oturmuş, hortumuyla bir kitap tutuyordu. Birden Necati gerindi. Kitap hortumundan fırladı ve sisin içinde kayboldu. "Kitabım nereye gitti?" diye sordu Necati. Şakir etrafa dikkatle baktı. Yakındaki ağacın dalında beyaz bir şey gördü. Bu, Necati'nin kitabıydı. Dal çok yüksekti ve Necati bile ona yetişemedi. Şakir şapkasını kitaba doğru attı. Kitap ve şapka daldan kaydı ve aşağı düştü. Necati kitabı hortumuyla havada yakaladı. "Teşekkürler, Şakir, sen olmasan kitabı bulamazdım!" dedi Necati. Şakir ile Necati banka oturdu ve kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Kitap hortumundan fırladı ve sisin içinde kayboldu.»
   - Açıklama: Kitabın kaybolduğu sorun ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0194` birebir aynı, ardından `@onarim: 30c83c12805d23aca1a50a2c2ac197b766d4303c`, sonra gövde.

### Hikâye 3: tohum sakir-0203 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0203
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'maske', fiil 'düzenlemek', sıfat 'yepyeni'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: çadırın içinden bir tık tık sesi geldi | şapkasına damla düşünce deliği buldu ve altına kap koydu
@tohum: sakir-0203
Yağmur yeni dinmişti. Şakir çadırın içinde eşyalarını düzenliyordu. Birden bir tık tık sesi duydu ve bu sesi çok merak etti. Ses çadırın ortasından geliyordu ama orada yalnız yepyeni maskesi vardı. Şakir maskeye doğru eğildi. O anda şapkasının üstüne bir damla düştü ve tık diye ses çıktı. Şakir hemen yukarı baktı. Çadırın tepesinde küçük bir delik vardı. Yağmur suyu oradan maskenin üstüne damlıyordu. Ses bu sudan geliyordu! Şakir maskesini alıp kuru bir köşeye koydu. Sonra deliğin altına boş bir kap bıraktı. Şakir bundan sonra çadırda bir ses duyunca önce tepeye baktı.
```

**Hakem bulguları (1):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "orada yalnız yepyeni maskesi"
   - Cümle 4: «Ses çadırın ortasından geliyordu ama orada yalnız yepyeni maskesi vardı.»
   - Açıklama: Kartta Şakir'e ait bir maske eşyası yok; kapalı dünyaya dışarıdan bir nesne ekleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0203` birebir aynı, ardından `@onarim: 318cbff2c373fa9596d25f2a71273603ae279294`, sonra gövde.

### Hikâye 4: tohum sakir-0206 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0206
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'limon', fiil 'uzamak', sıfat 'memnun'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: küçük limon her seferinde elinden kayıp düştü | şapkasını ters çevirdi ve limonu içine aldı
@tohum: sakir-0206
@degisim: memnun -> mutlu
Parkta Şakir ile annesi Kadriye top yerine limonla oynuyordu. Kadriye limonu atıyor, Şakir tutmaya çalışıyordu. Ama limon çok küçüktü ve Şakir'in elinden hep kayıp düşüyordu. Limon çimenlerin üstünde uzağa yuvarlandı. Şakir her seferinde limonun peşinden koştu. Sonra şapkasını çıkardı ve ters çevirip önünde tuttu. Kadriye limonu yine attı. Limon bu kez tam şapkanın içine düştü ve orada kaldı. Kadriye çok mutlu oldu ve alkışladı. Oyun uzadıkça ikisi de daha çok güldü. Şakir bundan sonra küçük bir şeyi tutarken bir kap kullandı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "top yerine limonla oynuyordu"
   - Cümle 1: «Parkta Şakir ile annesi Kadriye top yerine limonla oynuyordu.»
   - Açıklama: Top yerine küçük bir limonla oynamak sebepsiz ve saçma bir kurgu; sorun bu tuhaf seçimden doğuyor.
   - Açıklama: Top yerine limonla oynamanın sebebi yok ve sorun bu yapay seçimden doğuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0206` birebir aynı, `@degisim: memnun -> mutlu` (tutuyorsan), ardından `@onarim: a749810dcf10267ea0615be227c5537d8e8c6953`, sonra gövde.

### Hikâye 5: tohum sakir-0207 (deneme 2 -> 3)

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
@plan: aç sincaplar büyük filden dolayı kovaya yaklaşamadı | şapkaya fındık koyup ağacın dibine bıraktı
@tohum: sakir-0207
Şakir, Necati ile ormandaki kamp yerinde oturuyordu. Necati'nin önünde karışık fındıklarla dolu bir kova vardı. Ağaçtan aç sincaplar indi, ama Necati'yi görünce kovaya yaklaşamadılar. Sincaplar fındıklara uzaktan bakıyordu. "Onlara nasıl yardım ederiz?" diye sordu Necati. Şakir şapkasını çıkardı ve içine bir avuç fındık koydu. Şapkayı ağacın dibine bıraktı ve Necati ile biraz geri çekildi. Sincaplar önce durdu ve kulaklarını oynattı. Sonra yavaş yavaş onlara alıştılar ve şapkaya geldiler. Fındıkları tek tek yediler. "Bak, Necati, sincapların karnı doydu!" dedi Şakir. Sonra Şakir ile Necati kalan fındıkları mutlu mutlu yedi.
```

**Hakem bulguları (5):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "aç sincaplar büyük filden dolayı kovaya yaklaşamadı"
   - Cümle 0 (plan satırı): «aç sincaplar büyük filden dolayı kovaya yaklaşamadı | şapkaya fındık koyup ağacın dibine bıraktı»
   - Açıklama: Gövdede hiç fil geçmiyor; sincaplar Necati'yi görünce kovaya yaklaşamıyor.
   - Açıklama: Gövdede fil yok; sincaplar Necati'yi görünce kovaya yaklaşamıyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "içine bir avuç fındık koydu"
   - Cümle 6: «Şakir şapkasını çıkardı ve içine bir avuç fındık koydu.»
   - Açıklama: Yabani hayvanları elle beslemek çocuğun taklit edebileceği riskli bir davranış.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yavaş yavaş onlara alıştılar"
   - Cümle 9: «Sonra yavaş yavaş onlara alıştılar ve şapkaya geldiler.»
   - Açıklama: 'Onlara' zamirinin Şakir ile Necati'yi mi gösterdiği belli değil; son anılan şapka ve sincaplar.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "onlara alıştılar ve şapkaya geldiler"
   - Cümle 9: «Sonra yavaş yavaş onlara alıştılar ve şapkaya geldiler.»
   - Açıklama: Arka plandaki çoğul sincaplar olaya katılıyor.
5. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "alıştılar ve şapkaya geldiler"
   - Cümle 9: «Sonra yavaş yavaş onlara alıştılar ve şapkaya geldiler.»
   - Açıklama: Arka planda kalması gereken çoğul canlı sincaplar olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0207` birebir aynı, ardından `@onarim: 158145ac277b1722dad1806b4d680847e1d1b0c0`, sonra gövde.

### Hikâye 6: tohum sakir-0209 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0209
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ayakkabı', fiil 'uçuşmak', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: baloncuklar rüzgarda hemen patladı | şapkasını rüzgara karşı tuttu ve yavaşça üfledi
@tohum: sakir-0209
@degisim: narin -> büyük
Rüzgar esiyordu. Şakir kumsalda ilk kez sabunlu su ve çubukla baloncuk yapmayı denedi. Ama baloncuklar rüzgarda hemen patladı. Şakir tekrar üfledi ama yine büyük bir baloncuk olmadı. Sonra biraz düşündü. Şakir şapkasını çıkardı ve rüzgarın geldiği yöne doğru tuttu. Şapkanın arkasında hava sakindi. Şakir çubuğa yavaşça üfledi. Büyük ve parlak bir baloncuk oldu. Arkasından küçük baloncuklar da havada uçuştu. Bir tanesi Şakir'in ayakkabısının üstüne kondu. Şakir çok sevindi, çünkü büyük bir baloncuk yapmayı sonunda başarmıştı.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir kumsalda ilk kez sabunlu su"
   - Cümle 2: «Şakir kumsalda ilk kez sabunlu su ve çubukla baloncuk yapmayı denedi.»
   - Açıklama: Güvenli kullanım satırına göre Şakir tek başına uzağa gitmez; kumsalda yetişkinsiz yalnız.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bir tanesi Şakir'in ayakkabısının üstüne kondu"
   - Cümle 11: «Bir tanesi Şakir'in ayakkabısının üstüne kondu.»
   - Açıklama: Baloncuğun ayakkabıya konması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0209` birebir aynı, `@degisim: narin -> büyük` (tutuyorsan), ardından `@onarim: dbd77029d469c7f47f0fc7d26fb9f44e05c25d7a`, sonra gövde.

### Hikâye 7: tohum sakir-0212 (deneme 2 -> 3)

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
@plan: kız kardeşi de atlamak istedi ama tek halat vardı | şapkayı kardeşine verdi ve sırayla atladılar
@tohum: sakir-0212
@degisim: sağlıklı -> uzun
Şakir kamp yerinde uzun bir halatı çevirip üstünden atlıyordu. Güneş yeni doğmuştu ve hava serindi. Kardeşi Canan da atlamak istedi, ama orada tek bir halat vardı. "Ben de atlayabilir miyim, Şakir?" diye sordu Canan. Şakir durdu ve biraz düşündü. Sonra şapkasını Canan'ın başına koydu ve halatı ona verdi. "Önce sen atla, sonra şapkayı bana ver," dedi Şakir. Canan on kez atladı, sonra şapkayı ve halatı Şakir'e geri verdi. Bu kez Şakir atladı. Şakir ile Canan sırayla atlayıp mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Şakir kamp yerinde uzun"
   - Cümle 1: «Şakir kamp yerinde uzun bir halatı çevirip üstünden atlıyordu.»
   - Açıklama: Başlıktaki yer orman ama hikaye yalnız bir kamp yerinde geçiyor ve ormandan söz edilmiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "şapkasını Canan'ın başına koydu"
   - Cümle 6: «Sonra şapkasını Canan'ın başına koydu ve halatı ona verdi.»
   - Açıklama: Şapkanın halatı paylaşma sorununda hiçbir işlevi yok; çözüme sebepsizce giriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0212` birebir aynı, `@degisim: sağlıklı -> uzun` (tutuyorsan), ardından `@onarim: c665cda6fa7759c84ed0636a543eab86435a6a0d`, sonra gövde.

### Hikâye 8: tohum sakir-0223 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0223
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'vanilya', fiil 'sergilemek', sıfat 'saygılı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: kütük yamuk olduğu için kozalaklar yere yuvarlandı | şapkasını ters koyup kozalakları içine dizdi
@tohum: sakir-0223
@degisim: sergilemek -> dizmek
Ormandaki kamp yerinde Şakir pasta dükkanı oyunu oynuyordu. Kozalak pastalarını bir kütüğün üstüne diziyordu. Ama kütük yamuktu ve kozalaklar birer birer yere yuvarlandı. Şakir güldü ve onları tek tek topladı. Sonra şapkasını çıkardı ve kütüğün üstüne ters koydu. Kozalakları şapkanın içine dikkatle yerleştirdi. Bu kez hiçbir kozalak yere düşmedi. Şakir en büyük kozalağa vanilya pastası adını verdi. Onu şapkanın tam ortasına koydu. Saygılı bir şekilde pastaların önünde eğildi. Şakir pasta dükkanı oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Saygılı bir şekilde pastaların önünde"
   - Cümle 10: «Saygılı bir şekilde pastaların önünde eğildi.»
   - Açıklama: 'Saygılı' kelimesi kozalak pastalara yönelik kullanılınca anlamca uygunsuz kalıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Saygılı bir şekilde pastaların önünde eğildi"
   - Cümle 10: «Saygılı bir şekilde pastaların önünde eğildi.»
   - Açıklama: 'Saygılı' kelimesi kozalak pastalara karşı eğilmekte yanlış kullanılmış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Saygılı bir şekilde pastaların önünde eğildi"
   - Cümle 10: «Saygılı bir şekilde pastaların önünde eğildi.»
   - Açıklama: Pastaların önünde eğilmek sebepsiz ve olayda hiçbir işe yaramayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0223` birebir aynı, `@degisim: sergilemek -> dizmek` (tutuyorsan), ardından `@onarim: 918de88d6582c8134a58da4e8bb6c9cdec68bea7`, sonra gövde.

### Hikâye 9: tohum sakir-0229 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0229
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kese', fiil 'belirmek', sıfat 'mükemmel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: rüzgar numara örtüsünü uçurdu | keseyi şapkasının altına koyup yeniden gösterdi
@tohum: sakir-0229
Ormanda serin bir rüzgar esiyordu. Şakir, Fil Necati'ye bir kese numarası yapacaktı. Ama rüzgar numara örtüsünü uçurdu ve ağaçların arasına götürdü. "Örtü olmadan numara nasıl olacak?" diye sordu Necati. Şakir hemen şapkasını çıkardı. Küçük keseyi yere koydu ve üstünü şapkayla örttü. "Kese yok oldu!" dedi Şakir. Necati hortumunu kaldırdı ve şaşırmış gibi yaptı. "Kese nereye gitti?" diye sordu Necati. Şakir şapkayı yavaşça kaldırdı ve kese yeniden belirdi. Şakir şapkasını başına taktı ve eğilerek selam verdi. "Mükemmel bir numara, Şakir!" dedi Necati.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kese numarası yapacaktı"
   - Cümle 2: «Şakir, Fil Necati'ye bir kese numarası yapacaktı.»
   - Açıklama: 'Kese numarası' ve sihirbazlık anlamındaki 'numara' küçük çocuğun bilmeyeceği kelimeler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0229` birebir aynı, ardından `@onarim: 042fedf12174e214aa01eb76438ebb828b637e17`, sonra gövde.

### Hikâye 10: tohum sakir-0233 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0233
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kabak', fiil 'inmek', sıfat 'değerli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: çorba için boş tencere yoktu | şapkasını tencere gibi kullanıp oyun çorbası yaptı
@tohum: sakir-0233
@degisim: değerli -> küçük
Ormandaki kamp yerinde Şakir yemek oyunu oynuyordu. Annesi Kadriye'ye küçük bir kabakla oyun çorbası yapacaktı. Ama tencerede annesinin gerçek çorbası vardı. Şakir oturduğu kütükten indi ve biraz düşündü. Sonra şapkasını çıkarıp ters çevirdi. "Anne, şapkam tencere olsun!" dedi Şakir. Kabağı ve birkaç yaprağı şapkanın içine koydu. Bir dalla hepsini yavaşça karıştırdı. "Kabak çorbası hazır, anneciğim!" dedi Şakir. Kadriye çorbayı içer gibi yaptı ve güldü. "Çok güzel olmuş, Şakir," dedi Kadriye. Şakir ile annesi yemek oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Annesi Kadriye'ye küçük bir kabakla"
   - Cümle 2: «Annesi Kadriye'ye küçük bir kabakla oyun çorbası yapacaktı.»
   - Açıklama: Yapı belirsiz; 'annesi' özne gibi okunuyor, 'Annesi Kadriye için' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0233` birebir aynı, `@degisim: değerli -> küçük` (tutuyorsan), ardından `@onarim: 92ef9a521d2b990eef6d3b20a2288407127c3327`, sonra gövde.

### Hikâye 11: tohum sakir-0235 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0235
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'teker', fiil 'kurtarmak', sıfat 'elmalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: arabanın tekeri yumuşak kuma battı ve araba durdu | şapkasıyla kumu kazıdı ve arabayı kurtardı
@tohum: sakir-0235
@degisim: elmalı -> yumuşak
Bir sabah Şakir kumsalda ilk kez el arabası itiyordu. Arabayla Necati'nin kalesine kum taşıyordu. Ama arabanın tekeri yumuşak kuma battı ve araba durdu. Şakir arabayı itti, ama araba gitmedi. Sonra şapkasını çıkardı. Şapkayla tekerleğin önündeki kumu kazıdı. "Tekeri kurtaracağım, Necati!" dedi Şakir. Necati de hortumuyla arabayı yavaşça çekti. Teker kurtuldu ve araba yeniden ilerledi. Şakir şapkasındaki kumu döktü ve başına taktı. Sonra arabayı kaleye kadar götürdü. Şakir ile Necati kaleyi mutlu mutlu yapmaya devam etti.
```

**Hakem bulguları (1):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Necati de hortumuyla arabayı yavaşça çekti"
   - Cümle 8: «Necati de hortumuyla arabayı yavaşça çekti.»
   - Açıklama: Arabayı kurtaran çekişi yan karakter yapıyor, çözüm Şakir'e tam ait değil.
   - Açıklama: Arabayı kurtaran çekişi yan karakter Necati yapıyor; çözüm figürle paylaşılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0235` birebir aynı, `@degisim: elmalı -> yumuşak` (tutuyorsan), ardından `@onarim: 7e823a720ac53c5c1cfd4f862c829f3dc7518aaf`, sonra gövde.

### Hikâye 12: tohum sakir-0236 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0236
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'çit', fiil 'yetişmek', sıfat 'düzgün'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: küçük yengeçlerin önünü çit kapattı | yengeçleri şapkayla alıp çitin öbür yanına taşıdı
@tohum: sakir-0236
Kumsalda hafif bir rüzgar esiyordu. Şakir ile annesi Kadriye kumda yürürken küçük yengeçler gördüler. Yengeçler denize gitmek istiyordu, ama önlerinde düzgün bir çit vardı. Çitin tahtaları kuma kadar iniyordu ve yengeçler altından geçemedi. "Anne, yengeçler denize dönemiyor!" dedi Şakir. "Onlara elimizle dokunmayalım, çok küçükler," dedi Kadriye. Şakir şapkasını çıkardı ve yengeçlerin önüne koydu. Yengeçler yan yan yürüdü ve şapkanın içine girdi. Şakir şapkayı dikkatle kaldırdı ve çitin öbür yanına taşıdı. Suyun kenarında yengeçleri yavaşça kuma bıraktı. Küçük yengeçler hemen ilk dalgaya yetişti. Sonra Şakir ile annesi kumsalda mutlu mutlu yürümeye devam etti.
```

**Hakem bulguları (3):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Yengeçler yan yan yürüdü ve şapkanın içine girdi"
   - Cümle 8: «Yengeçler yan yan yürüdü ve şapkanın içine girdi.»
   - Açıklama: Arka planda kalması gereken çoğul canlı yengeçler olayın merkezine katılıyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Yengeçler yan yan yürüdü"
   - Cümle 8: «Yengeçler yan yan yürüdü ve şapkanın içine girdi.»
   - Açıklama: Arka planda kalması gereken çoğul canlı yengeçler olaya katılıyor.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir şapkayı dikkatle kaldırdı"
   - Cümle 9: «Şakir şapkayı dikkatle kaldırdı ve çitin öbür yanına taşıdı.»
   - Açıklama: Yabani yengeçleri toplayıp taşımak çocuğun taklit edebileceği riskli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0236` birebir aynı, ardından `@onarim: 7ea50457f2074b9bb7ee587d06ebc5274b9b2671`, sonra gövde.
