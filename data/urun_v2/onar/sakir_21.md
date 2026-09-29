# Editör görevi (onarım): Şakir, onarım partisi 21

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar21.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar21.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0022 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0022
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'eşarp', fiil 'kapamak', sıfat 'buzlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: rüzgar çitteki şapkayı çimenlere düşürüyordu | şapkayı eşarpla çitin tahtasına bağladı
@tohum: sakir-0022
Soğuk bir rüzgar esiyordu. Şakir parkta şapkasına kar topu atma oyunu oynuyordu. Ama rüzgar, çitin üstündeki şapkayı her seferinde buzlu çimenlere düşürüyordu. Şakir şapkayı yerden aldı ve gülümsedi. Sonra boynundaki eşarbı çözdü. Şapkayı eşarpla çitin tahtasına sıkıca bağladı. Rüzgar yine esti ama şapka bu kez düşmedi. Şakir bir gözünü kapadı ve dikkatle nişan aldı. Kar topu şapkanın tam ortasına çarptı. Şapkanın üstünde beyaz, yuvarlak bir iz kaldı. Şakir kahkahayla güldü ve bir top daha attı. Şakir çok eğlendi, çünkü şapkası artık yerinden düşmüyordu.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir parkta şapkasına kar topu atma oyunu oynuyordu"
   - Cümle 2: «Şakir parkta şapkasına kar topu atma oyunu oynuyordu.»
   - Açıklama: Kartın özellik alanına göre Şakir şapkasını hep takar; burada şapka takılmıyor, kar topu hedefi yapılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şapkayı eşarpla çitin tahtasına sıkıca bağladı"
   - Cümle 6: «Şapkayı eşarpla çitin tahtasına sıkıca bağladı.»
   - Açıklama: Karttaki 'Hep şapka takar' özelliği kullanılmıyor; şapka takılmıyor, yalnız nişan hedefi oluyor ve sorunu eşarp çözüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0022` birebir aynı, ardından `@onarim: 3a6d33ce6735421c5b41c669c4da2f89bf57a90d`, sonra gövde.

### Hikâye 2: tohum sakir-0032 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0032
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'yelkenli', fiil 'uzaklaşmak', sıfat 'bilgili'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: oyunda geminin yelkeni yoktu | annesinden havlu isteyip bir dala bağladı
@tohum: sakir-0032
@degisim: bilgili -> büyük
Şakir, kamp yerinde yere düşmüş kalın bir ağaca oturdu. Oyunda bu ağaç bir gemi oldu ve annesi Kadriye de arkasına oturdu. Ama geminin yelkeni yoktu ve yola çıkamıyordu. Şakir macerayı çok severdi, bu yüzden oyunu bırakmadı ve bir yelken aradı. "Anneciğim, büyük mavi havluyu alabilir miyim?" diye sordu Şakir. "Tabii, al," dedi Kadriye ve havluyu ona verdi. Şakir havluyu uzun bir dala bağladı. Sonra dalı iki eliyle havaya kaldırdı. Rüzgar esti ve havlu bir yelken gibi şişti. "Bak, anneciğim, yelkenlimiz uzaklaşıyor!" dedi Şakir. Kadriye güldü ve ellerini çırptı. Şakir çok mutlu oldu, çünkü gemisi sonunda yola çıkmıştı.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "annesinden havlu isteyip bir dala bağladı"
   - Cümle 0 (plan satırı): «oyunda geminin yelkeni yoktu | annesinden havlu isteyip bir dala bağladı»
   - Açıklama: Gövdede havlu hiçbir dala bağlanmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0032` birebir aynı, `@degisim: bilgili -> büyük` (tutuyorsan), ardından `@onarim: d02c3ca01cdd9afbbc023c27b0e811b71244abbc`, sonra gövde.

