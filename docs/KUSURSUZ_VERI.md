# Kusursuz veri hattı — son tasarım

## Kusursuz tanımı

KAPSAM (kullanıcıya açıkça söylenir): 'Kusursuz' şartı ince ayara giren bütün OYUNCAK hikâyeleri içindir: data/urun_v1'de yalnız izin listesindeki kayıtlar. İki sınırı var.
(a) İnce ayar akışının ~%73'ü genel TinyStories dilimidir (logs/c3ft_tek.log: 8 000 000 genel / 10 943 174 toplam token). Ön eğitim de TinyStories'in tamamıyla yapıldı. Bu metinler dili öğretmek için gerekli; milyonlarca hikâye olduğu için hakemden geçirilemez ve kusursuz değildir. Aşama 1'de genel dilimi yalnız kodla süzülmüş (K7, K8, Zemberek) ayrı bir kol ölçülür.
(b) Verinin kusursuz olması 5,7 M'lik modelin kusursuz yazacağı anlamına gelmez. Gerçekçi hedef rubrikte 5,5–6,5.

HİKÂYE DÜZEYİ: Bir hikâye ancak beş koşulun HEPSİNİ sağlarsa eğitime girer. Biri eksikse hikâye dışarıda kalır ve düzeltilmez.

(1) KOD: O anki sürümle K1–K9 ve K11'de sıfır ihlal. K10 (model kaybı) yalnız rapordur. K12 dağılım kotasıdır.

(2) KURUL: Üç mercek var:
- M mantık, 2 hakem
- D dil, 2 hakem
- K dünya-kart ve çocuk güvenliği, 1 hakem (pilot gerektirirse 2)
Her mercekteki HER hakem bütün maddelere 'yok' demeli.
Veto tek yönlüdür. Metinde doğrulanmış alıntılı tek bir 'var' hikâyeyi kalıcı olarak düşürür. Bu, 'var'ın geldiği parti geçerli de geçersiz de olsa, hikâye hedef, kanarya tabanı ya da dolgu da olsa böyledir. Geçersiz parti yalnız 'yok' oylarını boşa çıkarır; bir 'var' hiçbir zaman yeni bir hakemle silinmez. Alıntısı metinde bulunamayan 'var' de hikâyeyi düşürür.

(3) METİN BAĞI:
- Kimlik, normalleştirilmiş kanonik kaydın sha1'idir: {figür, yer, yan, sorun, çözüm, gövde}.
- Hakemlerin gördüğü alanlar, eğitime giren alanlardır.
- Eğitim dizgisini yalnız tek bir serileştirme fonksiyonu üretir (degerlendirme/urun_kayit.py); kapi.py ve prepare_ft2 bunu import eder. Planlı/plansız ve Yan alanlı/alansız biçimler aynı kaydın deterministik alt kümeleridir.
- Hakemden sonra tek harf değişmez ve LLM düzeltmesi yapılmaz.
- Hakemden önce yazar, kod geri bildirimiyle en çok 1 yerel yama yapabilir. Yamalı hikâye 'yamali' bayrağı ve farkıyla kayda geçer.

(4) KALİBRE KURUL: Kullanıcı altın seti kurul kararlarından ÖNCE, kör olarak etiketler. Set, koddan geçmiş yeni yazımlardan tabakalı olarak seçilen ≥150 hikâyedir; içinde ≥60 doğal kusurlu ve ≥60 temiz bulunur. Kurul bu sette şunları sağlamadan tam ölçeğe geçilmez:
- Birleşik yakalamanın %95 tek yönlü alt güven sınırı ≥%90. Bu, 60 doğal kusurludan en çok 1 kaçırma demektir.
- Beklenen kabul kusur oranı q̂ ≤ %1. Formül: q̂ = p·m / (p·m + (1−p)·(1−f)); burada p hakeme ulaşan hikâyelerde kusur yaygınlığı, m kaçırma oranı, f yanlış ret oranıdır. p≈%50 iken bu şart pratikte 60 doğal kusurludan 0 kaçırma ister. Yazar iyileşip p düştükçe tolerans açılır.
- Yanlış ret ≤%25.
- Her mercek kendi kanarya türlerinde (yalnız koddan geçen kusurlar) ≥%90 yakalar.
İstem her değiştiğinde ölçüm, istemin geliştirilmediği yarıda ve yeni etiketlerde yenilenir.

(5) SÜRÜM: Kabul kaydı bütün bileşenlerin içerik sha256'sını taşır: kapi.py ve import ettiği modüller, sec.py, bütün liste ve JSON dosyaları (beyaz liste, canli_rol, izinli ve tohum kelimeleri), kart, sade sözlük, Zemberek ve tokenizer sürümü, HAKEM_*.md. Git hash'i yetmez, çünkü commit edilmemiş değişikliği göstermez. Bir bileşen değişirse ilgili katman bütün kabullere yeniden koşulur.

VERİ KÜMESİ DÜZEYİ:
- Bütün düzeltmeler bitince veri sürümü dondurulur.
- Önceden kaydedilmiş TEK bir örneklem okunur: figür × yer tabakalı, figür başına 22, toplam 308 hikâye.
- Kullanıcının onayıyla örnekleme ~25 okur kanaryası (bilinen kusurlu hikâye) karıştırılır; hangileri olduğu söylenmez.
- Rapor biçimi: 'sürüm, n okuma, k kusur, Clopper-Pearson %95 üst sınırı, okurun kanarya yakalama oranı ve bununla düzeltilmiş üst sınır'.
- k=0 ise üst sınır 3/308 ≈ %0,97; okur duyarlılığı ≥%90 ile düzeltilince ≈ %1,1.
- Tek bir kusur bulunursa: kök nedeni koda, kanarya türüne ya da hakem maddesine çevrilir; katman bütün kabullere koşulur; YENİ sürüm dondurulur; örneklem baştan alınır (yeni 308).
- Önceki bütün örneklemler de raporda kalır (sürüm başına toplam okuma ve toplam kusur). Yalnız son temiz örneklem gösterilmez; isteğe bağlı durdurma yoktur.
- 'Sıfır hata' iddia edilmez; mutlak sıfır hiçbir yöntemle kanıtlanamaz.

## Hat

### 0. Hazırlık (aşamalı; önce yalnız pilotun gerektirdiği araçlar)

**Kim:** Kod (Claude oturumu yazar); kullanıcı tohum kelimeleri ile canlı/rol listesine göz atar

PİLOTTAN ÖNCE:
(a) `nice -n 19 .venv/bin/python degerlendirme/sade_sozluk.py olustur --nadir 20 --cok-nadir 5 --az-token 200 --sik 3000 --kok ek` çıktı olarak data/sade_sozluk.json (sha256'lı) ve data/sade_sozluk_sik.txt (3000 kök; kullanıcı kararı 1) üretir.
(b) data/canli_rol.json: sözlükteki 3000 kökten canlı ya da rol olanlar bir kez elle etiketlenir (keçi, kuzu, porsuk, martı, serçe, anne, dede, hala, abla…). K4'ün kapalı dünyası bu listeye dayanır; sec.HAYVAN'da 'keçi' bile yok.
(c) data/tohum_kelimeleri.json: somut ~600 isim, ~400 fiil, ~200 sıfat. Soyut, korkutucu, CANLI ve ROL isimleri çıkarılır. (b) ve (c) elle etiketlenir; etiketler degerlendirme/tohum_etiket.py'dedir (`tohum_etiket.py --yaz` iki JSON'u yazar).
(d) Zemberek kurulur (zemberek-python, setuptools<70; olmazsa Java jar). Figür ve yan adları özel ad olarak eklenir.
(e) degerlendirme/urun_kayit.py yazılır. İçinde kanonik kayıt, kelime listesine bağlı normalizasyon, sha1 ve TEK serileştirme fonksiyonu bulunur.
(f) degerlendirme/kapi.py yazılır: K1–K8 ve K11. kontrol.py ile sec.py kuralları buraya taşınır. sec.YABANCI'daki 'Anna' ve 'Mert' gibi ürün yanları ayıklanır. firmware/hikaye_oyuncak/secici.h'deki karşılıklar da aynı listeden üretilir.
(g) degerlendirme/bozucu.py yazılır. Her kanarya kapi.py'den geçirilir; kodun yakaladığı kanarya atılır.
(h) veri_hakem.py'ye alt komutlar eklenir: kart-kontrol, tohum, kontrol, kapi, hazirla --lens, oku, karar, altin, uyum.
(i) research/tinystories/prepare_ft2.py şöyle değişir:
- --yalniz <izin.txt> eklenir.
- --yalniz ile birlikte --plan, --haric, --bolme ya da elle --kaynak verilirse hata verir.
- Doğrulama yalnız izin listesinde 'dogrulama' işaretli kayıtlardan alınır. Satır 125'teki 'tum' listesinden seçim bu yolda kapanır.
- İzin listesindeki her sha1'i tam bir kez bulamazsa ya da listede olmayan bir oyuncak hikâyesi görürse durur.
- Model klasörüne manifest yazar: izin.txt sha256'sı, bileşen sürümleri, sayılar.
- KAYNAK varsayılanı kaldırılır; Tur 8'de v8 ve v9 bu yüzden yanlış veriyle eğitilmişti.
AŞAMA 1 SIRASINDA EKLENENLER: K9 havuzu, K12 kotaları, son, ornekle, hedefli-yeniden-hakem.
Eski hazirla/duzelt/tekrar/ozet komutları eski klasörler için kalır. HAKEM_VERI.md ve DUZELTICI.md yeni veride kullanılmaz.

**Geçme şartı:** Birim testleri:
(1) bozucu'nun biçimsel kusurlarını kod kapıları %100 yakalar: 'Tosbi'nın', 'koşdu', tırnak dışında yalın -yor/-mış, şapka, başka ürün figürü, tohumda olmayan yan, kart dışı canlı ('keçi'), 'ertesi sabah', 'hastaydı'.
(2) tr-tinystories'ten 200 rastgele hikâyede Zemberek'in özel ad dışı yanlış alarmı ≤%2; kalanlar beyaz listeye alınır. Aynı örneklemde K5 zaman kuralının ve K7 kalıplarının yanlış alarm oranı ölçülüp raporlanır. -mış/-acak sıfat-fiilleri ve 'yiyecek' gibi adlar yüklem sayılmaz; 'kuğunun kanadı' kanama sayılmaz.
(3) Sözlük sha256'sı tokenizer ile eşleşir.
(4) Aynı kayıt her zaman aynı dizgiyi verir.
(5) prepare_ft2'nin koruma testleri geçer: izin dışı hikâye, eksik sha1 ve yasak bayrak birleşimi hata verir.

### 1. Kart (kaynaklı figür dünyası)

**Kim:** Claude taslağı web kaynaklarıyla yazar. Kullanıcı onaylar ve dört yeni figürde (Keloğlan, Doru, Hayri, Şakir) kendi bilgisini ekler.

data/urun_kartlari.json'da 14 kart bulunur.
urun_figurleri.json'daki FİGÜR LİSTESİ kullanıcının kesin kararıdır. İçindeki yer ve yan bilgileri ise Claude taslağıdır ve kaynağa karşı doğrulanır.
Kaynak zorunludur: akrabalık, tür, huy, özellik ve konuşup konuşmadığı gibi her olgunun 'kaynak' alanı olur (yapımcı ya da TRT Çocuk sayfası, Vikipedi, bölüm adı ya da 'kullanıcı'). Kaynağı olmayan olgu karttan çıkar.

KART ALANLARI:
- ad ve okunuş (Chase→çeys)
- tek cümle kimlik (tür dahil)
- 2–3 özellik ve her biri için bir anahtar kök
- 'güvenli özellik kullanımı' satırı. Örümcek Adam için: ağ ve tırmanma yalnız süper güç olarak kullanılır; çocuğun taklit edebileceği ev içi tırmanma yoktur; 'tehlike' yerine 'bir sorun olduğunu haber verir' yazılır.
- yerler ve her yerin tek satırlık tarifi
- yanlar: metindeki kısa ad, yüzey biçimleri (Dedesi/dedeciğim/Dede → yan:dede), ilişki, tür, konuşup konuşmadığı
- en çok 5 dünya kuralı ve bunların yasak düzenli ifadeleri
- izinli dünya kökleri

Kart kapalı dünyadır: kartta olmayan aile, ev, yetenek ya da eşya yoktur. Slogan karta konmaz. Eski kartta 'Chase görevde! der' satırı vardı ve bu satır 21 hikâyede '...dedi Chase' olarak D5 ihlali üretti.
Kart metni kodla D kurallarına karşı denetlenir: kendine adıyla gönderme, deyim, şapka.

BU OTURUMDA WEB'DE DOĞRULANANLAR (taslağa kaynak olarak girer):
- Niloya: Murat ağabeyi. Mete, Murat'ın en yakın arkadaşı ve Niloya'yla yaşıt (niloya.com/characters/mete). Yani urun_figurleri.json doğru, eski karakterler.json:107 yanlış.
- Pepee: Bebee kız kardeşi, Şila kuzeni. Şuşu dizinin görünmeyen anlatıcısı (tr.wikipedia.org/wiki/Pepee_karakterleri_listesi). Şuşu ürün listesinde olmadığı için hikâyeye girmez; bu bir olgu hatası değil, ürün kararı.
- Kral Şakir: Remzi babası ve aslan. Kadriye annesi, Canan kız kardeşi; ikisi de beyaz kedi. Necati Remzi'nin en yakın arkadaşı, mor bir fil (king-shakir.fandom.com).
- Rafadan Tayfa: Mert ile Akın kardeş; ağabey Mert. Kamil'in ailesinin bakkalı var. Yumak Akın'ın köpeği ama Basri Amca'nın yanında kalıyor. Hale, Hayri'nin kız kardeşi. Resmî yazım 'Kamil' olduğu için şapka sorunu yok (sabah.com.tr).
- Keloğlan: Anası; Bilgecan Dede (köyün bilgesi, icat yapar); Balkız (akıllı arkadaşı); Karakaçan (sadık eşeği). Kara Vezir ve Çirkin Cadı yasak listesine girer (sabah.com.tr).
- Doru: Dorukısrak annesi, Karatay en yakın arkadaşı, Kırat sürünün en yaşlısı ve bilgesi, Gelincik küçük bir kuş (trtcocuk.net.tr/doru). 'Alaca' için kaynak bulunamadı; kaynak gelmezse çıkar.
- Maşa: resmî Türkçe yazım 'Daşa' (mashabear.com/tr-tr). Mişka konuşmaz.

