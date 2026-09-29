# Editör görevi (onarım): Şakir, onarım partisi 5

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 8 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar5.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar5.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0001 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Remzi
@tohum: sakir-0001
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'bilye', fiil 'incelemek', sıfat 'kocaman'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | ev | Remzi
@plan: bilye dolabın altına girdi ve babasının kolu sığmadı | yere uzanıp küçük eliyle bilyeyi dışarı çekti
@tohum: sakir-0001
Şakir babasıyla salonda bilye oynuyordu. Remzi'nin kocaman mavi bilyesi yuvarlandı ve dolabın altına girdi. Remzi eğildi ama kalın kolu oraya sığmadı. "Bilyemi alamıyorum, Şakir," dedi Remzi. "Ben alırım, baba," dedi Şakir. Macerayı çok seven Şakir hemen yere uzandı. Dolabın altını dikkatle inceledi. Mavi bilye en arkada duruyordu. Şakir'in küçük eli içeri rahatça girdi. Bilyeyi parmaklarıyla tuttu ve yavaşça dışarı çekti. Sonra onu babasına verdi. Remzi sevinçle güldü ve Şakir'e sarıldı. "Teşekkürler, Şakir, şimdi oyunumuza devam edelim!" dedi Remzi.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Remzi'nin kocaman mavi bilyesi"
   - Cümle 2: «Remzi'nin kocaman mavi bilyesi yuvarlandı ve dolabın altına girdi.»
   - Açıklama: Remzi adı, babanın adı olduğu söylenmeden birden kullanılıyor; çocuk Remzi'nin kim olduğunu bilemiyor.
   - Açıklama: Remzi'nin baba olduğu söylenmeden ad birden kullanılıyor; kimi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0001` birebir aynı, ardından `@onarim: 14391fc33f3e32a273a334ea3167f51775252cd4`, sonra gövde.

### Hikâye 2: tohum sakir-0002 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0002
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'terazi', fiil 'kurtulmak', sıfat 'yemyeşil'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: dalgalar yeşil bir kabuğu kumun altında bırakmıştı | kumu elleriyle yavaşça kazıp kabuğu çıkardı
@tohum: sakir-0002
@degisim: terazi -> kabuk
Bir sabah Şakir kumsalda yürüyordu. Suyun kenarında yemyeşil bir şey fark etti. Bu, dalgaların kuma gömdüğü bir deniz kabuğuydu. Kabuğun yalnız ucu görünüyordu. Macerayı çok seven Şakir kabuğu çıkarmak istedi. Hemen kabuğun yanına oturdu. Kumu elleriyle yavaş yavaş kazdı. Kabuğu kırmamak için çok dikkat etti. Sonunda kabuk kumdan kurtuldu. Şakir onu avucuna aldı ve hafifçe üfledi. Kabuk güneşin altında pırıl pırıl parladı. Şakir çok sevindi, çünkü güzel kabuğu bulup çıkarmıştı.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Bir sabah Şakir kumsalda yürüyordu"
   - Cümle 1: «Bir sabah Şakir kumsalda yürüyordu.»
   - Açıklama: Güvenli kullanım satırına göre Şakir tek başına uzağa gitmez; burada yavru Şakir yanında büyük olmadan su kenarında tek başına dolaşıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bu, dalgaların kuma gömdüğü bir deniz kabuğuydu"
   - Cümle 3: «Bu, dalgaların kuma gömdüğü bir deniz kabuğuydu.»
   - Açıklama: Kumdaki bir kabuğu çıkarmak gerçek bir sorun değil, önemsiz bir istek.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Macerayı çok seven Şakir"
   - Cümle 5: «Macerayı çok seven Şakir kabuğu çıkarmak istedi.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0002` birebir aynı, `@degisim: terazi -> kabuk` (tutuyorsan), ardından `@onarim: 3bc2c6a25aacec46965c6776613f46bd5c9653ab`, sonra gövde.

### Hikâye 3: tohum sakir-0003 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0003
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: bir şey yapmak
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kütük', fiil 'duymak', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: kutunun içi kağıtla dolu olduğu için ses çok azdı | kağıtları çıkarıp kapağı kapattı ve yeniden vurdu
@tohum: sakir-0003
@degisim: kütük -> kutu
Şakir macera oyunu için eski bir ayakkabı kutusundan davul yapmak istedi. Kutuya eliyle vurdu ama sesi zor duydu. Kutunun içi kağıtlarla dolu olduğu için ses çok azdı. Şakir kağıtları tek tek çıkardı ve bir kenara koydu. Sonra kapağı sıkıca kapattı. Davuluna yeniden vurdu. Bu kez yüksek ve güzel bir ses çıktı. Şakir masasından iki kalem aldı. Onlarla davulu hızlı hızlı çaldı. Şakir bu sesi çok beğendi ve güldü. Sonra yeni davuluyla oyununa mutlu mutlu başladı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "macera oyunu için eski"
   - Cümle 1: «Şakir macera oyunu için eski bir ayakkabı kutusundan davul yapmak istedi.»
   - Açıklama: Tohumdaki macera özelliği yalnız oyunun adı olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "olduğu için ses çok azdı"
   - Cümle 3: «Kutunun içi kağıtlarla dolu olduğu için ses çok azdı.»
   - Açıklama: Ses 'az' olmaz; 'ses çok kısıktı' gibi bir kelime gerekir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0003` birebir aynı, `@degisim: kütük -> kutu` (tutuyorsan), ardından `@onarim: 8d5c6aa9b98c1d573f8e92b7465fed7e08209c4f`, sonra gövde.