### Hikâye 3: tohum sakir-0034 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Canan
@tohum: sakir-0034
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tartı', fiil 'ısınmak', sıfat 'şekerli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | ev | Canan
@plan: uğur böcekleri tartıya ters düştü ve dönemedi | yaprak uzatıp böcekleri güneşe taşıdı
@tohum: sakir-0034
@degisim: şekerli -> yeşil
Şakir mutfakta kardeşi Canan ile birlikteydi. Birden içeri minik uğur böcekleri uçup geldi. Böcekler kaygan tartıya indi, kaydı ve ters düştü. Ayaklarını salladılar ama dönemediler. "Canan, onlara nasıl yardım ederiz?" diye sordu Şakir. "Onlara bir yaprak uzat, yaprağı tutarlar," dedi Canan. Şakir macerayı, yani yeni şeyler denemeyi çok severdi. Pencerenin önündeki çiçekten yeşil bir yaprak kopardı. Yaprağı böceklerin ayaklarına yavaşça yaklaştırdı. Böcekler yaprağa tutundu ve döndü. Şakir yaprağı güneşli pencerenin önüne koydu. Uğur böcekleri güneşte ısındı ve kanatlarını açtı. Sonra uçup çiçeğe kondular. "Teşekkürler, Canan, böceklere birlikte yardım ettik!" dedi Şakir.
```

**Hakem bulguları (4):**

1. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Böcekler kaygan tartıya indi"
   - Cümle 3: «Böcekler kaygan tartıya indi, kaydı ve ters düştü.»
   - Açıklama: Notlanan çoğul canlı uğur böcekleri arka planda kalmıyor, olayın merkezine katılıyor.
   - Açıklama: Çoğul canlı uğur böcekleri arka planda kalmıyor, olayın merkezine katılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı, yani yeni şeyler denemeyi"
   - Cümle 7: «Şakir macerayı, yani yeni şeyler denemeyi çok severdi.»
   - Açıklama: 'Macera' soyut bir kavram ve açıklamayla verilmiş.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı, yani yeni şeyler denemeyi çok severdi"
   - Cümle 7: «Şakir macerayı, yani yeni şeyler denemeyi çok severdi.»
   - Açıklama: Macera sevgisi cümlesi olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Macera sevgisi olaya bağlanmayan işlevsiz bir ayrıntı.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şakir yaprağı güneşli pencerenin önüne koydu"
   - Cümle 11: «Şakir yaprağı güneşli pencerenin önüne koydu.»
   - Açıklama: Böcekler döndükten sonra güneşe taşıma sebebe yönelmeyen fazladan bir adım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0034` birebir aynı, `@degisim: şekerli -> yeşil` (tutuyorsan), ardından `@onarim: 6ffddf7f75c8469aef6d4b6db4638b3ae17b9571`, sonra gövde.

