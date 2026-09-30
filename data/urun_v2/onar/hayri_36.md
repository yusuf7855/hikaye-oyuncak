# Editör görevi (onarım): Hayri, onarım partisi 36

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar36.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar36.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0122 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0122
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'pelerin', fiil 'tutunmak', sıfat 'açık'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: sürpriz bitmeden amca erken geldi | amcayı güldürdü ve sürprizi hızla bitirdi
@tohum: hayri-0122
Bir sabah Hayri ormanda Basri Amca'ya doğum günü sürprizi hazırlıyordu. Ağaçların arasındaki açık bir yere pelerinini serdi ve üstüne çiçek koymaya başladı. Ama sürpriz bitmeden Basri Amca erken geldi. Hayri koşarak amcanın önüne geçti. "Amca, şimdi bakarsan ben yüz kere üzülürüm!" dedi Hayri abartarak. Basri Amca güldü ve gözlerini kapattı. Hayri hızla dönüp son çiçekleri de koydu. Basri Amca gözleri kapalı Hayri'nin koluna tutundu ve yürüdü. "Şimdi bak, iyi ki doğdun!" dedi Hayri. Basri Amca çiçekleri görünce gülümsedi. "Çok güzel bir sürpriz, teşekkürler, Hayri," dedi Basri Amca. Hayri çok sevindi, çünkü sürprizini tam zamanında bitirmişti.
```

**Hakem bulguları (2):**

1. **K6** (K merceği) — Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
   - Alıntı: "açık bir yere pelerinini serdi"
   - Cümle 2: «Ağaçların arasındaki açık bir yere pelerinini serdi ve üstüne çiçek koymaya başladı.»
   - Açıklama: Kartta Hayri'nin pelerini gibi bir eşya yok; kapalı dünyaya aykırı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ben yüz kere üzülürüm"
   - Cümle 5: «"Amca, şimdi bakarsan ben yüz kere üzülürüm!" dedi Hayri abartarak.»
   - Açıklama: 'Yüz kere üzülmek' abartı ve mecaz; 'abartarak' da küçük çocuğun bilmeyeceği soyut bir kelime.
   - Açıklama: 'Yüz kere üzülmek' abartılı bir mecaz; küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0122` birebir aynı, ardından `@onarim: 0292cf34449a68b7992ba19cf6101e2eabe46140`, sonra gövde.

### Hikâye 2: tohum hayri-0123 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0123
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: sırayla oynamak
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'keman', fiil 'dizmek', sıfat 'sarı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: kozalaklar uzaktı ve top onlara çarpmadı | kozalakları tepsideki baklava gibi yan yana dizdi
@tohum: hayri-0123
@degisim: keman -> kozalak
Ormandaki kamp yerinde Hayri ile Yumak sırayla oynuyordu. Hayri yere kozalakları dizdi ve sarı topu onlara yuvarladı. Ama kozalaklar birbirinden uzaktı ve top hiçbir kozalağa çarpmadı. Yumak da topu itti ama yine hiçbiri devrilmedi. Yumak kulaklarını indirdi ve yere yattı. Hayri dükkanda baklavaları tepsiye sıkı sıkı dizerdi. Şimdi kozalakları da öyle, yan yana dizdi. "Sıra yine sende, Yumak!" dedi Hayri. Yumak kalktı, koştu ve topa burnuyla vurdu. Top ilk kozalağa çarptı ve hepsi birden devrildi. Yumak havladı ve kuyruğunu salladı. "Aferin, Yumak, hiçbiri ayakta kalmadı!" dedi Hayri sevinçle.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "hiçbiri ayakta kalmadı"
   - Cümle 12: «"Aferin, Yumak, hiçbiri ayakta kalmadı!" dedi Hayri sevinçle.»
   - Açıklama: Kozalaklar için 'ayakta kalmak' mecazlı bir anlatım.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0123` birebir aynı, `@degisim: keman -> kozalak` (tutuyorsan), ardından `@onarim: db9ffb531711ef0676d77a10161d08afe2d7f7aa`, sonra gövde.

### Hikâye 3: tohum hayri-0124 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Basri Amca
@tohum: hayri-0124
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Basri Amca
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'salatalık', fiil 'toplamak', sıfat 'çıtır'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Basri Amca
@plan: bir dalga salatalık dolu örtüye doğru geldi | amcaya bağırdı ve salatalıkları hızla topladı
@tohum: hayri-0124
Deniz kıyısında Hayri ile Basri Amca kuma bir örtü sermişti. Örtü suya yakındı ve üstünde çıtır salatalıklar vardı. Birden örtüye doğru bir dalga geldi. Basri Amca oturuyordu ve dalgayı görmedi. "Amca, dağ kadar bir dalga geliyor, kalk!" diye bağırdı Hayri abartarak. Basri Amca hemen ayağa kalktı ve sepeti aldı. Hayri de salatalıkları hızla topladı ve sepete koydu. Dalga küçüktü ama örtünün ucunu ıslattı. Salatalıklar sepette hiç ıslanmadı. "Dağ kadar değildi ama iyi ki bağırdın, Hayri," dedi Basri Amca gülerek. Sonra Hayri ile Basri Amca kuru kumda salatalıkları mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "dağ kadar bir dalga"
   - Cümle 5: «"Amca, dağ kadar bir dalga geliyor, kalk!" diye bağırdı Hayri abartarak.»
   - Açıklama: 'Dağ kadar' mecazlı bir abartı ifadesi, küçük çocuk için soyut.
   - Açıklama: 'Dağ kadar' abartılı bir mecaz ve 'abartarak' soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0124` birebir aynı, ardından `@onarim: b16d0c3e80c207ba2c4cef535d091863cd1180cc`, sonra gövde.

