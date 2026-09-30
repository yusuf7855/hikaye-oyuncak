# Editör görevi (onarım): Şakir, onarım partisi 39

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar39.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar39.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0170 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0170
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'düğme', fiil 'taşınmak', sıfat 'kıpkırmızı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: düğmeyi arkasına sakladı ama kardeşi onu hemen gördü | düğmeyi şapkasının içine koyup başına taktı
@tohum: sakir-0170
@degisim: taşınmak -> saklamak
Kuşlar ağaçlarda ötüyordu. Şakir kamp yerinde Canan'a bir sihir oyunu gösteriyordu. Kıpkırmızı bir düğmeyi arkasına sakladı ama Canan onu hemen gördü. "Düğme arkanda, Şakir!" dedi Canan ve güldü. Şakir biraz düşündü. "Gözlerini kapat, Canan," dedi Şakir. Sonra şapkasını çıkardı, düğmeyi içine koydu ve onu yine başına taktı. Canan gözlerini açtı ve Şakir boş ellerini gösterdi. "Düğme yok oldu!" dedi Şakir. Canan her yere baktı ama düğmeyi bulamadı. Sonra Şakir başını eğdi ve düğme Canan'ın önüne düştü. Canan şaşırdı ve ellerini çırptı. İkisi sihir oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "onu yine başına taktı"
   - Cümle 7: «Sonra şapkasını çıkardı, düğmeyi içine koydu ve onu yine başına taktı.»
   - Açıklama: Son anılan nesne düğme olduğundan 'onu' zamirinin şapkayı mı düğmeyi mi gösterdiği belirsiz.
   - Açıklama: 'Onu' zamiri düğmeyi mi şapkayı mı gösteriyor belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0170` birebir aynı, `@degisim: taşınmak -> saklamak` (tutuyorsan), ardından `@onarim: 2a56864da39939746f4c407142fbd795a5875bb7`, sonra gövde.

### Hikâye 2: tohum sakir-0173 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0173
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'baloncuk', fiil 'özlemek', sıfat 'parlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: güneş çok parlaktı ve baloncukların nereden geldiği görünmedi | şapkasını gözlerinin üstüne çekti ve kardeşini buldu
@tohum: sakir-0173
@degisim: özlemek -> üflemek
Şakir kumsalda kumdan bir kale yapıyordu. Birden havada küçük baloncuklar uçuştu. Şakir baloncukların nereden geldiğini merak etti ama güneş çok parlaktı. Şakir o yana baktı ama hiçbir şey göremedi. Sonra şapkasını gözlerinin üstüne biraz çekti. Şimdi her şeyi daha iyi görüyordu. Bir kayanın arkasında beyaz bir kuyruk vardı. Şakir kayaya doğru koştu. Canan orada oturmuş, elindeki şişeyle baloncuk üflüyordu. "Canan, baloncuklar senden mi geliyor?" diye sordu Şakir. "Evet, sen de dener misin?" dedi Canan. Şakir üfledi ve kocaman bir baloncuk yaptı. "Bu oyun çok güzel, Canan!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şakir o yana baktı"
   - Cümle 4: «Şakir o yana baktı ama hiçbir şey göremedi.»
   - Açıklama: 'O yana' ile hangi yönün kastedildiği belli değil.
   - Açıklama: 'o yana' hangi yanı gösterdiği belli değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "beyaz bir kuyruk vardı"
   - Cümle 7: «Bir kayanın arkasında beyaz bir kuyruk vardı.»
   - Açıklama: Kayanın arkasında görülen beyaz kuyruk Canan'a bağlanmıyor ve sebepsiz beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0173` birebir aynı, `@degisim: özlemek -> üflemek` (tutuyorsan), ardından `@onarim: dcdc3e3fcdaec47a6ce9b6a33e6284f35701d181`, sonra gövde.

