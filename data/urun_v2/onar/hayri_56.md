# Editör görevi (onarım): Hayri, onarım partisi 56

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar56.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar56.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0204 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0204
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'teleskop', fiil 'cevaplamak', sıfat 'sağlıklı'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: ağaçların arasından garip bir ses geldi | teleskopla bütün ağaçlara bakıp sesi yapan dalları buldu
@tohum: hayri-0204
@degisim: sağlıklı -> kuru
Hayri, Akın ile kamp yerinde oturuyordu. Birden ağaçların arasından garip bir ses geldi. Hayri sesi çok merak etti ama nereden geldiğini bulamadı. Akın elindeki teleskopu Hayri'ye verdi. Hayri işi abarttı ve teleskopla bütün ağaçlara tek tek baktı. En uzaktaki ağaçta iki kuru dal gördü. Rüzgar esince bu dallar birbirine çarpıyor ve ses çıkıyordu. Hayri bunun nasıl olduğunu Akın'a sordu. Akın soruyu hemen cevapladı: Kuru dallar rüzgarda böyle ses çıkarırdı. Hayri ile Akın sesi bulduklarına çok sevindi. Hayri bundan sonra ormanda bir ses duyunca teleskopla ağaçlara baktı.
```

**Hakem bulguları (7):**

1. **C1** (K merceği) — Korkutucu öğe yok.
   - Alıntı: "ağaçların arasından garip bir ses geldi"
   - Cümle 2: «Birden ağaçların arasından garip bir ses geldi.»
   - Açıklama: Ormanda kaynağı bilinmeyen garip bir ses 3-6 yaş için korkutucu bir öğe olabilir.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Akın elindeki teleskopu Hayri'ye verdi"
   - Cümle 4: «Akın elindeki teleskopu Hayri'ye verdi.»
   - Açıklama: Teleskop önceden kurulmadan sebepsizce beliriyor ve çözümü getiriyor.
   - Açıklama: Teleskop sebepsiz beliriyor ve yakındaki bir sesi bulmak için akla yatkın bir araç değil.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri işi abarttı ve"
   - Cümle 5: «Hayri işi abarttı ve teleskopla bütün ağaçlara tek tek baktı.»
   - Açıklama: 'İşi abartmak' deyimsel ve soyut bir anlatım; 3 yaşındaki çocuk için uygun değil.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri işi abarttı"
   - Cümle 5: «Hayri işi abarttı ve teleskopla bütün ağaçlara tek tek baktı.»
   - Açıklama: 'İşi abartmak' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuk anlamaz.
5. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "teleskopla bütün ağaçlara tek tek baktı"
   - Cümle 5: «Hayri işi abarttı ve teleskopla bütün ağaçlara tek tek baktı.»
   - Açıklama: Bir sesin kaynağını teleskopla bütün ağaçlara tek tek bakarak aramak sebebe doğrudan yönelen kısa bir çözüm değil.
6. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri bunun nasıl olduğunu Akın'a sordu"
   - Cümle 8: «Hayri bunun nasıl olduğunu Akın'a sordu.»
   - Açıklama: Sebep bir önceki cümlede zaten söylenmişken soru ve cevap işlevsiz tekrar oluyor.
7. **M9** (M merceği) — Hikayenin açık ve küçük bir hedefi var ve son bu hedefe doyurucu biçimde ulaşıyor: sorunun çözüldüğü görünüyor ve son cümle sıcak bir kapanış veriyor (olaya bağlı bir his, mutlu bir sonuç, sıcak bir replik ya da olaydan çıkan somut bir ders). Son cümle kapanışsız, çıplak bir eylem ya da durgun bir resimse ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'), okur ne olduğunu merak ederek kalıyorsa (hazine kutusu bulunuyor ama hiç açılmıyor) ya da hikayede hiçbir şey olmuyorsa M9 'var'dır. Ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor.
   - Alıntı: "Hayri bundan sonra ormanda bir ses duyunca teleskopla ağaçlara baktı"
   - Cümle 11: «Hayri bundan sonra ormanda bir ses duyunca teleskopla ağaçlara baktı.»
   - Açıklama: Son cümle olaydan çıkan sıcak bir ders değil, tuhaf ve çıplak bir alışkanlık cümlesi.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0204` birebir aynı, `@degisim: sağlıklı -> kuru` (tutuyorsan), ardından `@onarim: d2ae418f802d19034cc406788c94587b45812ee8`, sonra gövde.

