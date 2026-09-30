# Editör görevi (onarım): Hayri, onarım partisi 57

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar57.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar57.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0217 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0217
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'mama', fiil 'denemek', sıfat 'şık'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek topun arkasından koşup kayboldu | mama kabıyla zıplayıp köpeği çağırdı
@tohum: hayri-0217
Ormanda rüzgar hafifçe esiyordu. Hayri, Yumak'ın mama kabını doldurdu ama Yumak orada yoktu. Yumak topun arkasından koşmuş ve ağaçların arasında kaybolmuştu. Hayri önce yavaşça çağırmayı denedi. "Yumak, gel buraya!" dedi Hayri. Ama Yumak gelmedi. Sonra Hayri işi abarttı. Mama kabını havaya kaldırdı ve zıpladı. "Yumak, dünyanın en güzel maması burada!" diye bağırdı Hayri. Çalıların arasında Yumak'ın şık kırmızı tasması göründü. Yumak koşarak geldi ve kuyruğunu salladı. Hayri güldü ve Yumak mamasını mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **K3** (K merceği) — Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
   - Alıntı: "Hayri, Yumak'ın mama kabını doldurdu"
   - Cümle 2: «Hayri, Yumak'ın mama kabını doldurdu ama Yumak orada yoktu.»
   - Açıklama: Kartın yanlar ilişkisine göre Yumak Basri Amca'nın köpeğidir, ama Hayri onu kendi köpeği gibi besleyip ormanda tek başına yanında tutuyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri önce yavaşça çağırmayı denedi"
   - Cümle 4: «Hayri önce yavaşça çağırmayı denedi.»
   - Açıklama: 'Yavaşça' hız bildirir; çağırmaya uygun kelime 'sessizce' ya da 'alçak sesle' olurdu.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra Hayri işi abarttı."
   - Cümle 7: «Sonra Hayri işi abarttı.»
   - Açıklama: 'İşi abartmak' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0217` birebir aynı, ardından `@onarim: cd066f9f0acc7e523014ea744547eb4236cc77e0`, sonra gövde.

### Hikâye 2: tohum hayri-0218 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Mert
@tohum: hayri-0218
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'gazete', fiil 'anlaşmak', sıfat 'devasa'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Mert
@plan: kum kalesi için kürek kayboldu | acıkınca çantaya gitti ve küreği gazetenin altında buldu
@tohum: hayri-0218
Deniz kıyısında Hayri ile Mert devasa bir kum kalesi yapıyordu. Mert küreğini bir yere koymuştu ama şimdi bulamıyordu. Kürek olmadan kaleye kule yapamazlardı. İkisi anlaştı: Mert su kenarına, Hayri kalenin çevresine bakacaktı. Hayri kalenin her yanına baktı ama kürek yoktu. O sırada Hayri çok acıktı. Çantanın üstünde kumdan korumak için bir gazete vardı. Hayri gazeteyi kaldırdı ve kürek oradaydı! "Mert, kürek burada!" diye seslendi Hayri. "Aferin, Hayri, sonunda bulduk!" dedi Mert. İkisi önce sandviçlerini yedi, sonra kuleyi bitirdi. Hayri ile Mert bundan sonra küreği hep kalenin yanına koydular.
```

