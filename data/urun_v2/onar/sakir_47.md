# Editör görevi (onarım): Şakir, onarım partisi 47

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/sakir_onar47.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/sakir_onar47.txt --ad urun_v2`
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

### Hikâye 1: tohum sakir-0090 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0090
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'minder', fiil 'aramak', sıfat 'küçük'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: kozalaklar yüksek dallarda duruyordu ve eli uzanamadı | fil arkadaşından yardım istedi ve kozalakları şapkasıyla tuttu
@tohum: sakir-0090
@degisim: minder -> kozalak
Bir sabah Şakir ile Necati ormandaki kamp yerindeydi. Şakir çadırın önünü süslemek için küçük kozalaklar arıyordu. Ama yerde hiç kozalak yoktu, hepsi yüksek dallarda duruyordu. Şakir'in eli dallara uzanamadı. "Necati, bana yardım eder misin?" diye sordu Şakir. "Tabii, Şakir," dedi Necati. Şakir şapkasını çıkardı ve ters çevirip ağacın altında tuttu. Necati hortumuyla dalları yavaşça salladı. Kozalaklar tek tek şapkanın içine düştü. Az sonra şapka kozalaklarla doldu. Şakir kozalakları çadırın önüne sıra sıra dizdi. "Teşekkürler, Necati, çadırın önü artık çok güzel oldu!" dedi Şakir.
```

**Hakem bulguları (1):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Şakir'in eli dallara uzanamadı"
   - Cümle 4: «Şakir'in eli dallara uzanamadı.»
   - Açıklama: 'Eli uzanamadı' yanlış kullanım; 'eli dallara yetişmedi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0090` birebir aynı, `@degisim: minder -> kozalak` (tutuyorsan), ardından `@onarim: 7100eb716e623ed0692c8f0efb116f93b5539d76`, sonra gövde.

### Hikâye 2: tohum sakir-0155 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Necati
@tohum: sakir-0155
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kemer', fiil 'almak', sıfat 'ekşi'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | deniz | Necati
@plan: sürprizi hazırlarken fil erken geri geliyordu | şapkasıyla erikleri örttü ve sonra açtı
@tohum: sakir-0155
@degisim: kemer -> erik
Şakir, Fil Necati için kumsalda bir sürpriz hazırlıyordu. Çantasından Necati'nin en sevdiği ekşi erikleri aldı ve havluya dizdi. Ama Necati su kenarından erken geri geliyordu. Şakir erikleri saklamak istedi. Şakir geniş şapkasını hemen çıkardı. Şapkayla erikleri örttü. Necati geldi ve yerdeki şapkaya baktı. "Şakir, şapkan neden yerde?" diye sordu Necati. "Çünkü altında sana bir sürpriz var," dedi Şakir. Şakir şapkayı yavaşça kaldırdı. "Erikler mi, onları çok severim!" dedi Necati sevinçle. İkisi erikleri paylaştı ve mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sürprizi hazırlarken fil erken"
   - Cümle 0 (plan satırı): «sürprizi hazırlarken fil erken geri geliyordu | şapkasıyla erikleri örttü ve sonra açtı»
   - Açıklama: '-ken' yan cümlesinin öznesi ana cümleninkiyle aynı sayılır; sürprizi fil hazırlıyormuş gibi okunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0155` birebir aynı, `@degisim: kemer -> erik` (tutuyorsan), ardından `@onarim: ef1e20a84a3fc1c1118c95aa8db8e396386501c4`, sonra gövde.

### Hikâye 3: tohum sakir-0156 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | Kadriye
@tohum: sakir-0156
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Kadriye
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kızartma', fiil 'ödemek', sıfat 'umutlu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Şakir | deniz | Kadriye
@plan: kabuklar küçük elinden hep düşüyordu | kabukları şapkasına doldurup taşıdı
@tohum: sakir-0156
@degisim: ödemek -> taşımak
Kumsalda Şakir annesi için kabuklardan bir kalp yapmak istedi. Annesi Kadriye yakında örtüye patates kızartması koyuyordu. Ama kabuklar çoktu ve Şakir'in küçük elinden hep düşüyordu. Şakir şapkasını çıkardı. Kabukları tek tek şapkanın içine koydu. Şapka doldu ve hiçbir kabuk düşmedi. Şakir şapkayı örtünün yanına taşıdı. Kabuklarla kumun üstüne büyük bir kalp yaptı. "Anne, sana bir sürprizim var!" dedi Şakir umutlu bir sesle. Kadriye döndü ve kumdaki kalbi görünce gülümsedi. "Teşekkürler, Şakir, gel şimdi birlikte kızartma yiyelim!" dedi Kadriye.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Annesi Kadriye yakında örtüye"
   - Cümle 2: «Annesi Kadriye yakında örtüye patates kızartması koyuyordu.»
   - Açıklama: 'Yakında' daha çok 'birazdan' anlamında kullanılır; burada yer anlamı belirsiz.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Şakir umutlu bir"
   - Cümle 9: «"Anne, sana bir sürprizim var!" dedi Şakir umutlu bir sesle.»
   - Açıklama: 'Umutlu' soyut bir kelime ve 3 yaşındaki çocuğun bileceği bir kelime değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Şakir umutlu bir sesle"
   - Cümle 9: «"Anne, sana bir sürprizim var!" dedi Şakir umutlu bir sesle.»
   - Açıklama: 'Umutlu' soyut bir kavram; 3 yaşındaki çocuk bu kelimeyi bilmeyebilir.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0156` birebir aynı, `@degisim: ödemek -> taşımak` (tutuyorsan), ardından `@onarim: 24ab2dcd361238a57f1e6b192c99a8909cd1aa2a`, sonra gövde.