### Hikâye 2: tohum hayri-0205 (deneme 1 -> 2)

**Görev:** YENİDEN YAZ: hakem bu hikâyenin çekirdeğini önemsiz ya da saçma buldu (M3). Aynı tohumdan, çocuğun önemseyeceği bir sorunla baştan yaz.

**Tohum:**

```
### Hayri | orman | Kamil
@tohum: hayri-0205
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: figür başkasına yardım eder (hasta ya da yaralı hayvan değil)
- yan: Kamil
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'tuz', fiil 'yoğurmak', sıfat 'bulutlu'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Kamil
@plan: arkadaşının salatasında hiç tuz yoktu | yemek kutusundaki tuzu salataya serpti
@tohum: hayri-0205
@degisim: yoğurmak -> karıştırmak
Gökyüzü bulutluydu ve serin bir rüzgar esiyordu. Hayri ile Kamil kamp yerinde öğle yemeği hazırlıyordu. Kamil bir kapta salata karıştırdı ama yanında hiç tuz yoktu. "Bu salata tuz olmadan güzel olmaz," dedi Kamil. O sırada Hayri çok acıkmıştı ve çantasındaki yemek kutusunu açtı. Kutuda yumurtalar ve küçük bir tuzluk vardı. "Kamil, bak, burada tuz var!" dedi Hayri. Hayri salataya biraz tuz serpti. Kamil de salatayı yeniden karıştırdı. Kamil bir lokma yedi ve gülümsedi. "Şimdi çok lezzetli oldu, Hayri!" dedi Kamil. Sonra Hayri ile Kamil salatayı ve yumurtaları mutlu mutlu paylaştı.
```

**Hakem bulguları (3):**

1. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "Bu salata tuz olmadan güzel olmaz"
   - Cümle 4: «"Bu salata tuz olmadan güzel olmaz," dedi Kamil.»
   - Açıklama: Salatada tuz olmaması 3-6 yaş çocuğun önemseyeceği bir sorun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri çok acıkmıştı"
   - Cümle 5: «O sırada Hayri çok acıkmıştı ve çantasındaki yemek kutusunu açtı.»
   - Açıklama: Tuz, Hayri sorunu çözmek için değil acıktığı için kutuyu açınca tesadüfen beliriyor; çözüm sebepsizce geliyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri çok acıkmıştı ve çantasındaki yemek kutusunu açtı"
   - Cümle 5: «O sırada Hayri çok acıkmıştı ve çantasındaki yemek kutusunu açtı.»
   - Açıklama: Tuz, Hayri acıktığı için rastlantıyla açtığı kutudan çıkıyor; çözüm sorundan değil tesadüften geliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0205` birebir aynı, `@degisim: yoğurmak -> karıştırmak` (tutuyorsan), ardından `@onarim: 4e13928cf6096383f33f80e8060dac4abdb5bf41`, sonra gövde.

### Hikâye 3: tohum hayri-0206 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Akın
@tohum: hayri-0206
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: bir şey yapmak
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'hazine', fiil 'alkışlamak', sıfat 'tekerlekli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Akın
@plan: araba sallanınca kutu yere düştü | ipi kutuyla arabanın çevresine on kez sardı
@tohum: hayri-0206
Bir sabah Hayri ile Akın kamp yerinde bir kozalak hazinesi topladı. Hazineyi taşımak için Akın'ın tekerlekli arabasına bir kutu koydular. Ama araba her taşa çarpınca kutu yere düştü. Kozalaklar yaprakların arasına dağıldı. Hayri kamp çantasından uzun bir ip çıkardı. Hayri yine abarttı ve ipi arabanın çevresine tam on kez sardı. Kutu arabaya sımsıkı bağlandı. Akın kozalakları yeniden kutuya doldurdu. Hayri arabayı taşların üstünden yavaşça çekti. Kutu bu kez hiç kıpırdamadı. Akın sevinçle Hayri'yi alkışladı. Hayri ile Akın hazine arabasını ağaçların arasında mutlu mutlu dolaştırdı.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "bir kozalak hazinesi topladı"
   - Cümle 1: «Bir sabah Hayri ile Akın kamp yerinde bir kozalak hazinesi topladı.»
   - Açıklama: Kozalaklara 'hazine' demek mecaz; küçük çocuk için soyut.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri yine abarttı ve"
   - Cümle 6: «Hayri yine abarttı ve ipi arabanın çevresine tam on kez sardı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelimedir.
   - Açıklama: 'Abarttı' soyut bir kelime ve 'yine' daha önce geçmeyen bir abartmaya gönderme yapıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0206` birebir aynı, ardından `@onarim: fa57ee4508fdc303054777df452e582225bae28a`, sonra gövde.