KULLANICIYA ÖNERİLECEK YER DEĞİŞİKLİKLERİ (karar kullanıcının): Keloğlan'da 'şato' yerine 'padişahın sarayı' tarifi, ya da yerin çıkarılması. Doru'da 'park' yerine 'çayır' ya da 'yayla', ya da yerin çıkarılması. Yer etiketi firmware'in yer listesiyle aynı kalmalı.

**Geçme şartı:** `veri_hakem.py kart-kontrol` şu şartları doğrular: şema tam; her olgunun kaynağı var; kart, urun_figurleri.json ile değil kaynaklarla tutarlı; kart metni D denetiminden sıfır ihlalle geçiyor.
Kullanıcı 'onayli: true' işaretler ve kartın sha1'i kilitlenir. Onaysız kartla tek hikâye yazılmaz.
Kart değişirse o figürün bütün kabulleri K4 kapısından ve K merceğinden yeniden geçer.

### 2. Kayıt ve başlık biçimini sabitleme (yazımdan önce)

**Kim:** Kod; kullanıcı biçimi onaylar

Kanonik kayıt: {figür, yer, yan: [kısa ad…], sorun, çözüm, gövde}.
Eğitim dizgisi: 'Karakter: Tosbi | Yer: orman | Yan: baykuş\nSorun: <sorun>\nÇözüm: <çözüm>\n\n<gövde>'. Yan yoksa Yan alanı yazılmaz. Plan satırları %70 kopyada yer alır (mevcut --plan-orani).
Tema ve tohum kimliği eğitime girmez. E1'de başlığa tema koymak modeli kötüleştirmişti.
Cihazda model plan satırlarını kendisi yazıyor (baslangic.py plan=True); bu yüzden plan da D merceğinde hakemlenir.
Yazar dosya biçimi: '### Figür | yer | yan' / '@plan: sorun | çözüm' / '@tohum: id' / gövde.
baslangic.py, secici.h ve firmware aynı biçime geçer. Sistem yan karakteri seçiyor ama bugünkü başlık bunu modele iletmiyor; Yan alanı bu boşluğu kapatır. Yararı Aşama 1'de alanlı ve alansız iki kolla ölçülür. Alansız kol aynı kayıttan serileştirilir; yeniden hakem gerekmez.

**Geçme şartı:** Biçim yazıma başlamadan dondurulur ve serileştirme sürümü kabul kaydına girer. Biçim sonradan değişirse K1, K4 ve sha1 bütün veriye yeniden koşulur.

### 3. Tohum

**Kim:** Kod

