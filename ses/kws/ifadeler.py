"""Anahtar sözcük sınıfları ve ifade listeleri (docs/URUN_TANIMI.md tablosu + çocuk söyleyişleri).

Sınıf sırası modelin çıkışlarıdır; C tarafındaki KWS_* sırası (kws.h) UYANDIRMA'dan başlayarak aynıdır:
  sınıf 0 ARKA     : sessizlik, gürültü, hoparlörden gelen hikâye sesi (arka plan)
  sınıf 1 KONUSMA  : ön planda anahtar olmayan konuşma (bilinmeyen sözcük/cümle, "Eko" tek başına, "Merhaba" ...)
  sınıf 2.. 8      : UYANDIRMA, DUR, DEVAM, BASKA, BIR_DAHA, SESI_AC, SESI_KIS  (KWS_* = sınıf - 1)

Uyku sesli komutla DEĞİL, gece figürüyle açılır (ürün tanımı değişikliği, 13 Ekim 2026): eski UYKU ifadeleri
("Uykum geldi", "İyi geceler") artık yalnız olumsuz örnek (KONUSMA). Sentez iş listesi değişmesin (yarıda kalan
sentez aynı kimliklerle sürsün) diye SENTEZ_EK'te aynı sayıda sentezlenir; veri.py bunları olumsuz havuza koyar.

"egitim" listeleri eğitimde, "deneme" listeleri yalnız sınamada (görülmemiş çocuk söyleyişleri) kullanılır;
asıl tablo ifadeleri ikisinde de vardır (sınama başka seslerle yapılır).

Komut sözcükleri uzun konuşmanın içinde (ör. hikâyede "başka bir gün") komut sayılmaz: model yalnız kendi başına
söylenmiş (önünde sessizlik ya da "Merhaba Eko" olan) kısa ifadeleri komut diye öğrenir; ayrıca kart komutları
yalnız uyandırmadan sonraki ~4 sn içinde kabul eder.
"""

SINIFLAR = ["ARKA", "KONUSMA", "UYANDIRMA", "DUR", "DEVAM", "BASKA", "BIR_DAHA", "SESI_AC", "SESI_KIS"]
SINIF_NO = {s: i for i, s in enumerate(SINIFLAR)}

