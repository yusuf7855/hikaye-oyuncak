# Editör görevi (onarım): Şakir, onarım partisi 48

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar48.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar48.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0212 (deneme 3 -> 4)

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
@plan: kız kardeşi de atlamak istedi ama tek halat vardı | halatı kardeşine verdi ve sırayla atladılar
@tohum: sakir-0212
@degisim: sağlıklı -> uzun
Şakir ormandaki kamp yerinde uzun bir halatı çevirip üstünden atlıyordu. Güneş yeni doğmuştu ve çok parlaktı. Kardeşi Canan da atlamak istedi, ama orada tek bir halat vardı. "Ben de atlayabilir miyim, Şakir?" diye sordu Canan. Şakir durdu ve biraz düşündü. Sonra halatı Canan'a verdi ve şapkasını onun başına taktı. "Önce sen atla, şapka gözlerini güneşten korur," dedi Şakir. Canan on kez atladı, sonra şapkayı ve halatı Şakir'e geri verdi. Bu kez Şakir atladı. Şakir ile Canan sırayla atlayıp mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "uzun bir halatı çevirip"
   - Cümle 1: «Şakir ormandaki kamp yerinde uzun bir halatı çevirip üstünden atlıyordu.»
   - Açıklama: İp atlamak için 'halat' değil 'ip' kullanılır; kelime yanlış anlamda.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "şapkasını onun başına taktı"
   - Cümle 6: «Sonra halatı Canan'a verdi ve şapkasını onun başına taktı.»
   - Açıklama: Tohumdaki şapka özelliği sorunun (tek halat) çözümünde işe yaramıyor, yalnız süs olarak geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0212` birebir aynı, `@degisim: sağlıklı -> uzun` (tutuyorsan), ardından `@onarim: e71827327175b1c11713813946ca94eda942dd1f`, sonra gövde.

### Hikâye 2: tohum sakir-0223 (deneme 3 -> 4)

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
@degisim: saygılı -> dikkatli
Ormandaki kamp yerinde Şakir pasta dükkanı oyunu oynuyordu. Kozalak pastalarını bir kütüğün üstünde sergiliyordu. Ama kütük yamuktu ve kozalaklar birer birer yere yuvarlandı. Şakir güldü ve onları tek tek topladı. Sonra şapkasını çıkardı ve kütüğün üstüne ters koydu. Kozalakları şapkanın içine dikkatli bir şekilde dizdi. Bu kez hiçbir kozalak yere düşmedi. Şakir en büyük kozalağa vanilya pastası adını verdi. Onu şapkanın tam ortasına koydu. Şakir pasta dükkanı oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kütüğün üstünde sergiliyordu"
   - Cümle 2: «Kozalak pastalarını bir kütüğün üstünde sergiliyordu.»
   - Açıklama: 'sergilemek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Sergilemek' 3 yaşındaki çocuğun bilmediği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0223` birebir aynı, `@degisim: saygılı -> dikkatli` (tutuyorsan), ardından `@onarim: 137993375d91cfb9020e9034ed640bb7f4e00f15`, sonra gövde.

