# Yazar görevi: Ay Dede (uyku modu), parti 30

Sen bir çocuk ninnisi ve uyku masalı yazarısın. Aşağıdaki 24 tohumun her birinden, tohumdaki türde BİR
metin yaz (12 ninni, 12 uyku masalı). Metinler 3-6 yaş çocuklara uyumadan
önce yumuşak bir sesle okunacak ve küçük bir dil modelini eğitecek.

## Kurallar

- Çıktı dosyan: `data/urun_v4/aday/gece_30.txt`. YALNIZ bu dosyaya yaz; başka dosya yaratma ya da değiştirme. Commit
  yalnız bu dosyayı içerir. Başka yazarların çıktısını, ret kayıtlarını açma.
- Kelimeler için `data/sade_sozluk_sik.txt` dosyasını oku (sık kökler; fiiller 'koş-' biçiminde).
- Her metin tam dört parçadır: başlık, @plan, @tohum, gövde (tek satır, tek paragraf; ninnide dizeler art arda,
  her dize noktayla biter). Başlık ve @tohum satırını aşağıdaki tohumdan birebir kopyala; metinler arasında bir boş
  satır bırak:

```
### Ay Dede | <yer> | <yan ya da ->
@plan: <ninni, ... | ...> ya da <masal, ... | ...>
@tohum: <tohum kimliği>
<gövde>
```

- Tohumdaki üç kelimeden (isim, fiil, sıfat) en çok birini listeden başka bir kelimeyle değiştirebilirsin; o zaman
  @tohum satırının altına `@degisim: <eski> -> <yeni>` yaz.
- Hepsini yazdıktan sonra koş: `.venv/bin/python degerlendirme/veri_hakem.py kontrol data/urun_v4/aday/gece_30.txt --ad urun_v4`
  İşaretlenen metinde EN ÇOK 1 yerel düzeltme yap ve kontrolü bir kez daha koş. Yine geçmeyen metnin bütün
  bloğunu (başlık dahil) dosyadan sil; zorlama. Geçen metne dokunma (her değişiklik bir yama sayılır).

## Yazım kılavuzu (uyku modu)

# Uyku modu yazım kılavuzu: ninni ve uyku masalı (Ay Dede)

Gece figürü Ay Dede standa konunca oyuncak ninni ve uyku masalı okur: yavaş, alçak ve yumuşak bir sesle, cümle
aralarında uzun duraklarla. Bu metinler 3-6 yaş çocuklara uyumadan önce okunacak ve küçük bir dil modelini eğitecek.
Her metin bir tohumdan yazılır. Yanında Ay Dede'nin kaynaklı kartı ve sade sözlük (data/sade_sozluk_sik.txt) vardır.
Kart kapalı dünyadır: kartta yazmayan hiçbir şey metne girmez. Tohumdaki 'tür' metnin türüdür: **ninni** ya da
**uyku masalı**.

