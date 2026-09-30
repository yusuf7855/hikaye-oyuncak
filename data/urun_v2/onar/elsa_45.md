# Editör görevi (onarım): Elsa, onarım partisi 45

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/elsa_onar45.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Elsa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/elsa_onar45.txt --ad urun_v2`
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

## Kart: Elsa (kaynaklı, kapalı dünya)

- Ad: Elsa (okunuş: elsa; kesme eki okunuşa uyar)
- Kimlik: Elsa, buzu ve karı yönetebilen, bir krallığın genç kraliçesidir.
- Tür: kraliçe
- Güvenli özellik kullanımı: Buz ve kar gücü yalnız zararsız, güzel şeyler için kullanılır: kar yağdırır, buzdan şekil yapar. Hiçbir canlı donmaz, üşümez ya da incinmez; kimse buz tutmuş göl ya da deniz üstünde yürümez.
- Özellikler:
  - buz: Elinden buz ve kar çıkar; buzdan şekiller yapabilir. (örnek biçimler: buzdan, buzu)
  - kraliçe: Kraliçedir; kız kardeşini korur. (örnek biçimler: kraliçe)
- Yerler:
  - dağ: Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.
  - orman: Karlı ağaçlarla dolu orman.
  - deniz: Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.
  - şato: Elsa'nın kraliçesi olduğu krallığın sarayı; büyük salonlar ve avlu.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Anna: Elsa'nın cesur küçük kız kardeşi. Tür: prenses; konuşur. Yüzey biçimleri: Anna, kardeş, kardeşi
  - Olaf: Elsa'nın büyüsüyle canlanan neşeli kardan adam; sıcak sarılmaları ve yazı sever. Tür: kardan adam; konuşur. Yüzey biçimleri: Olaf, kardan adam
  - Kristoff: Buz toplayıp satan cesur dağ adamı; ren geyiği Sven'in arkadaşı. Tür: adam; konuşur. Yüzey biçimleri: Kristoff
  - Sven: Kristoff'un ren geyiği; kızağı çeker. Tür: ren geyiği; KONUŞMAZ. Yüzey biçimleri: Sven, ren geyiği, geyik
- Dünya kuralları:
  - Sven konuşmaz; sesle ve hareketle anlatır.
  - Anna Elsa'nın küçük kız kardeşidir; Elsa ablasıdır.
  - Olaf Elsa'nın büyüsüyle yapılmış kardan adamdır; hikayede erimez ya da parçalanmaz.
  - Elsa'nın gücü kimseyi dondurmaz ve incitmez.
- Yasak adlar: Hans, Weselton, Pabbie, Oaken, Marshmallow, Bruni, Arendelle
- Yasak: Anne babanın gemi yolculuğu, fırtına, troller, kurtlar ve kar canavarı hikayeye girmez.
- İzinli dünya kelimeleri: buz, kar, kraliçe, saray, kızak, fiyort, geyik

## Onarılacak hikâyeler

### Hikâye 1: tohum elsa-0181 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0181
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Sven
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'iplik', fiil 'kokmak', sıfat 'komik'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: geyik havuçlara dönerken kızağın ipi ağaca sarıldı | ters yöne dönmesini söyledi ve ip çözüldü
@tohum: elsa-0181
@degisim: iplik -> ip
Bir sabah Elsa ile Sven dağda, buz sarayının önündeydi. Sven'in çektiği küçük kızakta güzel kokan havuçlar vardı. Sven havuçlara ulaşmak isterken ağacın etrafında döndü ve ip ağaca sarıldı. Şimdi Sven ne öne ne de arkaya gidebiliyordu. Sven başını salladı ve komik bir ses çıkardı. Elsa gülümsedi ve bir kraliçe gibi Sven'in önüne geçti. "Sven, dur ve ağacın etrafında ters yöne bir kez dön," dedi Elsa. Sven hemen ağacın etrafında ters yöne döndü. İp ağaçtan çözüldü ve kızak yeniden serbest kaldı. Elsa kızaktan bir havuç aldı ve Sven'e verdi. "Aferin, Sven, şimdi afiyetle ye!" dedi Elsa.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elsa gülümsedi ve bir kraliçe gibi"
   - Cümle 6: «Elsa gülümsedi ve bir kraliçe gibi Sven'in önüne geçti.»
   - Açıklama: Elsa zaten kraliçe olduğu için 'bir kraliçe gibi' benzetmesi yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "gülümsedi ve bir kraliçe gibi"
   - Cümle 6: «Elsa gülümsedi ve bir kraliçe gibi Sven'in önüne geçti.»
   - Açıklama: 'Bir kraliçe gibi' benzetmesi mecazdır ve Elsa zaten kraliçe olduğu için anlamsızdır.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "bir kraliçe gibi Sven'in önüne geçti"
   - Cümle 6: «Elsa gülümsedi ve bir kraliçe gibi Sven'in önüne geçti.»
   - Açıklama: Tohumdaki kraliçe özelliği süs olarak geçiyor, sorunun çözümünde kartın 'özellikler' alanındaki gibi işe yaramıyor.
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) yalnız benzetme olarak geçiyor ve çözümü taşımıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0181` birebir aynı, `@degisim: iplik -> ip` (tutuyorsan), ardından `@onarim: 038919635b384a3f1be93259b54e6cc9a0f3ae61`, sonra gövde.

