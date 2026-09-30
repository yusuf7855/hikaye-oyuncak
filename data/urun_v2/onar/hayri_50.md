# Editör görevi (onarım): Hayri, onarım partisi 50

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 5 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar50.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Hakem puanlarını, ret kayıtlarını, parti dosyalarını ve başka hikâyeleri açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her hikâye normal aday biçimindedir; tek fark `@onarim` satırıdır (hikâyeler arasında bir boş satır):

```
### Hayri | <yer> | <yan ya da ->
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar50.txt --ad urun_v2`
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

## Kart: Hayri (kaynaklı, kapalı dünya)

- Ad: Hayri (okunuş: hayri; kesme eki okunuşa uyar)
- Kimlik: Hayri, mahallede arkadaşlarıyla maceralar yaşayan, yemek yemeyi çok seven bir çocuktur.
- Tür: oğlan
- Güvenli özellik kullanımı: Hayri'nin yemek sevgisi paylaşmak, beklemek ya da yemek hazırlamak olarak gösterilir; çok yiyip midesi ağrımaz, kimse onun yemesiyle ya da kilosuyla alay etmez, tanımadığı birinden yiyecek almaz.
- Özellikler:
  - acık: Yemek yemeyi çok sever; sık sık acıkır. (örnek biçimler: acıktı, acıkmıştı)
  - baklava: Mahalledeki baklava dükkanında çalışır. (örnek biçimler: baklava, baklavayı)
  - abart: Olayları abartmayı sever. (örnek biçimler: abarttı, abartarak)
- Yerler:
  - deniz: Mahallenin yakınındaki deniz kıyısı.
  - orman: Şehrin dışında, ağaçların arasındaki kamp yeri.
  - park: Mahallenin çocuk parkı.
  - ev: Mahalledeki evler, sokak ve bahçeler.
    - yan Basri Amca ise: Basri Amca'nın bahçesi; izinsiz girilmez.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - Akın: Mert'in küçük kardeşi ve arkadaş grubunun en küçüğü; çok zekidir, hayvanları çok sever. Tür: oğlan; konuşur. Yüzey biçimleri: Akın
  - Mert: Akın'ın ağabeyi; sakin ve düzenlidir, tartışmaları o bitirir. Tür: oğlan; konuşur. Yüzey biçimleri: Mert
  - Kamil: Hayri'nin yakın arkadaşı; uyumayı ve kitap okumayı çok sever, mahalle bakkalına bakar. Sık sık tartışsalar da birbirlerini çok severler. Tür: oğlan; konuşur. Yüzey biçimleri: Kamil
  - Basri Amca: Mahallede yaşar; çabuk kızar ama iyi kalplidir. Bahçesine izin almadan kimsenin girmesini istemez. Tür: amca; konuşur. Yüzey biçimleri: Basri Amca, Basri, amca
  - Yumak: Basri Amca'nın köpeği; onu Akın bulmuş ve Basri Amca'ya vermiştir. Tür: köpek; KONUŞMAZ. Yüzey biçimleri: Yumak, köpek, köpeği
- Dünya kuralları:
  - Mert ile Akın kardeştir, ağabey Mert'tir; hiçbiri Hayri'nin kardeşi değildir.
  - Yumak Basri Amca'nın köpeğidir; Hayri'nin köpeği yoktur.
  - Yumak konuşmaz; havlar, koklar, kuyruğunu sallar.
- Yasak adlar: Hale, Sevim, Rüstem, Fatma Nine, Sadettin, Saadettin, Kuşçu Baba, Ozan, Nuri, Tamtam
- Yasak: Hayri'nin kız kardeşi kartta yoktur; ailesi hikayeye girmez.
- İzinli dünya kelimeleri: mahalle, baklava, bakkal, abart

## Onarılacak hikâyeler

