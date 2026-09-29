# Editör görevi (onarım): Hayri, onarım partisi 25

Sen bir çocuk hikâyesi editörüsün. Aşağıdaki 12 hikâye hakem kurulundan somut, alıntılı bulgularla
döndü. Her birinden BİR onarılmış hikâye yaz. Hikâyeler 3-6 yaş çocuklara okunacak ve küçük bir dil modelini
eğitecek. Onarılmış hikâye YENİ bir adaydır: kod kapılarından ve bu bulguları hiç görmeyen yeni hakemlerden
baştan geçer; bütün maddelere yeniden bakılır. Yeni kusur ekleme.

## Kurallar

- Çıktı dosyan: `data/urun_v2/aday/hayri_onar25.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
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
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v2/aday/hayri_onar25.txt --ad urun_v2`
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

### Hikâye 1: tohum hayri-0046 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0046
- yer: park (Mahallenin çocuk parkı.)
- tema: hayali oyun (kaptan, aşçı, bahçıvan olmak gibi) ve oyunda küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'mıknatıs', fiil 'ölçmek', sıfat 'eski'
- diyalog: yok (hikâyede replik yok)
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | park | -
@plan: kum çok kuruydu ve pasta hep dağıldı | kumu ıslattı ve eski kovayla pasta yaptı
@tohum: hayri-0046
@degisim: mıknatıs -> kova
Parkın kum havuzunda Hayri pasta yapma oyunu oynuyordu. Hayri biraz abartıp kule kadar yüksek bir pasta yapmak istiyordu. Ama kum çok kuruydu ve pasta hep dağıldı. Kuru kum hiç birbirine yapışmıyordu. Bu yüzden su şişesini açtı. Suyu oyuncak bardağıyla ölçtü ve iki bardak kuma döktü. Islak kumu eski kovasına sıkıca bastırdı. Sonra kovayı ters çevirdi ve yavaşça kaldırdı. Kumdan pasta bu kez hiç yıkılmadı. Hayri onun üstüne iki kat daha yaptı. Pasta bir kule gibi yükseldi. Hayri onu yapraklarla süsledi ve oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri biraz abartıp kule"
   - Cümle 2: «Hayri biraz abartıp kule kadar yüksek bir pasta yapmak istiyordu.»
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
   - Açıklama: 'Abartmak' soyut bir kavram, 3 yaşındaki çocuğa uygun değil.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Bu yüzden su şişesini açtı"
   - Cümle 5: «Bu yüzden su şişesini açtı.»
   - Açıklama: Su şişesi önceden kurulmadan çözüm anında sebepsizce beliriyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0046` birebir aynı, `@degisim: mıknatıs -> kova` (tutuyorsan), ardından `@onarim: 5277775537ac351fc434bc8067aa4ebe13dfa11c`, sonra gövde.

### Hikâye 2: tohum hayri-0047 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0047
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: kaybolan eşya
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'pizza', fiil 'ıslatmak', sıfat 'çamurlu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: rüzgar şapkayı uçurdu ve şapka kayboldu | kıyıda dikkatle aradı ve taşların arkasında buldu
@tohum: hayri-0047
@degisim: pizza -> şapka
Rüzgar kıyıda hızlı esiyordu. Hayri denizin kenarında yürüyor ve dalgaları izliyordu. Birden rüzgar mavi şapkasını başından kaptı ve uçurdu. Hayri önce dalgaların ıslattığı çamurlu kumda aradı, ama şapka orada yoktu. Kıyıda büyük taşlar vardı. Hayri işi biraz abarttı ve her taşın arkasına tek tek baktı. Sonunda en büyük taşın arkasında mavi bir şey gördü. Şapka orada, kuru kumun üstündeydi. Hayri şapkayı aldı ve başına sıkıca taktı. Hayri çok sevindi, çünkü kaybolan şapkasını bulmuştu.
```

