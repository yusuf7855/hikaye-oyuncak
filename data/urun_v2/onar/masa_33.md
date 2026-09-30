# Editör görevi (onarım): Maşa, onarım partisi 33

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/masa_onar33.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Maşa | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/masa_onar33.txt --ad urun_v2`
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

## Kart: Maşa (kaynaklı, kapalı dünya)

- Ad: Maşa (okunuş: maşa; kesme eki okunuşa uyar)
- Kimlik: Maşa, ormanın yakınındaki evinde yaşayan, çok enerjik ve oyun seven küçük bir kızdır.
- Tür: kız
- Güvenli özellik kullanımı: Maşa'nın denemeleri kimseyi incitmez; kimse düşmez, bir şey kırılıp kimseyi yaralamaz. Yüksek yere çıkmaz, ateşe ve derin suya yaklaşmaz.
- Özellikler:
  - dene: Çok enerjiktir; her şeyi dener. (örnek biçimler: denedi, denemek, deniyordu)
  - reçel: Tatlıları ve reçeli çok sever. (örnek biçimler: reçel, reçeli)
- Yerler:
  - orman: Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.
  - dağ: Ormanın yanındaki tepe.
  - ev: Maşa'nın evi ve önündeki bahçe.
    - yan Koca Ayı ise: Koca Ayı'nın ormandaki ağaç evi ve sebze bahçesi.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Koca Ayı: Maşa'nın eski dostu; iyi kalpli ve her işi bilen bir ayı. Tür: ayı; KONUŞMAZ. Yüzey biçimleri: Koca Ayı, ayı
  - kirpi: Ormanda yaşayan, elmayı seven dost canlısı bir kirpi. Tür: kirpi; KONUŞMAZ. Yüzey biçimleri: kirpi
  - sincap: Ormanda küçük bir yuvada yaşayan hızlı sincap; fındık ve meşe palamudu sever. Tür: sincap; KONUŞMAZ. Yüzey biçimleri: sincap
  - Daşa: Maşa'nın şehirde yaşayan kuzeni; düşünceli, ciddi ve akıllı bir kız. Tür: kız; konuşur. Yüzey biçimleri: Daşa, kuzen, kuzeni
- Dünya kuralları:
  - Koca Ayı, kirpi ve sincap konuşmaz; sesle, hareketle ve yüzüyle anlatır. Yalnız Maşa ve Daşa konuşur.
  - Daşa şehirde yaşar; Maşa'yı ziyarete gelir.
- Yasak adlar: Rosie, Panda, Kaplan, Ayı Hanım, Siyah Ayı, Kurnaz Kurt, Aptal Kurt, Penguen
- Yasak: Kurtlar, sirk gösterisi ve ambulans hikayeye girmez.
- İzinli dünya kelimeleri: reçel, ayı, sincap, kirpi, patika

## Onarılacak hikâyeler

### Hikâye 1: tohum masa-0133 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | ev | sincap, Daşa
@tohum: masa-0133
- yer: ev (Maşa'nın evi ve önündeki bahçe.)
- tema: paylaşmak
- yan: sincap, Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'tebeşir', fiil 'olgunlaşmak', sıfat 'hızlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | ev | sincap, Daşa
@plan: iki kız çizmek istedi ama tek tebeşir vardı | tebeşiri ikiye bölüp bir parçayı kuzenine verdi
@tohum: masa-0133
@degisim: olgunlaşmak -> çizmek
Bahçede serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa yere resim çizmek istiyordu. Ama ellerinde tek bir beyaz tebeşir vardı. Maşa tebeşiri ikiye bölmeyi denedi. Tebeşir kolayca iki parça oldu. "Al, Daşa, bu parça senin!" dedi Maşa. "Teşekkürler, Maşa!" dedi Daşa. Maşa yere hızlı koşan bir sincap çizdi. Daşa da sincabın önüne üç fındık ekledi. O sırada ağaçtan gerçek bir sincap indi. Sincap resimdeki fındıkları kokladı ve kuyruğunu salladı. İki kuzen buna çok güldü. Sonra Maşa ile Daşa yeni resimler yapmaya mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede serin bir rüzgar esiyordu"
   - Cümle 1: «Bahçede serin bir rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer ev iken hikaye bahçede başlıyor ve bahçede geçiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada ağaçtan gerçek bir sincap indi"
   - Cümle 10: «O sırada ağaçtan gerçek bir sincap indi.»
   - Açıklama: Sorun çözüldükten sonra sincap sebepsizce beliriyor ve sorunla ilgisi olmayan bir sahne açıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0133` birebir aynı, `@degisim: olgunlaşmak -> çizmek` (tutuyorsan), ardından `@onarim: 07cc673dffed54271989a5df9232e86da38c51e0`, sonra gövde.