### Hikâye 1: tohum hayri-0191 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | -
@tohum: hayri-0191
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'tutkal', fiil 'yüklemek', sıfat 'cömert'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | -
@plan: kamyonun kasası küçüktü ve bloklar düşüyordu | kamyona kocaman bir kutu yapıştırdı ve blokları yükledi
@tohum: hayri-0191
@degisim: cömert -> kocaman
Bahçede güneş parlıyordu. Hayri oyuncak kamyonuna tahta bloklar yüklüyordu. Ama kamyonun kasası küçüktü ve bloklar hep yere düşüyordu. Hayri işi abarttı ve evden en kocaman karton kutuyu getirdi. Kutuyu tutkalla kamyonun üstüne yapıştırdı. Biraz bekledi ve tutkal kurudu. Sonra bütün blokları yeni kasaya tek tek yükledi. Artık hiçbir blok yere düşmedi. Hayri kamyonun ipini tuttu ve onu bahçede yavaş yavaş çekti. Kamyon blokları rahatça taşıdı. Hayri çok sevindi, çünkü kocaman kasa bütün blokları tutmuştu.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede güneş parlıyordu"
   - Cümle 1: «Bahçede güneş parlıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor ve kutu evden getiriliyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri işi abarttı"
   - Cümle 4: «Hayri işi abarttı ve evden en kocaman karton kutuyu getirdi.»
   - Açıklama: 'İşi abartmak' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'İşi abartmak' deyim; küçük çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri işi abarttı ve evden"
   - Cümle 4: «Hayri işi abarttı ve evden en kocaman karton kutuyu getirdi.»
   - Açıklama: Kartın özellikler alanı olayları abartmayı anlatır; burada özellik en büyük kutuyu getirmek gibi fiziksel bir aşırılığa kaydırılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0191` birebir aynı, `@degisim: cömert -> kocaman` (tutuyorsan), ardından `@onarim: b8b8346ae31b814a00e1704d836d119befd7eaf1`, sonra gövde.

### Hikâye 2: tohum hayri-0192 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0192
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'fincan', fiil 'gülümsemek', sıfat 'ekşi'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: kamp yerinde nereden geldiği bilinmeyen garip bir ses vardı | sesin kendi karnından geldiğini buldu ve elmasını paylaştı
@tohum: hayri-0192
Ormandaki kamp yerinde her yer çok sessizdi. Birden Hayri ile Akın garip bir ses duydu. İkisi de sesin nereden geldiğini çok merak etti. Akın çadırın arkasına baktı ama hiçbir şey bulamadı. Hayri bir ağacın arkasına baktı, orası da boştu. Sonra ses yine geldi, bu kez çok yakından. Hayri elini karnına koydu ve güldü. Ses Hayri'nin karnından geliyordu, çünkü çok acıkmıştı. "Akın, sesi yapan benim karnım!" dedi Hayri. Akın gülümsedi ve iki fincana su koydu. Hayri de çantasından iki ekşi elma çıkardı ve Akın'a bir tane verdi. "Afiyet olsun, Akın, sesi birlikte bulduk!" dedi Hayri.
```

**Hakem bulguları (4):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Hayri ile Akın garip bir ses duydu"
   - Cümle 2: «Birden Hayri ile Akın garip bir ses duydu.»
   - Açıklama: Ormanda kaynağı bilinmeyen garip bir sesin aranması küçük çocuk için ürkütücü bir gerilim kuruyor.
2. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "Akın garip bir ses duydu"
   - Cümle 2: «Birden Hayri ile Akın garip bir ses duydu.»
   - Açıklama: Sessiz ormanda nereden geldiği bilinmeyen garip ses gerilim ve korku öğesi olarak kurulmuş.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ses Hayri'nin karnından geliyordu, çünkü çok acıkmıştı"
   - Cümle 8: «Ses Hayri'nin karnından geliyordu, çünkü çok acıkmıştı.»
   - Açıklama: Kişinin kendi karnının guruldamasını tanımayıp her yerde araması saçma bir sorun.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "iki fincana su koydu"
   - Cümle 10: «Akın gülümsedi ve iki fincana su koydu.»
   - Açıklama: Fincanlara konan su sebepsiz beliriyor ve olayda hiçbir işe yaramıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0192` birebir aynı, ardından `@onarim: 524879646188b9521fc50264f26eb2b750c51493`, sonra gövde.

### Hikâye 3: tohum hayri-0193 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0193
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: bir şey yapmak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'üniforma', fiil 'girmek', sıfat 'kırık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: bilye kutusunun altında delik vardı ve bilyeler düşüyordu | kartonu baklava kutusu gibi katlayıp yeni kutu yaptı
@tohum: hayri-0193
@degisim: üniforma -> karton
Hayri ile Mert bahçede bilye oynuyordu. Mert'in bilye kutusu kırıktı ve altında büyük bir delik vardı. Bilyeler bu delikten yere düşüp dağılıyordu. "Yeni bir kutu yapalım mı, Mert?" diye sordu Hayri. "Olur ama nasıl yapacağız?" dedi Mert. Hayri'nin çantasında dükkandan getirdiği düz bir karton vardı. Hayri kartonu, dükkandaki baklava kutuları gibi dört yerden katladı. Köşeleri birbirine geçirdi ve sağlam bir kutu yaptı. Mert yerdeki bilyeleri tek tek topladı. Bütün bilyeler yeni kutuya rahatça girdi. "Harika bir kutu olmuş, Hayri!" dedi Mert. Hayri bundan sonra kırık bir kutu görünce hemen yenisini yaptı.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri ile Mert bahçede bilye oynuyordu"
   - Cümle 1: «Hayri ile Mert bahçede bilye oynuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor.
   - Açıklama: Başlıktaki yer ev iken hikaye bahçede geçiyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri'nin çantasında dükkandan getirdiği düz bir karton vardı"
   - Cümle 6: «Hayri'nin çantasında dükkandan getirdiği düz bir karton vardı.»
   - Açıklama: Karton tam gerektiği anda önceden kurulmadan beliriyor ve çözümü sebepsizce getiriyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "kırık bir kutu görünce hemen yenisini yaptı"
   - Cümle 12: «Hayri bundan sonra kırık bir kutu görünce hemen yenisini yaptı.»
   - Açıklama: 'Bundan sonra' ile süregelen alışkanlık anlatılıyor; 'yapardı' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0193` birebir aynı, `@degisim: üniforma -> karton` (tutuyorsan), ardından `@onarim: a4f3d1b0a48aedd0bc82a10bc98d805a85024878`, sonra gövde.