### Hikâye 2: tohum elsa-0183 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Anna
@tohum: elsa-0183
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'yıldız', fiil 'savrulmak', sıfat 'mor'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Anna
@plan: ormanda garip bir ses ve karda delikler vardı | kardeşini durdurdu ve yukarı bakınca yemişleri gördü
@tohum: elsa-0183
Elsa, kardeşi Anna ile karlı ormanda yürüyordu. Birden yakından garip bir ses geldi. Karda da yıldız gibi küçük delikler vardı. "Elsa, bu ses nereden geliyor?" diye sordu Anna. Anna sese doğru koşmak istedi. Kraliçe Elsa kardeşini korumak için onun elini tuttu. "Anna, koşma, dur ve yukarı bak," dedi Elsa. Anna durdu ve başını kaldırdı. Rüzgar esince ağaçtan küçük mor yemişler savruldu. Yemişler kara düştü ve aynı sesi çıkardı. Her yemiş karda yıldız gibi bir delik açtı. "Sesi bu yemişler yapıyormuş!" dedi Anna. Elsa çok sevindi, çünkü sesin nereden geldiğini kardeşiyle bulmuştu.
```

**Hakem bulguları (4):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kardeşini korumak"
   - Cümle 6: «Kraliçe Elsa kardeşini korumak için onun elini tuttu.»
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında unvanıyla yeniden tanıtılıyor.
   - Açıklama: Önceden tanıtılmış Elsa 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "koşma, dur ve yukarı bak"
   - Cümle 7: «"Anna, koşma, dur ve yukarı bak," dedi Elsa.»
   - Açıklama: Elsa sesin kaynağını bilmesi için hiçbir sebep yokken yukarı bakmayı söylüyor; çözüm sebepsizce geliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Anna, koşma, dur ve yukarı bak"
   - Cümle 7: «"Anna, koşma, dur ve yukarı bak," dedi Elsa.»
   - Açıklama: Elsa'nın neden yukarı bakmayı bildiği söylenmiyor ve cevabı tam o anda esen rüzgar sebepsizce getiriyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Yemişler kara düştü ve aynı sesi çıkardı"
   - Cümle 10: «Yemişler kara düştü ve aynı sesi çıkardı.»
   - Açıklama: Küçük yemişlerin yumuşak kara düşerek garip bir ses çıkarması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0183` birebir aynı, ardından `@onarim: aee480a0c26acec4c44bd51bc6f32040ceee22d4`, sonra gövde.

