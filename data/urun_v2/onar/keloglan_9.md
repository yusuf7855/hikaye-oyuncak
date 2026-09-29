# Editör görevi (onarım): Keloğlan, onarım partisi 9

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/keloglan_onar9.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Keloğlan | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/keloglan_onar9.txt --ad urun_v2`
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

## Kart: Keloğlan (kaynaklı, kapalı dünya)

- Ad: Keloğlan (okunuş: keloğlan; kesme eki okunuşa uyar)
- Kimlik: Keloğlan, bir köyde annesiyle yaşayan azimli ve dürüst bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Sakarlığı yalnız bir şeyi düşürmek ya da karıştırmak olarak gösterilir; kimse düşüp incinmez. Azmi tehlikeli bir işe girişmek olarak gösterilmez.
- Özellikler:
  - dürüst: Dürüsttür ve azimlidir; işini bırakmaz. (örnek biçimler: dürüst, dürüstçe)
  - öğren: Yeni şeyler öğrenmeyi sever. (örnek biçimler: öğrendi, öğrenmek)
  - sakar: Biraz sakardır ama iyi kalplidir. (örnek biçimler: sakar, sakarlık)
- Yerler:
  - orman: Köyün yakınındaki orman; büyük ağaçlar vardır.
  - dağ: Köyün yakınındaki tepe.
  - ev: Keloğlan'ın annesiyle yaşadığı köy evi.
  - şato: Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - anası: Keloğlan'ın annesi; onu her zaman korur. Tür: anne; konuşur. Yüzey biçimleri: ana, anası, anne, annesi, anneciğim
  - Bilgecan Dede: Köyün en bilge kişisi; çok kitap okur, icatlar yapar, çocuklara bilmediklerini öğretir. Tür: dede; konuşur. Yüzey biçimleri: Bilgecan Dede, Bilgecan, dede
  - Balkız: Keloğlan'ın akıllı arkadaşı; sarı saçlıdır. Tür: kız; konuşur. Yüzey biçimleri: Balkız
  - eşeği: Keloğlan'ın akıllı eşeği; yük taşır, Keloğlan ıslık çalınca gelir. Tür: eşek; KONUŞMAZ. Yüzey biçimleri: Karakaçan, eşek, eşeği
- Dünya kuralları:
  - Bilgecan Dede iksir ve ilaç vermez; bilgisiyle ve icatlarıyla yardım eder.
  - Karakaçan konuşmaz; yük taşır, başını sallar, anırır.
  - Keloğlan'ın babası hikayede yoktur.
  - Balkız Keloğlan'ın arkadaşıdır; aşk, nişan ya da evlilik konusu yoktur.
- Yasak adlar: Kara Vezir, Çirkin Cadı, Kara, Sivri, Örgülü, Huysuz, Uzun, Sinek, İnatçı, Tomurcuk, Prenses, Kuyu Canavarı, Kötülükler Kraliçesi, Çizmeli Tilki, Mucit, Tilkican, Nasreddin Hoca
- Yasak: Cadı, vezir, asker, canavar ve büyü hikayeye girmez.
- İzinli dünya kelimeleri: köy, eşek, ıslık, icat

## Onarılacak hikâyeler

### Hikâye 1: tohum keloglan-0025 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | -
@tohum: keloglan-0025
- yer: dağ (Köyün yakınındaki tepe.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'yaprak', fiil 'heyecanlanmak', sıfat 'güzel'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | dağ | -
@plan: tepeden ıslık sesi geldi ama ıslık çalan yoktu | yapraklar deliğe girince sesi yapan dalı buldu
@tohum: keloglan-0025
Keloğlan tepede güzel sarı yapraklar topluyordu. Birden rüzgar esti ve ince bir ıslık sesi duyuldu. Ama tepede ıslık çalan kimse yoktu. Keloğlan çok heyecanlandı ve bu sesi merak etti. Sesin geldiği yere doğru yürüdü. Otların arasına baktı ama bir şey göremedi. Keloğlan biraz sakardı ve eğilirken yapraklar elinden düştü. Rüzgar yaprakları yerdeki kuru bir dalın deliğine itti. O anda ıslık kesildi. Keloğlan dalı eline aldı. Dalın içi boştu. Yaprakları delikten çıkardı ve ıslık yeniden başladı. Ses, dalın içinden geçen rüzgardan çıkıyordu. Keloğlan dalı rüzgara doğru tuttu ve ıslığı mutlu mutlu dinledi.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "eğilirken yapraklar elinden düştü"
   - Cümle 7: «Keloğlan biraz sakardı ve eğilirken yapraklar elinden düştü.»
   - Açıklama: Çözüm sakarlıkla düşen yapraklarla tesadüfen, sebepsizce geliyor.
   - Açıklama: Çözüm figürün eyleminden değil sakarlık ve rüzgarla gelen bir rastlantıdan çıkıyor.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Rüzgar yaprakları yerdeki kuru bir dalın deliğine itti"
   - Cümle 8: «Rüzgar yaprakları yerdeki kuru bir dalın deliğine itti.»
   - Açıklama: Sesin kaynağını Keloğlan değil kaza ve rüzgar buluyor.
   - Açıklama: Sesin kaynağını Keloğlan bulmuyor; düşen yaprakları rüzgar tesadüfen deliğe itiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0025` birebir aynı, ardından `@onarim: 0125eaad01bde8d13f75bb3fdb316ad89150bc61`, sonra gövde.