### Hikâye 3: tohum sakir-0229 (deneme 3 -> 4)

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
@plan: rüzgar oyundaki örtüyü uçurdu | keseyi şapkasının altına koyup yeniden gösterdi
@tohum: sakir-0229
Ormanda serin bir rüzgar esiyordu. Şakir sihir oyunu oynuyordu ve Fil Necati'ye bir keseyi yok edecekti. Ama rüzgar örtüsünü uçurdu ve ağaçların arasına götürdü. "Örtü olmadan keseyi nasıl yok edeceksin?" diye sordu Necati. Şakir hemen şapkasını çıkardı. Küçük keseyi yere koydu ve üstünü şapkayla örttü. "Kese yok oldu!" dedi Şakir. Necati hortumunu kaldırdı ve şaşırmış gibi yaptı. "Kese nereye gitti?" diye sordu Necati. Şakir şapkayı yavaşça kaldırdı ve kese yeniden belirdi. Şakir şapkasını başına taktı ve eğilerek selam verdi. "Mükemmel bir sihir, Şakir!" dedi Necati.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Fil Necati'ye bir keseyi yok edecekti"
   - Cümle 2: «Şakir sihir oyunu oynuyordu ve Fil Necati'ye bir keseyi yok edecekti.»
   - Açıklama: Yönelme ekli nesne fiile bağlanmıyor; 'Necati'ye keseyi yok edip gösterecekti' gibi olmalı.
   - Açıklama: 'Necati'ye' yönelme eki 'yok etmek' fiiline uymuyor; 'Necati'ye bir keseyi yok etme sihri gösterecekti' gibi olmalı.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Şakir sihir oyunu oynuyordu"
   - Cümle 2: «Şakir sihir oyunu oynuyordu ve Fil Necati'ye bir keseyi yok edecekti.»
   - Açıklama: Kartın tohum yasak kategorileri büyüyü dünyanın dışında tutuyor; sihir oyunu bu kapalı dünyaya aykırı olabilir.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kese yeniden belirdi"
   - Cümle 10: «Şakir şapkayı yavaşça kaldırdı ve kese yeniden belirdi.»
   - Açıklama: 'Kese' ve 'belirdi' 3 yaşındaki bir çocuğun bilmeyeceği kelimeler.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0229` birebir aynı, ardından `@onarim: fcb3e6c8f0892ed5d8f82531a595ace18e91ee95`, sonra gövde.

### Hikâye 4: tohum sakir-0235 (deneme 3 -> 4)

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
Bir sabah Şakir kumsalda ilk kez el arabası itiyordu. Arabayla Necati'nin kalesine kum taşıyordu. Ama arabanın tekeri yumuşak kuma battı ve araba durdu. Şakir arabayı itti, ama araba gitmedi. Sonra şapkasını çıkardı. Şapkayla tekerleğin önündeki kumu kazıdı. "Tekeri kurtaracağım, Necati!" dedi Şakir. Şakir arabayı yeniden itti ve teker kumdan çıktı. Araba yine ilerledi. Şakir şapkasındaki kumu döktü ve başına taktı. Sonra arabayı kaleye kadar götürdü. Şakir ile Necati kaleyi mutlu mutlu yapmaya devam etti.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "şapkasındaki kumu döktü ve başına taktı"
   - Cümle 10: «Şakir şapkasındaki kumu döktü ve başına taktı.»
   - Açıklama: 'taktı' fiilinin nesnesi eksik, cümle kumu başına taktı diye okunuyor; 'şapkayı başına taktı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0235` birebir aynı, `@degisim: elmalı -> yumuşak` (tutuyorsan), ardından `@onarim: b1f70c7bd025212e9b20aa8704c95abf3cfe1063`, sonra gövde.

### Hikâye 5: tohum sakir-0239 (deneme 2 -> 3)

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
Bir sabah dalgalar kumsala deniz kokulu bir sürü beyaz kabuk getirmişti. Şakir onlarla kumdaki kalesini süslemek istedi. Ama küçük avucuna yalnız üç kabuk sığıyordu. Kale de kabuklardan biraz uzaktaydı. Şakir başındaki şapkayı çıkardı ve kuma koydu. Şapkanın içini kabuklarla doldurdu. Sonra şapkayı iki eliyle yavaşça kaleye taşıdı. Kabukları kalenin çevresine tek tek yatırdı. Kale beyaz kabuklarla çok güzel oldu. Şakir bundan sonra çok şey taşırken elleri yerine bir kap kullandı.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "çevresine tek tek yatırdı"
   - Cümle 8: «Kabukları kalenin çevresine tek tek yatırdı.»
   - Açıklama: Kabuklar için 'yatırmak' fiili uygun değil; 'dizdi' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kalenin çevresine tek tek yatırdı"
   - Cümle 8: «Kabukları kalenin çevresine tek tek yatırdı.»
   - Açıklama: Kabuk 'yatırılmaz'; 'dizdi' ya da 'koydu' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "elleri yerine bir kap kullandı"
   - Cümle 10: «Şakir bundan sonra çok şey taşırken elleri yerine bir kap kullandı.»
   - Açıklama: Yapı eksik; 'ellerini kullanmak yerine' ya da 'elleri yerine bir kapla taşıdı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0239` birebir aynı, `@degisim: patlıcan -> kabuk` (tutuyorsan), ardından `@onarim: f7420513d34cc8cbd93ec237947445aa32d19cf3`, sonra gövde.

