"""data/canli_rol.json ve data/tohum_kelimeleri.json: elle etiketlenmiş listeler (KUSURSUZ_VERI.md Adım 0b-c),
sade sözlüğün sık kök listesine karşı denetlenip yazılır. Sözlük yeniden üretilince (sade_sozluk.py olustur) bu
betik koşulur; yeni sık köklerin etiketi buraya elle eklenir.

Kullanım: .venv/bin/python degerlendirme/tohum_etiket.py          # denetim: sık listede olmayan ya da çift kelime
          .venv/bin/python degerlendirme/tohum_etiket.py --yaz    # iki JSON'u yazar (sha256'lı)
"""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "degerlendirme"))
import sade_sozluk as S
Z = S.yukle()
SIK = Z.d["sik"]
SIKS = set(SIK)
KOK = Z.d["kok"]

def ayir(s):
    return [w for w in s.split() if w]

# ------------------------------------------------------------------ canlı (hayvan ve yaratık)
HAYVAN = ayir("""
kuş köpek kedi ayı tavşan balık kelebek hayvan böcek sincap kurbağa fare ördek aslan maymun fil tilki baykuş arı at
karınca yavru kaplumbağa örümcek inek tavuk kurt yengeç yılan koyun tırtıl geyik kaplan timsah solucan güvercin
dinozor kuğu zürafa karga kaz domuz keçi papağan boğa ahtapot köstebek köpekbalığı goril kertenkele zebra penguen fok
hindi kartal kanguru karides civciv çekirge pire leopar martı devekuşu eşek gergedan turna sivrisinek salyangoz kuzu
kirpi midilli serçe domuzcuk kedicik farecik denizanası istiridye balina yunus sinek katır panda samur porsuk kunduz
rakun kokarca ceylan karaca lama deve hipopotam çita jaguar vaşak sırtlan çakal şempanze orangutan öküz dana buzağı
manda oğlak teke koç horoz kumru bülbül kanarya saksağan leylek flamingo pelikan şahin atmaca akbaba kırlangıç
ağaçkakan sinekkuşu tavuskuşu mors denizyıldızı istakoz midye alabalık hamsi somon bukalemun iguana eşekarısı
ateşböceği akrep yarasa sıçan hamster sansar enik tay sıpa kuzucuk köpekçik tavşancık kuşçuk yavrucuk pony kene
denizatı ayıbalığı tırtılcık kelebekçik sümüklüböcek uğurböceği yusufçuk aygır""")
YARATIK = ayir("""canavar peri ejderha cadı hayalet melek cin uzaylı yaratık cüce unicorn vampir trol goblin elf zombi
denizkızı mumya""")

# ------------------------------------------------------------------ rol (akrabalık, insan, meslek, unvan)
AILE = ayir("""anne baba kardeş dede büyükanne babaanne anneanne abla abi ağabey amca teyze nine nene oğul kız torun
ikiz büyükbaba evlat aile dayı yenge enişte kuzen yeğen eş karı ebeveyn akraba""")
INSAN = ayir("""adam kadın çocuk insan kişi oğlan arkadaş dost komşu misafir kahraman öğrenci köylü erkek bay bayan
hanım hanımefendi beyefendi turist gezgin dilenci""")
MESLEK = ayir("""doktor polis kral prenses prens kraliçe çiftçi palyaço itfaiyeci veteriner asker şoför korsan bekçi
dondurmacı oyuncakçı avcı tamirci berber hırsız hemşire pilot postacı balıkçı denizci şövalye sihirbaz ressam aşçı
satıcı garson kuaför müzisyen dansçı şarkıcı büyücü avukat kamyoncu oyuncu görevli memur öğretmen kaptan bahçıvan
temizlikçi kaşif fırıncı pastacı manav kasap simitçi eczacı dişçi mühendis astronot terzi marangoz çoban oduncu
madenci cankurtaran rehber şef patron işçi müdür hakem antrenör padişah sultan vezir hakim yargıç kütüphaneci
taksici sürücü kapıcı bilim_insanı kovboy savaşçı lider hizmetçi müşteri yetişkin yolcu hekim ebe efe makinist
balerin değirmenci pizzacı şekerci kitapçı yarışmacı seyirci sanatçı düşman""")