### Hikâye 3: tohum elsa-0184 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0184
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: kaybolan eşya
- yan: -
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'papatya', fiil 'paylaşmak', sıfat 'yağmurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: kurabiye torbası kütükten kaydı ve kara düştü | karda küçük bir delik görüp torbayı buldu
@tohum: elsa-0184
@degisim: papatya -> kurabiye
Ormanda hafif ve yağmurlu bir hava vardı. Kraliçe Elsa kuşlarla paylaşmak için küçük bir torba kurabiye getirmişti. Ama torbayı bir kütüğün üstüne koyunca torba kaydı ve kara düştü. Şimdi torba hiçbir yerde görünmüyordu. Elsa kütüğün çevresine baktı ama torbayı bulamadı. Sonra kütüğün yanında, karda küçük bir delik gördü. Deliğin yanında birkaç kurabiye kırıntısı vardı. Elsa elini yavaşça deliğe soktu ve torbayı buldu. Torbayı çıkardı ve üstündeki karı silkeledi. Sonra kurabiyeleri ağaçların altında kuru bir yere koydu. Elsa bundan sonra torbayı hep elinde tuttu.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "hafif ve yağmurlu bir hava"
   - Cümle 1: «Ormanda hafif ve yağmurlu bir hava vardı.»
   - Açıklama: 'Hafif hava' kelimesi havaya uygun bir anlamda kullanılmamış; 'hafif yağmurlu' gibi bir ifade olmalı.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "hafif ve yağmurlu bir hava vardı"
   - Cümle 1: «Ormanda hafif ve yağmurlu bir hava vardı.»
   - Açıklama: Hava yağmurlu deniyor ama torba kara düşüyor ve karda delik açılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kuşlarla paylaşmak için"
   - Cümle 2: «Kraliçe Elsa kuşlarla paylaşmak için küçük bir torba kurabiye getirmişti.»
   - Açıklama: Kraliçe özelliği yalnız unvan olarak anılıyor, karttaki gibi işe yarar biçimde kullanılmıyor.
   - Açıklama: Tohumdaki kraliçe özelliği kartta kız kardeşini korumak olarak tanımlı, burada yalnız unvan olarak geçiyor ve işe yaramıyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Elsa elini yavaşça deliğe soktu"
   - Cümle 8: «Elsa elini yavaşça deliğe soktu ve torbayı buldu.»
   - Açıklama: Çocuğun taklit edebileceği biçimde bilinmeyen bir deliğe el sokuluyor.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Elsa bundan sonra torbayı hep elinde tuttu"
   - Cümle 11: «Elsa bundan sonra torbayı hep elinde tuttu.»
   - Açıklama: Kurabiyeleri kuşlarla paylaşma hedefine dönülmüyor ve hikaye sıcak bir kapanış olmadan kuru bir cümleyle bitiyor.
   - Açıklama: Kuşlarla paylaşma hedefine dönülmüyor ve hikaye sıcak bir kapanış olmadan bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0184` birebir aynı, `@degisim: papatya -> kurabiye` (tutuyorsan), ardından `@onarim: defc61b2c906c0c48e2900977daded14b27adc3c`, sonra gövde.

### Hikâye 4: tohum elsa-0185 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Kristoff
@tohum: elsa-0185
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'içecek', fiil 'süzülmek', sıfat 'reçelli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Kristoff
@plan: kuşları gösterirken arkadaşının bardağını devirdi | özür diledi ve kendi içeceğini onunla paylaştı
@tohum: elsa-0185
Limanda Elsa ile Kristoff yan yana oturuyordu. Önlerindeki taşta iki bardak içecek ve reçelli ekmek vardı. Elsa suyun üstünde süzülen kuşları gösterirken Kristoff'un bardağını devirdi. İçecek döküldü ve bardak boş kaldı. "Özür dilerim, Kristoff, dikkat etmedim," dedi Elsa. Kraliçe Elsa kendi bardağını aldı ve içeceğin yarısını Kristoff'a verdi. "Kristoff, al, bu yarısı senin," dedi Elsa. "Teşekkür ederim, Elsa," dedi Kristoff ve gülümsedi. Elsa ile Kristoff reçelli ekmeklerini yiyip kuşları mutlu mutlu izlediler.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa kendi bardağını"
   - Cümle 6: «Kraliçe Elsa kendi bardağını aldı ve içeceğin yarısını Kristoff'a verdi.»
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Zaten tanınan Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa kendi bardağını aldı"
   - Cümle 6: «Kraliçe Elsa kendi bardağını aldı ve içeceğin yarısını Kristoff'a verdi.»
   - Açıklama: Tohumdaki kraliçe özelliği karttaki gibi kız kardeşi korumak için değil, yalnız unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, çözümde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0185` birebir aynı, ardından `@onarim: fd45766bbc77ced9fd1547ca620292c3403d8e8f`, sonra gövde.