`veri_hakem.py tohum --figur Tosbi --n 400 --tohum 2026` çıktı olarak data/urun_v1/tohum/tosbi.jsonl üretir. Her tohumda şu alanlar bulunur:
- figür
- yer: ağırlık kart sırasına göre azalır ve her yer ≥%10 alır (3 yer: %45/35/20; 4 yer: %40/30/20/10; Chase'in 5 yeri: %30/25/20/15/10)
- tema: 17 tema, tanımları kılavuzda ve tek sahneye uyarlanmış; ağırlıklı (veri_hakem.py TEMA_AGIRLIK); hiçbiri figür başına %12'yi geçmez; ahlaki çatışma temaları (paylaşmak, yardım istemek, özür dilemek, sırayla oynamak) birlikte ≤%30
- yan: 0–1 adlı + 0–1 isimsiz (%30 yansız, %40 tek yan, %30 iki yan)
- tek bir figür özelliği
- sözlükten rastgele 1 isim + 1 fiil + 1 sıfat (canlı ya da rol olmayan)
- diyalog: %60 var, %40 yok
- açılış türü: figür adı / zaman / yer / ses-hava, eşit dağılım. '<Ad> adında … yaşardı' bir açılış türü değildir.
- kapanış türü: duygu %35, sonuç %30, replik %20, ders %15 (her türde sorun çözülmüş ve son cümle sıcak bir kapanış verir)
Ders artık ayrı bir %30'luk özellik değil, bir kapanış türüdür.

**Geçme şartı:** Bütün paylar hedefin ±5 puanı içinde. Figür içinde aynı (yer, tema, isim) üçlüsü tekrarlanmaz. Bütün kelimeler tohum_kelimeleri.json'da. Yan ve özellik kaynaklı kartta var.

### 4. Yazar

**Kim:** LLM yazar ajanı; altın sette kusur yaygınlığı p en düşük çıkan model seçilir

Bir yazar ajanı tek çağrıda 12 tohum alır. Yanında kaynaklı kart, data/urun_v1/YAZIM_KILAVUZU.md (10 kural) ve sade_sozluk_sik.txt vardır.
Her hikâyeyi yazar ve dosyasına `veri_hakem.py kontrol` koşar. Kodun işaretlediği hikâyede EN ÇOK 1 yerel düzeltme turu yapabilir. Yamalı hikâye kayda 'yamali: true' ve farkıyla (diff) geçer. İkinci kontrolden de geçemeyen hikâye 'boş' bırakılır; tohum, deneme sayısı +1 ile kuyruğa döner ve sonra yeni bir bağlamda baştan yazılır.
Tohumdaki üç kelimeden en çok biri listeden başka bir kelimeyle değiştirilebilir; değişiklik kayda yazılır.
Yazar hakem gerekçesini, reddedilmiş metni ve başka yazarların çıktısını görmez.
Çıktı data/urun_v1/aday/<figür>_<parti>.txt dosyasıdır. Ajan yalnız kendi dosyasına yazar; commit'i yalnız o dosyayı içerir. 20c1e76'da stitch_1.txt'ye başka bir ajan yazmıştı.

**Geçme şartı:** Dosya ayrıştırılabilir ve her hikâye tek bir tohuma bağlı. Hikâye başına yama sayısı ≤1 ve fark kayıtlı.
Yamalı ve yamasız hikâyelerin kabul oranı ve insan kusuru ayrı raporlanır. Yamalı hikâyeler insan örnekleminde 2 kat ağırlıkla örneklenir.

### 5. Kod kapıları

**Kim:** Kod

`veri_hakem.py kapi --figur Tosbi` sırasıyla şunları yapar:
(1) Kelime listesine bağlı normalizasyon: rüzgâr→rüzgar, kâğıt→kağıt. Eşsesli üreten 'hâlâ' dönüştürülmez, K3 reddeder. “ ” „ → düz tırnak, ’ ‘ → ', çift boşluk teke iner.
(2) Kanonik kayıt ve sha1 kimlik: 'urun/<figür>#' + sha1[:10].
(3) K1–K9 ve K11 kapıları sırayla koşulur. K10 kaybı rapora yazılır.
Sonuçlar bileşen sürümleriyle birlikte data/urun_v1/aday.jsonl'e yazılır. Zemberek'in çözemediği kelimeler degerlendirme/urun_v1/bilinmeyen_kelimeler.txt'ye düşer. Kullanıcı onaylarsa kelime beyaz listeye yalnız yeni üretimler için girer; beyaz liste sürümün parçasıdır.

**Geçme şartı:** Sıfır ihlal. Tek ihlal hikâyeyi atar ve tohum Adım 9'a döner. Kanaryalar da bu kapılardan geçer; kodun yakaladığı kanarya atılır.

### 6. Altın set ve hakem kalibrasyonu (kurul kararlarından ÖNCE; her istem değişikliğinde)

**Kim:** Kullanıcı etiketler; LLM hakemler koşar; kod ölçer

KAYNAK: Pilot-1 yazımı (14 figür × 12 tohum). Koddan geçen hikâyeler figür × yer tabakalı olarak seçilir; en az 150 hikâye. Doğal kusurlu ya da temiz hikâye 60'tan azsa 14'lük ek partiler yazılır.

ETİKETLEME: Kullanıcı ya da anadili Türkçe bir okur, kurulu görmeden etiketler: 'kusursuz' ya da 'kusurlu: <cümle> <neden> <mercek>'. Listeye habersiz %8 okur kanaryası karışır; okurun duyarlılığı böyle ölçülür.

KURUL: Etiketleme bittikten sonra `veri_hakem.py altin` pilot düzeninde koşar: her mercekte 2 hakem, kısa devre yok. Uyuşmazlıklar kullanıcıya açılır. Hakem haklıysa etiket düzeltilir ve bu durum okur kaçırması olarak sayılır.

DİĞER KURALLAR:
- bozucu çıktıları ayrı raporlanır ve ortak eşiğe girmez.
- Set rastgele ikiye bölünür: 'geliştirme' ve 'ölçüm'. İstem yalnız geliştirme yarısına bakılarak düzeltilir. Yeniden ölçüm, ölçüm yarısında ve yeni etiketlenmiş 14×6 hikâyede yapılır; böylece istem sete ezberletilmez.
- Kullanıcının 3–5 gerçek eleştirisi HAKEM_<lens>.md'ye örnek olarak girer.
- Yazar ve hakem modeli burada seçilir.
- Kullanıcı yeni bir kusur türü fark ederse (ölçüt kayması) önce altın sete örnek eklenir, sonra istem güncellenir.

**Geçme şartı:** - Birleşik kurul yakalamasının %95 alt güven sınırı ≥%90 (60 doğal kusurludan en çok 1 kaçırma).
- q̂ ≤ %1 (p≈%50 iken 0 kaçırma).
- Temizlerde yanlış ret ≤%25.
- Her mercek, koddan geçen kanarya türlerinde ≥%90 yakalar.
- Uydurma alıntı ≤%3.
- Konum etkisi ≤5 puan.
- Okurun kanarya yakalaması ≥%90.
Şartlar sağlanmazsa istem düzeltilir (en çok 2 tur). Yine sağlanmazsa pilot alanındaki geri çekilme yolu uygulanır.

### 7. Hakem kurulu (M, D, K)

**Kim:** LLM hakem ajanları: tam ölçekte hikâye başına 5 karar (M 2, D 2, K 1), pilotta 6

Üç mercek:
- M mantık: 2 hakem
- D dil: 2 hakem
- K dünya-kart ve çocuk güvenliği: 1 hakem (pilotta 2). Eski C merceği K'ya katıldı.

PARTİLER: `veri_hakem.py hazirla urun_v1 --lens M --parti-boyu 10` partileri kurar.
- Parti en çok 10 hikâyedir.
- Her partiye rastgele konumda 0–2 kanarya konur (%20: 0, %50: 1, %30: 2).
- M ve D partilerinde figürler karışıktır. K partileri tek figürlüdür, yani tek kart taşır.
- Kanarya, partideki bir figürün kabul edilmiş ya da altın setteki hikâyesinden üretilir. Tabanı aynı partide olmaz.
- İki hakemli mercekte ikinci hakem farklı bir bileşimi ters sırayla okur.
- Madde sırası her hakem için karıştırılır; madde kimlikleri sabit kalır.

BAĞIMSIZLIK: Her parti yeni bir bağlamda tek bir ajana gider. Ajan yalnız HAKEM_<lens>.md'yi ve parti dosyasını okur, degerlendirme/urun_v1/hakem/<lens>/puan_<n>.json yazar.

KISA DEVRE (tam ölçekte): M (iki hakemin ikisi de okur) → D (iki hakem) → K. Bir mercekte düşen hikâye sonrakine gitmez.

KONUM: Pilotta partinin ilk ve ikinci yarısında ret ve kanarya yakalama oranları ölçülür. Fark 5 puanı aşarsa o mercekte parti boyu 5'e iner. Tam ölçekte konuma göre ret oranı sürekli izlenir.

**Geçme şartı:** Hikâye ancak her mercekteki her hakem bütün maddelere 'yok' derse geçer.

### 8. Parti doğrulama ve oy (tek yönlü veto)

**Kim:** Kod

`veri_hakem.py oku urun_v1` şunları denetler:
(a) JSON eksiksiz mi ve 'gecti' alanı maddelerle tutarlı mı.
(b) Her 'var'ın alıntısı, hikâyeye uygulanan normalizasyondan geçirilip plan ve gövdede aranır; ≤2 karakterlik düzenleme mesafesi kabul edilir. Eksiklik maddelerinde (M1, M5, M9) alıntı yerine 'cumle_no' kabul edilir.
(c) Partideki bütün kanaryalar doğru mercekte (herhangi bir maddede) yakalanmış mı.

OY KURALLARI:
- Geçerli ya da geçersiz her partideki doğrulanmış 'var' hikâyeyi düşürür.
- Alıntısı metinde bulunamayan 'var' de hikâyeyi düşürür. Bu uydurma sayılır ve raporlanır; hikâye yeni hakeme gitmez, çünkü yeniden yazım ucuz.
- Geçersiz parti yalnız 'yok' oylarını boşa çıkarır. O hikâyeler yeni bir ajana gider.
- Kanarya ya da dolgu hikâyesinin değiştirilmemiş kısmına verilen 'var' taban hikâyeyi izin listesinden çıkarır ve kök neden kaydına düşer.

KANARYA KAÇIRILIRSA: Parti yeni bir ajanla yeniden koşulur. İkinci kez de kaçırılırsa partinin hikâyeleri kuyruğa döner; hat durmaz. Bir mercekte son 50 partide kanarya kaçırma %10'u ya da uydurma alıntı %3'ü aşarsa o mercek durur ve istem sorunu olarak kullanıcıya raporlanır.

KAYIT: `veri_hakem.py karar urun_v1` iki dosya yazar:
- kabul.jsonl: sha1, tohum, deneme numarası, yamalı bayrağı, bütün kararlar, bileşen sürümleri
- ret.jsonl: mercek, madde, alıntı

**Geçme şartı:** Kabul için dört şart: her hakemin GEÇERLİ bir partiden 'yok' kararı olmalı; hiçbir partide doğrulanmış ya da uydurma 'var' olmamalı; sha1 eşleşmeli; taban veya dolgu 'var'ı olmamalı.

### 9. Ret: düzeltme yok, en çok 2 deneme

**Kim:** Kod

Reddedilen metin düzeltilmez, atılır. ret.jsonl'de altın set ve kök neden analizi için saklanır. Tohum, deneme sayısı +1 ile kuyruğa döner; yeni yazar eski metni ve gerekçeyi görmez.
EN ÇOK 2 DENEME: İki kez düşen tohum bırakılır ve aynı (yer, tema, kapanış) hücresinden yeni bir tohum üretilir. Hakemin kör noktasındaki bir tohumu defalarca denemek, kusurlu hikâyeyi sonunda kabule taşır.
DUZELTICI.md bu hatta hiç kullanılmaz.

GEREKÇE:
- Düzeltilen metin de bütün mercekleri yeniden geçmek zorunda; maliyet yeni yazımla aynı.
- Düzeltmeden sonra yeni hakem vakaların %40'ında kusur buldu. Bunların yaklaşık üçte biri (46/137) ilk hakemin kaçırdığı eski kusurdu. Bu bulgu hem düzeltmenin zararını hem tek hakemin zayıflığını gösteriyor.
- Düzeltilen hikâyeler ortalama 4 kelime uzadı. spidey_1#21'de figür özelliği silindi. Tur geçme oranı %65 → %59 → %47 düştü.
- _2 paketlerinde nadir kelime %36–77 arttı. _2 paketlerini içeren üç model tabandan %42–47'de kaldı. Ancak DENEYLER.md bunu 'ya _2 zararlı ya da v6'nın üstünlüğü kısmen şanstı' diye kaydediyor; kesin kanıt değil.

**Geçme şartı:** Eğitim verisinde hakemden sonra düzeltilip yeniden hakemlenmemiş metin sayısı 0 (onarılmış hikâye
yeni adaydır; aşağıdaki Onarım döngüsü). 1. ve 2. denemede kabul edilen hikâyelerin insan kusuru ayrı raporlanır. 2. deneme kabulleri insan örnekleminde 2 kat ağırlıkla örneklenir.

### 9a. Onarım döngüsü (hakem güdümlü; kullanıcı yetkisiyle karar)

**Kim:** Kod (istem, kapı, karar) + editör ajanı (onarım) + yeni hakemler

urun_v2'nin ilk hakem turunda 85 adaydan yalnız 2'si kabul edildi: hemen her hikâyede 1-3 somut, alıntılı ve
yerel kusur vardı (yanlış kelime, dilbilgisi, sebepsiz beliren ayrıntı, hafif mecaz). Bunlar gerçek ama
onarılabilir kusurlardır; hikâyeyi atıp tohumdan yeniden yazmak aynı türden yeni kusurlar üretiyordu. Adım 9'un
'düzeltme yok' kuralı yerine şu döngü uygulanır:

1. `veri_hakem.py onar-istemi <ad> --figur F | --hepsi [--n 12]`: figürün her tohumunun son yazılan denemesi
   kurulca reddedilmişse, bütün gerekçeleri hakem merceğinden (M, D, K) geliyorsa, K1 (figür düzeyi) ya da
   altin_kusurlu (okurun etiketi) değilse, tohumun kabulü yoksa ve sonraki deneme 3'ü aşmıyorsa editör istemi
   yazılır: `data/<ad>/onar/<figür>_<n>.md` (+ .json atama kaydı). Kod kapısından (K1-K11) ya da kanaryadan düşen
   hikâye onarılmaz; tohum Adım 9'daki gibi yeni yazıma döner.
2. İstem, yaz-istemi gibi kılavuzu (KILAVUZ_URUN.md) ve kartı, sonra her hikâye için tohumu, özgün bloğu (başlık,
   @plan, @tohum, @degisim, gövde) ve hakem bulgularını taşır: mercek, madde, maddenin HAKEM_<L>.md tanımı,
   birebir alıntı, cümle numarası ve o cümle, açıklamalar. Aynı (mercek, madde, alıntı) tek bulgudur (iki hakemin
   açıklamaları birleşir). Cümle numarası alıntı metinde aranarak bulunur (kanarya tabanı gerekçesinde
   hakemin numarası kanaryanındır).
3. Editör yalnız bulguların gösterdiği yeri ve tutarlılık için değişmesi gerekeni düzeltir; tohum (figür, yer, yan,
   tema, açılış, kapanış, diyalog, özellik, kelimeler) ve hikâye (sorun, çözüm) korunur, gövde 70-100 kelime.
   Yanlış görünen bulguda da o cümle daha basit söylenir. M3 hikâyenin çekirdeğini önemsiz ya da saçma bulduysa
   (açıklamada 'önemsiz', 'saçma', 'gerçek bir sorun değil'...) görev YENİDEN YAZ'dır: aynı tohumdan baştan.
4. Çıktı `data/<ad>/aday/<figür>_onar<n>.txt`, normal aday biçiminde, aynı @tohum ve ek satır
   `@onarim: <ebeveyn sha1>` (urun_kayit.ayristir tanır; kanonik kayda ve eğitim dizgisine girmez). Editör
   `kontrol` koşar (en çok 1 yama, Adım 4 gibi).
5. Onarılmış hikâye YENİ adaydır: `kapi` ve yeni hakem partilerinden (`hazirla`, `oku`, `karar`) her aday gibi
   geçer. Hakemler önceki bulguları ve ebeveyni görmez (parti görünümünde deneme, tohum ve @onarim yok).
6. Deneme sayımı: kapı onarımın denemesini ebeveynden alır (ebeveyn + 1). Ebeveyn aday kayıtlarında yok, başka
   tohumdan ya da ret.jsonl'de değilse K1.onarim; deneme 3'ü aşarsa K1.deneme_siniri. Aday ve kabul kaydında
   `onarim` alanı ebeveynin sha1'idir.
7. K9: aynı tohumun adayı (onarımın reddedilmiş ebeveyni dahil) ve kurulca reddedilmiş adaylar turdaki K9
   havuzuna girmez; onarım kendi ebeveyninin yakın kopyası sayılmaz, reddedilen hikâye başka tohumun
   hikâyesini engellemez. Kabul havuzu yalnız kabulleri taşır.
8. Karar: aynı tohumun önceki reddedilmiş denemesi sonraki denemenin kabulünü engellemez; bir tohumdan en çok bir
   kabul (ikincisi 'tohum_zaten_kabul' bekler). Kuyruk kaydı `onarilabilir` ve `ebeveyn` taşır. Sınır: yeni
   yazımla en çok 2 deneme (YAZIM_TAVANI; yaz-istemi 3. denemeyi vermez), onarımla en çok 3 deneme
   (DENEME_TAVANI; en çok 2 onarım turu). 3. denemede düşen ya da 2. denemede onarılamaz gerekçeyle düşen tohum
   bırakılır. yaz-istemi ve onar-istemi aynı tohumu aynı denemeye iki kez atamaz (istem/ ve onar/ kayıtları
   birlikte okunur).

GEREKÇE: Adım 9'daki kaygı, hakemin bulgusunu okuyan düzelticinin metni hakeme göre ayarlaması ve düzeltilen
metnin yeniden hakemlenmeden girmesiydi. Burada onarım yeni bir adaydır, bütün mercekleri bulguları görmeyen
yeni hakemlerle baştan geçer ve deneme sınırı kör noktada sonsuz denemeyi engeller. Onarımla kabul edilen
hikâyeler (kabul kaydında `onarim`) insan örnekleminde ayrı raporlanır.

### 10. Kabul anında kota ve dağılım izleme

**Kim:** Kod

Her kabulde figür başına yürüyen sayaçlar tutulur:
- son cümlede 'çünkü' ≤%15
- son cümle duygu fiiliyle (gülümsedi, sevindi, mutlu oldu) ≤%50 (duygu kapanışı %35 ve sonuç kapanışında 'mutlu mutlu' olağan)
- '<Ad> adında' açılışı ≤%15
- en sık açılış 4-gramı ≤%20
- 'O günden sonra' ≤%5
- en sık plan sorunu ≤%10
Bu oturumdaki ölçüm: v4'te son cümlede 'çünkü' %67–95 ve duygu kapanışı %25–93. Türkçe TinyStories'te bu oranlar %1 ve %23. Yani Claude'un gerçek kalıbı bu; eski tasarımın hedeflediği 'O günden sonra' değil.
Kotayı aşan kusursuz hikâye atılmaz, yedek havuza gider. Eğitime girmez; sonda kota izin verirse girer.
Tohum özelliği başına (yer, tema, yan sayısı, diyalog, açılış, kapanış) kabul payı tohum payıyla karşılaştırılır. 5 puandan fazla sapan hücreye fazladan tohum verilir; kapı gevşetilmez.
Her 50 kabulde Self-BLEU ve yakın kopya ret oranı raporlanır.

**Geçme şartı:** Bütün paylar eşik içinde. Bir figürde yakın kopya reddi %15'i ya da Self-BLEU artışı %10'u geçerse o figürde üretim durur ve tohum çeşitliliği artırılır.

### 11. Son kontrol ve eğitime veriş

**Kim:** Kod

`veri_hakem.py son urun_v1` şunları yapar:
- Her kabulde kanonik kaydın sha1'inin hakemlenen sha1'e eşit olduğunu doğrular.
- Bir bileşenin sürümü değiştiyse ilgili katmanı bütün kabullere yeniden koşar.
- K9 yakın kopya denetimini figürler arasında ve doğrulama bölmesine karşı yapar.
- K12 dağılımlarını denetler.
DOĞRULAMA BÖLMESİ: Figür × yer hücresi başına 1 kabul ayrılır (~50 hikâye). Bu hikâyeler de kusursuzdur ama eğitime girmez. data/bolme.json eski hikâyelerden oluştuğu için yeni veride kullanılmaz.
Çıktılar: data/urun_v1/<figür>.txt (yalnız kabuller) ve data/urun_v1/izin.txt (her satırda sha1 ve 'egitim' ya da 'dogrulama').
Eğitim yalnız `prepare_ft2.py --yalniz data/urun_v1/izin.txt` ile yapılır ve manifest model klasörüne yazılır.

**Geçme şartı:** Bütün kontroller sıfır ihlal verir ve dağılımlar eşik içindedir. prepare_ft2 izin listesindeki her sha1'i tam bir kez bulmuş ve listede olmayan hiçbir oyuncak hikâyesi görmemiştir; aksi hâlde durur. Tutmayan hikâye izin listesinden çıkar ve düzeltilmez.

### 12. İnsan denetimi ve kök neden döngüsü

**Kim:** Kullanıcı ya da anadili Türkçe bir okur; kod

(a) ALARM ÖRNEKLEMİ (Aşama 1 ve 2 sırasında): figür başına 10 rastgele kabul okunur; yamalı ve 2. deneme kabulleri 2 kat ağırlıklıdır. Bu bir geçme şartı değil, erken uyarıdır.
(b) KESİN ÖRNEKLEM (sürüm dondurulunca bir kez): `veri_hakem.py ornekle urun_v1 --n 308 --tohum <önceden kayıtlı>` figür × yer tabakalı 308 kabul seçer; ~25 okur kanaryası karışık sırayla araya girer. Çıktı degerlendirme/urun_v1/insan/kesin_<sürüm>.md dosyasıdır. Okur her hikâyeye 'kusursuz' ya da 'kusurlu: <cümle> <neden>' yazar.
(c) KÖK NEDEN: Her bulguda kusur kod ya da düzenli ifadeyle yakalanabiliyorsa kapıya eklenir ve bütün kabullere koşulur. Yakalanamıyorsa yeni bir hakem maddesi ve kanarya türü eklenir, ardından hedefli yeniden hakem uygulanır:
- Kod şüpheli alt kümeyi bulur.
- Yalnız o alt küme, tek maddelik kısa bir istemle 30'luk partiler hâlinde hakemlenir.
- Kalan kabullerden rastgele %10 da aynı istemle okunur. Bu %10'da tek bir bulgu çıkarsa madde bütün kabullere koşulur.
Ardından yeni sürüm dondurulur ve yeni bir kesin örneklem alınır.

**Geçme şartı:** Kesin örneklemde k=0 ve okurun kanarya yakalaması ≥%90 ise DENEYLER.md'ye 'sürüm X, n=308, k=0, CP %95 üst sınır %0,97, duyarlılıkla düzeltilmiş ≈%1,1' yazılır.
k>0 ise veri 'kusursuz' sayılmaz; kök neden döngüsü çalışır ve yeni sürüm için yeni örneklem alınır. Alarm örneklemleri dahil bütün örneklemler raporda kalır.

## Yazım kılavuzu özeti

- Kural 1, uzunluk: 70–100 kelime. Her cümle en çok 12 kelime, çoğu 5–9 kelime. Tek paragraf.
- Kural 2, tek sahne ve tek zaman: Hikâye tohumdaki yerde başlar ve biter. 'ertesi', '… gün/hafta sonra', 'akşama/sabaha kadar', 'bütün gün', 'o gece', 'günlerce' gibi zaman atlamaları yok. Bekleme sahnenin içinde olur.
- Kural 3, tek sorun: İlk 3 cümlede sebebiyle birlikte söylenir ('Top çalıya takıldı'). Sorunu figür kendisi 1–2 adımda çözer; yardım istemek de figürün çözümü sayılır. Yan karakter en fazla yardım eder.
- Kural 4, figür görünür ve etkin: Adı ilk 2 cümlede ve sonda geçer. Hikâye onun gözünden anlatılır.
- Kural 5, yan karakter ve kapalı dünya: Yalnız başlıktaki Yan alanında yazan karakterler bulunur; kartta yazan kısa adla ve karttaki ilişkiyle (Niloya'nın ağabeyi Murat'tır; Mete, Murat'ın arkadaşıdır). Başka ad, canlı, rol ya da aile üyesi yok. Arka plandaki çoğul canlılar ('kuşlar') konuşmaz ve olaya katılmaz. Konuşmayan karakter konuşmaz. Kartta olmayan ev, eşya ya da yetenek uydurulmaz.
- Kural 6, figür özelliği: Yalnız tohumdaki özellik kullanılır; bir kez, olayda işe yarar biçimde ve kartın 'güvenli özellik kullanımı' satırına uygun. Özellikler sıralanmaz, betimlenmez. Slogan ve kalıp replik yok.
- Kural 7, sade kelime: Kelimeler sade_sozluk_sik.txt'den seçilir; en çok 2 liste dışı kelime. Deyim, mecaz, soyut kavram ve şapkalı harf yok; 'hâlâ' yerine 'yine' ya da 'daha' kullanılır. Tohumdaki isim, fiil ve sıfat geçmeli; biri listeden başka bir kelimeyle değiştirilebilir ve değişiklik yazılır.
- Kural 8, dil: Anlatım -dı'lı geçmiş zamanda. Her replikte konuşan belli ('dedi Niloya'). Kimse kendi kendine konuşmaz ya da kendine adıyla seslenmez. Plan satırları da aynı dil ve yazım kurallarına uyar, çünkü cihazda model planı kendisi yazıyor.
- Kural 9, son: Son 1-2 cümle hikâyeyi kapatır: sorunun çözüldüğü görünür ve son cümle sıcak, doyurucu bir kapanış verir. Hikâye çıplak bir eylemle ya da durgun bir resimle bitmez. Son, tohumdaki kapanış türüyle yazılır: duygu, sonuç, replik ya da ders; 'çünkü' ile açıklama yalnız 'duygu' türünde. Son güvenli olur. Korku, yaralanma, hastalık ve taklit edilince tehlikeli davranış yok.
- Kural 10, biçim ve öz-denetim: '### Figür | yer | yan' / '@plan: sorun | çözüm' (her biri 3–9 küçük harfli kelime, özel ad yok) / '@tohum: id' / gövde. Yazdıktan sonra `veri_hakem.py kontrol` koşulur. İşaretli hikâyede en çok 1 yerel düzeltme yapılır; yine geçmezse hikâye boş bırakılır, zorlanmaz.
- Kural bütçesi (kural patlamasına karşı): Kılavuz tek sayfa ve 10 maddedir. Yeni bir kusur türü kılavuza değil koda ya da hakem listesine eklenir. Kılavuza yeni madde ancak bir madde çıkarılarak girer. Kılavuzda kullanıcının onayladığı 2 iyi örnek bulunur; farklı figürlerden ve farklı kapanış türlerinden seçilir. Kötü örnek konmaz.
- Sistem tarafı, çeşitlilik (yazara kural olarak değil, tohumla gelir; TinyStories/SimpleStories yöntemi): Her tohumda sözlükten rastgele 1 isim + 1 fiil + 1 sıfat (canlı ya da rol olmayan). Diyalog %60, diyalogsuz %40. Açılış türü: figür adı / zaman / yer / ses-hava, eşit. Kapanış türü: duygu %35, sonuç %30, replik %20, ders %15. Figür içinde aynı kelime üçlüsü tekrarlanmaz. Hikâye yapısı dayatılmaz; iskeletli üretim deneyi başarısız olmuştu.
- Sistem tarafı, yer dağılımı: Ağırlık kart sırasına göre azalır, doğa yerleri öndedir (ızgarada doğa 4,77, diğer yerler 3,87 almıştı). Her yer ≥%10 alır. 3 yer: %45/35/20. 4 yer: %40/30/20/10. 5 yer (Chase): %30/25/20/15/10. Böylece figür başına 200 hikâyede en küçük yer de ≥20 hikâye alır.
- Sistem tarafı, tema tanımları (tek sahneye ve güvenlik kurallarına uyarlandı; ağırlık parantezde): merak edip keşfetmek (%10); eğlenceli bir oyun ve küçük aksilik (%10); figür başkasına yardım eder (%8); küçük bir kutlama ya da sürpriz hazırlamak (%7); doğada bir şeyi fark etmek ve küçük bir hedef (%7); hayali oyun (%7); kaybolan eşya (%5); yeni bir şeyi denemek (%5); bir şey yapmak (%4); yağmur ya da kar günü (%3); sıkışmış, kaybolmuş ya da aç bir hayvana yardım, hasta ya da yaralı hayvan değil (%3); yeni arkadaş, ilk adımı figür atar (%2); ilginç bir şeyi sahne içinde beklemek, yalnız yağmurun dinmesi değil (%1); paylaşmak, yardım istemek, özür dilemek, sırayla oynamak (%7'şer, birlikte %28). Figürde kullanılamayan temanın payı kalanlara oranla dağılır. Hiçbiri figür başına %12'yi geçmez; ahlaki çatışma temaları birlikte ≤%30. Tema eğitim başlığına ve hakeme gitmez.

## Otomatik kontroller

- NORMALİZASYON (hakemden önce; tek deterministik değişiklik): Kelime listesine bağlıdır; yalnız eşsesli üretmeyen biçimler dönüştürülür (rüzgâr→rüzgar, kâğıt→kağıt). 'hâlâ' dönüştürülmez, K3 reddeder: 'hala' babanın kız kardeşi demektir; tr-tinystories'te 'hala' 10 749 kez, 'hâlâ' 191 kez geçiyor. Tırnaklar “ ” „ → düz tırnak; kesme işaretleri ’ ‘ → '; çift boşluk teke iner. Aynı normalizasyon hakem alıntısına da uygulanır.
- K1 Biçim ve sahne: Başlık '### <Figür> | <yer> | <yan>', ardından '@plan: sorun | çözüm' (her biri 3–9 küçük harfli kelime, özel ad yok) ve '@tohum: <id>'. Figür 14 figürden biri olmalı. Yer figürün kart yerlerinden olmalı ve tohumdaki yerle aynı olmalı. Yan tohumdaki yanla aynı olmalı. Tek paragraf, tırnaklar dengeli, son karakter . ya da ! ya da tırnak. Zaman atlaması ifadeleri (ertesi, '<sayı/bir> gün|hafta|ay sonra', 'akşama/sabaha kadar', 'bütün gün', 'o gece', 'günlerce', 'her sabah') için eşleşme 0. 10 almış eski hikâyelerden 53'ünde bu ifadeler vardı.
- K2 Uzunluk ve token: Gövde 70–100 kelime. Her cümle, tırnak içi dahil, ≤12 kelime. hf_c3ft_v6 tokenizer'ıyla gövde ≤150 token, tam eğitim dizgisi + EOT ≤200 token.
- K3 Sade sözlük: tr-tinystories'te 20 kereden az geçen kelime biçimi hikâye başına ≤2, 5 kereden az geçen ≤1. Kesmeden sonraki ek sayılmaz; adlar ve izinli dünya kökleri hariç tutulur. Adlar dışında ön eğitimde 20 kereden az görülmüş token sayısı 0. Normalizasyondan sonra şapkalı harf 0 ('hâlâ' dahil). Ateşman ≥75 ikincil kapıdır.
- K4 Kapalı dünya, ad ve tohum uyumu: Büyük harfli her ad {figür} ∪ {tohumdaki adlı yan} kümesinde olmalı. Diğer 13 ürün figürü, çıkarılan figürler, eski 12 figür ve kartın yasak adları (Kara Vezir, Çirkin Cadı, Şuşu…) ret sebebidir. Metindeki her TEKİL canlı ya da rol lemması (data/canli_rol.json) {figürün türü} ∪ {tohumdaki yanların yüzey biçimleri} kümesinde olmalı. Farklı yan kimliği sayısı tohumla aynı olmalı. ÇOĞUL canlı adları ('kuşlar') arka plan sayılır, ret değildir; K merceğine not olarak gider. Figür adı ilk 2 cümlede ve son %40'ta geçmeli. Kartın yasak düzenli ifadelerinden hiçbiri eşleşmemeli. Tohumdaki özelliğin anahtar kökü ≥1 kez geçmeli. Tohumdaki isim, fiil ve sıfat lemmaları gövdede bulunmalı; yazarın kayda geçirdiği tek değişiklik geçerlidir.
- K5 Zemberek biçimbilimi: Tırnak içi dahil her kelime çözümlenmeli ya da beyaz listede olmalı. Kesmeden sonraki ek, adın kartta yazan okunuşuna ünlü uyumu ve sertleşme bakımından uymalı (Chase'ten). Zaman kuralı: tırnak dışındaki çekimli YÜKLEMLERİN son zaman eki -dı olmalı ('yürüdü', 'yürüyordu', 'takılmıştı', 'mutluydu'); yalın -mış, -yor, -acak ve geniş zaman ret. -mış/-acak sıfat-fiilleri ve 'yiyecek' gibi adlar yüklem sayılmaz. Yanlış alarm oranı tr-tinystories örnekleminde ölçülür.
- K6 Dil işaretleri (ret değil; D hakemine 'özellikle bak' notu olarak gider): 'de/da' ve 'ki' bitişik yazılmış olabilir; Zemberek'in birden çok biçimde çözümlediği belirsiz kelimeler; çoğul arka plan canlıları. Bu işaretlerin denk geldiği kusur türleri kanarya olarak kullanılmaz.
- K7 Güvenlik ve sağlık: sec.GUVENLIK ile ek kalıplar (dizini, canı yandı, sürüklen-, akıntı, boğul-, yangın, bıçak, ilaç, 'yabancı biriyle') ve hastalık kökleri (hasta, hastalan-, üşü-, hapşır-, öksür-, ağrı, 'başım dönüyor', 'midem bulan-', 'burnu ak-') için eşleşme 0. 10 almış 16 hikâyede 'hastaydı çünkü yağmurda ıslanıp üşümüştü' kalıbı vardı. Kanama ile kanat Zemberek çözümlemesiyle ayrılır ('kanadı' = kanat+ı ret değildir). Kartın güvenli özellik satırındaki izinli ifadeler figüre özel beyaz listededir. Yanlış alarm oranı altın sette ölçülür.
- K8 Tekrar: Aynı cümle iki kez geçmez; 3-gram tekrarı ≤2. Kod ayrıca 'X ve X' kalıbını, kendine göndermeyi ('Tosbi, Tosbi'nin'), kendine adıyla seslenmeyi ('... dedi Chase' içinde 'Chase') ve aynı konuşmacının üst üste konuşmasını işaretler. Bunlar sec.cezalar ve olay_cezalari kurallarının kart adlarıyla çalışan hâlidir.
- K9 Yakın kopya: Normalleştirilmiş metinde birebir kopya olmaz; kelime 3-gram Jaccard <0,5 ve ROUGE-L <0,7. Karşılaştırma aynı figürün kabul havuzuna karşı yapılır; son kontrolde bütün figürlere ve urun_v1 doğrulama bölmesine karşı da yapılır. Saf Python yeter.
- K10 Model kaybı (RAPOR, kapı değil): c3 ön eğitim modeliyle gövdede token başına ortalama kayıp hesaplanır; ad tokenları hariç tutulur. Figür başına dağılım raporlanır. Pilotun 12'şer kabulünden p90 eşiği anlamlı değildir ve c3'ün oyuncak kaybı (5,80 / genel 2,15) başlık ve ad biçimine bağlıdır. Zorluk göstergesini (nadir kelime, r=0,66) K3 zaten kesiyor. Hesap CPU'da nice -n 19 ile yapılır.
- K11 Kimlik ve sürüm: Kimlik 'urun/<figür>#' + sha1(kanonik kayıt)[:10] biçimindedir; bütün puan ve kararlar sha1'e bağlanır. Sürüm şu bileşenlerin içerik sha256'larından oluşur: kapi.py ve import ettiği modüller, sec.py, urun_kayit.py (serileştirme dahil), canli_rol.json, izinli_kelimeler.json, tohum_kelimeleri.json, Zemberek beyaz listesi, sade_sozluk.json, kart, HAKEM_*.md, Zemberek ve tokenizer sürümü. Biri değişirse son kontrol ilgili katmanı bütün kabullere yeniden koşar; istem değişirse hedefli yeniden hakem uygulanır.
- K12 Dağılım ve kalıp kotası (kabul anında yürüyen; son kontrolde tekrar): Figür başına son cümlede 'çünkü' ≤%15; duygu fiiliyle kapanış ≤%50; '<Ad> adında' açılışı ≤%15; en sık açılış 4-gramı ≤%20; 'O günden sonra' ≤%5; en sık plan sorunu ≤%10. Yer, tema, yan sayısı, diyalog, açılış ve kapanış payları tohum hedefinin ±5 puanı içinde; her tohum özelliğinin kabul oranı raporlanır. Self-BLEU her 50 kabulde raporlanır.
- Kanarya kuralı: Kanaryalar K1–K9 ve K11'den geçmek zorundadır; kodun yakaladığı kanarya atılır, bu türler yalnız kod birim testinde kullanılır. Kanaryalar ayrı bir ad alanında tutulur ve eğitim klasörüne ya da izin listesine asla yazılamaz.
- prepare_ft2 korumaları: --yalniz ile birlikte --plan, --haric, --bolme ya da elle --kaynak verilemez. Doğrulama yalnız izin listesindeki 'dogrulama' kayıtlarından alınır. İzin listesindeki her sha1 tam bir kez bulunmalı; listede olmayan oyuncak hikâyesi bulunursa betik durur. Manifest model klasörüne yazılır. KAYNAK varsayılanı kaldırılır.
- Genel dilim süzme (yalnız Aşama 1'in B kolu): 8M'lik genel TinyStories dilimi yalnız K7 (güvenlik ve hastalık), K8 (tekrar) ve Zemberek çözümlenemeyen kelime ile süzülür. K5 zaman kuralı uygulanmaz, çünkü -mış masal anlatımı kusur değil üsluptur. LLM hakem kullanılmaz.
- İsteğe bağlı ikinci dil katmanı (pilottan sonra, D merceği kanarya kaçırırsa): GECTurk dizi etiketleyici ya da hunspell-tr. Ret yerine K6 gibi D hakemine not olarak gider. Önce altın sette yanlış alarm oranı ölçülür.

## Hakem düzeni

ÜÇ MERCEK, ÜÇ İSTEM: degerlendirme/HAKEM_M.md, HAKEM_D.md, HAKEM_K.md. HAKEM_VERI.md yeni veride kullanılmaz.
C merceği K'ya katıldı. Nedenleri: C'nin varsayılan geçme oranı ~%97'ydi; K7 aynı kalıpları kodla arıyor; C ayrı mercekken hakem çağrılarının ~%18'ini tüketiyordu. Birleşince güvenlik maddeleri kartın 'güvenli özellik kullanımı' satırını da görüyor; Örümcek Adam'ın tırmanması ancak böyle doğru değerlendirilebilir. C türü kanaryaların yakalanması <%90 kalırsa C yeniden ayrı mercek olur.
Her istem şu metinle başlar: 'Yalnız kusur ara. Zenginlik, betimleme ve yaratıcılık ödüllendirilmez; kısa ve sade olmak kusur değildir. Şapkasız yazım (rüzgar, kagıt değil kağıt) kuraldır, kusur sayma. Emin değilsen var de ve alıntıla.'
Puan verilmez; her madde yok/var olarak işaretlenir.

M, mantık (2 hakem). Girdi: başlık (figür, yer, yan), plan, gövde ve kartın özellik satırı. Tema verilmez.
M1 Sorun ilk 3 cümlede açıkça söyleniyor.
M2 Hikâyede yalnız bir sorun var.
M3 Sorunun sebebi söyleniyor ve akla yatkın.
M4 Sorunu figür çözüyor (yardım istemek de figürün çözümüdür); yan karakter yalnız yardım ediyor.
M5 Çözüm sebebe doğrudan yöneliyor ve en çok 2 adım sürüyor.
M6 Her olay bir öncekinden çıkıyor; sebepsiz beliren nesne ya da karakter, işlevsiz ayrıntı yok.
M7 Çelişki yok ('yürüyemiyorum' deyip sonra tırmanmak gibi).
M8 Tek sahne ve tek zaman: hikâye başlıktaki yerde başlıyor ve bitiyor; gün, gece ya da hafta atlaması yok.
M9 Son, sorunun çözülmesinden çıkıyor; ders varsa vaaz gibi değil, yaşanan olaydan çıkıyor (eski C5).
M10 Plan satırı hikâyenin sorununu ve çözümünü doğru söylüyor.

D, dil (2 hakem). Girdi: plan satırları, gövde, adlar listesi ve kodun K6 işaretleri.
D1 Her cümle, plan dahil, dilbilgisel: ek, tamlama ('buz köprü' değil 'buz köprüsü'), uyum.
D2 Her kelime doğru anlamda ve öznesine uygun ('köprü kaymıyordu' uygun değil).
D3 Anlatım -dı'lı geçmiş zamanda ve kaymıyor (replikler hariç).
D4 Her replikte konuşan belli ve doğru kişi.
D5 Kimse kendi kendine konuşmuyor ya da kendine adıyla seslenmiyor.
D6 Deyim, mecaz ve soyut kavram yok; 3 yaşındaki bir çocuk her kelimeyi biliyor. İstisna: olaydan çıkan tek ve somut ders cümlesi ('Sırayla oynayınca herkes eğlendi') soyut sayılmaz.
D7 Gereksiz tekrar yok.
D8 Yazım ve noktalama doğru (de/da, ki, kesme, tırnak); plan dahil.
D9 Kimse iki kez tanıtılmıyor; her zamirin kimi gösterdiği belli.

K, dünya-kart ve çocuk güvenliği (1 hakem; pilotta 2). Girdi: kaynaklı tam kart ('güvenli özellik kullanımı' dahil), başlık, plan, gövde, hedef yaş 3–6 ve kodun çoğul canlı notları.
K1 Figür karttaki kimliğine (tür, görünüş, huy) uygun.
K2 Tohumdaki özellik karttaki gibi, bir kez ve işe yarar biçimde kullanılmış; özellik listesi sayılmıyor.
K3 Yan karakterler başlıktaki Yan alanıyla aynı, kartta var ve ilişkileri doğru.
K4 En çok 1 adlı ve 1 isimsiz yan var; arka plandaki çoğul canlılar konuşmuyor ve olaya katılmıyor.
K5 Konuşmayan karakter konuşmuyor; dünyanın kuralları çiğnenmiyor.
K6 Kapalı dünya: kartta olmayan aile üyesi, ev, yetenek, eşya, ya da başka dizinin karakteri, nesnesi veya yeri yok.
K7 Yer, kartın o yer için verdiği tarife uygun.
K8 Diziyi izlemiş bir çocuk figürü ve dünyasını tanır; yanlış bilgi yok.
C1 Korkutucu öğe yok.
C2 Yaralanma, acı ya da hastalık yok (hasta hayvan, üşüyüp hasta olmak dahil).
C3 Taklit edilince tehlikeli davranış yok (derin su, yükseğe tırmanma, ateş, yabancıyla gitme, ilaç); figürün gücü yalnız kartın güvenli kullanım satırındaki gibi kullanılıyor.
C4 Kaba söz, alay, dışlama ya da ceza örnek alınacak biçimde yok.
C5 Son güvenli ve sorun çözülmüş ('sıcaklık' aranmaz; 'sıcak son' şartı Claude'un '…gülümsedi çünkü…' kalıbını besliyordu).
C6 Kalıp yargı yok.

ÇIKTI: Her hakem puan_<lens>_<n>.json dosyasını partideki sırayla yazar. Kayıt biçimi:
{"id", "maddeler": {"M1": "yok", ...}, "ihlaller": [{"madde", "alinti": "<metinden birebir ≥3 kelime>" | null, "cumle_no", "aciklama": "tek cümle"}], "gecti": bool}
Alıntı yerine yalnız cumle_no yalnız eksiklik maddelerinde kabul edilir (M1, M5, M9 ve silinmiş çözüm gibi).
Hakem önce alıntıyı ve açıklamayı, sonra kararı yazar. Kod 'gecti' alanını maddelerden yeniden hesaplar. Tutarsız JSON partiyi geçersiz kılar.

BAĞIMSIZLIK: Her parti yeni bir bağlamda tek bir ajana gider. Ajan yalnız kendi istemini ve parti dosyasını okur; ona başka puan dosyası, yazar bilgisi, deneme numarası ya da önceki gerekçe verilmez. Parti bileşimi mercekler ve hakemler arasında farklıdır (tohumlu karıştırma). İki hakemli mercekte ikinci hakem ters sırayla okur. Madde sırası her hakem için karıştırılır.
Parti boyu ≤10'dur. Eksik kalan parti altın setteki temiz hikâyelerle doldurulur; dolgu hikâyeye verilen 'var' da sayılır. Parti boyu 15–20'ye çıkarılmaz: 40'lık partinin son 8 hikâyesi %30, aynı hikâyeler yeni 8'lik partide %66 reddedilmişti. Pilotta konum etkisi 5 puanı aşarsa parti 5'e iner.
Mümkünse hakem modeli yazardan farklı olur; seçim altın setteki yakalama oranına göre yapılır.

KANARYA:
- Kaynak: degerlendirme/bozucu.py, partideki bir figürün kabul edilmiş ya da altın setteki hikâyesine merceğin türünden tek, küçük ve akıcı bir kusur ekler. Tabanı aynı partide olmaz. Figür partiye yabancı olmadığı için kanarya tek aykırı örnek olarak göze batmaz; K partisi tek kart taşır.
- Sayı: partide rastgele 0–2 (%20 / %50 / %30), rastgele konumda.
- Koşul: her kanarya K1–K9 ve K11'den geçmek zorundadır; kodun yakaladığı tür kanarya olamaz.
- Türler (yalnız kodun göremediği kusurlar):
  M: çözüm cümlesini silmek; sebebi saçma bir gerekçeyle değiştirmek; çelişki eklemek; çözümü yan karaktere vermek; ikinci bir sorun; sebepsiz beliren nesne.
  D: tamlama ekini silmek; özne ile fiil arasında anlam uyumsuzluğu; konuşanı değiştirmek; zamir belirsizliği; ad kullanmadan kendi kendine replik.
  K: kart dışı bir ilişki ya da aile üyesi (yasak düzenli ifadesi olmayan); figürün özelliğine aykırı davranış (düzenli ifadesi olmayan biçimde); yer tarifine aykırılık; kartta olmayan yetenek ya da eşya; kodda listesi olmayan bir sözcükle taklit edilir tehlike, alay, korkutucu öğe ya da kalıp yargı.
- Doğal kanaryalar: altın setteki kullanıcı onaylı, koddan geçmiş, yeni üslupta kusurlu hikâyelerden gelir. Eski hikâyeler K2'yi geçmediği ve üslupları farklı olduğu için kanarya olmaz.
- Hakeme kanarya olduğu söylenmez; kanaryanın kimliği gerçek hikâyelerle aynı biçimdedir.
- Parti ancak BÜTÜN kanaryalar doğru mercekte yakalanırsa geçerlidir. Kaçırılırsa parti yeni bir ajanla bir kez daha koşulur; yine kaçırılırsa hikâyeleri kuyruğa döner. Mercek başına son 50 partide kaçırma %10'u aşarsa o mercek durur ve kullanıcıya raporlanır.
- Yakalama oranı tür × konum × doğal/yapay kırılımıyla raporlanır. Eşik yalnız koddan geçen kanaryalar üzerinden verilir.

OY KURALI (tek yönlü veto): Doğrulanmış ya da uydurma tek bir 'var' ret demektir. Bu, 'var' geçersiz bir partiden gelse de, hikâye kanarya tabanı ya da dolgu olsa da geçerlidir. Geçersiz parti yalnız 'yok' oylarını siler. 'var' hiçbir zaman yeni hakemle silinmez. Eski geçmişte ikinci turda yeniden reddedilen hikâyelerin %34'ünde (46/137) kusur ilk hakemin gördüğü metinde zaten vardı; tek_kedi_2#46'daki hastalık kusuru ikinci görüşte silinmişti.

HAKEM SAYISI:
- M ve D varsayılan olarak 2 hakemle çalışır; K 1 hakemle. Pilotta K de 2 hakemle çalışır.
- Neden iki hakem: q ≤%1 hedefi, p≈%50 iken kaçırmanın ≤%0,75 olmasını gerektirir. En sık kusurlar (mantıksızlık %89, bozuk dil %82) M ve D'ye düşüyor.
- Bir merceği 1 hakeme indirme şartı: ≥200 hikâyede ikinci hakemin tek başına yakaladığı ve kullanıcının örneklemde doğruladığı kusur oranı <%1.
- K'yı 2 hakeme çıkarma şartı: pilotta bu oran ≥%1 çıkarsa ya da C türü kanarya yakalaması <%90 kalırsa.
- Uyum ölçüsü olarak κ kullanılmaz: 'var' oranı ~%10 ve n ~150 iken kappa paradoksu yüzünden κ güvenilmez. Bunun yerine pozitif uyum (2a/(2a+b+c)), ikinci hakemin tek başına yakalama oranı ve kurulun birleşik yakalaması raporlanır.

AĞIRLIK: Bütün hakemler Claude olduğu için aynı hatalarda birlikte yanılabilirler; literatüre göre büyük bir kurul ~2 bağımsız oy değerindedir. Bu yüzden gerçek bağımsızlık kod kapılarından, Zemberek'ten, kullanıcı etiketli altın setten ve dondurulmuş sürümdeki insan örnekleminden gelir. Hakemler bu katmanların yerine geçmez.

## Mevcut verinin akıbeti

KARAR: YENİDEN YAZ. Mevcut hikâyelerin hiçbiri yeni hatta 'kabul' olarak taşınmaz ve hiçbiri düzeltilmez.
Eğitim, izin listesiyle yalnız data/urun_v1'den beslenir. data/oyuncak_v2, v3, v4 ve oyuncak_populer kendiliğinden eğitim dışında kalır ve arşiv olarak durur.
Önceki tasarımdaki 'eski veri yoklaması' (24 Niloya + 24 Tosbi, olumluysa ~150–250 hikâyelik ayrı bir hakem yolu) KALDIRILDI. Nedenleri:
- Eski hikâyelerin tohumu yok; K4 ve Yan alanı tohuma bağlı.
- Plan satırları sonradan LLM ile çıkarıldı ve konumsal kimlikle bağlandı. populer/stitch_1#35'in puanı bugün başka bir metne bağlı.
- v4'te son cümlede 'çünkü' %67–95; bu hikâyeler K12 kalıp kotasına takılır.
- İki hakemli M ve D ile verim daha da düşer.
- Ayrı bir kod yolu karmaşıklık ekler.

GEREKÇE (ölçümler):
(1) Uzunluk: Yalnız '70–100 kelime + her cümle ≤12 kelime' şartı uygulanınca geçen hikâye sayısı: popülerde Maşa 5/96, Niloya 8/96, Pepee 9/96, Elsa 13/96, Chase 16/96, Örümcek Adam 32/96. Temelde paket başına v2 %10–37, v3 %28–47, v4 %39–70. (Ölçüm betiği: scratchpad/mevcut_kapi.py.)
(2) Sade sözlük kapısı tek başına hikâyelerin %21–52'sini geçiriyor. K2 ile K3 birlikte eski oyuncak verisinin yalnız %3–22'sini geçiriyor; 70–100 kelimelik TinyStories hikâyelerinin ise %84'ünü.
(3) Kart hataları sistematik ve kaynağa karşı doğrulandı:
- Niloya'da 43/96 hikâyede 'ağabeyi Mete' geçiyor. niloya.com'a göre ağabey Murat, Mete ise Murat'ın arkadaşı; yani eski karakterler.json:107 yanlıştı. Kartı gören hakem bu hikâyelerin 38'ine 10 verdi.
- Pepee'de 42/96 hikâyede Şuşu ya da Pisi var. Şuşu dizinin görünmeyen anlatıcısı; ürün yan listesinde yok.
- Maşa'nın ve Chase'in yan karakterleri ürün listesinde yok.
- Chase'in sloganı 21 hikâyede D5 ihlali üretti.
(4) 10 almış 20 rastgele hikâyenin yalnız 5'i gerçekten temiz (%25).
(5) Temel figürlerde 672 hikâye hiç hakem görmedi. Hakemden geçen tek paket (v4_2) sade sözlük ölçüsünde en kötü paket.
(6) Stil uyumsuzluğu: Eski hikâyeler tohumsuz ve başka bir sözlükle yazıldı. Kapanışları tekdüze: v4'te duygu kapanışı %25–93; Türkçe TinyStories'te %23.
Düzelterek kurtarmak pratikte yeniden yazmak demek ve riskli:
- Düzeltmeden sonra yeni hakem vakaların %40'ında kusur buldu; bunların üçte biri ilk hakemin kaçırdığı eski kusurlardı.
- Düzeltilen hikâyeler ortalama 4 kelime uzadı.
- _2 paketlerinde nadir kelime %36–77 arttı. _2 içeren modeller tabandan %42–47'de kaldı; ancak bu sonuç 'ya da şans' diye kayıtlı.

ESKİ VERİ NEREDE KULLANILIR:
(a) Hakem istemlerinde örnek: sample20'deki 15 kusurlu ya da pürüzlü hikâyeden kullanıcı onaylı 3–5 gerçek eleştiri HAKEM_<lens>.md'ye girer. Bu hikâyeler altın sete ya da kanaryaya girmez: K2'yi geçmiyorlar (sample20'de yalnız 6/20 geçiyor) ve hakemin göreceği metni temsil etmiyorlar.
(b) Kök neden kaynağı: 10 almış eski hikâyelerdeki kusur desenleri (zaman atlaması 53, hasta hayvan kalıbı 16, liste dışı hayvan %24) K1, K4 ve K7 kurallarının ve kanarya türlerinin kaynağıdır.
(c) Eski planlardan (sorun | çözüm) yalnız tema fikri alınabilir; metin kopyalanmaz.

Hakemsiz veriyle eğitilmiş modeller (c3ft_v6, c3ft_tek gibi) 'kusursuz veriyle eğitildi' diye sunulmaz; bunlar yalnız kıyas tabanıdır. Keloğlan, Doru, Hayri ve Şakir'in hiç verisi yok; zaten sıfırdan yazılır.

## Miktar ve takvim

HEDEF: Figür başına 200 eğitim kabulü, yani 14 × 200 = 2800. Buna ~50 doğrulama kabulü eklenir (figür × yer hücresi başına 1; kusursuz ama eğitime girmez). Toplam iki aşamada toplanır:
- Aşama 1: figür başına 100 (1400) + doğrulama bölmesi; ardından eğitim ve ölçüm.
- Aşama 2: figür başına 200.
- Figür başına 300'e yalnız şu durumda çıkılır: Aşama 2 modeli Aşama 1 modelini ikili hakemde anlamlı olarak yenerse (p<0,1) ve öğrenme eğrisi hâlâ yükseliyorsa.

GEREKÇE:
(1) Bilinen çalışan ölçek: Tek kazanan c3ft_v6 ~4353 oyuncak hikâyesiyle eğitildi. c3ft_tek 2995 hikâyeyle, ×6 tekrarla eğitildi. c3ft_tek günlüğünde doğrulama kaybı 1750–4000. adımlar arasında 2,87–2,91 aralığında salınıyor. Bu, eski tasarımın dediği gibi aşırı uyum değil, bir plato. Aşama 1'in 1400 hikâyesi ~0,245 M token eder; aynı 5000 adımda her hikâye ~13 kez görülür. Bu yüzden tekrar sayısı ve adım oyuncak maruziyetine göre ayarlanır (örneğin tekrar 4, ~3000 adım). Eğitim, urun_v1 doğrulama bölmesinde en düşük kayba ulaşılan adımda durur.
(2) Kapsama: Figür başına 3–5 yer × 12 tema = 36–60 hücre. 200 hikâyede hücre başına 3–5 hikâye düşer; en küçük yer bile ≥20 hikâye alır (her yere ≥%10).
(3) Kalıplaşma: K12 kotaları ve kapanış türü ile sınırlanır. Yakın kopya reddi %15'i ya da Self-BLEU artışı %10'u geçerse o figürde üretim erken durur.
(4) Az ama temiz (LIMA, phi): Kusurlu hikâye hacim için asla tutulmaz. 2800 × ~175 token ≈ 0,49 M; bu v6'nın ~%60'ı.

AŞAMA 1 DENEYİ (hangi etkinin hangisi olduğunu ayırmak için dört kol):
- A: ana tarif (Yan alanlı başlık, genel 8M).
- B: A ile aynı, ama genel dilim kodla süzülmüş.
- C: A ile aynı, ama Yan alanı yok.
- D: A tarifi, 700 hikâyeyle (öğrenme eğrisi noktası).
Kıyas iki kısımdan oluşur:
- 10 ortak figürün 30 vakası, c3ft_v6 ve c3ft_tek'e karşı. Her model kendi eğitim başlık biçimiyle istenir; eski modeller 'Karakter: kaplumbağa' biçimiyle.
- 4 yeni figürün 12 vakası, ayrı ve mutlak rubrikle. Eski modeller bu figürleri hiç görmediği için bu vakalar kıyasa bedava kazanç olarak girmez.
Sonucun yorumu: A v6'ya yenilir ve D ≈ A ise sorun yeni üsluptadır, hacimde değil; kılavuz ve tohum gözden geçirilir. D belirgin olarak A'nın altındaysa hacim işe yarıyordur ve Aşama 2'ye geçilir.

TAHMİNİ AJAN ÇAĞRISI (pilottan gelecek gerçek oranlarla güncellenir):
Varsayımlar:
- Tek yama turundan sonra kod kapısı geçişi %85.
- Mercek geçme oranları: M (iki hakem birleşik) %58, D (iki hakem) %74, K %88. Oy birliği ≈ %38.
- Kabul/yazılan ≈ %32. Kota ve yedek kaybı %5.
Hesap:
- Gereken kabul ≈ 3000; yazılacak hikâye ≈ 9400. Figür başına ~670 yazım ve ~400 tohum; 2 denemeyle bir tohumun geçme olasılığı ~%54.
- Yazar: 9400 / 12 ≈ 785 çağrı.
- Hakem kararı: M 2 × 7990 + D 2 × 4630 + K 3430 ≈ 28 700 karar. Parti başına ortalama 1 kanarya ile ≈ 31 900 parti yeri. Çağrı başına 10 kararla ≈ 3190 çağrı; %5 yeniden koşuyla ≈ 3350.
- Pilot-0, Pilot-1 ve kalibrasyon turları ≈ 320.
- Hedefli yeniden hakem ve kök neden payı ≈ %20–30 ≈ 700–1000.
TOPLAM ≈ 5300 çağrı (aralık 4500–6500). Bu, eski tahminin (2750) yaklaşık iki katıdır; M ve D'deki ikinci hakemin ve yeniden koşu payının bedeli. Oy birliği %28'e düşerse ~6500'e çıkar. Pilotta ikinci hakemin tek başına yakaladığı kusur <%1 çıkarsa ~%25 azalır.

SÜRE: Yazar çağrısı ~8 dk, hakem çağrısı ~3 dk. Toplam ≈ 19 900 ajan-dakika (~330 ajan-saat). Bu, 16 paralel ajanla ~21 saat, 8 paralel ajanla ~41 saat duvar saati eder. Aşama 1 bunun yaklaşık yarısıdır. Eğitim: c3ft_tek günlüğüne göre 2750 adım 4658 sn sürdü; 3000–5000 adımlık bir kol ~1,5–2,5 saat, dört kol ~8–10 saat.

TAKVİM:
- Gün 1: pilot araçları (Adım 0'ın ilk kısmı) ve 14 kartın web kaynaklı taslağı. Kartlar kullanıcı onayına gider.
- Gün 2: kart onayı. Pilot-0 (Tosbi ve Keloğlan, 12'şer; araç hata ayıklama). Pilot-1 yazımı (14 × 12).
- Gün 3: kullanıcı ~150 hikâyeyi körlemesine etiketler (~2 saat). Kurul koşar (~100 çağrı). Uyum raporu çıkar. En çok 2 istem turu yapılır.
- Gün 4–5: Aşama 1 (1400 + 50 kabul). Alarm örneklemi: figür başına 10, yani 140 okuma (~1,5 saat).
- Gün 6: dört eğitim kolu ve ölçüm.
- Gün 7–8: Aşama 2 (+1400) ve alarm örneklemi.
- Gün 9: dondurma, son kontrol, kesin örneklem (308 + ~25 kanarya, ~4 saat okuma), c3ft_urun2 eğitimi ve ölçümü.
Kullanıcının toplam okuma yükü ≈ 150 + 140 + 140 + 333 ≈ 760 hikâye, ~9 saat; günlere yayılır. Anadili Türkçe ikinci bir okur yükü bölebilir. Kesin örneklemde kusur çıkarsa her yeni sürüm için +333 okuma gerekir.

## Pilot

İKİ PARÇA.

PİLOT-0 (duman testi; ölçü alınmaz):
- Önkoşul: Tosbi ve Keloğlan kartları kaynaklı ve kullanıcı onaylı.
- 12'şer tohumla bütün zincir uçtan uca koşulur: tohum → yazar → kontrol/yama → kapi → hazirla → hakem → oku → karar.
- Serileştirme, sha1 bağı ve prepare_ft2 --yalniz korumaları küçük bir izin listesiyle sınanır. Hatalar giderilir.
- ~20 çağrı.

PİLOT-1 (altın set = kalibrasyon):
- Önkoşul: 14 kartın hepsi onaylı; Adım 0'ın birim testleri geçmiş.
(1) 14 figür × 12 tohum = 168 yazım (14 yazar çağrısı). Tohumlar tam dağılımdan çekilir.
(2) `kapi`: kapı başına geçme tablosu çıkarılır. Tohum kaynaklı retler ayrıca sayılır.
(3) Koddan geçen ~145 hikâye ve ~12 okur kanaryası karışık sırayla degerlendirme/urun_v1/pilot/insan.md'ye yazılır. Kullanıcı ya da anadili Türkçe okur, kurulu görmeden her hikâyeye 'kusursuz' ya da 'kusurlu: <cümle> <neden> <mercek>' yazar (~2 saat). Doğal kusurlu ya da temiz hikâye 60'tan azsa 14'lük ek partiler yazılır ve etiketlenir.
(4) Etiketleme bittikten sonra kurul koşar: her mercekte 2 hakem (K dahil), kısa devre yok, parti ≤10, 0–2 kanarya (~100 hakem çağrısı).
(5) `oku`, `karar` ve `uyum urun_v1 --pilot` komutları koşulur.
(6) Uyuşmazlıklar kullanıcıya açılır: hakemin 'var' dediği ama kullanıcının kusursuz dediği hikâyeler ve tersi. Kullanıcı kimin haklı olduğunu işaretler. Hakem haklıysa bu, okur kaçırması olarak kaydedilir.
(7) Set 'geliştirme' ve 'ölçüm' olarak ikiye bölünür. Kullanıcının 3–5 eleştirisi istemlere, onayladığı 2 kabul (farklı figür ve kapanış türünden) kılavuza girer.
Toplam ~120 çağrı ve kullanıcı için ~2,5 saat.

ÖLÇÜLECEKLER (hepsi uyum raporunda):
a) Kapı başına geçiş; hedef, tek yama turundan sonra ≥%85. K5 ve K7'nin yanlış alarmı. Eşik gevşetilmez; kılavuz ya da liste düzeltilir.
b) Kusur yaygınlığı p (kullanıcı etiketinden), mercek başına ret, birleşik oy birliği, uçtan uca verim (hedef ≥%25).
c) Her hakem ve birleşik kurul için kaçırma m ve yanlış ret f, %95 güven aralığıyla. Bunlardan q̂ = p·m / (p·m + (1−p)(1−f)) hesaplanır.
d) Mercek içi pozitif uyum ve ikinci hakemin tek başına yakaladığı, kullanıcının doğruladığı kusur oranı. Mercek başına hakem sayısı buna göre belirlenir.
e) Kanarya yakalama: tür × konum × doğal/yapay kırılımıyla.
f) Uydurma alıntı ve geçersiz parti oranı.
g) Konum etkisi: ilk ve ikinci yarı ret farkı; iki okuma sırası arasındaki fark.
h) Yamalı ve yamasız hikâyelerde kusur oranı; okurun kanarya yakalama oranı.
i) Kabul edilen hikâyelerin ölçüleri: kelime sayısı, cümle uzunluğu, nadir kelime (≤1,5), Ateşman, c3 kaybı (rapor), kapanış ve açılış kalıp payları, tohum özelliği başına kabul payı.
j) Kabul edilen hikâye başına çağrı ve dakika; tam ölçek tahmini bununla güncellenir.
k) Kullanıcının kartlarda bulduğu olgu hataları.
l) Yazar ve hakem modeli seçimi.