BELIRSIZ = {
    "bebek": ("rol", "insan bebek / oyuncak bebek"),
    "hala": ("rol", "babanın kız kardeşi / 'hâlâ'nın şapkasız yazımı (tr-tinystories'te çoğunlukla 'hâlâ' anlamında)"),
    "koca": ("rol", "eş / 'koca bir' (büyük) sıfatı; 'Koca Ayı' Maşa kartında yan adı"),
    "ayıcık": ("canli", "oyuncak ayı / yavru ayı"),
    "robot": ("canli", "oyuncak robot / konuşan karakter"),
    "dev": ("canli", "masal devi / 'dev bir' (çok büyük) sıfatı"),
    "yabancı": ("rol", "tanımadık kişi / 'yabancı' sıfatı"),
    "biri": ("rol", "belgisiz zamir: 'biri geldi' yeni karakter, 'ikisinden biri' değil"),
    "birisi": ("rol", "belgisiz zamir, yeni karakter getirebilir"),
    "sevgili": ("rol", "hitap ('sevgili arkadaşım') / kişi"),
    "genç": ("rol", "genç kişi / sıfat"),
    "yaşlı": ("rol", "yaşlı kişi / sıfat ('yaşlı ağaç')"),
    "usta": ("rol", "meslek sahibi / 'usta' sıfatı"),
    "bilge": ("rol", "bilge kişi (Doru kartında Kırat 'bilge at') / sıfat"),
    "bakkal": ("rol", "dükkan / dükkancı; Rafadan Tayfa'da Kamil'in ailesinin bakkalı"),
    "yazar": ("rol", "meslek / 'yazar' (yazmak, geniş zaman)"),
    "yardımcı": ("rol", "yardımcı kişi / 'yardımcı oldu' deyimi"),
    "gelincik": ("canli", "hayvan / çiçek; Doru kartında küçük bir kuşun adı"),
    "palamut": ("canli", "balık / meşe palamudu (sincap hikâyelerinde çoğunlukla meyve)"),
    "yaban": ("canli", "'yaban arısı', 'yaban domuzu' / 'yaban mersini' (meyve)"),
    "sürü": ("canli", "hayvan topluluğu: tek tek canlı değil ama yeni canlılar getirir"),
    "kalabalık": ("rol", "insan topluluğu / 'kalabalık' sıfatı"),
    "halk": ("rol", "topluluk"),
    "grup": ("rol", "topluluk"),
    "takım": ("rol", "oyuncu topluluğu / eşya takımı"),
    "cırcır": ("canli", "'cırcır böceği' / ses yansıması"),
}
# Kullanıcı kararı (KUSURSUZ_VERI.md 'Kullanıcı kararları' 2): belirsiz kelimeler KARAKTER (canlı, konuşan, rol) olarak
# yasaktır; yalnız cansız/oyuncak anlamı açıkça yazılırsa geçer. K4 şu durumlarda kelimeyi cansız sayar (K merceğine
# not gider): önündeki iki kelimede 'oyuncak' var, kelimenin hemen ardından canlı/rol ismi geliyor (sıfat: 'bilge
# kaplumbağa', 'yaşlı at'; o isim ayrıca denetlenir) ya da aşağıdaki nesne kalıplarından biri o geçişi kapsıyor.
# Öteki her geçiş K4.belirsiz retidir. Kalıplar küçük harfli metne uygulanır (Python re).
NESNE_KALIPLARI = {
    "koca": [r"\bkoca\s+(?:bir|koca)\b"],
    "dev": [r"\bdev\s+(?:bir|gibi)\b"],
    "biri": [r"\b\w+(?:dan|den|tan|ten)\s+biri\w*", r"\bher\s+biri\w*"],
    "birisi": [r"\b\w+(?:dan|den|tan|ten)\s+birisi\w*"],
    "genç": [r"\bgenç\s+bir\b", r"\bgenç(?:ti|tir|miş)\b"],
    "yaşlı": [r"\byaşlı\s+bir\b", r"\byaşlı(?:ydı|dır|ymış)\b"],
    "bilge": [r"\bbilge\s+bir\b", r"\bbilge(?:ydi|dir|ymiş|ce)\b"],
    "usta": [r"\busta\s+bir\b", r"\busta(?:ydı|dır)\b"],
    "kalabalık": [r"\bkalabalık\s+bir\b", r"\bkalabalık(?:tı|tır)\b"],
    "yardımcı": [r"\byardımcı\s+ol\w*"],
    "gelincik": [r"\bgelincik\s+çiçe\w*"],
    "palamut": [r"\bmeşe\s+palamu\w*"],
    "yaban": [r"\byaban\s+mersin\w*"],
    "sürü": [r"\bbir\s+sürü\b"],
    "takım": [r"\btakım\s+elbise\w*", r"\b(?:çay|boya|kalem|oyun)\s+takım\w*"],
}
assert set(NESNE_KALIPLARI) <= set(BELIRSIZ)
# Temel figür türleri ve kartlarda yan olarak geçen türler canli listesinde kalır; kapi.py bunları tohumdaki yanla eşler.

