# Editör görevi (onarım): Şakir, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar15.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0017 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0017
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'fındık', fiil 'anlamak', sıfat 'peynirli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kayaların arasından bilinmeyen bir ses geldi | şapkasını öne çekip delikteki fındığı gördü
@tohum: sakir-0017
@degisim: peynirli -> küçük
Bir sabah Şakir ile Canan kumsalda fındık yiyordu. Şakir'in elinden bir fındık düştü ve kayalara doğru yuvarlandı. Biraz sonra kayaların arasından tık tık diye bir ses geldi. Şakir bu sesin ne olduğunu anlamak istedi. "Canan, bu ses nereden geliyor?" diye sordu Şakir. "Bilmiyorum, ben de merak ettim," dedi Canan. Şakir kayalara yaklaştı ve sesin geldiği bir delik buldu. Deliğe baktı, ama güneş çok parlaktı ve içini göremedi. Hemen geniş şapkasını öne doğru çekti. Şapka gözlerine gölge yaptı ve deliğin içi göründü. İçeride düşen fındık vardı ve küçük dalgalar onu taşa vuruyordu. "Bak, Canan, sesi yapan benim fındığımmış!" dedi Şakir sevinçle.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir kayalara yaklaştı ve sesin geldiği bir delik buldu"
   - Cümle 7: «Şakir kayalara yaklaştı ve sesin geldiği bir delik buldu.»
   - Açıklama: Dalgaların vurduğu kayalara yalnız yaklaşıp deliğe bakmak çocuğun taklit edebileceği tehlikeli bir davranış.
   - Açıklama: Şakir dalgaların vurduğu kayalara yaklaşıp deliğe bakıyor; çocuk taklit ederse kayalık kıyıda tehlikeli olabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0017` birebir aynı, `@degisim: peynirli -> küçük` (tutuyorsan), ardından `@onarim: 11b69483bcdc18b9a0164b635dd975a0f1af2a35`, sonra gövde.

### Hikâye 2: tohum sakir-0021 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0021
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'simit', fiil 'sarmak', sıfat 'ılık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: fil acıkmıştı ama yanında yiyecek yoktu | simidini ikiye böldü ve yarısını file verdi
@tohum: sakir-0021
Bir sabah Şakir ile Necati ormandaki kamp yerindeydi. Ama Necati'nin karnı acıkmıştı ve yanında hiç yiyecek yoktu. Şakir macerayı çok severdi, bu yüzden kampa gelirken çantasına yiyecek koymuştu. Çantadan bir beze sardığı ılık bir simit çıkardı. Sonra bezi açtı ve simidi iki eşit parçaya böldü. "Necati, yarısı senin," dedi Şakir. Necati simidin yarısını hortumuyla aldı. "Teşekkür ederim, Şakir, çok acıkmıştım," dedi Necati. İkisi bir kütüğün üstüne oturdu ve simidi birlikte yedi. Şakir çok sevindi, çünkü simidini Necati ile paylaşmıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 3: «Şakir macerayı çok severdi, bu yüzden kampa gelirken çantasına yiyecek koymuştu.»
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden kampa gelirken"
   - Cümle 3: «Şakir macerayı çok severdi, bu yüzden kampa gelirken çantasına yiyecek koymuştu.»
   - Açıklama: Çözümü getiren yiyecek, macerayı sevmek gibi ilgisiz bir sebeple çantadan çıkarılıyor ve bağ zorlama kalıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden kampa gelirken çantasına yiyecek koymuştu"
   - Cümle 3: «Şakir macerayı çok severdi, bu yüzden kampa gelirken çantasına yiyecek koymuştu.»
   - Açıklama: Maceracı olmak yiyecek getirmenin sebebi değil; çözümü getiren simit zayıf bir sebep-sonuç bağıyla beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0021` birebir aynı, ardından `@onarim: 57b27487bf5ef7bb51bd3e115e1b284eb2f10295`, sonra gövde.