### Hikâye 2: tohum keloglan-0027 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | anası
@tohum: keloglan-0027
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'gümüş', fiil 'düzenlemek', sıfat 'sabırsız'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | orman | anası
@plan: sepet düştü ve çilekler otlara döküldü | özür diledi ve çilekleri toplayıp düzenledi
@tohum: keloglan-0027
@degisim: gümüş -> çilek
Keloğlan anasıyla ormanda çilek topluyordu. Keloğlan çilekleri yemek için sabırsızdı ve dolu sepeti hızla kaptı. Ama Keloğlan biraz sakardı. Sepet elinden kaydı ve çilekler otlara döküldü. Keloğlan anasına üzgün üzgün baktı. "Özür dilerim, anne, acele ettim," dedi Keloğlan. "Üzülme, gel birlikte toplayalım," dedi anası. Keloğlan çilekleri otların arasından tek tek topladı. Sonra onları sepette güzelce düzenledi. Bu kez sepeti iki eliyle sıkıca tuttu. Anası gülümsedi ve onun başını okşadı. "Teşekkürler, anneciğim, çilekleri birlikte yiyelim!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama Keloğlan biraz sakardı"
   - Cümle 3: «Ama Keloğlan biraz sakardı.»
   - Açıklama: 'sakar' soyut ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Sepet elinden kaydı ve çilekler otlara döküldü"
   - Cümle 4: «Sepet elinden kaydı ve çilekler otlara döküldü.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede ortaya çıkıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0027` birebir aynı, `@degisim: gümüş -> çilek` (tutuyorsan), ardından `@onarim: 7b2cdc257eb15d2345fe0ce97ecbbfafb537c66a`, sonra gövde.

### Hikâye 3: tohum keloglan-0028 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Bilgecan Dede
@tohum: keloglan-0028
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'sayfa', fiil 'sokulmak', sıfat 'mükemmel'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | Bilgecan Dede
@plan: rüzgar dedenin kitap sayfasını uçurdu | sayfayı ağacın dibinde bulup dedeye geri verdi
@tohum: keloglan-0028
Keloğlan ormanda Bilgecan Dede ile karşılaştı. Dede üzgündü, çünkü rüzgar bir kitap sayfasını uçurmuştu. Keloğlan hemen büyük ağaçların arasına baktı. Bir ağacın dibinde kayıp sayfayı buldu. Sayfada güzel bir çiçek resmi vardı. Keloğlan resmi çok beğendi ama dürüst bir çocuktu. "Al, dede, sayfa burada," dedi Keloğlan. Bilgecan Dede sevindi ve ağacın altına oturdu. "Gel, kitabı birlikte okuyalım," dedi Bilgecan Dede. Keloğlan hemen Bilgecan Dede'ye sokuldu. Dede kitabı yavaşça okudu. "Mükemmel bir hikaye, dede!" dedi Keloğlan. Keloğlan çok sevindi, çünkü sayfayı bulmuştu ve kitabı Dede ile paylaşmıştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ama dürüst bir çocuktu"
   - Cümle 6: «Keloğlan resmi çok beğendi ama dürüst bir çocuktu.»
   - Açıklama: 'Dürüst' soyut bir kavram ve olaydan çıkan somut bir ders değil.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Keloğlan hemen Bilgecan Dede'ye sokuldu"
   - Cümle 10: «Keloğlan hemen Bilgecan Dede'ye sokuldu.»
   - Açıklama: 'Bilgecan Dede' art arda üç cümlede gereksiz yere tekrarlanıyor.
3. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "kitabı Dede ile paylaşmıştı"
   - Cümle 13: «Keloğlan çok sevindi, çünkü sayfayı bulmuştu ve kitabı Dede ile paylaşmıştı.»
   - Açıklama: Ad olarak kullanılmayan 'dede' cümle ortasında büyük harfle yazılmış; öteki yerlerle tutarsız.
   - Açıklama: Cümle ortasında ad olmadan kullanılan 'dede' küçük harfle yazılır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0028` birebir aynı, ardından `@onarim: 9b4b9ff1e6b42bdab1ddcc35bd01c3248624f1c0`, sonra gövde.