### Hikâye 4: tohum hayri-0125 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Kamil
@tohum: hayri-0125
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yorgan', fiil 'koşmak', sıfat 'pembe'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Kamil
@plan: arkadaşı pembe yorganı üstünde uyudu ve uyanmadı | sıcak simit kokusuyla arkadaşını uyandırdı
@tohum: hayri-0125
Bir sabah Hayri ile Kamil deniz kıyısında yarış yapacaktı. Ama Kamil pembe yorganını kuma serdi ve hemen uyudu. "Kamil, kalk, yarış zamanı!" dedi Hayri. Kamil uyanmadı, yalnız yorganın içinde döndü. Hayri arkadaşının omzuna yavaşça dokundu ama Kamil gözlerini açmadı. Bu sırada Hayri acıkmıştı ve çantasından sıcak bir simit çıkardı. Simidi Kamil'in burnuna doğru tuttu. Güzel koku Kamil'i uyandırdı. Kamil gözlerini açtı ve "Bu koku ne?" diye sordu. Hayri güldü, simidi ikiye böldü ve yarısını Kamil'e verdi. İkisi simidi yedi ve kumda koşarak yarıştı. Hayri çok sevindi, çünkü Kamil sonunda uyanmıştı.
```

**Hakem bulguları (5):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "pembe yorganı üstünde uyudu"
   - Cümle 0 (plan satırı): «arkadaşı pembe yorganı üstünde uyudu ve uyanmadı | sıcak simit kokusuyla arkadaşını uyandırdı»
   - Açıklama: Tamlama eksik; 'yorganının üstünde' olmalı.
   - Açıklama: Tamlama eksik; 'pembe yorganının üstünde' olmalı.
2. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Kamil pembe yorganını kuma serdi ve hemen uyudu"
   - Cümle 2: «Ama Kamil pembe yorganını kuma serdi ve hemen uyudu.»
   - Açıklama: Kamil'in yarış öncesi kumda yorganla uyumasının sebebi söylenmiyor ve akla yatkın değil.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "pembe yorganını kuma serdi ve hemen uyudu"
   - Cümle 2: «Ama Kamil pembe yorganını kuma serdi ve hemen uyudu.»
   - Açıklama: Kamil'in yarış öncesi kumda yorgan serip uyumasının sebebi söylenmiyor ve akla yatkın değil.
4. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "yalnız yorganın içinde döndü"
   - Cümle 4: «Kamil uyanmadı, yalnız yorganın içinde döndü.»
   - Açıklama: Yorgan kuma serilmişti, Kamil üstündeydi; 'içinde' yanlış.
5. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu sırada Hayri acıkmıştı"
   - Cümle 6: «Bu sırada Hayri acıkmıştı ve çantasından sıcak bir simit çıkardı.»
   - Açıklama: Çözümü getiren simit, amaçlı bir fikirle değil rastlantısal bir acıkmayla ortaya çıkıyor.
   - Açıklama: Çözümü getiren simit, Hayri'nin tesadüfen acıkmasıyla sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0125` birebir aynı, ardından `@onarim: 9065f3da7f84a91c6e67a9a5cb42549d8cb2e148`, sonra gövde.