### Hikâye 6: tohum sakir-0241 (deneme 2 -> 3)

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
@plan: tek tren vardı ve ikisi de onu itmek istedi | şapkayı sırayla taktılar ve şapkayı takınca treni ittiler
@tohum: sakir-0241
@degisim: dürüst -> kısa
Bir sabah Şakir ile Canan kumsalda oyuncak trenle oynuyordu. Kumda uzun bir tren yolu yapmışlardı. Ama tek bir tren vardı ve ikisi de onu itmek istedi. Şakir şapkasını çıkardı ve Canan'ın başına taktı. Artık ikisi de treni yalnız şapkayı takınca itiyordu. Canan treni yolda kısa bir süre itti. Sonra başını eğdi, şapkayı çıkardı ve Şakir'e verdi. Şakir de şapkayı taktı ve treni yolun sonuna kadar götürdü. Böylece ikisi de sırayla oynadı ve kimse üzülmedi. Şakir ile Canan oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "şapkayı sırayla taktılar ve şapkayı takınca"
   - Cümle 0 (plan satırı): «tek tren vardı ve ikisi de onu itmek istedi | şapkayı sırayla taktılar ve şapkayı takınca treni ittiler»
   - Açıklama: Plan satırında 'şapkayı' gereksiz yere iki kez tekrarlanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Artık ikisi de treni yalnız şapkayı takınca itiyordu"
   - Cümle 5: «Artık ikisi de treni yalnız şapkayı takınca itiyordu.»
   - Açıklama: Şapka kuralı kimse önermeden ve sebepsizce ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0241` birebir aynı, `@degisim: dürüst -> kısa` (tutuyorsan), ardından `@onarim: 81488d00d1afa9c457392dbcc6a6a403f4de787e`, sonra gövde.

### Hikâye 7: tohum sakir-0243 (deneme 2 -> 3)

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
@plan: paylaşmak istedi ama rüzgar cipsleri uçurdu | paketin yarısını şapkaya boşaltıp filin önüne bıraktı
@tohum: sakir-0243
Bir sabah Şakir ile Necati ormandaki rüzgarlı kamp yerinde oturuyordu. Şakir'in bir paket cipsi vardı ve onu Necati ile paylaşmak istedi. Paketin ipi çözüldü, ama rüzgar cipsleri hemen uçurmaya başladı. Şakir hemen şapkasını çıkardı ve paketin yarısını içine boşalttı. Sonra şapkayı Necati'nin önüne bıraktı. Necati uzun hortumuyla cipsleri tek tek aldı ve yedi. Şapkanın içindekiler hiç uçmadı. Şakir de kalan cipsleri yedi. Şakir çok sevindi, çünkü cipsleri Necati ile birlikte yemişlerdi.
```

