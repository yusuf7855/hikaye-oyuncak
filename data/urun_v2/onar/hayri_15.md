# Editör görevi (onarım): Hayri, onarım partisi 15

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar15.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar15.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0009 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0009
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: paylaşmak
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tabure', fiil 'sallamak', sıfat 'hazır'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: arkadaşı top oynamaktan çok acıkmıştı | tabaktaki karpuzu arkadaşıyla paylaştı
@tohum: hayri-0009
Bir sabah Hayri evin önündeki tabureye bir tabak karpuz koydu. Çok acıkmıştı ve iki dilim karpuz yemeye hazırdı. O sırada top oynamaktan acıkan Akın sokaktan el salladı. Hayri tabağa baktı ve biraz düşündü. "Akın, gel, bir dilim senin!" dedi Hayri. Akın koşup geldi ve tabureye yakın oturdu. Hayri büyük dilimi Akın'a uzattı. İkisi yan yana oturup karpuz yedi. Sonra siyah çekirdekleri tabağa koyup gülen bir yüz yaptılar. "Teşekkürler, Hayri, birlikte yemek çok güzeldi!" dedi Akın.
```

**Hakem bulguları (1):**

1. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "top oynamaktan acıkan Akın sokaktan el salladı"
   - Cümle 3: «O sırada top oynamaktan acıkan Akın sokaktan el salladı.»
   - Açıklama: Sorun ilk cümlelerde açıkça bir sorun olarak söylenmiyor; Akın'ın acıkmış olması yalnız bir sıfatla geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0009` birebir aynı, ardından `@onarim: 45747e5b8377d11cf508d0baf42fe01b79f763a0`, sonra gövde.

### Hikâye 2: tohum hayri-0012 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0012
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çöp', fiil 'yaklaşmak', sıfat 'kilitli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: evin anahtarı düştü ve kayboldu | çöp kutusunun yanına eğilip anahtarı buldu
@tohum: hayri-0012
Evin bahçesinde Hayri, kapının önünde üzgün duran Kamil'e yaklaştı. Kapı kilitliydi ve Kamil anahtarı bulamıyordu. "Anahtar yoksa bahçede uyuyacaksın!" dedi Hayri abartarak. Kamil buna güldü ve sakin sakin düşündü. "Çöpü atarken anahtarı düşürdüm galiba," dedi Kamil. Sonra Hayri çöp kutusunun yanına gitti ve yere eğildi. Kutunun arkasında parlayan küçük bir anahtar vardı. Hayri anahtarı aldı ve Kamil'e uzattı. Kamil kapıyı hemen açtı. "Teşekkürler, Hayri, sen çok iyi bir arkadaşsın!" dedi Kamil.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 3: «"Anahtar yoksa bahçede uyuyacaksın!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Abartarak' soyut bir kelime; 3 yaşındaki çocuk bilmez.
2. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Çöpü atarken anahtarı düşürdüm galiba"
   - Cümle 5: «"Çöpü atarken anahtarı düşürdüm galiba," dedi Kamil.»
   - Açıklama: Anahtarın yerini bulan asıl akıl yürütme yan karakter Kamil'den geliyor, Hayri yalnız gidip alıyor.
   - Açıklama: Anahtarın yerini bulan asıl fikir yan karakter Kamil'den geliyor; Hayri yalnız gidip anahtarı alıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0012` birebir aynı, ardından `@onarim: 9b1e93c6a292c2a6a878719540f6bf8ef6c2f1e5`, sonra gövde.