# ------------------------------------------------------------------ tohum: somut isimler
ISIM = ayir("""
top oyuncak araba çiçek su kutu taş kapı resim kitap yaprak elma salıncak yatak kek kaydırak elbise dondurma şeker
kurabiye para kamyon yuva meyve ip balon şapka masa tekne kar yıldız pasta dal kalem boya bisiklet kum kağıt uçak tüy
pencere gemi çanta yiyecek tren havuç ekmek blok sandviç hediye bulut çikolata çorba kabuk anahtar mektup yumurta
gökkuşağı bal fındık süt hazine sepet uçurtma peynir telefon ayakkabı sandalye battaniye şişe çubuk kavanoz muz sebze
çimen tekerlek kolye düğme domates bardak tabak ot mısır çilek koltuk kaşık limon çöp vazo yastık fotoğraf buz
halı bez hamur defter ayna un pizza raf davul şemsiye hortum gitar çit kova bant eldiven çuval çalı değnek sabun fıstık
lamba buzdolabı mama kupa ceket biber bayrak portakal salata üzüm çorap elmas patates tabela kase taç armut köpük
kurdele makarna kart fırça yapboz baloncuk soğan zeytin boru küp lolipop çadır reçel paket sakız havlu çan kiraz
çamaşır bileklik bilgisayar pantolon fener kilit kristal piyano balkabağı eşarp kürek flüt sos kabak fermuar tasma
tişört şeftali yapıştırıcı düdük odun cüzdan zarf pul fasulye kostüm kemer silgi çatal kavun mıknatıs tereyağı kazak
musluk kütük keman spagetti yüzük radyo kayık maske turp krem ayçiçeği sosis çember mücevher etek misket papatya
limonata scooter waffle gözlük bavul zil gazete trompet börek kaktüs avokado buğday zincir kök perde karnabahar kask
dergi kıyafet inci yem tuz erik mikrofon tost tuğla kapak madalya pilav damla teker yoğurt yelek kereviz çerçeve
yelken içecek takvim fincan nane kravat yulaf bluz kumaş yün karton yağ salatalık çarşaf sayfa çekmece gevrek baston
bulmaca kırıntı köfte dilim tarak testi saman jöle muffin tepsi askı peçete etiket bornoz tebeşir ceviz şampuan bot
şekerleme paspas pirinç mont bisküvi bilezik süpürge torba krema böğürtlen poşet karpuz topaç palto giysi pankek
saksı mendil kakao pastel boncuk kumbara önlük bilye külah çıkartma klasör tüp mercan menekşe çakıl kadife pijama
atkı koza kızartma üniforma biftek cips traktör koni cetvel baharat fidan marul zambak filiz ağaç kaya toprak çamur
tahta bitki tohum güneş ay yağmur rüzgar sis dalga gölge toz altın gümüş kozalak meşe çam harita heykel televizyon
saat delik dolap kanepe beşik duvar çeşme yemek kemik gül bulaşık leke satranç dosya kamera mikroskop bilet halka
gömlek kitaplık lastik iplik düğüm pedal toka ruj parfüm çim direk kaymak brokoli sofra kasa damga süs demet mürekkep
terazi tartı gardırop alet posta
sürahi kalıp pelerin yosun poğaça örtü yelpaze minder palmiye çekirdek tomurcuk file yama nota davetiye küpe patik
fiyonk kaykay çörek bambu kartopu kepçe teneke örgü tutkal pota kızak yorgan fıçı forma lokma başörtüsü tablo bağcık
mayo yağmurluk nilüfer kraker şal halat lale simit sünger yonca tahterevalli fıskiye turşu tabure şort valiz petek
vanilya sucuk jelibon patlıcan buket ipek fide bezelye çömlek basamak şerit sabahlık mobilya vagon yelkenli kamyonet
minibüs plak teyp teleskop hamburger mermer dolma kebap karabiber kese iz
""")