**Hakem bulguları (6):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "paketin yarısını şapkaya boşaltıp filin önüne bıraktı"
   - Cümle 0 (plan satırı): «paylaşmak istedi ama rüzgar cipsleri uçurdu | paketin yarısını şapkaya boşaltıp filin önüne bıraktı»
   - Açıklama: Plan çözümü figüre veriyor ama gövdede bunu Necati yapıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Paketin ipi çözüldü,"
   - Cümle 3: «Paketin ipi çözüldü, ama rüzgar cipsleri hemen uçurmaya başladı.»
   - Açıklama: Cips paketinin ipi olmaz; 'paketin ağzı açıldı' gibi bir kelime gerekir.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Paketin ipi çözüldü"
   - Cümle 3: «Paketin ipi çözüldü, ama rüzgar cipsleri hemen uçurmaya başladı.»
   - Açıklama: Cips paketinde sebepsiz bir ip beliriyor ve çözülmesi açıklanmıyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "paketin yarısını içine boşalttı"
   - Cümle 4: «Şakir hemen şapkasını çıkardı ve paketin yarısını içine boşalttı.»
   - Açıklama: Sorunun sebebi rüzgar ama açık şapkaya boşaltmak rüzgara karşı neden işe yaradığı belli olmayan, sebebe doğrudan yönelmeyen bir çözüm.
   - Açıklama: Açık şapka rüzgarı engellemiyor; çözüm cipsleri uçuran rüzgara doğrudan yönelmiyor.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sonra şapkayı Necati'nin önüne bıraktı"
   - Cümle 5: «Sonra şapkayı Necati'nin önüne bıraktı.»
   - Açıklama: Şapkayı çıkaran Necati şapkayı yine kendi önüne bırakıyor, özne çelişkili.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şakir de kalan cipsleri yedi"
   - Cümle 8: «Şakir de kalan cipsleri yedi.»
   - Açıklama: Rüzgar paketteki cipsleri uçuruyordu ama pakette kalan cipsler sorunsuz yeniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0243` birebir aynı, ardından `@onarim: 6839c22d68a8c3334b650f34c40049f753117e0b`, sonra gövde.

### Hikâye 8: tohum sakir-0246 (deneme 2 -> 3)

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
Bir sabah Şakir kumsalda ilk kez kumdan bir kule yapmayı denedi. Ama kule hep yıkıldı, çünkü kum çok kuruydu. Kuru kum elinden hep dökülüyordu. Şakir kumu biraz kazdı ve altında ıslak kum buldu. Islak kum yumuşaktı ve hiç dökülmüyordu. Şakir meyveli şapkasını çıkardı ve ıslak kumla doldurdu. Şapkayı çevirip kuma bastırdı ve yavaşça kaldırdı. Kumda yuvarlak ve yüksek bir kule duruyordu. Kule kocaman bir keke benziyordu ve Şakir'in karnı guruldadı. Şakir buna çok güldü ve yanına iki kule daha yaptı. Sonra Şakir mutlu mutlu yeni kuleler yapmaya devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir'in karnı guruldadı"
   - Cümle 9: «Kule kocaman bir keke benziyordu ve Şakir'in karnı guruldadı.»
   - Açıklama: Karnının guruldaması olaydan çıkmıyor ve hiçbir işe yaramayan ayrıntı.
   - Açıklama: Şakir'in acıkması sebepsiz ekleniyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0246` birebir aynı, `@degisim: vazo -> kum` (tutuyorsan), ardından `@onarim: c42288ade7332ca5f602b296fb60c0dfdbc68dbf`, sonra gövde.

### Hikâye 9: tohum sakir-0251 (deneme 2 -> 3)

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
Kumsalda Canan bir havlunun üstünde kitap okuyordu. Şakir resimlere bakmak için kardeşinin kitabını hızla kendine çekti. Bir sayfa koptu ve kuma düştü. Canan şaşkın şaşkın önce kitaba, sonra Şakir'e baktı. "Özür dilerim, Canan, kitabını hızla çektim," dedi Şakir. "Çantada bant var," dedi Canan. Şakir sayfayı aldı ve üstündeki kumu şapkasıyla sildi. Sonra sayfayı bantla kitaba dikkatle yapıştırdı. Canan gülümsedi ve Şakir'e resimleri gösterdi. Şakir çok sevindi, çünkü kardeşinin kitabı yeniden tamamdı.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "üstündeki kumu şapkasıyla sildi"
   - Cümle 7: «Şakir sayfayı aldı ve üstündeki kumu şapkasıyla sildi.»
   - Açıklama: Tohumdaki şapka özelliği sorunu çözmüyor, yalnız kum silmek için yan bir ayrıntı olarak geçiyor; çözüm bantla sağlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0251` birebir aynı, ardından `@onarim: 1b5f3887801d76a6ff6d44f7b4644adc4a9dd99c`, sonra gövde.

### Hikâye 10: tohum sakir-0259 (deneme 2 -> 3)

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
@plan: kuru kum ince tüylerde hep dağıldı | yosunları şapkayla getirip tüy yaptı
@tohum: sakir-0259
@degisim: tasarlamak -> yapmak
Serin bir rüzgar esiyordu. Şakir kumsalda kumdan bir aslan yapmak istedi. Aslanın gövdesini yaptı, ama tüyler çok inceydi ve kuru kum hep dağıldı. Biraz ileride kumun üstünde uzun yeşil yosunlar vardı. Ama yosunlar ıslak ve kaygandı, elinden kayıp düşüyordu. Şakir şapkasını çıkardı ve yosunları içine doldurdu. Şapkayı kumdan aslanın yanına getirdi. Yosunları aslanın başının çevresine tek tek dizdi. Kumdan aslanın yeşil tüyleri oldu. Şakir aslana bakıp güldü. Sonra Şakir kumda mutlu mutlu yeni aslanlar yapmaya devam etti.
```

