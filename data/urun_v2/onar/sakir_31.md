# Editör görevi (onarım): Şakir, onarım partisi 31

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar31.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar31.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0085 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0085
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kumbara', fiil 'geçmek', sıfat 'kirli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: yağmur yağmıştı ve ağaca giden yolda çamur vardı | düz taşları çamura koyup karşıya geçti
@tohum: sakir-0085
@degisim: kumbara -> kutu
Şakir ile babası Remzi ormandaki kamp yerinde hazine oyunu oynuyordu. Remzi büyük bir ağacın dibine bir hazine kutusu saklamıştı. Ama yağmur yağmıştı ve ağaca giden yolda büyük bir çamur vardı. Şakir çamurdan geçerse ayakları kirli olacaktı. Çamurun kenarında düz taşlar gördü. Şakir macera oyunlarını hatırladı ve taşlardan bir yol yapmayı düşündü. Taşları tek tek topladı ve çamurun içine sıra sıra dizdi. Taşların üstüne basarak karşıya geçti. Remzi de onun arkasından geldi. Şakir ağacın dibinde hazine kutusunu buldu. Kutuyu açtı ve içinde iki kurabiye gördü. Kurabiyelerden birini babasına verdi. Sonra ikisi ağacın dibine oturdu ve kurabiyelerini mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macera oyunlarını hatırladı"
   - Cümle 6: «Şakir macera oyunlarını hatırladı ve taşlardan bir yol yapmayı düşündü.»
   - Açıklama: 'Macera' soyut ve 3 yaşındaki bir çocuğun bilmeyebileceği bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0085` birebir aynı, `@degisim: kumbara -> kutu` (tutuyorsan), ardından `@onarim: ec2ae08dcdf3ea600a9b35d0dcdc389cbf90dcfd`, sonra gövde.

### Hikâye 2: tohum sakir-0086 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0086
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: paylaşmak
- yan: Canan
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'kumaş', fiil 'çiğnemek', sıfat 'paslı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: güneş çok parlaktı ve kardeşi okuyamadı | kumaştan gölgeli küçük bir çadır kurdu
@tohum: sakir-0086
@degisim: çiğnemek -> okumak
Ormandaki kamp yerinde Şakir ile kardeşi Canan vardı. Canan paslı bir sandalyede kitap okumak istedi. Ama güneş çok parlaktı ve Canan yazıları göremedi. Şakir yerde geniş bir kumaşın üstünde oturuyordu. Şakir macera oyunlarını hatırladı ve kumaştan bir çadır yapmayı düşündü. Kalktı ve kumaşın iki ucunu iki alçak dala sıkıca bağladı. Böylece sandalyenin üstüne küçük bir çadır kurdu. Çadırın altı serin oldu. Canan kitabını rahatça okudu. Şakir de çadıra girdi ve kardeşinin yanına oturdu. İkisi kitaptaki resimlere birlikte baktı. Şakir kumaşını paylaşınca ikisi de gölgede oturabildi.
```

**Hakem bulguları (5):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Ormandaki kamp yerinde Şakir ile kardeşi Canan vardı"
   - Cümle 1: «Ormandaki kamp yerinde Şakir ile kardeşi Canan vardı.»
   - Açıklama: Güvenli kullanım satırına göre Şakir tek başına uzağa gitmez; iki çocuk şehir dışındaki kamp yerinde yetişkinsiz kalıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir yerde geniş bir kumaşın üstünde oturuyordu"
   - Cümle 4: «Şakir yerde geniş bir kumaşın üstünde oturuyordu.»
   - Açıklama: Çözümü sağlayan kumaş sorun söylendikten hemen sonra sebepsizce beliriyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macera oyunlarını hatırladı"
   - Cümle 5: «Şakir macera oyunlarını hatırladı ve kumaştan bir çadır yapmayı düşündü.»
   - Açıklama: 'Macera' soyut bir kelime ve 3 yaşındaki bir çocuk bilmeyebilir.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Çadırın altı serin oldu"
   - Cümle 8: «Çadırın altı serin oldu.»
   - Açıklama: İçine girilen bir çadır için 'altı' uygun değil; 'Çadırın içi' ya da 'gölgesi' olmalı.
5. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Şakir kumaşını paylaşınca ikisi de gölgede oturabildi"
   - Cümle 12: «Şakir kumaşını paylaşınca ikisi de gölgede oturabildi.»
   - Açıklama: Hikaye gölge kurma üzerine iken son cümle olaydan tam çıkmayan bir paylaşma dersiyle kapanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0086` birebir aynı, `@degisim: çiğnemek -> okumak` (tutuyorsan), ardından `@onarim: 9593ff0b6042f69889f44f8d6dbb6537adb03db7`, sonra gövde.

### Hikâye 3: tohum sakir-0088 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Remzi
@tohum: sakir-0088
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Remzi
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'tebeşir', fiil 'sıçratmak', sıfat 'plastik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Remzi
@plan: kayanın arkasından garip bir ses geldi | babasıyla kayanın arkasına gidip sesi yapan kovayı buldu
@tohum: sakir-0088
Rüzgar esiyordu ve dalgalar kıyıya vuruyordu. Şakir kumsalda babası Remzi'yle taşlara tebeşirle resim çiziyordu. Birden büyük kayanın arkasından "tak tak" diye garip bir ses geldi. Şakir bu sesi çok merak etti. "Baba, macera oyunu gibi sesi bulalım mı?" diye sordu Şakir. Remzi güldü ve Şakir'in elini tuttu. İkisi birlikte kayanın arkasına yürüdü. Orada mavi, plastik bir kova vardı. Dalgalar kovaya su sıçratıyordu ve kova kayaya çarpıyordu. "Bu kova bizim, rüzgar onu buraya getirmiş!" dedi Remzi. Şakir kovayı aldı ve ikisi resimlerin yanına geri döndü. "Kovayı bulduk, baba, şimdi kumdan kale yapalım!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "macera oyunu gibi sesi bulalım"
   - Cümle 5: «"Baba, macera oyunu gibi sesi bulalım mı?" diye sordu Şakir.»
   - Açıklama: 'Macera oyunu gibi sesi bulalım' yapısı bozuk; neyin neye benzetildiği anlaşılmıyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "macera oyunu gibi sesi"
   - Cümle 5: «"Baba, macera oyunu gibi sesi bulalım mı?" diye sordu Şakir.»
   - Açıklama: 'Macera oyunu gibi sesi bulmak' soyut ve anlamı belirsiz bir benzetme.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0088` birebir aynı, ardından `@onarim: e7988e742137ffd51301685cfd7d15b40b3c3851`, sonra gövde.