### Hikâye 4: tohum hayri-0207 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Kamil
@tohum: hayri-0207
- yer: park (Mahallenin çocuk parkı.)
- tema: sırayla oynamak
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'taş', fiil 'kazanmak', sıfat 'serin'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Kamil
@plan: iki arkadaşın tek bir taşı vardı | arkadaşına önce sırayı verip beklerken zıpladı
@tohum: hayri-0207
Parkta serin bir rüzgar esiyordu. Hayri ile Kamil seksek oynayacaktı ama tek bir taşları vardı. İkisi de taşı önce atmak istedi. "Taşı ben atacağım!" dedi Kamil. Hayri biraz düşündü ve güldü. "Önce sen at, Kamil, ben beklerken yüz kez zıplarım!" dedi Hayri. Kamil taşı attı ve tek ayak üstünde zıpladı. Hayri de yanında abartarak kocaman zıpladı ve saydı. Kamil ona bakıp çok güldü. Sonra sıra Hayri'ye geldi ve bu kez Kamil zıpladı. İkisi taşı sırayla attı ve hiç kavga etmedi. Oyunu Kamil kazandı ama Hayri hiç üzülmedi. Hayri çok mutluydu, çünkü sırayla oynamak çok eğlenceliydi.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "yanında abartarak kocaman zıpladı"
   - Cümle 8: «Hayri de yanında abartarak kocaman zıpladı ve saydı.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "sıra Hayri'ye geldi ve bu kez Kamil zıpladı"
   - Cümle 10: «Sonra sıra Hayri'ye geldi ve bu kez Kamil zıpladı.»
   - Açıklama: Sıra Hayri'ye geldiği halde zıplayan yine Kamil oluyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0207` birebir aynı, ardından `@onarim: 1d72bedfa5d5f54f53e816a8e74e9f143dd01c86`, sonra gövde.

### Hikâye 5: tohum hayri-0209 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Yumak
@tohum: hayri-0209
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: sıkışmış, kaybolmuş ya da aç bir hayvana yardım (hasta ya da yaralı hayvan değil)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'kitaplık', fiil 'fırçalamak', sıfat 'karışık'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Yumak
@plan: köpek sokakta kaybolmuştu ve yaklaşmıyordu | baklava kokan önlüğüyle köpeği bahçesine götürdü
@tohum: hayri-0209
@degisim: fırçalamak -> koklamak
Mahallenin sokağında Hayri baklava dükkanından dönüyordu. Bir evin önündeki eski kitaplığın arkasında Yumak'ı gördü. Bahçe kapısı açık kalmıştı ve Yumak karışık sokaklarda evini bulamamıştı. Hayri eğildi ama Yumak yanına gelmedi. Sonra Hayri önlüğüne baktı. Önlüğü dükkandaki baklavalar gibi kokuyordu. Hayri önlüğünü çıkardı ve Yumak'a uzattı. Yumak önlüğü kokladı ve kuyruğunu salladı. Hemen Hayri'nin arkasından yürüdü. Hayri onu Yumak'ın açık bahçe kapısına götürdü. Yumak bahçeye koştu ve Hayri kapıyı dışarıdan kapattı. Hayri önlüğünü yeniden giydi ve mutlu mutlu evine gitti.
```

**Hakem bulguları (2):**

1. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "köpeği bahçesine götürdü"
   - Cümle 0 (plan satırı): «köpek sokakta kaybolmuştu ve yaklaşmıyordu | baklava kokan önlüğüyle köpeği bahçesine götürdü»
   - Açıklama: Plandaki 'bahçesine' zamirinin Hayri'nin mi köpeğin mi bahçesini gösterdiği belli değil.
2. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Mahallenin sokağında Hayri baklava dükkanından dönüyordu"
   - Cümle 1: «Mahallenin sokağında Hayri baklava dükkanından dönüyordu.»
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta başlıyor ve geçiyor.
   - Açıklama: Başlıktaki yer ev iken hikaye sokakta başlıyor ve Hayri'nin evine gitmesiyle bitiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0209` birebir aynı, `@degisim: fırçalamak -> koklamak` (tutuyorsan), ardından `@onarim: 0e22166ae3639c31de07f8c6c6bfc2009e4a252e`, sonra gövde.