### Hikâye 4: tohum hayri-0194 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0194
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'minibüs', fiil 'yaratmak', sıfat 'basit'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: yol suya yakındı ve dalga yolu bozdu | yolun önüne kocaman bir kum duvarı yaptı
@tohum: hayri-0194
@degisim: minibüs -> araba
Bir sabah Hayri kıyıda oyuncak arabasıyla oynuyordu. Kumda araba için basit bir yol yaratmıştı. Ama yol suya çok yakındı ve bir dalga gelip yolun yarısını bozdu. Araba ıslak kumun içinde kaldı. Hayri arabayı çıkardı ve yolu yeniden düzeltti. Sonra abartarak yolun önüne arabadan beş kat yüksek bir kum duvarı yaptı. Biraz sonra yeni bir dalga geldi. Dalga duvara çarptı ve geri döndü. Bu kez yol olduğu gibi kaldı. Hayri arabasıyla kumdaki yolda mutlu mutlu oynamaya devam etti.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "basit bir yol yaratmıştı"
   - Cümle 2: «Kumda araba için basit bir yol yaratmıştı.»
   - Açıklama: Kumda yol 'yaratılmaz', 'yapılır'; fiil nesnesine uymuyor.
   - Açıklama: Kumda yol 'yaratılmaz', 'yapılır'; fiil yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra abartarak yolun önüne"
   - Cümle 6: «Sonra abartarak yolun önüne arabadan beş kat yüksek bir kum duvarı yaptı.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "abartarak yolun önüne arabadan beş kat yüksek"
   - Cümle 6: «Sonra abartarak yolun önüne arabadan beş kat yüksek bir kum duvarı yaptı.»
   - Açıklama: Karttaki özellik olayları abartmaktır, hikayede büyük duvar yapmak olarak kullanılıyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra abartarak yolun önüne arabadan beş kat yüksek"
   - Cümle 6: «Sonra abartarak yolun önüne arabadan beş kat yüksek bir kum duvarı yaptı.»
   - Açıklama: Karttaki abartma özelliği olayları abartmaktır; burada kum duvarını büyük yapmak olarak farklı biçimde kullanılmış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0194` birebir aynı, `@degisim: minibüs -> araba` (tutuyorsan), ardından `@onarim: 9998d1503da298f32abe0eb333ea96eef374b242`, sonra gövde.

### Hikâye 5: tohum hayri-0195 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0195
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'lolipop', fiil 'saymak', sıfat 'düşünceli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: kamp yerinde nereden geldiği bilinmeyen bir ses vardı | ağacın altına bakıp düşen cevizleri buldu
@tohum: hayri-0195
@degisim: lolipop -> ceviz
Rüzgar ağaçların arasında hafifçe esiyordu. Hayri kamp yerinde tık tık diye bir ses duydu. Bu sesin nereden geldiğini çok merak etti. Hayri sesin peşinden büyük bir ağacın altına yürüdü. Yerde yeşil kabuklu, yuvarlak şeyler vardı. Hayri bunlardan bir tanesini eline aldı ve düşünceli bir yüzle baktı. Sonra onu hemen tanıdı, bu bir cevizdi. Dükkanda baklavanın içine hep bundan koyuyordu. O sırada rüzgar esti ve daldan bir ceviz daha düştü. Ceviz bir taşa çarptı ve tık diye ses çıkardı. Hayri yerdeki cevizleri tek tek saydı, tam on iki tane vardı. Sonra hepsini dükkandaki baklavalar için mutlu mutlu topladı.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri sesin peşinden büyük"
   - Cümle 4: «Hayri sesin peşinden büyük bir ağacın altına yürüdü.»
   - Açıklama: 'Sesin peşinden' mecazlı bir söyleyiş; 'sesin geldiği yere' daha somut olur.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri yerdeki cevizleri tek tek saydı"
   - Cümle 11: «Hayri yerdeki cevizleri tek tek saydı, tam on iki tane vardı.»
   - Açıklama: Cevizlerin sayılması sesin sebebini bulma olayına hizmet etmeyen işlevsiz bir ayrıntı.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "tam on iki tane vardı"
   - Cümle 11: «Hayri yerdeki cevizleri tek tek saydı, tam on iki tane vardı.»
   - Açıklama: Cevizlerin sayılması ve on iki tane olması olayda hiçbir işe yaramayan işlevsiz bir ayrıntı.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "hepsini dükkandaki baklavalar için"
   - Cümle 12: «Sonra hepsini dükkandaki baklavalar için mutlu mutlu topladı.»
   - Açıklama: Tohum özelliği baklava bir kez değil iki kez kullanılıyor.
5. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra hepsini dükkandaki baklavalar için"
   - Cümle 12: «Sonra hepsini dükkandaki baklavalar için mutlu mutlu topladı.»
   - Açıklama: Tohumdaki baklava özelliği 8. cümlede kullanıldıktan sonra sonda ikinci kez kullanılıyor; kartın özellik kullanımı bir kez olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0195` birebir aynı, `@degisim: lolipop -> ceviz` (tutuyorsan), ardından `@onarim: 1bcad0227a977382abd6aa0d0315eb248e4e9b3b`, sonra gövde.