### Hikâye 5: tohum hayri-0126 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Yumak
@tohum: hayri-0126
- yer: park (Mahallenin çocuk parkı.)
- tema: aynı sahnede küçük bir kutlama ya da sürpriz hazırlamak
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fıstık', fiil 'ıslanmak', sıfat 'soslu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Yumak
@plan: yağmur başladı ama baklava tepsisi açıktı | kapağı kapattı ve tepsiyi kaydırağın altına taşıdı
@tohum: hayri-0126
@degisim: soslu -> kuru
Parkta Hayri, arkadaşları için bir sürpriz hazırlıyordu. Dükkandan getirdiği baklavaların üstüne fıstık serpti. Birden yağmur başladı, ama tepsi açıktı. Yumak havladı ve kaydırağın altına koştu. Hayri, dükkanda yaptığı gibi, kapağı hemen sıkıca kapattı. Sonra tepsiyi iki eliyle kaldırdı ve Yumak'ın yanına koştu. Kaydırağın altı kuruydu. Hayri orada kapağı açtı ve baklavalara baktı. Hiçbir baklava ıslanmadı ve fıstıklar da yerindeydi. Yumak kuyruğunu salladı ve tepsiyi kokladı. "Sağ ol, Yumak, sürprizimiz kurtuldu!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "sürprizimiz kurtuldu"
   - Cümle 11: «"Sağ ol, Yumak, sürprizimiz kurtuldu!" dedi Hayri.»
   - Açıklama: 'Sürprizin kurtulması' mecazlı ve soyut bir anlatım, küçük çocuğa uygun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0126` birebir aynı, `@degisim: soslu -> kuru` (tutuyorsan), ardından `@onarim: c795ca6e37670ce2330aafceb1e103a7ddba30a3`, sonra gövde.

### Hikâye 6: tohum hayri-0127 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0127
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: sırayla oynamak
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'fide', fiil 'koparmak', sıfat 'memnun'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: dalga kovayı götürdü ve kale yarım kaldı | boş baklava kutusunu kova yaptı ve sırayla doldurdular
@tohum: hayri-0127
@degisim: fide -> kova
Deniz kıyısında Hayri ile Akın sırayla kumdan kale yapıyordu. Hayri kovayı dolduruyor, Akın ters çeviriyordu. Birden bir dalga geldi ve kovayı alıp uzağa götürdü. Akın üzüldü, çünkü kale daha yarımdı. Hayri çantasına baktı ve dükkandan getirdiği boş baklava kutusunu buldu. Az önce kutudaki baklavaları birlikte yemişlerdi. Hayri kutunun kapağını kopardı ve kutuyu kova gibi kullandı. "Şimdi sıra sende, Akın," dedi Hayri. Akın kutuyu kumla doldurdu ve ters çevirdi. Kumdan kare bir kule çıktı. Akın çok memnun oldu ve ellerini çırptı. Hayri ile Akın sırayla kuleler yaptı ve kaleyi mutlu mutlu bitirdi.
```