### Hikâye 3: tohum sakir-0174 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0174
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yapboz', fiil 'ayırmak', sıfat 'meşgul'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: kutular devrildi ve iki yapbozun parçaları karıştı | mavi parçaları şapkasına koyup ayırdı
@tohum: sakir-0174
Şakir kamp yerinde bir masaya doğru yürüdü. Fil Necati orada çok meşguldü. Kutular devrilmiş ve iki yapbozun parçaları birbirine karışmıştı. "Mavi parçalar deniz resminin, yeşil parçalar orman resminin," dedi Necati. "Sana yardım ederim, Necati," dedi Şakir. Şakir şapkasını çıkardı ve masaya koydu. Mavi parçaları tek tek içine attı. Yeşil parçalar masada kaldı. Böylece Şakir iki yapbozu kolayca ayırdı. Necati önce orman resmini, sonra deniz resmini bitirdi. "Teşekkürler, Şakir, çok iyi bir fikir!" dedi Necati. Şakir çok mutlu oldu, çünkü Necati'nin iki resmi de bitmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "orada çok meşguldü"
   - Cümle 2: «Fil Necati orada çok meşguldü.»
   - Açıklama: 'Meşgul' soyut ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Meşgul' 3 yaşındaki çocuğun bilmediği bir kelime.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "tek tek içine attı"
   - Cümle 7: «Mavi parçaları tek tek içine attı.»
   - Açıklama: 'İçine' son geçen masayı da gösterebilir; şapka olduğu belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0174` birebir aynı, ardından `@onarim: a611862de6af01df4f82497b0b9efc438a0533e6`, sonra gövde.

### Hikâye 4: tohum sakir-0183 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0183
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: kaybolan eşya
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'çörek', fiil 'boşalmak', sıfat 'heyecanlı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: küçük kürek dolu çantanın içinde görünmüyordu | çantayı şapkasının içine ters çevirip küreği buldu
@tohum: sakir-0183
Bir sabah Şakir ile Canan kumsala geldi. Şakir çok heyecanlıydı, çünkü kumdan kale yapacaktı. Ama küçük küreği dolu çantanın içinde görünmüyordu. Çantada havlu, kitap ve çörekler vardı. "Çantayı kuma dökme, çörekler kumlu olur," dedi Canan. Şakir bir an durdu. Sonra şapkasını çıkardı ve çantayı onun içine ters çevirdi. Çanta yavaş yavaş boşaldı. Küçük kürek de şapkanın içine düştü. "Buldum, Canan!" dedi Şakir. Şakir çörekleri yine çantaya koydu. Sonra ikisi mutlu mutlu kumdan büyük bir kale yaptı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "küçük küreği dolu çantanın içinde görünmüyordu"
   - Cümle 3: «Ama küçük küreği dolu çantanın içinde görünmüyordu.»
   - Açıklama: Küreğin çantada görünmemesi elini sokup aramakla biten önemsiz bir sorun.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0183` birebir aynı, ardından `@onarim: 4794a43c915e07b004e7fc5ed1f724fa4ec71b90`, sonra gövde.

### Hikâye 5: tohum sakir-0184 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Kadriye
@tohum: sakir-0184
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'top', fiil 'tamamlamak', sıfat 'çamurlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Kadriye
@plan: küçük bir kedi kaygan bir çukurdan çıkamıyordu | şapkasını çukura uzatıp kediyi yukarı kaldırdı
@tohum: sakir-0184
Şakir kamp yerinde annesiyle top oynarken bir miyav sesi duydu. Küçük bir kedi çamurlu bir çukura düşmüştü. Çukurun kenarı kaygandı ve kedi dışarı çıkamıyordu. "Anne, kedi çıkamıyor!" dedi Şakir. Kadriye çukura baktı. "Kedi çok aşağıda, Şakir," dedi Kadriye. Şakir şapkasını çıkardı, kenarından tuttu ve çukura uzattı. Kedi hemen şapkanın içine girdi. Şakir onu yavaşça yukarı kaldırdı ve kediyi yere bıraktı. Kedi hemen topa doğru koştu. Sonra Şakir, annesi ve kedi top oyununu mutlu mutlu tamamladı.
```

**Hakem bulguları (6):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Küçük bir kedi çamurlu bir çukura düşmüştü"
   - Cümle 2: «Küçük bir kedi çamurlu bir çukura düşmüştü.»
   - Açıklama: Başlığın Yan alanında yalnız Kadriye var; olaya katılan küçük kedi başlıkta ve kartın yanlar alanında yok.
   - Açıklama: Başlıktaki Yan alanında ve kartın 'yanlar' bölümünde olmayan bir kedi olaya katılıyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kadriye çukura baktı"
   - Cümle 5: «Kadriye çukura baktı.»
   - Açıklama: Kadriye'nin Şakir'in annesi olduğu söylenmeden adıyla anılıyor; kimi gösterdiği belli değil.
   - Açıklama: Kadriye adı 'annesi' ile bağlanmadan geliyor; kim olduğu açıkça belli değil.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir şapkasını çıkardı, kenarından tuttu ve çukura uzattı"
   - Cümle 7: «Şakir şapkasını çıkardı, kenarından tuttu ve çukura uzattı.»
   - Açıklama: Çocuğun taklit edebileceği biçimde kaygan bir çukurun kenarından içeri uzanılıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "kenarından tuttu ve çukura uzattı"
   - Cümle 7: «Şakir şapkasını çıkardı, kenarından tuttu ve çukura uzattı.»
   - Açıklama: Çocuğun kaygan bir çukurun kenarına eğilip hayvan kurtarmaya çalışması taklit edilince tehlikelidir.
5. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Şakir onu yavaşça yukarı"
   - Cümle 9: «Şakir onu yavaşça yukarı kaldırdı ve kediyi yere bıraktı.»
   - Açıklama: 'Onu' zamirinin şapkayı mı kediyi mi gösterdiği belli değil.
6. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Sonra Şakir, annesi ve kedi top oyununu"
   - Cümle 11: «Sonra Şakir, annesi ve kedi top oyununu mutlu mutlu tamamladı.»
   - Açıklama: Kartın yanlar alanında olmayan bir kedi karakteri oyuna katılıyor; kart kapalı dünyasına aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0184` birebir aynı, ardından `@onarim: 8a966c11306048ff7d0a9a6399aebce7eac6d2c2`, sonra gövde.