**Hakem bulguları (4):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "işi biraz abarttı ve her taşın"
   - Cümle 6: «Hayri işi biraz abarttı ve her taşın arkasına tek tek baktı.»
   - Açıklama: Taşların arkasına bakmak abartmak değildir; kelime yanlış anlamda.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri işi biraz abarttı"
   - Cümle 6: «Hayri işi biraz abarttı ve her taşın arkasına tek tek baktı.»
   - Açıklama: 'İşi abartmak' deyimsel ve soyut bir anlatım, 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'İşi abartmak' deyimi 3 yaşındaki çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri işi biraz abarttı"
   - Cümle 6: «Hayri işi biraz abarttı ve her taşın arkasına tek tek baktı.»
   - Açıklama: Karttaki özellik olayları abartmak iken burada abartma titizce aramak anlamında kullanılıyor, kartın özellik tanımına uymuyor.
4. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri işi biraz abarttı ve her taşın arkasına tek tek baktı"
   - Cümle 6: «Hayri işi biraz abarttı ve her taşın arkasına tek tek baktı.»
   - Açıklama: Karttaki özellik olayları abartmak; her taşın arkasına bakmak abartma değil dikkatli aramadır.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0047` birebir aynı, `@degisim: pizza -> şapka` (tutuyorsan), ardından `@onarim: 0bdad3e572aa3c79973bcab4bdf48837bf63f522`, sonra gövde.

### Hikâye 3: tohum hayri-0048 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0048
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: doğada bir şeyi fark etmek (gökkuşağı, kelebekler, kardaki şekiller) ve küçük bir hedef
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kürek', fiil 'ilerlemek', sıfat 'yumuşak'
- diyalog: yok (hikâyede replik yok)
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: çukur sudan uzaktı ve içine su gelmedi | çukurdan denize kadar uzun bir yol kazdı
@tohum: hayri-0048
Hayri deniz kıyısında küreğiyle yumuşak kumda bir çukur kazıyordu. Orada küçük bir havuz yapmak istiyordu. Ama çukur sudan uzaktı ve içine hiç su gelmedi. Hayri durdu ve denize dikkatle baktı. Dalgaların kıyıya gelip geri gittiğini fark etti. Hayri işi biraz abarttı ve çukurdan denize kadar uzun bir yol kazdı. Az sonra bir dalga geldi. Su yolun içinde yavaş yavaş ilerledi ve çukura aktı. Birkaç dalgadan sonra havuz suyla doldu. Hayri sevinçle zıpladı ve ellerini çırptı. Hayri bundan sonra havuzuna suyu hep böyle bir yoldan getirdi.
```

**Hakem bulguları (5):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri işi biraz abarttı"
   - Cümle 6: «Hayri işi biraz abarttı ve çukurdan denize kadar uzun bir yol kazdı.»
   - Açıklama: Denize kadar yol kazmak sorunun çözümüdür, abartma değildir; kelime yanlış anlamda kullanılmış.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri işi biraz abarttı"
   - Cümle 6: «Hayri işi biraz abarttı ve çukurdan denize kadar uzun bir yol kazdı.»
   - Açıklama: 'İşi abartmak' soyut bir anlatım; 3 yaşındaki çocuğa uygun değil.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri işi biraz abarttı"
   - Cümle 6: «Hayri işi biraz abarttı ve çukurdan denize kadar uzun bir yol kazdı.»
   - Açıklama: Kartın özelliği olayları abartmaktır; burada abartma işi fazla yapmak anlamında kullanılıyor ve karttaki özelliğe uymuyor.
   - Açıklama: Karttaki özellik olayları abartmayı sevmektir; burada özellik işi fazla yapmak anlamında, karttan farklı kullanılıyor.
4. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri işi biraz abarttı"
   - Cümle 6: «Hayri işi biraz abarttı ve çukurdan denize kadar uzun bir yol kazdı.»
   - Açıklama: Denize yol kazmak abartı değil gereken çözüm; abartma ayrıntısı işlevsiz ve yersiz.
5. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "Hayri işi biraz abarttı"
   - Cümle 6: «Hayri işi biraz abarttı ve çukurdan denize kadar uzun bir yol kazdı.»
   - Açıklama: Kazdığı yol tam gereken çözüm olduğu halde işi abarttığı söyleniyor; anlatım kendi içinde çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0048` birebir aynı, ardından `@onarim: 96009e3bda8c247dd04de8f7c9eb679c251233f4`, sonra gövde.

### Hikâye 4: tohum hayri-0050 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0050
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'paspas', fiil 'konmak', sıfat 'yeterli'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: rüzgar örtünün kenarlarını hep havaya kaldırdı | yardım istedi ve köşelere taş ve kutu koydu
@tohum: hayri-0050
@degisim: paspas -> örtü
Rüzgar ormanda hızlı hızlı esiyordu. Hayri dükkandan getirdiği ağır baklava kutusu için yere örtü yaydı. Ama rüzgar örtünün kenarlarını hep havaya kaldırdı. Hayri örtüyü tek başına tutamadı. "Basri Amca, bana yardım eder misin?" diye sordu Hayri. "Tabii, hemen geliyorum," dedi Basri Amca. Basri Amca iki köşeyi sıkıca tuttu. Hayri de ağaçların dibinden üç büyük taş getirdi. Taşları üç köşeye koydu. Sonra kutu da dördüncü köşeye kondu. "Bu taşlar ve kutu yeterli, Hayri," dedi amca. Basri Amca bir dilim baklava yedi ve gülümsedi. Hayri çok sevindi, çünkü örtü artık yerinde duruyordu.
```

**Hakem bulguları (1):**

1. **M5** (M merceği) — Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
   - Alıntı: "Sonra kutu da dördüncü köşeye kondu"
   - Cümle 10: «Sonra kutu da dördüncü köşeye kondu.»
   - Açıklama: Çözüm yardım isteme, taş getirme ve kutu koyma gibi ikiden fazla adıma yayılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0050` birebir aynı, `@degisim: paspas -> örtü` (tutuyorsan), ardından `@onarim: 7237e9ca6bca09530ca83b26b443f2869a396f94`, sonra gövde.

### Hikâye 5: tohum hayri-0051 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0051
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'yağmurluk', fiil 'yetişmek', sıfat 'patlak'
- diyalog: yok (hikâyede replik yok)
- açılış: bir zaman ifadesiyle başlar ('Bir sabah ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: kırık kovadan kozalaklar yere düştü | yağmurluğunu katlayıp kovanın dibine koydu
@tohum: hayri-0051
@degisim: patlak -> kırık
Bir sabah Hayri kamp yerinde kozalakları bir kovaya atıp oynuyordu. Çok acıkmıştı ama kahvaltıdan önce kovayı doldurmak istiyordu. Ama kova kırıktı ve kozalaklar alttaki delikten yere düştü. Bir kozalak otların arasına yuvarlandı. Hayri birkaç adımda ona yetişti. Sonra deliğe baktı ve biraz düşündü. Sarı yağmurluğunu çıkardı, katladı ve kovanın dibine koydu. Artık delik kapanmıştı. Hayri kozalağı yine kovaya attı. Bu kez kozalak yere düşmedi. Hayri hızlı hızlı attı ve kova çabucak doldu. Sonra dolu kovanın yanına oturdu ve kahvaltısını mutlu mutlu yaptı.
```

**Hakem bulguları (3):**

1. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Çok acıkmıştı ama kahvaltıdan"
   - Cümle 2: «Çok acıkmıştı ama kahvaltıdan önce kovayı doldurmak istiyordu.»
   - Açıklama: Tohumdaki acıkma özelliği yalnız süs olarak geçiyor ve sorunun çözümünde işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Çok acıkmıştı ama kahvaltıdan önce"
   - Cümle 2: «Çok acıkmıştı ama kahvaltıdan önce kovayı doldurmak istiyordu.»
   - Açıklama: Açlık ayrıntısı olayı hiç etkilemiyor ve sondaki kahvaltı sebepsizce beliriyor.
3. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "Ama kova kırıktı ve"
   - Cümle 3: «Ama kova kırıktı ve kozalaklar alttaki delikten yere düştü.»
   - Açıklama: Bir önceki cümledeki 'ama' hemen ardından yeniden 'Ama' ile tekrarlanıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0051` birebir aynı, `@degisim: patlak -> kırık` (tutuyorsan), ardından `@onarim: e062049a88fe1de28500eb5257a80890ae8ab317`, sonra gövde.

### Hikâye 6: tohum hayri-0054 (deneme 5 -> 6)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | -
@tohum: hayri-0054
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: bir şey yapmak
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'bez', fiil 'yarışmak', sıfat 'cesur'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | deniz | -
@plan: teknenin yelkeni yoktu ve tekne suda gitmedi | bezle çubuktan büyük bir yelken yaptı
@tohum: hayri-0054
@degisim: cesur -> büyük
Rüzgar deniz kıyısında hafif hafif esiyordu. Hayri tahta teknesini bezden çıkarıp kumdaki küçük su çukuruna koydu. Ama teknenin yelkeni yoktu ve tekne suda hiç gitmedi. Hayri teknesine baktı ve biraz düşündü. Sonra kumda uzun bir çubuk buldu. Hayri işi abarttı ve bezin hepsini açıp çubuğa bağladı. Çubuğu teknedeki bir deliğe taktı. Büyük yelken rüzgarla şişti ve tekne hızla ilerledi. Hayri çukurun kenarında koşarak tekneyle yarıştı. Hayri çok mutluydu, çünkü teknesi sonunda suda gidiyordu.
```

**Hakem bulguları (2):**

1. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri işi abarttı"
   - Cümle 6: «Hayri işi abarttı ve bezin hepsini açıp çubuğa bağladı.»
   - Açıklama: 'İşi abartmak' soyut bir deyim; 3 yaşındaki çocuğa uygun değil.
   - Açıklama: 'İşi abartmak' deyimsel ve soyut bir anlatım, küçük çocuk anlamaz.
2. **M7** (M merceği) — Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
   - Alıntı: "çukurun kenarında koşarak tekneyle yarıştı"
   - Cümle 9: «Hayri çukurun kenarında koşarak tekneyle yarıştı.»
   - Açıklama: Tekne küçük bir su çukurunda olduğu halde Hayri'nin kenarında koşarak onunla yarışması ve teknenin hafif rüzgarda hızla ilerlemesi çelişiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0054` birebir aynı, `@degisim: cesur -> büyük` (tutuyorsan), ardından `@onarim: 15c40ffe9992d89b52ff646e2c261b84625cbb31`, sonra gövde.