**Hakem bulguları (1):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Akın çok memnun oldu"
   - Cümle 11: «Akın çok memnun oldu ve ellerini çırptı.»
   - Açıklama: 'Memnun' 3 yaşındaki bir çocuğun bilmeyebileceği soyut bir kelime.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0127` birebir aynı, `@degisim: fide -> kova` (tutuyorsan), ardından `@onarim: 9fc9b1c71b053654b1abeb3c0048fd48bb590618`, sonra gövde.

### Hikâye 7: tohum hayri-0128 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0128
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'avokado', fiil 'basmak', sıfat 'şapkalı'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: adımları küçük olduğu için resim kumda belli olmadı | adımlarını büyüttü ve kuma sertçe bastı
@tohum: hayri-0128
@degisim: avokado -> güneş
Deniz kıyısında Hayri kuma basarak bir resim yapıyordu. Şapkalı bir güneş yapmak istiyordu. Ama adımları küçüktü ve güneş kumda hiç belli olmadı. Hayri biraz düşündü ve adımlarını abarttı. Uzun adımlar attı ve kuma sertçe bastı. Güneşin ışıklarını iki ayağıyla zıplayarak yaptı. Sonra güneşin üstüne büyük adımlarla bir şapka yaptı. Geri çekildi ve resmine baktı. Resim artık çok büyük ve belliydi. Hayri çok güldü ve sevindi, çünkü şapkalı güneş uzaktan bile görünüyordu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "düşündü ve adımlarını abarttı"
   - Cümle 4: «Hayri biraz düşündü ve adımlarını abarttı.»
   - Açıklama: 'Abartmak' adımları büyütmek anlamına gelmez; kelime yanlış anlamda.
   - Açıklama: 'Abartmak' burada yanlış anlamda kullanılmış; 'adımlarını büyüttü' olmalı.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "düşündü ve adımlarını abarttı"
   - Cümle 4: «Hayri biraz düşündü ve adımlarını abarttı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime ve burada 'büyüttü' yerine yanlış anlamda kullanılmış.
   - Açıklama: 'Abarttı' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "düşündü ve adımlarını abarttı"
   - Cümle 4: «Hayri biraz düşündü ve adımlarını abarttı.»
   - Açıklama: Karttaki özellik olayları abartmak; burada adımları büyütmek olarak kelime oyunuyla yanlış kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0128` birebir aynı, `@degisim: avokado -> güneş` (tutuyorsan), ardından `@onarim: fcded11d847dd0458ee999565dac146ad6806cbe`, sonra gövde.

### Hikâye 8: tohum hayri-0129 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Mert
@tohum: hayri-0129
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: kaybolan eşya
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'tabela', fiil 'işaretlemek', sıfat 'güzel'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Mert
@plan: rüzgar dükkanın tabelasını uçurdu ve tabela kayboldu | yaprakların toplandığı köşeye bakıp tabelayı buldu
@tohum: hayri-0129
@degisim: işaretlemek -> asmak
Sokakta sert bir rüzgar esiyordu. Hayri'nin çalıştığı baklava dükkanının güzel tabelası kaybolmuştu. Rüzgar tabelayı kapıdan düşürmüş ve alıp götürmüştü. Mert de Hayri'ye yardım etmek için geldi. İkisi evlerin önüne baktı ama tabelayı bulamadı. Hayri dükkanın önünü süpürürken yaprakları hep köşedeki duvarın yanında bulurdu. "Rüzgar yaprakları o köşeye götürür, Mert," dedi Hayri. İkisi köşeye koştu. Tabela yaprakların arasında, duvarın yanında duruyordu. Hayri tabelayı kaldırdı ve üstündeki yaprakları silkti. Sonra ikisi tabelayı dükkanın kapısına sıkıca astı. Hayri, Mert'e bir dilim baklava verdi ve ikisi mutlu mutlu yedi.
```

**Hakem bulguları (1):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Sokakta sert bir rüzgar esiyordu"
   - Cümle 1: «Sokakta sert bir rüzgar esiyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta ve dükkanın önünde geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta, dükkanın önünde geçiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0129` birebir aynı, `@degisim: işaretlemek -> asmak` (tutuyorsan), ardından `@onarim: 4ca728eac1ac7d2448b031e4009bf4ca31f94732`, sonra gövde.