GEÇ/KAL ŞARTLARI (hepsi ölçüm yarısında gerekli):
- q̂ ≤ %1, ve birleşik yakalamanın %95 alt sınırı ≥%90.
- Yanlış ret ≤%25.
- Her mercek, koddan geçen kanaryalarda ≥%90.
- Uydurma alıntı ≤%3.
- Kod geçişi ≥%85.
- Uçtan uca verim ≥%25.
- Kabul edilen hikâyeler K2 ve K3 hedeflerinde.
- Okurun kanarya yakalaması ≥%90. Değilse okuma yöntemi değişir (daha kısa oturumlar ya da ikinci okur).

BAŞARISIZLIKTA:
- İstem yalnız geliştirme yarısına bakılarak düzeltilir. Yeniden ölçüm, ölçüm yarısında ve yeni etiketlenmiş 14 × 6 hikâyede yapılır. En çok 2 tur.
- GERİ ÇEKİLME 1: Bütün mercekler 2 hakemle çalışır, parti 5'e iner ve kesin insan örneklemi iki katına (616) çıkar.
- GERİ ÇEKİLME 2 (o da tutmazsa): Kullanıcıya sorulur. Ya durulur ya da veri 'kod ve hakem kapılarından geçti, kusursuzluğu kanıtlanmadı' etiketiyle devam eder. Sessizce devam edilmez.
Bu şartlar sağlanmadan tam ölçeğe geçilmez.