### Hikâye 4: tohum keloglan-0029 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | Balkız
@tohum: keloglan-0029
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: paylaşmak
- yan: Balkız
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'fırça', fiil 'tamamlamak', sıfat 'sessiz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | Balkız
@plan: tek bir fırça vardı ve arkadaşının fırçası yoktu | fırçayı paylaştı ve sırayla boyadılar
@tohum: keloglan-0029
Bir sabah Keloğlan ile Balkız sessiz ormanda bir ağacın resmini yapıyordu. Ama tek bir fırça vardı, çünkü Balkız fırçasını evde unutmuştu. "Ben nasıl boyayacağım?" diye sordu Balkız üzgün üzgün. Keloğlan elindeki fırçaya baktı ve biraz düşündü. "Fırçayı paylaşalım, önce sen boya," dedi Keloğlan. Balkız ağacın yapraklarını yeşile boyadı. Balkız da fırçayı Keloğlan'a verdi. Keloğlan ağacın altına küçük bir çiçek boyadı. İkisi resmi sırayla boyadı ve tamamladı. Keloğlan, bir fırçanın ikisine de yettiğini öğrendi. Sonra Keloğlan ile Balkız resimlerine bakıp mutlu mutlu güldü.
```

**Hakem bulguları (4):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Balkız fırçasını evde unutmuştu"
   - Cümle 2: «Ama tek bir fırça vardı, çünkü Balkız fırçasını evde unutmuştu.»
   - Açıklama: Kartın yerler alanında Balkız'ın evi yok; kapalı dünyada kartta olmayan bir ev anılıyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Balkız da fırçayı Keloğlan'a verdi"
   - Cümle 7: «Balkız da fırçayı Keloğlan'a verdi.»
   - Açıklama: 'da' bağlacı burada anlamsız; Balkız'dan başka fırça veren olmadı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bir fırçanın ikisine de yettiğini öğrendi"
   - Cümle 10: «Keloğlan, bir fırçanın ikisine de yettiğini öğrendi.»
   - Açıklama: Tohumdaki öğrenme sevgisi sorunu çözmüyor, sona eklenmiş bir ders olarak kalıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan, bir fırçanın ikisine de yettiğini öğrendi"
   - Cümle 10: «Keloğlan, bir fırçanın ikisine de yettiğini öğrendi.»
   - Açıklama: Tohumdaki 'öğren' özelliği sorunun çözümünde işe yaramıyor, çözüm paylaşmakla geliyor ve öğrenme sona eklenmiş bir sonuç olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0029` birebir aynı, ardından `@onarim: 5811a6b85dc6e0b77ca5e0a851c9080897e059bb`, sonra gövde.