### Hikâye 9: tohum hayri-0130 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Yumak
@tohum: hayri-0130
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'dalga', fiil 'kalkmak', sıfat 'geniş'
- diyalog: var
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | Yumak
@plan: dalga köpeğin topunu suya çekti | geniş tepsiyi uzatıp topu kıyıya getirdi
@tohum: hayri-0130
Bir sabah Hayri deniz kıyısında Yumak'la top oynuyordu. Yanında geniş bir baklava tepsisi vardı, onu dükkana geri götürecekti. Birden bir dalga geldi ve Yumak'ın topunu suya çekti. Top su kenarında sallanıyordu ama Hayri'nin eli ona yetişemedi. Yumak topa bakıp havladı ve kuma oturdu. Hayri suya girmedi, kenarda durdu. Geniş tepsiyi aldı ve ucunu suya uzattı. Tepsiyle topu yavaşça kendine doğru çekti. Top kuma yuvarlandı. Yumak hemen kalktı ve topa koştu. Sonra kuyruğunu salladı ve Hayri'nin elini kokladı. Hayri çok sevindi, çünkü Yumak'ın topunu dalgadan geri almıştı.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "geniş bir baklava tepsisi vardı"
   - Cümle 2: «Yanında geniş bir baklava tepsisi vardı, onu dükkana geri götürecekti.»
   - Açıklama: Plajda baklava tepsisi yalnız çözümü getirmek için kurulmuş gibi sebepsizce beliriyor.
2. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Geniş tepsiyi aldı ve ucunu suya uzattı"
   - Cümle 7: «Geniş tepsiyi aldı ve ucunu suya uzattı.»
   - Açıklama: Çocuk yalnız başına dalgaların içindeki topa uzanmayı taklit edebilir.
   - Açıklama: Dalganın suya çektiği topu su kenarından uzanarak almak çocuğun taklit edebileceği tehlikeli bir davranış.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0130` birebir aynı, ardından `@onarim: ddb590fc855748c695dac257a60f438f80c4b4fa`, sonra gövde.

### Hikâye 10: tohum hayri-0131 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | park | Kamil
@tohum: hayri-0131
- yer: park (Mahallenin çocuk parkı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'şerit', fiil 'anlatmak', sıfat 'akıllı'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Kamil
@plan: arkadaşı hazineyi nereye sakladığını unuttu | acıktı ve poğaça kokusunu izleyip hazineyi buldu
@tohum: hayri-0131
Parkta Hayri ile Kamil hazine avı oynuyordu. Kamil bir hazine saklamıştı ve Hayri onu arayacaktı. Ama Kamil hazineyi nereye sakladığını unuttu. Yerini anlatmaya çalıştı ama hep başka bir yeri gösterdi. "Hazine bir paket, içinde de poğaça var," dedi Kamil. Hayri o sırada çok acıkmıştı. Burnunu havaya kaldırdı ve poğaça kokusunu aradı. Koku kaydırağın yanındaki bankın altından geliyordu. Hayri eğildi ve üstünde kırmızı bir şerit olan paketi çıkardı. "Sen çok akıllısın, Hayri!" dedi Kamil. "Hazineyi paylaşalım, yarısı senin, Kamil!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Ama Kamil hazineyi nereye sakladığını unuttu"
   - Cümle 3: «Ama Kamil hazineyi nereye sakladığını unuttu.»
   - Açıklama: Hazine avında hazineyi zaten Hayri arayacaktı, Kamil'in unutması oyunu engelleyen akla yatkın bir sorun değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0131` birebir aynı, ardından `@onarim: 7d1f60a17fa9b720df1aa376b465d9ff8576463f`, sonra gövde.