### Hikâye 6: tohum sakir-0187 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0187
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sırayla oynamak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'papatya', fiil 'güldürmek', sıfat 'kabarık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: ikisi aynı anda konuşunca kimse kimseyi duymadı | şapka kimde olursa sıranın onda olduğunu söyledi
@tohum: sakir-0187
Rüzgar esiyordu ve havada kabarık bulutlar vardı. Şakir ile Fil Necati kamp yerinde komik bir oyun oynuyordu. Ama ikisi aynı anda konuştu ve kimse kimseyi duymadı. Şakir şapkasını çıkardı ve Necati'ye uzattı. "Şapka sende olunca sıra sende, Necati," dedi Şakir. Necati şapkayı kocaman başına taktı. Sonra bir papatya ile Şakir'in burnunu gıdıkladı. Şakir çok güldü. Sonra Necati şapkayı Şakir'e geri verdi. Şakir komik bir aslan yüzü yaptı ve Necati'yi güldürdü. Necati hortumunu salladı ve kahkaha attı. Şakir çok sevindi, çünkü sırayla oynadıkları için ikisi de çok eğlenmişti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Sonra bir papatya ile Şakir'in burnunu gıdıkladı"
   - Cümle 7: «Sonra bir papatya ile Şakir'in burnunu gıdıkladı.»
   - Açıklama: Sorun aynı anda konuşmak iken sıra konuşmaya değil sebepsiz beliren papatyayla gıdıklamaya geçiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir papatya ile Şakir'in burnunu"
   - Cümle 7: «Sonra bir papatya ile Şakir'in burnunu gıdıkladı.»
   - Açıklama: Papatya sebepsiz beliriyor ve sıra kuralı konuşmaya yönelikken oyun gıdıklamaya kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0187` birebir aynı, ardından `@onarim: 85194eebfc9cc244e65a65f06f5b107cefe0e26f`, sonra gövde.

### Hikâye 7: tohum sakir-0188 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0188
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sırayla oynamak
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'jelibon', fiil 'yavaşlamak', sıfat 'çalışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: tek kaşık vardı ve ikisi de önce başlamak istedi | şapkasına bir uzun bir kısa dal koydu
@tohum: sakir-0188
@degisim: jelibon -> şeker
Şakir kamp yerinde babası Remzi ile bir kaşık oyunu oynuyordu. Kaşığın içine bir şeker koyup ağaca kadar yürüyeceklerdi. Ama tek bir kaşık vardı ve ikisi de önce başlamak istedi. "Önce ben!" dedi Remzi. Şakir şapkasını çıkardı ve içine bir uzun, bir kısa dal koydu. "Uzun dalı çeken önce başlar, baba," dedi Şakir. Remzi kısa dalı çekti ve güldü. Önce Şakir kaşığı aldı ve ağaca kadar yavaş yavaş yürüdü. Sonra kaşığı babasına verdi. Remzi önce hızlı yürüdü, sonra yoldaki çalışkan karıncaları görünce yavaşladı. İkisi sırayla oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Remzi önce hızlı yürüdü"
   - Cümle 10: «Remzi önce hızlı yürüdü, sonra yoldaki çalışkan karıncaları görünce yavaşladı.»
   - Açıklama: 'Önce' kelimesi hikayede beş kez tekrarlanıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "yoldaki çalışkan karıncaları görünce yavaşladı"
   - Cümle 10: «Remzi önce hızlı yürüdü, sonra yoldaki çalışkan karıncaları görünce yavaşladı.»
   - Açıklama: Karıncalar sebepsiz beliriyor ve olayda işlevi yok.
   - Açıklama: Karıncalar sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0188` birebir aynı, `@degisim: jelibon -> şeker` (tutuyorsan), ardından `@onarim: b2c61fa66744b8ef3957c241bb089eae5cf2ea9f`, sonra gövde.

