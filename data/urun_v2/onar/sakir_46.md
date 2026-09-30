# Editör görevi (onarım): Şakir, onarım partisi 46

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 10 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar46.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar46.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0285 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0285
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'gitar', fiil 'toplamak', sıfat 'sarı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: koşarken torbaya çarptı ve armutlar döküldü | babasından özür diledi ve armutları şapkasına topladı
@tohum: sakir-0285
Şakir kamp yerinde koşarken babasının armut torbasına çarptı. Kağıt torba yırtıldı ve sarı armutlar çimlere döküldü. Babası Remzi gitar çalmayı bıraktı ve armutlara baktı. "Özür dilerim, baba, koşarken torbayı görmedim," dedi Şakir. "Önemli değil, ama onları nereye koyacağız?" diye sordu Remzi. Şakir hemen şapkasını çıkardı ve ters çevirdi. Sonra armutları tek tek içine topladı. Remzi de uzaktaki iki armudu getirdi. Şapka çabucak doldu. "Şapkan tam bir sepet gibi oldu!" dedi Remzi ve güldü. "Teşekkürler, baba, hadi şimdi birlikte birer armut yiyelim!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Şakir kamp yerinde koşarken"
   - Cümle 1: «Şakir kamp yerinde koşarken babasının armut torbasına çarptı.»
   - Açıklama: Başlıktaki yer orman ama hikaye kamp yerinde başlıyor ve ormandan hiç söz edilmiyor.
2. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Babası Remzi gitar çalmayı bıraktı"
   - Cümle 3: «Babası Remzi gitar çalmayı bıraktı ve armutlara baktı.»
   - Açıklama: Kartta Remzi'nin gitarı ya da gitar çalma yeteneği yok.
3. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Babası Remzi gitar çalmayı"
   - Cümle 3: «Babası Remzi gitar çalmayı bıraktı ve armutlara baktı.»
   - Açıklama: Kartın yanlar bölümündeki Remzi ilişkisinde gitar çalma yeteneği ya da gitar yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0285` birebir aynı, ardından `@onarim: bcd9d2d45d38eab31dde0b649d57ddcef2037444`, sonra gövde.

### Hikâye 2: tohum sakir-0287 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0287
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kitaplık', fiil 'bitirmek', sıfat 'yardımsever'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: küçük bir kitap kitaplığın altına kaydı | şapkasıyla kitabı dışarı çekti
@tohum: sakir-0287
Evin salonunda Kadriye kitaplığın tozunu alıyordu. Şakir de annesinin yanında duruyordu. Kadriye rafı silerken küçük bir kitap düştü ve kitaplığın altına kaydı. Kadriye elini altına uzattı, ama kitaba ulaşamadı. "Anneciğim, ben yardım edeyim," dedi Şakir. Şakir yere yattı ve şapkasını çıkardı. Şapkanın kenarını kitaplığın altına soktu. Sonra şapkayı yavaşça kendine doğru çekti. Küçük kitap şapkayla birlikte dışarı çıktı. "Aferin, Şakir, çok yardımsever davrandın!" dedi Kadriye. Şakir kitabı annesine verdi ve Kadriye onu rafına koydu. Böylece Kadriye işini bitirdi. Sonra Şakir ile annesi o kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (3):**

1. **C6** (K merceği) — Kalıp yargı yok.
   - Alıntı: "Kadriye kitaplığın tozunu alıyordu"
   - Cümle 1: «Evin salonunda Kadriye kitaplığın tozunu alıyordu.»
   - Açıklama: Annenin ev temizliği yapması kalıp yargı olarak okunabilir.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şakir de annesinin yanında"
   - Cümle 2: «Şakir de annesinin yanında duruyordu.»
   - Açıklama: Anne önce Kadriye adıyla tanıtılıp hemen 'annesi' diye anılıyor; ikisinin aynı kişi olduğu belli değil.
3. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "o kitabı birlikte mutlu mutlu okudu"
   - Cümle 13: «Sonra Şakir ile annesi o kitabı birlikte mutlu mutlu okudu.»
   - Açıklama: Kitap rafa konup iş bitmişken hemen o kitabın okunması çelişkili bir kapanış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0287` birebir aynı, ardından `@onarim: 12be2e652124b79ee746fb9dfb661038472bb360`, sonra gövde.