### Hikâye 5: tohum keloglan-0030 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0030
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'çatal', fiil 'fırçalamak', sıfat 'güneşli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kozalak uzun olduğu için hep yana kaçtı | yuvarlak bir ceviz bulup onu yuvarladı
@tohum: keloglan-0030
@degisim: fırçalamak -> yuvarlamak
Keloğlan güneşli bir sabah ormanda yeni bir oyun kurdu. Yere çatal bir dal dikti. Bir kozalağı dalın iki ucu arasından geçirmek istedi. Ama kozalak yumurta gibi uzundu ve her seferinde yana kaçtı. Keloğlan kozalağı üç kez yuvarladı ama yine olmadı. Sonra top gibi bir şey aramaya başladı. Büyük bir ağacın altında küçük bir ceviz buldu. Cevizi dala doğru yavaşça yuvarladı. Ceviz dümdüz gitti ve iki ucun arasından geçti. Keloğlan yuvarlak şeylerin daha düz gittiğini öğrendi. Sonra Keloğlan cevizle oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "kozalak yumurta gibi uzundu"
   - Cümle 4: «Ama kozalak yumurta gibi uzundu ve her seferinde yana kaçtı.»
   - Açıklama: Sorun (kozalağın yana kaçması) ancak 4. cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0030` birebir aynı, `@degisim: fırçalamak -> yuvarlamak` (tutuyorsan), ardından `@onarim: c8d5ff4c6c8bb08797eddcc770007e6a3eb76f6a`, sonra gövde.

### Hikâye 6: tohum keloglan-0031 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | şato | eşeği
@tohum: keloglan-0031
- yer: şato (Köyün uzağındaki büyük taş saray; bahçesi ve yüksek kapıları vardır.)
- tema: yeni bir şeyi denemek
- yan: eşeği
- özellik: öğren (Yeni şeyler öğrenmeyi sever.)
- kelimeler: isim 'damla', fiil 'işaretlemek', sıfat 'kirli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | şato | eşeği
@plan: kağıda boya damladı ve kağıt kirlendi | fırçayı kabın kenarına silip yeniden boyadı
@tohum: keloglan-0031
Keloğlan şatonun bahçesinde ilk kez boyayla resim yapmayı denedi. Karakaçan resim çantasını sırtında taşımıştı. Ama kağıda iri bir boya damlası düştü ve kağıt kirli oldu. "Ah, resmim bozuldu!" dedi Keloğlan. Keloğlan fırçaya dikkatle baktı. Fırça boyayla doluydu. Fırçayı kabın kenarına hafifçe sildi. Böylece boyayı az almayı öğrendi. Sonra çantadan temiz bir kağıt aldı. Önce şatonun yüksek kapısını kalemle işaretledi. Sonra çizgileri yavaşça boyadı ve kağıda hiç leke düşmedi. Karakaçan başını salladı. "Karakaçan, bak, ilk resmim ne güzel oldu!" dedi Keloğlan.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kapısını kalemle işaretledi"
   - Cümle 10: «Önce şatonun yüksek kapısını kalemle işaretledi.»
   - Açıklama: Kapı resmi işaretlenmez, çizilir; fiil anlama uymuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Önce şatonun yüksek kapısını kalemle işaretledi"
   - Cümle 10: «Önce şatonun yüksek kapısını kalemle işaretledi.»
   - Açıklama: Kalem sebepsiz beliriyor ve çözüme bir katkısı olmayan fazladan bir adım ekliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0031` birebir aynı, ardından `@onarim: b7234669b378e0a8ec13633e9aa72c168f3e0826`, sonra gövde.