## Riskler

- Korelasyonlu hakem hatası: Bütün hakemler Claude. Literatüre göre büyük bir kurul ~2 bağımsız oy değerinde. Kodla yakalanamayan mantık ve dünya kusurları kaçabilir. Önlem: tek yönlü veto, M ve D'de iki hakem, koddan geçen kanaryalar, kuruldan önce etiketlenmiş altın set, dondurulmuş sürümde tek insan örneklemi, mümkünse yazardan farklı hakem modeli. Kalan risk Clopper-Pearson üst sınırıyla raporlanır; 'sıfır hata' iddia edilmez.
- Kusur yaygınlığı p yüksek kalırsa hedef tutmaz. q ≤%1, p≈%50 iken kurulun kusurluların ≥%99,3'ünü yakalamasını gerektirir. Bunu 60 kusurluluk bir altın set ancak '0 kaçırma' olarak gösterebilir. Önlem: yazar modeli p'ye göre seçilir; tohum ve kılavuz p'yi düşürecek biçimde sadeleştirilir; asıl güvence kesin insan örneklemidir.
- Kanaryalar tanınabilir kalabilir. Önlem: kanarya aynı figürden gelir, kod kapılarından geçer, partide 0–2 tane ve rastgele konumda bulunur, bir kısmı doğal kusurlu yeni hikâyelerdir. Eşik yalnız koddan geçen kanaryalarla verilir. Kalan risk: bozucu'nun yaptığı değişiklikler yine de biçemce sezilebilir. Bu yüzden karar altın setteki doğal kusurlara dayanır.
- Yanlış ret ve tek tipleşme: 'Emin değilsen var de', tek yönlü veto ve iki hakem birlikte bazı temaları ve tohum özelliklerini sessizce eleyebilir. Önlem: yanlış ret ≤%25; tohum özelliği başına kabul payı izlenir ve sapan hücreye fazladan tohum verilir; kalıp kotaları ve Self-BLEU izlenir. Çözüm kapıyı gevşetmek değil, tohumu çoğaltmaktır.
- Kart bilgisi: Claude'un dizi bilgisi güvenilir değil. Bu oturumda iki Claude kaynağı Niloya'nın ağabeyi konusunda çelişiyordu; niloya.com hangisinin doğru olduğunu gösterdi. Doru'nun 'Alaca'sı için kaynak bulunamadı. Keloğlan'ın 'şato' yeri ve Doru'nun 'park' yeri dünyaya uymuyor. Önlem: her olgu için zorunlu kaynak, kapalı dünya kuralı, kullanıcı onayı, sha1 kilidi; kart değişince K4 ve K merceği o figürde yeniden koşulur.
- Resmî adlar sade kurallarla çatışır: 'Dorukısrak' 5 token, 'Karakaçan' 4 token, 'Örümcek Adam' iki kelime. Önlem: kartta metinde kullanılacak kısa ad ya da rol yazılır ('annesi', 'eşeği') ve kullanıcı onaylar. Kesme eki okunuş alanıyla denetlenir. 'Kamil' kaynaklarda şapkasız yazılıyor.
- Başlık biçimi değişikliği: Yan alanı; baslangic.py, secici.h ve firmware'de de değişiklik gerektirir. Kullanılmayan kol (Yan alanlı ya da alansız) Aşama 1'den sonra atılır. sec.py listeleri değişince secici.h'nin eşzamanlı güncellenmesi gerekir. Önlem: listeler tek kaynaktan üretilir; secici.h'nin sürümü manifest'e girer.
- Kapsam yanılgısı: Kullanıcı 'eğitime giren her hikâye' dedi, ama ince ayar tokenlarının ~%73'ü ve ön eğitimin tamamı hakemsiz TinyStories'tir. Önlem: bu durum kullanıcıya açıkça yazılır ve B kolu (kodla süzülmüş genel dilim) ölçülür. Ön eğitimi yeniden yapmak bu planın dışındadır.
- Az veri ve yeni üslup: Aşama 1'de oyuncak verisi v6'nın yaklaşık üçte biri. R-temiz ve c3ft_v9 az veya süzülmüş verinin kaybedebildiğini gösterdi. 'Kusursuz ama az' veri v6'dan kötü sonuç verebilir. Önlem: urun_v1'den ayrılmış doğrulama bölmesiyle erken durdurma; D kolu (700 hikâye) ile hacim ve üslup etkisi ayrılır; kıyas ortak 10 figürde ve her modelin kendi başlık biçimiyle yapılır. Hacim yalnız yeni kusursuz hikâyeyle artırılır.
- Beklenti: Verinin kusursuz olması modelin kusursuz yazacağı anlamına gelmez. 5,7 M'lik model kusursuz veriyle de mantıksız ve bozuk cümleler üretecek; gerçekçi hedef rubrikte 5,5–6,5.
- Zemberek ve kod yanlış alarmları: özel adlar, 'gökkuşağı', -mış sıfat-fiilleri, 'kanadı'. numpy 2 ile yazım denetleyicisi hata veriyor; yalnız biçimbilim kullanılacak. Önlem: beyaz liste (sürüme dahil), tr-tinystories ve altın sette yanlış alarm ölçümü, Python sürümü olmazsa Java jar.
- Süreç disiplini: hakemden sonra metnin değişmesi, paralel ajanların birbirinin dosyasına yazması (20c1e76), sürüm kaybı, yanlış KAYNAK ile eğitim (Tur 8). Önlem: kanonik kayıt sha1'i, ortak serileştirme, izin listesi, prepare_ft2 korumaları ve manifest, ajan başına tek dosya, içerik sha256'lı sürüm.
- Okuma yükü ve maliyet: ~760 okuma (~9 saat) ve ~5300 ajan çağrısı (~330 ajan-saat). Kesin örneklemde her kusur +333 okuma demektir. Okuma yapılmazsa istatistiksel güvence ortadan kalkar; o durumda veriye 'kusursuz' değil, 'kod ve hakem kapılarından geçti' denmeli.
- REDDEDİLEN ya da DEĞİŞTİRİLEN ELEŞTİRİLER (1/5): Eleştiri 2, D ve C partilerini 15–20 hikâyeye çıkarmayı önerdi; REDDEDİLDİ. Eleştiri 1'in konum kanıtı tersini gösteriyor: 40'lık partinin son 8'i %30, aynı paketlerin yeni 8'lik partisi %66 reddedildi; 48'lik partide ilk 8 %56, son 8 %26. Büyük parti katılığı düşürür. Parti ≤10 kalır, konum etkisi çıkarsa 5'e iner.
- REDDEDİLEN ya da DEĞİŞTİRİLEN ELEŞTİRİLER (2/5): Eleştiri 2, 'hâlâ'yı beyaz listeye almayı önerdi; REDDEDİLDİ. Şapka 0 kuralını deler, normalizasyon ve alıntı eşleşmesini karıştırır, ön eğitimde nadirdir (191'e karşı 10 749). Eleştiri 1'in çözümü alındı: yazar 'yine' ya da 'daha' kullanır, K3 'hâlâ'yı reddeder. Eleştiri 2'nin genel dilimi K5 ile de süzme önerisi KISMEN REDDEDİLDİ: yalnız -dı anlatımı bir üslup kuralıdır, kusur değildir. -mış masal anlatımı TinyStories'in %17'sinde meşrudur. Süzme yalnız K7, K8 ve Zemberek ile ve yalnız ayrı bir kol olarak yapılır; R-temiz'de körlemesine temizlik kaybetmişti.
- REDDEDİLEN ya da DEĞİŞTİRİLEN ELEŞTİRİLER (3/5): Eleştiri 1, sha1'in prepare_ft2'nin yazacağı kesin dizgi üzerinden alınmasını önerdi; BİÇİM OLARAK DEĞİŞTİRİLDİ. Aynı hikâye planlı ve plansız (%70) ve Yan alanlı ve alansız kollarda farklı dizgilere dönüşür; dizgi sha1'i hikâyeyi dörde bölerdi. sha1 kanonik kayıttan alınır; dizgiyi yalnız kapi.py ile prepare_ft2'nin ortak import ettiği serileştirme fonksiyonu üretir. Amaç (hakemlenen = eğitilen) korunur, çünkü bütün alanlar hakemlenir ve dizgiler bu alanların deterministik alt kümeleridir. Eleştiri 1'in çağrı başına ≤3 ya da tek hikâye önerisi varsayılan olarak ALINMADI: hakem maliyetini 3–10 kat artırır ve 10'luk partide etki henüz ölçülmedi; iki hakemli M ve D'de ters sıra etkiyi zaten dengeler. Pilotta etki >5 puan çıkarsa parti 5'e iner.
- REDDEDİLEN ya da DEĞİŞTİRİLEN ELEŞTİRİLER (4/5): Eleştiri 1, Keloğlan'ın 'şato' ve Doru'nun 'park' yerlerini doğrudan değiştirmeyi önerdi; ÖNERİ OLARAK ALINDI, karar kullanıcıya bırakıldı. Yer listesi ürünün kesin figür listesinin parçası ve firmware'in yer seçimini etkiliyor. Eleştiri 2, kalıp kotasını yalnız kabul anında uygulamayı önerdi; KISMEN alındı. Asıl yönlendirme tohumdaki kapanış türüyle yapılır; kota yedek hattır; kotayı aşan kusursuz hikâye atılmaz, yedek havuza gider. Eleştiri 2, κ'yı pozitif uyumla değiştirmeyi önerdi; ALINDI.
- REDDEDİLEN ya da DEĞİŞTİRİLEN ELEŞTİRİLER (5/5): Eleştiri 2, altın setin 50 temiz örneğini 'ilk 200 kabulden sonra' tamamlamayı önerdi; REDDEDİLDİ. Kabullerden kurulan set kurulun kendi kararına dayanır, yani döngüseldir. Eleştiri 1'in yöntemi alındı: koddan geçmiş pilot yazımından tabakalı örneklem kuruldan önce etiketlenir; bu, 50 temiz örnek bulma sorununu da çözer. Eleştiri 2'nin 'kanarya 3. hatada hat durmasın' önerisi alındı, ama ek bir güvenlikle: mercek başına son 50 partide kaçırma >%10 olursa o mercek durur. Tasarımın kendi iki iddiası düzeltildi: '_2 modeli kötüleştirdi' iddiası 'ya da şans' kaydıyla yumuşatıldı; c3ft_tek'teki kayıp eğrisi 'aşırı uyum' değil 'plato' olarak yazıldı (logs/c3ft_tek.log: 1750–4000. adımlarda 2,87–2,91).
## Kullanıcı kararları (kullanıcı "en iyisi neyse" dedi; uygulanan seçimler)

1. Tohum listeleri: sık kök listesi 2100 → 3000'e çıkarılır (dışlama kuralları aynen kalır); hedef 600/400/200'e yaklaşılır.
2. canli_rol.json'daki 26 belirsiz kelime: çocuk güvenliği ve kapalı dünya gereği yasak (karakter olarak geçerse ret);
   yalnız cansız/oyuncak anlamı açık olanlar ('oyuncak bebek', 'ayıcık' = oyuncak ayı) karakter sayılmaz.
3. Temel figürlerin isimsiz yan hayvanları konuşur (figürler de konuşuyor; dünya tutarlı).
4. Karakaçan (Keloğlan'ın eşeği) ve Yumak (Basri Amca'nın köpeği) konuşmaz.

Uygulama (kullanıcı yetkisiyle karar; kullanıcı "en iyisi nasıl olacaksa" dedi):

- Karar 1: `sade_sozluk.py olustur --sik 3000 --kok ek` (en az kök sıklığı 506 → 137; ilk 2100 kök aynı kaldı). Yeni
  900 kök elle etiketlendi: +isim, +fiil, +sıfat ve yeni canlı/rol adları (yusufçuk, aygır, mumya, kovboy, lider,
  yolcu...). Sonuç 461 isim / 393 fiil / 236 sıfat (hedef 600/400/200; isimde kalan açık, soyut, yer, vücut ve
  tehlikeli isimlerin dışlanmasından). Etiket kaynağı degerlendirme/tohum_etiket.py.
- Karar 2: K4 belirsiz kelimeyi reddeder (K4.belirsiz); yalnız önünde 'oyuncak' varsa, ardından canlı/rol ismi
  geliyorsa (sıfat: 'bilge kaplumbağa') ya da canli_rol.json'daki kelimeye özel nesne kalıbı ('bir sürü', 'meşe
  palamudu', 'yardımcı ol-') geçişi kapsıyorsa geçirir ve K merceğine not yollar. Kartın izinli dünya kökü olan
  belirsizler (Hayri'de 'bakkal', Doru'da 'sürü') nottur. HAKEM_K.md: notlanan kelime canlı ya da konuşan olarak
  geçerse K6 'var'. Kılavuz Kural 5'e tek cümle eklendi. Elsa'nın 'halkını korur' özelliği 'kız kardeşini korur'
  oldu (halk belirsiz). Tohum kelimeleri belirsizleri ve ürün adlarıyla aynı kelimeleri (pamuk) hiç almaz.
- Karar 3 ve 4: kartlarda temel figürlerin 16 isimsiz yanı konusur: true, Karakaçan ve Yumak konusur: false;
  kaynak 'kullanici_karari', onay_bekliyor bayrakları kalktı.
- K3 az görülmüş token eşiği 20 (ret); 20-199 arası yalnız rapor (aday.jsonl 'az_token_200').
- Açık noktalar, en ihtiyatlı kaynaklı seçimle kapandı (her kartın 'kararlar' alanı): Niloya'da 'babaannesi'; Maşa'da
  dağ = kaynaktaki tepe; Pepee'de orman ve park genel tarifle kalır, kısa ad 'Nenee'; Keloğlan'da şato sahipsiz taş
  saray (Kara Vezir ve padişah girmez), dağ = köyün tepesi, kısa ad 'eşeği'; Doru'da park = sürünün çayırı (etiket
  firmware için 'park'), kısa ad 'annesi', Gelincik yasak adlarda; Hayri'de yerler genel tarifle kalır, Hale yasak
  adlarda; Şakir'de park genel; Elsa'da orman karlı orman; Chase okunuşları kabul; Örümcek Adam'da kısa ad
  'Ghost-Spider' (Gwen yasak). Yer listesi ürün listesiyle aynı kaldı; yer çıkarılmadı. 14 kart onaylı ve
  `veri_hakem.py kart-kontrol --kilitle` ile data/urun_v1/kart_kilidi.json'a kilitlendi.