### Hikâye 2: tohum masa-0134 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı
@tohum: masa-0134
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yağmur ya da kar günü
- yan: Koca Ayı
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'nota', fiil 'kurtulmak', sıfat 'utangaç'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı
@plan: yağmur başladı ve piknik yarım kaldı | boş kavanozu yağmurun altına koyup müzik yaptı
@tohum: masa-0134
@degisim: utangaç -> boş
Ormanda Maşa ile Koca Ayı piknik yapıyordu. Birden yağmur başladı ve piknik yarım kaldı. İkisi büyük bir ağacın altına koştu ve yağmurdan kurtuldu. Ama Koca Ayı pikniğin yarım kalmasına üzüldü. Sepette biraz reçel kalmıştı. Maşa reçeli çok severdi ve son kaşığını hemen yedi. Sonra boş kavanozu ve iki boş bardağı yağmurun altına koydu. Damlalar kavanoza düşünce ince bir nota çıktı. Bardaklardan ise kalın notalar geldi. "Dinle, Koca Ayı, bu bizim yağmur şarkımız!" dedi Maşa. Koca Ayı gülümsedi ve başını seslerle birlikte salladı. Maşa çok sevindi, çünkü yağmurlu piknik yine eğlenceli olmuştu.
```

**Hakem bulguları (4):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra boş kavanozu ve iki boş bardağı yağmurun altına koydu"
   - Cümle 7: «Sonra boş kavanozu ve iki boş bardağı yağmurun altına koydu.»
   - Açıklama: Sorun yarım kalan piknik ama çözüm pikniği sürdürmüyor, yalnız yağmurdan müzik yaparak konuyu değiştiriyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "boş kavanozu ve iki boş bardağı yağmurun altına koydu"
   - Cümle 7: «Sonra boş kavanozu ve iki boş bardağı yağmurun altına koydu.»
   - Açıklama: Çözüm yağmura ya da yarım kalan pikniğe yönelmiyor, sorunu çözmek yerine konuyu müziğe kaydırıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ince bir nota çıktı"
   - Cümle 8: «Damlalar kavanoza düşünce ince bir nota çıktı.»
   - Açıklama: 'Nota' ve ince/kalın nota soyut, küçük çocuğa uygun olmayan bir kavram.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "kavanoza düşünce ince bir nota çıktı"
   - Cümle 8: «Damlalar kavanoza düşünce ince bir nota çıktı.»
   - Açıklama: 'Nota' ve 'ince/kalın nota' soyut müzik kavramları olup 3 yaşındaki bir çocuğun bileceği kelimeler değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0134` birebir aynı, `@degisim: utangaç -> boş` (tutuyorsan), ardından `@onarim: 0312be2bae61ab9cd6869ce5e25acb89d3c794f6`, sonra gövde.

