# Editör görevi (onarım): Hayri, onarım partisi 19

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar19.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar19.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0009 (deneme 4 -> 5)

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
@plan: arkadaşının karnı çok açtı | tabaktaki karpuzu arkadaşıyla paylaştı
@tohum: hayri-0009
Bir sabah Hayri evin önündeki tabureye bir tabak karpuz koydu. Çok acıkmıştı ve iki dilim karpuz yemeye hazırdı. O sırada Akın sokaktan el salladı ve "Karnım çok aç!" dedi. Hayri tabağa baktı ve biraz düşündü. "Akın, gel, bir dilim senin!" dedi Hayri. Akın koşup geldi ve tabureye yakın oturdu. Hayri büyük dilimi Akın'a uzattı. İkisi yan yana oturup karpuz yedi. Sonra siyah çekirdekleri tabağa koyup gülen bir yüz yaptılar. "Teşekkürler, Hayri, birlikte yemek çok güzeldi!" dedi Akın.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: ""Karnım çok aç!" dedi"
   - Cümle 3: «O sırada Akın sokaktan el salladı ve "Karnım çok aç!" dedi.»
   - Açıklama: Akın'ın neden aç olduğu söylenmiyor; sorunun sebebi verilmiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0009` birebir aynı, ardından `@onarim: 1b7c2f7204b1e4737382051742faf4c6fba580a7`, sonra gövde.

### Hikâye 2: tohum hayri-0021 (deneme 5 -> 6)

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
Ormanda, kamp yerinde Hayri büyük tarağıyla saçını tarıyordu. Yumak da yakındaki çalıların arasında oynuyordu. Birden Yumak'ın uzun tüyleri dikenli bir çalıya takıldı ve havladı. "Gel, Yumak!" diye seslendi Hayri. Ama Yumak kıpırdadı ve tüyler çalıya daha çok takıldı. Hayri çok acıkmıştı ve çantasında bir ekmek vardı. Yine de ekmeğin yarısını Yumak'a verdi. Yumak durdu ve ekmeği sakince yedi. Bu sırada Hayri elindeki tarakla tüyleri çalıdan yavaş yavaş ayırdı. Yumak zıpladı ve kuyruğunu salladı. "Oh, Yumak, sonunda kurtuldun!" dedi Hayri sevinçle.
```

**Hakem bulguları (4):**

1. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "Yumak'ın uzun tüyleri dikenli bir çalıya takıldı"
   - Cümle 3: «Birden Yumak'ın uzun tüyleri dikenli bir çalıya takıldı ve havladı.»
   - Açıklama: Köpeğin dikenli çalıya takılıp havlaması acı ya da yaralanma çağrıştırıyor.
2. **C2** (K merceği) — Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
   - Alıntı: "tüyleri dikenli bir çalıya takıldı ve havladı"
   - Cümle 3: «Birden Yumak'ın uzun tüyleri dikenli bir çalıya takıldı ve havladı.»
   - Açıklama: Köpeğin dikenli çalıya takılıp havlaması acı çekme izlenimi veriyor.
3. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "bir çalıya takıldı ve havladı"
   - Cümle 3: «Birden Yumak'ın uzun tüyleri dikenli bir çalıya takıldı ve havladı.»
   - Açıklama: Bağlı cümlede 'havladı' fiilinin öznesi dilbilgisel olarak 'tüyleri' oluyor; özne Yumak ayrıca belirtilmeli.
4. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "tüyleri dikenli bir çalıya takıldı ve havladı"
   - Cümle 3: «Birden Yumak'ın uzun tüyleri dikenli bir çalıya takıldı ve havladı.»
   - Açıklama: Bağlaçla birleşen cümlede özne tüyler kalıyor; tüyler havlamaz, özne Yumak olarak yeniden verilmeli.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0021` birebir aynı, ardından `@onarim: 11d6e139c1788dc302b8cfb74e65e039c7eee060`, sonra gövde.