### Hikâye 7: tohum keloglan-0032 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | eşeği
@tohum: keloglan-0032
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: paylaşmak
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'örgü', fiil 'uçmak', sıfat 'karmakarışık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Keloğlan | ev | eşeği
@plan: üç havuç iki arkadaşa eşit yetmiyordu | birer havuç alıp son havucu ikiye kırdı
@tohum: keloglan-0032
@degisim: karmakarışık -> turuncu
Keloğlan evin önünde oturuyordu ve çiçeklerin üstünde kelebekler uçuyordu. Örgü sepetinde üç turuncu havuç vardı ve Karakaçan da acıkmıştı. Keloğlan onları eşit paylaşmak istedi ama havuçlar üç taneydi. "Karakaçan, bir tane senin, bir tane benim," dedi Keloğlan. Karakaçan başını salladı ve havucunu yedi. Keloğlan da kendi havucunu yedi. Sonra sepette kalan son havuca baktı. Keloğlan dürüst bir çocuktu ve kendine fazla almadı. Onu tam ortasından ikiye kırdı. İki parça aynı boydaydı. "Bu yarısı da senin, Karakaçan," dedi Keloğlan. Karakaçan sevinçle parçasını yedi. Sonra ikisi yan yana oturup kelebekleri mutlu mutlu izledi.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "iki arkadaşa eşit yetmiyordu"
   - Cümle 0 (plan satırı): «üç havuç iki arkadaşa eşit yetmiyordu | birer havuç alıp son havucu ikiye kırdı»
   - Açıklama: 'Eşit yetmemek' yanlış kullanım; havuçlar eşit bölünmüyordu denmeli.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "birer havuç alıp son havucu ikiye kırdı"
   - Cümle 0 (plan satırı): «üç havuç iki arkadaşa eşit yetmiyordu | birer havuç alıp son havucu ikiye kırdı»
   - Açıklama: Plandaki havucu ikiye kırma adımı gövdede yazılmıyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Bu yarısı da senin"
   - Cümle 11: «"Bu yarısı da senin, Karakaçan," dedi Keloğlan.»
   - Açıklama: 'Bu yarısı' dilbilgisel değil; 'Bu yarım' ya da 'Bunun yarısı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0032` birebir aynı, `@degisim: karmakarışık -> turuncu` (tutuyorsan), ardından `@onarim: c3d14334e96f58f3814bef1b33f77b1937c17c9a`, sonra gövde.