1. **Uzunluk ve biçim.** Gövde 50-100 kelime, tek satır, tek paragraf; her cümle en çok 12 kelime. **Ninni** 8-14
   kısa dizedir. Her dize büyük harfle başlar ve nokta ile biter; dize içindeki kısa durak virgüldür ('Ninni ninni,
   yavrum ninni.'). Dizeler alt satıra geçmez, art arda yazılır: oyuncak her noktada uzun, her virgülde kısa durur.
   Ninnide tırnak ve konuşma yoktur. **Uyku masalı** çoğu 5-9 kelimelik kısa cümlelerle, -dı'lı geçmiş zamanla
   anlatılır ('uyudu', 'parlıyordu', 'kıvrılmıştı').
2. **Tek sahne, tek gece.** Metin tohumdaki yerde başlar ve biter. 'ertesi', '... gün sonra', 'günlerce', 'her sabah'
   gibi zaman atlaması yok. 'Bu gece', 'o gece' ve 'sabaha kadar' serbesttir.
3. **Sakin akış.** Ninnide olay yoktur: uyuyan dünya, Ay Dede'nin ışığı ve gecenin yumuşak sesleri sırayla anlatılır.
   Uyku masalında sorun yoktur ya da çok küçüktür (minik sincabın uykusu gelmez, battaniye kayar) ve sakin bir
   hareketle geçer (yıldız saymak, dalga sesini dinlemek, üstünü örtmek). Hızlı hareket, koşu, yarış, şaşırtıcı olay,
   bağırma ve kahkaha yok; fiiller yavaştır (sallamak, örtmek, esnemek, kıvrılmak, fısıldamak, dinlemek, parlamak).
4. **Ay Dede görünür.** 'Ay Dede' adı ilk 2 cümlede ve son 3 cümleden birinde geçer. Ay Dede gökte kalır: bakar, ışık
   verir, fısıldar, gülümser. Yere inmez, yürümez, kimseyi bir yere götürmez.
5. **Kapalı dünya.** Tekil olarak yalnız tohumdaki yanlar geçer, kartta yazan kısa adla: *uyuyan* (metnin uykuya
   dalan kahramanı) ve varsa *eşlik* (baykuş, annesi, babası ya da yıldız; uyanık kalıp eşlik eder). Öteki canlılar
   yalnız çoğul ve arka planda geçer ('Kuşlar yuvalarında uyudu.'); konuşmaz ve olaya katılmaz. Dinleyen çocuğa
   'yavrum' diye seslenilir; 'kuzum' yalnız kuzu tohumunda. Başka ad, figür ya da aile üyesi yok; anne ve baba
   yalnız tohumda varsa ve yalnız evde. Kartta olmayan eşya, yer ya da yetenek uydurulmaz.
6. **Tohum.** Tohumdaki isim, fiil ve sıfat geçer; biri listeden başka bir kelimeyle değiştirilebilir ve değişiklik
   kayda yazılır. İsim tohumdaki duyu öğesidir (görme, işitme, dokunma, koku, tat): metinde yumuşak bir ayrıntı
   olarak geçer ('yaprakların hışırtısı', 'yumuşak battaniye'). Tohumdaki Ay Dede özelliği (ışık, fısıltı ya da
   gülümseme) bir kez, sakin bir hareket olarak geçer. İsmin çekimli biçimi seyrekse ('yorgana') yalın biçim
   ('yorgan') ya da başka bir cümle kurulur.
7. **Sade ve yumuşak kelime.** Kelimeler sade sözlükten; en çok 2 liste dışı kelime. Deyim, soyut kavram ve şapkalı
   harf yok. Benzetme yalnız 'gibi' ile ve yumuşaktır ('pamuk gibi bulut'). Okunması kolay, sesi yumuşak kelimeler
   seçilir: mışıl mışıl, pırıl pırıl, usulca, yavaşça, tatlı tatlı ('mışıl mışıl' dize başında değil, sonunda:
   'Uyu yavrum, mışıl mışıl.'). Uyku masalında kısa kelimeler seçilir; uzun ekli kelimeler okunmayı zorlaştırır.
8. **Ninnide tekrar.** Ninni tekrarla ilerler. Bir nakarat dizesi ('Ninni ninni, yavrum ninni.' ya da 'Uyusun da
   büyüsün, ninni.') en çok 3 kez geçer ve 'ninni' kelimesi en az 2 kez geçer; öteki dizeler birbirinden farklıdır
   (dizelerin en az %60'ı farklı). Aynı kelime art arda en çok 2 kez yazılır ('ninni ninni' olur, 'ninni ninni ninni'
   olmaz). Her yeni dize yeni bir resim ekler: bir dizede tavşan, birinde yıldızlar, birinde rüzgar. Uyku masalında
   tekrar yoktur; aynı cümle iki kez geçmez.
9. **Son ve güvenlik.** Metin herkes uyurken biter; son 2 cümlede uyku geçer (uyumak, uyku, mışıl mışıl, rüya). Son,
   tohumdaki kapanış türüyle yazılır. Korku, karanlık, kötü rüya, canavar, öcü, kurt, kaybolmak, kaza, ağlamak,
   fırtına, hastalık, yaralanma ve tehdit ('uyumazsan ...') yok; 'karanlık' yerine 'gece' yazılır. Çocuk gece
   dışarı çıkmaz, pencereden sarkmaz; kimse suya girmez, bir yere tırmanmaz, düşmez; mum ya da ateş yok.
10. **Biçim ve öz-denetim.** Her metin dört parçadır:
    `### Ay Dede | yer | yan` / `@plan: sorun | çözüm` / `@tohum: id` / gövde.
    Başlık tohumdaki yer ve yan alanlarının birebir kopyasıdır. Plan satırının ilk kelimesi türdür: ninnide
    `ninni, <kimi uyutuyor> | <nasıl uyutuyor>` ('ninni, minik kuzuyu uyutuyor | ay ışığıyla ve rüzgarın sesiyle'),
    uyku masalında `masal, <küçük durum> | <nasıl yatıştı>` ('masal, sincabın uykusu gelmedi | yıldızları saydı ve
    uyudu'). Her yarım 3-9 küçük harfli kelimedir; özel ad yoktur ('ay dede' değil 'ay ışığı'). Yazdıktan sonra
    metin cümle cümle okunur, kusur düzeltilir, sonra `veri_hakem.py kontrol` koşulur. İşaretli metinde en çok 1
    yerel düzeltme yapılır; yine geçmezse metin boş bırakılır, zorlanmaz.

**Tohum alanları (tanım, kural değil).** *Uyuyan*: metnin uykuya dalan kahramanı; tohumda yan yoksa uyuyan dinleyen
çocuktur ('yavrum'). *Eşlik*: uyanık kalan ve uyuyana eşlik eden yan. *Duyu*: ismin hangi duyuya seslendiği.
Açılış türü (ninni): *nakarat* ('Ninni ninni, ...'), *ay_dede* ('Ay Dede gökte ...'), *hitap* ('Uyu yavrum, ...').
Açılış türü (uyku masalı): *zaman* ('Gece oldu.'), *ay_dede*, *yer* ('Ormanda ...'), *ses* ('Rüzgar usulca
esiyordu.'). Kapanış türü: *uyudu* (son cümlede uyuyan ve herkes uykuya dalar: 'Herkes mışıl mışıl uyudu.'),
*iyi_geceler* (son cümle 'iyi geceler' dileğidir), *ruya* (son cümle tatlı rüya dileğidir ya da rüyayı anlatır),
*nakarat* (yalnız ninni: son dize nakarattır ve 'ninni' geçer). Diyalog 'var' ise (yalnız uyku masalı) en çok 2
kısa, yumuşak replik vardır ve konuşan bellidir ('"İyi geceler, minik sincap," diye fısıldadı Ay Dede.'); 'yok' ise
replik yoktur.

**Örnekler** (pilotta yazıldı; ikisi de `veri_hakem.py kontrol`dan geçer):

Tohum: ninni, bahçe, uyuyan kuzu, duyu koku (çimen), özellik ışık, kelimeler çimen/sallamak/yumuşak, açılış
nakarat, kapanış nakarat.

```
### Ay Dede | bahçe | kuzu
@plan: ninni, minik kuzuyu uyutuyor | ay ışığıyla ve rüzgarın sesiyle
@tohum: gece-9001
Ninni ninni, yavrum ninni. Ay Dede gökte parlıyor. Gümüş ışığı bahçeye yayılıyor. Minik kuzu çimende yatıyor. Yumuşak çimen onu sarıyor. Rüzgar dalları yavaşça sallıyor. Çiçekler de uykuya dalıyor. Kuşlar yuvada uyuyor. Ninni ninni, yavrum ninni. Kuzu yavaşça esniyor. Ay Dede tatlı tatlı bakıyor. Uyu kuzum, mışıl mışıl uyu. Ninni ninni, yavrum ninni.
```

Tohum: uyku masalı, orman, uyuyan sincap, duyu işitme (yaprak), özellik fısıltı, kelimeler yaprak/saymak/uykulu,
tema uykusu gelmeyen, diyalog var, açılış zaman, kapanış iyi_geceler.

```
### Ay Dede | orman | sincap
@plan: masal, minik sincabın uykusu gelmedi | yaprakların sesini dinledi ve uyudu
@tohum: gece-9002
Gece oldu ve orman sessizleşti. Ay Dede ağaçların üstünde parlıyordu. Minik sincap yuvasında gözlerini açtı. Sincabın hiç uykusu gelmiyordu. "Yaprakların sesini dinle," diye fısıldadı Ay Dede. Sincap kulağını yapraklara yaklaştırdı. Rüzgar esti ve yapraklar usulca sallandı. Sincap sesleri tek tek saydı. Bir, iki, üç derken uykulu gözleri kapandı. Ay Dede gökten tatlı tatlı gülümsedi. Sincap kuyruğuna sarıldı ve uyudu. "İyi geceler, minik sincap," dedi Ay Dede.
```

## Kart: Ay Dede (kaynaklı, kapalı dünya)

- Ad: Ay Dede (okunuş: ay dede; kesme eki okunuşa uyar)
- Kimlik: Ay Dede, gökyüzünden uyuyan çocuklara ve hayvanlara tatlı tatlı bakan, yumuşak ışıklı ve sakin bir aydır.
- Tür: ay
- Güvenli özellik kullanımı: Ay Dede yalnız gökten bakar, ışık verir, fısıldar ve gülümser; yere inmez, kimseyi bir yere götürmez. Çocuk gece evden çıkmaz; yatağından ya da pencerenin içinden bakar. Kimse suya girmez, kimse yükseğe çıkmaz.
- Özellikler:
  - ışık: Gece her yere yumuşak, gümüş bir ışık verir. (örnek biçimler: ışık, ışığı, ışığıyla, aydınlattı)
  - fısılda: Uyumak isteyenlere yavaşça ninni fısıldar. (örnek biçimler: fısıldadı, fısıldıyor, fısıltıyla)
  - gülümse: Uyuyanlara gökten tatlı tatlı gülümser. (örnek biçimler: gülümsedi, gülümsüyor, gülümseyerek)
- Yerler:
  - gökyüzü: Ay Dede'nin bulunduğu gece göğü; yıldızlar ve yumuşak bulutlar vardır.
  - bahçe: Köy evinin gece bahçesi; çimenler, çiçekler ve küçük yuvalar vardır.
  - orman: Gece sessiz orman; ağaçlarda yuvalar vardır, yapraklar yavaşça sallanır.
  - ev: Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.
  - deniz: Gece deniz kıyısı; kum, sakin dalgalar ve ay ışığının sudaki yolu vardır. Herkes kumda kalır.
- Yanlar (metinde kısa adla; yalnız tohumdaki yanlar hikâyeye girer):
  - çocuk: Odasında uyumaya hazırlanan küçük çocuk; Ay Dede ona pencereden bakar. Tür: çocuk; konuşur. Yüzey biçimleri: çocuk
  - annesi: Çocuğun annesi; onu yatağına yatırır ve üstünü örter. Tür: anne; konuşur. Yüzey biçimleri: anne, annesi, Anne
  - babası: Çocuğun babası; ona iyi geceler der ve ışığı kapatır. Tür: baba; konuşur. Yüzey biçimleri: baba, babası, Baba
  - kedi: Evde ya da bahçede uyuyan küçük, tüylü bir kedi yavrusu. Tür: kedi; konuşur. Yüzey biçimleri: kedi
  - kuzu: Bahçede çimenlerin üstünde uyuyan küçük, beyaz bir kuzu. Tür: kuzu; konuşur. Yüzey biçimleri: kuzu
  - civciv: Bahçedeki yuvada uyuyan sarı, minik bir civciv. Tür: civciv; konuşur. Yüzey biçimleri: civciv
  - tavşan: Yuvasında uyuyan uzun kulaklı, küçük bir tavşan. Tür: tavşan; konuşur. Yüzey biçimleri: tavşan
  - sincap: Ağaçtaki yuvasında uyuyan küçük bir sincap. Tür: sincap; konuşur. Yüzey biçimleri: sincap
  - kirpi: Yaprakların altında uyuyan küçük bir kirpi. Tür: kirpi; konuşur. Yüzey biçimleri: kirpi
  - baykuş: Gece uyanık kalan bilge baykuş; dalından uyuyanlara bakar. Tür: baykuş; konuşur. Yüzey biçimleri: baykuş
  - martı: Kıyıdaki büyük bir taşın üstünde uyuyan küçük bir martı. Tür: martı; konuşur. Yüzey biçimleri: martı
  - kaplumbağa: Kumun üstünde uyuyan küçük bir kaplumbağa. Tür: kaplumbağa; konuşur. Yüzey biçimleri: kaplumbağa
  - yıldız: Ay Dede'nin yanında parlayan küçük bir yıldız; gece ilerleyince onun da uykusu gelir. Tür: yıldız; konuşur. Yüzey biçimleri: yıldız
  - bulut: Gökte yavaşça süzülen yumuşak, küçük bir bulut; yorulunca uyur. Tür: bulut; konuşur. Yüzey biçimleri: bulut
- Dünya kuralları:
  - Ay Dede gökte kalır; yere inmez, yürümez, koşmaz ve kimseyi bir yere götürmez.
  - Gece kimse dışarı çıkmaz ve tek başına dolaşmaz; çocuk yatağında ya da pencerenin içinde kalır.
  - Kimse suya girmez; deniz yalnız kıyıdan dinlenir.
  - Mum, ateş ve ocak yoktur; ışığı Ay Dede ve yıldızlar verir.
  - Korkutma ve tehdit yoktur: uyumayana bir şey olacağı söylenmez, kimse bir şeyle korkutulmaz.
- Yasak adlar: -
- Yasak: Başka figürler, onların arkadaşları ve adlı karakterler hikayeye girmez.
- Yasak: Korku, karanlık korkusu, canavar, kaybolmak, kaza, ağlamak, fırtına ve tehdit yoktur.
- Yasak: Çocuk gece dışarı çıkmaz; kimse suya girmez, kimse yükseğe tırmanmaz, mum ya da ateş yakılmaz.
- İzinli dünya kelimeleri: yavru

## Tohumlar

### Ay Dede | bahçe | -
@tohum: gece-0697
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: bahçe (Köy evinin gece bahçesi; çimenler, çiçekler ve küçük yuvalar vardır.)
- tema: uyusun da büyüsün: dinleyen çocuğa sevgi ve büyüme dileği
- uyuyan: yavrum (dinleyen çocuk; yan yok); eşlik: -
- duyu: işitme (isim 'rüzgar' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: gülümse (Uyuyanlara gökten tatlı tatlı gülümser.)
- kelimeler: isim 'rüzgar', fiil 'sarılmak', sıfat 'sakin'
- diyalog: yok (replik yok, tırnak yok)
- açılış: Ay Dede ile başlar ('Ay Dede gökte ...')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | ev | çocuk
@tohum: gece-0698
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: ev (Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.)
- tema: Ay Dede bütün gece uyuyanların başında bekler ve onlara ışık verir
- uyuyan: çocuk; eşlik: -
- duyu: dokunma (isim 'yorgan' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'yorgan', fiil 'dinlemek', sıfat 'mavi'
- diyalog: yok (replik yok, tırnak yok)
- açılış: nakaratla başlar ('Ninni ninni, ...')
- kapanış: nakarat (son dize nakarattır, 'ninni' geçer ('Ninni ninni, uyu yavrum.'))

### Ay Dede | ev | çocuk
@tohum: gece-0699
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: ev (Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.)
- tema: minik birinin uykusu gelmez; sakin bir şeyle (bir ses dinlemek, gökyüzüne bakmak) uykuya dalar
- uyuyan: çocuk; eşlik: -
- duyu: görme (isim 'yıldız' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: gülümse (Uyuyanlara gökten tatlı tatlı gülümser.)
- kelimeler: isim 'yıldız', fiil 'parlamak', sıfat 'yumuşacık'
- diyalog: yok (replik yok, tırnak yok)
- açılış: Ay Dede ile başlar ('Ay Dede ...')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | gökyüzü | yıldız
@tohum: gece-0700
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: gökyüzü (Ay Dede'nin bulunduğu gece göğü; yıldızlar ve yumuşak bulutlar vardır.)
- tema: yumuşak bir yatak ya da yuva hazırlamak (yaprak, ot, battaniye)
- uyuyan: yıldız; eşlik: -
- duyu: görme (isim 'bulut' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: gülümse (Uyuyanlara gökten tatlı tatlı gülümser.)
- kelimeler: isim 'bulut', fiil 'esnemek', sıfat 'tatlı'
- diyalog: yok (replik yok, tırnak yok)
- açılış: yerle başlar ('Ormanda ...', 'Odada ...')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | orman | tavşan, baykuş
@tohum: gece-0701
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: orman (Gece sessiz orman; ağaçlarda yuvalar vardır, yapraklar yavaşça sallanır.)
- tema: Ay Dede'nin fısıldadığı bir ninniyi dinleyip uyumak
- uyuyan: tavşan; eşlik: baykuş
- duyu: dokunma (isim 'tüy' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'tüy', fiil 'saymak', sıfat 'mavi'
- diyalog: yok (replik yok, tırnak yok)
- açılış: yerle başlar ('Ormanda ...', 'Odada ...')
- kapanış: iyi_geceler (son cümle 'iyi geceler' dileğidir ('İyi geceler, yavrum.'))

### Ay Dede | orman | kirpi
@tohum: gece-0702
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: orman (Gece sessiz orman; ağaçlarda yuvalar vardır, yapraklar yavaşça sallanır.)
- tema: yumuşak bir yatak ya da yuva hazırlamak (yaprak, ot, battaniye)
- uyuyan: kirpi; eşlik: -
- duyu: dokunma (isim 'yuva' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: ışık (Gece her yere yumuşak, gümüş bir ışık verir.)
- kelimeler: isim 'yuva', fiil 'saymak', sıfat 'gümüş'
- diyalog: yok (replik yok, tırnak yok)
- açılış: yerle başlar ('Ormanda ...', 'Odada ...')
- kapanış: iyi_geceler (son cümle 'iyi geceler' dileğidir ('İyi geceler, yavrum.'))

### Ay Dede | bahçe | civciv, baykuş
@tohum: gece-0703
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: bahçe (Köy evinin gece bahçesi; çimenler, çiçekler ve küçük yuvalar vardır.)
- tema: Ay Dede'nin fısıldadığı bir ninniyi dinleyip uyumak
- uyuyan: civciv; eşlik: baykuş
- duyu: koku (isim 'çimen' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: gülümse (Uyuyanlara gökten tatlı tatlı gülümser.)
- kelimeler: isim 'çimen', fiil 'kapanmak', sıfat 'yumuşacık'
- diyalog: var (en çok 2 kısa, yumuşak replik; konuşan belli)
- açılış: yumuşak bir sesle başlar ('Rüzgar usulca esiyordu.')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | bahçe | civciv
@tohum: gece-0704
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: bahçe (Köy evinin gece bahçesi; çimenler, çiçekler ve küçük yuvalar vardır.)
- tema: Ay Dede bütün gece uyuyanların başında bekler ve onlara ışık verir
- uyuyan: civciv; eşlik: -
- duyu: dokunma (isim 'tüy' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: ışık (Gece her yere yumuşak, gümüş bir ışık verir.)
- kelimeler: isim 'tüy', fiil 'örtmek', sıfat 'tüylü'
- diyalog: yok (replik yok, tırnak yok)
- açılış: nakaratla başlar ('Ninni ninni, ...')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | ev | babası, kedi
@tohum: gece-0705
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: ev (Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.)
- tema: gecenin yumuşak seslerini dinlemek ve uyumak
- uyuyan: kedi; eşlik: babası
- duyu: tat (isim 'süt' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'süt', fiil 'süzülmek', sıfat 'ılık'
- diyalog: yok (replik yok, tırnak yok)
- açılış: bir gece ifadesiyle başlar ('Gece oldu.')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | bahçe | kuzu
@tohum: gece-0706
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: bahçe (Köy evinin gece bahçesi; çimenler, çiçekler ve küçük yuvalar vardır.)
- tema: gecenin yumuşak sesleri (rüzgar, yapraklar, dalgalar) uyutur
- uyuyan: kuzu; eşlik: -
- duyu: koku (isim 'çimen' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: ışık (Gece her yere yumuşak, gümüş bir ışık verir.)
- kelimeler: isim 'çimen', fiil 'okşamak', sıfat 'gümüş'
- diyalog: yok (replik yok, tırnak yok)
- açılış: dinleyen çocuğa seslenerek başlar ('Uyu yavrum, ...')
- kapanış: iyi_geceler (son cümle 'iyi geceler' dileğidir ('İyi geceler, yavrum.'))

### Ay Dede | ev | kedi
@tohum: gece-0707
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: ev (Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.)
- tema: tatlı rüya dileği: uyuyana güzel ve sakin bir rüya dilenir
- uyuyan: kedi; eşlik: -
- duyu: dokunma (isim 'tüy' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'tüy', fiil 'örtmek', sıfat 'yumuşak'
- diyalog: yok (replik yok, tırnak yok)
- açılış: dinleyen çocuğa seslenerek başlar ('Uyu yavrum, ...')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | ev | çocuk
@tohum: gece-0708
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: ev (Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.)
- tema: uyusun da büyüsün: dinleyen çocuğa sevgi ve büyüme dileği
- uyuyan: çocuk; eşlik: -
- duyu: dokunma (isim 'battaniye' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'battaniye', fiil 'kıvrılmak', sıfat 'yumuşacık'
- diyalog: yok (replik yok, tırnak yok)
- açılış: nakaratla başlar ('Ninni ninni, ...')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | deniz | martı
@tohum: gece-0709
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: deniz (Gece deniz kıyısı; kum, sakin dalgalar ve ay ışığının sudaki yolu vardır. Herkes kumda kalır.)
- tema: gecenin yumuşak sesleri (rüzgar, yapraklar, dalgalar) uyutur
- uyuyan: martı; eşlik: -
- duyu: dokunma (isim 'kum' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: ışık (Gece her yere yumuşak, gümüş bir ışık verir.)
- kelimeler: isim 'kum', fiil 'dinlenmek', sıfat 'tatlı'
- diyalog: yok (replik yok, tırnak yok)
- açılış: nakaratla başlar ('Ninni ninni, ...')
- kapanış: nakarat (son dize nakarattır, 'ninni' geçer ('Ninni ninni, uyu yavrum.'))

### Ay Dede | ev | çocuk
@tohum: gece-0710
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: ev (Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.)
- tema: herkes uyuyor: dizeler sırayla uyuyanları anlatır, en son uyuyan da uyur
- uyuyan: çocuk; eşlik: -
- duyu: dokunma (isim 'battaniye' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: gülümse (Uyuyanlara gökten tatlı tatlı gülümser.)
- kelimeler: isim 'battaniye', fiil 'saymak', sıfat 'tatlı'
- diyalog: yok (replik yok, tırnak yok)
- açılış: dinleyen çocuğa seslenerek başlar ('Uyu yavrum, ...')
- kapanış: nakarat (son dize nakarattır, 'ninni' geçer ('Ninni ninni, uyu yavrum.'))

### Ay Dede | orman | kirpi
@tohum: gece-0711
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: orman (Gece sessiz orman; ağaçlarda yuvalar vardır, yapraklar yavaşça sallanır.)
- tema: tatlı rüya dileği: uyuyana güzel ve sakin bir rüya dilenir
- uyuyan: kirpi; eşlik: -
- duyu: görme (isim 'dal' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: ışık (Gece her yere yumuşak, gümüş bir ışık verir.)
- kelimeler: isim 'dal', fiil 'süzülmek', sıfat 'yumuşacık'
- diyalog: yok (replik yok, tırnak yok)
- açılış: Ay Dede ile başlar ('Ay Dede gökte ...')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | bahçe | civciv
@tohum: gece-0712
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: bahçe (Köy evinin gece bahçesi; çimenler, çiçekler ve küçük yuvalar vardır.)
- tema: Ay Dede'nin fısıldadığı bir ninniyi dinleyip uyumak
- uyuyan: civciv; eşlik: -
- duyu: dokunma (isim 'ot' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: gülümse (Uyuyanlara gökten tatlı tatlı gülümser.)
- kelimeler: isim 'ot', fiil 'parlamak', sıfat 'tüylü'
- diyalog: var (en çok 2 kısa, yumuşak replik; konuşan belli)
- açılış: yumuşak bir sesle başlar ('Rüzgar usulca esiyordu.')
- kapanış: iyi_geceler (son cümle 'iyi geceler' dileğidir ('İyi geceler, yavrum.'))

### Ay Dede | orman | sincap
@tohum: gece-0713
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: orman (Gece sessiz orman; ağaçlarda yuvalar vardır, yapraklar yavaşça sallanır.)
- tema: Ay Dede uyuyanlara tek tek iyi geceler der
- uyuyan: sincap; eşlik: -
- duyu: görme (isim 'bulut' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'bulut', fiil 'sallamak', sıfat 'ılık'
- diyalog: yok (replik yok, tırnak yok)
- açılış: yumuşak bir sesle başlar ('Rüzgar usulca esiyordu.')
- kapanış: uyudu (uyuyanın ve herkesin uykuya dalmasıyla biter ('Herkes mışıl mışıl uyudu.'))

### Ay Dede | bahçe | -
@tohum: gece-0714
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: bahçe (Köy evinin gece bahçesi; çimenler, çiçekler ve küçük yuvalar vardır.)
- tema: uyusun da büyüsün: dinleyen çocuğa sevgi ve büyüme dileği
- uyuyan: yavrum (dinleyen çocuk; yan yok); eşlik: -
- duyu: görme (isim 'dal' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: ışık (Gece her yere yumuşak, gümüş bir ışık verir.)
- kelimeler: isim 'dal', fiil 'örtmek', sıfat 'uykulu'
- diyalog: yok (replik yok, tırnak yok)
- açılış: Ay Dede ile başlar ('Ay Dede gökte ...')
- kapanış: ruya (son cümle tatlı rüya dileğidir ya da rüyayı anlatır ('Tatlı rüyalar gör, yavrum.'))

### Ay Dede | orman | kirpi, baykuş
@tohum: gece-0715
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: orman (Gece sessiz orman; ağaçlarda yuvalar vardır, yapraklar yavaşça sallanır.)
- tema: yıldızları birlikte yavaşça saymak; sayarken uyumak
- uyuyan: kirpi; eşlik: baykuş
- duyu: koku (isim 'çam' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'çam', fiil 'saymak', sıfat 'sessiz'
- diyalog: var (en çok 2 kısa, yumuşak replik; konuşan belli)
- açılış: yumuşak bir sesle başlar ('Rüzgar usulca esiyordu.')
- kapanış: iyi_geceler (son cümle 'iyi geceler' dileğidir ('İyi geceler, yavrum.'))

### Ay Dede | ev | çocuk
@tohum: gece-0716
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: ev (Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.)
- tema: yıldızları birlikte yavaşça saymak; sayarken uyumak
- uyuyan: çocuk; eşlik: -
- duyu: görme (isim 'parıltı' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'parıltı', fiil 'uzanmak', sıfat 'sakin'
- diyalog: var (en çok 2 kısa, yumuşak replik; konuşan belli)
- açılış: yumuşak bir sesle başlar ('Rüzgar usulca esiyordu.')
- kapanış: iyi_geceler (son cümle 'iyi geceler' dileğidir ('İyi geceler, yavrum.'))

### Ay Dede | bahçe | civciv
@tohum: gece-0717
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: bahçe (Köy evinin gece bahçesi; çimenler, çiçekler ve küçük yuvalar vardır.)
- tema: herkes uyuyor: dizeler sırayla uyuyanları anlatır, en son uyuyan da uyur
- uyuyan: civciv; eşlik: -
- duyu: koku (isim 'çimen' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'çimen', fiil 'okşamak', sıfat 'beyaz'
- diyalog: yok (replik yok, tırnak yok)
- açılış: Ay Dede ile başlar ('Ay Dede gökte ...')
- kapanış: iyi_geceler (son cümle 'iyi geceler' dileğidir ('İyi geceler, yavrum.'))

### Ay Dede | gökyüzü | bulut
@tohum: gece-0718
- tür: ninni (plan satırı 'ninni, <kimi uyutuyor> | <nasıl uyutuyor>')
- yer: gökyüzü (Ay Dede'nin bulunduğu gece göğü; yıldızlar ve yumuşak bulutlar vardır.)
- tema: herkes uyuyor: dizeler sırayla uyuyanları anlatır, en son uyuyan da uyur
- uyuyan: bulut; eşlik: -
- duyu: görme (isim 'parıltı' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: fısılda (Uyumak isteyenlere yavaşça ninni fısıldar.)
- kelimeler: isim 'parıltı', fiil 'dinlemek', sıfat 'uykulu'
- diyalog: yok (replik yok, tırnak yok)
- açılış: nakaratla başlar ('Ninni ninni, ...')
- kapanış: nakarat (son dize nakarattır, 'ninni' geçer ('Ninni ninni, uyu yavrum.'))

### Ay Dede | ev | çocuk
@tohum: gece-0719
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: ev (Çocuğun odası; yumuşak bir yatak, yastık, battaniye ve pencere vardır. Ay ışığı pencereden içeri girer.)
- tema: Ay Dede uyuyanlara tek tek iyi geceler der
- uyuyan: çocuk; eşlik: -
- duyu: dokunma (isim 'yorgan' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: gülümse (Uyuyanlara gökten tatlı tatlı gülümser.)
- kelimeler: isim 'yorgan', fiil 'sarılmak', sıfat 'yumuşacık'
- diyalog: yok (replik yok, tırnak yok)
- açılış: Ay Dede ile başlar ('Ay Dede ...')
- kapanış: ruya (son cümle tatlı rüya dileğidir ya da rüyayı anlatır ('Tatlı rüyalar gör, yavrum.'))

### Ay Dede | orman | tavşan
@tohum: gece-0720
- tür: uyku masalı (plan satırı 'masal, <küçük durum> | <nasıl yatıştı>')
- yer: orman (Gece sessiz orman; ağaçlarda yuvalar vardır, yapraklar yavaşça sallanır.)
- tema: Ay Dede uyuyanlara tek tek iyi geceler der
- uyuyan: tavşan; eşlik: -
- duyu: işitme (isim 'yaprak' metinde yumuşak bir ayrıntı olarak geçer)
- özellik: ışık (Gece her yere yumuşak, gümüş bir ışık verir.)
- kelimeler: isim 'yaprak', fiil 'okşamak', sıfat 'sessiz'
- diyalog: var (en çok 2 kısa, yumuşak replik; konuşan belli)
- açılış: yumuşak bir sesle başlar ('Rüzgar usulca esiyordu.')
- kapanış: iyi_geceler (son cümle 'iyi geceler' dileğidir ('İyi geceler, yavrum.'))