### Hikâye 3: tohum sakir-0025 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0025
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'piyano', fiil 'küçültmek', sıfat 'şanslı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: fazla çiçek yüzünden taç çok büyük oldu | üç çiçek çıkarıp tacı şapkasına göre küçülttü
@tohum: sakir-0025
@degisim: piyano -> çiçek
Şakir, ormandaki kamp yerinde annesi Kadriye için sürpriz bir çiçek tacı yapıyordu. Ama tacı çok fazla çiçekle yaptığı için taç büyük oldu. Şakir tacı şapkasına taktı ama taç aşağı düştü. Üç çiçek çıkardı ve tacı küçülttü. Bu kez taç şapkada kaldı. Sonra şapkayı arkasına sakladı ve annesinin yanına koştu. "Anne, gözlerini kapar mısın?" diye sordu Şakir. Kadriye gülümsedi ve gözlerini kapadı. Şakir şapkayı tacıyla birlikte annesinin başına yavaşça koydu. Kadriye gözlerini açtı ve tacı eliyle tuttu. "Teşekkür ederim, Şakir, ben çok şanslı bir anneyim!" dedi Kadriye.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben çok şanslı bir anneyim"
   - Cümle 11: «"Teşekkür ederim, Şakir, ben çok şanslı bir anneyim!" dedi Kadriye.»
   - Açıklama: 'Şanslı' soyut bir kavram; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'Şanslı' soyut bir kavram, 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0025` birebir aynı, `@degisim: piyano -> çiçek` (tutuyorsan), ardından `@onarim: bced2b791a4472e22741b1636bcd6d082ddf9aad`, sonra gövde.

### Hikâye 4: tohum sakir-0026 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0026
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'palmiye', fiil 'tutunmak', sıfat 'yeterli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: palmiyeler arasında rüzgar güçlü değildi | açık bir yere koşup ipi sıkıca tuttu
@tohum: sakir-0026
@degisim: yeterli -> güçlü
Şakir babası Remzi ile kumsalda ilk kez uçurtma uçuracaktı. Remzi ona mavi bir uçurtma verdi. Ama palmiyeler arasında rüzgar güçlü değildi ve uçurtma hep kuma düştü. Şakir macerayı çok severdi, bu yüzden uçurtma için yeni bir yer aradı. Etrafına baktı ve deniz kenarında açık bir yer gördü. Uçurtmayı aldı ve babasının eline tutunarak oraya koştu. Orada rüzgar daha güçlüydü. Şakir ipi iki eliyle sıkıca tuttu. Remzi de uçurtmayı havaya bıraktı. Mavi uçurtma hızla yükseldi ve ağaçların üstüne çıktı. Remzi sevinçle zıplayıp güldü. "Babacığım, ilk uçurtmam gökyüzünde uçuyor!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Şakir babası Remzi ile"
   - Cümle 1: «Şakir babası Remzi ile kumsalda ilk kez uçurtma uçuracaktı.»
   - Açıklama: 'Şakir' ile 'babası Remzi' arasında virgül olmalı; yoksa 'Şakir'in babası' diye okunuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden"
   - Cümle 4: «Şakir macerayı çok severdi, bu yüzden uçurtma için yeni bir yer aradı.»
   - Açıklama: Yeni yer araması maceracılıktan değil rüzgarın zayıflığından çıkmalı; kurulan sebep bağı yanlış.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden uçurtma için yeni bir yer aradı"
   - Cümle 4: «Şakir macerayı çok severdi, bu yüzden uçurtma için yeni bir yer aradı.»
   - Açıklama: Yeni yer arama sebebi zayıf rüzgar olmalıyken macera sevgisine bağlanıyor; sebep-sonuç bağı kopuk.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0026` birebir aynı, `@degisim: yeterli -> güçlü` (tutuyorsan), ardından `@onarim: 2ff5e81431f950b8aa89b55cc0dbe348050d5ca7`, sonra gövde.