### Hikâye 4: tohum sakir-0006 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0006
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'alet', fiil 'yapışmak', sıfat 'sadık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: kum çok kuruydu ve kule hep yıkıldı | şapkasını ıslak kumla doldurup kalenin üstüne ters çevirdi
@tohum: sakir-0006
@degisim: sadık -> ıslak
Rüzgar esiyordu ve Şakir kumsalda Fil Necati ile kale yapıyordu. Necati küçük bir kürekle kalenin üstüne kule yapıyordu. Ama kum çok kuruydu ve kule hep yıkılıyordu. "Bu aletle kule hiç durmuyor," dedi Necati üzgün üzgün. Şakir su kenarındaki kumun ıslak olduğunu gördü. Şapkasını çıkardı ve o kumla doldurdu. Sonra onu kalenin üstüne ters çevirdi. Ardından şapkayı yavaşça yukarı kaldırdı. Kum birbirine yapışmıştı ve kule sağlam durdu. "Kule tıpkı şapkana benziyor, Şakir!" dedi Necati sevinçle. Şakir ile Necati ıslak kumla yapılan kulenin yıkılmadığını öğrendi.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Bu aletle kule hiç durmuyor"
   - Cümle 4: «"Bu aletle kule hiç durmuyor," dedi Necati üzgün üzgün.»
   - Açıklama: Sorunun sebebi kuru kum iken Necati suçu alete atıyor ve bu sebep sonra hiç düzeltilmiyor.
   - Açıklama: Sebep kuru kum olarak verilmişken Necati suçu alete yüklüyor ve bu düzeltilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0006` birebir aynı, `@degisim: sadık -> ıslak` (tutuyorsan), ardından `@onarim: 2ca0012d274f1c40e66f325496d75e72cd4166ae`, sonra gövde.

### Hikâye 5: tohum sakir-0007 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0007
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: kaybolan eşya
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'silgi', fiil 'yorulmak', sıfat 'sağlam'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: silgi elinden kaydı ve kayboldu | koltuğun altına ve yastıkların arasına baktı
@tohum: sakir-0007
@degisim: sağlam -> yumuşak
Salonda Şakir koltukta oturmuş, resim yapıyordu. Silgisi birden elinden kaydı ve kayboldu. Şakir kağıttaki fazla bir çizgiyi silmek istiyordu. Önce yere eğildi ve koltuğun altına baktı ama silgi orada yoktu. Şakir macerayı çok sevdiği için hiç yorulmadan aramaya devam etti. Yumuşak yastıkları tek tek kaldırdı. Silgi iki yastığın arasına düşmüştü! Şakir silgiyi aldı ve fazla çizgiyi hemen sildi. Resmi yine tertemiz oldu. Şakir çok sevindi, çünkü kayıp silgisini kendisi bulmuştu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok sevdiği"
   - Cümle 5: «Şakir macerayı çok sevdiği için hiç yorulmadan aramaya devam etti.»
   - Açıklama: 'Macera' soyut bir kavram ve silgi aramakla ilgisi 3 yaşındaki çocuğa anlaşılır değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok sevdiği için"
   - Cümle 5: «Şakir macerayı çok sevdiği için hiç yorulmadan aramaya devam etti.»
   - Açıklama: 'Macera' soyut bir kavram ve silgi aramaya uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0007` birebir aynı, `@degisim: sağlam -> yumuşak` (tutuyorsan), ardından `@onarim: 9d92943e501c279ed6d74e2b225c2e72b1abd50f`, sonra gövde.