### Hikâye 3: tohum sakir-0288 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Canan
@tohum: sakir-0288
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'krema', fiil 'uyandırmak', sıfat 'bozuk'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Canan
@plan: oyuncak saat bozuktu ve çalmadı | şapkasını salladı ve kardeşini uyandırdı
@tohum: sakir-0288
Parkta Şakir ile Canan kremalı kek için bir oyun oynuyordu. Canan çimlere uzandı ve uyuyor gibi yaptı. Şakir onu oyuncak saatle uyandırmak istedi, ama saat bozuktu ve çalmadı. Şakir düğmeye iki kez bastı, yine ses çıkmadı. Canan gözlerini kapalı tuttu ve hiç kıpırdamadı. Sonra Şakir şapkasını çıkardı. Şapkayı Canan'ın yüzüne doğru yavaşça salladı. Şapkanın serin rüzgarı Canan'ın bıyıklarını gıdıkladı. Canan güldü ve gözlerini açtı. "Uyandım, uyandım, bu çok komik bir rüzgardı!" dedi Canan. "Kazandım, ama kekin en kremalı parçası senin, Canan!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kremalı kek için bir oyun oynuyordu"
   - Cümle 1: «Parkta Şakir ile Canan kremalı kek için bir oyun oynuyordu.»
   - Açıklama: Kek için oynanan oyunun kuralı hiç anlatılmıyor ve sondaki kazanma sebepsiz beliriyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şapkanın serin rüzgarı"
   - Cümle 8: «Şapkanın serin rüzgarı Canan'ın bıyıklarını gıdıkladı.»
   - Açıklama: Şapkanın rüzgarı olmaz; sallanan şapkanın yaptığı esinti kastediliyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şapkanın serin rüzgarı Canan'ın"
   - Cümle 8: «Şapkanın serin rüzgarı Canan'ın bıyıklarını gıdıkladı.»
   - Açıklama: Şapkanın rüzgarı olmaz; sallanan şapkanın yaptığı esinti öznesine uygun anlatılmamış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0288` birebir aynı, ardından `@onarim: 0b6b3092c0d4a8c2e0f923b5f8c28f5007af5143`, sonra gövde.

### Hikâye 4: tohum sakir-0289 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0289
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'fasulye', fiil 'bırakmak', sıfat 'kararlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: rüzgar havlunun köşelerini hep havaya kaldırdı | babasından yardım istedi ve şapkasını kumla doldurdu
@tohum: sakir-0289
Rüzgar kumsalda hızlı hızlı esiyordu. Şakir öğle yemeği için büyük havluyu kumun üstüne açmak istedi. Ama rüzgar havlunun köşelerini hep havaya kaldırdı. Şakir iki kez daha denedi, ama havlu yine uçuştu. Sonra kararlı bir sesle babasına seslendi. "Baba, bana yardım eder misin?" diye sordu Şakir. Remzi hemen geldi ve havlunun bir kenarına oturdu. Şakir şapkasını kumla doldurdu ve boş bir köşeye koydu. Öbür köşeye de fasulye kabını bıraktı. Artık rüzgar havluyu kaldıramadı. "Aferin, Şakir, şimdi rahatça yemek yiyebiliriz!" dedi Remzi. Şakir çok sevindi, çünkü babasıyla birlikte havluyu yerinde tutmuştu.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kararlı bir sesle babasına"
   - Cümle 5: «Sonra kararlı bir sesle babasına seslendi.»
   - Açıklama: 'Kararlı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Remzi hemen geldi ve"
   - Cümle 7: «Remzi hemen geldi ve havlunun bir kenarına oturdu.»
   - Açıklama: Remzi'nin baba olduğu hiç söylenmeden adıyla geliyor; kim olduğu belli değil.
   - Açıklama: Remzi'nin baba olduğu söylenmeden adıyla anılıyor; kimin geldiği belli değil.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Öbür köşeye de fasulye kabını bıraktı"
   - Cümle 9: «Öbür köşeye de fasulye kabını bıraktı.»
   - Açıklama: Çözüm babanın oturması, kumlu şapka ve fasulye kabı olmak üzere ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0289` birebir aynı, ardından `@onarim: 83168414df4fdf07ba6fe81b8bfcb05cf8f96c8f`, sonra gövde.