- Kart metni kapılarla çatışmaz: kart-kontrol artık yazarın kopyalayacağı metinde (yer tarifi, özellik, kimlik
  cümlesi, yan ilişkisi) K7 kalıbını ve kökü de yüzeyi de nadir (< 20) kelimeyi hata sayar. 'yamaç', 'ağaçlı',
  'ağaçlık', 'tepelik', 'oyunbaz', 'anaç', 'kapkara', 'dalmaçyalı', 'isimsiz'... sade kelimeyle yeniden yazıldı;
  Chase'te 'iskele' izinli dünya kökü oldu. Yer tariflerinden 'Kimse derin suya girmez' çıktı ('Herkes kumda ve su
  kenarında kalır'); güvenli kullanım satırı 'derin suya girmez' diyen kartlarda (Tosbi, Pepee, Maşa, Doru)
  'derin suya girmedi' yankısı k7_izinli ile K7'ye takılmaz. K4'te cümle başındaki yaygın kelime ardından fiil ya da
  bağlaç olmayan kelime gelince ad sayılmaz ('Kara bulutlar'); ürün adları ('Pamuk') yalnız 'gibi' ile sıfat sayılır.
- Tohum kartın dünyasına uyar (Adım 3): yanın 'yerler' alanı (Tosbi'de balık yalnız denizde; kirpi, sincap ve
  baykuş orman ve dağda; Pamuk'ta keçi dağ ve deniz kıyısında), kartın 'tohum_yasak_kategoriler' alanı (doğa
  dünyası: Tosbi, Tekir, Pamuk, Karabaş, Doru — teknoloji, araç, çağdaş eşya, ev eşyası, mutfak, giysi, okul yok;
  masal ve köy: Keloğlan, Elsa, Niloya, Maşa — teknoloji, çağdaş araç ve çağdaş eşya yok; Şakir ve Örümcek Adam —
  teknoloji yok) ve kelimenin gerektirdiği canlı (tasma/kemik köpek, havlamak köpek, ötmek kuş...). Kartın kendi
  metninde geçen kelime yasak kategoride olsa da gelir (Niloya'nın parkında kaydırak). tohum_denetle bunları da
  denetler.
- K9 havuzu aynı turdaki önceki adayları da içerir (kapı ve yazar kontrolünde; aynı tohumun kendi kaydı hariç):
  hakemden önce iki yakın kopyanın birlikte kabul edilmesi önlenir; turdaki ilk aday kalır.
- prepare_ft2 --yalniz onaysız kartla kabul edilmiş veriyi ('# taslak_kart' izin notu ya da kabul.jsonl'de
  taslak_kart) reddeder; yalnız duman testi için --taslak-kart-izin.
- Kılavuzun iki iyi örneği (ilk hâli Tosbi/görüntü, Niloya/replik; kapanış kararından sonra Tosbi/duygu, Niloya/replik) ve HAKEM_M/D/K.md'deki eleştiri örnekleri kullanıcı
  yetkisiyle yazıldı; hepsi kod kapılarından geçer (kusurlu örnekler yalnız hakemin görebileceği türdendir).
- Zemberek (zemberek-python 0.2.3, setuptools<70) .venv'e kuruldu; K5 çözümlemesi artık atlanmıyor.
- Pilot tur 2'den sonra (kullanıcı yetkisiyle karar): tohum kategorilerine `hazir_yiyecek`, `bostan`, `calgi`, `buyu`
  eklendi. Doğa figürleri (Tosbi, Tekir, Pamuk, Karabaş) üçünü de, Doru `hazir_yiyecek` ve `calgi`'yı yasaklar;
  `buyu` Elsa ve Keloğlan dışında yasak. Kartlar yeniden kilitlendi; pilotun 3 kabulü eğitimden önce K4 ve K
  merceğinden yeniden geçmeli.
- 21 hikâyeyi okuduktan sonra (kullanıcı geri bildirimi) — son: 'eylem' ve 'görüntü' kapanışları hikâyeyi yarım
  bırakıyordu ('Sonra Elsa uzun zinciri sarayın kapısına astı.', '... kırmızı hazine kutusu duruyordu.'). Her hikâye
  sorun çözülmüş ve sıcak bir kapanış cümlesiyle biter; kapanış türleri duygu %35 (olaya bağlı his, 'çünkü' serbest),
  sonuç %30 ('oyunlarına mutlu mutlu devam ettiler'), replik %20 (kapanış, teşekkür ya da sevinç repliği; ardından
  cümle yok), ders %15 ('bundan sonra' serbest). Kılavuz Kural 9 ve tohum tanımları yeniden yazıldı; Kural 3'e
  'açık küçük hedef ve doyurucu sonuç' eklendi (madde sayısı 10 kaldı). HAKEM_M.md M9 kapanışsız sonu (çıplak eylem,
  durgun resim, açılmayan hazine kutusu) ve 'hiçbir şey olmayan' hikâyeyi işaretler. Kılavuzun Tosbi örneği yağmur
  beklemek yerine merak/keşif ve duygu kapanışıyla yeniden yazıldı; Niloya örneği ve HAKEM_M tabanları sıcak bir
  son cümle aldı (hepsi `veri_hakem.py kontrol`dan geçer). K12'nin duygu fiili kotası %35 → %50 (duygu kapanışı
  tek başına %35).