### Hikâye 4: tohum sakir-0035 (deneme 5 -> 6)

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
@plan: kalemin mürekkebi birden bitti | kalemini paylaştı ve ikisi sırayla çizdi
@tohum: sakir-0035
@degisim: bağlamak -> paylaşmak
Şakir, Necati ile kamp yerinde bir orman haritası çiziyordu. Necati büyük ağaçları çizecekti. Ama Necati'nin kaleminin mürekkebi birden bitti. Necati üzgün bir yüzle kalemine baktı. "Kalemim artık çizmiyor," dedi Necati. Şakir macerayı, yani yeni yerler görmeyi çok severdi. Bitmiş haritayla kamp yerini dolaşmak istiyordu. Şakir'in tek bir kırmızı kalemi vardı. Şakir bu kalemi hemen Necati'ye uzattı. "Kalemimi seninle paylaşırım, sırayla çizelim," dedi Şakir. Önce Necati ağaçları çizdi. Sonra Şakir çadırı ve yolu çizdi. Harita bitince Şakir ile Necati onu alıp kamp yerini mutlu mutlu gezdi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı, yani yeni yerler görmeyi"
   - Cümle 6: «Şakir macerayı, yani yeni yerler görmeyi çok severdi.»
   - Açıklama: 'Macera' ve tanım cümlesi 3 yaşındaki çocuk için soyut.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı, yani yeni yerler görmeyi çok severdi"
   - Cümle 6: «Şakir macerayı, yani yeni yerler görmeyi çok severdi.»
   - Açıklama: Tohumdaki macera özelliği kartın 'ozellikler' alanından tanım olarak sayılıyor; sorun kalem paylaşmakla çözülüyor, özellik çözümde iş görmüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0035` birebir aynı, `@degisim: bağlamak -> paylaşmak` (tutuyorsan), ardından `@onarim: 6487a9ecddff97c1bd6caf688c311f649a4b6776`, sonra gövde.

### Hikâye 5: tohum sakir-0039 (deneme 5 -> 6)

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
Bir sabah Şakir kamp yerinde küçük bir fidan dikti. Şakir fidanı kendisi sulamak istedi. Ama su dolu kova çok ağırdı ve Şakir onu kaldıramadı. Annesi Kadriye çadırın önünde oturuyordu. Şakir macerayı, yani yeni şeyler denemeyi çok severdi. Bu yüzden hiç çekinmedi ve annesinin yanına koştu. "Anne, kovayı birlikte taşır mıyız?" diye sordu Şakir. "Tabii, hemen geliyorum," dedi Kadriye. İkisi kovayı iki yanından tuttu ve fidanın yanına taşıdı. Şakir suyu fidana yavaş yavaş döktü. Kuru toprak ıslandı ve fidanın yaprakları parladı. "Teşekkürler, anneciğim, fidan artık susuz değil!" dedi Şakir.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı, yani yeni şeyler denemeyi çok severdi."
   - Cümle 5: «Şakir macerayı, yani yeni şeyler denemeyi çok severdi.»
   - Açıklama: 'Macera' ve 'yeni şeyler denemek' 3 yaşındaki çocuk için soyut kavramlardır.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı, yani yeni şeyler denemeyi"
   - Cümle 5: «Şakir macerayı, yani yeni şeyler denemeyi çok severdi.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı, yani yeni şeyler denemeyi çok severdi"
   - Cümle 5: «Şakir macerayı, yani yeni şeyler denemeyi çok severdi.»
   - Açıklama: Karttaki macera özelliği anneden yardım istemenin gerekçesine çevrilmiş, işe yarar biçimde kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden hiç çekinmedi ve annesinin yanına koştu"
   - Cümle 6: «Bu yüzden hiç çekinmedi ve annesinin yanına koştu.»
   - Açıklama: Maceraya düşkünlük annesinden yardım istemenin sebebi olarak zorla bağlanıyor; olay bir öncekinden çıkmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden hiç çekinmedi"
   - Cümle 6: «Bu yüzden hiç çekinmedi ve annesinin yanına koştu.»
   - Açıklama: Macerayı sevmek ile yardım istemekten çekinmemek arasında akla yatkın bir bağ yok; işlevsiz ve zorlama bir gerekçe.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0039` birebir aynı, `@degisim: fide -> fidan` (tutuyorsan), ardından `@onarim: 080dd76e33d5eb482ba1db489c8d988ffebeac59`, sonra gövde.

### Hikâye 6: tohum sakir-0042 (deneme 5 -> 6)

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
Parkta Şakir ile Necati oyuncak kamyonla oynuyordu. Şakir taze bir elmayı kamyona koydu ve kamyonu Necati'ye yolladı. Ama kamyon kumdaki bir çukura girdi ve tekerlekleri takıldı. "Kamyon çukurdan çıkamıyor!" dedi Şakir. Şakir macerayı çok severdi ve oyunu bırakmak istemedi. Hemen çukurun başına koştu ve kamyonu çukurdan çıkardı. Sonra çukuru avuç avuç kumla doldurdu ve düzeltti. Kamyonu yeniden itip Necati'ye yolladı. Bu kez kamyon düz kumdan geçti ve Necati'nin önünde durdu. Necati elmayı hortumuyla aldı ve güldü. "Elma geldi, teşekkürler, Şakir!" dedi Necati. Sonra Şakir ile Necati oyuna mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi ve oyunu bırakmak istemedi.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuk için anlaşılır değil.
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0042` birebir aynı, ardından `@onarim: 43212411dc92ca728d08860aa44e73fe0774a561`, sonra gövde.

### Hikâye 7: tohum sakir-0043 (deneme 5 -> 6)

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
Bir sabah Şakir ile Canan kumsalda oynuyordu. Kumdan bir gemi yapmışlardı. Kırmızı yeleği giyen gemiyi sürecekti ama yelek bir taneydi. Şakir de Canan da gemiyi sürmek istedi. Şakir macerayı çok severdi ve oyunu bırakmak istemedi. "Canan, sırayla sürelim, önce sen giy," dedi Şakir. Canan yeleği giydi ve geminin önüne oturdu. "Çok cesuruz, gemimiz yola çıktı!" dedi Canan. Şakir onun arkasında iki eliyle kürek çekti. Sonra Canan yeleği çıkarıp Şakir'e verdi. Bu kez gemiyi Şakir sürdü ve Canan kürek çekti. Kardeşler bol bol güldü. Şakir çok sevindi, çünkü sırayla oynayınca ikisi de gemiyi sürmüştü.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi ve oyunu bırakmak istemedi.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0043` birebir aynı, ardından `@onarim: eaf99c96b0841b670ea916f5aff85d4f3f31cfff`, sonra gövde.