### Hikâye 5: tohum sakir-0291 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0291
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'demet', fiil 'öğretmek', sıfat 'esnek'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: esnek top her seferinde ellerinden kaçtı | şapkasını ters tuttu ve topu içine yakaladı
@tohum: sakir-0291
@degisim: demet -> hortum
Bir sabah Şakir, Necati'ye kumsalda top yakalama oyununu öğretiyordu. Necati topu hortumuyla atıyor, Şakir yakalıyordu. Ama top çok esnekti ve her seferinde Şakir'in ellerinden kaçtı. Top kumda zıplayarak uzağa gitti. Necati kulaklarını salladı ve güldü. Şakir de güldü ve biraz düşündü. Sonra şapkasını çıkardı ve ters çevirip iki eliyle tuttu. "Hadi, Necati, şimdi at!" dedi Şakir. Necati topu yavaşça fırlattı. Top şapkanın içine düştü ve dışarı çıkmadı. "Yakaladın, aferin!" dedi Necati. Sonra oyunu birçok kez daha oynadılar. Şakir çok mutluydu, çünkü artık topu hiç kaçırmıyordu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ama top çok esnekti"
   - Cümle 3: «Ama top çok esnekti ve her seferinde Şakir'in ellerinden kaçtı.»
   - Açıklama: 'Esnek' topun elden kaçmasını anlatmaya uygun kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "top çok esnekti"
   - Cümle 3: «Ama top çok esnekti ve her seferinde Şakir'in ellerinden kaçtı.»
   - Açıklama: 'Esnek' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Necati topu yavaşça fırlattı"
   - Cümle 9: «Necati topu yavaşça fırlattı.»
   - Açıklama: 'Fırlatmak' hızlı atmaktır; 'yavaşça' ile çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0291` birebir aynı, `@degisim: demet -> hortum` (tutuyorsan), ardından `@onarim: b94cca57db99ec3f8482acbb40ad74c3f43ec738`, sonra gövde.

### Hikâye 6: tohum sakir-0292 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0292
- yer: park (Şehirdeki park.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'şemsiye', fiil 'başlamak', sıfat 'güvenli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: çalılardan garip bir pıt pıt sesi geldi | şapkasını yağmura tuttu ve sesin nereden geldiğini buldu
@tohum: sakir-0292
Bir öğleden sonra parkta hafif bir yağmur başladı. Şakir kaydırağın altındaki kuru ve güvenli yere geçti. Birden çalıların arasından pıt pıt diye garip bir ses geldi. Şakir bu sesi çok merak etti. Ama çalılar çok sıktı ve içini göremedi. Sonra şapkasını çıkardı ve yağmura doğru tuttu. Damlalar şapkanın üstüne düştü. Şapkadan da aynı pıt pıt sesi geldi. Şakir çalılara yeniden baktı. Çalıların büyük yaprakları şemsiye gibi açılmıştı. Yağmur damlaları o yapraklara vuruyordu ve ses oradan geliyordu. Şakir sesi bulduğu için güldü ve şapkasını yine taktı. Şakir bundan sonra yağmur başlayınca yaprakların sesini keyifle dinledi.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "pıt pıt diye garip bir ses geldi"
   - Cümle 3: «Birden çalıların arasından pıt pıt diye garip bir ses geldi.»
   - Açıklama: Çalıdan gelen yağmur sesi gerçek bir sorun değil, yalnız bir merak; çocuğun önemseyeceği bir güçlük kurulmuyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çalılar çok sıktı ve içini göremedi"
   - Cümle 5: «Ama çalılar çok sıktı ve içini göremedi.»
   - Açıklama: Özne çalılardan Şakir'e belirtilmeden kayıyor; 'göremedi' fiilinin öznesi belirsiz.
   - Açıklama: Özne 'çalılar' iken 'göremedi' fiili Şakir'e ait ve 'içini' çoğul çalılara uymuyor; özne ve iyelik uyumu bozuk.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yaprakları şemsiye gibi açılmıştı"
   - Cümle 10: «Çalıların büyük yaprakları şemsiye gibi açılmıştı.»
   - Açıklama: Yaprakları şemsiyeye benzeten benzetme mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0292` birebir aynı, ardından `@onarim: 5f57594ae4be8a005b3e5d93afa923a9af7a47e6`, sonra gövde.