POZITIF = {
    "UYANDIRMA": {
        "egitim": ["Merhaba Eko", "Merhaba, Eko", "Melhaba Eko", "Meraba Eko", "Merhaba Ekoo", "Merhaba Ekooo",
                   "Meaba Eko", "Melhaba Ekko", "Merhabaa Eko", "Mehaba Eko", "Melaba Eko", "Merhaba Ekko",
                   "Meyhaba Eko", "Merabaa Ekoo", "Merhaba Eekoo", "Melhaba, Eko", "Merhaba Eko Eko"],
        "deneme": ["Merhaba Eko", "Melhaba Eko", "Meraba Eko", "Merhaba Ekoo",
                   "Melhabaa Ekoo", "Mehhaba Ekko", "Meraaba Eko", "Meaba Ekoo"],
    },
    "DUR": {
        "egitim": ["Dur", "Durr", "Duur", "Dul", "Dursun", "Dulsun", "Dursuun", "Sus", "Suus", "Dur dur",
                   "Sus artık", "Dur artık"],
        "deneme": ["Dur", "Dursun", "Sus", "Duuur", "Susss", "Dulsuun"],
    },
    "DEVAM": {
        "egitim": ["Devam", "Devam et", "Devam ed", "Deam et", "Devaam", "Hadi", "Hadii", "Hadi devam et",
                   "Devam et hadi", "Devam etsin"],
        "deneme": ["Devam", "Devam et", "Hadi", "Devaaam et", "Hadiii"],
    },
    "BASKA": {
        "egitim": ["Başka", "Başkaa", "Baska", "Başka masal", "Başka masal oku", "Başka hikâye", "Bunu sevmedim",
                   "Bunu sevmedimm", "Bunu sevmedim ben", "Ben bunu sevmedim", "Bunu seemedim", "Baska masal"],
        "deneme": ["Başka", "Başka masal", "Bunu sevmedim", "Başka masaal", "Bunu sevmedii"],
    },
    "BIR_DAHA": {
        "egitim": ["Bir daha", "Bi daha", "Bidaha", "Bir daha oku", "Bi daha oku", "Yine", "Yinee", "Yine oku",
                   "Tekrar", "Tekral", "Tekrar oku", "Tekrarr"],
        "deneme": ["Bir daha", "Yine", "Tekrar", "Biii daha", "Tekraal"],
    },
    "SESI_AC": {
        "egitim": ["Sesini aç", "Sesini aaç", "Sesi aç", "Sesini açar mısın", "Sesini aç lütfen", "Yüksek",
                   "Yüksek ses", "Daha yüksek", "Duyamıyorum", "Duyamıyoyum", "Duyamıyolum", "Duyamıyorum ki"],
        "deneme": ["Sesini aç", "Yüksek", "Duyamıyorum", "Sesini açç", "Duyamıyorumm"],
    },
    "SESI_KIS": {
        "egitim": ["Sesini kıs", "Sesini kııs", "Sesi kıs", "Sesini kısar mısın", "Çok yüksek", "Çok yüksek ya",
                   "Çook yüksek", "Yavaş konuş", "Yavaş konuş lütfen", "Yavas konus", "Yavaş konuşş"],
        "deneme": ["Sesini kıs", "Çok yüksek", "Yavaş konuş", "Sesini kısss", "Çok yüksekk"],
    },
}

# Pozitifler gibi sentezlenip OLUMSUZ (KONUSMA) kullanılan ifadeler (eski UYKU komutu).
SENTEZ_EK = {
    "UYKU": {
        "egitim": ["Uykum geldi", "Uykum geldii", "Uykum gedi", "Uykum gelldi", "İyi geceler", "İi geceler",
                   "İyi geseler", "İyi gecelerr", "İyi geceler Eko", "Uykum geldi anne"],
        "deneme": ["Uykum geldi", "İyi geceler", "Uyyykum geldi", "İyi gecelel"],
    },
}

# Karıştırılabilecek (zor) olumsuzlar: kısa ifadeler, KONUSMA sınıfı.
KARISAN = [
    # uyandırmaya benzeyenler: tek sözcük yetmez, başka ad/sözcük olmaz
    "Merhaba", "Merhaba!", "Merhabaa", "Melhaba", "Meraba", "Eko", "Eko!", "Ekoo", "Eko eko", "Hey Eko", "Eko gel",
    "Eko bak", "Eko nerede", "Merhaba anne", "Merhaba baba", "Merhaba Ece", "Merhaba Ekin", "Merhaba Efe",
    "Merhaba Emre", "Merhaba Elif", "Merhaba Ebru", "Merhaba Ekrem", "Merhaba Deniz", "Merhaba arkadaşlar",
    "Merhaba Niloya", "Merhaba Pepee", "Merhaba Maşa", "Merhaba ekip", "Merhabalar", "Ekmek", "Ekim", "Ekin",
    "Ekonomi", "Merak", "Meraklı", "Merdiven", "Mehmet", "Teko", "Deko", "Neko", "Ego", "Ekol", "Selam Eko",
    "Merhaba kedi", "Merhaba Ayşe", "Merhaba Ela",
    # komutlara benzeyenler
    "Durak", "Durum", "Duvar", "Dut", "Su", "Su ver", "Susadım", "Kuş", "Devamlı", "Davul", "Deve",
    "Hadi gidelim", "Hadi gel", "Başkan", "Baş", "Başım ağrıyor", "Kaşık", "Bunu sevdim", "Bunu seviyorum",
    "Bir", "Biraz daha", "Bir tane", "Yeni", "Tekerlek", "Tekne", "Yüzük", "Yürü", "Sesini duydum", "Sesi güzel",
    "Duyuyorum", "Uyku", "Uykum yok", "Uyumayacağım", "İyi", "İyi misin", "İyi günler", "Günaydın", "Yavaş",
    "Çok güzel", "Çok", "Konuş", "Kış", "Kız", "Aç", "Acıktım", "Masal", "Masal oku", "Kitap oku",
]