### Hikâye 8: tohum keloglan-0034 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Keloğlan | dağ | Balkız
@tohum: keloglan-0034
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: Balkız
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'krema', fiil 'güvenmek', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | dağ | Balkız
@plan: sepette iki arkadaşa tek bir kremalı kek vardı | arkadaşına güvendi ve keki tabakta ikiye böldü
@tohum: keloglan-0034
Tepede serin bir rüzgar esiyordu. Keloğlan ile Balkız tekerlekli sepeti tepeye kadar çekmişti. Sepette tek bir kremalı kek vardı ama ikisi de çok acıkmıştı. Keloğlan keki Balkız ile yarı yarıya paylaşmak istedi. Ama Keloğlan biraz sakardı ve elindeki şeyleri sık sık düşürürdü. Bu yüzden Balkız'a güvendi ve sepetteki tabağı ona verdi. Balkız tabağı iki eliyle sıkıca tuttu. Keloğlan keki tabağın üstünde yavaşça ikiye böldü. Hiçbir parça yere düşmedi. İkisi çimenlere oturdu ve keklerini yedi. Keloğlan'ın burnuna biraz krema bulaştı ve Balkız güldü. Keloğlan çok mutluydu, çünkü kekini arkadaşı Balkız ile paylaşmıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tekerlekli sepeti tepeye kadar çekmişti"
   - Cümle 2: «Keloğlan ile Balkız tekerlekli sepeti tepeye kadar çekmişti.»
   - Açıklama: Tekerlekli sepet ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Sepette tek bir kremalı kek vardı"
   - Cümle 3: «Sepette tek bir kremalı kek vardı ama ikisi de çok acıkmıştı.»
   - Açıklama: Tek keki ikiye bölmek kendiliğinden çözülen önemsiz bir durum; gerçek bir sorun ve sebep kurulmuyor.
   - Açıklama: Tek keki ikiye bölmek zaten kolay olduğundan sorunun gerçek bir sebebi ve ağırlığı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0034` birebir aynı, ardından `@onarim: 8622c9a6556843ceb8c98001412a5e8b0fbe0bc2`, sonra gövde.

### Hikâye 9: tohum keloglan-0035 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | ev | anası
@tohum: keloglan-0035
- yer: ev (Keloğlan'ın annesiyle yaşadığı köy evi.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: anası
- özellik: sakar (Biraz sakardır ama iyi kalplidir.)
- kelimeler: isim 'süpürge', fiil 'ısınmak', sıfat 'aceleci'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | ev | anası
@plan: aceleci koşarken un kabını düşürdü ve un döküldü | unu süpürgeyle temizleyip anasından özür diledi
@tohum: keloglan-0035
Dışarıda soğuk bir rüzgar esiyordu. Keloğlan ısınmak için aceleci adımlarla eve koştu. Ama biraz sakardı ve koşarken masadaki un kabını düşürdü. Beyaz un bütün yere döküldü. Anası yeri daha yeni temizlemişti ve biraz üzüldü. Keloğlan anasının yüzüne baktı ve çok utandı. Keloğlan hemen köşedeki süpürgeyi aldı. Dökülen bütün unu dikkatle süpürdü. Sonra anasına sarıldı ve özür diledi. Anası gülümsedi ve onu sıcacık öptü. Keloğlan çok rahatladı, çünkü anası artık üzgün değildi.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "aceleci koşarken un kabını"
   - Cümle 0 (plan satırı): «aceleci koşarken un kabını düşürdü ve un döküldü | unu süpürgeyle temizleyip anasından özür diledi»
   - Açıklama: 'Aceleci' sıfatı zarf gibi kullanılmış; 'aceleyle koşarken' olmalı.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Dışarıda soğuk bir rüzgar esiyordu"
   - Cümle 1: «Dışarıda soğuk bir rüzgar esiyordu.»
   - Açıklama: Hikaye başlıktaki evde değil dışarıda başlıyor ve sonra eve geçiyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "aceleci adımlarla eve koştu"
   - Cümle 2: «Keloğlan ısınmak için aceleci adımlarla eve koştu.»
   - Açıklama: Tohumdaki özellik sakarlık; acelecilik karttaki özelliklere ikinci bir huy olarak ekleniyor.
4. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Keloğlan ısınmak için aceleci adımlarla eve koştu"
   - Cümle 2: «Keloğlan ısınmak için aceleci adımlarla eve koştu.»
   - Açıklama: Hikaye evin dışında başlıyor ve sonra eve geçiyor; tek sahne kuralı çiğneniyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ama biraz sakardı"
   - Cümle 3: «Ama biraz sakardı ve koşarken masadaki un kabını düşürdü.»
   - Açıklama: 'Sakar' 3 yaşındaki çocuğun bilmeyeceği bir kelime.
6. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Beyaz un bütün yere döküldü"
   - Cümle 4: «Beyaz un bütün yere döküldü.»
   - Açıklama: 'Bütün yere' bozuk; 'yere' ya da 'her yere' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0035` birebir aynı, ardından `@onarim: 7a0baeabc5806d48fadeeb468a446ba52fa2cfc0`, sonra gövde.