### Hikâye 7: tohum sakir-0293 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0293
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ay', fiil 'değmek', sıfat 'bulutlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: güneş çok parlaktı ve beyaz aya bakamadı | şapkasıyla gölge yaptı ve aya rahatça baktı
@tohum: sakir-0293
Ormanda serin bir rüzgar esiyordu. Şakir kamp yerinde bulutlu gökyüzünde beyaz bir ay gördü. Ona iyice bakmak istedi, ama güneş çok parlaktı. Şakir elini gözlerinin üstüne koydu, ama eli küçüktü. Sonra şapkasının kenarını gözlerinin üstüne indirdi. Şapka güneşi kapattı ve gözlerine gölge yaptı. Şimdi ay iyice görünüyordu. Ay, uzun bir ağacın ucuna değiyor gibiydi. Sonra bir bulut geldi ve ay bir süre kayboldu. Şakir sessizce bekledi. Bulut gidince ay yine çıktı. Sonra Şakir çadırın önüne oturdu ve aya mutlu mutlu el salladı.
```

**Hakem bulguları (7):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir kamp yerinde bulutlu"
   - Cümle 2: «Şakir kamp yerinde bulutlu gökyüzünde beyaz bir ay gördü.»
   - Açıklama: Şakir şehrin dışındaki dağdaki kamp yerinde tek başına; güvenli özellik kullanımı satırı tek başına uzağa gitmemesini söylüyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "bulutlu gökyüzünde beyaz bir ay"
   - Cümle 2: «Şakir kamp yerinde bulutlu gökyüzünde beyaz bir ay gördü.»
   - Açıklama: Gökyüzü bulutlu deniyor ama hemen ardından güneşin çok parlak olduğu söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "uzun bir ağacın ucuna değiyor gibiydi"
   - Cümle 8: «Ay, uzun bir ağacın ucuna değiyor gibiydi.»
   - Açıklama: Ayın ağaca değiyor gibi olması benzetmeli bir mecaz; küçük çocuk için soyut.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ay, uzun bir ağacın ucuna değiyor gibiydi"
   - Cümle 8: «Ay, uzun bir ağacın ucuna değiyor gibiydi.»
   - Açıklama: Ayın ağaca değmesi olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
5. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "Sonra bir bulut geldi ve ay bir süre kayboldu"
   - Cümle 9: «Sonra bir bulut geldi ve ay bir süre kayboldu.»
   - Açıklama: Sorun çözüldükten sonra bulutun ayı kapatması ikinci bir sorun açıyor.
6. **M2** (M merceği) — Hikayede yalnız bir sorun var.
   - Alıntı: "bir bulut geldi ve ay bir süre kayboldu"
   - Cümle 9: «Sonra bir bulut geldi ve ay bir süre kayboldu.»
   - Açıklama: Güneş sorunu çözüldükten sonra bulutun ayı kapatması ikinci bir sorun olarak ekleniyor.
7. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bulut gidince ay yine çıktı"
   - Cümle 11: «Bulut gidince ay yine çıktı.»
   - Açıklama: Bulut olayı ana sorundan çıkmıyor ve hikayeye hiçbir katkı sağlamıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0293` birebir aynı, ardından `@onarim: c8e8b3c3b1310c5f0b581268a2f996b12174c1c0`, sonra gövde.