# ------------------------------------------------------------------ tohum: fiiller (sık listedeki kök biçimi)
FIIL = ayir("""
oyna- gör- git- gel- al- yap- gülümse- bak- başla- ver- koş- bul- sor- gül- eğlen- çık- ye- dön- söyle- parla- aç-
yürü- uç- çalış- koy- zıpla- at- dinle- sarıl- topla- otur- uyu- izle- kal- çıkar- göster- gir- geç- öğren- ara-
dur- tut- konuş- yaklaş- yakala- götür- salla- duy- anlat- getir- paylaş- sallan- tak- bekle- bin- oku- görün-
kay- öğret- büyü- sür- dene- çiz- bit- yorul- kırıl- dokun- bırak- temizle- kullan- iç- kaç- çek- kalk- in- uyan-
yaz- kapat- saklan- giy- yağ- koru- yıka- taşı- dol- gez- ayrıl- dolaş- kaybet- havla- dinlen- buluş- kazan- çağır-
kaldır- sakla- acık- kurtar- şakı- bitir- hazırla- öp- açıl- kok- kon- say- yuvarlan- uzaklaş- atla- karıştır-
es- yarış- koştur- takıl- seslen- yat- uzat- bas- tanış- düşür- okşa- boya- keşfet- uzan- kokla- öt- çırp-
ak- seç- incele- belir- fırlat- kur- uçuş- doy- yapıştır- dök- ekle- değiş- doldur- eğil- çevir- sil- kucakla-
süzül- uçur- kurtul- sar- bağla- alkışla- ıslan- sula- süsle- diz- sat- kapan- ölç- miyavla- katla- değ- kuru-
küçül- susa- parılda- hazırlan- ilerle- sıkış- düzelt- güneşlen- cevapla- indir- toplan- koşuştur- yayıl- biriktir-
zıplat- gönder- tat- yuvarla- seyret- dökül- doyur- fırçala- temizlen- kopar- dağıl- düzenle- düzel- üfle-
birleştir- mırıldan- gezin- durdur- vedalaş- besle- çöz- ayır- yerleştir- karış- yırtıl- gülüş- fısılda- gezdir-
karşılaş- sıçra- ısın- çekil- tutun- yavaşla- ek- güldür- yapış- kurut- tara- güzelleş- süpür- havalan- cıvılda-
çiğne- kutla- güzelleştir- sıçrat- taşın- ör- parlat- kurula- kavuş- yarat- dağıt- giyin- çalıştır- yıkan- kapa-
gurulda- yala- karşıla- kırp- serp- anlaş- ört- büyüt- kıpırda- tamamla- kaydet- ıslat- yaklaştır- tart- oynat-
aydınlat- kilitle- sığın- kemir- şişir- yetiştir- korun- yardımlaş- eşleştir- somurt- homurdan- serinle-
dik- as- sık- asıl- doğ- eri- soğu- bozul- kop- uza- din- taş- devir- yankılan- görüş-
sev- sevin- şaşır- düşün- anla- unut- beğen- hatırla- özle- hoşlan- utan- sıkıl- rahatla- sakinleş- heyecanlan-
sabırsızlan- güven- üzül- dile- ulaş- yüksel- değiştir- çekin- sus- döndür- öde- böl- sığ- yoğur- yetiş- alış-
yumuşa- saç- kapla- buruştur- dolan- sokul- bindir- oturt- giydir- yatır- uzaklaştır- kat- sol- hızlan- eğ- aş-
savur- katıl- affet- tanı- yakalan- tamamlan- ilgilen- kaz- inan- rahatlat-
esne- uyandır- damla- daya- yedir- birleş- olgunlaş- dalgalan- küçült- ov- yay- bük- aydınlan- kıvrıl- yükle- yerleş-
fışkır- sarar- uyut- sırala- ovuştur- barış- süslen- silk- savrul- şaşırt- eğlendir- hopla- tasarla- yolla- boşal-
yeşer- gizlen- yaslan- ışılda- kurulan- şekillendir- gıdıkla- kirlet- planla- boşalt- paketle- çoğal- sektir- gerin-
işaretle- eşele- sun- tanıştır- serinlet- selamla- çözül- yeşillen- birik- köpür- kıvır- şakalaş- sergile- tekrarla-
kabar- sürt-
""")