### Hikâye 4: tohum sakir-0173 (deneme 3 -> 4)

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
Şakir kumsalda kumdan bir kale yapıyordu. Birden havada küçük baloncuklar uçuştu. Şakir baloncukların nereden geldiğini merak etti. Ama güneş çok parlaktı ve hiçbir şey göremedi. Sonra şapkasını gözlerinin üstüne biraz çekti. Şimdi her şeyi daha iyi görüyordu. Bir kayanın arkasında Canan'ın beyaz kuyruğu görünüyordu. Şakir kayaya doğru koştu. Canan orada oturmuş, elindeki şişeyle baloncuk üflüyordu. "Canan, baloncuklar senden mi geliyor?" diye sordu Şakir. "Evet, sen de dener misin?" dedi Canan. Şakir üfledi ve kocaman bir baloncuk yaptı. "Bu oyun çok güzel, Canan!" dedi Şakir.
```

**Hakem bulguları (2):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama güneş çok parlaktı"
   - Cümle 4: «Ama güneş çok parlaktı ve hiçbir şey göremedi.»
   - Açıklama: Plandaki sorun (güneşin görmeyi engellemesi) ilk üç cümlede değil dördüncü cümlede söyleniyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "güneş çok parlaktı ve hiçbir şey göremedi"
   - Cümle 4: «Ama güneş çok parlaktı ve hiçbir şey göremedi.»
   - Açıklama: Şakir baloncukları görmüşken hiçbir şey göremediği söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0173` birebir aynı, `@degisim: özlemek -> üflemek` (tutuyorsan), ardından `@onarim: 37b9e19fb9b15a4213f3902e9771f3746659e2b2`, sonra gövde.