### Hikâye 8: tohum sakir-0046 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0046
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sırayla oynamak
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'zincir', fiil 'seslenmek', sıfat 'temkinli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: ikisi de önce zinciri saklamak istedi | sırayla oynamayı söyleyip ilk sırayı annesine verdi
@tohum: sakir-0046
@degisim: temkinli -> yavaş
Ormanda, kamp yerinde Şakir ile annesi Kadriye bir oyun oynayacaktı. Ama ikisi de parlak zinciri önce saklamak istedi, çünkü çok eğlenceliydi. Şakir macerayı, yani gizli şeyleri bulmayı da çok severdi. "Anneciğim, sırayla oynayalım, önce sen sakla," dedi Şakir. Kadriye gülümsedi ve zinciri büyük bir taşın altına koydu. "Bul bakalım, Şakir!" diye seslendi Kadriye. Şakir yavaş adımlarla yürüdü ve taşları tek tek kaldırdı. Zincir üçüncü taşın altındaydı. "Buldum!" dedi Şakir sevinçle. Sonra sıra Şakir'e geldi ve zinciri çalıların arasına sakladı. Kadriye etrafa baktı ve zinciri buldu. Şakir ile annesi oyunlarına sırayla, mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı, yani gizli"
   - Cümle 3: «Şakir macerayı, yani gizli şeyleri bulmayı da çok severdi.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sıra Şakir'e geldi ve zinciri çalıların arasına sakladı"
   - Cümle 10: «Sonra sıra Şakir'e geldi ve zinciri çalıların arasına sakladı.»
   - Açıklama: Bağlı iki yüklemin öznesi farklı; 'sıra' zinciri saklamaz, özne uyumu bozuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0046` birebir aynı, `@degisim: temkinli -> yavaş` (tutuyorsan), ardından `@onarim: 36637989e9933a1ce96020f374e7a96042e9ae8f`, sonra gövde.

### Hikâye 9: tohum sakir-0054 (deneme 4 -> 5)

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
Şakir kumsalda ilk kez kırmızı bir uçurtma uçurmayı denedi. Ama uçurtma hep yere düştü, çünkü Şakir ipi hiç bırakmıyordu. Sonra şemsiyenin gölgesine oturdu ve biraz somurttu. Ama Şakir macerayı çok severdi, bu yüzden uçurtmayı bir daha denemek istedi. Uçurtmaya ve ipe uzun uzun baktı. Denizden hafif bir rüzgar esiyordu. Şakir kalktı ve kumda yeniden koştu. Bu kez ipi yavaş yavaş bıraktı. Kırmızı uçurtma rüzgarla yükseldi ve havada kaldı. Şakir sevinçle zıpladı ve ipi sıkıca tuttu. Sonra kumsalda uçurtmasını mutlu mutlu uçurmaya devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Ama Şakir macerayı çok severdi, bu yüzden uçurtmayı bir daha denemek istedi.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şakir sevinçle zıpladı ve ipi sıkıca tuttu"
   - Cümle 10: «Şakir sevinçle zıpladı ve ipi sıkıca tuttu.»
   - Açıklama: Sorunun sebebi ipi sıkı tutmakken çözümden hemen sonra Şakir ipi yine sıkıca tutuyor ve uçurtma düşmüyor.
   - Açıklama: Sorun ipi sıkı tutmakken çözümden sonra Şakir ipi yine sıkıca tutuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0054` birebir aynı, ardından `@onarim: eca817d788064ea99861a848ecad1832081f4da7`, sonra gövde.