**Hakem bulguları (5):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "devasa bir kum kalesi"
   - Cümle 1: «Deniz kıyısında Hayri ile Mert devasa bir kum kalesi yapıyordu.»
   - Açıklama: 'Devasa' kelimesini 3 yaşındaki çocuk bilmez.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Mert devasa bir kum kalesi"
   - Cümle 1: «Deniz kıyısında Hayri ile Mert devasa bir kum kalesi yapıyordu.»
   - Açıklama: 'Devasa' 3 yaşındaki bir çocuğun bilmediği bir kelime; 'kocaman' olmalı.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "O sırada Hayri çok acıktı"
   - Cümle 6: «O sırada Hayri çok acıktı.»
   - Açıklama: Tohumdaki acıkma özelliği küreğin bulunmasına açıkça yol açmıyor; çantaya neden gidildiği gövdede kurulmamış.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "O sırada Hayri çok acıktı"
   - Cümle 6: «O sırada Hayri çok acıktı.»
   - Açıklama: Kürek aramayla değil, acıkınca tesadüfen bulunuyor; çözüm sebebe yönelmiyor.
   - Açıklama: Kürek arama sonucunda değil, acıkma tesadüfüyle bulunuyor; çözüm sebebe yönelmiyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çantanın üstünde kumdan korumak için bir gazete vardı"
   - Cümle 7: «Çantanın üstünde kumdan korumak için bir gazete vardı.»
   - Açıklama: Çözümü getiren gazete ve açlık sebepsizce beliriyor.
   - Açıklama: Gazete ve açlık çözümü sebepsizce getiriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0218` birebir aynı, ardından `@onarim: 0f5cd9045b1344a30658965ee53ebe04295de78a`, sonra gövde.

### Hikâye 3: tohum hayri-0219 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0219
- yer: park (Mahallenin çocuk parkı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'bavul', fiil 'kilitlemek', sıfat 'eksik'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: ikisi de bavulu kilitlemek istedi | dükkandaki gibi sıra yapıp önce arkadaşına verdi
@tohum: hayri-0219
@degisim: eksik -> küçük
Hayri parkta Akın ile yolculuk oyunu oynuyordu. Akın'ın küçük bir oyuncak bavulu ve bavulun anahtarı vardı. İkisi de bavulu kilitlemek istedi ve anahtarı aynı anda tuttu. "Ben kilitleyeceğim!" dedi Akın. "Hayır, ben!" dedi Hayri. Sonra Hayri durdu ve baklava dükkanını düşündü. Dükkanda herkes sıraya girerdi ve Hayri baklavaları sırayla verirdi. "Dükkandaki gibi sıra yapalım, Akın, önce sen," dedi Hayri. Akın anahtarı çevirdi ve bavulu kilitledi. Sonra anahtarı Hayri'ye uzattı. Hayri de bavulu açtı ve sonra o da kilitledi. "Sırayla oynamak çok güzel, Hayri!" dedi Akın.
```

**Hakem bulguları (2):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Dükkandaki gibi sıra yapalım"
   - Cümle 8: «"Dükkandaki gibi sıra yapalım, Akın, önce sen," dedi Hayri.»
   - Açıklama: 'Sıra yapmak' yerine doğru kullanım 'sıraya girmek' ya da 'sıra olmak'tır.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "bavulu açtı ve sonra o da kilitledi"
   - Cümle 11: «Hayri de bavulu açtı ve sonra o da kilitledi.»
   - Açıklama: Bir önceki cümledeki 'Sonra' ve aynı cümledeki 'de' ile 'o da' gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0219` birebir aynı, `@degisim: eksik -> küçük` (tutuyorsan), ardından `@onarim: 90fa8f56bbc1f8efc4c54eaa812922232f460319`, sonra gövde.

### Hikâye 4: tohum hayri-0220 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0220
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kolye', fiil 'boşalmak', sıfat 'yalnız'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: arkadaşı şemsiyenin altında uyudu ve kolyeyi göremedi | acıktı, simit çıkardı ve koku arkadaşını uyandırdı
@tohum: hayri-0220
Bir sabah Hayri ile Kamil deniz kıyısına geldi. Hayri, Kamil için deniz kabuklarıyla bir kolye yapmıştı. Ama Kamil çok yorgundu ve şemsiyenin altında hemen uyudu. Hayri kolyeyi elinde tuttu ve sessizce bekledi. Kumsal yavaş yavaş boşaldı ve Hayri kendini yalnız hissetti. Bir süre sonra Hayri çok acıktı. Çantasından iki simit çıkardı. Güzel simit kokusu Kamil'in yanına kadar gitti. Kamil burnunu oynattı ve gözlerini açtı. "Bu koku nereden geliyor?" diye sordu Kamil. Hayri ona bir simit ve kolyeyi uzattı. Kamil kolyeyi hemen boynuna taktı. "Teşekkürler, Hayri, bu kolyeyi çok sevdim!" dedi Kamil.
```