### Hikâye 5: tohum sakir-0183 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

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
@plan: delik çantadan kitap ve çörek paketi yere düştü | yoldan geri yürüdü ve kitabı buldu
@tohum: sakir-0183
Bir sabah Şakir ile Canan aileleriyle kumsala geldi. Canan çok heyecanlıydı, çünkü kitabını denizin yanında okuyacaktı. Ama Canan'ın çantası delikti ve yolda boşalmıştı. Kitap da çörek paketi de kaybolmuştu. "Kitabım nerede, Şakir?" diye sordu Canan. "Yoldan geri yürüyelim, Canan," dedi Şakir. Geri yürürken Şakir kumda çörek paketini buldu. Çanta delik olduğu için paketi şapkasının içine koydu. Biraz ileride kitap kumun üstündeydi. Şakir kitabı da şapkaya koydu ve Canan'a getirdi. "Teşekkürler, Şakir, kitabım burada!" dedi Canan. Sonra ikisi kuma oturdu ve çörek yedi. Canan kitabını Şakir'e mutlu mutlu okudu.
```

**Hakem bulguları (2):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Şakir ile Canan aileleriyle kumsala"
   - Cümle 1: «Bir sabah Şakir ile Canan aileleriyle kumsala geldi.»
   - Açıklama: Yanlar alanına göre Canan Şakir'in kız kardeşidir; 'aileleriyle' ikisini ayrı ailelerden gösteriyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Yoldan geri yürüyelim, Canan"
   - Cümle 6: «"Yoldan geri yürüyelim, Canan," dedi Şakir.»
   - Açıklama: Güvenli kullanım satırına göre Şakir tek başına uzağa gitmez; iki çocuk aileden ayrılıp yoldan geri yürüyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0183` birebir aynı, ardından `@onarim: 97e9c0a3c7c09d3b03b147782a2248f14ca100bb`, sonra gövde.

### Hikâye 6: tohum sakir-0184 (deneme 3 -> 4)

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
@plan: küçük bir kedi kaygan çamurdan çıkamıyordu | şapkasını çamura uzatıp kediyi dışarı aldı
@tohum: sakir-0184
Şakir kamp yerinde annesi Kadriye ile top oynuyordu. Top çamurlu bir su birikintisinin yanına yuvarlandı. Orada küçük bir kedi kaygan çamurda kayıyordu ve dışarı çıkamıyordu. "Anne, kedi çamurdan çıkamıyor!" dedi Şakir. Kadriye çamura baktı. "Çamur çok kaygan, içine basma, Şakir," dedi Kadriye. Şakir şapkasını çıkardı ve çamurun kenarına koydu. Kedi şapkaya tutundu ve içine girdi. Şakir şapkayı kaldırdı ve kediyi kuru otların üstüne bıraktı. Kedi ağaçlara doğru koşup gitti. Sonra Şakir ve annesi top oyununu mutlu mutlu tamamladı.
```

**Hakem bulguları (3):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Orada küçük bir kedi kaygan"
   - Cümle 3: «Orada küçük bir kedi kaygan çamurda kayıyordu ve dışarı çıkamıyordu.»
   - Açıklama: Başlıktaki Yan alanında yalnız Kadriye var; kartta olmayan bir kedi olaya katılıyor.
2. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Orada küçük bir kedi kaygan çamurda kayıyordu"
   - Cümle 3: «Orada küçük bir kedi kaygan çamurda kayıyordu ve dışarı çıkamıyordu.»
   - Açıklama: Başlığın Yan alanında yalnız Kadriye var; olaya katılan isimsiz kedi başlıkta ve kartın yanlar bölümünde yok.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "top oyununu mutlu mutlu tamamladı"
   - Cümle 11: «Sonra Şakir ve annesi top oyununu mutlu mutlu tamamladı.»
   - Açıklama: 'Tamamlamak' 3 yaşındaki bir çocuğun bildiği bir kelime değil; 'bitirdi' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0184` birebir aynı, ardından `@onarim: 92388f0774a287ffe0422c3903f36a53cf74f9cf`, sonra gövde.