### Hikâye 8: tohum sakir-0189 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0189
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ekmek', fiil 'sığmak', sıfat 'hafif'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: hafif tüy rüzgarla uçuyor ve elinden kaçıyordu | şapkasını tüyün altında tuttu ve tüy içine düştü
@tohum: sakir-0189
@degisim: ekmek -> tüy
Şakir annesi Kadriye ile kumsalda yürürken havada bembeyaz bir tüy gördü. Şakir tüyü yakalamak istedi ama tüy hep elinden kaçtı. Tüy çok hafifti ve rüzgarla bir yukarı, bir aşağı uçuyordu. "Anne, bu tüyü yakalayamıyorum!" dedi Şakir. Sonra Şakir şapkasını çıkardı ve tüyün altında tuttu. Tüy yavaşça aşağı indi ve şapkanın içine düştü. Şakir tüyü annesine verdi. Kadriye tüyü çantasına koydu, uzun tüy oraya tam sığdı. "Teşekkürler, Şakir, bu çok güzel bir hediye," dedi Kadriye. Şakir çok sevindi, çünkü tüyü sonunda yakalamıştı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "uzun tüy oraya tam sığdı"
   - Cümle 8: «Kadriye tüyü çantasına koydu, uzun tüy oraya tam sığdı.»
   - Açıklama: Tüyün çantaya tam sığması hiçbir işe yaramayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0189` birebir aynı, `@degisim: ekmek -> tüy` (tutuyorsan), ardından `@onarim: 4a51a7964fb79758246634e445ec5db490cb985d`, sonra gövde.

### Hikâye 9: tohum sakir-0192 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0192
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'sucuk', fiil 'taramak', sıfat 'faydalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: güneş çok parlaktı ve hazinenin yanındaki dal görünmedi | şapkasını gözlerinin üstüne çekti ve kumsalı taradı
@tohum: sakir-0192
@degisim: faydalı -> parlak
Bir sabah Şakir kumsalda babasıyla hazine oyunu oynuyordu. Babası hazineyi kuma gömmüş ve yanına bir dal dikmişti. Ama güneş çok parlaktı ve Şakir dalı göremedi. "Hazine seni bekliyor, Şakir!" dedi Remzi. Şakir şapkasını gözlerinin üstüne indirdi. Artık gözleri gölgede kaldı. Şakir bütün kumsalı yavaş yavaş taradı. Sonunda kumsalın ucunda küçük dalı gördü. Hemen oraya koştu ve dalın dibini kazdı. Kumun altından bir kutu çıktı. Kutunun içinde iki sucuklu ekmek vardı. "Hazineyi buldum, baba!" dedi Şakir. İkisi kuma oturdu ve ekmekleri afiyetle yedi. Şakir bundan sonra güneşte uzağa bakarken gözlerini hep gölgede tuttu.
```

**Hakem bulguları (4):**

1. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "dedi Remzi. Şakir"
   - Cümle 4: «"Hazine seni bekliyor, Şakir!" dedi Remzi.»
   - Açıklama: Remzi daha önce tanıtılmadığı için konuşanın babası olduğu belli değil.