**Hakem bulguları (6):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kumsal yavaş yavaş boşaldı"
   - Cümle 5: «Kumsal yavaş yavaş boşaldı ve Hayri kendini yalnız hissetti.»
   - Açıklama: Kumsalın boşalması ve yalnızlık hissi olaya hiçbir katkı yapmayan işlevsiz bir ayrıntı.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Kumsal yavaş yavaş boşaldı"
   - Cümle 5: «Kumsal yavaş yavaş boşaldı ve Hayri kendini yalnız hissetti.»
   - Açıklama: Kumsalın boşalması hikayede uzun bir zaman atlaması olduğunu gösteriyor.
3. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Bir süre sonra Hayri çok acıktı"
   - Cümle 6: «Bir süre sonra Hayri çok acıktı.»
   - Açıklama: Kamil'i uyandıran Hayri'nin bilinçli bir çözümü değil, tesadüfi bir acıkma.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Bir süre sonra Hayri çok acıktı"
   - Cümle 6: «Bir süre sonra Hayri çok acıktı.»
   - Açıklama: Çözüm soruna yönelmiyor; Hayri'nin acıkması sorunu rastlantıyla çözüyor.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Güzel simit kokusu Kamil'in yanına kadar gitti"
   - Cümle 8: «Güzel simit kokusu Kamil'in yanına kadar gitti.»
   - Açıklama: Kamil'i Hayri'nin bilinçli bir çözümü değil tesadüfen yayılan simit kokusu uyandırıyor.
6. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Güzel simit kokusu Kamil'in yanına kadar gitti"
   - Cümle 8: «Güzel simit kokusu Kamil'in yanına kadar gitti.»
   - Açıklama: Çözüm sebebe yönelmiyor; arkadaş tesadüfen simit kokusuyla uyanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0220` birebir aynı, ardından `@onarim: 995e31653229bafef4a1fe1510e3c20f3c15e8b8`, sonra gövde.

### Hikâye 5: tohum hayri-0221 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0221
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'çanta', fiil 'uzaklaşmak', sıfat 'paslı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: dalgalar büyüdü ve çantaya doğru geldi | çantayı hemen sudan çok uzağa taşıdı
@tohum: hayri-0221
Hayri deniz kıyısında renkli taşlar topluyordu. Taşları kumdaki çantasına koyuyordu. Birden rüzgar çıktı ve dalgalar büyüyüp çantaya doğru geldi. Hayri suyun içindeki paslı direğe baktı. Önce dalgalar direğin önünde kalıyordu. Şimdi ise direği geçip kuma kadar geliyordu. Hayri bunu hemen fark etti ve olayı çok abarttı. Denizin bütün kumsala geleceğini sandı. Hemen çantasını aldı ve sudan koşarak uzaklaştı. Çantayı kumsalın arkasındaki kuru kumun üstüne koydu. Biraz sonra büyük bir dalga geldi. Dalga, çantanın eski yerini baştan sona ıslattı. Ama çanta ve taşlar kuru kaldı. Hayri bundan sonra çantasını hep sudan uzak bir yere koydu.
```

**Hakem bulguları (4):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve olayı çok abarttı"
   - Cümle 7: «Hayri bunu hemen fark etti ve olayı çok abarttı.»
   - Açıklama: 'Olayı abartmak' soyut bir ifade ve 3 yaşındaki çocuğun bileceği bir kelime değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "olayı çok abarttı"
   - Cümle 7: «Hayri bunu hemen fark etti ve olayı çok abarttı.»
   - Açıklama: 'Abartmak' soyut bir kavram ve 3 yaşındaki çocuğun bilmeyeceği bir kelime.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri bunu hemen fark etti ve olayı çok abarttı"
   - Cümle 7: «Hayri bunu hemen fark etti ve olayı çok abarttı.»
   - Açıklama: Abartma ayrıntısı olayı değiştirmiyor, üstelik tehlike gerçek çıktığı için işlevsiz kalıyor.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri bunu hemen fark etti ve olayı çok abarttı"
   - Cümle 7: «Hayri bunu hemen fark etti ve olayı çok abarttı.»
   - Açıklama: Hayri'nin abarttığı söyleniyor ama büyük dalga gerçekten gelip çantanın yerini ıslatıyor, yani endişesi haklı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0221` birebir aynı, ardından `@onarim: 7adfd748d8fd50a7c0b43af71db52bfdf8d1a95c`, sonra gövde.