### Hikâye 3: tohum masa-0137 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | -
@tohum: masa-0137
- yer: dağ (Ormanın yanındaki tepe.)
- tema: bir şey yapmak
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'tepsi', fiil 'örmek', sıfat 'yakın'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | -
@plan: rüzgar esince yapraklar tepside durmuyordu | yaprakları reçelle tepsiye yapıştırdı
@tohum: masa-0137
@degisim: örmek -> yapıştırmak
Bir sabah Maşa tepede reçelli ekmek yiyordu. Sonra boş tepsiye sarı yapraklarla bir güneş resmi yapmak istedi. Ama rüzgar esince yapraklar tepsiden uçup gidiyordu. Maşa tepsiye baktı ve düşündü. Kavanozda biraz reçel kalmıştı. Maşa parmağıyla tepsiye küçük reçel noktaları koydu. Sonra yakındaki ağacın dibinden yeni yapraklar topladı. Her yaprağı bir noktanın üstüne yapıştırdı. Rüzgar yine esti ama yapraklar hiç kıpırdamadı. Tepside kocaman sarı bir güneş resmi oldu. Maşa parmağında kalan tatlıyı da yaladı ve güldü. Maşa çok mutluydu, çünkü yaprak güneşini sonunda bitirmişti.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "parmağında kalan tatlıyı da"
   - Cümle 11: «Maşa parmağında kalan tatlıyı da yaladı ve güldü.»
   - Açıklama: Reçel için 'tatlı' kelimesi yanlış anlamda; 'reçeli' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0137` birebir aynı, `@degisim: örmek -> yapıştırmak` (tutuyorsan), ardından `@onarim: e487471e4be8274f3a6c2953e7dd7c57fa718e20`, sonra gövde.

### Hikâye 4: tohum masa-0140 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Koca Ayı, sincap
@tohum: masa-0140
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni arkadaş (ilk adımı figür atar)
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yelpaze', fiil 'heyecanlanmak', sıfat 'gürültülü'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Koca Ayı, sincap
@plan: yeni sincap onları tanımadığı için dalda kaldı | reçelli fındık bırakıp sincabı yanına çağırdı
@tohum: masa-0140
@degisim: yelpaze -> fındık
Ormanda yapraklar hışır hışır sallanıyordu. Maşa ile Koca Ayı bir ağacın altında reçelli ekmek yiyordu. Dalda yeni bir sincap vardı, ama onları tanımadığı için aşağı inmiyordu. Maşa bu sincapla arkadaş olmak istedi. "Koca Ayı, sepette fındık var mı?" diye sordu Maşa. Koca Ayı başını salladı ve Maşa'ya bir avuç fındık verdi. Maşa en sevdiği reçelden fındıkların üstüne biraz sürdü. Sonra fındıkları ağacın dibine koydu. "Gel, küçük sincap, bunlar senin için!" dedi Maşa. Tatlı reçel kokusu dala kadar gitti. Sincap heyecanlandı ve hızla aşağı indi. Fındıkları çıtır çıtır, gürültülü bir sesle yedi. Maşa çok sevindi, çünkü ormanda yeni bir arkadaşı olmuştu.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "yeni sincap onları tanımadığı"
   - Cümle 0 (plan satırı): «yeni sincap onları tanımadığı için dalda kaldı | reçelli fındık bırakıp sincabı yanına çağırdı»
   - Açıklama: Plan satırında 'onları' zamirinin kimi gösterdiği belli değil.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "çıtır çıtır, gürültülü bir sesle"
   - Cümle 12: «Fındıkları çıtır çıtır, gürültülü bir sesle yedi.»
   - Açıklama: 'Çıtır çıtır' ile 'gürültülü bir sesle' aynı şeyi gereksiz yere tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0140` birebir aynı, `@degisim: yelpaze -> fındık` (tutuyorsan), ardından `@onarim: 45f47e1175ed34a45ef9a4f66bd02819a9814471`, sonra gövde.