### Hikâye 3: tohum hayri-0022 (deneme 5 -> 6)

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
Hayri kamp yerinde Kamil'in ağaç resmini izliyordu. Birden Kamil'in yeşil pasteli yere düştü ve kırıldı. Küçük parçalar toprağa karıştı ve Kamil resmini bitiremedi. Kamil çok üzüldü. Hayri abarttı ve çadırda yüz tane pasteli olduğunu söyledi. Kamil buna güldü. Hayri hemen çadıra koştu ve kendi pastel kutusunu getirdi. Kutuda yüz tane yoktu ama rengarenk boyalar vardı. Kamil yeşil bir pastel aldı ve ağaçları boyadı. Sonra Hayri ile Kamil birlikte mutlu mutlu yeni bir resim yaptı.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve çadırda"
   - Cümle 5: «Hayri abarttı ve çadırda yüz tane pasteli olduğunu söyledi.»
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0022` birebir aynı, `@degisim: ucuz -> rengarenk` (tutuyorsan), ardından `@onarim: f7e33e295c782a740182c8e320cfc3287fccdaf2`, sonra gövde.

### Hikâye 4: tohum hayri-0023 (deneme 5 -> 6)

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
Parkta çok hafif bir müzik sesi geliyordu. Hayri salıncaktan indi ve Basri Amca'yı üzgün gördü. Basri Amca, Hayri için aldığı oyuncak piyanoyu yürürken düşürmüştü. Hayri piyanoyu bulmak istedi ve sesi dikkatle dinledi. Ses büyük ağacın arkasından geliyordu. Hayri oraya koştu ve çimenlerin arasında sarı bir piyano buldu. Piyanonun şarkı düğmesi açık kalmıştı. Hayri piyanoyu Basri Amca'ya götürdü. Hayri abarttı ve piyanonun sesini bütün mahallenin duyduğunu söyledi. Basri Amca buna güldü ve artık üzgün değildi. Sonra Hayri piyanoyu çaldı ve şarkının sonuna bir alkış ekledi. Hayri çok sevindi, çünkü piyanoyu sesinden bulmuştu.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "oyuncak piyanoyu yürürken düşürmüştü"
   - Cümle 3: «Basri Amca, Hayri için aldığı oyuncak piyanoyu yürürken düşürmüştü.»
   - Açıklama: Müzik çalan bir piyanonun düştüğünü fark etmeden yürümek ve onu bulamamak akla yatkın değil.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abarttı ve piyanonun"
   - Cümle 9: «Hayri abarttı ve piyanonun sesini bütün mahallenin duyduğunu söyledi.»
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
3. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "şarkının sonuna bir alkış ekledi"
   - Cümle 11: «Sonra Hayri piyanoyu çaldı ve şarkının sonuna bir alkış ekledi.»
   - Açıklama: Şarkıya alkış eklemek anlamca uygun olmayan bir kullanım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0023` birebir aynı, `@degisim: sabırlı -> sarı` (tutuyorsan), ardından `@onarim: dd9160ef47800cbdde15abbe8386da8b0b8b27a8`, sonra gövde.

### Hikâye 5: tohum hayri-0028 (deneme 5 -> 6)

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
Yağmur damlaları bahçede tıp tıp ses çıkarıyordu. Hayri yeni kovasıyla yağmur suyu topluyordu. Ama yağmurdan önce masaya koyduğu tatlıların üstü açıktı. Hayri baklava dükkanında tatlıların üstünü hep kapatırdı. Hemen kovadaki suyu çimene döktü. Kovayı ters çevirdi ve tabağın üstüne kapattı. Biraz sonra yağmur dindi. Hayri kovayı kaldırdı ve tatlıları kokladı. Tatlılar kuru kalmıştı ve çok güzel kokuyordu. Hayri bir dilim aldı ve afiyetle yedi. Sonra yeni kovasıyla bahçede mutlu mutlu oynadı.
```

**Hakem bulguları (2):**

1. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Tatlılar kuru kalmıştı"
   - Cümle 9: «Tatlılar kuru kalmıştı ve çok güzel kokuyordu.»
   - Açıklama: Tatlılar yağmur başladığından beri açıktaydı, yine de kuru kaldıkları söyleniyor.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Tatlılar kuru kalmıştı ve"
   - Cümle 9: «Tatlılar kuru kalmıştı ve çok güzel kokuyordu.»
   - Açıklama: Tatlılar yağmurda bir süre açık kaldığı halde kuru kalmış olması çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0028` birebir aynı, ardından `@onarim: 7d48b417b0d9bfd989be98530de174354d02e78d`, sonra gövde.