- 21 hikâyeyi okuduktan sonra (kullanıcı geri bildirimi) — tema: hikâyeler hep 'hata → özür → düzeltme'
  mantığındaydı; 'beklemek' (kayanın altında yağmurun dinmesini bekleyen köpek) anlamsızdı. Temalar ağırlıklı oldu
  (TEMA_AGIRLIK): yeni temalar merak_kesif, oyun_eglence, yardim_etmek (hasta ya da yaralı hayvan değil),
  kutlama_hazirlik ('surpriz' buna katıldı), doga_gozlem, taklit_hayal; ahlaki çatışma temaları (paylaşmak, yardım
  istemek, özür dilemek, sırayla oynamak) birlikte %28 ve tohum_denetle ≤%30'u denetler; 'beklemek' yalnız ilginç bir
  hedefle (fırındaki kek) ve %1. Kılavuz Kural 3: sorun çoğunlukla dışarıdan gelir; figürün kendi hatası yalnız özür
  temasında olur. `tohum --figur hepsi --n 400 --tohum 2026` 14 figürde geçer. data/urun_v1/tohum altındaki eski
  tohumlar değiştirilmedi; yeni temalar yeni tohum üretiminde gelir.
- 21 hikâyeyi okuduktan sonra (kullanıcı geri bildirimi) — Örümcek Adam: ev tarifi 'Takımın gizli üssü.' 'gizli
  üste' yazdırıyordu ve çocuk 'üst' ile karıştırıyor. Tarif 'Takımın gizli evi.' oldu, 'üs' izinli dünya
  köklerinden çıktı ve bir dünya kuralı ('üs', 'üssü', 'üsse', 'gizli üste' yasak; 'üst', 'üstüne' serbest) eklendi.
  Kart yeniden kilitlendi (`kart-kontrol --kilitle`); Örümcek Adam'ın eski kabulleri K4 ve K merceğinden yeniden
  geçmeli.