### Hikâye 5: tohum sakir-0027 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0027
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: paylaşmak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'süpürge', fiil 'çözmek', sıfat 'sessiz'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: kardeşi kitabını unuttuğu için oynayacak bir şeyi yoktu | çantanın ipini çözdü ve ikinci küreği paylaştı
@tohum: sakir-0027
@degisim: süpürge -> kürek
Rüzgar hafif hafif esiyordu. Şakir kumsalda küreğiyle büyük bir kale yapıyordu. Kardeşi Canan kitabını evde unuttuğu için oynayacak bir şeyi yoktu. Canan kumun üstünde sessiz oturuyordu. Şakir'in oyuncak çantasında bir kürek daha vardı. Şakir çantanın ipini çözdü ve ikinci küreği çıkardı. "Canan, bu kürek senin olsun, gel bir macera oyunu oynayalım!" dedi Şakir. "Ne yapacağız?" diye sordu Canan. "Kalenin etrafına uzun bir yol kazalım!" dedi Şakir. Canan küreği aldı ve gülümsedi. İkisi yan yana kumu kazdı. Sonunda yol kalenin etrafını tam sardı. Şakir ile Canan, kalelerinin yanında mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir macera oyunu oynayalım"
   - Cümle 7: «"Canan, bu kürek senin olsun, gel bir macera oyunu oynayalım!" dedi Şakir.»
   - Açıklama: 'Macera' 3 yaşındaki çocuk için soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0027` birebir aynı, `@degisim: süpürge -> kürek` (tutuyorsan), ardından `@onarim: 191da27b60e30d5fe03d524c4bb82058fc3a8b9d`, sonra gövde.

### Hikâye 6: tohum sakir-0028 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0028
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tüy', fiil 'gülümsemek', sıfat 'eksik'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: kumdan pastanın mumu eksikti | şemsiyenin yanında beyaz bir tüy bulup pastaya dikti
@tohum: sakir-0028
Kumsalda Fil Necati büyük bir şemsiyenin altında uyuyordu. Şakir ona sürpriz olarak kumdan bir pasta yaptı ve üstüne kabuklar dizdi. Ama pastanın mumu eksikti ve kumsalda hiç mum yoktu. Şakir mum yerine uzun ve ince bir şey bulmak istedi. Macerayı çok severdi ve şemsiyenin çevresini bir hazine arar gibi gezdi. Sonunda kumun üstünde uzun, beyaz bir tüy buldu. Tüyü pastanın tam ortasına dikti. Şimdi pasta tamamdı. Biraz sonra Necati uyandı ve pastayı gördü. Hortumuyla tüye yavaşça dokundu ve gülümsedi. Şakir de sevinçle ellerini çırptı. Şakir bundan sonra bir şey eksik olunca önce etrafına dikkatle baktı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir hazine arar gibi"
   - Cümle 5: «Macerayı çok severdi ve şemsiyenin çevresini bir hazine arar gibi gezdi.»
   - Açıklama: Benzetme ve 'macera' gibi soyut kelime 3 yaşındaki çocuğa uygun değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok severdi ve şemsiyenin çevresini bir hazine arar gibi gezdi"
   - Cümle 5: «Macerayı çok severdi ve şemsiyenin çevresini bir hazine arar gibi gezdi.»
   - Açıklama: 'Macera' soyut bir kavram ve 'hazine arar gibi' benzetmesi küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0028` birebir aynı, ardından `@onarim: 0986b4d75459d1c82392a32aa8add6eecfc5e302`, sonra gövde.