### Hikâye 5: tohum masa-0141 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | sincap, Daşa
@tohum: masa-0141
- yer: dağ (Ormanın yanındaki tepe.)
- tema: paylaşmak
- yan: sincap, Daşa
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yatak', fiil 'temizlenmek', sıfat 'saklı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | sincap, Daşa
@plan: kuzeninin yiyeceği yoktu ve tek ekmek vardı | reçelli ekmeğini ikiye bölüp kuzeniyle paylaştı
@tohum: masa-0141
@degisim: yatak -> kırıntı
Tepede serin bir rüzgar esiyordu. Maşa ile kuzeni Daşa çimenlerin üstünde oturuyordu. Maşa'nın elinde tek bir reçelli ekmek vardı, ama Daşa'nın yiyeceği yoktu. Daşa şehirden gelirken çantasını evde unutmuştu. Maşa reçeli çok severdi, ama ekmeğini hemen ikiye böldü. "Al, Daşa, yarısı senin!" dedi Maşa. "Teşekkürler, Maşa, çok tatlı!" dedi Daşa. İkisi ekmeklerini gülerek yedi. Yere birkaç kırıntı düştü. O sırada bir kayanın arkasında saklı duran bir sincap dışarı çıktı. Sincap kırıntıları hızla topladı. Çimenlerin üstü bir anda temizlendi. Maşa bundan sonra reçelli ekmeğini hep kuzeniyle paylaştı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Teşekkürler, Maşa, çok tatlı!"
   - Cümle 7: «"Teşekkürler, Maşa, çok tatlı!" dedi Daşa.»
   - Açıklama: 'Tatlı' ekmeği mi yoksa mecazla Maşa'yı mı nitelediği belirsiz.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir kayanın arkasında saklı duran bir sincap dışarı çıktı"
   - Cümle 10: «O sırada bir kayanın arkasında saklı duran bir sincap dışarı çıktı.»
   - Açıklama: Sincap sorun çözüldükten sonra sebepsiz beliriyor ve olaya hiçbir katkısı yok.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "bir sincap dışarı çıktı"
   - Cümle 10: «O sırada bir kayanın arkasında saklı duran bir sincap dışarı çıktı.»
   - Açıklama: Sorun çözüldükten sonra sincap sebepsiz beliriyor ve olaya bir katkısı olmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0141` birebir aynı, `@degisim: yatak -> kırıntı` (tutuyorsan), ardından `@onarim: 7fe7a6f09c949badf8f621a645287254f115368b`, sonra gövde.

### Hikâye 6: tohum masa-0142 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0142
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: bir şey yapmak
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'çöp', fiil 'kıvırmak', sıfat 'yumuşacık'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: böğürtlenler küçük ellerinden düşüyordu | büyük bir yaprağı külah gibi kıvırdı
@tohum: masa-0142
@degisim: çöp -> yaprak
Bir sabah Maşa ormanda bir patikada yürüyordu. Birden böğürtlenlerle dolu bir çalı gördü. Maşa reçeli çok severdi ve böğürtlenleri reçel için toplamak istedi. Ama elleri küçüktü ve böğürtlenler parmaklarının arasından düşüyordu. Maşa etrafına baktı ve büyük, yumuşacık bir yaprak buldu. Yaprağı bir külah gibi kıvırdı. Sonra böğürtlenleri tek tek külahın içine koydu. Yaprak hiç yırtılmadı ve hiçbir böğürtlen düşmedi. Kısa bir süre sonra külah ağzına kadar doldu. Maşa dolu külahı iki eliyle tuttu ve mutlu mutlu güldü.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa reçeli çok severdi"
   - Cümle 3: «Maşa reçeli çok severdi ve böğürtlenleri reçel için toplamak istedi.»
   - Açıklama: Tohumdaki reçel özelliği yalnız söylenerek sayılıyor, çözümde işe yaramıyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Maşa reçeli çok severdi ve böğürtlenleri reçel için toplamak istedi.»
   - Açıklama: Sorun (böğürtlenlerin küçük ellerden düşmesi) ancak 4. cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "külah ağzına kadar doldu"
   - Cümle 9: «Kısa bir süre sonra külah ağzına kadar doldu.»
   - Açıklama: 'Ağzına kadar' kalıp bir söyleyiş; küçük çocuk 'ağız' kelimesini yanlış anlayabilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0142` birebir aynı, `@degisim: çöp -> yaprak` (tutuyorsan), ardından `@onarim: d521e86fc3e87dc8aac90f27becae86b9eccff6a`, sonra gövde.