### Hikâye 7: tohum sakir-0187 (deneme 3 -> 4)

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
@plan: ikisi aynı anda konuşunca kimse kimseyi duymadı | sıra için şapkayı birbirine vermeyi önerdi
@tohum: sakir-0187
Rüzgar esiyordu ve havada kabarık bulutlar vardı. Şakir ile Fil Necati kamp yerinde komik bir oyun oynuyordu. Ama ikisi aynı anda konuştu ve kimse kimseyi duymadı. Şakir şapkasını çıkardı ve Necati'ye uzattı. "Şapka sende olunca sıra sende, Necati," dedi Şakir. Necati şapkayı kocaman başına koydu. Sonra komik olsun diye hortumuna bir papatya taktı. "Bak, Şakir, ben çiçekli bir filim!" dedi Necati. Şakir çok güldü. Sonra Necati şapkayı Şakir'e geri verdi. Şakir komik bir aslan sesi çıkardı ve Necati'yi güldürdü. Şakir çok sevindi, çünkü sırayla oynadıkları için ikisi de çok eğlenmişti.
```

**Hakem bulguları (3):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "sıra için şapkayı birbirine vermeyi önerdi"
   - Cümle 0 (plan satırı): «ikisi aynı anda konuşunca kimse kimseyi duymadı | sıra için şapkayı birbirine vermeyi önerdi»
   - Açıklama: Tekil özneyle 'birbirine vermeyi' ve 'sıra için' bozuk; 'sırayla şapkayı birbirlerine vermeyi' olmalı.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Sonra komik olsun diye"
   - Cümle 7: «Sonra komik olsun diye hortumuna bir papatya taktı.»
   - Açıklama: 'Komik' kelimesi kısa hikayede üç kez gereksizce tekrarlanıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Şakir komik bir aslan sesi"
   - Cümle 11: «Şakir komik bir aslan sesi çıkardı ve Necati'yi güldürdü.»
   - Açıklama: 'Komik' kelimesi 2., 7. ve 11. cümlelerde gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0187` birebir aynı, ardından `@onarim: 3f528e01ea522edfbc5c5fbadf82f7b722086c69`, sonra gövde.

### Hikâye 8: tohum sakir-0192 (deneme 3 -> 4)

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
@plan: güneş çok parlaktı ve hazinenin yanındaki dal görünmedi | şapkasını gözlerinin üstüne çekti ve dalı buldu
@tohum: sakir-0192
@degisim: faydalı -> parlak
Bir sabah Şakir kumsalda babası Remzi ile hazine oyunu oynuyordu. Remzi hazineyi kuma gömmüş ve yanına bir dal dikmişti. Ama güneş çok parlaktı ve Şakir dalı göremedi. "Hazineyi bul, Şakir!" dedi Remzi. Şakir şapkasını gözlerinin üstüne indirdi. Artık gözleri gölgede kaldı. Şakir her yere yavaş yavaş baktı. Sonunda kumsalın ucunda küçük dalı gördü. Hemen oraya koştu ve dalın dibindeki kumu parmaklarıyla taradı. Kumun altından bir kutu çıktı. Kutunun içinde iki sucuklu ekmek vardı. "Hazineyi buldum, baba!" dedi Şakir. İkisi kuma oturdu ve ekmekleri afiyetle yedi. Şakir bundan sonra güneşte uzağa bakarken gözlerini hep gölgede tuttu.
```

**Hakem bulguları (1):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Sonunda kumsalın ucunda küçük dalı gördü"
   - Cümle 8: «Sonunda kumsalın ucunda küçük dalı gördü.»
   - Açıklama: Güvenli özellik kullanımı satırı Şakir'in tek başına uzağa gitmediğini söylüyor, ama Şakir kumsalın ucuna tek başına koşuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0192` birebir aynı, `@degisim: faydalı -> parlak` (tutuyorsan), ardından `@onarim: 41cc9e6819bebd87f66167cef740f71327b692c7`, sonra gövde.