### Hikâye 6: tohum hayri-0210 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Basri Amca
@tohum: hayri-0210
- yer: park (Mahallenin çocuk parkı.)
- tema: paylaşmak
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'pencere', fiil 'yapıştırmak', sıfat 'dalgalı'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | Basri Amca
@plan: dükkanda baklava kalmamıştı ve amca üzüldü | kutusundaki baklavaları amcayla paylaştı
@tohum: hayri-0210
@degisim: pencere -> kutu
Serin bir rüzgar esiyordu. Hayri parkta tahta bir bankta oturuyordu ve kucağında baklava kutusu vardı. "Hayri, dükkanda hiç baklava kalmamış," dedi Basri Amca üzgün üzgün. Basri Amca bankın öbür ucuna oturdu. Hayri kutusuna baktı. Kutuyu dükkanda kendi eliyle hazırlamış, kapağına bir etiket yapıştırmıştı. Hayri etiketi yavaşça kaldırdı ve kutuyu açtı. Sonra iki baklavayı altındaki dalgalı kağıtla birlikte çıkardı. "Alın, Basri Amca, bunlar sizin," dedi Hayri. Basri Amca kağıdı aldı ve gülümsedi. "Çok teşekkür ederim, Hayri," dedi Basri Amca. Sonra Hayri ile Basri Amca baklavalarını mutlu mutlu yediler.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "kapağına bir etiket yapıştırmıştı"
   - Cümle 6: «Kutuyu dükkanda kendi eliyle hazırlamış, kapağına bir etiket yapıştırmıştı.»
   - Açıklama: Etiket işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.
   - Açıklama: Etiket ayrıntısı işe yarayacakmış gibi kuruluyor ama olayda hiçbir işlevi yok.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0210` birebir aynı, `@degisim: pencere -> kutu` (tutuyorsan), ardından `@onarim: fad600e691cc956c2263cf1468b2a07d1660e735`, sonra gövde.

### Hikâye 7: tohum hayri-0211 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Mert
@tohum: hayri-0211
- yer: park (Mahallenin çocuk parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Mert
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'düdük', fiil 'tanışmak', sıfat 'ince'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | Mert
@plan: düdüğü sormadan aldı ve arkadaşı üzüldü | özür diledi ve baklavasını paylaştı
@tohum: hayri-0211
@degisim: tanışmak -> aramak
Parkta Mert bankların altına eğilip bir şey arıyordu. Hayri cebine elini soktu ve Mert'in ince düdüğünü buldu. Düdüğü Mert'e sormadan almış ve sonra unutmuştu. Hayri hemen Mert'in yanına koştu. "Düdük bende, Mert, çok özür dilerim," dedi Hayri. Mert düdüğünü aldı ama biraz üzgündü. Hayri çantasından küçük bir baklava kutusu çıkardı. Kutudaki baklavaları dükkanda kendisi hazırlamıştı. "Gel, bunları seninle paylaşalım," dedi Hayri. Mert gülümsedi ve bir baklava aldı. "Tamam, Hayri, ama bir dahaki sefere önce bana sor," dedi Mert. Hayri çok rahatladı, çünkü arkadaşı yine gülüyordu.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutudaki baklavaları dükkanda kendisi hazırlamıştı"
   - Cümle 8: «Kutudaki baklavaları dükkanda kendisi hazırlamıştı.»
   - Açıklama: Baklavaların dükkanda hazırlanması olayda işe yaramayan bir ayrıntı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0211` birebir aynı, `@degisim: tanışmak -> aramak` (tutuyorsan), ardından `@onarim: 682bd8c61617c5219c908dfaa6f34d939dd316a4`, sonra gövde.