### Hikâye 6: tohum hayri-0222 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0222
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'değnek', fiil 'kurulanmak', sıfat 'plastik'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar kumu savurdu ve oyuncak araba kayboldu | kuma kareler çizdi ve her kareyi tek tek aradı
@tohum: hayri-0222
Kıyıda sert bir rüzgar esiyordu. Hayri su kenarından döndü ve havlusuyla kurulandı. Ama rüzgar kumu savurdu ve plastik arabası kumun altında kayboldu. Hayri her yere baktı ama arabayı göremedi. Sonra baklava dükkanını düşündü. Dükkanda baklavayı hep kare kare kesiyordu. Hayri kumu da öyle bölmek istedi. Yerdeki bir değnekle arabanın durduğu yere kareler çizdi. Sonra kareleri tek tek eliyle yavaşça karıştırdı. Birden parmakları sert bir şeye değdi. Kumun altından kırmızı arabası çıktı. Hayri arabayı silkeledi ve sıkıca tuttu. Hayri çok sevindi, çünkü en sevdiği arabasını bulmuştu.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Hayri su kenarından döndü ve havlusuyla kurulandı"
   - Cümle 2: «Hayri su kenarından döndü ve havlusuyla kurulandı.»
   - Açıklama: Çocuğun yetişkinsiz tek başına denize girdiği ima ediliyor ve bu taklit edilince tehlikeli.
   - Açıklama: Hayri'nin yalnız başına denize girip ıslandığı ima ediliyor; çocuk taklit edebilir.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Dükkanda baklavayı hep kare kare kesiyordu"
   - Cümle 6: «Dükkanda baklavayı hep kare kare kesiyordu.»
   - Açıklama: Baklavayı kimin kestiği belli değil; gizli özne Hayri'yi gösteriyor ama kıyıdaki çocuğun dükkanda baklava kestiği anlaşılmıyor.
   - Açıklama: Baklavayı kimin kestiği belli değil; özne Hayri gibi okunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0222` birebir aynı, ardından `@onarim: 0d0269ae16a696957ef30287cfbdb6a9306d2b59`, sonra gövde.

### Hikâye 7: tohum hayri-0223 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0223
- yer: park (Mahallenin çocuk parkı.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kabak', fiil 'düzenlemek', sıfat 'karmakarışık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: arkadaşı kapalı bir kutu getirdi ve açmadı | acıkıp kutuyu kokladı ve içindekini bildi
@tohum: hayri-0223
@degisim: karmakarışık -> tatlı
Hayri parkta bir bankta Mert'i bekliyordu. Mert elinde kapalı bir kutuyla geldi. Kutudan tatlı bir koku geliyordu ama Mert kutuyu açmadı. "Kutuda ne var, Mert?" diye sordu Hayri. "Önce tahmin et, sonra açarım," dedi Mert. Hayri çok acıkmıştı ve kutuyu yavaşça kokladı. Bu kokuyu hemen tanıdı. "Bu kabak tatlısı!" dedi Hayri. Mert güldü ve kutuyu açtı. İçinde gerçekten turuncu kabak dilimleri vardı. Mert dilimleri iki eşit sıraya düzenledi. İki arkadaş bankta oturup tatlıyı paylaştı. Hayri bundan sonra yiyeceğini hep arkadaşıyla eşit böldü.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Mert kutuyu açmadı"
   - Cümle 3: «Kutudan tatlı bir koku geliyordu ama Mert kutuyu açmadı.»
   - Açıklama: Arkadaşın kutuyu hemen açmaması bir tahmin oyunu, gerçek bir sorun değil.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "iki eşit sıraya düzenledi"
   - Cümle 11: «Mert dilimleri iki eşit sıraya düzenledi.»
   - Açıklama: 'Sıraya düzenledi' dilbilgisel değil; 'iki eşit sıra halinde dizdi' olmalı.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Mert dilimleri iki eşit sıraya düzenledi"
   - Cümle 11: «Mert dilimleri iki eşit sıraya düzenledi.»
   - Açıklama: 'Sıraya düzenlemek' yanlış bir kullanım; 'iki eşit sıraya dizdi' ya da 'ikiye ayırdı' olmalı.
4. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hayri bundan sonra yiyeceğini hep arkadaşıyla eşit böldü"
   - Cümle 13: «Hayri bundan sonra yiyeceğini hep arkadaşıyla eşit böldü.»
   - Açıklama: Tatlıyı eşit bölen Mert olduğu için bu ders Hayri'nin yaşadığı olaydan çıkmıyor.
   - Açıklama: Eşit bölme dersi olaydan çıkmıyor, çünkü hikayede tatlıyı Hayri değil Mert bölüyor ve sorun tahminle ilgili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0223` birebir aynı, `@degisim: karmakarışık -> tatlı` (tutuyorsan), ardından `@onarim: 55f4b08093b59f88a11f6bb063c457c9141bd577`, sonra gövde.