### Hikâye 5: tohum elsa-0186 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0186
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'koltuk', fiil 'beslemek', sıfat 'sessiz'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: ekmek kırıntıları yumuşak kara gömüldü ve kuşlar bulamadı | buzdan düz bir tabak yapıp kırıntıları üstüne koydu
@tohum: elsa-0186
@degisim: koltuk -> tabak
Elsa, Sven ile dağda ekmek yiyordu ve karın üstüne küçük kuşlar kondu. Elsa kuşları beslemek için kara ekmek kırıntıları attı. Ama kırıntılar yumuşak karın içine gömüldü ve kuşlar onları bulamadı. "Sven, kuşlar kırıntıları göremiyor," dedi Elsa. Elsa elini salladı ve karın üstüne buzdan düz bir tabak yaptı. Kırıntıları tabağa koydu ve Sven ile biraz geri çekildi. Elsa ile Sven sessiz durdu ve kuşları izledi. Kuşlar tabağa kondu ve kırıntıları yedi. "Bak, Sven, kuşların hepsi yiyor, ne güzel!" dedi Elsa.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "kara ekmek kırıntıları attı"
   - Cümle 2: «Elsa kuşları beslemek için kara ekmek kırıntıları attı.»
   - Açıklama: 'Kara' hem 'kara (kar)' hem 'siyah' okunabiliyor; 'karın üstüne' gibi açık bir ifade gerekir.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Kuşlar tabağa kondu ve kırıntıları yedi"
   - Cümle 8: «Kuşlar tabağa kondu ve kırıntıları yedi.»
   - Açıklama: Çoğul canlı kuşlar arka planda kalmıyor, sorunun ve çözümün merkezinde olaya katılıyor.
   - Açıklama: Arka planda kalması gereken çoğul canlı kuşlar olayın merkezine girip olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0186` birebir aynı, `@degisim: koltuk -> tabak` (tutuyorsan), ardından `@onarim: d870b70c2dc6a0cb5d87d5aff63d9bf61c4b2742`, sonra gövde.

### Hikâye 6: tohum elsa-0188 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | Olaf
@tohum: elsa-0188
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Olaf
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'atkı', fiil 'sürmek', sıfat 'buzlu'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | Olaf
@plan: atkı yüksek ve buzlu bir dala takıldı | özür diledi ve buzdan bir çubukla atkıyı indirdi
@tohum: elsa-0188
Bir sabah Elsa ile Olaf karlı ormanda oynuyordu. Elsa şaka olsun diye Olaf'ın kırmızı atkısını havaya attı. Ama atkı yüksek ve buzlu bir dala takıldı. "Atkım çok yüksekte kaldı!" dedi Olaf. "Özür dilerim, Olaf, bu şaka hiç iyi değildi," dedi Elsa. Sonra elinden çıkan buzla uzun bir çubuk yaptı. Çubukla atkıyı daldan yavaşça indirdi. Bu iş çok kısa sürdü. Elsa atkıyı Olaf'ın boynuna geri taktı. Olaf gülerek Elsa'ya sıkıca sarıldı. Elsa çok sevindi, çünkü arkadaşının atkısı yine yerindeydi.
```