### Hikâye 8: tohum sakir-0295 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0295
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kabuk', fiil 'tanışmak', sıfat 'şeffaf'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kumdaki kabukların arasından garip bir ses geldi | şapkasıyla kabukları tek tek örttü ve sesi buldu
@tohum: sakir-0295
@degisim: tanışmak -> dinlemek
Sert bir rüzgar esiyordu. Şakir ile Canan kumsalda yürürken ince bir ıslık sesi duydular. Ses kumdaki kabukların arasından geliyordu. "Bu ses ne, Canan?" diye sordu Şakir. "Bilmiyorum, ama bir kabuktan geliyor olmalı," dedi Canan. Şakir şapkasını çıkardı ve kabukların üstüne tek tek kapattı. Şapkayı büyük, şeffaf bir kabuğun üstüne kapattı ve ses durdu. Şapkayı kaldırdı ve ses yeniden başladı. "Buldum, sesi bu kabuk yapıyor!" dedi Şakir. "Rüzgar kabuğun içine girince böyle ses çıkar," dedi Canan. Şakir kabuğu kulağına tuttu ve sesi dinledi. "Teşekkürler, Canan, bu sesi birlikte bulduk!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ses kumdaki kabukların arasından geliyordu"
   - Cümle 3: «Ses kumdaki kabukların arasından geliyordu.»
   - Açıklama: Kabuktan gelen ses gerçek bir sorun değil, çocuğun önemseyeceği bir dert kurulmuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "büyük, şeffaf bir kabuğun"
   - Cümle 7: «Şapkayı büyük, şeffaf bir kabuğun üstüne kapattı ve ses durdu.»
   - Açıklama: 'Şeffaf' kelimesini 3 yaşındaki bir çocuk bilmez.
   - Açıklama: 'Şeffaf' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0295` birebir aynı, `@degisim: tanışmak -> dinlemek` (tutuyorsan), ardından `@onarim: a2d62d691896ce0d54326e93fc2ac71d59caaf9e`, sonra gövde.

### Hikâye 9: tohum sakir-0299 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0299
- yer: park (Şehirdeki park.)
- tema: paylaşmak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'rüzgar', fiil 'düzeltmek', sıfat 'saklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: rüzgar esti ve annesinin kurabiyesi yere düştü | şapkasında saklı kurabiyeyi annesiyle paylaştı
@tohum: sakir-0299
Şakir ile annesi Kadriye parkta bir bankta oturuyordu. Birden sert bir rüzgar esti ve Kadriye'nin peçetesindeki kurabiye yere düştü. Kurabiye kirlendi ve Kadriye biraz üzüldü. Şakir hemen başındaki şapkasını çıkardı. Şapkanın içinde saklı iki kurabiye vardı. Şakir onları parkta yemek için oraya koymuştu. "Anneciğim, al, bu senin," dedi Şakir. Kadriye kurabiyeyi aldı ve gülümsedi. "Şapkanda yiyecek mi saklıyorsun?" diye sordu Kadriye ve güldü. Sonra şapkayı Şakir'in başına taktı ve düzeltti. Sonra Şakir ile annesi bankta mutlu mutlu kurabiye yedi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şapkanın içinde saklı iki kurabiye vardı"
   - Cümle 5: «Şapkanın içinde saklı iki kurabiye vardı.»
   - Açıklama: Çözümü getiren kurabiyeler önceden kurulmadan tam gereken anda şapkadan beliriyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra Şakir ile annesi"
   - Cümle 11: «Sonra Şakir ile annesi bankta mutlu mutlu kurabiye yedi.»
   - Açıklama: Art arda iki cümle 'Sonra' ile başlıyor; gereksiz tekrar.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0299` birebir aynı, ardından `@onarim: e1fa158716b87455030fc3649ebbf64250aac72f`, sonra gövde.

### Hikâye 10: tohum sakir-0300 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0300
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'bitki', fiil 'çıkmak', sıfat 'keyifli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: kum çok kuruydu ve kule hep dağıldı | ıslak kumu şapkasına doldurdu ve ters çevirdi
@tohum: sakir-0300
Şakir kumsalda ilk kez kumdan bir kule yapmayı deniyordu. Necati de yanında oturmuş ona bakıyordu. Ama kum çok kuruydu ve kule hep dağıldı. "Necati, kum neden dağılıyor?" diye sordu Şakir. "Kum ıslak olunca birbirine yapışır," dedi Necati. Necati hortumuyla deniz kenarından biraz su çekti ve kuma püskürttü. Şakir ıslak kumu şapkasının içine doldurdu ve iyice bastırdı. Sonra şapkayı ters çevirdi ve yavaşça kaldırdı. Kumdan şapka biçiminde sağlam bir kule çıktı. Şakir kumda bulduğu kuru bir bitki dalını kulenin tepesine taktı. "Bu çok keyifli bir oyun!" dedi Necati. Şakir bundan sonra kule yaparken kumu hep önce ıslattı.
```

**Hakem bulguları (3):**

1. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Necati hortumuyla deniz kenarından biraz su çekti ve kuma püskürttü"
   - Cümle 6: «Necati hortumuyla deniz kenarından biraz su çekti ve kuma püskürttü.»
   - Açıklama: Sorunun sebebi olan kuru kumu Şakir değil Necati ıslatıyor; yan karakter çözümün asıl adımını yapıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Necati hortumuyla deniz kenarından biraz su çekti"
   - Cümle 6: «Necati hortumuyla deniz kenarından biraz su çekti ve kuma püskürttü.»
   - Açıklama: Sorunun sebebi olan kuru kumu Şakir değil Necati ıslatıyor; yan karakter asıl çözüm adımını yapıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kuru bir bitki dalını kulenin tepesine taktı"
   - Cümle 10: «Şakir kumda bulduğu kuru bir bitki dalını kulenin tepesine taktı.»
   - Açıklama: Bitki dalı sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.
   - Açıklama: Dal sebepsiz beliriyor ve olaya hiçbir katkı yapmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0300` birebir aynı, ardından `@onarim: 9dc747805dc538642112c5ea8477205900496140`, sonra gövde.