### Hikâye 10: tohum keloglan-0036 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | -
@tohum: keloglan-0036
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'duvar', fiil 'öğrenmek', sıfat 'yüksek'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | -
@plan: kar çok yumuşaktı ve duvar hep yıkılıyordu | karı sıkıca sıkıp sert toplar yaptı
@tohum: keloglan-0036
Bir sabah ormana bembeyaz kar yağmıştı. Keloğlan büyük ağaçların arasında kardan bir duvar yapmak istedi. Ama kar çok yumuşaktı ve duvar hep yıkılıyordu. Keloğlan dürüst ve çalışkan bir çocuktu, bu yüzden hemen vazgeçmedi. Karı iki elinin arasında sıkıca sıktı. Kar sert bir top oldu. Böylece karla sağlam toplar yapmayı öğrendi. Keloğlan sert kar toplarını yan yana ve üst üste koydu. Duvar yavaş yavaş yükseldi. Sonunda Keloğlan'ın boyu kadar yüksek oldu. Keloğlan onun arkasına oturdu ve gülümsedi. Keloğlan çok sevindi, çünkü kardan duvar sonunda bitmişti.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "dürüst ve çalışkan bir çocuktu"
   - Cümle 4: «Keloğlan dürüst ve çalışkan bir çocuktu, bu yüzden hemen vazgeçmedi.»
   - Açıklama: Tohumdaki dürüstlük olayda işe yaramıyor ve çalışkanlık ek bir özellik olarak sayılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "sağlam toplar yapmayı öğrendi"
   - Cümle 7: «Böylece karla sağlam toplar yapmayı öğrendi.»
   - Açıklama: Tohum özelliği dürüst/azimli iken kartın 'öğrenmeyi sever' özelliği de ekleniyor ve dürüst yalnız etiket olarak sayılıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kardan duvar sonunda bitmişti"
   - Cümle 12: «Keloğlan çok sevindi, çünkü kardan duvar sonunda bitmişti.»
   - Açıklama: 'Sonunda' kelimesi 10. cümleden hemen sonra gereksizce tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0036` birebir aynı, ardından `@onarim: 69c1dd0b0b965e22781d4f7d2fbe2f2ed82df2b7`, sonra gövde.

### Hikâye 11: tohum keloglan-0037 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | orman | eşeği
@tohum: keloglan-0037
- yer: orman (Köyün yakınındaki orman; büyük ağaçlar vardır.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: eşeği
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'tereyağı', fiil 'kurmak', sıfat 'çilekli'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Keloğlan | orman | eşeği
@plan: eşeğin ipi bir çalıya takıldı ve gelemedi | sese yürüyüp düğümü yavaş yavaş çözdü
@tohum: keloglan-0037
Bir sabah Keloğlan ormanda sofra kurdu ve Karakaçan'ı ıslıkla çağırdı. Ama Karakaçan gelmedi, üzgün bir anırma duyuldu. Keloğlan sese yürüdü ve Karakaçan'ın ipini bir çalıya takılmış gördü. İp çalının dallarına sıkıca sarılmıştı. Keloğlan dürüst ve çalışkan bir çocuktu, hiç vazgeçmedi. Düğümü yavaş yavaş çözdü. "Gel, Karakaçan, kahvaltı hazır!" dedi Keloğlan. Karakaçan başını salladı ve onunla sofraya yürüdü. Sofrada ekmek, tereyağı ve çilekli reçel vardı. Bir dilim ekmeği Karakaçan'a verdi. Kendisi de reçelli ekmeğini yedi. Keloğlan çok sevindi, çünkü Karakaçan yine yanındaydı.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "eşeğin ipi bir çalıya takıldı ve gelemedi"
   - Cümle 0 (plan satırı): «eşeğin ipi bir çalıya takıldı ve gelemedi | sese yürüyüp düğümü yavaş yavaş çözdü»
   - Açıklama: Planda 'gelemedi' fiilinin öznesi dilbilgisel olarak ip oluyor; eşek öznesi eksik.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst ve çalışkan bir çocuktu"
   - Cümle 5: «Keloğlan dürüst ve çalışkan bir çocuktu, hiç vazgeçmedi.»
   - Açıklama: Dürüstlük olayda işe yaramıyor ve karttaki özelliklere çalışkanlık etiketi ekleniyor.
   - Açıklama: Kartın özellik alanındaki dürüstlük işe yarar biçimde kullanılmıyor, yalnız özellik listesi gibi sayılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Bir dilim ekmeği Karakaçan'a verdi"
   - Cümle 10: «Bir dilim ekmeği Karakaçan'a verdi.»
   - Açıklama: Öznesiz cümlede son özne Karakaçan olduğundan ekmeği kimin verdiği belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0037` birebir aynı, ardından `@onarim: f495ac95c12993bf985952e8de7ba4b5266aadd0`, sonra gövde.