**Hakem bulguları (3):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "Olaf'ın kırmızı atkısını havaya"
   - Cümle 2: «Elsa şaka olsun diye Olaf'ın kırmızı atkısını havaya attı.»
   - Açıklama: Kartın yanlar bölümünde Olaf'a ait bir atkı yok; kapalı dünyaya eşya ekleniyor.
2. **K8** (K merceği) — Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
   - Alıntı: "Olaf'ın kırmızı atkısını havaya"
   - Cümle 2: «Elsa şaka olsun diye Olaf'ın kırmızı atkısını havaya attı.»
   - Açıklama: Kartın Olaf tarifinde ve dizide Olaf'ın kırmızı atkısı yok; figürün dünyası hakkında yanlış bilgi veriliyor.
   - Açıklama: Diziyi izleyen çocuk Olaf'ı atkısız bilir; görünüşü hakkında yanlış bilgi veriliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu iş çok kısa sürdü"
   - Cümle 8: «Bu iş çok kısa sürdü.»
   - Açıklama: Bu cümle olaya hiçbir şey katmayan işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0188` birebir aynı, ardından `@onarim: 78191090d49612cd25ebe01ec3f3ff96406768a3`, sonra gövde.

### Hikâye 7: tohum elsa-0189 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | Anna
@tohum: elsa-0189
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: paylaşmak
- yan: Anna
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'boncuk', fiil 'kirletmek', sıfat 'devasa'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Elsa | deniz | Anna
@plan: çamur kız kardeşinin boncuklarını kirletti | kardeşini sudan uzak tuttu ve boncuklarını paylaştı
@tohum: elsa-0189
Deniz kıyısında Elsa ile Anna boncuklarla kolye yapıyordu. Birden Anna'nın kutusu yere düştü. Yerdeki çamur bütün boncukları kirletti. Anna boncukları yıkamak için suya doğru koştu. Kraliçe Elsa hemen kardeşinin elini tuttu ve onu geri çekti. Anna durdu ve Elsa'nın yanına oturdu. Sonra Elsa kendi kutusunu açtı. Boncuklarını ikiye ayırdı ve yarısını Anna'ya verdi. Kutuda devasa, mavi bir boncuk da vardı. Elsa onu da kardeşine verdi. Anna büyük boncuğu kolyesinin ortasına taktı. Sonra Elsa ile Anna kolyelerini mutlu mutlu bitirdi.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen kardeşinin"
   - Cümle 5: «Kraliçe Elsa hemen kardeşinin elini tuttu ve onu geri çekti.»
   - Açıklama: Önceden tanıtılan Elsa unvanıyla yeniden tanıtılıyor.
   - Açıklama: Zaten tanıtılmış Elsa hikayenin ortasında 'Kraliçe Elsa' diye yeniden tanıtılıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kraliçe Elsa hemen kardeşinin elini tuttu ve onu geri çekti"
   - Cümle 5: «Kraliçe Elsa hemen kardeşinin elini tuttu ve onu geri çekti.»
   - Açıklama: Anna'nın boncukları yıkamak için suya gitmesi makul bir çözümken Elsa'nın onu neden durdurduğu hiç söylenmiyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "hemen kardeşinin elini tuttu ve onu geri çekti"
   - Cümle 5: «Kraliçe Elsa hemen kardeşinin elini tuttu ve onu geri çekti.»
   - Açıklama: Anna'nın boncukları yıkamaya gitmesi akla yatkınken Elsa'nın onu neden geri çektiği hiç söylenmiyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Boncuklarını ikiye ayırdı ve yarısını Anna'ya verdi"
   - Cümle 8: «Boncuklarını ikiye ayırdı ve yarısını Anna'ya verdi.»
   - Açıklama: Çözüm çamurlu boncuklara yönelmiyor; kirli boncuklar temizlenmeden yerine başka boncuk veriliyor.
   - Açıklama: Sorun boncukların kirlenmesi ama çözüm boncukları temizlemeye değil yeni boncuk vermeye yöneliyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kutuda devasa, mavi bir"
   - Cümle 9: «Kutuda devasa, mavi bir boncuk da vardı.»
   - Açıklama: 'Devasa' 3 yaşındaki çocuğun bilmediği bir kelime.
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmeyeceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0189` birebir aynı, ardından `@onarim: d7b523eaef354f65de6325128b96f8b6ba7b84ec`, sonra gövde.