### Hikâye 6: tohum hayri-0031 (deneme 3 -> 4)

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
Evin bahçesinde sıcak bir güneş parlıyordu. Hayri, Akın'a baklava dükkanından bir tepsi tatlı getiriyordu. Ama ayakkabısı yeni temizlenmişti, ıslak bağı kaydı ve çözüldü. Hayri'nin iki eli de tepsiyle doluydu ve bağı bağlayamadı. Tam o sırada Akın evinden bahçeye çıktı. "Akın, bu bağı bağlar mısın?" diye sordu Hayri. "Tabii, hemen," dedi Akın. Akın eğildi ve bağı sıkıca bağladı. Hayri artık rahatça yürüyebildi. Teşekkür etti ve tepsiyi Akın'a uzattı. Sonra ikisi bahçede oturdu ve tatlıları mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "ayakkabısı yeni temizlenmişti, ıslak bağı kaydı"
   - Cümle 3: «Ama ayakkabısı yeni temizlenmişti, ıslak bağı kaydı ve çözüldü.»
   - Açıklama: İki yan cümle bağlaçsız virgülle birleştirilmiş, neden-sonuç bağı dilbilgisel olarak kurulmamış.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yeni temizlenmişti, ıslak bağı kaydı ve çözüldü"
   - Cümle 3: «Ama ayakkabısı yeni temizlenmişti, ıslak bağı kaydı ve çözüldü.»
   - Açıklama: İki cümle virgülle yanlış birleştirilmiş ve 'ıslak bağı' belirtme eki gibi okunuyor; 'Ayakkabısının bağı ıslaktı, kaydı ve çözüldü' olmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0031` birebir aynı, `@degisim: puantiyeli -> ıslak` (tutuyorsan), ardından `@onarim: 343ca4b157f1c127fe7fcc277179c111a630a6de`, sonra gövde.

### Hikâye 7: tohum hayri-0032 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0032
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'etiket', fiil 'okşamak', sıfat 'yemyeşil'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: toprak yumuşaktı ve fidan yana yattı | toprak isteyip ekledi ve iki eliyle sıkıca bastırdı
@tohum: hayri-0032
@degisim: etiket -> kova
Bir sabah Hayri, Basri Amca'yla parkta ilk kez fidan dikmeyi denedi. Basri Amca ona küçük, yemyeşil bir fidan verdi. Ama çukurdaki toprak yumuşaktı ve fidan hemen yana yattı. "Bu fidan parkın en büyük ağacı olacak, çok toprak lazım!" dedi Hayri. "Yine abartıyorsun, Hayri," dedi Basri Amca ve ona bir kova toprak verdi. Hayri bu toprağı çukura ekledi. Sonra toprağı iki eliyle sıkıca bastırdı. Fidan bu kez dimdik durdu. Hayri fidanın yapraklarını okşadı. Hayri bundan sonra fidan dikerken toprağı hep sıkıca bastırdı.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Yine abartıyorsun, Hayri"
   - Cümle 5: «"Yine abartıyorsun, Hayri," dedi Basri Amca ve ona bir kova toprak verdi.»
   - Açıklama: 'Abartmak' soyut bir kelime; 3 yaşındaki çocuk bilmeyebilir.
   - Açıklama: 'abartmak' soyut bir kavram, 3 yaşındaki çocuk bilmez.
2. **M10** (M merceği) — Plan satırı hikayenin sorununu ve çözümünü doğru söylüyor.
   - Alıntı: "iki eliyle sıkıca bastırdı"
   - Cümle 7: «Sonra toprağı iki eliyle sıkıca bastırdı.»
   - Açıklama: Gövdede Hayri toprağı ne istiyor ne de bastırıyor; toprağı Basri Amca kendiliğinden veriyor.
3. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "toprağı hep sıkıca bastırdı"
   - Cümle 10: «Hayri bundan sonra fidan dikerken toprağı hep sıkıca bastırdı.»
   - Açıklama: Ders cümlesi hikayede hiç yaşanmamış bir bastırma eyleminden çıkıyor, olaya bağlı değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0032` birebir aynı, `@degisim: etiket -> kova` (tutuyorsan), ardından `@onarim: a26c56b02ba8dda730ca9ad2c70bcf655cc15783`, sonra gövde.