### Hikâye 3: tohum hayri-0015 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0015
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'turp', fiil 'eğilmek', sıfat 'güneşli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: yuvarlak turp yarışta hep yere düşüyordu | turpu düz yanından kaşığa koyup yavaş yürüdü
@tohum: hayri-0015
Ormanda, kamp yerinde hava çok güneşliydi. Hayri ile Mert kaşıkla turp taşıyarak büyük ağaca kadar yarışıyordu. Ama Hayri'nin turpu çok yuvarlaktı ve hep yere düşüyordu. "Mert, turp yine düştü!" dedi Hayri ve güldü. Hayri eğildi ve turpu yerden aldı. Hayri çok acıkmıştı, yarış bitince yemek yiyeceklerdi. Bu kez turpu düşürmemek için ona dikkatle baktı. Turpun bir yanı biraz düzdü. Hayri turpu kaşığa düz yanından koydu. Sonra yavaş yavaş yürüdü ve bu kez hiç düşürmedi. "Bak, Mert, artık düşmüyor!" dedi Hayri. İkisi büyük ağaca vardı ve sonra birlikte mutlu mutlu yemek yedi. Hayri bundan sonra yuvarlak şeyleri kaşığa düz yanından koydu.
```

**Hakem bulguları (4):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri çok acıkmıştı, yarış bitince"
   - Cümle 6: «Hayri çok acıkmıştı, yarış bitince yemek yiyeceklerdi.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
2. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri çok acıkmıştı"
   - Cümle 6: «Hayri çok acıkmıştı, yarış bitince yemek yiyeceklerdi.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız anılıyor, sorunun çözümünde işe yaramıyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri çok acıkmıştı, yarış bitince yemek yiyeceklerdi"
   - Cümle 6: «Hayri çok acıkmıştı, yarış bitince yemek yiyeceklerdi.»
   - Açıklama: Açlık ayrıntısı sorunun ortasına sebepsiz giriyor ve turp sorunuyla hiçbir ilgisi yok.
   - Açıklama: Açlık ayrıntısı turp sorununun ortasına sebepsizce giriyor ve sorunla ilgisi yok.
4. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "bu kez hiç düşürmedi"
   - Cümle 10: «Sonra yavaş yavaş yürüdü ve bu kez hiç düşürmedi.»
   - Açıklama: 'Bu kez' 7. cümlede de geçtiği için gereksiz tekrar ediliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0015` birebir aynı, ardından `@onarim: 151c0bfa57ac8289a436beff9c409660afd13981`, sonra gövde.

### Hikâye 4: tohum hayri-0018 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Yumak
@tohum: hayri-0018
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çit', fiil 'bindirmek', sıfat 'çalışkan'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Yumak
@plan: bahçede çamurlu izler vardı ve kimin olduğu belli değildi | deliğe gidip çitin arasından baktı
@tohum: hayri-0018
@degisim: bindirmek -> eşelemek
Hayri evin bahçesinde yürürken yerde çamurlu izler gördü. İzler çitin altındaki bir deliğe kadar gidiyordu. Hayri bu izleri çok merak etti. Sonra izlerin peşinden deliğe kadar yürüdü. Çitin arasından öbür bahçeye dikkatle baktı. Çalışkan köpek Yumak orada ıslak toprağı eşeledi. Yumak'ın dört ayağı da çamurluydu. "Yumak, bahçeye bir kamyon dolusu çamur getirdin!" dedi Hayri abartarak. Yumak kuyruğunu salladı ve Hayri'ye bir kez havladı. Hayri çok sevindi, çünkü izleri kimin yaptığını sonunda bulmuştu.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "orada ıslak toprağı eşeledi"
   - Cümle 6: «Çalışkan köpek Yumak orada ıslak toprağı eşeledi.»
   - Açıklama: Hayri'nin baktığı anda süren eylem 'eşeliyordu' olmalı; görünüş uyumu bozuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kamyon dolusu çamur getirdin"
   - Cümle 8: «"Yumak, bahçeye bir kamyon dolusu çamur getirdin!" dedi Hayri abartarak.»
   - Açıklama: Abartılı mecaz ve 'abartarak' kelimesi 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0018` birebir aynı, `@degisim: bindirmek -> eşelemek` (tutuyorsan), ardından `@onarim: 50ace5c567beaf7fefe4c04872ddec36c1934d76`, sonra gövde.

### Hikâye 5: tohum hayri-0019 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0019
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çeşme', fiil 'kırpmak', sıfat 'kocaman'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: musluğu çok açtı ve su arkadaşını ıslattı | özür dileyip ona kocaman bir havlu getirdi
@tohum: hayri-0019
Bir sabah Hayri ile Akın kamp yerinde çeşmede ellerini yıkıyordu. Hayri musluğu birden çok fazla açtı ve su her yana fışkırdı. Hayri musluğu hemen kapattı ama Akın'ın yüzü sırılsıklam olmuştu. Akın gözlerini hızlı hızlı kırptı ve yüzünü buruşturdu. "Özür dilerim, Akın, seni ıslatmak istemedim," dedi Hayri. Sonra çadıra koştu ve kocaman bir havlu getirdi. Akın havluyla yüzünü ve saçlarını kuruladı. "Akın, üstüne bütün çeşmenin suyu geldi!" dedi Hayri. Hayri yine abartıyordu ve Akın buna güldü. "Sorun değil, Hayri, havlu için teşekkürler!" dedi Akın.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "musluğu birden çok fazla açtı"
   - Cümle 2: «Hayri musluğu birden çok fazla açtı ve su her yana fışkırdı.»
   - Açıklama: 'Birden çok' ifadesi 'birden fazla' diye de okunabildiği için anlam belirsiz.
   - Açıklama: 'birden çok' dizisi 'birden fazla' anlamına da okunuyor; anlam belirsiz ve söyleyiş bozuk.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri yine abartıyordu"
   - Cümle 9: «Hayri yine abartıyordu ve Akın buna güldü.»
   - Açıklama: 'Abartmak' 3 yaşındaki bir çocuğun bilmeyeceği soyut bir kavram.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri yine abartıyordu ve"
   - Cümle 9: «Hayri yine abartıyordu ve Akın buna güldü.»
   - Açıklama: Abartma özelliği sorun çözüldükten sonra süs olarak geçiyor, işe yarar biçimde kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0019` birebir aynı, ardından `@onarim: 62105693cfc055e1e92fe6747e447768300a28e8`, sonra gövde.

