# Editör görevi (onarım): Şakir, onarım partisi 27

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar27.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar27.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0051 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0051
- yer: park (Şehirdeki park.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'un', fiil 'susamak', sıfat 'ıslak'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: annesi sürprizi görecekti çünkü su almaya geliyordu | yaprakları şapkasının altına sakladı ve sonra verdi
@tohum: sakir-0051
@degisim: un -> yaprak
Parkta, Şakir annesi Kadriye için ıslak çimenlerden renkli yapraklar topluyordu. Bu yapraklar annesine bir sürpriz olacaktı. Ama susayan Kadriye su almak için yanına geliyordu ve yaprakları görebilirdi. Şakir hemen şapkasını çıkardı ve yaprakları altına sakladı. "Şakir, su şişesi sende mi?" diye sordu Kadriye. "Evet, anneciğim," dedi Şakir ve şişeyi ona verdi. Kadriye suyunu içti ve gülümsedi. "Anne, şimdi gözlerini kapat," dedi Şakir. Kadriye gözlerini kapadı ve Şakir yaprak demetini ona uzattı. "Sürpriz!" dedi Şakir. "Çok teşekkür ederim, Şakir, bu demet çok güzel!" dedi Kadriye.
```

**Hakem bulguları (1):**

1. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "yaprakları şapkasının altına sakladı ve sonra verdi"
   - Cümle 0 (plan satırı): «annesi sürprizi görecekti çünkü su almaya geliyordu | yaprakları şapkasının altına sakladı ve sonra verdi»
   - Açıklama: Planda yaprakları Şakir saklıyor ama gövdede saklayan Kadriye.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0051` birebir aynı, `@degisim: un -> yaprak` (tutuyorsan), ardından `@onarim: 8eaade7270bc40edc8c0a3145482a33c0f001c05`, sonra gövde.

### Hikâye 2: tohum sakir-0057 (deneme 5 -> 6)

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
Rüzgar esiyordu ve Şakir kamp yerinde koşuyordu. Kardeşi Canan örtüde kitap okuyordu. Yanında oyuncak bebeğinin elbisesi vardı. Koşarken Şakir'in ayağı elbiseye takıldı ve elbise rüzgarla uçup kayboldu. Canan çok üzüldü, çünkü oyuncak bebeğinin başka elbisesi yoktu. Şakir hemen durdu ve kardeşinden özür diledi. Şakir macerayı çok severdi, bu yüzden karmakarışık çalılara eğilip baktı. Küçük elbise bir dala takılmıştı. Şakir elbiseyi dikkatle aldı ve Canan'a götürdü. İkisi oyuncak bebeğe elbiseyi birlikte giydirdi. Canan gülümsedi ve Şakir'e sarıldı. Şakir ile Canan oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (4):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Koşarken Şakir'in ayağı elbiseye takıldı"
   - Cümle 4: «Koşarken Şakir'in ayağı elbiseye takıldı ve elbise rüzgarla uçup kayboldu.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede ortaya çıkıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 7: «Şakir macerayı çok severdi, bu yüzden karmakarışık çalılara eğilip baktı.»
   - Açıklama: 'Macera' ve 'karmakarışık' 3 yaşındaki çocuk için soyut ve zor kelimeler.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "karmakarışık çalılara eğilip"
   - Cümle 7: «Şakir macerayı çok severdi, bu yüzden karmakarışık çalılara eğilip baktı.»
   - Açıklama: 'Karmakarışık' kelimesini 3 yaşındaki bir çocuk bilmez.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şakir ile Canan oyunlarına mutlu mutlu devam etti"
   - Cümle 12: «Şakir ile Canan oyunlarına mutlu mutlu devam etti.»
   - Açıklama: Canan oyun oynamıyor, kitap okuyordu; oyunlarına devam etmeleri başlangıçla çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0057` birebir aynı, `@degisim: pirinç -> elbise` (tutuyorsan), ardından `@onarim: 2185da2fe037988b6cd3ca06158a1677c6a2a3bb`, sonra gövde.

### Hikâye 3: tohum sakir-0059 (deneme 5 -> 6)

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
@plan: rüzgar kardeşinin kazağını götürdü ve kumda iz kaldı | iz boyunca yürüdü ve şapkasıyla kumu kazdı
@tohum: sakir-0059
@degisim: giysi -> kazak
Deniz kıyısında rüzgar esiyordu ve hava biraz soğumuştu. Şakir ile Canan kumda oynuyordu. Canan havluya bıraktığı kazağını giymek istedi. Ama rüzgar kazağı havludan alıp götürmüştü. Kumda uzun, ince bir iz vardı. "Bu iz nereye gidiyor?" diye sordu Şakir. "Sabırlı olalım ve yavaşça yürüyüp bakalım," dedi Canan. İkisi iz boyunca adım adım yürüdü. İz küçük bir çukurda bitti. Kumun altından kazağın bir kolu görünüyordu. Şakir şapkasını çıkardı ve onunla kumu kazdı. Canan'ın kazağı çukurdan çıktı. "İzi kumda giden kazağın yapmış!" dedi Şakir. Canan kazağını silkti ve giydi. İkisi de çok sevindi, çünkü kazağı bulmuşlardı.
```

**Hakem bulguları (5):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Canan havluya bıraktığı kazağını giymek istedi.»
   - Açıklama: Kazağın kaybolduğu sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama rüzgar kazağı havludan alıp götürmüştü"
   - Cümle 4: «Ama rüzgar kazağı havludan alıp götürmüştü.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
   - Açıklama: Sorun ilk üç cümlede değil dördüncü cümlede söyleniyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Sabırlı olalım ve yavaşça yürüyüp bakalım"
   - Cümle 7: «"Sabırlı olalım ve yavaşça yürüyüp bakalım," dedi Canan.»
   - Açıklama: İzi takip etme çözümünü figür Şakir değil yan karakter Canan öneriyor.
   - Açıklama: İzi takip etme çözümünü figür değil yan karakter Canan buluyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kumun altından kazağın bir kolu görünüyordu"
   - Cümle 10: «Kumun altından kazağın bir kolu görünüyordu.»
   - Açıklama: Rüzgarın kazağı kumda iz bırakarak sürükleyip çukura gömmesi akla yatkın değil.
5. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "İzi kumda giden kazağın yapmış!"
   - Cümle 13: «"İzi kumda giden kazağın yapmış!" dedi Şakir.»
   - Açıklama: Cümle dizilişi ve iyelik bozuk; 'Bu izi kumda sürüklenen kazağın yapmış' gibi olmalı.
   - Açıklama: Cümle dilbilgisel olarak bozuk; 'Bu izi kumda sürüklenen kazağın yapmış!' gibi olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0059` birebir aynı, `@degisim: giysi -> kazak` (tutuyorsan), ardından `@onarim: c1ee711e28ac5c94cce27f91c032c7b49d876f26`, sonra gövde.

### Hikâye 4: tohum sakir-0060 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0060
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: sırayla oynamak
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'altın', fiil 'birleşmek', sıfat 'turuncu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: tek bir turuncu kova vardı ve ikisi de istedi | kovayı sırayla kullanmayı önerdi
@tohum: sakir-0060
Şakir kumsalda Necati ile oynuyordu. Oyuncak altın için kumdan büyük bir kale yapacaklardı. Ama tek bir turuncu kova vardı ve ikisi de onu istedi. Şakir macerayı çok severdi, bu yüzden oyunun durmasını istemedi. "Necati, kovayı sırayla dolduralım mı?" diye sordu Şakir. "Olur, önce sen başla," dedi Necati. Şakir kovayı kumla doldurdu ve sol yanda bir kule yaptı. Sonra Necati kovayı aldı ve sağ yana ikinci bir kule dikti. Kuleler büyüdükçe duvarları ortada birleşti. Şakir oyuncak altını kalenin ortasına koydu. "Ne güzel bir kale oldu, Şakir!" dedi Necati. Şakir çok sevindi, çünkü birlikte kocaman bir kale yapmışlardı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 4: «Şakir macerayı çok severdi, bu yüzden oyunun durmasını istemedi.»
   - Açıklama: 'Macera' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden oyunun durmasını istemedi"
   - Cümle 4: «Şakir macerayı çok severdi, bu yüzden oyunun durmasını istemedi.»
   - Açıklama: Tohumdaki macera özelliği kovayı paylaşma çözümüne işe yaramadan, yalnız söylenerek ekleniyor.
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak söyleniyor, kovayı sırayla kullanma çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0060` birebir aynı, ardından `@onarim: 521cc7abc0d78e5bd4af3d9f7d40095df7b168bf`, sonra gövde.

### Hikâye 5: tohum sakir-0069 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0069
- yer: park (Şehirdeki park.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'meşe', fiil 'sallamak', sıfat 'işaretli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | -
@plan: parkta çok ağaç vardı ve kağıttaki ağacı bulamadı | yapraklara bakıp kağıttaki meşe ağacını buldu
@tohum: sakir-0069
Bir sabah Şakir parkta yaprak toplama oyunu oynuyordu. Elindeki işaretli kağıtta büyük yapraklı bir meşe ağacı vardı. Şakir oyunda bu ağacın bir yaprağını kağıdına koymak istiyordu. Ama parkta çok ağaç vardı ve Şakir o ağacı hemen bulamadı. Şakir macerayı çok severdi, bu yüzden ağaçları tek tek gezdi. Ağaçların yapraklarına dikkatle baktı. Sonunda kağıttaki yapraklara benzeyen bir ağaç gördü. Alçak bir dalı hafifçe salladı ve birkaç yaprak eline düştü. Yapraklar kağıttaki resmin aynısıydı ve bu ağaç bir meşe ağacıydı. Şakir en güzel yaprağı kağıdının üstüne koydu. Sonra oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (6):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "işaretli kağıtta büyük yapraklı bir meşe ağacı vardı"
   - Cümle 2: «Elindeki işaretli kağıtta büyük yapraklı bir meşe ağacı vardı.»
   - Açıklama: Kağıtta ağaç değil ağacın resmi olur; 'işaretli' de anlamı belirsiz.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Elindeki işaretli kağıtta"
   - Cümle 2: «Elindeki işaretli kağıtta büyük yapraklı bir meşe ağacı vardı.»
   - Açıklama: Kağıtta işaret değil ağaç resmi var; 'işaretli' kelimesi yerinde kullanılmamış.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama parkta çok ağaç vardı"
   - Cümle 4: «Ama parkta çok ağaç vardı ve Şakir o ağacı hemen bulamadı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.
4. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "bu yüzden ağaçları tek tek gezdi"
   - Cümle 5: «Şakir macerayı çok severdi, bu yüzden ağaçları tek tek gezdi.»
   - Açıklama: Güvenli özellik kullanımı satırına göre Şakir tek başına uzağa gitmez, ama parkta yalnız ağaç ağaç dolaşıyor.
5. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi, bu yüzden ağaçları tek tek gezdi.»
   - Açıklama: 'Macera' 3 yaşındaki çocuk için soyut bir kavram.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden ağaçları tek tek gezdi"
   - Cümle 5: «Şakir macerayı çok severdi, bu yüzden ağaçları tek tek gezdi.»
   - Açıklama: Ağaçları gezmenin sebebi aramak iken macera sevgisine zorla bağlanıyor; nedensellik yapay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0069` birebir aynı, ardından `@onarim: 92dab6dd126060246fbff6215346df098d196ebd`, sonra gövde.

### Hikâye 6: tohum sakir-0070 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0070
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'ruj', fiil 'dokunmak', sıfat 'şirin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: şirin bir kabuk ağır bir kütüğün altında kaldı | yardım istedi ve fil kütüğü kenara itti
@tohum: sakir-0070
@degisim: ruj -> kütük
Denizden serin bir rüzgar esiyordu. Şakir, Necati ile kumsalda macera oyunu oynuyor ve kabuk arıyordu. Birden şirin, pembe bir kabuk gördü ama kabuk ağır bir kütüğün altındaydı. Şakir kütüğü iki eliyle çekti ama kütük hiç kıpırdamadı. "Necati, bana yardım eder misin?" diye sordu Şakir. Necati hortumuyla kütüğü kolayca kenara itti. Şakir kabuğu aldı ve ona parmağıyla yavaşça dokundu. Kabuğun içi çok parlaktı. "Çok güzel bir kabuk buldun, Şakir," dedi Necati. "Teşekkürler, Necati, bu kabuğu hep saklayacağım!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "kumsalda macera oyunu oynuyor"
   - Cümle 2: «Şakir, Necati ile kumsalda macera oyunu oynuyor ve kabuk arıyordu.»
   - Açıklama: Tohumdaki macera özelliği yalnız etiket olarak anılıyor, sorunun çözümünde işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0070` birebir aynı, `@degisim: ruj -> kütük` (tutuyorsan), ardından `@onarim: bd96a353f10f4484bb457b28c68890255ccefc49`, sonra gövde.

### Hikâye 7: tohum sakir-0071 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0071
- yer: park (Şehirdeki park.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ceket', fiil 'bindirmek', sıfat 'soslu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: kumdan pasta yapmak için kalıbı yoktu | şapkasını kalıp olarak kullandı
@tohum: sakir-0071
@degisim: bindirmek -> dökmek
Şakir parkta kum havuzunda yemek oyunu oynuyordu. Kum yağmurdan ıslaktı ve Şakir ceketini kirletmemek için çıkarıp kenara koydu. Şakir büyük bir pasta yapmak istedi ama kalıbı yoktu. Kum elinde dağılıyor ve hiç yuvarlak olmuyordu. Şakir biraz düşündü ve şapkasını çıkardı. Şapkayı ıslak kumla doldurdu ve sıkıca bastırdı. Sonra şapkayı ters çevirdi ve yavaşça kaldırdı. Kumda yuvarlak bir pasta duruyordu. Şakir onun üstüne sos gibi ince kum döktü. Böylece güzel, soslu bir kum pastası oldu. Şakir bundan sonra kalıp bulamayınca yanındaki eşyalara bakardı.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir ceketini kirletmemek için çıkarıp kenara koydu"
   - Cümle 2: «Kum yağmurdan ıslaktı ve Şakir ceketini kirletmemek için çıkarıp kenara koydu.»
   - Açıklama: Ceket özenle kuruluyor ama olayda hiç kullanılmıyor ve şapkasını kumla doldurması bu özenle de uyuşmuyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ceketini kirletmemek için çıkarıp kenara koydu"
   - Cümle 2: «Kum yağmurdan ıslaktı ve Şakir ceketini kirletmemek için çıkarıp kenara koydu.»
   - Açıklama: Ceket ayrıntısı kuruluyor ama olayda hiçbir işe yaramıyor.
3. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "kalıp bulamayınca yanındaki eşyalara bakardı"
   - Cümle 11: «Şakir bundan sonra kalıp bulamayınca yanındaki eşyalara bakardı.»
   - Açıklama: Anlatım -dı'lı geçmişten alışkanlık bildiren -ardı biçimine kayıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0071` birebir aynı, `@degisim: bindirmek -> dökmek` (tutuyorsan), ardından `@onarim: 43bed218f81fd62d772ac2c0bf054aa92a711e1c`, sonra gövde.

### Hikâye 8: tohum sakir-0072 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0072
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: kaybolan eşya
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'bulmaca', fiil 'eğilmek', sıfat 'kremalı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: kalem kütüğün yanında yaprakların arasında kayboldu | yere eğilip yaprakları kaldırdı ve kalemi buldu
@tohum: sakir-0072
Şakir babası Remzi ile kamp yerinde bir bulmaca yapıyordu. Bulmaca bitince Remzi ona kremalı bir kek verecekti. Ama Şakir'in kalemi elinden kaydı ve kütüğün yanında kayboldu. "Baba, kalemimi ben bulurum!" dedi Şakir. Şakir yere eğildi ve kütüğün yanına baktı. Orada bir sürü kuru yaprak vardı. Şakir macerayı çok severdi, bu yüzden yaprakları tek tek kaldırdı. Kalem bir yaprağın altında duruyordu. Şakir kalemi aldı ve bulmacanın son kelimesini yazdı. "Bulmaca bitti, baba!" dedi Şakir. Remzi gülerek ona keki verdi. Şakir çok sevindi, çünkü kalemini kendisi bulmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden"
   - Cümle 7: «Şakir macerayı çok severdi, bu yüzden yaprakları tek tek kaldırdı.»
   - Açıklama: Yaprak kaldırmak macera sevgisiyle açıklanmış; özellik kelimesi yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 7: «Şakir macerayı çok severdi, bu yüzden yaprakları tek tek kaldırdı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macerayı çok severdi, bu yüzden"
   - Cümle 7: «Şakir macerayı çok severdi, bu yüzden yaprakları tek tek kaldırdı.»
   - Açıklama: Yaprakları kaldırmanın sebebi olarak maceracılık uyduruluyor; sebep-sonuç bağı yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0072` birebir aynı, ardından `@onarim: 8302b37ab75bd5f346db7ab45463fb684b75bd0e`, sonra gövde.

### Hikâye 9: tohum sakir-0073 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0073
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'başörtüsü', fiil 'buluşmak', sıfat 'güneşli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: çiçek eğilmişti çünkü toprağı çok kuruydu | çeşmeden su getirip çiçeği suladı
@tohum: sakir-0073
@degisim: başörtüsü -> çiçek
Güneşli bir sabah Şakir parkta yürüyordu. Birden bankın yanında küçük, sarı bir çiçek gördü. Çiçek yere doğru eğilmişti, çünkü toprağı çok kuruydu. Şakir çiçeğe su vermek istedi. Şakir macerayı çok severdi ve hemen su aramaya başladı. Çiçeğe yakın, iki yolun buluştuğu yerde bir çeşme buldu. Ellerine su doldurdu. Yavaşça yürüdü ve suyu çiçeğin dibine boşalttı. Sonra bir kez daha gidip su getirdi. Toprak ıslandı ve çiçek yavaş yavaş doğruldu. Sarı yaprakları güneşte parladı. Şakir bundan sonra toprağı kuru bir çiçek görünce ona su getirdi.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi ve hemen su aramaya başladı.»
   - Açıklama: 'Macera' soyut bir kavram ve 3 yaşındaki çocuğa uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "macerayı çok severdi ve hemen su aramaya başladı"
   - Cümle 5: «Şakir macerayı çok severdi ve hemen su aramaya başladı.»
   - Açıklama: Tohumdaki macera özelliği yalnız söyleniyor, çiçek sulamada işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi ve hemen su aramaya başladı.»
   - Açıklama: Tohumdaki macera özelliği kartta söylendiği gibi cümleyle sayılıyor, yakındaki çeşmeden su getirmek bir maceraya dönüşmüyor.
4. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "kuru bir çiçek görünce ona su getirdi"
   - Cümle 12: «Şakir bundan sonra toprağı kuru bir çiçek görünce ona su getirdi.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılıyor ama fiil tek seferlik -dı'lı; 'getirirdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0073` birebir aynı, `@degisim: başörtüsü -> çiçek` (tutuyorsan), ardından `@onarim: fe2fba926820afe70f5831d7d57fd7e08b1831ed`, sonra gövde.

### Hikâye 10: tohum sakir-0075 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0075
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Necati
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'cüzdan', fiil 'köpürmek', sıfat 'yeni'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: fil çok hızlı üfledi ve köpükler uçtu | ondan yavaşça üflemesini istedi ve kova köpükle doldu
@tohum: sakir-0075
@degisim: cüzdan -> kova
Ormanda kamp yerinde Şakir ile Fil Necati bir kova sabunlu suyla oynuyordu. Bu yeni oyunda kova köpükle dolacaktı. Ama Necati hortumuyla suya çok hızlı üfledi ve köpükler havaya uçtu. Köpükler Necati'nin başına kondu ve kovada hiç köpük kalmadı. Şakir macerayı çok severdi ve oyunu bırakmak istemedi. "Necati, bu kez hafifçe üfle," dedi Şakir. Necati hortumunu suya soktu ve öyle yaptı. Su yavaş yavaş köpürdü. Beyaz köpük kovanın ağzına kadar çıktı. "Bak, Şakir, kova doldu!" dedi Necati. İkisi köpüklerle oynamaya mutlu mutlu devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macerayı çok severdi"
   - Cümle 5: «Şakir macerayı çok severdi ve oyunu bırakmak istemedi.»
   - Açıklama: 'Macera' 3 yaşındaki bir çocuğun bilmediği soyut bir kavram.
   - Açıklama: 'Macera' soyut bir kavram; 3 yaşındaki çocuk için uygun değil.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "macerayı çok severdi ve oyunu bırakmak istemedi"
   - Cümle 5: «Şakir macerayı çok severdi ve oyunu bırakmak istemedi.»
   - Açıklama: Tohumdaki macera özelliği yalnız söyleniyor, köpük oyununda işe yarar biçimde kullanılmıyor.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir macerayı çok severdi ve oyunu bırakmak istemedi"
   - Cümle 5: «Şakir macerayı çok severdi ve oyunu bırakmak istemedi.»
   - Açıklama: Tohumdaki macera özelliği yalnız söylenip geçiliyor; çözümde işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0075` birebir aynı, `@degisim: cüzdan -> kova` (tutuyorsan), ardından `@onarim: d17c6ae7b406de48b9c411acd00bec6b72c403a1`, sonra gövde.

### Hikâye 11: tohum sakir-0076 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0076
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tost', fiil 'koşuşturmak', sıfat 'sevecen'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: kumdan nereden geldiği bilinmeyen ince bir ses geldi | sesin geldiği yere bakıp sesi yapan kabuğu buldu
@tohum: sakir-0076
@degisim: sevecen -> neşeli
Şakir babası Remzi ile kumsalda tost yiyordu. Birden kumdan ince bir ses geldi. Şakir bu sesin nereden geldiğini çok merak etti. Şakir macerayı çok severdi ve sesi bulmak istedi. Tostunu bitirdi ve kumda yavaş yavaş yürüdü. Ses yakındaki bir kum tepesinin arkasından geliyordu. Şakir oraya baktı ve kumda büyük bir kabuk gördü. Rüzgar kabuğun deliğine esince ince bir ses çıkıyordu. "Baba, gel, sesi bu kabuk yapıyor!" dedi Şakir. Remzi geldi ve kabuğu dinledi. "Ne güzel buldun, Şakir," dedi Remzi neşeli bir sesle. Sonra ikisi kumda koşuşturdu ve güldü. Şakir çok sevindi, çünkü sesin nereden geldiğini bulmuştu.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "nereden geldiği bilinmeyen ince bir ses geldi"
   - Cümle 0 (plan satırı): «kumdan nereden geldiği bilinmeyen ince bir ses geldi | sesin geldiği yere bakıp sesi yapan kabuğu buldu»
   - Açıklama: Plan satırında 'geldiği ... geldi' gereksiz tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0076` birebir aynı, `@degisim: sevecen -> neşeli` (tutuyorsan), ardından `@onarim: 9cd1fab8d27bea9e50f8998259a35ed9f567c513`, sonra gövde.

### Hikâye 12: tohum sakir-0078 (deneme 3 -> 4)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | orman | -
@tohum: sakir-0078
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'karton', fiil 'çağırmak', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | -
@plan: kozalaklar yolda yere döküldü ve oyun durdu | şapkasını ters çevirip kozalakları içinde taşıdı
@tohum: sakir-0078
@degisim: çağırmak -> taşımak
Şakir kamp yerinde karton bir aslanla komik bir oyun oynuyordu. Oyunda aslan çok acıkmıştı ve ağzı delikti. Şakir kozalakları kucağında getirdi ama yolda hepsi yere döküldü. Şakir bir daha denedi ama kozalaklar yine düştü. Oyun durdu ve Şakir üzüldü. Sonra şapkasını çıkardı ve ters çevirdi. Kozalakları tek tek şapkanın içine koydu. Dolu şapkayı hiç düşürmeden aslanın yanına taşıdı. Şakir cömert davrandı ve en büyük kozalakları aslanın ağzına attı. Şakir çok eğlendi, çünkü oyununa yeniden devam edebilmişti.
```

**Hakem bulguları (6):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir kamp yerinde karton"
   - Cümle 1: «Şakir kamp yerinde karton bir aslanla komik bir oyun oynuyordu.»
   - Açıklama: Güvenli kullanım satırına göre Şakir tek başına uzağa gitmez, burada şehir dışındaki dağ kampında yanında kimse yokken oynuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "aslan çok acıkmıştı ve ağzı delikti"
   - Cümle 2: «Oyunda aslan çok acıkmıştı ve ağzı delikti.»
   - Açıklama: 'Ağzı delikti' delinmiş anlamına gelir; 'ağzı bir delikti' kastediliyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Şakir kozalakları kucağında getirdi ama yolda hepsi yere döküldü"
   - Cümle 3: «Şakir kozalakları kucağında getirdi ama yolda hepsi yere döküldü.»
   - Açıklama: Kozalakların neden iki kez döküldüğü açıkça söylenmiyor; sorunun sebebi belirsiz kalıyor.
4. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yolda hepsi yere döküldü"
   - Cümle 3: «Şakir kozalakları kucağında getirdi ama yolda hepsi yere döküldü.»
   - Açıklama: Kucaktan dökülen kozalaklar şapkaya toplanıp bitiyor; sorun önemsiz ve kucağa sığmama sebebi zayıf.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir cömert davrandı"
   - Cümle 9: «Şakir cömert davrandı ve en büyük kozalakları aslanın ağzına attı.»
   - Açıklama: Tohumdaki özellik şapka; cömertlik karttaki özelliklere ikinci bir özellik olarak ekleniyor.
6. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "oyununa yeniden devam edebilmişti"
   - Cümle 10: «Şakir çok eğlendi, çünkü oyununa yeniden devam edebilmişti.»
   - Açıklama: 'Yeniden devam' gereksiz tekrar içeriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0078` birebir aynı, `@degisim: çağırmak -> taşımak` (tutuyorsan), ardından `@onarim: 31abdbfa20ea8b528fc4d29d7d35df06b71314a8`, sonra gövde.