### Hikâye 7: tohum sakir-0029 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Remzi
@tohum: sakir-0029
- yer: park (Şehirdeki park.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kek', fiil 'gezinmek', sıfat 'tuzlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | Remzi
@plan: rüzgar oyunun haritasını uçurdu | babasından sıcak soğuk demesini isteyip kutuyu buldu
@tohum: sakir-0029
@degisim: tuzlu -> sarı
Parkta Şakir ile babası Remzi bir macera oyunu oynuyordu. Remzi içinde kek olan sarı bir kutuyu saklamıştı. Bir de harita çizmişti. Ama rüzgar esti ve harita uçup gitti. Şakir hiç üzülmedi ve oyunu bırakmadı. "Baba, yaklaşınca 'sıcak', uzaklaşınca 'soğuk' der misin?" diye sordu Şakir. "Tamam, haydi başla!" dedi Remzi gülerek. Şakir parkta gezinmeye başladı. "Soğuk, çok soğuk!" dedi Remzi ve titriyormuş gibi yaptı. Şakir döndü ve banklara doğru yürüdü. "Sıcak, çok sıcak!" dedi Remzi. Şakir bankın altına baktı ve sarı kutuyu buldu. Sonra ikisi banka oturdu ve keki mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "sıcak soğuk demesini isteyip"
   - Cümle 0 (plan satırı): «rüzgar oyunun haritasını uçurdu | babasından sıcak soğuk demesini isteyip kutuyu buldu»
   - Açıklama: Söylenecek kelimeler tırnaksız ve virgülsüz yazılmış; 'sıcak', 'soğuk' biçiminde olmalı.
2. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "babasından sıcak soğuk demesini"
   - Cümle 0 (plan satırı): «rüzgar oyunun haritasını uçurdu | babasından sıcak soğuk demesini isteyip kutuyu buldu»
   - Açıklama: Aktarılan 'sıcak' ve 'soğuk' kelimeleri tırnak ya da virgülle ayrılmamış.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar esti ve harita uçup gitti"
   - Cümle 4: «Ama rüzgar esti ve harita uçup gitti.»
   - Açıklama: Sorun ilk üç cümlede değil, ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0029` birebir aynı, `@degisim: tuzlu -> sarı` (tutuyorsan), ardından `@onarim: 5264b745879ed4058a6daf24088879e7808db4bf`, sonra gövde.

### Hikâye 8: tohum sakir-0031 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Necati
@tohum: sakir-0031
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'patates', fiil 'göstermek', sıfat 'kırılgan'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Necati
@plan: fil ağır adımlarla küçük çiçeğe doğru geliyordu | fili durdurup çiçeğin etrafına taş dizdi
@tohum: sakir-0031
@degisim: patates -> çiçek
Bir sabah Şakir ile Fil Necati parkta yürüyordu. Şakir yolun ortasında küçük bir çiçek gördü. Çiçeğin sapı çok ince ve kırılgandı. Ama Necati ağır adımlarla tam çiçeğe doğru geliyordu. "Dur, Necati, sana bir çiçek göstermek istiyorum!" dedi Şakir. Necati durdu ve eğilip çiçeğe baktı. "Onu hiç görmemiştim," dedi Necati. Şakir çiçeği korumak istedi. Macera oyunlarında hep taşlarla yol yapardı. Hemen çalıların arasından dört büyük taş topladı. Taşları çiçeğin etrafına dizdi. Şimdi çiçek uzaktan kolayca görünüyordu. Necati ayak uçlarında yürüdü ve çiçeğin yanından dikkatle geçti. "Artık çiçeğe kimse basmaz, Necati!" dedi Şakir sevinçle.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sapı çok ince ve kırılgandı"
   - Cümle 3: «Çiçeğin sapı çok ince ve kırılgandı.»
   - Açıklama: 'Kırılgan' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Macera oyunlarında hep taşlarla yol yapardı"
   - Cümle 9: «Macera oyunlarında hep taşlarla yol yapardı.»
   - Açıklama: Taşlarla yol yapma alışkanlığı çiçeğin etrafına taş dizme çözümüne mantıkla bağlanmıyor, çözümü sebepsizce getiriyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Necati ayak uçlarında yürüdü"
   - Cümle 13: «Necati ayak uçlarında yürüdü ve çiçeğin yanından dikkatle geçti.»
   - Açıklama: Doğru kalıp 'parmak uçlarında yürüdü' olmalı; kelime yanlış kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0031` birebir aynı, `@degisim: patates -> çiçek` (tutuyorsan), ardından `@onarim: 28ab0889b5d1f01635b7692f2a76bc2bbafceb14`, sonra gövde.

### Hikâye 9: tohum sakir-0033 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0033
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'pota', fiil 'üflemek', sıfat 'ahşap'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: üflerken topun havası geri kaçıyordu | kardeşinden topun ağzını tutmasını istedi
@tohum: sakir-0033
@degisim: pota -> top
Kumsalda Şakir ile Canan ahşap oyuncak kutusunu açtı. İçinden havası inmiş mavi bir deniz topu çıktı. Şakir topa üfledi, ama nefes alırken hava hep geri kaçtı. Şakir macerayı çok severdi, bu yüzden hemen başka bir yol denedi. "Canan, ben nefes alırken topun ağzını tutar mısın?" diye sordu Şakir. "Tabii, tutarım," dedi Canan. Şakir yine üfledi. Şakir nefes alırken Canan topun ağzını parmağıyla kapattı. Böylece hava hiç kaçmadı. Top yavaş yavaş büyüdü ve yuvarlak oldu. Sonunda Şakir topun ağzını sıkıca kapattı. "Teşekkürler, Canan, şimdi birlikte oynayabiliriz!" dedi Şakir.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi, bu yüzden hemen başka bir yol denedi.»
   - Açıklama: 'Macera' soyut bir kavram ve olayla bağı kurulmadan kullanılmış.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden hemen başka bir yol denedi"
   - Cümle 4: «Şakir macerayı çok severdi, bu yüzden hemen başka bir yol denedi.»
   - Açıklama: Macera özelliği top şişirme çözümüne anlamsızca bağlanıyor, işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi, bu yüzden hemen başka bir yol denedi.»
   - Açıklama: Kartın özellikler alanındaki macera sayılarak söyleniyor, top şişirme çözümünde işe yarar biçimde kullanılmıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden hemen başka bir yol denedi"
   - Cümle 4: «Şakir macerayı çok severdi, bu yüzden hemen başka bir yol denedi.»
   - Açıklama: Maceraya düşkünlük yeni bir yol denemenin sebebi olarak olaydan çıkmıyor; bağlantı yapay.
5. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şakir yine üfledi. Şakir nefes alırken"
   - Cümle 8: «Şakir nefes alırken Canan topun ağzını parmağıyla kapattı.»
   - Açıklama: Art arda iki cümlede özne gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0033` birebir aynı, `@degisim: pota -> top` (tutuyorsan), ardından `@onarim: dfef3cfc4d62f724e6cce697ae43bf5b631e8d83`, sonra gövde.

### Hikâye 10: tohum sakir-0034 (deneme 3 -> 4)

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
@plan: uğur böcekleri soğuk tartıya ters düştü ve dönemedi | yaprak uzatıp böcekleri güneşe taşıdı
@tohum: sakir-0034
@degisim: şekerli -> yeşil
Şakir mutfakta kardeşi Canan ile birlikteydi. Şakir macerayı çok severdi, bu yüzden her köşeye dikkatle bakıyordu. Birden tartının üstünde ters dönmüş minik uğur böcekleri gördü. Böcekler pencerenin önündeki çiçekten uçmuştu ve soğuk tartıya düşmüştü. "Canan, onlara nasıl yardım ederiz?" diye sordu Şakir. "Onlara bir yaprak uzat, yaprağı tutarlar," dedi Canan. Şakir o çiçekten yeşil bir yaprak kopardı. Yaprağı böceklerin ayaklarına yavaşça yaklaştırdı. Böcekler yaprağa tutundu ve döndü. Şakir yaprağı güneşli pencerenin önüne koydu. Uğur böcekleri güneşte ısındı ve kanatlarını açtı. Sonra uçup yine çiçeğe kondular. "Teşekkürler, Canan, böcekleri birlikte kurtardık!" dedi Şakir.
```

**Hakem bulguları (3):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "ve soğuk tartıya düşmüştü"
   - Cümle 4: «Böcekler pencerenin önündeki çiçekten uçmuştu ve soğuk tartıya düşmüştü.»
   - Açıklama: Soğukta ters dönüp kalan böcekler sıkıntıda/üşümüş hayvan öğesi taşıyor.
2. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "soğuk tartıya düşmüştü"
   - Cümle 4: «Böcekler pencerenin önündeki çiçekten uçmuştu ve soğuk tartıya düşmüştü.»
   - Açıklama: Ters dönüp dönemeyen, soğukta kalan böcekler sıkıntı içinde bir hayvan tablosu çiziyor.
3. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Böcekler yaprağa tutundu ve döndü"
   - Cümle 9: «Böcekler yaprağa tutundu ve döndü.»
   - Açıklama: Arka planda kalması gereken çoğul canlılar (uğur böcekleri) olayın merkezinde yer alıyor.
   - Açıklama: Notlanan çoğul canlı uğur böcekleri arka planda kalmıyor, olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0034` birebir aynı, `@degisim: şekerli -> yeşil` (tutuyorsan), ardından `@onarim: 373722a70d7ed64b2cfff3664ebfedc432fa06c0`, sonra gövde.

### Hikâye 11: tohum sakir-0035 (deneme 3 -> 4)

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
@plan: filin kaleminin mürekkebi birden bitti | kalemini paylaştı ve ikisi sırayla çizdi
@tohum: sakir-0035
@degisim: bağlamak -> paylaşmak
Şakir, Necati ile kamp yerinde bir orman haritası çiziyordu. Necati büyük ağaçları çizecekti. Ama Necati'nin kaleminin mürekkebi birden bitti. Necati üzgün bir yüzle kalemine baktı. "Kalemim artık çizmiyor," dedi Necati. Şakir macerayı çok severdi ve harita bitince ormanı gezmek istiyordu. Şakir'in tek bir kırmızı kalemi vardı. Şakir bu kalemi hemen Necati'ye uzattı. "Kalemimi seninle paylaşırım, sırayla çizelim," dedi Şakir. Önce Necati ağaçları çizdi. Sonra Şakir çadırı ve yolu çizdi. Harita bitince Şakir ile Necati onu alıp kamp yerini mutlu mutlu gezdi.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "filin kaleminin mürekkebi birden bitti"
   - Cümle 0 (plan satırı): «filin kaleminin mürekkebi birden bitti | kalemini paylaştı ve ikisi sırayla çizdi»
   - Açıklama: Plan kalemin bir filin olduğunu söylüyor ama gövdede fil yok, kalem Necati'nin.
   - Açıklama: Plan bir filden söz ediyor ama gövdede fil yok, kalemi biten Necati.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 6: «Şakir macerayı çok severdi ve harita bitince ormanı gezmek istiyordu.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuk için uygun değil.
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve harita bitince ormanı gezmek istiyordu"
   - Cümle 6: «Şakir macerayı çok severdi ve harita bitince ormanı gezmek istiyordu.»
   - Açıklama: Tohumdaki macera özelliği sorunun çözümüne hiç katkı vermiyor, yalnız süs olarak anılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0035` birebir aynı, `@degisim: bağlamak -> paylaşmak` (tutuyorsan), ardından `@onarim: 904ab0bc76a0d3420588f21276d4a3705ab85358`, sonra gövde.

### Hikâye 12: tohum sakir-0036 (deneme 3 -> 4)

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
Kumsalda kum çok sıcaktı. Şakir şapkasını ters çevirip kuma koydu. Şakir ile annesi Kadriye şapkaya kabuk atıp yarışıyordu. Ama ikisi aynı anda attı ve hangi kabuğun kimin olduğunu bilemediler. "Anne, sırayla atalım mı?" diye sordu Şakir. "Olur, önce sen at," dedi Kadriye. Şakir bir kabuk attı ve kabuk şapkaya girdi. Sonra Kadriye attı ama onun kabuğu kuma düştü. Her seferinde kabukları birlikte saydılar. Sonunda Kadriye'nin bir kabuğu daha fazlaydı. Şakir yarışı kaybetti ama güldü. "Tebrikler, anneciğim, sen kazandın!" dedi Şakir. Şakir yine de çok sevindi, çünkü sırayla oynayınca kabuklar hiç karışmamıştı.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama ikisi aynı anda attı"
   - Cümle 4: «Ama ikisi aynı anda attı ve hangi kabuğun kimin olduğunu bilemediler.»
   - Açıklama: Sorun ilk 3 cümlede değil ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0036` birebir aynı, `@degisim: mobilya -> kabuk` (tutuyorsan), ardından `@onarim: c10f295543005cff9f313079b380ee61074e6009`, sonra gövde.