2. **D4** (D merceği) — Her replikte konuşan belli ve doğru kişi.
   - Alıntı: "Şakir!" dedi Remzi"
   - Cümle 4: «"Hazine seni bekliyor, Şakir!" dedi Remzi.»
   - Açıklama: Remzi daha önce tanıtılmadığı için konuşanın baba olduğu belli değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hazine seni bekliyor, Şakir!"
   - Cümle 4: «"Hazine seni bekliyor, Şakir!" dedi Remzi.»
   - Açıklama: Hazinenin beklemesi mecazdır.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hazine seni bekliyor"
   - Cümle 4: «"Hazine seni bekliyor, Şakir!" dedi Remzi.»
   - Açıklama: Hazine beklemez; mecazlı anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0192` birebir aynı, `@degisim: faydalı -> parlak` (tutuyorsan), ardından `@onarim: 2e624b89991f976328400aa4cb082e9c143b55b8`, sonra gövde.

### Hikâye 10: tohum sakir-0193 (deneme 1 -> 2)

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
Bir sabah Şakir kamp yerinde bilye oynuyordu. Küçük kutusu çok doluydu ve bilyeler kutudan taştı. Birden mavi bir bilye yere düştü ve uzun otların arasında kayboldu. Şakir otların arasına baktı ama bilyeyi göremedi. Otların arasında çok kuru yaprak vardı. Şakir şapkasını yaprakların üstünde hızlı hızlı salladı. Yapraklar havaya uçtu ve bir yana gitti. Yaprakların altında mavi bir şey parladı. Bu kayıp bilyeydi! Şakir bu bilyeyi ve kutudan iki bilye daha alıp cebine koydu. Artık kutu çok dolu değildi. Şakir oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Otların arasında çok kuru yaprak vardı"
   - Cümle 5: «Otların arasında çok kuru yaprak vardı.»
   - Açıklama: Bilye uzun otlarda kayboluyor ama çözümü getiren kuru yapraklar sebepsizce kuruluyor ve bilye birden yaprakların altından çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0193` birebir aynı, `@degisim: takvim -> bilye` (tutuyorsan), ardından `@onarim: c0c036f8dab86a6005844942fad1225a3966371f`, sonra gövde.

### Hikâye 11: tohum sakir-0194 (deneme 1 -> 2)

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
Şakir sisli bir sabah Necati ile parktaydı. Necati bankta oturmuş, hortumuyla bir kitap tutuyordu. Birden Necati gerindi ve kitap hortumundan fırladı ve sisin içinde kayboldu. "Kitabım nereye gitti?" diye sordu Necati. Şakir etrafa dikkatle baktı. Yakındaki ağacın dalında beyaz bir şey gördü. Bu, Necati'nin kitabıydı. Dal çok yüksekti ve Necati bile ona yetişemedi. Şakir şapkasını kitaba doğru attı. Kitap ve şapka daldan kaydı ve aşağı düştü. Necati kitabı hortumuyla havada yakaladı. "Teşekkürler, Şakir, sen olmasan kitabı bulamazdım!" dedi Necati. Şakir ile Necati banka oturdu ve kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "gerindi ve kitap hortumundan fırladı ve sisin"
   - Cümle 3: «Birden Necati gerindi ve kitap hortumundan fırladı ve sisin içinde kayboldu.»
   - Açıklama: Tek cümlede iki kez 've' bağlacı gereksiz tekrarla zincirleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0194` birebir aynı, ardından `@onarim: 8f09b0c898f638963819011d39e4f8cd75b100e8`, sonra gövde.

### Hikâye 12: tohum sakir-0200 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Remzi
@tohum: sakir-0200
- yer: park (Şehirdeki park.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'toka', fiil 'görünmek', sıfat 'hazırlıklı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Remzi
@plan: rüzgar babanın yelesini gözlerinin önüne getirdi | şapkasını babasının başına taktı
@tohum: sakir-0200
@degisim: hazırlıklı -> rüzgarlı
Şakir rüzgarlı bir günde babasıyla parkta top oynuyordu. Rüzgar Remzi'nin uzun yelesini gözlerinin önüne getirdi. Remzi topu göremedi ve top yanından geçip gitti. "Keşke bir toka olsaydı," dedi Remzi. Şakir biraz düşündü. Sonra şapkasını çıkardı ve babasının başına taktı. Remzi'nin yelesi şapkanın altında kaldı. "Gözlerin artık görünüyor, baba!" dedi Şakir. Remzi güldü ve topu Şakir'e attı. Şakir de onu geri yolladı. Remzi bu kez iki eliyle yakaladı. İkisi uzun süre oynadı ve çok güldü. "Teşekkürler, Şakir, artık her topu görüyorum!" dedi Remzi.
```

**Hakem bulguları (1):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Rüzgar Remzi'nin uzun yelesini"
   - Cümle 2: «Rüzgar Remzi'nin uzun yelesini gözlerinin önüne getirdi.»
   - Açıklama: Remzi'nin Şakir'in babası olduğu söylenmeden adıyla anılıyor, kimi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0200` birebir aynı, `@degisim: hazırlıklı -> rüzgarlı` (tutuyorsan), ardından `@onarim: 54270b31c084808aad9eff976aa8346ce2370ec5`, sonra gövde.