### Hikâye 8: tohum elsa-0190 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | -
@tohum: elsa-0190
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'kürek', fiil 'basmak', sıfat 'hevesli'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | -
@plan: dağ soğuk olduğu için hiç çiçek açmıyordu | buzdan çiçekler yapıp karın içine dikti
@tohum: elsa-0190
Karlı dağın tepesinde Elsa bahçe oyunu oynuyordu. Elsa çok hevesliydi ve sarayın önüne bir bahçe yapmak istiyordu. Ama dağ çok soğuktu ve orada hiç çiçek açmıyordu. Elsa yine de küreği aldı. Ayağıyla küreğe bastı ve karda küçük çukurlar açtı. Sonra boş çukurlara bakıp biraz düşündü. Elinden çıkan buzla parlak çiçekler yaptı. Çiçekleri tek tek çukurlara dikti. Güneşte çiçekler ışıl ışıl parladı. Sarayın önünde güzel bir bahçe oldu. Elsa, soğuk dağda da kendi çiçeklerini yapabileceğini öğrendi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Elsa çok hevesliydi ve"
   - Cümle 2: «Elsa çok hevesliydi ve sarayın önüne bir bahçe yapmak istiyordu.»
   - Açıklama: 'Hevesli' 3 yaşındaki çocuk için soyut bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Elsa yine de küreği aldı"
   - Cümle 4: «Elsa yine de küreği aldı.»
   - Açıklama: Elsa henüz çiçeği yokken ve bir fikri yokken sebepsizce kürekle boş çukurlar açıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0190` birebir aynı, ardından `@onarim: 6709b8f9e226d7e82df5c12be7982045c265c9de`, sonra gövde.

### Hikâye 9: tohum elsa-0191 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | orman | -
@tohum: elsa-0191
- yer: orman (Karlı ağaçlarla dolu orman.)
- tema: bir şey yapmak
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'yüzük', fiil 'korunmak', sıfat 'utangaç'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | orman | -
@plan: dal çok kuru olduğu için yüzük kırıldı | buzdan kalın bir yüzük yaptı
@tohum: elsa-0191
@degisim: utangaç -> parlak
Elsa karlı ormanda kendine bir yüzük yapmak istiyordu. Yerden ince bir dal aldı ve yavaşça büktü. Ama dal çok kuruydu ve çıt diye kırıldı. Elsa ikinci bir dal denedi, o da kırıldı. Elsa kırık dallara bakıp biraz düşündü. Sonra elinden çıkan buzla bir yüzük yaptı. Yüzüğü kalın tuttu, böylece yüzük kırılmaya karşı korundu. Parlak yüzüğü parmağına taktı ve elini salladı. Yüzük hiç kırılmadı ve parmağında çok güzel durdu. Elsa bundan sonra yüzük yaparken kuru dal kullanmadı.
```