### Hikâye 6: tohum hayri-0020 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0020
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: bir şey yapmak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamera', fiil 'açmak', sıfat 'sakin'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: kum kuru olduğu için kale hep yıkılıyordu | kovayla ıslak kum getirip kaleyi yeniden yaptı
@tohum: hayri-0020
@degisim: kamera -> kova
Bir sabah deniz çok sakindi. Hayri kıyıda Basri Amca'yla kumdan bir kale yapıyordu. Ama kale hep yıkılıyordu, çünkü kum çok kuruydu. "Of, yine olmadı, bırakalım!" dedi Basri Amca. "Bırakmayalım, bu kale saray kadar büyük olacak!" dedi Hayri abartarak. Basri Amca buna güldü ve yeniden denemek istedi. Hayri suyun kenarında küçük bir çukur açtı, oradaki kum ıslaktı. Hayri kovasını bu kumla doldurdu ve geri getirdi. İkisi ıslak kumu sıkıca bastırdı ve kaleyi yeniden kurdu. Bu kez kale hiç yıkılmadı. Hayri çok sevindi, çünkü birlikte güzel bir kale yapmışlardı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dedi Hayri abartarak"
   - Cümle 5: «"Bırakmayalım, bu kale saray kadar büyük olacak!" dedi Hayri abartarak.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0020` birebir aynı, `@degisim: kamera -> kova` (tutuyorsan), ardından `@onarim: ecc099be83f78de05ec61e352cec7f377826f9bc`, sonra gövde.

### Hikâye 7: tohum hayri-0021 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0021
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tarak', fiil 'seslenmek', sıfat 'büyük'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpeğin tüyleri dikenli bir çalıya takıldı | ekmeğini paylaştı ve tüyleri tarakla ayırdı
@tohum: hayri-0021
Ormanda, kamp yerinde Hayri büyük tarağıyla saçını tarıyordu. Hayri, Yumak'ı da yanında kampa getirmişti. Birden Yumak uzakta havladı ve Hayri sese doğru yürüdü. Yumak'ın uzun tüyleri dikenli bir çalıya takılmıştı. "Gel, Yumak!" diye seslendi Hayri. Ama Yumak kıpırdadı ve tüyler çalıya daha çok takıldı. Hayri çok acıkmıştı ve çantasında bir ekmek vardı. Yine de ekmeğin yarısını Yumak'a verdi. Yumak durdu ve ekmeği sakince yedi. Bu sırada Hayri elindeki tarakla tüyleri çalıdan yavaş yavaş ayırdı. Yumak zıpladı ve kuyruğunu salladı. "Oh, Yumak, sonunda kurtuldun!" dedi Hayri sevinçle.
```

**Hakem bulguları (4):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Hayri, Yumak'ı da yanında kampa getirmişti"
   - Cümle 2: «Hayri, Yumak'ı da yanında kampa getirmişti.»
   - Açıklama: Kartta Yumak Basri Amca'nın köpeğidir; Hayri onu sahibi yokken kendi köpeği gibi kampa getiriyor.
   - Açıklama: Yanlar alanına göre Yumak Basri Amca'nın köpeğidir; Hayri onu kendi köpeği gibi kampa getiriyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri sese doğru yürüdü"
   - Cümle 3: «Birden Yumak uzakta havladı ve Hayri sese doğru yürüdü.»
   - Açıklama: Çocuk ormanda tek başına uzaktaki bir sese doğru gidiyor; taklit edilince tehlikeli.
3. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: yok (eksiklik bulgusu)
   - Cümle 3: «Birden Yumak uzakta havladı ve Hayri sese doğru yürüdü.»
   - Açıklama: Tüylerin çalıya takıldığı ilk 3 cümlede değil ancak 4. cümlede söyleniyor.
4. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Yumak'ın uzun tüyleri dikenli bir çalıya takılmıştı"
   - Cümle 4: «Yumak'ın uzun tüyleri dikenli bir çalıya takılmıştı.»
   - Açıklama: Sorun ilk üç cümlede değil ancak dördüncü cümlede söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0021` birebir aynı, ardından `@onarim: d1acd469171e73b5498019fb045462b38019f667`, sonra gövde.

### Hikâye 8: tohum hayri-0022 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0022
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'pastel', fiil 'getirmek', sıfat 'ucuz'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: yeşil pastel kırıldı ve arkadaşı resmini bitiremedi | çadırdan kendi pastel kutusunu getirdi
@tohum: hayri-0022
@degisim: ucuz -> rengarenk
Hayri kamp yerinde Kamil'in ağaç resmini izliyordu. Birden Kamil'in yeşil pasteli yere düştü ve kırıldı. Küçük parçalar toprağa karıştı ve Kamil resmini bitiremedi. Kamil çok üzüldü. Hayri abartarak çadırda yüz tane pasteli olduğunu söyledi. Kamil buna güldü. Hayri hemen çadıra koştu ve kendi pastel kutusunu getirdi. Kutuda yüz tane yoktu ama rengarenk boyalar vardı. Kamil yeşil bir pastel aldı ve ağaçları boyadı. Sonra Hayri ile Kamil birlikte mutlu mutlu yeni bir resim yaptı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak çadırda"
   - Cümle 5: «Hayri abartarak çadırda yüz tane pasteli olduğunu söyledi.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0022` birebir aynı, `@degisim: ucuz -> rengarenk` (tutuyorsan), ardından `@onarim: eff90d656ef026a3d73bee0da6e67e60b3fe7a56`, sonra gövde.

### Hikâye 9: tohum hayri-0023 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0023
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'piyano', fiil 'eklemek', sıfat 'sabırlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: oyuncak piyano parkta kayboldu | sesin peşinden gitti ve piyanoyu buldu
@tohum: hayri-0023
@degisim: sabırlı -> sarı
Parkta ince bir müzik sesi geliyordu. Hayri salıncaktan indi ve Basri Amca'yı üzgün gördü. Basri Amca, Hayri için aldığı oyuncak piyanoyu yürürken düşürmüştü. Hayri piyanoyu bulmak istedi ve sesi dikkatle dinledi. Ses büyük ağacın arkasından geliyordu. Hayri oraya koştu ve çimenlerin arasında sarı bir piyano buldu. Piyanonun şarkı düğmesi açık kalmıştı. Hayri piyanoyu Basri Amca'ya götürdü. Hayri abartarak piyanonun sesini bütün mahallenin duyduğunu söyledi. Basri Amca buna güldü ve artık üzgün değildi. Sonra Hayri piyanoyu çaldı ve şarkıya kendi sesini ekledi. Hayri çok sevindi, çünkü piyanoyu sesinden bulmuştu.
```

**Hakem bulguları (4):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Parkta ince bir müzik sesi geliyordu"
   - Cümle 1: «Parkta ince bir müzik sesi geliyordu.»
   - Açıklama: Piyano bütün parkta duyulan bir ses çıkarırken Basri Amca'nın onu bulamayıp üzülmesi çelişkili.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak piyanonun sesini bütün mahallenin duyduğunu söyledi"
   - Cümle 9: «Hayri abartarak piyanonun sesini bütün mahallenin duyduğunu söyledi.»
   - Açıklama: 'Abartmak' soyut bir kavram ve dolaylı anlatım küçük çocuk için zor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak piyanonun sesini"
   - Cümle 9: «Hayri abartarak piyanonun sesini bütün mahallenin duyduğunu söyledi.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "şarkıya kendi sesini ekledi"
   - Cümle 11: «Sonra Hayri piyanoyu çaldı ve şarkıya kendi sesini ekledi.»
   - Açıklama: 'Şarkıya sesini eklemek' mecazlı bir anlatım; 'şarkı söyledi' somut olurdu.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0023` birebir aynı, `@degisim: sabırlı -> sarı` (tutuyorsan), ardından `@onarim: 6e3b1d098040cb32441b66d5a68d8b0f0297c8bf`, sonra gövde.