### Hikâye 8: tohum hayri-0033 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0033
- yer: park (Mahallenin çocuk parkı.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'şampuan', fiil 'indirmek', sıfat 'heyecanlı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: koşarken anahtar uzun çimenlere düştü | köpekten yardım istedi ve anahtarı buldu
@tohum: hayri-0033
@degisim: şampuan -> anahtar
Rüzgar hafif hafif esiyordu. Hayri parkta Yumak ile oynuyordu. Hayri koşarken baklava dükkanının anahtarı cebinden uzun çimenlere düştü. Hayri yere eğildi ama anahtarı göremedi. Hayri sabah dükkanda baklava taşımıştı, eli de anahtar da baklava kokuyordu. Hayri elini yavaşça Yumak'ın burnuna indirdi. "Yumak, anahtarımı bulur musun?" diye sordu Hayri. Yumak onun elini kokladı ve burnunu yere eğdi. Çimenlerin arasında biraz ilerledi, sonra durup havladı. Heyecanlı Hayri hemen oraya koştu. Anahtar çimenlerin arasında parlıyordu. "Aferin sana, Yumak!" dedi Hayri ve anahtarı aldı. Anahtarı bu kez ceketinin iç cebine koydu. Sonra ikisi oyunlarına mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri yere eğildi ama"
   - Cümle 4: «Hayri yere eğildi ama anahtarı göremedi.»
   - Açıklama: 'Hayri' art arda dört cümlenin başında gereksizce tekrar ediliyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri sabah dükkanda baklava"
   - Cümle 5: «Hayri sabah dükkanda baklava taşımıştı, eli de anahtar da baklava kokuyordu.»
   - Açıklama: Art arda beş cümle 'Hayri' ile başlıyor; gereksiz tekrar var.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0033` birebir aynı, `@degisim: şampuan -> anahtar` (tutuyorsan), ardından `@onarim: 0f745d9c3050e026c7ce046aec9740d6759c8253`, sonra gövde.

### Hikâye 9: tohum hayri-0035 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | -
@tohum: hayri-0035
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'çimen', fiil 'konuşmak', sıfat 'oynak'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | ev | -
@plan: top düz tahtadan zıplayıp yere düştü | kenarı yüksek boş bir tepsi kullandı
@tohum: hayri-0035
@degisim: konuşmak -> zıplamak
Evin bahçesinde Hayri yeni bir oyun buldu. Oynak topunu düz bir tahtayla çimenin öbür ucuna taşıyacaktı. Ama Hayri yürürken top tahtada zıpladı ve yere düştü. Hayri durdu ve düşündü. Hayri, çalıştığı baklava dükkanında hep kenarı yüksek tepsiler taşıyordu. Hayri hemen eve koştu ve boş bir tepsi getirdi. Topu tepsiye koydu. Tepsiyi iki eliyle tuttu ve yavaş yavaş yürüdü. Top kenara çarptı ama yere düşmedi. Sonunda Hayri çimenin öbür ucuna vardı. Hayri çok sevindi, çünkü topu düşürmeden bahçeyi geçmişti.
```

**Hakem bulguları (3):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Oynak topunu düz bir tahtayla"
   - Cümle 2: «Oynak topunu düz bir tahtayla çimenin öbür ucuna taşıyacaktı.»
   - Açıklama: 'Oynak' kelimesi topa uygun değil ve 3 yaşındaki çocuğun bileceği bir kelime değil.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri durdu ve düşündü."
   - Cümle 4: «Hayri durdu ve düşündü.»
   - Açıklama: Art arda üç cümle (4, 5, 6) 'Hayri' adıyla başlıyor; ad gereksiz tekrarlanıyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Hayri hemen eve koştu"
   - Cümle 6: «Hayri hemen eve koştu ve boş bir tepsi getirdi.»
   - Açıklama: Art arda cümlelerde özne 'Hayri' gereksiz yere tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0035` birebir aynı, `@degisim: konuşmak -> zıplamak` (tutuyorsan), ardından `@onarim: 15e14a87904875056679585fd5a9e52154c168c7`, sonra gövde.

### Hikâye 10: tohum hayri-0037 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0037
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'topaç', fiil 'tasarlamak', sıfat 'gururlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: yumuşak toprakta topaç hemen devrildi | düz ve sert bir taşın üstünde topacı çevirdi
@tohum: hayri-0037
@degisim: tasarlamak -> çevirmek
Ağaçların arasında kuşlar ötüyordu. Hayri kamp yerinde tahta topacını çevirdi. Ama toprak yumuşaktı ve topaç hemen devrildi. Hayri topacı iki kez daha çevirdi ama topaç yine toprağa battı. Biraz düşündü. Hayri baklava dükkanında tepsileri hep düz ve sert masaya koyardı. Etrafına baktı ve yerde büyük, düz bir taş gördü. Topacı taşın üstünde çevirdi. Topaç bu kez uzun uzun döndü. Hayri bir, iki, üç, dört, beş diye saydı. Hayri çok gururluydu, çünkü topacı bu kez hiç devrilmemişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri baklava dükkanında tepsileri hep düz ve sert masaya koyardı"
   - Cümle 6: «Hayri baklava dükkanında tepsileri hep düz ve sert masaya koyardı.»
   - Açıklama: Baklava dükkanı ayrıntısı topaç sorununa zorla bağlanmış, çözümü gerçekten getirmeyen işlevsiz bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0037` birebir aynı, `@degisim: tasarlamak -> çevirmek` (tutuyorsan), ardından `@onarim: 85118c5a53385c875ad34ec279f8342a818a28e6`, sonra gövde.

### Hikâye 11: tohum hayri-0038 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0038
- yer: park (Mahallenin çocuk parkı.)
- tema: sırayla oynamak
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kilit', fiil 'yalamak', sıfat 'elmalı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: tek salıncak vardı ve ikisi de önce binmek istedi | dükkandaki sırayı hatırladı ve sırayla binmeyi söyledi
@tohum: hayri-0038
@degisim: kilit -> salıncak
Parkta tek bir salıncak vardı. Hayri ile Mert aynı anda salıncağa koştu. İkisi de salıncağın zincirini tuttu ve önce binmek istedi. Hayri biraz düşündü. Hayri'nin çalıştığı baklava dükkanında müşteriler hep sırayla beklerdi. "Mert, gel, sırayla binelim," dedi Hayri. "Tamam, önce sen bin, ben de elmalı dondurmamı bitireyim," dedi Mert. Hayri salıncağa bindi ve on kez sallandı. Mert o sırada dondurmasını yaladı. Sonra Hayri indi ve Mert salıncağa bindi. Bu kez Hayri bekledi ve yüksek sesle saydı. Hayri ile Mert çok sevindi, çünkü sırayla ikisi de salıncağa binmişti.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "ben de elmalı dondurmamı bitireyim"
   - Cümle 7: «"Tamam, önce sen bin, ben de elmalı dondurmamı bitireyim," dedi Mert.»
   - Açıklama: Dondurma sebepsiz beliriyor ve Mert'in binme isteğinden birden vazgeçmesini açıklamak için getiriliyor.
   - Açıklama: Dondurma daha önce hiç anılmadan sebepsizce beliriyor ve beklemeyi kolaylaştırmak için getiriliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0038` birebir aynı, `@degisim: kilit -> salıncak` (tutuyorsan), ardından `@onarim: 52037ac33fdd1300d05c7311058c57dc6fa0fa43`, sonra gövde.

### Hikâye 12: tohum hayri-0042 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0042
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'portakal', fiil 'sokulmak', sıfat 'iyi'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar kumu portakal tabağına doğru savurdu | tabağı kayanın arkasına götürdü ve oraya sokuldu
@tohum: hayri-0042
Rüzgar denizden sert sert esiyordu. Hayri kumda portakal dilimleriyle baklava dükkanı oyunu oynuyordu. Ama rüzgar kumu portakal tabağına doğru savurmaya başladı. Hayri kumlu portakal yemek istemiyordu. Etrafına baktı ve büyük bir kaya gördü. Kayanın arkası iyi bir yerdi, çünkü orada rüzgar yoktu. Hayri tabağı iki eliyle dikkatle kaldırdı ve kayaya götürdü. Sonra kayanın dibine sokuldu ve tabağı kucağına koydu. Artık portakalın üstüne hiç kum gelmedi. Hayri tatlı bir portakal parçası yedi ve güldü. Hayri bundan sonra rüzgarlı günlerde kayanın arkasında oynadı.
```

**Hakem bulguları (2):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "portakal dilimleriyle baklava dükkanı oyunu oynuyordu"
   - Cümle 2: «Hayri kumda portakal dilimleriyle baklava dükkanı oyunu oynuyordu.»
   - Açıklama: Tohumdaki baklava dükkanı özelliği yalnız süs olarak geçiyor, sorunun çözümünde işe yaramıyor.
   - Açıklama: Baklava dükkanında çalışma özelliği yalnız oyun adı olarak geçiyor ve çözüme katkısı yok.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "portakal dilimleriyle baklava dükkanı oyunu oynuyordu"
   - Cümle 2: «Hayri kumda portakal dilimleriyle baklava dükkanı oyunu oynuyordu.»
   - Açıklama: Baklava dükkanı oyunu kuruluyor ama bir daha geçmiyor ve Hayri portakalı oyun yerine yiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0042` birebir aynı, ardından `@onarim: bd4b51ad53627a207a3519c4b6ca605f770bfd1d`, sonra gövde.