**Hakem bulguları (3):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "dal çok kuru olduğu için yüzük kırıldı"
   - Cümle 0 (plan satırı): «dal çok kuru olduğu için yüzük kırıldı | buzdan kalın bir yüzük yaptı»
   - Açıklama: Gövdede yüzük değil, yüzük olmadan önce dal kırılıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "böylece yüzük kırılmaya karşı korundu"
   - Cümle 7: «Yüzüğü kalın tuttu, böylece yüzük kırılmaya karşı korundu.»
   - Açıklama: 'Kırılmaya karşı korundu' soyut ve 3 yaşındaki çocuğa ağır bir anlatım.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yüzük kırılmaya karşı korundu"
   - Cümle 7: «Yüzüğü kalın tuttu, böylece yüzük kırılmaya karşı korundu.»
   - Açıklama: 'Kırılmaya karşı korunmak' soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0191` birebir aynı, `@degisim: utangaç -> parlak` (tutuyorsan), ardından `@onarim: e2ca53d5595b5cfe32cea59cd175a87d941c83ce`, sonra gövde.

### Hikâye 10: tohum elsa-0192 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Kristoff
@tohum: elsa-0192
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kristoff
- özellik: kraliçe (Kraliçedir; kız kardeşini korur.)
- kelimeler: isim 'kurabiye', fiil 'tanışmak', sıfat 'şanslı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Kristoff
@plan: sürpriz hazır olmadan arkadaşı erken geldi | ona kapıda gözlerini kapatmasını söyledi
@tohum: elsa-0192
Karlı dağın tepesindeki sarayda Elsa bir sürpriz hazırlıyordu. Kristoff ile tanıştıkları günü kurabiyelerle kutlamak istiyordu. Ama Kristoff erken geldi ve kapıyı açtı. Masa daha hazır değildi. Kraliçe Elsa hemen elini kaldırdı. "Kristoff, kapıda dur ve gözlerini kapat," dedi Elsa. Kristoff durdu ve gözlerini sıkıca kapattı. Elsa kurabiyeleri hızla masaya dizdi. "Şimdi bakabilirsin, Kristoff," dedi Elsa. Kristoff baktı ve kurabiyeleri gördü. "Ne şanslıyım, bu çok güzel bir sürpriz!" dedi Kristoff. İkisi kurabiyeleri birlikte yedi ve güldü. Elsa bundan sonra sürprizlerini hep erkenden hazırladı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kristoff ile tanıştıkları günü kurabiyelerle kutlamak"
   - Cümle 2: «Kristoff ile tanıştıkları günü kurabiyelerle kutlamak istiyordu.»
   - Açıklama: Tanışma gününü kutlamak 3 yaşındaki çocuk için soyut bir kavram.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Kraliçe Elsa hemen elini"
   - Cümle 5: «Kraliçe Elsa hemen elini kaldırdı.»
   - Açıklama: Zaten tanıtılmış Elsa 'Kraliçe Elsa' diye yeniden tanıtılıyor.
   - Açıklama: Elsa zaten tanıtılmışken 'Kraliçe Elsa' diye yeniden tanıtılıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Kraliçe Elsa hemen elini kaldırdı"
   - Cümle 5: «Kraliçe Elsa hemen elini kaldırdı.»
   - Açıklama: Tohumdaki kraliçe özelliği (kız kardeşini korur) işe yarar biçimde kullanılmıyor, yalnız unvan olarak geçiyor.
   - Açıklama: Tohumdaki kraliçe özelliği yalnız unvan olarak geçiyor, kartındaki gibi işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0192` birebir aynı, ardından `@onarim: 0c1ac011f1add933ec87749871694f19ea631ddf`, sonra gövde.