### Hikâye 7: tohum hayri-0057 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | Akın
@tohum: hayri-0057
- yer: park (Mahallenin çocuk parkı.)
- tema: özür dilemek (figürün kendi hatası yalnız bu temada olur)
- yan: Akın
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'çim', fiil 'gizlenmek', sıfat 'yuvarlak'
- diyalog: var
- açılış: figürün adıyla başlar ('Tosbi ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | park | Akın
@plan: saklambaçta sayarken gizlice gözlerini açtı | özür diledi ve gözlerini kapayıp yeniden saydı
@tohum: hayri-0057
Hayri ile Akın parkta saklambaç oynuyordu. Hayri sayarken Akın'ın nereye saklanacağını çok merak etti. Bu yüzden gizlice gözlerini açtı. Akın bunu gördü ve çok üzüldü. "Hayri, sen bana baktın, bu olmaz!" dedi Akın. Hayri yanlış yaptığını anladı. "Haklısın, Akın, özür dilerim," dedi Hayri. Akın bunu duyunca gülümsedi. Hayri baklava dükkanında tepsileri hep yavaş yavaş sayıyordu. Bu kez gözlerini sıkıca kapadı ve ona kadar öyle saydı. Akın çimlerin üstünden koştu ve yuvarlak bir çalının arkasına gizlendi. Hayri parkı dolaştı ve sonunda Akın'ı buldu. İkisi birlikte güldü. "Çok güzel oynadık, Hayri, bir daha oynayalım!" dedi Akın.
```

**Hakem bulguları (3):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri baklava dükkanında tepsileri hep yavaş yavaş sayıyordu"
   - Cümle 9: «Hayri baklava dükkanında tepsileri hep yavaş yavaş sayıyordu.»
   - Açıklama: Baklava dükkanı ayrıntısı parktaki olaydan çıkmıyor ve hikayede hiçbir işe yaramıyor.
2. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "Hayri baklava dükkanında tepsileri"
   - Cümle 9: «Hayri baklava dükkanında tepsileri hep yavaş yavaş sayıyordu.»
   - Açıklama: Baklava dükkanında tepsi sayma ayrıntısı olaya bağlanmıyor ve işlevsiz.
3. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "ona kadar öyle saydı"
   - Cümle 10: «Bu kez gözlerini sıkıca kapadı ve ona kadar öyle saydı.»
   - Açıklama: 'Öyle' ilgisiz baklava cümlesine bağlanıyor ve neyi gösterdiği belli değil.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0057` birebir aynı, ardından `@onarim: a0259f8be5603c424db65e6f104c584d0bb7a4d7`, sonra gövde.

### Hikâye 8: tohum hayri-0061 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | park | -
@tohum: hayri-0061
- yer: park (Mahallenin çocuk parkı.)
- tema: yeni bir şeyi denemek
- yan: -
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'atkı', fiil 'yaymak', sıfat 'dolu'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: duygu (figürün ya da karakterlerin olaya bağlı hissi; 'çünkü' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | park | -
@plan: uçurtmanın kuyruğu yoktu ve uçurtma dönüp düşüyordu | atkısını uçurtmaya uzun bir kuyruk olarak bağladı
@tohum: hayri-0061
Rüzgar esiyordu ve gökyüzü beyaz bulutlarla doluydu. Hayri parkta ilk kez uçurtma uçurmayı deniyordu. Ama uçurtmanın kuyruğu yoktu ve uçurtma havada dönüp düşüyordu. Hayri uçurtmayı çimlere yaydı ve dikkatle baktı. Sonra boynundaki uzun kırmızı atkıyı çıkardı. Hayri abartarak bütün atkıyı uçurtmanın alt ucuna sıkıca bağladı. Hayri ipi tuttu ve rüzgara karşı koştu. Bu kez uçurtma hiç dönmedi. Kırmızı kuyruğuyla yavaş yavaş yükseldi. Hayri çok sevindi, çünkü ilk uçurtmasını kendisi uçurmuştu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "Hayri abartarak bütün atkıyı"
   - Cümle 6: «Hayri abartarak bütün atkıyı uçurtmanın alt ucuna sıkıca bağladı.»
   - Açıklama: 'Abartarak' atkıyı bağlama eylemine anlamca uymuyor.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "Hayri abartarak bütün atkıyı"
   - Cümle 6: «Hayri abartarak bütün atkıyı uçurtmanın alt ucuna sıkıca bağladı.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmediği soyut bir kelime.
   - Açıklama: 'Abartmak' soyut bir kavram; 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "Hayri abartarak bütün atkıyı"
   - Cümle 6: «Hayri abartarak bütün atkıyı uçurtmanın alt ucuna sıkıca bağladı.»
   - Açıklama: Karttaki özellik olayları abartmak (anlatımda büyütmek) iken burada abartma fiziksel bir işi fazla yapmak olarak kullanılıyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0061` birebir aynı, ardından `@onarim: 69de69343d57f97f329be01735389c6952cce018`, sonra gövde.

### Hikâye 9: tohum hayri-0065 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Basri Amca
@tohum: hayri-0065
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: ilginç bir şeyi sahne içinde beklemek (fırındaki kek, açılacak bir çiçek; yalnız yağmurun dinmesi değil)
- yan: Basri Amca
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'patik', fiil 'açılmak', sıfat 'turuncu'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: replik (son cümle sıcak bir konuşmadır: kapanış, teşekkür ya da sevinç; ardından cümle yok)
```

**Özgün blok:**

```
### Hayri | orman | Basri Amca
@plan: amca beklemekten sıkıldı ve gitmek istedi | baklava paylaştı ve amcayla birlikte bekledi
@tohum: hayri-0065
@degisim: patik -> çiçek
Ormandaki kamp yerinde turuncu bir çiçek açılmak üzereydi. Hayri ile Basri Amca, bir kutu baklavayla çiçeği bekliyordu. Ama Basri Amca beklemekten sıkıldı ve ayağa kalktı. "Çok uzun sürdü, ben gidiyorum," dedi Basri Amca. Hayri, çiçeği amcayla birlikte görmek istiyordu. Hayri, çalıştığı dükkandan getirdiği kutuyu açtı ve amcaya uzattı. "Beklerken birer baklava yiyelim mi, Basri Amca?" diye sordu Hayri. Amca gülümsedi ve yeniden oturdu. İkisi baklavalarını yerken çiçeğe baktı. Az sonra turuncu çiçek bütün yapraklarıyla açıldı. "Çok güzel, Hayri, iyi ki gitmemişim!" dedi Basri Amca.
```

**Hakem bulguları (1):**

1. **D8** (D merceği) — Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
   - Alıntı: "Hayri ile Basri Amca, bir kutu"
   - Cümle 2: «Hayri ile Basri Amca, bir kutu baklavayla çiçeği bekliyordu.»
   - Açıklama: Özne ile tümleç arasına gereksiz virgül konmuş.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0065` birebir aynı, `@degisim: patik -> çiçek` (tutuyorsan), ardından `@onarim: 886160ef763b4974300b825e5f0fc187c981b0df`, sonra gövde.

### Hikâye 10: tohum hayri-0066 (deneme 4 -> 5)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | Yumak
@tohum: hayri-0066
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: yardım istemek (çözüm, figürün yardım istemesidir)
- yan: Yumak
- özellik: baklava (Mahalledeki baklava dükkanında çalışır.)
- kelimeler: isim 'zil', fiil 'ödemek', sıfat 'sıcacık'
- diyalog: var
- açılış: yerle başlar ('Ormanda ...')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | orman | Yumak
@plan: köpek baklava kutusunu ağaçların arasına götürdü | köpekten yardım istedi ve kutuyu geri aldı
@tohum: hayri-0066
@degisim: ödemek -> koklamak
Ormandaki kamp yerinde Hayri küçük bir zil çalıyor, Yumak da sese koşuyordu. Hayri'nin getirdiği sıcacık baklava kutusu bir kütüğün üstündeydi. Ama Yumak kutuyu ağzına aldı, ağaçların arasına koştu ve kutusuz döndü. Hayri her yere baktı ama kutuyu bulamadı. Hayri baklava dükkanında çalıştığı için elleri tatlı kokuyordu. Hayri ellerini Yumak'a uzattı. "Yumak, kutuyu bulmama yardım eder misin?" diye sordu Hayri. Yumak ellerini kokladı. Sonra ağaçların arasına koştu ve kutuyu ağzında geri getirdi. Hayri kutuyu açtı ve baklavaların hepsinin yerinde olduğunu gördü. Sonra Hayri ile Yumak zil oyununa mutlu mutlu devam etti.
```

**Hakem bulguları (2):**

1. **M6** (M merceği) — Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok. Yeri kuran tek kısa betim ('Kumsal sıcaktı.') ayrıntı sayılmaz; ama bir nesne ya da olay işe yarayacakmış gibi kurulup kullanılmıyorsa ya da çözümü sebepsizce getiriyorsa M6'dır.
   - Alıntı: "elleri tatlı kokuyordu"
   - Cümle 5: «Hayri baklava dükkanında çalıştığı için elleri tatlı kokuyordu.»
   - Açıklama: Kutuyu Yumak kendisi götürdüğü için ellerin koklatılması işlevsiz ve çözümü sebepsizce getiriyor.
2. **D9** (D merceği) — Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.
   - Alıntı: "Yumak ellerini kokladı."
   - Cümle 8: «Yumak ellerini kokladı.»
   - Açıklama: 'Ellerini' kimin ellerini gösterdiği belli değil; Hayri'nin elleri olduğu yazılmalı.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0066` birebir aynı, `@degisim: ödemek -> koklamak` (tutuyorsan), ardından `@onarim: c3fb0fa54a81a63f360532a40ffabb6269db77a8`, sonra gövde.

### Hikâye 11: tohum hayri-0072 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | deniz | Akın
@tohum: hayri-0072
- yer: deniz (Mahallenin yakınındaki deniz kıyısı.)
- tema: eğlenceli ya da komik bir oyun ve oyunda küçük bir aksilik
- yan: Akın
- özellik: abart (Olayları abartmayı sever.)
- kelimeler: isim 'kamyonet', fiil 'ayırmak', sıfat 'özel'
- diyalog: var
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: sonuc (ardından mutlulukla ne yaptıkları ya da olayın sonucu ('oyunlarına mutlu mutlu devam ettiler'))
```

**Özgün blok:**

```
### Hayri | deniz | Akın
@plan: dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı | kumu elleriyle iki yana ayırıp kamyoneti çekti
@tohum: hayri-0072
Dalgalar kıyıya yavaşça vuruyordu. Hayri ile Akın, oyuncak kamyoneti kumla doldurup bir tepe yapıyordu. Birden büyük bir dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı. "Kamyonet denizin dibine gidiyor!" diye abarttı Hayri. Akın güldü. "Hayır, yalnız tekerlekleri battı," dedi Akın. Hayri tekerleklerin önündeki kumu elleriyle iki yana ayırdı. Sonra kamyoneti yavaşça çekti ve kumdan çıkardı. "Teşekkürler, Hayri, bu kamyonet benim için çok özel!" dedi Akın. İki arkadaş kamyoneti dalgalardan uzağa, kuru kuma götürdü. Orada tepeyi büyütmeye mutlu mutlu devam ettiler.
```

**Hakem bulguları (3):**

1. **C3** (K merceği) — Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
   - Alıntı: "Birden büyük bir dalga geldi"
   - Cümle 3: «Birden büyük bir dalga geldi ve kamyonetin tekerlekleri ıslak kuma battı.»
   - Açıklama: Çocuklar büyük dalganın ulaştığı su kenarında oynuyor; taklit edilince tehlikeli olabilir.
2. **D6** (D merceği) — Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz. Figürün karttaki özellik kelimesi (sabırlı/sabırla, bilge, yardımsever, cesur…) tohumun istediği kelimedir; D6 sayılmaz. Mecazlı ya da yanlış kullanımı yine D2/D6'dır.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 4: «"Kamyonet denizin dibine gidiyor!" diye abarttı Hayri.»
   - Açıklama: 'Abartmak' 3 yaşındaki çocuğun bilmeyebileceği soyut bir kelime.
   - Açıklama: 'Abartmak' soyut bir kelime, 3 yaşındaki çocuk bilmez.
3. **K2** (K merceği) — Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
   - Alıntı: "diye abarttı Hayri"
   - Cümle 4: «"Kamyonet denizin dibine gidiyor!" diye abarttı Hayri.»
   - Açıklama: Tohumdaki abartma özelliği yalnız bir replikte geçiyor, sorunun çözümüne hiç katkı vermiyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0072` birebir aynı, ardından `@onarim: 87c1901118daed5c926f7b825b17d5ab6e849aa6`, sonra gövde.

### Hikâye 12: tohum hayri-0073 (deneme 3 -> 4)

**Görev:** ONAR: yalnız aşağıdaki bulguların gösterdiği yerleri (ve tutarlılık için değişmesi gerekeni) düzelt; öteki cümlelere dokunma.

**Tohum:**

```
### Hayri | orman | -
@tohum: hayri-0073
- yer: orman (Şehrin dışında, ağaçların arasındaki kamp yeri.)
- tema: merak edip bulmak (bir ses, bir iz, bir kabuk; sonunda ne olduğu ortaya çıkar)
- yan: -
- özellik: acık (Yemek yemeyi çok sever; sık sık acıkır.)
- kelimeler: isim 'saat', fiil 'hoplamak', sıfat 'sisli'
- diyalog: yok (hikâyede replik yok)
- açılış: bir ses ya da havayla başlar ('Rüzgar esiyordu.', 'Bir kuş ötüyordu.')
- kapanış: ders (olaya bağlı tek ve somut bir cümle; 'bundan sonra' kullanılabilir)
```

**Özgün blok:**

```
### Hayri | orman | -
@plan: masa yamuktu ve saat kayıp sisin içinde kayboldu | sessizce durup dinledi ve saatin sesini buldu
@tohum: hayri-0073
Kamp yerinde her yer çok sisliydi. Hayri küçük saatini masanın kenarına koymuştu. Ama masa biraz yamuktu ve saat kenardan kayıp yere düştü. Sis yüzünden Hayri saati göremedi. Hayri çok acıkmıştı ve yemek zamanını saatten öğrenmek istiyordu. Bu yüzden durdu ve sessizce dinledi. Birden masanın yanındaki çalıdan tik tak sesi geldi. Hayri sevinçle hopladı ve çalıya yürüdü. Saat çalının dibinde duruyordu. Hayri saati aldı ve baktı. Yemek zamanı gelmişti. Hayri masaya oturdu ve yemeğini afiyetle yedi. Hayri bundan sonra saatini hep masanın ortasına koydu.
```

**Hakem bulguları (3):**

1. **D2** (D merceği) — Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
   - Alıntı: "saat kayıp sisin içinde kayboldu"
   - Cümle 0 (plan satırı): «masa yamuktu ve saat kayıp sisin içinde kayboldu | sessizce durup dinledi ve saatin sesini buldu»
   - Açıklama: 'Kayıp' kaymak mı kaybolmak mı belli değil ve 'kayboldu' ile yan yana anlamı bulandırıyor.
2. **D7** (D merceği) — Gereksiz tekrar yok.
   - Alıntı: "saat kayıp sisin içinde kayboldu"
   - Cümle 0 (plan satırı): «masa yamuktu ve saat kayıp sisin içinde kayboldu | sessizce durup dinledi ve saatin sesini buldu»
   - Açıklama: 'kayıp' ile 'kayboldu' art arda gelerek gereksiz ve karışık bir tekrar yaratıyor.
3. **M3** (M merceği) — Sorunun sebebi söyleniyor ve akla yatkın; sorun çocuğun önemseyeceği bir şey (önemsiz ya da saçma olay M3'tür: 'kurdele hamurun içine düştü', 'rüzgar oyun yapraklarını dağıttı, topladı, bitti').
   - Alıntı: "yemek zamanını saatten öğrenmek istiyordu"
   - Cümle 5: «Hayri çok acıkmıştı ve yemek zamanını saatten öğrenmek istiyordu.»
   - Açıklama: Aç olan Hayri'nin yemek için saate ihtiyaç duyması sorunun önemini yapay biçimde kuruyor.

**Yazacağın bloğun satırları:** başlık ve `@tohum: hayri-0073` birebir aynı, ardından `@onarim: 5e11671043742a62cfe9a3d930e31ca9ca851108`, sonra gövde.