# ------------------------------------------------------------------ tohum: sıfatlar
SIFAT = ayir("""
güzel mutlu küçük büyük iyi yeni kırmızı kocaman mavi üzgün hızlı dikkatli yavaş sarı uzun renkli yeşil tatlı eski
eğlenceli parlak sıcak pembe minik sihirli lezzetli farklı dolu yüksek özel zor cesur uzak güçlü heyecanlı nazik
harika beyaz rengarenk yorgun yumuşak temiz soğuk hazır yakın sevimli mor güneşli komik siyah garip meraklı tüylü
kahverengi ağır turuncu yuvarlak gri rahat güvenli gizli dağınık açık düzenli zeki sağlıklı değerli şanslı kirli sert
kolay çikolatalı kısa sakin utangaç ilginç neşeli sıcacık sabırlı pahalı kapalı ıslak yumuşacık tertemiz uslu
küçücük kalın ekşi gururlu kuru mutsuz sağlam serin çilekli tuhaf büyülü ince keyifli yardımsever gizemli yemyeşil
sıkı masmavi yağmurlu çalışkan taze mükemmel bol tozlu sevinçli sakar kilitli huzurlu havalı bozuk gürültülü hafif
basit kibar bembeyaz enerjik ahşap esnek yetenekli narin paslı plastik yaratıcı yırtık yeterli eksik hareketli sadık
karışık geniş berrak çizgili kaygan yamuk şık rüzgarlı yepyeni düzgün süslü sulu kokulu hareketsiz boş akıllı
sessiz çamurlu dürüst ucuz vanilyalı yalnız memnun çabuk kırık şaşkın sırılsıklam çıtır
cömert incecik sevecen çekingen saygılı çiçekli dalgalı düz benekli ılık şirin şeffaf faydalı ufak minicik meşgul
tuzlu sabırsız düşünceli bomboş aceleci sisli pürüzsüz yapışkan zarif kırılgan kararlı boyalı buzlu uykulu kıpkırmızı
şapkalı bilgili değişik hazırlıklı tekerlekli dar karmakarışık saklı aydınlık bulutlu kabarık ışıltılı meyveli resimli
limonlu kızıl temkinli puantiyeli patlak şekerli kıvrımlı umutlu soslu çevik reçelli ferah hevesli uyanık oynak işaretli
yapraklı nefis biberli peynirli elmalı kremalı sabunlu simsiyah koyu devasa konuşkan eskimiş tedbirli somurtkan
""")