### Hikâye 11: tohum elsa-0194 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | deniz | -
@tohum: elsa-0194
- yer: deniz (Krallığın önündeki fiyort kıyısı ve limanı; kimse suya girmez.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'bilye', fiil 'şakımak', sıfat 'boyalı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | deniz | -
@plan: yer düz olmadığı için bilyeler her yana yuvarlandı | buzdan yuvarlak bir duvar yapıp içinde oynadı
@tohum: elsa-0194
Elsa limanda bilye oynuyordu. Kıyıda kuşlar şakıyordu ve boyalı bilyeler güneşte parlıyordu. Ama yer düz değildi ve bilyeler her yana yuvarlanıyordu. Elsa bilyeleri yakalamak için oradan oraya koştu. Bir bilyeyi tuttu, bir başkası uzağa yuvarlandı. Elsa durdu ve biraz düşündü. Sonra elinden çıkan buzla yere yuvarlak bir duvar yaptı. Bilyeleri bu duvarın içine koydu ve yeniden oynadı. Bilyeler duvara çarpıp geri döndü. Hiçbiri uzağa gitmedi. Elsa çok sevindi, çünkü bilyeleri artık hep yanındaydı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Kıyıda kuşlar şakıyordu"
   - Cümle 2: «Kıyıda kuşlar şakıyordu ve boyalı bilyeler güneşte parlıyordu.»
   - Açıklama: 'Şakımak' edebi bir fiil; 3 yaşındaki bir çocuk bilmeyebilir, 'cıvıldıyordu' daha uygun.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bilyeleri yakalamak için oradan oraya koştu"
   - Cümle 4: «Elsa bilyeleri yakalamak için oradan oraya koştu.»
   - Açıklama: Limanda yuvarlanan bilyelerin peşinden koşmak çocuğun su kenarında taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0194` birebir aynı, ardından `@onarim: 3a1d19cfe6292d98c6b112a4c9d5b5179706d32a`, sonra gövde.

### Hikâye 12: tohum elsa-0195 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Elsa | dağ | Sven
@tohum: elsa-0195
- yer: dağ (Karlı yüksek dağ; tepede Elsa'nın buzdan yaptığı saray vardır.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Sven
- özellik: buz (Elinden buz ve kar çıkar; buzdan şekiller yapabilir.)
- kelimeler: isim 'leke', fiil 'sıçratmak', sıfat 'ucuz'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Elsa | dağ | Sven
@plan: kızağın ucuz ipi ikiye koptu | geyikten yardım istedi ve ipi buzla birleştirdi
@tohum: elsa-0195
@degisim: leke -> ip
Bir sabah Elsa karlı dağda kızağını çekiyordu. Kızakta sarayın kapısını süslemek için çam dalları vardı. Ama kızağın ipi ucuz ve inceydi, birden ikiye koptu. Elsa ipin uçlarını iki eliyle tuttu. Ama elleri doluydu ve buz yapamadı. "Sven, ipin bu ucunu tutar mısın?" diye sordu Elsa. Sven başını salladı ve ipin ucunu ağzıyla tuttu. Elsa elindeki ucu yanına getirdi ve iki ucu buzla birleştirdi. Sonra Sven kızağı sarayın kapısına kadar çekti. Sven koşarken karı her yana sıçrattı. Elsa güldü ve çam dallarını kapıya astı. Elsa bundan sonra bir işi tek başına yapamadığında Sven'den yardım istedi.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kızağın ipi ucuz ve inceydi"
   - Cümle 3: «Ama kızağın ipi ucuz ve inceydi, birden ikiye koptu.»
   - Açıklama: 'Ucuz' fiyat kavramıdır, 3 yaşındaki çocuğa soyut kalır ve ipin kopmasını açıklamaz.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "elindeki ucu yanına getirdi"
   - Cümle 8: «Elsa elindeki ucu yanına getirdi ve iki ucu buzla birleştirdi.»
   - Açıklama: 'yanına' zamirinin kimi ya da neyi gösterdiği belli değil; Sven'in tuttuğu ucun yanı olduğu açık yazılmamış.
   - Açıklama: 'Yanına' ekinin kimin ya da neyin yanını gösterdiği belli değil.
3. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sven kızağı sarayın kapısına kadar çekti"
   - Cümle 9: «Sonra Sven kızağı sarayın kapısına kadar çekti.»
   - Açıklama: Hikaye dağda başlıyor ama sarayın kapısında bitiyor; tek sahne kuralı çiğneniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: elsa-0195` birebir aynı, `@degisim: leke -> ip` (tutuyorsan), ardından `@onarim: 0415f1bab0dc89f8878ee22529cd7e8793e962f1`, sonra gövde.