### Hikâye 8: tohum hayri-0224 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0224
- yer: park (Mahallenin çocuk parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'yonca', fiil 'keşfetmek', sıfat 'dürüst'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: baklava tepsisi çok ağırdı ve kolları titredi | tepsiyi birlikte tutmak için amcadan yardım istedi
@tohum: hayri-0224
@degisim: keşfetmek -> bulmak
Parktaki bankta Basri Amca oturuyordu. Hayri baklava dükkanından ona büyük bir tepsi getiriyordu. Ama tepsi çok ağırdı ve Hayri'nin kolları titremeye başladı. Dükkanda ağır tepsiyi hep birlikte taşıyorlardı. Bu yüzden Hayri durdu ve dürüst davrandı. "Basri Amca, tepsi çok ağır, bir ucunu tutar mısın?" diye sordu Hayri. Basri Amca hemen kalktı ve tepsiyi öbür ucundan tuttu. İkisi yoncalar arasından yavaş yavaş yürüdü. Bankın üstünde tepsiye güzel bir yer buldular. Basri Amca baklavalara bakıp gülümsedi. "Teşekkürler, Basri Amca, birlikte çok kolay oldu!" dedi Hayri.
```

**Hakem bulguları (5):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ağır tepsiyi hep birlikte taşıyorlardı"
   - Cümle 4: «Dükkanda ağır tepsiyi hep birlikte taşıyorlardı.»
   - Açıklama: 'Taşıyorlardı' öznesinin kimleri gösterdiği belli değil.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Dükkanda ağır tepsiyi hep birlikte taşıyorlardı"
   - Cümle 4: «Dükkanda ağır tepsiyi hep birlikte taşıyorlardı.»
   - Açıklama: '-lardı' ile kimlerin kastedildiği belli değil.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri durdu ve dürüst davrandı"
   - Cümle 5: «Bu yüzden Hayri durdu ve dürüst davrandı.»
   - Açıklama: Yardım istemek için 'dürüst davrandı' demek kelimeyi yerinde kullanmıyor.
   - Açıklama: Yardım istemek dürüstlük değildir; 'dürüst' kelimesi yanlış anlamda kullanılmış.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri durdu ve dürüst davrandı"
   - Cümle 5: «Bu yüzden Hayri durdu ve dürüst davrandı.»
   - Açıklama: Yardım istemek dürüstlükle ilgili değil; 'dürüst davrandı' olaydan çıkmıyor.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden Hayri durdu ve dürüst davrandı"
   - Cümle 5: «Bu yüzden Hayri durdu ve dürüst davrandı.»
   - Açıklama: Dükkandaki taşıma alışkanlığından dürüstlük çıkmıyor; olay bir öncekinden mantıkla doğmuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0224` birebir aynı, `@degisim: keşfetmek -> bulmak` (tutuyorsan), ardından `@onarim: 96b9a21b4b5613af56fc43c1b0e79149a796e455`, sonra gövde.

### Hikâye 9: tohum hayri-0225 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Akın
@tohum: hayri-0225
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'kağıt', fiil 'kurumak', sıfat 'huzurlu'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | Akın
@plan: acele edip suyu devirdi ve resim ıslandı | özür diledi ve kağıt kururken yiyeceğini paylaştı
@tohum: hayri-0225
Hayri bahçedeki masada Akın ile oturuyordu. Akın boya kalemleriyle kağıda kocaman bir ağaç çizmişti. Hayri acıkmıştı ve aceleyle sandviçine uzandı, ama koluyla su bardağını devirdi. Su Akın'ın kağıdına döküldü. Akın resmine baktı ve çok üzüldü. "Özür dilerim, Akın, çok acele ettim," dedi Hayri. Hayri kağıdı dikkatle güneşli bir yere koydu. Sonra sandviçini ikiye böldü ve büyük parçayı Akın'a verdi. İkisi yan yana oturup sandviçlerini yedi. Biraz sonra kağıt kurudu ve ağaç resmi eskisi gibi göründü. "Resmim kurtuldu!" dedi Akın. Bahçe yine huzurlu oldu. Hayri bundan sonra masada hiç acele etmedi.
```

**Hakem bulguları (3):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri bahçedeki masada Akın"
   - Cümle 1: «Hayri bahçedeki masada Akın ile oturuyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye bahçede başlıyor ve bahçede bitiyor.
2. **M1** (M merceği) — Sorun ilk 3 cümlede açıkça söyleniyor.
   - Alıntı: "Su Akın'ın kağıdına döküldü"
   - Cümle 4: «Su Akın'ın kağıdına döküldü.»
   - Açıklama: Resmin ıslanması sorunu ilk 3 cümlede değil 4. cümlede söyleniyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Bahçe yine huzurlu oldu"
   - Cümle 12: «Bahçe yine huzurlu oldu.»
   - Açıklama: 'Huzurlu' soyut bir kavram ve bahçeye yüklenmiş bir mecaz.
   - Açıklama: 'Huzurlu' soyut bir kavramdır ve bahçeye yüklenmesi mecazdır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0225` birebir aynı, ardından `@onarim: 750a429f092abd06456d4ec62fe8579722dbbe12`, sonra gövde.

### Hikâye 10: tohum hayri-0226 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0226
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: Basri Amca
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'bluz', fiil 'uçuşmak', sıfat 'kolay'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: kuru kum rüzgarda uçuştu ve kumdan pasta dağıldı | acıkınca simidini çıkarıp amcaya yemek olarak sundu
@tohum: hayri-0226
@degisim: bluz -> önlük
Rüzgar kıyıda hızlı hızlı esiyordu. Hayri önlüğünü takmış, Basri Amca'ya kumdan pasta yapıyordu. Ama kuru kum rüzgarda uçuştu ve pasta dağıldı. "Yemeğim nerede, Hayri?" diye sordu Basri Amca. O sırada Hayri acıktı ve çantasını hatırladı. Çantasında büyük bir simit vardı. Hayri simidi ikiye böldü ve havlunun üstüne koydu. "İşte size taze bir simit!" dedi Hayri. "Harika, en kolay ve en güzel yemek!" dedi Basri Amca ve güldü. Hayri ile Basri Amca kumda oturup simidi mutlu mutlu yedi.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri acıktı ve çantasını hatırladı"
   - Cümle 5: «O sırada Hayri acıktı ve çantasını hatırladı.»
   - Açıklama: Acıkma ve çantadaki simit sebepsizce beliriyor ve çözümü dışarıdan getiriyor.
   - Açıklama: Çözüm tesadüfi bir acıkma ve önceden kurulmamış bir simitle sebepsizce geliyor.
2. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri simidi ikiye böldü ve havlunun üstüne koydu"
   - Cümle 7: «Hayri simidi ikiye böldü ve havlunun üstüne koydu.»
   - Açıklama: Sorun kuru kumun uçuşup pastayı dağıtması ama çözüm bu sebebe hiç yönelmiyor, pasta yeniden yapılmıyor.
3. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri simidi ikiye böldü"
   - Cümle 7: «Hayri simidi ikiye böldü ve havlunun üstüne koydu.»
   - Açıklama: Çözüm kumun kuru olmasına ve pastanın dağılmasına yönelmiyor, sorunu bırakıp simit sunuyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0226` birebir aynı, `@degisim: bluz -> önlük` (tutuyorsan), ardından `@onarim: df9a775a2e35b87a1c8ee8783a2f02b013098c4c`, sonra gövde.

### Hikâye 11: tohum hayri-0228 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0228
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'bot', fiil 'hazırlamak', sıfat 'gürültülü'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: kuru yapraklar kırıldı ve baklava olmadı | dükkanı hatırladı ve yumuşak yeşil yapraklar topladı
@tohum: hayri-0228
Ormandaki kamp yerinde yerler kuru yapraklarla doluydu. Hayri botlarıyla yürürken yapraklar gürültülü bir ses çıkarıyordu. Hayri yapraklardan baklava hazırlamak istedi, ama kuru yapraklar hep kırıldı. Düz bir taş onun oyun tepsisi oldu. Sonra Hayri baklava dükkanını düşündü. Orada baklavanın hamuru hep ince ve yumuşaktı. Hayri ağaçların altından yeşil ve taze yapraklar topladı. Yaprakları taşın üstüne kat kat dizdi. Sonra küçük bir dalla üstlerine kareler çizdi. Yaprak baklava tıpkı dükkandaki gibi oldu. Hayri güldü ve baklava oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (1):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "kamp yerinde yerler kuru"
   - Cümle 1: «Ormandaki kamp yerinde yerler kuru yapraklarla doluydu.»
   - Açıklama: 'Yerinde yerler' aynı kelimeyi gereksiz tekrarlıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0228` birebir aynı, ardından `@onarim: ee236cd502a43fab9f58d7351398eb7f152e653b`, sonra gövde.

### Hikâye 12: tohum hayri-0229 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | Mert
@tohum: hayri-0229
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Mert
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'poşet', fiil 'köpürmek', sıfat 'sadık'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Mert
@plan: sürpriz için hazır bir içecek yoktu | yoğurdu suyla şişede salladı ve ayran yaptı
@tohum: hayri-0229
@degisim: sadık -> serin
Hayri kamp yerinde Mert'e bir sürpriz hazırlamak istedi. Mert o sırada ağaçların arasında çadırı kuruyordu. Ama Hayri'nin yanında hazır bir içecek yoktu. Hayri acıkmıştı ve yiyecek poşetini açtı. İçinde ekmek, yoğurt ve yarım şişe serin su vardı. Hayri yoğurdu şişenin içine döktü ve kapağı sıkıca kapattı. Sonra şişeyi hızlı hızlı salladı. Şişedeki ayran bembeyaz köpürdü. Mert çadırdan çıkınca Hayri ona ekmek ve şişeyi uzattı. "Sürpriz, Mert, çadırın bitti, işte ayran!" dedi Hayri. "Bu çok güzel olmuş!" dedi Mert. Hayri çok sevindi, çünkü sürprizi Mert'i mutlu etmişti.
```

**Hakem bulguları (4):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama Hayri'nin yanında hazır bir içecek yoktu"
   - Cümle 3: «Ama Hayri'nin yanında hazır bir içecek yoktu.»
   - Açıklama: İçecek olmamasının sebebi söylenmiyor ve sorun zayıf kuruluyor.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yanında hazır bir içecek yoktu"
   - Cümle 3: «Ama Hayri'nin yanında hazır bir içecek yoktu.»
   - Açıklama: Hazır içecek olmamasının sebebi söylenmiyor ve bu, çocuğun önemseyeceği gerçek bir sorun gibi kurulmuyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri acıkmıştı ve yiyecek poşetini açtı"
   - Cümle 4: «Hayri acıkmıştı ve yiyecek poşetini açtı.»
   - Açıklama: Hayri'nin acıkması hiçbir işe yaramayan, sonra unutulan işlevsiz bir ayrıntı.
   - Açıklama: Açlık hiç kullanılmıyor, yalnız çözümü getiren poşeti sebepsizce açtırmak için hikayeye giriyor.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Sürpriz, Mert, çadırın bitti"
   - Cümle 10: «"Sürpriz, Mert, çadırın bitti, işte ayran!" dedi Hayri.»
   - Açıklama: Çadır kurulur, 'bitmek' fiili burada yanlış anlamda kullanılmış ve anlam belirsiz.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0229` birebir aynı, `@degisim: sadık -> serin` (tutuyorsan), ardından `@onarim: f07b98d3b6650f8301bc949ef2fe8123cd651864`, sonra gövde.