### Hikâye 9: tohum sakir-0193 (deneme 3 -> 4)

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
@plan: mavi bilye kutudan taştı ve uzun otların arasında kayboldu | şapkasıyla kuru yaprakları havaya uçurdu
@tohum: sakir-0193
@degisim: takvim -> bilye
Bir sabah Şakir kamp yerinde bilye oynuyordu. Küçük kutusu çok doluydu ve mavi bir bilye kutudan taştı. Bilye yere düştü ve uzun otların arasına yuvarlandı. Otların dibinde bir sürü kuru yaprak vardı ve Şakir bilyeyi göremedi. Şakir şapkasını yaprakların üstünde hızlı hızlı salladı. Yapraklar havaya uçtu ve bir yana gitti. Yaprakların altında mavi bir şey parladı. Bu kayıp bilyeydi! Şakir bilyeyi alıp cebine koydu. Şakir oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "mavi bilye kutudan taştı"
   - Cümle 0 (plan satırı): «mavi bilye kutudan taştı ve uzun otların arasında kayboldu | şapkasıyla kuru yaprakları havaya uçurdu»
   - Açıklama: Plan satırında da tek bilye için 'taşmak' fiili yanlış kullanılmış.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "mavi bir bilye kutudan taştı"
   - Cümle 2: «Küçük kutusu çok doluydu ve mavi bir bilye kutudan taştı.»
   - Açıklama: Tek bir bilye taşmaz; 'kutudan düştü' olmalı.
   - Açıklama: 'Taşmak' sıvılar için kullanılır, bilyeye uymaz; 'kutudan düştü' olmalı (plan satırında da aynı kusur var).

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0193` birebir aynı, `@degisim: takvim -> bilye` (tutuyorsan), ardından `@onarim: 6c86a8fb8a748e20c89a9d28cfe21096460cf79b`, sonra gövde.

### Hikâye 10: tohum sakir-0194 (deneme 3 -> 4)

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
Şakir sisli bir sabah Necati ile parktaydı. Necati bankta oturmuş, hortumuyla bir kitap tutuyordu. Birden Necati gerindi ve kitap yukarı gidip sisin içinde kayboldu. "Kitabım nereye gitti?" diye sordu Necati. Şakir etrafa dikkatle baktı. Yakındaki ağacın dalında beyaz bir şey gördü. Bu, Necati'nin kitabıydı. Dal çok yüksekti ve Necati bile ona yetişemedi. Şakir şapkasını kitaba doğru attı. Kitap ve şapka daldan kaydı ve aşağı düştü. Necati kitabı hortumuyla havada yakaladı. "Teşekkürler, Şakir, sen olmasan kitabı bulamazdım!" dedi Necati. Şakir ile Necati banka oturdu ve kitabı birlikte mutlu mutlu okudu.
```