### Hikâye 7: tohum masa-0144 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı
@tohum: masa-0144
- yer: dağ (Ormanın yanındaki tepe.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Koca Ayı
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'kıyafet', fiil 'açmak', sıfat 'kibar'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı
@plan: aç ayının sepetindeki ip sıkı bir düğüm olmuştu | minik parmaklarıyla düğümü çekip sepeti açtı
@tohum: masa-0144
@degisim: kıyafet -> sepet
Maşa tepede Koca Ayı ile yürüyüş yapıyordu. Koca Ayı çok acıkmıştı ve karnı guruldadı. Ama yemek sepetinin ipi küçük, sıkı bir düğüm olmuştu. Koca Ayı'nın kalın pençeleri bu düğümü çözemiyordu. Koca Ayı üzgün üzgün sepete baktı. "Bekle, Koca Ayı, ben açarım!" dedi Maşa. Maşa minik parmaklarıyla düğümün ucunu çekmeyi denedi. Düğüm yavaş yavaş gevşedi ve çözüldü. Maşa sepetin kapağını açtı. İçinde ekmek ve kırmızı elmalar vardı. Koca Ayı kibar bir şekilde başını eğdi ve bir elma aldı. "Afiyet olsun, Koca Ayı, sepetin artık açık!" dedi Maşa.
```

**Hakem bulguları (1):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "kalın pençeleri bu düğümü çözemiyordu"
   - Cümle 4: «Koca Ayı'nın kalın pençeleri bu düğümü çözemiyordu.»
   - Açıklama: Kartın yanlar alanındaki ilişki Koca Ayı'yı her işi bilen bir ayı olarak tanımlıyor; burada basit bir düğümü çözemiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0144` birebir aynı, `@degisim: kıyafet -> sepet` (tutuyorsan), ardından `@onarim: 502fa214d4661227e9dbcb4a443d4dff26337282`, sonra gövde.

### Hikâye 8: tohum masa-0145 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | Koca Ayı, sincap
@tohum: masa-0145
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yağmur ya da kar günü
- yan: Koca Ayı, sincap
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'elbise', fiil 'almak', sıfat 'ince'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Maşa | dağ | Koca Ayı, sincap
@plan: yağmur yağdı ve reçelli ekmekler ıslanmaya başladı | ekmekleri sepete koyup ağacın altına koştu
@tohum: masa-0145
@degisim: elbise -> sepet
Bir sabah Maşa, Koca Ayı ve sincap tepede piknik yapıyordu. Çimenlerin üstünde ince reçelli ekmekler duruyordu. Birden yağmur yağdı ve ekmekler ıslanmaya başladı. "Reçelli ekmekler ıslanmasın!" dedi Maşa. Hemen hepsini sepete koydu ve sepeti aldı. Sonra yakındaki büyük bir ağacı gösterdi. "Koca Ayı, hadi o ağacın altına gidelim!" diye seslendi Maşa. Koca Ayı başını salladı ve sincap onun omzuna zıpladı. Hep birlikte ağacın altına koştular. Ağacın geniş dalları yağmuru tutuyordu. Sepetteki ekmekler kuruydu. Maşa bir dilimi Koca Ayı'ya uzattı. Maşa ve dostları yağmuru izleyerek pikniklerine mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "reçelli ekmekler ıslanmaya başladı"
   - Cümle 0 (plan satırı): «yağmur yağdı ve reçelli ekmekler ıslanmaya başladı | ekmekleri sepete koyup ağacın altına koştu»
   - Açıklama: Tohumdaki reçel sevgisi çözümde işe yaramıyor; reçel yalnız yiyecek adı olarak geçiyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çimenlerin üstünde ince reçelli ekmekler duruyordu"
   - Cümle 2: «Çimenlerin üstünde ince reçelli ekmekler duruyordu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız eşya olarak geçiyor, çözümde işe yaramıyor.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Ağacın geniş dalları yağmuru tutuyordu"
   - Cümle 10: «Ağacın geniş dalları yağmuru tutuyordu.»
   - Açıklama: Dallar yağmuru tutmaz; 'yağmurdan koruyordu' anlamında fiil yanlış kullanılmış.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Sepetteki ekmekler kuruydu"
   - Cümle 11: «Sepetteki ekmekler kuruydu.»
   - Açıklama: Ekmeklerin ıslanmaya başladığı söylenmişken sonra hiç ıslanmamış gibi kuru oldukları söyleniyor.
   - Açıklama: Ekmekler ıslanmaya başlamıştı ama sonra kuru oldukları söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0145` birebir aynı, `@degisim: elbise -> sepet` (tutuyorsan), ardından `@onarim: c44eb93cd46bb99abf99ad60682cf15fe3dda9ee`, sonra gövde.

### Hikâye 9: tohum masa-0146 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | Daşa
@tohum: masa-0146
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Daşa
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'biftek', fiil 'tatmak', sıfat 'huzurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | Daşa
@plan: evcilik oyununda biftek yapacak bir şey yoktu | önce bir taşı sonra büyük bir yaprağı denedi
@tohum: masa-0146
Bir sabah Maşa ile Daşa ormanda evcilik oyunu oynuyordu. Daşa oyun için bir biftek istedi. Ama Maşa'nın biftek yapacak hiçbir şeyi yoktu. Maşa hemen bir şeyler denemeye başladı. Önce yuvarlak bir taş buldu ve bir kütüğün üstüne koydu. Ama taş bifteğe hiç benzemiyordu. Sonra büyük, kahverengi bir yaprak aldı. Yaprak tıpkı ince bir biftek gibiydi. Maşa yaprağı iki çubukla çevirdi ve kuzenine uzattı. Daşa bifteği tadıyormuş gibi yaptı ve gülümsedi. Sonra başını salladı ve ellerini çırptı. Maşa çok mutlu ve huzurluydu, çünkü kuzeni oyun bifteğini beğenmişti.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Maşa çok mutlu ve huzurluydu"
   - Cümle 12: «Maşa çok mutlu ve huzurluydu, çünkü kuzeni oyun bifteğini beğenmişti.»
   - Açıklama: 'Huzurlu' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Huzurlu' soyut bir kavram; 3 yaşındaki çocuk bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0146` birebir aynı, ardından `@onarim: b3b9509968b89f61a4862ab33a95e6d1cd15e7de`, sonra gövde.

### Hikâye 10: tohum masa-0147 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0147
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'yastık', fiil 'dinmek', sıfat 'iyi'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: kamp oyununda karnı acıktı ve uyuyamadı | sepetindeki reçelli ekmeği yiyip yeniden uzandı
@tohum: masa-0147
Ormanda Maşa kamp oyunu oynuyordu ve biraz uyumak istiyordu. Yastığını ve sepetini büyük bir ağacın altına koydu. Sonra yastığa uzandı ama karnı guruldamaya başladı, çünkü çok acıkmıştı. Bu sesle gözlerini kapatamadı. Maşa oturdu ve sepetini açtı. İçinden reçelli bir ekmek çıkardı. Ekmeği ağacın altında yavaş yavaş yedi. Parmaklarındaki tatlı reçeli de tek tek yaladı. Son lokmada karnının sesi dindi. Maşa yastığını düzeltti ve yeniden uzandı. Şimdi iyi bir kamp uykusuna hazırdı. Gözlerini kapattı ve kuşları dinledi. Maşa çok mutluydu, çünkü kamp oyunu tam istediği gibi olmuştu.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karnının sesi dindi"
   - Cümle 9: «Son lokmada karnının sesi dindi.»
   - Açıklama: 'Dinmek' yağmur ya da ağrı için kullanılır; ses için 'kesildi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0147` birebir aynı, ardından `@onarim: 9b2c09087438d4cdccd0405cfc63a5d718821bc1`, sonra gövde.

### Hikâye 11: tohum masa-0148 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | dağ | kirpi
@tohum: masa-0148
- yer: dağ (Ormanın yanındaki tepe.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: kirpi
- özellik: reçel (Tatlıları ve reçeli çok sever.)
- kelimeler: isim 'kaya', fiil 'ayrılmak', sıfat 'benekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | dağ | kirpi
@plan: kavanozun kapağı kayanın altındaki dar deliğe girdi | kirpiden kapağı getirmesi için yardım istedi
@tohum: masa-0148
Maşa ile kirpi tepede benekli bir kayanın yanında oturuyordu. Maşa kaşıkla reçel yiyordu, kirpi de elmasını kemiriyordu. Birden kavanozun kapağı yuvarlandı ve kayanın altındaki deliğe girdi. Maşa elini uzattı ama eli dar deliğe sığmadı. Kapak olmazsa kavanoza toz girecekti. Maşa kirpiye döndü. "Kirpi, sen çok küçüksün, bana yardım eder misin?" diye sordu Maşa. Kirpi elmasından ayrıldı ve yavaşça deliğe girdi. Burnuyla kapağı itti ve dışarı çıkardı. Maşa kapağı aldı ve kavanozu sıkıca kapattı. "Çok teşekkürler, kirpi," dedi Maşa. Kirpi de mutlu mutlu burnunu oynattı. Maşa bundan sonra eli bir yere sığmayınca hemen yardım istedi.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Maşa kaşıkla reçel yiyordu"
   - Cümle 2: «Maşa kaşıkla reçel yiyordu, kirpi de elmasını kemiriyordu.»
   - Açıklama: Tohumdaki reçel özelliği yalnız arka planda geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Tohumdaki reçel özelliği yalnız ortam olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden kavanozun kapağı yuvarlandı"
   - Cümle 3: «Birden kavanozun kapağı yuvarlandı ve kayanın altındaki deliğe girdi.»
   - Açıklama: Kapağın neden yuvarlandığı söylenmiyor ve Maşa'nın elinin sığmadığı dar deliğe kirpinin bütün bedeniyle girmesi akla yatkın değil.
3. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Maşa elini uzattı ama eli dar deliğe sığmadı"
   - Cümle 4: «Maşa elini uzattı ama eli dar deliğe sığmadı.»
   - Açıklama: Çocuğun taklit edebileceği biçimde kayanın altındaki dar deliğe el sokuluyor.
   - Açıklama: Kayanın altındaki dar deliğe el sokmak çocuğun taklit edebileceği riskli bir davranıştır.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Maşa bundan sonra eli bir yere sığmayınca hemen yardım istedi"
   - Cümle 13: «Maşa bundan sonra eli bir yere sığmayınca hemen yardım istedi.»
   - Açıklama: 'Bundan sonra' süreklilik bildirdiği halde tek seferlik 'istedi' kullanılmış; 'isterdi' olmalı.
   - Açıklama: 'Bundan sonra' alışkanlık bildirir, fiil 'isterdi' ya da 'istemeye başladı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0148` birebir aynı, ardından `@onarim: c745fe3269f9bffbd1ce0fa8c1ecde937cc0aca7`, sonra gövde.

### Hikâye 12: tohum masa-0150 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Maşa | orman | -
@tohum: masa-0150
- yer: orman (Maşa'nın evinin yakınındaki büyük orman; ağaçlar ve patikalar vardır.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: dene (Çok enerjiktir; her şeyi dener.)
- kelimeler: isim 'zincir', fiil 'saklanmak', sıfat 'çalışkan'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Maşa | orman | -
@plan: papatyaları bağladı ama ince sapı koptu | her sapı parmağıyla deldi ve çiçekleri geçirdi
@tohum: masa-0150
@degisim: saklanmak -> bağlamak
Çalışkan arılar çiçeklerin arasında vızıldıyordu. Maşa ormanda ilk kez papatyalardan bir zincir yapıyordu. Maşa papatyaları birbirine bağladı ama ince sapı hemen koptu. Zincir dağıldı ve çiçekler yere düştü. Maşa durmadı ve başka bir yol denedi. Parmağıyla her sapı ortasından deldi. Sonra bir çiçeği öbür çiçeğin deliğinden geçirdi. Bu kez zincir hiç kopmadı. Maşa bir sürü papatyayı arka arkaya dizdi. Sonra uzun zinciri bir halka yaptı ve başına taç gibi taktı. Maşa bundan sonra papatya zincirini hep böyle yaptı.
```

**Hakem bulguları (4):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "papatyaları bağladı ama ince sapı koptu"
   - Cümle 0 (plan satırı): «papatyaları bağladı ama ince sapı koptu | her sapı parmağıyla deldi ve çiçekleri geçirdi»
   - Açıklama: Plan satırında da çoğul papatyalara tekil 'sapı' bağlanmış.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ama ince sapı hemen koptu"
   - Cümle 3: «Maşa papatyaları birbirine bağladı ama ince sapı hemen koptu.»
   - Açıklama: Çoğul 'papatyaları' ile tekil 'sapı' uyuşmuyor; hangi çiçeğin sapı belirsiz.
   - Açıklama: Çoğul papatyalara tekil iyelik uyumsuz; 'ince sapları' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bağladı ama ince sapı hemen koptu"
   - Cümle 3: «Maşa papatyaları birbirine bağladı ama ince sapı hemen koptu.»
   - Açıklama: Çoğul papatyalardan söz edilirken tekil 'sapı' kullanılmış; 'ince sapları' ya da 'bir papatyanın sapı' olmalı.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "başka bir yol denedi"
   - Cümle 5: «Maşa durmadı ve başka bir yol denedi.»
   - Açıklama: 'Yol denemek' yöntem anlamında mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: masa-0150` birebir aynı, `@degisim: saklanmak -> bağlamak` (tutuyorsan), ardından `@onarim: 0ca7e6dd917cda1077326f50b932919059f44dbc`, sonra gövde.