### Hikâye 6: tohum sakir-0009 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | -
@tohum: sakir-0009
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'jöle', fiil 'kurulanmak', sıfat 'boyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | -
@plan: oyun için taç gerekiyordu ama evde taç yoktu | kağıdı sarıya boyayıp şapkasının çevresine sardı
@tohum: sakir-0009
@degisim: jöle -> kağıt
Evde Şakir ormanın en büyük aslanı olma oyunu oynamak istedi. Bunun için başına takacak bir taç gerekiyordu ama evde hiç taç yoktu. Şakir biraz düşündü ve şapkasına baktı. Masadan uzun bir kağıt ve sarı boya aldı. Kağıdı baştan sona sarıya boyadı. Ellerine de boya bulaştı. Şapkası kirlenmesin diye ellerini yıkadı ve kurulandı. Şapkasını aldı ve boyalı kağıdı onun çevresine sardı. Şapka artık sarı bir taç gibi olmuştu. Sonra şapkayı başına taktı ve aynaya baktı. Koltuğa oturdu ve oyununu mutlu mutlu oynadı. Şakir kağıt ve boyayla kendi tacını yapabileceğini öğrendi.
```

**Hakem bulguları (4):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Ellerine de boya bulaştı"
   - Cümle 6: «Ellerine de boya bulaştı.»
   - Açıklama: Ellere boya bulaşıp yıkanması çözüme bir şey katmayan araya girmiş işlevsiz bir ayrıntı.
   - Açıklama: Ellere bulaşan boya ve el yıkama çözüme hiçbir şey katmayan işlevsiz bir ara olay.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "ellerini yıkadı ve kurulandı"
   - Cümle 7: «Şapkası kirlenmesin diye ellerini yıkadı ve kurulandı.»
   - Açıklama: Eller için dönüşlü 'kurulandı' değil 'kuruladı' olmalı.
   - Açıklama: 'Kurulandı' dönüşlü fiil ellere uymuyor; 'ellerini kuruladı' olmalı.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Şapkası kirlenmesin diye ellerini yıkadı ve kurulandı"
   - Cümle 7: «Şapkası kirlenmesin diye ellerini yıkadı ve kurulandı.»
   - Açıklama: Çözüm boyama, el yıkama ve sarma gibi ikiden fazla adıma yayılıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Koltuğa oturdu ve oyununu mutlu mutlu oynadı"
   - Cümle 11: «Koltuğa oturdu ve oyununu mutlu mutlu oynadı.»
   - Açıklama: Kaybolduğu söylenen koltuğa hiçbir açıklama olmadan oturuluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0009` birebir aynı, `@degisim: jöle -> kağıt` (tutuyorsan), ardından `@onarim: 07e0d486fffb0a499c5dc8f1222fb7ca3de96b2e`, sonra gövde.