### Hikâye 11: tohum hayri-0132 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0132
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'leke', fiil 'uyandırmak', sıfat 'yorgun'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: yağmur başladı ve poğaça ıslanıyordu | poğaçayı havluya sardı ve yağmur dinene kadar bekledi
@tohum: hayri-0132
Hayri deniz kıyısında çok oynamıştı ve yorgun olduğu için kumda uyudu. Birden yağmur damlaları yüzüne düştü ve onu uyandırdı. Yanındaki havlunun üstünde duran poğaça da ıslanıyordu. Hayri poğaçayı hemen havluya sardı ve göğsüne bastırdı. Sonra sırtını yağmura döndü. Hayri çok acıkmıştı ama yağmur dinene kadar bekledi. Yağmur kısa sürdü ve güneş yeniden çıktı. Havlunun üstünde küçük ıslak lekeler vardı. Hayri havluyu yavaşça açtı. İçindeki poğaça kuru kalmıştı. Hayri kumda oturdu ve poğaçayı mutlu mutlu yedi.
```

**Hakem bulguları (2):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "yorgun olduğu için kumda uyudu"
   - Cümle 1: «Hayri deniz kıyısında çok oynamıştı ve yorgun olduğu için kumda uyudu.»
   - Açıklama: Hayri deniz kıyısında yalnız başına uyuyor; çocuğun taklit edebileceği güvensiz bir davranış.
   - Açıklama: Çocuğun deniz kıyısında yalnız başına uyuması taklit edilince tehlikeli bir davranış.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "İçindeki poğaça kuru kalmıştı"
   - Cümle 10: «İçindeki poğaça kuru kalmıştı.»
   - Açıklama: Poğaça havluya sarılmadan önce ıslanıyordu ama sonunda kuru kalmış deniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0132` birebir aynı, ardından `@onarim: c8be167b2fc00de3bafaf147589670cb776a8dca`, sonra gövde.

### Hikâye 12: tohum hayri-0134 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0134
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: yağmur ya da kar günü
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'tepsi', fiil 'inmek', sıfat 'tatlı'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: yağmur suyu kumdan gelip kaleyi yıkıyordu | tepsiyle denize giden uzun bir yol kazdı
@tohum: hayri-0134
@degisim: tatlı -> ıslak
Hafif bir yağmur yağıyordu. Hayri deniz kıyısında kumdan bir kale yapıyordu. Islak kumu küçük bir tepsiyle taşıyordu. Birden yukarıdaki kumdan kaleye doğru yağmur suyu aktı. Kalenin bir kulesi yavaşça yıkıldı. Hayri kalesini kurtarmak istedi. Tepsiyle kalenin önüne bir yol kazdı. Sonra abartarak yolu çok uzun ve geniş yaptı. Yol kaleden denize kadar uzandı. Su bu yoldan geçti ve denize indi. Artık kaleye hiç su gitmedi. Hayri yıkılan kuleyi yeniden yaptı. Sonra Hayri yağmurun altında kalesine mutlu mutlu yeni kuleler ekledi.
```

**Hakem bulguları (6):**

1. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "yukarıdaki kumdan kaleye doğru"
   - Cümle 4: «Birden yukarıdaki kumdan kaleye doğru yağmur suyu aktı.»
   - Açıklama: Kelime dizilişi belirsiz; 'yukarıdaki kumdan kale' gibi okunabiliyor.
2. **D1** (D merceği) — Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
   - Alıntı: "Birden yukarıdaki kumdan kaleye"
   - Cümle 4: «Birden yukarıdaki kumdan kaleye doğru yağmur suyu aktı.»
   - Açıklama: 'kumdan' hem 'kumdan kale' hem 'kumdan gelen' diye okunabiliyor; cümle belirsiz.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra abartarak yolu"
   - Cümle 8: «Sonra abartarak yolu çok uzun ve geniş yaptı.»
   - Açıklama: 'Abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'abartarak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Sonra abartarak yolu çok uzun"
   - Cümle 8: «Sonra abartarak yolu çok uzun ve geniş yaptı.»
   - Açıklama: Karttaki özellik olayları abartmak (sözle büyütmek); burada abartı yalnız bedensel büyük bir harekete dönüşmüş, özellik karttaki gibi kullanılmamış.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Yol kaleden denize kadar uzandı"
   - Cümle 9: «Yol kaleden denize kadar uzandı.»
   - Açıklama: Su yukarıdan kaleye akıyor ama yol kaleden denize kazılıyor; çözüm suyun geldiği yere yönelmiyor.
6. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Artık kaleye hiç su gitmedi"
   - Cümle 11: «Artık kaleye hiç su gitmedi.»
   - Açıklama: Yağmur kalenin üstüne yağmaya devam ederken kaleye hiç su gitmediği söyleniyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0134` birebir aynı, `@degisim: tatlı -> ıslak` (tutuyorsan), ardından `@onarim: 824dd45626f7c7cffd0db68b98c01d7d726070d5`, sonra gövde.