### Hikâye 8: tohum hayri-0212 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0212
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yağ', fiil 'yemek', sıfat 'enerjik'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: rüzgar yemek paketini çalıların arasına düşürdü | köpekten yardım istedi ve köpek paketi buldu
@tohum: hayri-0212
Rüzgar ağaçların arasında hızlı hızlı esiyordu. Hayri kamp yerinde çok acıkmıştı ve yemek paketini aradı. Ama rüzgar paketi kütüğün üstünden çalıların arasına düşürmüştü. Hayri çalılara baktı ama paketi göremedi. Yanında enerjik Yumak zıplayıp duruyordu. "Yumak, yemeğimi bulur musun, lütfen?" diye sordu Hayri. Yumak burnunu yere yaklaştırdı ve çalıları tek tek kokladı. Sonra bir çalının dibinde durdu ve havladı. Hayri eğildi ve paketi orada buldu. İçinde ekmek, küçük bir kutu yağ ve bir elma vardı. Hayri ekmeğine biraz yağ sürdü ve afiyetle yedi. "Teşekkürler, Yumak, yemeğimi sen buldun!" dedi Hayri.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "küçük bir kutu yağ ve bir elma vardı"
   - Cümle 10: «İçinde ekmek, küçük bir kutu yağ ve bir elma vardı.»
   - Açıklama: Elma işe yarayacakmış gibi sayılıyor ama hiç kullanılmıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0212` birebir aynı, ardından `@onarim: 81c235dc651b3481310992feffe4b3a34eea2c8f`, sonra gövde.

### Hikâye 9: tohum hayri-0213 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0213
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'cüzdan', fiil 'içmek', sıfat 'rüzgarlı'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: top amcanın tabağına çarptı ve ekmeği düştü | özür diledi ve baklavasını verdi
@tohum: hayri-0213
@degisim: cüzdan -> tabak
Hayri rüzgarlı kamp yerinde top oynuyordu. Basri Amca bir kütüğün üstünde oturmuş, çay içiyordu. Hayri topa çok sert vurdu ve top Basri Amca'nın tabağına çarptı. Tabaktaki ekmek toprağa düştü. "Hayri, bak ne yaptın!" dedi Basri Amca kızgın kızgın. Hayri hemen yanına gitti. "Özür dilerim, Basri Amca, dikkat etmedim," dedi Hayri. Sonra çantasından baklava kutusunu çıkardı. Kutuyu çalıştığı dükkandan getirmişti. "Bu baklava sizin olsun," dedi Hayri. Basri Amca bir baklava aldı ve gülümsedi. "Teşekkür ederim, Hayri, çok güzel olmuş," dedi Basri Amca. Hayri bundan sonra topu herkesten uzakta oynadı.
```

**Hakem bulguları (1):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Kutuyu çalıştığı dükkandan getirmişti"
   - Cümle 9: «Kutuyu çalıştığı dükkandan getirmişti.»
   - Açıklama: Çözümü getiren baklava kutusu çantadan sebepsizce beliriyor ve sonradan açıklanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0213` birebir aynı, `@degisim: cüzdan -> tabak` (tutuyorsan), ardından `@onarim: e1db081ec41ebf8e5b8a0c6b5eb8175f29e1198f`, sonra gövde.

### Hikâye 10: tohum hayri-0214 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0214
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'köpük', fiil 'kavuşmak', sıfat 'yamuk'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: yamuk halkadan hiç balon çıkmadı | kocaman ve yuvarlak yeni bir halka yaptı
@tohum: hayri-0214
@degisim: kavuşmak -> üflemek
Ormandaki kamp yerinde hava sıcaktı. Hayri bir kovaya sabunlu su koymuş, köpük balonu uçurmak istiyordu. Ama elindeki tel halka yamuktu, bu yüzden hiç balon çıkmadı. Hayri halkaya üfledi ama köpük hemen dağıldı. Sonra Hayri işi abarttı. Teli açtı ve kova kadar büyük, yuvarlak bir halka kıvırdı. Halkayı kovaya batırdı ve kollarını yavaşça salladı. Havada kocaman bir balon oluştu. Balon Hayri'nin burnuna değdi ve pat diye patladı. Hayri çok güldü ve yeni bir balon uçurdu. Hayri bundan sonra balon oyununda halkasını hep düzgün ve yuvarlak tuttu.
```