# Günlük çocuk / ev konuşması (KONUSMA); bir kısmı komut sözcüğü içerir ama akan konuşmadır.
GUNLUK = [
    "Anne su istiyorum.", "Baba bak ne buldum!", "Oyuncağım nerede?", "Gel buraya.", "Tamam.", "Evet.", "Hayır!",
    "Olmaz.", "Peki.", "Neden?", "Bu ne?", "Bilmiyorum.", "Oynayalım mı?", "Ben de istiyorum.", "Acıktım anne.",
    "Bak bak, kuş uçuyor!", "Benim sıram.", "Kardeşim aldı.", "Çizgi film izleyebilir miyim?", "Dışarı çıkalım.",
    "Bugün parka gittik.", "Kedi miyavladı.", "Elimi yıkadım.", "Yemek ne zaman?", "Sarı top benim.",
    "Ayakkabılarımı giydim.", "Anneanne geldi mi?", "Resim yapıyorum.", "Bu çok güzel.", "Kırmızı kalemi ver.",
    "Ben büyüdüm.", "Abla bana bak.", "Hadi gidelim parka.", "Dur bakalım ne olacak.", "Başka bir gün oynarız.",
    "Yine mi yağmur yağıyor?", "Sesini duydum ama gelmedim.", "Bir daha yapmayacağım dedi.", "Çok yüksek bir ağaç.",
    "Yavaş yavaş yürüdük.", "İyi geceler dedi ve uyudu.", "Merhaba dedi tavşan.", "Eko diye bir köpeğim olsa.",
    "Tekrar tekrar baktı.", "Uykum geldi dedi ayıcık.", "Sus pus oturdu.", "Devam ettiler yollarına.",
    "Masal okur musun?", "Bunu kim yaptı?", "Ellerim kirlendi.", "Pijamamı giydim.", "Dişimi fırçaladım.",
    "Anne bak, ben uçuyorum!", "Arabam hızlı gidiyor.", "Kule yaptım, yıkılmasın.", "Bana da ver.",
    "Şimdi ne yapalım?", "Kim geldi?", "Kapıyı aç.", "Işığı kapat.", "Televizyonu aç.", "Pencereyi kapat.",
    "Merhaba, ben geldim.", "Bugün okulda resim yaptık.", "Kuzum benim.", "Aferin sana.", "Hadi yemeğini ye.",
    "Yeter artık, uyu.", "Oyuncakları topla.", "Ne güzel bir gün.", "Elbiseni giy.", "Ayakkabını bağla.",
]


def _kucuk(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


_KOMUT_BASLARI = sorted({_kucuk(p).replace(",", "").split()[0]
                         for k, v in POZITIF.items() if k != "UYANDIRMA" for p in v["egitim"] + v["deneme"]})


def komutla_baslar(metin):
    """Cümle bir komut sözcüğüyle mi başlıyor? (o zaman cümlenin içi etiketlenmez: nedensel model geleceği bilemez)"""
    s = _kucuk(metin).lstrip("\"“'- ")
    ilk = "".join(ch for ch in s.split()[0] if ch.isalpha()) if s.split() else ""
    return ilk in _KOMUT_BASLARI or ilk.startswith(("dur", "sus", "devam", "hadi", "başka", "baska", "yine", "tekrar",
                                                    "sesi", "yüksek", "duyamıyor", "uykum", "yavaş"))