### Hikâye 4: tohum sakir-0091 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | Kadriye
@tohum: sakir-0091
- yer: park (Şehirdeki park.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'fermuar', fiil 'sakinleşmek', sıfat 'düzenli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | park | Kadriye
@plan: bir yaprak fermuara sıkıştı ve çanta kapanmadı | annesinden yardım isteyip büyük yaprağı şapkasına taktı
@tohum: sakir-0091
Şakir parkta annesi Kadriye'yle renkli yapraklar topluyordu. Yaprakları çantasına tek tek, düzenli diziyordu. Ama büyük bir yaprak fermuara sıkıştı ve çanta kapanmadı. Şakir önce kızdı, sonra derin bir nefes alıp sakinleşti. "Anneciğim, fermuar sıkıştı, yardım eder misin?" diye sordu Şakir. "Tabii, Şakir," dedi Kadriye. Kadriye yaprağı yavaşça çekip çıkardı. Büyük yaprak bir daha sıkışmasın diye Şakir onu şapkasına taktı. Sonra çantayı kolayca kapattı. "Teşekkürler, anneciğim, bütün yapraklar burada!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Şakir onu şapkasına taktı"
   - Cümle 8: «Büyük yaprak bir daha sıkışmasın diye Şakir onu şapkasına taktı.»
   - Açıklama: Sorunu Kadriye çözüyor; tohumdaki şapka özelliği işe yarar biçimde kullanılmayıp süs olarak kalıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0091` birebir aynı, ardından `@onarim: 571b7ef4ab5d21badd2c9973a5bb99fdec1e5fc0`, sonra gövde.

### Hikâye 5: tohum sakir-0092 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0092
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kadriye
- özellik: macera (Macerayı çok sever.)
- kelimeler: isim 'ip', fiil 'savrulmak', sıfat 'çevik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: perde savruldu ve yumağı koltuğun altına düşürdü | yere uzanıp ipi çekti ve yumağı çıkardı
@tohum: sakir-0092
@degisim: çevik -> uzun
Şakir evde annesi Kadriye'nin yanında oturuyordu. Kadriye, Şakir için mavi bir atkı örüyordu. Birden rüzgar esti, perde savruldu ve yumağı koltuğun altına düşürdü. "Şakir, yumak olmadan atkı bitmez," dedi Kadriye. Şakir macera oyunlarını hatırladı, yere uzandı ve koltuğun altına baktı. Yumak çok içerideydi ama uzun bir ip dışarıda duruyordu. Şakir ipi yavaşça çekti ve yumak önüne yuvarlandı. "İşte buldum, anneciğim!" dedi Şakir. Kadriye yumağı aldı ve güldü. "Teşekkürler, Şakir, şimdi örmeye devam edebilirim," dedi Kadriye. Şakir çok sevindi, çünkü annesine yardım etmişti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Şakir macera oyunlarını hatırladı"
   - Cümle 5: «Şakir macera oyunlarını hatırladı, yere uzandı ve koltuğun altına baktı.»
   - Açıklama: 'Macera oyunları' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Şakir macera oyunlarını hatırladı"
   - Cümle 5: «Şakir macera oyunlarını hatırladı, yere uzandı ve koltuğun altına baktı.»
   - Açıklama: Macera oyunlarını hatırlamak olayda hiçbir işe yaramayan, sebepsiz eklenmiş bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0092` birebir aynı, `@degisim: çevik -> uzun` (tutuyorsan), ardından `@onarim: 5da4e7c39293e6986cde8bd89878cf5100b60a0a`, sonra gövde.

### Hikâye 6: tohum sakir-0100 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Remzi
@tohum: sakir-0100
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Remzi
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yün', fiil 'sunmak', sıfat 'çilekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | orman | Remzi
@plan: kavanozun kapağı çok sıkıydı ve açılmadı | babasından yardım isteyip kapağı yün şapkayla çevirdi
@tohum: sakir-0100
Şakir kamp yerinde babasına çilekli bisküvi sunmak istedi. Ama kavanozun kapağı çok sıkıydı. Şakir kapağı çevirdi ama elleri kaydı ve kapak açılmadı. "Baba, kavanozu tutar mısın?" diye sordu Şakir. Babası Remzi kavanozu iki eliyle sıkıca tuttu. Şakir de yün şapkasıyla kapağı tuttu ve çevirdi. Yün kaymadı ve kapak bu kez döndü. Kavanoz sonunda açıldı. Şakir babasına bir bisküvi uzattı. "Teşekkürler, Şakir, bisküvi çok güzel kokuyor!" dedi Remzi. İkisi çadırın önünde oturup bisküvileri yedi. Şakir çok sevindi, çünkü kavanozu babasıyla birlikte açmıştı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "babasına çilekli bisküvi sunmak"
   - Cümle 1: «Şakir kamp yerinde babasına çilekli bisküvi sunmak istedi.»
   - Açıklama: 'Sunmak' 3 yaşındaki bir çocuğun bilmediği resmi bir kelime; 'vermek' olmalı.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Yün kaymadı ve kapak"
   - Cümle 7: «Yün kaymadı ve kapak bu kez döndü.»
   - Açıklama: Kayan ya da kaymayan şey yün değil şapka veya el; fiil öznesine tam uymuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0100` birebir aynı, ardından `@onarim: 3e2fdba06ffa3713889c0fd9d3b3575414c3e5a0`, sonra gövde.

### Hikâye 7: tohum sakir-0101 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Canan
@tohum: sakir-0101
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: bir şey yapmak
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ağaç', fiil 'süzülmek', sıfat 'hevesli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Canan
@plan: rüzgar esti ve küçük evin çatısı uçtu | şapkasını evin üstüne yeni çatı olarak koydu
@tohum: sakir-0101
Şakir ile Canan kamp yerinde bir ağacın dibine küçük bir ev yapıyordu. Evin duvarları dallardan yapılmıştı, çatısı da büyük bir yapraktı. Ama birden rüzgar esti ve çatı havada süzüldü. "Evimizin çatısı gitti, Şakir," dedi Canan. Şakir biraz düşündü ve şapkasını çıkardı. Şapkayı evin üstüne yavaşça yerleştirdi. Şapka yapraktan ağırdı ve rüzgarda uçmadı. Yeni çatı evi tam kapattı. Canan çok hevesliydi ve evin önüne küçük taşlar dizdi. "Şapkalı evimiz çok güzel oldu, Şakir!" dedi Canan.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Canan çok hevesliydi ve evin önüne küçük taşlar dizdi"
   - Cümle 9: «Canan çok hevesliydi ve evin önüne küçük taşlar dizdi.»
   - Açıklama: Taş dizme ayrıntısı sorunla ya da çözümle bağlantısız, işlevsiz bir olay.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0101` birebir aynı, ardından `@onarim: a68323ade2a0cbb092175b2f8d3b74e1e2055f7e`, sonra gövde.

### Hikâye 8: tohum sakir-0104 (deneme 2 -> 3)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0104
- yer: park (Şehirdeki park.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'külah', fiil 'gülmek', sıfat 'ferah'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | park | -
@plan: rüzgar düşen yaprakları hep uzağa götürdü | şapkasını ters çevirip yaprakları içine yakaladı
@tohum: sakir-0104
@degisim: ferah -> geniş
Park geniş ve serindi. Şakir ağaçtan sarı yaprakların yavaş yavaş düştüğünü fark etti. Bir yaprağı yere düşmeden yakalamak istedi ama rüzgar yaprakları hep götürdü. Şakir ellerine baktı ve şapkasını çıkardı. Şapkayı ters çevirip bir dondurma külahı gibi tuttu. Sonra ağacın altında sessizce bekledi. Bir yaprak süzülerek şapkanın içine düştü. Şakir sevinçle güldü. Az sonra şapkaya iki sarı yaprak daha girdi. Şakir üç yaprağı dikkatle çimenlerin üstüne dizdi. Şakir bundan sonra yaprak yakalarken şapkasını ters tuttu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yaprakları içine yakaladı"
   - Cümle 0 (plan satırı): «rüzgar düşen yaprakları hep uzağa götürdü | şapkasını ters çevirip yaprakları içine yakaladı»
   - Açıklama: 'İçine yakalamak' dilbilgisel olarak bozuk; 'yaprakları içinde yakaladı' ya da 'yaprakları içine topladı' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "rüzgar yaprakları hep götürdü"
   - Cümle 3: «Bir yaprağı yere düşmeden yakalamak istedi ama rüzgar yaprakları hep götürdü.»
   - Açıklama: Rüzgarın yaprakları götürmesi istemdeki önemsiz yaprak olayı örneğine çok yakın, çocuğun önemseyeceği gerçek bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0104` birebir aynı, `@degisim: ferah -> geniş` (tutuyorsan), ardından `@onarim: 6bdbb7e9872dbe25c8f83e831b3bb7141717d759`, sonra gövde.

### Hikâye 9: tohum sakir-0108 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0108
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'erik', fiil 'kabarmak', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: dalga eriği kumla örttü ve erik görünmedi | şapkasıyla kabarık kumu itip eriği buldu
@tohum: sakir-0108
Şakir kumsalda oturuyordu ve elinde son bir erik vardı. Ama erik elinden kaydı ve suyun kenarına yuvarlandı. Küçük bir dalga geldi ve eriği kumla örttü. Dalga geri çekildi ama erik görünmüyordu. Şakir hemen oraya yürüdü. Kumun bir yeri küçük bir tepe gibi kabarmıştı. Şakir düşünceli düşünceli kabarık yere baktı. Erik bu kumun altında olabilirdi. Şakir şapkasını çıkardı ve onu küçük bir kürek gibi tuttu. Şapkayla kumu yavaş yavaş kenara itti. Kumun altından mor erik çıktı. Şakir onun üstündeki kumu sildi. Sonra şapkasını yeniden taktı ve eriği mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Şakir hemen oraya yürüdü"
   - Cümle 5: «Şakir hemen oraya yürüdü.»
   - Açıklama: Yalnız başına kumsaldaki Şakir dalganın geldiği su kenarına gidiyor; güvenli kullanım satırındaki tek başına uzağa gitmez kuralına ve su güvenliğine aykırı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0108` birebir aynı, ardından `@onarim: 5e3ab3330b79e77b286624b72a1fd428db877ea3`, sonra gövde.

### Hikâye 10: tohum sakir-0109 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | park | -
@tohum: sakir-0109
- yer: park (Şehirdeki park.)
- tema: kaybolan eşya
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'karpuz', fiil 'büyütmek', sıfat 'zarif'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | park | -
@plan: top bankın altına yuvarlandı ve çok uzaktaydı | şapkasını bankın altına uzatıp topu kendine çekti
@tohum: sakir-0109
@degisim: büyütmek -> çekmek
Parkta güneşli bir gündü. Şakir karpuz desenli küçük topuyla oynuyordu. Top bir taşa çarptı ve bankın altına yuvarlandı. Şakir eğilip baktı ve topu bankın altında gördü. Kolunu uzattı ama top çok uzaktaydı. Sonra başındaki zarif, beyaz şapkayı çıkardı. Şapkayı bankın altına uzattı. Şapkanın kenarı topun arkasına yetişti. Şakir şapkayı yavaşça kendine doğru çekti. Top şapkanın önünde dışarı yuvarlandı. Şakir topu iki eliyle sıkıca tuttu. Şapkanın tozunu silkeledi ve onu yeniden taktı. Sonra Şakir topuyla mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "başındaki zarif, beyaz şapkayı"
   - Cümle 6: «Sonra başındaki zarif, beyaz şapkayı çıkardı.»
   - Açıklama: 'Zarif' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
   - Açıklama: 'Zarif' kelimesi 3 yaşındaki bir çocuğun bildiği bir kelime değil.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şapkanın kenarı topun arkasına yetişti"
   - Cümle 8: «Şapkanın kenarı topun arkasına yetişti.»
   - Açıklama: 'Yetişti' burada yanlış anlamda; 'uzandı' ya da 'ulaştı' olmalı.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Top şapkanın önünde dışarı"
   - Cümle 10: «Top şapkanın önünde dışarı yuvarlandı.»
   - Açıklama: Hareket fiiliyle çıkma eki gerekir; 'şapkanın önünden' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0109` birebir aynı, `@degisim: büyütmek -> çekmek` (tutuyorsan), ardından `@onarim: 76d41d84a44c766af3cc48ff8aab94015b1f12fb`, sonra gövde.

### Hikâye 11: tohum sakir-0117 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Canan
@tohum: sakir-0117
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Canan
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'yumurta', fiil 'koklamak', sıfat 'gri'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | Canan
@plan: güneş kitabın sayfalarına vurdu ve kardeşi okuyamadı | şapkasını kardeşinin başına takıp gölge yaptı
@tohum: sakir-0117
Bir sabah Şakir ile Canan kumsalda oturuyordu. Canan gri kapaklı kitabını açtı ve yeni sayfalarını kokladı. Ama güneş sayfalara çok parlak vuruyordu ve Canan okuyamıyordu. Şakir kardeşine yardım etmek istedi. Şapkasını çıkarıp Canan'ın başına taktı. Şapkanın geniş kenarı sayfalara gölge yaptı. Canan artık sayfaları rahatça gördü. Kitaptaki yumurta masalını Şakir'e sesli okudu. Masal çok güzeldi. Şakir kardeşinin yanına oturdu ve masalı dinledi. Sonra Canan kardeşine sarıldı. Şakir çok sevindi, çünkü kardeşi gölgede kitabını okuyabiliyordu.
```

**Hakem bulguları (1):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Şakir kardeşinin yanına oturdu"
   - Cümle 10: «Şakir kardeşinin yanına oturdu ve masalı dinledi.»
   - Açıklama: İkisi baştan beri kumsalda birlikte oturuyorken Şakir yeniden kardeşinin yanına oturuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0117` birebir aynı, ardından `@onarim: 960fde9580547fc340a8cc1c84a81e5f12a63acb`, sonra gövde.

### Hikâye 12: tohum sakir-0123 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | ev | Kadriye
@tohum: sakir-0123
- yer: ev (Şakir'in ailesiyle yaşadığı apartman dairesi.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'gardırop', fiil 'gülüşmek', sıfat 'koyu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | ev | Kadriye
@plan: balon gardırobun üstünde kaldı ve oyun durdu | şapkasını balona atıp onu aşağı düşürdü
@tohum: sakir-0123
Dışarıda yağmur cama tık tık vuruyordu. Şakir ile annesi Kadriye evde balonu yere düşürmeden havaya atıyordu. Ama Kadriye balona çok güçlü vurdu ve balon gardırobun üstünde kaldı. Koyu kahverengi gardırop çok yüksekti. "Balonumuz orada kaldı, anneciğim!" dedi Şakir. Sonra şapkasını çıkardı ve balona doğru yavaşça attı. Şapka balona değdi ve balon aşağı süzüldü. Şapka da halının üstüne düştü. "Harika bir atış, Şakir!" dedi Kadriye. İkisi gülüştü. Şakir çok sevindi, çünkü balon oyunları yeniden başlayabilirdi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "balon oyunları yeniden başlayabilirdi"
   - Cümle 11: «Şakir çok sevindi, çünkü balon oyunları yeniden başlayabilirdi.»
   - Açıklama: Tek oyun için çoğul 'oyunları' uyumsuz; 'balon oyunu' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0123` birebir aynı, ardından `@onarim: 86b634510189d1970eb393c4d414d6f682dccfb9`, sonra gövde.