### Hikâye 12: tohum keloglan-0038 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Keloğlan | dağ | Bilgecan Dede
@tohum: keloglan-0038
- yer: dağ (Köyün yakınındaki tepe.)
- tema: paylaşmak
- yan: Bilgecan Dede
- özellik: dürüst (Dürüsttür ve azimlidir; işini bırakmaz.)
- kelimeler: isim 'kozalak', fiil 'konuşmak', sıfat 'havalı'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Keloğlan | dağ | Bilgecan Dede
@plan: dede tepede hiç kozalak bulamadı | dürüst davranıp çantasını dede ile paylaştı
@tohum: keloglan-0038
Bir sabah Keloğlan tepede kozalak topluyordu. Kısa sürede çantası doldu. Sonra Bilgecan Dede tepeye geldi ama yerde hiç kozalak bulamadı. "Keloğlan, icadım için kozalak lazım," dedi Bilgecan Dede. Keloğlan dürüst bir çocuktu. "Hepsini ben topladım, dede, yarısı senin olsun," dedi Keloğlan. Yarısını hemen Dede'ye verdi. Bilgecan Dede onları bir ipe dizdi ve bir dala astı. Rüzgar esince hepsi birbirine çarptı ve tık tık ses çıkardı. İkisi bu yeni icat hakkında uzun uzun konuştu. "Ne havalı bir icat, dede!" dedi Keloğlan. "Bu güzel hediye için teşekkürler, Keloğlan," dedi Bilgecan Dede.
```

**Hakem bulguları (8):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dürüst davranıp çantasını dede"
   - Cümle 0 (plan satırı): «dede tepede hiç kozalak bulamadı | dürüst davranıp çantasını dede ile paylaştı»
   - Açıklama: Paylaşmak dürüstlük değildir; 'dürüst' kelimesi yanlış anlamda kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "dürüst davranıp çantasını dede ile paylaştı"
   - Cümle 0 (plan satırı): «dede tepede hiç kozalak bulamadı | dürüst davranıp çantasını dede ile paylaştı»
   - Açıklama: Paylaşılan çanta değil kozalaklar; paylaşmak da dürüstlük değil.
3. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "dürüst davranıp çantasını dede ile paylaştı"
   - Cümle 0 (plan satırı): «dede tepede hiç kozalak bulamadı | dürüst davranıp çantasını dede ile paylaştı»
   - Açıklama: Gövdede çözüm dürüstlük değil paylaşmak; plan çözümü yanlış adlandırıyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "ama yerde hiç kozalak bulamadı"
   - Cümle 3: «Sonra Bilgecan Dede tepeye geldi ama yerde hiç kozalak bulamadı.»
   - Açıklama: Dedenin neden kozalak bulamadığı açıkça söylenmiyor ve sorun figürün değil dedenin sorunu.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Keloğlan dürüst bir çocuktu"
   - Cümle 5: «Keloğlan dürüst bir çocuktu.»
   - Açıklama: Kartın özellikler alanındaki dürüstlük burada paylaşma/cömertlik olarak kullanılıyor, dürüstlüğün işe yaradığı bir durum yok.
6. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hepsini ben topladım, dede, yarısı senin olsun"
   - Cümle 6: «"Hepsini ben topladım, dede, yarısı senin olsun," dedi Keloğlan.»
   - Açıklama: Tohumdaki özellik dürüstlük ama olayda gösterilen cömertçe paylaşmadır, dürüstlük işe yaramıyor.
7. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Yarısını hemen Dede'ye verdi."
   - Cümle 7: «Yarısını hemen Dede'ye verdi.»
   - Açıklama: Başka yerlerde küçük harfle 'dede' yazılan hitap burada büyük harf ve kesmeyle yazılmış; yazım tutarsız.
8. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Ne havalı bir icat"
   - Cümle 11: «"Ne havalı bir icat, dede!" dedi Keloğlan.»
   - Açıklama: 'İcat' soyut, 'havalı' argo bir kelime; 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: keloglan-0038` birebir aynı, ardından `@onarim: c76647ca024580e50679dc8d8b08da7f0b48b33b`, sonra gövde.