# ------------------------------------------------------------------ tohum: dünya kategorileri (Adım 3; kartın
# 'tohum_yasak_kategoriler' alanı). Tohum kelimesi kartın dünyasında olmayan bir eşya getirmesin: kaplumbağanın
# ormanında telefon, Keloğlan'ın köyünde pizza yok. Etiketsiz kelime her dünyaya uyar (doğa, oyuncak, yiyecek...).
KATEGORI = {
    "teknoloji": """telefon bilgisayar televizyon radyo mikrofon kamera mikroskop teleskop teyp plak buzdolabı musluk
                    hortum mıknatıs tüp""",
    "cagdas_arac": "araba kamyon tren uçak traktör bisiklet scooter kaykay vagon kamyonet minibüs",
    "arac": "gemi tekne kayık yelken yelkenli kızak tekerlek teker pedal lastik",
    "cagdas": """pizza spagetti waffle pankek muffin cips hamburger sosis sucuk tost lolipop sakız jelibon kraker
                 makarna kakao sandviç çikolata gazete dergi bilet para cüzdan kumbara pul posta fotoğraf klasör dosya
                 fermuar tişört şort kask ruj parfüm şampuan krem çıkartma yapıştırıcı bant poşet kravat üniforma
                 pijama bornoz sabahlık mont kostüm valiz bavul yapboz tabela pastel madalya forma pota kaydırak piyano
                 tahterevalli""",
    "ev_esyasi": """yatak koltuk kanepe sandalye masa dolap gardırop çekmece raf kitaplık halı perde beşik yastık
                    battaniye yorgan minder tabure lamba ayna vazo çerçeve tablo çarşaf havlu paspas süpürge çamaşır
                    bulaşık sofra mobilya kapı pencere duvar saat kilit anahtar zil heykel askı kasa terazi
                    tartı saksı tuğla boru direk mermer tutkal zincir sabun sünger tarak mendil fıskiye""",
    "mutfak": """tabak çatal kaşık bardak fincan kase tepsi kupa sürahi kepçe peçete kavanoz şişe testi çömlek fıçı
                 teneke biftek köfte kebap kızartma dolma pilav börek çorba""",
    "giysi": """elbise şapka ceket kazak atkı eldiven çorap ayakkabı etek gömlek pantolon yelek kemer önlük eşarp bluz
                palto bot pelerin şal başörtüsü mayo yağmurluk patik kıyafet giysi kolye bileklik bilezik yüzük küpe
                toka taç fiyonk kurdele maske gözlük çanta mücevher inci elmas kristal kumaş ipek kadife""",
    "hazir_yiyecek": """reçel bisküvi çörek dondurma ekmek gevrek hamur jöle kaymak kek krema kurabiye limonata pasta
                        peynir poğaça salata simit sos süt şeker şekerleme tereyağı turşu tuz un yağ yemek yoğurt
                        içecek baharat karabiber vanilya reçelli çikolatalı kremalı peynirli soslu vanilyalı şekerli
                        biberli limonlu sabunlu""",
    "bostan": """patlıcan soğan fasulye bezelye brokoli karnabahar kereviz marul patates domates salatalık turp biber
                 sebze avokado muz limon portakal karpuz kavun mısır pirinç yulaf""",
    "calgi": "davul düdük flüt gitar keman trompet",
    "buyu": "büyülü sihirli",
    "okul": """kitap defter kalem silgi cetvel tebeşir sayfa harita takvim bulmaca mektup zarf mürekkep damga boya
               fırça kart etiket kağıt karton nota davetiye satranç""",
}
# Kelime yalnız bu canlılardan biri figürün türü ya da tohumdaki bir yanın türüyse seçilir (tasma köpek getirir).
CANLI_GEREKTIRIR = {
    "tasma": ["köpek"], "kemik": ["köpek"], "mama": ["köpek", "kedi"], "yem": ["kuş", "at", "keçi", "tavşan", "balık"],
    "yuva": ["kuş", "baykuş", "sincap", "kirpi", "tavşan", "fare"], "petek": ["arı"],
    "havla-": ["köpek"], "miyavla-": ["kedi"], "öt-": ["kuş", "baykuş"], "cıvılda-": ["kuş"],
    "kemir-": ["fare", "sincap", "tavşan"], "eşele-": ["köpek", "kedi", "tavuk"],
}




def denetle(ad, liste, sik_sart=True):
    goruldu, eksik, cift = [], [], []
    for w in liste:
        w = w.replace("_", " ")
        if w in goruldu:
            cift.append(w); continue
        goruldu.append(w)
        k = w if w.endswith("-") else Z.kok(w)
        if sik_sart and w not in SIKS:
            eksik.append((w, k, k in SIKS, KOK.get(k)))
    print(f"{ad}: {len(goruldu)} kelime; çift: {cift}; sık listede yok: {len(eksik)}")
    for e in eksik:
        print("   ", e)
    return goruldu