### Hikâye 10: tohum sakir-0056 (deneme 4 -> 5)

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
Şakir ormandaki kamp yerinde ağaçların arasında koşuyordu. Babası Remzi bir taşın üstünde oturmuş, yapraklardan ufak bir taç yapıyordu. Şakir koşarken babasının koluna çarptı ve tacı yere düşürdü. Tacın yaprakları otların arasına dağıldı. Şakir hemen durdu ve dağılan yapraklara baktı. "Özür dilerim, baba, seni görmedim," dedi Şakir. "Tamam, Şakir, birlikte düzeltelim," dedi Remzi ve gülümsedi. Şakir macerayı çok severdi, yaprakları taşın arkasında bile aradı. Hepsini tek tek buldu. Sonra babasıyla birlikte onları taca taktı. Remzi tacı Şakir'in başına koydu ve ikisi de güldü. Şakir çok sevindi, çünkü özür dilemiş ve tacı babasıyla yeniden yapmıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "çok severdi, yaprakları taşın"
   - Cümle 8: «Şakir macerayı çok severdi, yaprakları taşın arkasında bile aradı.»
   - Açıklama: İki bağımsız cümle bağlaçsız virgülle birleştirilmiş ve aralarında dilbilgisel bağ kurulmamış.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Şakir macerayı çok severdi, yaprakları"
   - Cümle 8: «Şakir macerayı çok severdi, yaprakları taşın arkasında bile aradı.»
   - Açıklama: İki ilgisiz yargı virgülle bağlanmış, cümle dilbilgisel olarak kopuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0056` birebir aynı, ardından `@onarim: 7bb3e0881fa3281271b1ba743fcfc325488976f2`, sonra gövde.

### Hikâye 11: tohum sakir-0057 (deneme 3 -> 4)

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
@plan: koşarken ayağı elbiseye takıldı ve elbise rüzgarla uçtu | özür diledi ve çalılarda elbiseyi bulup getirdi
@tohum: sakir-0057
@degisim: pirinç -> elbise
Rüzgar esiyordu ve Şakir kamp yerinde koşuyordu. Kardeşi Canan örtüde oyuncak bebeğine bir elbise hazırlıyordu. Şakir koşarken ayağı elbiseye takıldı. Elbise havaya kalktı ve rüzgarla uçup kayboldu. Canan çok üzüldü, çünkü oyuncak bebeğinin başka elbisesi yoktu. Şakir hemen durdu ve kardeşinden özür diledi. Macerayı çok seven Şakir yakındaki karmakarışık çalılara eğilip baktı. Küçük elbise bir dala takılmıştı. Şakir elbiseyi dikkatle aldı ve Canan'a götürdü. İkisi oyuncak bebeğe elbiseyi birlikte giydirdi. Canan gülümsedi ve Şakir'e sarıldı. Şakir ile Canan oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 4: «Elbise havaya kalktı ve rüzgarla uçup kayboldu.»
   - Açıklama: Asıl sorun olan elbisenin uçup kaybolması ilk 3 cümlede değil ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0057` birebir aynı, `@degisim: pirinç -> elbise` (tutuyorsan), ardından `@onarim: 5831273160cdf72a698028e9e0194f3a0304bd08`, sonra gövde.

### Hikâye 12: tohum sakir-0059 (deneme 3 -> 4)

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
Deniz kıyısında hava biraz soğumuştu. Şakir ile Canan kalın giysiler içinde kumda oturuyordu. Birden rüzgarla birlikte ıslık gibi ince bir ses geldi. "Bu ses nereden geliyor?" diye sordu Şakir. "Sabırlı olalım ve dikkatle dinleyelim," dedi Canan. İkisi sessizce bekledi. Rüzgar yine esti ve ses büyük bir kabuğun yanından geldi. Şakir şapkasını çıkardı ve kabuğun üstüne kapattı. Islık hemen kesildi. Şapkayı kaldırınca ıslık tekrar başladı. "Rüzgar kabuğun içine esince bu ses çıkıyor!" dedi Şakir. Sonra kabuğu kulağına tuttu ve güldü. İkisi de çok sevindi, çünkü sesin nereden geldiğini bulmuşlardı.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şapkasını çıkardı ve kabuğun üstüne kapattı"
   - Cümle 8: «Şakir şapkasını çıkardı ve kabuğun üstüne kapattı.»
   - Açıklama: 'Şapkayı kabuğun üstüne kapatmak' yanlış kullanım; 'şapkayla kabuğu kapattı' ya da 'şapkayı kabuğun üstüne koydu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0059` birebir aynı, ardından `@onarim: 99b68ac71144cfa33a79e2f6918c3c2f3e84d3e6`, sonra gövde.