**Hakem bulguları (2):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Birden Necati gerindi ve kitap yukarı gidip sisin içinde kayboldu"
   - Cümle 3: «Birden Necati gerindi ve kitap yukarı gidip sisin içinde kayboldu.»
   - Açıklama: Gerinmenin kitabı yüksek bir ağaç dalına fırlatması akla yatkın bir sebep değil.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Necati gerindi ve kitap yukarı gidip sisin içinde kayboldu"
   - Cümle 3: «Birden Necati gerindi ve kitap yukarı gidip sisin içinde kayboldu.»
   - Açıklama: Fil gerinince hortumundaki kitabın uçup yüksek bir ağaç dalına takılması akla yatkın bir sebep değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0194` birebir aynı, ardından `@onarim: ca79f2ea1632fe8157992d82be5a146871653403`, sonra gövde.

### Hikâye 11: tohum sakir-0207 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | orman | Necati
@tohum: sakir-0207
- yer: orman (Şehrin dışındaki dağda, ağaçlar arasında kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Necati
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'kova', fiil 'alışmak', sıfat 'karışık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Şakir | orman | Necati
@plan: aç sincaplar korkup fındık kovasına yaklaşamadı | şapkaya fındık döküp ağacın dibine bıraktı
@tohum: sakir-0207
Şakir, Necati ile ormandaki kamp yerinde oturuyordu. Necati'nin önünde karışık fındıklarla dolu bir kova vardı. Ağaçtan aç sincaplar indi, ama Necati'den korkup kovaya yaklaşamadılar. Sincaplar fındıklara uzaktan bakıyordu. "Onlara nasıl yardım ederiz?" diye sordu Necati. Şakir şapkasını çıkardı ve kovadan içine biraz fındık döktü. Şapkayı ağacın dibine bıraktı ve Necati ile biraz geri çekildi. Sincaplar önce durdu ve kulaklarını oynattı. Sonra yavaş yavaş Şakir ile Necati'ye alıştılar ve şapkaya geldiler. Fındıkları tek tek kemirdiler. "Bak, Necati, sincapların karnı doydu!" dedi Şakir. Şakir ile Necati de kalan fındıkları mutlu mutlu yedi.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "karışık fındıklarla dolu"
   - Cümle 2: «Necati'nin önünde karışık fındıklarla dolu bir kova vardı.»
   - Açıklama: Yalnız fındık olan kova için 'karışık' kelimesi anlamca uymuyor.
2. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "Ağaçtan aç sincaplar indi"
   - Cümle 3: «Ağaçtan aç sincaplar indi, ama Necati'den korkup kovaya yaklaşamadılar.»
   - Açıklama: Çoğul canlı sincaplar arka planda kalmıyor, olayın merkezine katılıyor.
   - Açıklama: Çoğul canlı sincaplar arka planda kalmıyor, sorunun ve çözümün merkezinde olaya katılıyor.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "kovadan içine biraz fındık"
   - Cümle 6: «Şakir şapkasını çıkardı ve kovadan içine biraz fındık döktü.»
   - Açıklama: 'İçine' zamirinin şapkayı mı kovayı mı gösterdiği belirsiz; 'şapkanın içine' olmalı.
   - Açıklama: 'İçine' zamirinin şapkayı mı kovayı mı gösterdiği belli değil.
4. **K4** (K merceği) — En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
   - Alıntı: "yavaş yavaş Şakir ile Necati'ye alıştılar ve şapkaya geldiler"
   - Cümle 9: «Sonra yavaş yavaş Şakir ile Necati'ye alıştılar ve şapkaya geldiler.»
   - Açıklama: Sincaplar şapkaya gelip fındık yiyerek olaya katılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0207` birebir aynı, ardından `@onarim: 438a9fa393a938ab467cd82684ff8db13c99e2d4`, sonra gövde.

### Hikâye 12: tohum sakir-0209 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Şakir | deniz | -
@tohum: sakir-0209
- yer: deniz (Deniz kıyısı ve kumsal.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: şapka (Hep şapka takar; şapkası yerden yere değişir.)
- kelimeler: isim 'ayakkabı', fiil 'uçuşmak', sıfat 'narin'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Şakir | deniz | -
@plan: baloncuklar rüzgarda hemen patladı | şapkasını rüzgara karşı tuttu ve yavaşça üfledi
@tohum: sakir-0209
@degisim: narin -> büyük
Rüzgar esiyordu. Şakir kumsalda, şemsiyelerinin yanındaydı. İlk kez sabunlu su ve çubukla baloncuk yapmayı denedi. Ama baloncuklar rüzgarda hemen patladı. Şakir tekrar üfledi ama yine büyük bir baloncuk olmadı. Sonra biraz düşündü. Şakir şapkasını çıkardı ve rüzgarın geldiği yöne doğru tuttu. Şapkanın arkasında hava sakindi. Şakir çubuğa yavaşça üfledi. Büyük ve parlak bir baloncuk oldu. Arkasından küçük baloncuklar da havada uçuştu. Parlak baloncuk yavaşça Şakir'in ayakkabısına kondu ve patlamadı. Şakir çok sevindi, çünkü büyük bir baloncuk yapmayı sonunda başarmıştı.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kumsalda, şemsiyelerinin yanındaydı"
   - Cümle 2: «Şakir kumsalda, şemsiyelerinin yanındaydı.»
   - Açıklama: Çoğul iyelik eki yanlış; tek kişi için 'şemsiyesinin' olmalı.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Ama baloncuklar rüzgarda hemen patladı"
   - Cümle 4: «Ama baloncuklar rüzgarda hemen patladı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: sakir-0209` birebir aynı, `@degisim: narin -> büyük` (tutuyorsan), ardından `@onarim: 0f81109093347e0f941cd979a51e996b94948744`, sonra gövde.