### Hikâye 7: tohum sakir-0011 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0011
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'anahtar', fiil 'yumuşamak', sıfat 'limonlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: rüzgarda kumsaldan ince bir ıslık sesi geliyordu | şapkasıyla kabuğu kapatıp sesin kabuktan geldiğini buldu
@tohum: sakir-0011
@degisim: limonlu -> beyaz
Rüzgar hafif hafif esiyordu. Kumsalda yürüyen Şakir ince bir ıslık sesi duydu. Şakir sesin nereden geldiğini çok merak etti. Sesin geldiği yere doğru yavaşça yürüdü. Kumda büyük, beyaz bir deniz kabuğu buldu. Kabuğun ucunda anahtar deliği gibi küçük bir delik vardı. Şakir şapkasını kabuğun üstüne koydu ve ses hemen kesildi. Onu kaldırınca ses yine başladı. Rüzgar deliğe girince kabuk ıslık çalıyordu. Az sonra rüzgar azaldı ve ıslık sesi de yumuşadı. Şakir güldü ve kabuğu yanına aldı. Sonra onu rüzgara doğru tuttu ve mutlu mutlu oynadı.
```

**Hakem bulguları (5):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şakir sesin nereden geldiğini çok merak etti"
   - Cümle 3: «Şakir sesin nereden geldiğini çok merak etti.»
   - Açıklama: Islık sesi yalnız bir merak konusu; çocuğun önemseyeceği gerçek bir sorun yok.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu kaldırınca ses"
   - Cümle 8: «Onu kaldırınca ses yine başladı.»
   - Açıklama: 'Onu' zamirinin şapkayı mı kabuğu mu gösterdiği belirsiz.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Onu kaldırınca ses yine"
   - Cümle 8: «Onu kaldırınca ses yine başladı.»
   - Açıklama: 'Onu' şapkayı mı kabuğu mu gösteriyor belli değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kabuk ıslık çalıyordu"
   - Cümle 9: «Rüzgar deliğe girince kabuk ıslık çalıyordu.»
   - Açıklama: Kabuk ıslık çalamaz; mecazlı anlatım.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Az sonra rüzgar azaldı ve ıslık sesi de yumuşadı"
   - Cümle 10: «Az sonra rüzgar azaldı ve ıslık sesi de yumuşadı.»
   - Açıklama: Rüzgarın azalması olaya hiçbir şey katmayan işlevsiz bir ayrıntı.
   - Açıklama: Rüzgarın azalması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0011` birebir aynı, `@degisim: limonlu -> beyaz` (tutuyorsan), ardından `@onarim: d79e92e36aacad59fdb90860a78c39f3e3f95793`, sonra gövde.

### Hikâye 8: tohum sakir-0014 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0014
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kök', fiil 'tatmak', sıfat 'yuvarlak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: güneş ilk kez yiyeceği karpuzu ısıtmıştı | kabı ıslak kuma gömüp şapkasıyla gölge yaptı
@tohum: sakir-0014
@degisim: kök -> karpuz
Şakir kumsalda ilk kez karpuz yiyecekti. Yuvarlak kabın içinde kırmızı karpuz dilimleri vardı. Ama güneş kabı çok ısıtmıştı ve karpuz ılık olmuştu. Şakir kabı suyun kenarına götürdü. Orada kum ıslak ve serindi. Şakir kabı ıslak kuma yarıya kadar gömdü. Sonra şapkasını kabın üstüne koydu ve gölge yaptı. Şakir yanına oturdu ve biraz bekledi. Az sonra kap serinledi. Şakir bir dilim aldı ve tattı. Karpuz serin ve çok tatlıydı. Şakir bütün dilimleri mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "güneş ilk kez yiyeceği karpuzu"
   - Cümle 0 (plan satırı): «güneş ilk kez yiyeceği karpuzu ısıtmıştı | kabı ıslak kuma gömüp şapkasıyla gölge yaptı»
   - Açıklama: Plan satırında karpuzu kimin yiyeceği belli değil; cümle güneş yiyecekmiş gibi okunuyor.
   - Açıklama: 'Yiyeceği' kimin yiyeceğini göstermiyor; cümlede tek özne güneş.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir kumsalda ilk kez karpuz yiyecekti"
   - Cümle 1: «Şakir kumsalda ilk kez karpuz yiyecekti.»
   - Açıklama: Karpuzu ilk kez yemesi önemliymiş gibi kuruluyor ama hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0014` birebir aynı, `@degisim: kök -> karpuz` (tutuyorsan), ardından `@onarim: ae9cbb89c730dd8863ae615971c7622ef638153c`, sonra gövde.