- Hello Kitty yeni popüler figür (kullanıcı isteği). Kart kaynaklı (Sanrio resmi sitesi ve blogu, Vikipedi EN/TR,
  Hello Kitty çizgi dizileri listesi): kırmızı kurdeleli beyaz kedi; özellikler arkadaş edinmek, kurabiye yapmak,
  elmalı turta; yerler park, orman, ev (park ve orman yalnız bölüm adlarına dayanır: 'A Trip to Rainbow Park',
  'Happy Campers'); yanlar Mimi (kaynakta Mimmy, ikiz kız kardeşi), annesi, babası. Çizimde ağzı yok ama dizilerde
  konuşur: hikâyede konuşur, ağzından söz edilmez; Londra/şehir yolculuğu, marka ve mağaza yok; tohumda teknoloji,
  çağdaş araç ve büyü yok. Dear Daniel, evcil hayvanlar, dede/nine ve öteki Sanrio karakterleri yasak adlarda.
  Kart onaylı (kullanıcı yetkisiyle karar) ve urun_v1, urun_v2 kilitlerine eklendi (öteki kilitler değişmedi);
  `tohum urun_v2 --figur "Hello Kitty" --n 400 --tohum 2027` geçti, ilk yazım istemi data/urun_v2/istem/hello_kitty_1.md.
- Yalnız çizgi film karakterleri (kullanıcı isteği): temel figürler Tosbi, Tekir, Pamuk, Karabaş ürün listesinden
  çıktı (data/urun_figurleri.json 'cikarilanlar', 'cikarilma_nedeni'; eski girdileri 'cikarilan_temel'). Kartları
  urun_kartlari.json'da değişmeden durur (kilitler bozulmaz); kart-kontrol onları denetler ama etkin saymaz,
  `tohum --figur hepsi` atlar, kapı K1 onların hikâyesini reddeder (K1.figur) ve adları 'cikarilan_figur' olarak
  öteki figürlerin hikâyelerinde yasaktır. Etkin liste 11 figür: Niloya, Maşa, Pepee, Keloğlan, Doru, Hayri, Şakir,
  Elsa, Chase, Örümcek Adam, Hello Kitty. Kapı mekaniği testleri Tosbi tabanlarıyla yazıldığından testler bu
  figürlerin etkin olduğu bir kopya listeyle koşar (tests/test_urun_kapi.py); gerçek listeyi ayrı testler sınar.
  Tosbi'nin mevcut aday ve kabulleri silinmedi ama eğitime girmemeli.
- Onarım döngüsü (kullanıcı yetkisiyle karar; urun_v2'nin ilk hakem turunda 85 adaydan 2 kabul, kusurlar gerçek
  ama yerel): Adım 9a. `onar-istemi` yalnız hakem merceği gerekçesiyle düşen adayı alıntılı bulgularla editöre
  verir; onarım `@onarim: <ebeveyn sha1>` taşıyan yeni adaydır, deneme ebeveyn + 1, en çok 3 (2 onarım turu), K9
  ebeveyni ve reddedilenleri havuza almaz, hakemler bulguları görmez. `kontrol --ad` artık varsayılan olarak
  dosyanın data/<ad>/aday/ klasöründen gelir (önceden urun_v1'di ve istemdeki komutta `--ad` yoktu; urun_v1
  dışındaki bir adda yama sayacı ve K9 kabul havuzu yanlış klasörden okunabilirdi) ve istemler `--ad` ile yazılır. İlk koşu: `onar-istemi urun_v2 --hepsi` 11 istem,
  81 hikâye (21'i M3 yeniden yazımı); 9 aday kod kapısı gerekçesiyle (Pepee) yeni yazıma kalır.
- Kural çatışması ve aşırı katı maddeler (kullanıcı yetkisiyle karar): 'ders' kapanışı 'bundan sonra' ile biten
  son cümleye izin veriyordu ama HAKEM_M M8 (tek zaman) onu reddediyordu; M8 artık son cümle olan tek bir ders
  cümlesinde 'bundan sonra' / 'artık'a izin verir, hikâyenin içinde zaman atlaması yine M8'dir. HAKEM_D D6:
  çocuğun bildiği yaygın kelimeler ve basit benzetmeler ('top gibi') D6 değildir; yalnız deyim, gerçek mecaz ve
  soyut isim sayılır; 'keşif/keşfetmek' sınırdadır ve kılavuz ile tema tanımı 'bulmak' der (taklit oyununda 'kaşif'
  yerine 'bahçıvan'). HAKEM_M M6: yere doğal olarak ait yaygın nesne (kumsalda şemsiye, denizde kova) önceden
  kurulmadan kullanılabilir. 'Emin değilsen var de' yalnız M6, D6 ve D7'den kalktı (bunlar yalnız eminken
  işaretlenir); güvenlik, dünya ve dilbilgisi maddelerinde kalır. HAKEM dosyaları kapı sürümüne girdiğinden
  (K11) bütün adaylar için `kapi` yeniden koşulmalı; önceki kabuller o zamana dek 'kapi_surumu_eski' bekler.
- Hakemler yumuşatılmaz (kullanıcı isteği): M6, D6 ve D7'deki gevşetme ile bu maddelerden 'emin değilsen var de'nin
  kaldırılması geri alındı. Yalnız M8'deki son 'ders' cümlesi istisnası kalır; o kendi kapanış kuralımızla çelişkiyi
  giderir. Doğru bulunan her kusur onarılır ve hikâye yeni hakemlerden yeniden geçer; onarım tavanı 6 deneme
  (en çok 5 onarım turu). Aynı döngü bütün üretim verisine uygulanır.

- **Şakir 'macera' özelliği yeni yazımdan çıkarıldı (tur 12, hakemler değişmedi).** Kart bu özellik için
  hikâyede "macera" kelimesini zorunlu kılıyor, dil hakemleri ise bu kelimeyi 3-6 yaş için soyut buluyor (D6).
  Şakir'in 180 D6 bulgusunun 132'si "macera" alıntılı; kod kapısı ile hakem birbirine ters düşüyordu.
  `yaz-istemi --ozellik-haric macera` ile Şakir'in yeni tohumları yalnız somut "şapka" özelliğinden seçilir;
  kart ve hakem yönergeleri aynen kaldı. Yazar istemine ayrıca "tohumdaki özellik çözümü doğuran somut bir
  eylem olmalı" kuralı eklendi (Elsa ve Hello Kitty'de K2 ret oranı %37'ydi).