**Hakem bulguları (2):**

1. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Ama yosunlar ıslak ve kaygandı"
   - Cümle 5: «Ama yosunlar ıslak ve kaygandı, elinden kayıp düşüyordu.»
   - Açıklama: Kumun dağılmasından sonra yosunların elden kayması ikinci bir sorun açıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Kumdan aslanın yeşil tüyleri oldu"
   - Cümle 9: «Kumdan aslanın yeşil tüyleri oldu.»
   - Açıklama: Aslanın başının çevresindeki kıllar 'yele'dir; 'tüy' yanlış anlamda kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0259` birebir aynı, `@degisim: tasarlamak -> yapmak` (tutuyorsan), ardından `@onarim: bc80fbd49121ef75126e9ca30b919e2c6a05df2c`, sonra gövde.

### Hikâye 11: tohum sakir-0260 (deneme 2 -> 3)

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
Şakir kumsalda havlusunun yanında resimli valizini açtı ve bir top çıkardı. Topu iyice şişirdi ve yere koydu. Ama Şakir arkasını dönünce top yerinde yoktu. Kumda yalnız ince, uzun bir iz vardı. Şakir bu izi çok merak etti. İzin yanından birkaç adım yürüdü. İz, küçük bir yosun yığınında bitiyordu. Şakir şapkasını çıkardı ve onunla yosunları dikkatle kenara itti. Altından topun kırmızı rengi göründü. Top rüzgarla yuvarlanmış ve yosunların altına girmişti. Şakir topunu çıkarıp sıkıca tuttu. Şakir çok sevindi, çünkü iz onu topuna götürmüştü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "iz onu topuna götürmüştü"
   - Cümle 12: «Şakir çok sevindi, çünkü iz onu topuna götürmüştü.»
   - Açıklama: İz birini bir yere götürmez; mecazlı anlatım küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0260` birebir aynı, ardından `@onarim: 9d7856cd0c5150d972d08ac9a4d391b440188602`, sonra gövde.

### Hikâye 12: tohum sakir-0261 (deneme 2 -> 3)

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
Rüzgar hafif hafif esiyordu. Canan ahşap bir masada Şakir'e bezelye satıyordu. Ama Şakir hızlı koştu, masaya çarptı ve bezelyeler otlara döküldü. Canan buna çok üzüldü. "Özür dilerim, Canan, çok hızlı koştum," dedi Şakir. Sonra şapkasını çıkarıp ters çevirdi. Taneleri tek tek toplayıp içine koydu. Hepsini masanın üstüne yavaşça boşalttı. "Teşekkürler, Şakir," dedi Canan ve güldü. Sonra Canan ona bir avuç bezelye sattı. İkisi de çok sevindi, çünkü kamp yerindeki oyunları yeniden başlamıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama Şakir hızlı koştu"
   - Cümle 3: «Ama Şakir hızlı koştu, masaya çarptı ve bezelyeler otlara döküldü.»
   - Açıklama: Önceki cümleyle karşıtlık olmadığı için 'ama' bağlacı yanlış anlamda kullanılmış.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kamp yerindeki oyunları yeniden başlamıştı"
   - Cümle 11: «İkisi de çok sevindi, çünkü kamp yerindeki oyunları yeniden başlamıştı.»
   - Açıklama: Kamp yeri ve oyun daha önce hiç kurulmadan son cümlede sebepsiz beliriyor.
   - Açıklama: Hikayede hiç kurulmamış bir oyun ve kamp yeri sonda sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0261` birebir aynı, ardından `@onarim: 0e8275f14e20e9f444e28daa0bdbeeac075687b0`, sonra gövde.