**Hakem bulguları (4):**

1. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "bir kovaya sabunlu su koymuş"
   - Cümle 2: «Hayri bir kovaya sabunlu su koymuş, köpük balonu uçurmak istiyordu.»
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı biçime kayıyor; 'koymuştu' olmalı.
2. **D3** (D merceği) — Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
   - Alıntı: "sabunlu su koymuş"
   - Cümle 2: «Hayri bir kovaya sabunlu su koymuş, köpük balonu uçurmak istiyordu.»
   - Açıklama: Anlatım -dı'lı geçmişten -mış'lı geçmişe kayıyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Sonra Hayri işi abarttı"
   - Cümle 5: «Sonra Hayri işi abarttı.»
   - Açıklama: 'İşi abartmak' deyimsel ve soyut bir anlatımdır, üstelik doğru çözümü yanlış tanımlıyor.
   - Açıklama: 'İşi abarttı' deyimsel ve soyut bir anlatım.
4. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "kova kadar büyük, yuvarlak bir halka kıvırdı"
   - Cümle 6: «Teli açtı ve kova kadar büyük, yuvarlak bir halka kıvırdı.»
   - Açıklama: Halka kova kadar büyük yapılıyor ama hemen ardından kovanın içine batırılıyor, bu mümkün değil.
   - Açıklama: Kova kadar büyük halkanın aynı kovaya batırılabilmesi çelişkili.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0214` birebir aynı, `@degisim: kavuşmak -> üflemek` (tutuyorsan), ardından `@onarim: 800d4c90f8a012e7c3d0113c1a35fc81078e86f4`, sonra gövde.

### Hikâye 11: tohum hayri-0215 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | ev | Kamil
@tohum: hayri-0215
- yer: ev (Mahalledeki evler, sokak ve bahçeler.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Kamil
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kereviz', fiil 'dalgalanmak', sıfat 'yetenekli'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | ev | Kamil
@plan: koşarken arkadaşının tebeşir resmine bastı | özür diledi ve onu çok güldürdü
@tohum: hayri-0215
@degisim: kereviz -> tebeşir
Hayri sokakta koşarak Kamil'in yanına geldi. Kamil yere tebeşirle büyük bir gemi çizmişti. Resimde geminin bayrağı rüzgarda dalgalanıyordu. Ama Hayri bakmadan resmin üstüne bastı ve bayrak silindi. "Hayri, bayrağım gitti!" dedi Kamil üzgün üzgün. Hayri durdu ve resme baktı. "Özür dilerim, Kamil, koşarken görmedim," dedi Hayri. Sonra Hayri iki kolunu açtı ve abartarak yere kadar eğildi. "Sen dünyanın en yetenekli çocuğusun, Kamil!" dedi Hayri. Kamil buna çok güldü ve tebeşiri eline aldı. "Gel, bayrağı yeniden çizelim," dedi Kamil. Sonra Hayri ile Kamil yeni bayrağı birlikte çizdiler ve mutlu oldular.
```

**Hakem bulguları (5):**

1. **M8** (M merceği) — Tek sahne ve tek zaman: hikaye başlıktaki yerde başlıyor ve bitiyor; hikayenin içinde gün, gece ya da hafta atlaması yok. İstisna: hikayenin son cümlesi olaydan çıkan tek bir ders cümlesiyse 'bundan sonra' ya da 'artık' içerebilir ('Niloya bundan sonra zorda kalınca büyüklerinden yardım istedi.'); bu M8 sayılmaz.
   - Alıntı: "Hayri sokakta koşarak Kamil'in yanına geldi"
   - Cümle 1: «Hayri sokakta koşarak Kamil'in yanına geldi.»
   - Açıklama: Başlıktaki yer ev olduğu halde hikaye sokakta geçiyor.
   - Açıklama: Başlıktaki yer ev ama hikaye sokakta geçiyor.
2. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "geminin bayrağı rüzgarda dalgalanıyordu"
   - Cümle 3: «Resimde geminin bayrağı rüzgarda dalgalanıyordu.»
   - Açıklama: Yere tebeşirle çizilmiş bir bayrak rüzgarda dalgalanamaz; fiil öznesine uymuyor.
   - Açıklama: Tebeşirle yere çizilmiş bir bayrak rüzgarda dalgalanmaz; fiil öznesine uymuyor.
3. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "abartarak yere kadar eğildi"
   - Cümle 8: «Sonra Hayri iki kolunu açtı ve abartarak yere kadar eğildi.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmeyeceği soyut bir kelime.
4. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "ve abartarak yere kadar"
   - Cümle 8: «Sonra Hayri iki kolunu açtı ve abartarak yere kadar eğildi.»
   - Açıklama: 'Abartarak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
5. **M4** (M merceği) — Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
   - Alıntı: "Gel, bayrağı yeniden çizelim"
   - Cümle 11: «"Gel, bayrağı yeniden çizelim," dedi Kamil.»
   - Açıklama: Silinen bayrağı yeniden çizme çözümünü Hayri değil Kamil öneriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0215` birebir aynı, `@degisim: kereviz -> tebeşir` (tutuyorsan), ardından `@onarim: 79fdd8b18380d59274130971b9182de29478446e`, sonra gövde.

### Hikâye 12: tohum hayri-0216 (deneme 1 -> 2)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0216
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'bant', fiil 'tartmak', sıfat 'yağmurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: gökkuşağının renklerini sayarken karıştırdı | acıkınca yiyecekleri renklere göre dizdi
@tohum: hayri-0216
@degisim: tartmak -> saymak
Hayri yağmurlu bir sabah kampta çadırında oturuyordu. Yağmur dindi ve ağaçların üstünde kocaman bir gökkuşağı çıktı. Hayri renkleri saymak istedi ama renkler çok yakın olduğu için karıştırdı. O sırada Hayri çok acıktı. Yemek kutusunun bandını çekip kutuyu açtı. İçinde kırmızı bir elma, turuncu bir havuç ve sarı bir muz vardı. Yeşil bir salatalık ve mor üzümler de vardı. Hayri yiyecekleri gökkuşağı gibi yan yana dizdi. Mavi için de parmağıyla gökyüzünü gösterdi. Sonra her rengi tek tek saydı ve bu kez hiç şaşırmadı. En son kırmızı elmasını afiyetle yedi. Hayri çok sevindi, çünkü gökkuşağının bütün renklerini bulmuştu.
```

**Hakem bulguları (4):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "O sırada Hayri çok acıktı"
   - Cümle 4: «O sırada Hayri çok acıktı.»
   - Açıklama: Çözüm renk karışıklığına yönelmiyor, acıkma tesadüfüyle başlıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "O sırada Hayri çok acıktı"
   - Cümle 4: «O sırada Hayri çok acıktı.»
   - Açıklama: Çözümü getiren açlık sorundan çıkmıyor, tesadüfen beliriyor.
3. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "İçinde kırmızı bir elma, turuncu bir havuç ve sarı bir muz vardı"
   - Cümle 6: «İçinde kırmızı bir elma, turuncu bir havuç ve sarı bir muz vardı.»
   - Açıklama: Kutuda tam gökkuşağı renklerinde yiyecekler olması çözümü sebepsizce getiriyor.
4. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Hayri yiyecekleri gökkuşağı gibi yan yana dizdi"
   - Cümle 8: «Hayri yiyecekleri gökkuşağı gibi yan yana dizdi.»
   - Açıklama: Çözüm renklerin yakın olması sebebine değil, gökkuşağı yerine yiyecekleri saymaya yöneliyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0216` birebir aynı, `@degisim: tartmak -> saymak` (tutuyorsan), ardından `@onarim: eb1aabc0bd1576a5185c05655856203a73d78b3c`, sonra gövde.