if __name__ == "__main__":
    for ad, l in (("HAYVAN", HAYVAN), ("YARATIK", YARATIK), ("AILE", AILE), ("INSAN", INSAN), ("MESLEK", MESLEK),
                  ("ISIM", ISIM), ("FIIL", FIIL), ("SIFAT", SIFAT)):
        denetle(ad, l, sik_sart=ad in ("ISIM", "FIIL", "SIFAT"))


def tekil(l):
    return list(dict.fromkeys(w.replace("_", " ") for w in l))


def tr_sirala(l):
    return sorted(l, key=S.tr_anahtar)


def mastar(k):
    g = k.rstrip("-")
    son = [h for h in g if h in "aeıioöuü"][-1]
    return g + ("mak" if son in "aıou" else "mek")


def yaz(yol, d):
    d["sha256"] = S.icerik_sha256(d)
    with open(yol, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("yazıldı:", yol, d["sha256"][:12])


def kaynak():
    return {"sade_sozluk": "data/sade_sozluk.json", "sade_sozluk_sha256": Z.d["sha256"],
            "sik_txt_sha256": Z.d["sik_txt_sha256"], "kok_yontemi": Z.d["kok_yontemi"]}


def uret():
    canli, rol, sik_disi = {}, {}, {}
    for tur, liste, hedef in (("hayvan", HAYVAN, canli), ("yaratık", YARATIK, canli), ("aile", AILE, rol),
                              ("insan", INSAN, rol), ("meslek/unvan", MESLEK, rol)):
        for w in tekil(liste):
            hedef[w] = tur
            if w not in SIKS:
                sik_disi[w] = Z.tf.get(w, 0)                  # yalın biçimin yüzey sıklığı (0: 5'ten az)
    belirsiz = {w: {"aday": a, "neden": n, "nesne_kaliplari": NESNE_KALIPLARI.get(w, [])}
                for w, (a, n) in BELIRSIZ.items()}
    assert not set(belirsiz) & (set(canli) | set(rol))
    etiketlenen = set(canli) | set(rol) | set(belirsiz)
    cr = {
        "aciklama": "K4 kapalı dünya listesi (KUSURSUZ_VERI.md Adım 0b). Sade sözlüğün sık kök listesindeki (data/"
                    "sade_sozluk_sik.txt) canlı ve rol kökleri elle etiketlendi; ayrıca sık liste dışındaki bilinen hayvan, "
                    "yaratık, akrabalık ve meslek adları eklendi (sik_disinda: yalın biçimin tr-tinystories sıklığı; 0 = "
                    "5'ten az ya da iki kelime). Metinde bu lemmaların TEKİL biçimi {figürün türü} ∪ {tohumdaki "
                    "yanların yüzey biçimleri} dışında geçerse K4 reddeder; çoğul biçim (kuşlar) arka plandır, K "
                    "merceğine not gider. belirsiz: anlamı bağlama göre canlı/rol olan ya da olmayan kelimeler. "
                    "Kullanıcı kararı: KARAKTER (canlı, konuşan, rol) olarak yasak; K4 bunları reddeder, yalnız cansız ya "
                    "da oyuncak anlamı açıksa geçirir ve K merceğine not yollar: önünde 'oyuncak' var, ardından canlı/rol "
                    "ismi geliyor (sıfat: 'yaşlı at') ya da 'nesne_kaliplari'ndan biri geçişi kapsıyor ('bir sürü', "
                    "'meşe palamudu'). Değişirse K4 bütün kabullere yeniden koşulur (sürüm: sha256).",
        "surum": 2,
        "kaynak": kaynak(),
        "canli": dict(sorted(canli.items(), key=lambda kv: S.tr_anahtar(kv[0]))),
        "rol": dict(sorted(rol.items(), key=lambda kv: S.tr_anahtar(kv[0]))),
        "belirsiz": dict(sorted(belirsiz.items(), key=lambda kv: S.tr_anahtar(kv[0]))),
        "sik_disinda": dict(sorted(sik_disi.items(), key=lambda kv: S.tr_anahtar(kv[0]))),
        "sayilar": {"canli": len(canli), "rol": len(rol), "belirsiz": len(belirsiz),
                    "sik_listeden": sum(1 for w in etiketlenen if w in SIKS), "sik_disinda": len(sik_disi)},
    }
    yaz(ROOT + "/data/canli_rol.json", cr)

    isim, fiil, sifat = tekil(ISIM), tekil(FIIL), tekil(SIFAT)
    for l in (isim, fiil, sifat):
        assert all(w in SIKS for w in l), [w for w in l if w not in SIKS]
        assert not set(l) & etiketlenen, set(l) & etiketlenen
    kategori = {k: tr_sirala(tekil(ayir(v))) for k, v in KATEGORI.items()}
    for k, v in kategori.items():
        assert set(v) <= set(isim) | set(sifat), (k, set(v) - set(isim) - set(sifat))   # sıfat da olabilir (reçelli)
    tum = [w for v in kategori.values() for w in v]
    assert len(tum) == len(set(tum)), "bir kelime tek kategoride olur"
    for w, cs in CANLI_GEREKTIRIR.items():
        assert w in isim + fiil + sifat and all(c in canli for c in cs), (w, cs)
    tk = {
        "aciklama": "Tohum kelimeleri (KUSURSUZ_VERI.md Adım 0c ve 3): her tohuma buradan rastgele 1 isim + 1 fiil + 1 "
                    "sıfat. Hepsi sade sözlüğün sık kök listesinden (fiiller o listedeki gibi '-' ile; fiil_mastar yazara "
                    "gösterilecek biçim). Çıkarılanlar: canlı ve rol isimleri (data/canli_rol.json, belirsizler dahil); "
                    "soyut isimler; yer ve yapı isimleri (tek sahne kuralı: tohum kelimesi sahneyi taşımasın); vücut "
                    "parçaları (yaralanma/hastalık kalıpları, K7); tehlikeli ya da korkutucu nesneler (bıçak, makas, "
                    "kibrit, mum, ateş, ilaç, tabanca...); olay ve etkinlik adları (parti, piknik); fiillerde yardımcı "
                    "ve çok genel fiiller (ol-, et-, de-, iste-), K7 hastalık/yaralanma, şiddet, yıkım, ateş/ısı, derin "
                    "su ve yükseğe tırmanma fiilleri (kork-, düş-, tırman-, yüz-, dal-, yak-, kes-, vur-...); sıfatlarda "
                    "korkutucu, tehlikeli, vücut ve alay edilebilir özellik sıfatları (korkunç, keskin, şişman, çirkin...). "
                    "kategori: dünya kategorisi -> isimler; kartın 'tohum_yasak_kategoriler' alanındaki kategorilerin "
                    "kelimeleri o figürün tohumuna gelmez (kartın kendi metninde geçen kelime hariç). canli_gerektirir: "
                    "kelime -> canlılar; kelime yalnız bunlardan biri figürün türü ya da tohumdaki bir yanın türüyse "
                    "seçilir (tasma köpek, havlamak köpek getirir).",
        "surum": 2,
        "kaynak": kaynak() | {"canli_rol_sha256": cr["sha256"]},
        "isim": tr_sirala(isim),
        "fiil": tr_sirala(fiil),
        "fiil_mastar": {k: mastar(k) for k in tr_sirala(fiil)},
        "sifat": tr_sirala(sifat),
        "kategori": kategori,
        "canli_gerektirir": dict(sorted(CANLI_GEREKTIRIR.items(), key=lambda kv: S.tr_anahtar(kv[0]))),
        "sayilar": {"isim": len(isim), "fiil": len(fiil), "sifat": len(sifat),
                    "hedef": {"isim": 600, "fiil": 400, "sifat": 200}},
    }
    yaz(ROOT + "/data/tohum_kelimeleri.json", tk)


if __name__ == "__main__" and "--yaz" in sys.argv:
    uret()