### Hikâye 10: tohum hayri-0028 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | -
@tohum: hayri-0028
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kova', fiil 'koklamak', sıfat 'yeni'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | -
@plan: yağmur yağıyordu ve tatlıların üstü kapalı değildi | kovasını boşaltıp tabağın üstüne ters kapattı
@tohum: hayri-0028
Yağmur damlaları bahçede tıp tıp ses çıkarıyordu. Hayri yeni kovasıyla yağmur suyu topluyordu. Ama masadaki tabakta tatlılar vardı ve üstleri kapalı değildi. Hayri baklava dükkanında tatlıların üstünü hep kapatırdı. Hemen kovadaki suyu çimene döktü. Kovayı ters çevirdi ve tabağın üstüne kapattı. Biraz sonra yağmur dindi. Hayri kovayı kaldırdı ve tatlıları kokladı. Tatlılar kuru kalmıştı ve çok güzel kokuyordu. Hayri bir dilim aldı ve afiyetle yedi. Sonra yeni kovasıyla bahçede mutlu mutlu oynadı.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "masadaki tabakta tatlılar vardı"
   - Cümle 3: «Ama masadaki tabakta tatlılar vardı ve üstleri kapalı değildi.»
   - Açıklama: Tatlıların neden yağmurun altında, dışarıdaki bir masada olduğu söylenmiyor; sorunun sebebi belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0028` birebir aynı, ardından `@onarim: 16903583143662bd3aa14e15c3eed677a9dabb4f`, sonra gövde.

### Hikâye 11: tohum hayri-0029 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0029
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fener', fiil 'gezinmek', sıfat 'garip'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: fener yumuşak yastığa battı ve ışık tavana vurdu | feneri çantanın sert üstüne koydu
@tohum: hayri-0029
Bir sabah erkenden ormandaki kamp yeri karanlıktı. Hayri çadırında fenerini açtı ve gölge oyunu oynamak istedi. Ama fener yumuşak yastığa battı ve ucu yukarı döndü. Işık yalnız tavana vurdu ve duvar karanlık kaldı. Hayri baklava dükkanında tepsileri hep düz ve sert yere koyardı. Bu yüzden feneri çantasının sert üstüne koydu. Işık bu kez duvara düştü. Hayri ellerini ışığın önünde tuttu ve garip şekiller yaptı. Gölgeler duvarda bir o yana bir bu yana gezindi. Hayri çok sevindi, çünkü gölge oyununu sonunda oynamıştı.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "feneri çantanın sert üstüne koydu"
   - Cümle 6: «Bu yüzden feneri çantasının sert üstüne koydu.»
   - Açıklama: 'Sert' sıfatı 'üst' kelimesine uymuyor; 'çantanın sert yüzeyine' ya da 'sert çantanın üstüne' olmalı.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "feneri çantanın sert üstüne koydu"
   - Cümle 6: «Bu yüzden feneri çantasının sert üstüne koydu.»
   - Açıklama: Gövdede çanta ve feneri çantanın üstüne koyma hiç geçmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0029` birebir aynı, ardından `@onarim: 2042ce88686340fe546565adeb8875bb701f7012`, sonra gövde.

### Hikâye 12: tohum hayri-0031 (deneme 2 -> 3)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0031
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'ayakkabı', fiil 'temizlenmek', sıfat 'puantiyeli'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: ıslak ayakkabı bağı kaydı ve çözüldü | yardım istedi ve arkadaşı bağı bağladı
@tohum: hayri-0031
@degisim: puantiyeli -> ıslak
Bahçede sıcak bir güneş parlıyordu. Hayri, Akın'a baklava dükkanından bir tepsi tatlı getiriyordu. Ama ayakkabısı yeni temizlenmişti, ıslak bağı kaydı ve çözüldü. Hayri'nin iki eli de tepsiyle doluydu ve bağı bağlayamadı. Tam o sırada Akın bahçe kapısından çıktı. "Akın, bu bağı bağlar mısın?" diye sordu Hayri. "Tabii, hemen," dedi Akın. Akın eğildi ve bağı sıkıca bağladı. Hayri artık rahatça yürüyebildi. Teşekkür etti ve tepsiyi Akın'a uzattı. Sonra ikisi bahçede oturdu ve tatlıları mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Bahçede sıcak bir güneş parlıyordu"
   - Cümle 1: «Bahçede sıcak bir güneş parlıyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede geçiyor ve Akın bahçe kapısından çıkınca sahnenin neresi olduğu belirsizleşiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0031` birebir aynı, `@degisim: puantiyeli -> ıslak` (tutuyorsan), ardından `@onarim: a04204000449682882f54e71d7b0067e074463f7`, sonra gövde.
