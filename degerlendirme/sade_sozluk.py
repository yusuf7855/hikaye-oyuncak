"""Sade sözlük (KUSURSUZ_VERI.md Adım 0a; K3 kapısı ve yazarın kelime listesi).

Türkçe TinyStories ön eğitim metninden (c3'ün gördüğü train.bin bölümü) kelime biçimi (yüzey) ve kök sıklıkları,
token sıklıkları ve ad adayları çıkarılır.

Kullanım: nice -n 19 .venv/bin/python degerlendirme/sade_sozluk.py olustur --nadir 20 --cok-nadir 5 --az-token 200
          .venv/bin/python degerlendirme/sade_sozluk.py olc <metin|dosya> [--haric Tosbi,baykuş] [--json]
          .venv/bin/python degerlendirme/sade_sozluk.py dogrula [--tokenizer hf_c3ft_v6/tokenizer.json]
Çıktı: data/sade_sozluk.json   yüzey sıklıkları (tf >= --cok-nadir), kök sıklıkları, sık kök listesi, eşikler,
                               token sayımları, kaynak ve tokenizer sha256'ları, kendi içerik sha256'sı
       data/sade_sozluk_sik.txt ~2100 sık kök, sıklık sırasıyla (fiil kökleri '-' ile biter: 'koş-', 'oyna-')

Kaynak: data/tr_tinystories/raw/tr-tinystories.txt; prepare_tr2 bu metni <|endoftext|> ile böler, tokenize edip
data/tr2_tinystories/vocab-16384/train.bin + val.bin yazar (son %0,5 val). Sayım yalnız train.bin'e tam giren
hikâyelerle yapılır (train.bin'deki EOT sayısı); ilk hikâyelerin yeniden tokenize edilip train.bin'in başıyla
aynı çıktığı ve toplam hikâye sayısının EOT sayısına eşit olduğu denetlenip kaydedilir.

Kelime: sec.kucuk ile küçültülür; kesmeden sonraki ek atılır ('Lily'nin' -> 'lily'); şapka yüzeyde korunur
(K3 şapkayı ayrıca reddeder), kökte düzleştirilir (rüzgâr -> rüzgar).

Kök: Zemberek (zemberek-python) kuruluysa onun lemması; değilse 'ek soyma': kelimenin sonundan Türkçe çekim ekleri
(isim: çoğul, iyelik, hâl, ki, ek-fiil, kişi; fiil: olumsuzluk, yeterlik, zaman, ek-zaman, kişi, sıfat-fiil ve
zarf-fiil) kesilir ve kalan gövde derlemde doğrulanır: isim gövdesi derlemde yalın geçmeli, fiil gövdesi en az iki
ayırt edici fiil ekiyle (-yor, -mak/-maya/-mayı, -ıp, -arak, -ınca) geçmeli. Ünsüz yumuşaması (kitabı -> kitap),
-yor daralması (oynuyor -> oyna-), birkaç ünlü düşmesi (ağzı -> ağız) geri alınır. Tek harflik belirsiz eklerde
(ayı = ay+ı mı, kalem = kale+m mi?) kelime kendi çoğulu ya da y-kaynaştırmalı hâlleri sık geçiyorsa kök sayılır.
Tasarımın eski ölçümlerindeki 5 harf kesmesi ('F5 kök', OLAY_ORGUSU_PLANI.md) --kok f5 ile seçilebilir.
Kök yöntemi ve sürümü json'a yazılır; yöntem değişirse sözlük (ve ona bağlı listeler) yeni sürümdür.

olc (kapi.py import eder: from sade_sozluk import yukle; yukle().olc(metin, haric=...)):
  nadir     : tr-tinystories'te --nadir (20) kereden az geçen kelime biçimleri (K3: hikâye başına <= 2)
  cok_nadir : --cok-nadir (5) kereden az geçenler (K3: <= 1)
  liste_disi: kökü sade_sozluk_sik.txt'de olmayan kelimeler (yazım kılavuzu Kural 7: <= 2)
  az_token  : ön eğitimde --az-token kereden az görülmüş BPE token'ları (haric'teki adların token'ları sayılmaz)
  sapkali   : şapkalı harf taşıyan kelimeler (normalizasyondan sonra K3: 0)
haric: adlar ve izinli dünya kökleri (küçük harfle karşılaştırılır; kesme eki atılmış yüzey ya da kök eşleşir).
"""
import argparse, collections, hashlib, json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HAM = os.path.join(ROOT, "data", "tr_tinystories", "raw", "tr-tinystories.txt")
TS2 = os.path.join(ROOT, "data", "tr2_tinystories", "vocab-16384")
CIKTI = os.path.join(ROOT, "data", "sade_sozluk.json")
SIK_CIKTI = os.path.join(ROOT, "data", "sade_sozluk_sik.txt")
K2_TOKENIZER = os.path.join(ROOT, "hf_c3ft_v6", "tokenizer.json")   # K2'nin tokenizer'ı; tr2 ile aynı dosya olmalı
EOT = "<|endoftext|>"

HARF = "a-zçğıöşüâîû"
BUYUK_HARF = "A-ZÇĞİÖŞÜÂÎÛ"
SAPKA = str.maketrans("âîû", "aiu")
KESME_EKI = re.compile(rf"(?<=[{HARF}{BUYUK_HARF}])['’][{HARF}{BUYUK_HARF}]+")   # Lily'nin -> Lily
KELIME = re.compile(rf"[{HARF}]+")
BUYUK_KELIME = re.compile(rf"[{BUYUK_HARF}][{HARF}{BUYUK_HARF}]*")
ORTA_BUYUK = re.compile(rf"(?<=[\w,])[ \t]+([{BUYUK_HARF}][{HARF}{BUYUK_HARF}]*)")   # cümle ortasında büyük harf


def kucuk(s):
    """sec.kucuk ile aynı (Türkçe I/İ)."""
    return s.replace("I", "ı").replace("İ", "i").lower()


def kelimeler(metin):
    """Metindeki kelimeler: küçük harf, kesme eki atılmış, şapka korunmuş. Sayım ve ölçüm aynı fonksiyonu kullanır."""
    return KELIME.findall(kucuk(KESME_EKI.sub("", metin.replace("’", "'"))))


def sha256_dosya(yol):
    h = hashlib.sha256()
    with open(yol, "rb") as f:
        for parca in iter(lambda: f.read(1 << 20), b""):
            h.update(parca)
    return h.hexdigest()


def icerik_sha256(d):
    """Sözlüğün kendi sha256'sı: 'sha256' alanı dışındaki içeriğin kanonik JSON'u."""
    govde = {k: v for k, v in d.items() if k != "sha256"}
    return hashlib.sha256(json.dumps(govde, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


# ---------------------------------------------------------------- ön eğitim metni ve token'lar

def hikayeler(n_max=None):
    """Ham metindeki hikâyeler, prepare_tr2 ile aynı bölmeyle (son EOT'den sonrası atılır, boşlar atlanır)."""
    tampon, n = [], 0
    with open(HAM, encoding="utf-8", errors="ignore") as f:
        for satir in f:
            if EOT not in satir:
                tampon.append(satir)
                continue
            parcalar = satir.split(EOT)
            tampon.append(parcalar[0])
            for p in parcalar[1:]:
                h = "".join(tampon)
                if h.strip():
                    yield h
                    n += 1
                    if n_max is not None and n >= n_max:
                        return
                tampon = [p]


def token_sayimi():
    import numpy as np
    tr = np.memmap(os.path.join(TS2, "train.bin"), dtype=np.uint16, mode="r")
    va = np.memmap(os.path.join(TS2, "val.bin"), dtype=np.uint16, mode="r")
    return tr, va


def kaynak_denetimi(tok, tr, va, n_bas=50):
    """Ham metin, tokenizer ve bin dosyaları birbirini tutuyor mu: ilk n_bas hikâye yeniden tokenize edilip
    train.bin'in başıyla karşılaştırılır; ham metindeki hikâye sayısı EOT sayısına eşit olmalı."""
    import numpy as np
    eot = tok.token_to_id(EOT)
    ids = []
    for h in hikayeler(n_bas):
        ids += tok.encode(h).ids + [eot]
    bas_esit = bool(np.array_equal(np.asarray(tr[:len(ids)], dtype=np.int64), np.array(ids, dtype=np.int64)))
    n_eot_tr = int((np.asarray(tr) == eot).sum())
    n_eot_va = int((np.asarray(va) == eot).sum())
    return {"ilk_hikayeler_ayni": bas_esit, "kontrol_hikaye": n_bas, "train_eot": n_eot_tr, "val_eot": n_eot_va}


def say(n_hikaye):
    """İlk n_hikaye hikâyede (train.bin'e tam girenler) kelime sayımları."""
    tf, df, buyuk, orta = (collections.Counter() for _ in range(4))
    n = nk = 0
    t0 = time.time()
    for h in hikayeler(n_hikaye):
        h = KESME_EKI.sub("", h.replace("’", "'"))
        ws = KELIME.findall(kucuk(h))
        tf.update(ws)
        df.update(set(ws))
        buyuk.update(kucuk(w) for w in BUYUK_KELIME.findall(h))
        orta.update(kucuk(w) for w in ORTA_BUYUK.findall(h))
        n += 1
        nk += len(ws)
        if n % 50000 == 0:
            print(f"  {n} hikâye, {nk:,} kelime, {time.time() - t0:.0f} s", file=sys.stderr, flush=True)
    return {"tf": tf, "df": df, "buyuk": buyuk, "orta_buyuk": orta, "n_hikaye": n, "n_kelime": nk}


# ---------------------------------------------------------------- kök: ek soyma

I, A, D, C = "[ıiuü]", "[ae]", "[dt]", "[cç]"
UNLU = set("aeıioöuü")
KISI_DI = f"(?:m|n|k|n{I}z|l{A}r)"                               # -dı'dan ve -sa'dan sonra


def _kopula(unlu):
    """ek-fiil: güzeldi, mutluydu, evdeyim, hazırsın, çocukken"""
    y = "y" if unlu else ""
    return (f"(?:{y}{D}{I}{KISI_DI}?|{y}m{I}ş(?:{I}m|s{I}n|{I}z|l{A}r|{D}{I}{KISI_DI}?)?|{y}s{A}{KISI_DI}?"
            f"|{D}{I}r(?:l{A}r)?|{y}k{A}n|{y}{I}m|s{I}n|{y}{I}z|s{I}n{I}z)")


KI = f"ki(?:n{I}|n{A}|nd{A}n?|l{A}r(?:{I}|{A}|d{A}n?|{I}n)?)?"   # evdeki, evdekini, evdekiler


def _isim_kuyrugu(unlu, cogul=True):
    """Gövdenin son harfine göre isim çekimi: çoğul, iyelik, hâl (+ki), ek-fiil. Kaynaştırma ünsüzleri
    (y, n, s) yalnız ünlüden sonra, bağlayıcı ünlü yalnız ünsüzden sonra gelir (kır+mızı reddedilir)."""
    y, n, s, bag = ("y", "n", "s", "") if unlu else ("", "", "", I)
    kop_v, kop_c = _kopula(True), _kopula(False)
    hal = f"(?:{y}{I}|{y}{A}|{D}{A}(?:{KI}|{kop_v})?|{D}{A}n|{n}{I}n(?:ki)?|{y}l{A})"
    hal_c = f"(?:{I}|{A}|{D}{A}(?:{KI}|{kop_v})?|{D}{A}n|{I}n(?:ki)?|l{A})"
    hal_p = f"(?:n{I}|n{A}|n{D}{A}(?:{KI}|{kop_v})?|n{D}{A}n|n{I}n(?:ki)?|yl{A})"   # 3. kişi iyelikten sonra
    parcalar = [f"(?:{s}{I}|l{A}r{I})(?:{hal_p}|{kop_v})?",                   # annesi(ne), kuşları(nı)
                f"(?:{bag}m{I}z|{bag}n{I}z|{bag}m|{bag}n)(?:{hal_c}|{kop_c})?",   # annem(e), evimiz(de)
                hal, _kopula(unlu)]
    if cogul:
        parcalar.insert(0, f"l{A}r(?:{_isim_kuyrugu(False, False)})?")
    return "(?:" + "|".join(parcalar) + ")"


def _zaman(unlu):
    y, bag, genis = ("y", "", "r") if unlu else ("", I, f"(?:{A}r|{I}r)")
    return (f"(?:{D}{I}(?:{KISI_DI}|l{A}r)?(?:{D}{I})?"                                  # geldi, geldiler
            f"|m{I}ş(?:{D}{I}{KISI_DI}?|{I}m|s{I}n|{I}z|l{A}r(?:{D}{I})?|{D}{I}r|s{A})?"     # gelmiş(ti)
            f"|{bag}yor(?:l{A}r)?(?:{D}{I}{KISI_DI}?|m{I}ş|s{A}{KISI_DI}?|{I}m|s{I}n|{I}z|s{I}n{I}z|k{A}n)?"
            f"|{genis}(?:l{A}r)?(?:{I}m|s{I}n|{I}z|s{I}n{I}z|{D}{I}{KISI_DI}?|m{I}ş|s{A}{KISI_DI}?|k{A}n)?"
            f"|m{A}l{I}(?:y{D}{I}{KISI_DI}?|ym{I}ş|y{I}m|s{I}n|y{I}z|l{A}r)?"
            f"|s{A}{KISI_DI}?(?:y{D}{I})?"                                                 # gelse(ydi)
            f"|{y}{A}l{I}m|{y}{A}y{I}m|s{I}n(?:l{A}r)?|{y}{I}n{I}z)")                       # gelelim, gelsin


def _adlasma(unlu):
    """mastar, sıfat-fiil, zarf-fiil (+ isim çekimi)"""
    y = "y" if unlu else ""
    return (f"(?:m{A}k(?:t{A}(?:n|y?{D}{I})?|l{A})?|m{A}{_isim_kuyrugu(True)}?|{y}{A}n{_isim_kuyrugu(False)}?"
            f"|{D}{I}[kğ]{_isim_kuyrugu(False)}?|{y}{A}{C}{A}[kğ]{_isim_kuyrugu(False)}?"
            f"|{y}{I}p|{y}{A}r{A}k|{y}{I}n{C}{A}(?:y{A})?)")


def _fiil_kuyrugu(unlu):
    """Gövdenin son harfine göre fiil çekimi. Olumsuzluk (-ma) ve yeterlik (-abil, -ama) önde."""
    y = "y" if unlu else ""
    sonra_ma = (f"(?:{_zaman(True)}|z(?:l{A}r)?(?:s{I}n|{D}{I}{KISI_DI}?|s{A}|k{A}n)?|m|y{I}z|{_adlasma(True)})")
    return (f"(?:m{I}yor(?:l{A}r)?(?:{D}{I}{KISI_DI}?|m{I}ş|{I}m|s{I}n|{I}z|k{A}n)?"   # gelmiyor
            f"|m{A}{sonra_ma}?|{y}{A}m{A}{sonra_ma}?|{y}{A}m{I}yor(?:{D}{I}{KISI_DI}?|{I}m|s{I}n|{I}z)?"
            f"|{y}{A}bil(?:{_zaman(False)}|{_adlasma(False)}|m{A}{sonra_ma}?|m{I}yor(?:{D}{I}{KISI_DI}?)?)?"
            f"|{_zaman(unlu)}|{_adlasma(unlu)})")


ISIM_KUYRUK = {u: re.compile(_isim_kuyrugu(u)) for u in (True, False)}
FIIL_KUYRUK = {u: re.compile(_fiil_kuyrugu(u)) for u in (True, False)}
CEKIMLI = {u: re.compile(f"(?:m{A}|{'y' if u else ''}{A}m{A}|{'y' if u else ''}{A}bil)?{_zaman(u)}|m{I}yor.*")
           for u in (True, False)}                      # çekimli fiil: arkasına hâl eki gelmez (yardım != yar+dım)
SIFAT_FIIL = re.compile(f"(?:y?{A}n|{D}{I}[kğ]|y?{A}{C}{A}[kğ]){_isim_kuyrugu(False)}?|m{A}{_isim_kuyrugu(True)}?")
# ^ koşanları, yaptıkları, koşmaları: sıfat-fiil ve ad-fiil çoğul ve hâl alır (koşmak almaz)
HAL_YA_DA_KOPULA = re.compile(f"[yn]?{I}|[yn]?{A}|{D}{A}n?|n?{I}n|y?l{A}|{_kopula(True)}|{_kopula(False)}")
BELIRSIZ_ISIM = re.compile(f"{I}|{A}|{I}?[mn]|s{I}|y{I}|y{A}|n{I}|n{A}|l{A}|{I}n|{I}z")   # ayı = ay+ı mı?
BELIRSIZ_IYELIK = re.compile(f"{I}?[mn]|{I}z|s{I}")      # doğum = doğu+m mu? (iyelik, sıkı eşik)
YUMUSAMA = {"b": "p", "c": "ç", "d": "t", "ğ": "k", "g": "k"}   # kitabı, ağacı, kanadı, köpeği, rengi
DUSME = {"ağz": "ağız", "burn": "burun", "oğl": "oğul", "aln": "alın", "göğs": "göğüs", "boyn": "boyun",
         "karn": "karın", "akl": "akıl", "gönl": "gönül", "beyn": "beyin", "ism": "isim", "resm": "resim",
         "şehr": "şehir", "nehr": "nehir", "zehr": "zehir", "fikr": "fikir", "kayb": "kayıp", "sabr": "sabır",
         "ömr": "ömür", "vakt": "vakit", "koyn": "koyun", "bağr": "bağır", "kokl": "koku"}
KISA_KOK = {"ev", "su", "el", "at", "ot", "ip", "iş", "ok", "ağ", "ay", "ad", "ön", "iç", "uç", "üç", "on",
            "af", "ak", "an", "ar", "az", "ek", "et", "üst", "alt", "yaş", "yan", "yol", "göz", "dağ", "yüz", "saç",
            "kaz", "tat", "kar", "baş", "taş", "kış", "yaz", "top", "gün", "yer", "diş", "un"}
FIIL_DEGIL = {"var"}                                    # vardı: var+dı (ek-fiil), varmak değil
ZAMIR = {}
for _k, _g in {"o": "on", "bu": "bun", "şu": "şun"}.items():
    for _e in ("u", "a", "un", "da", "dan", "unla", "lar", "ları", "lara", "ların", "larla", "lardan", "larda"):
        ZAMIR[_g + _e] = _k                                  # onu, bunlara, şundan
for _e in ("m", "n", "ni", "ne", "nden", "si", "sine", "sini", "sinden", "leri", "lerine", "lerini", "mi", "me",
           "mize", "mizi", "nize", "nizi", "miz", "niz", "nde", "sinde"):
    ZAMIR["kendi" + _e] = "kendi"                         # kendini, kendisine
for _k, _g in {"ben": ("beni", "bana", "benim", "bende", "benden", "benimle"),
               "sen": ("seni", "sana", "senin", "sende", "senden", "seninle"),
               "biz": ("bizi", "bize", "bizim", "bizde", "bizden", "bizimle", "bizler"),
               "siz": ("sizi", "size", "sizin", "sizde", "sizden", "sizinle", "sizler")}.items():
    for _f in _g:
        ZAMIR[_f] = _k
KAPALI = {"için", "bile", "ama", "ile", "gibi", "kadar", "diye", "hala", "hâlâ", "hepsi", "hep", "yine", "şimdi",
          "sonra", "önce", "belki", "sadece", "hemen", "birden", "birlikte", "neden", "niye", "nasıl", "nerede",
          "nereye", "ne", "kim", "kimse", "hiç", "henüz", "artık", "daha", "en", "çok", "az", "ise", "ancak", "fakat",
          "çünkü", "eğer", "ki", "de", "da", "mi", "mı", "mu", "mü", "ve", "veya", "ya", "yani", "işte", "evet",
          "hayır", "tamam", "lütfen", "merhaba", "teşekkürler", "iyi", "kendi", "bir", "biri", "birisi", "aniden",
          "sonunda", "birbirine", "birbirini", "birbirlerine", "birbirlerini", "hiçbir", "herkes", "her", "bazı",
          "anda", "hani", "haydi", "hadi", "göre", "hatta", "elbette", "adı", "adını", "adına", "adında"}
GOVDE_OLMAZ = {"için", "ama", "ile", "diye", "hala", "hâlâ", "bile", "ise", "de", "da", "ki", "mi", "mı", "mu", "mü",
               "ya", "ve", "en", "anda", "sonunda", "aniden", "hani"}   # içinde != için+de
LEKSIK = {"dondurma", "yemek", "ekmek", "kızartma", "çıkartma", "dolma", "sarma", "çakmak", "kaymak", "yiyecek",
          "içecek", "salıncak", "gelecek", "kazan", "yazar", "doğan", "uçurtma", "oyuncak", "kaydırak"}   # sözlükleşmiş
HAL_KESIN = {True: ("ya", "ye", "da", "de", "dan", "den"),              # iyelik ve fiil ekiyle karışmayanlar
             False: ("a", "e", "da", "de", "ta", "te", "dan", "den", "tan", "ten")}
HAL_EKLERI = {True: ("ya", "ye", "yı", "yi", "yu", "yü", "da", "de", "dan", "den", "nın", "nin", "nun", "nün",
                     "yla", "yle"),
              False: ("a", "e", "ı", "i", "u", "ü", "da", "de", "ta", "te", "dan", "den", "tan", "ten", "ın", "in",
                      "un", "ün", "la", "le")}


class Kokcu:
    """Ek soyma kökü. tf: yüzey sıklıkları (şapkası düzleştirilmiş), fiil: fiil gövdeleri -> temel kanıt
    (-mak ve -dı sıklığı), ad: özel ad olarak geçen biçimler. En uzun geçerli gövde seçilir ve kalan kelime
    üzerinde tekrarlanır (kuşlarına -> kuşların -> kuşları -> kuşlar -> kuş); fiil gövdesine ulaşınca durulur.
    Fiil kökleri '-' ile işaretlenir. Aynı kesimde fiil ve isim geçerliyse fiil seçilir (yazdı -> yaz-),
    FIIL_DEGIL hariç (vardı -> var). Kelimenin kendisinin kök olduğunu gösteren kanıtlar (çoğul+hâl alması,
    hâl alması, y-kaynaştırması) kesmeyi durdurur."""

    def __init__(self, tf, fiil, ad=(), isim_esik=5):
        self.tf = tf
        self.fiil = dict(fiil)
        self.ad = set(ad)
        self.isim_esik = isim_esik
        self._on = {}

    def cogullu_hal(self, x):
        """x çoğul + hâl ekiyle geçiyor mu (kelimeleri, yastıklara): x bir sözcük köküdür, çekimli biçim değil.
        Yalın çoğul sayılmaz: ağladılar, üzgündüler çekimli fiil/ek-fiil biçimleridir."""
        g = self.tf.get
        n = sum(g(x + c + h, 0) for c in ("lar", "ler") for h in HAL_EKLERI[False])
        return n >= max(2, 0.005 * g(x, 0))

    def yalin_cogul(self, x):
        """x yalın çoğul alıyor mu (kadınlar, kapılar): tek harflik belirsiz ekle biten x yine de sözcük kökü."""
        g = self.tf.get
        return g(x + "lar", 0) + g(x + "ler", 0) >= max(2, 0.01 * g(x, 0))

    def hal_alir(self, x):
        """x yönelme, bulunma ya da ayrılma hâli alıyor mu (yardıma, kadında, yerden, gürültüden): çekimli fiil,
        ek-fiilli ve hâl ekli biçimler bir daha hâl eki almaz."""
        g = self.tf.get
        return sum(g(x + h, 0) for h in HAL_KESIN[x[-1] in UNLU]) >= max(3, 0.01 * g(x, 0))

    def y_kaynastirir(self, x):
        """ünlüyle biten x y-kaynaştırmalı hâl alıyor mu (ayıya, kapıyı): x = kök + iyelik değil."""
        g = self.tf.get
        y = sum(g(x + "y" + u, 0) for u in "aeıiuü")
        nn = sum(g(x + "n" + u, 0) for u in "aeıiuü")
        return y >= max(3, 0.01 * g(x, 0)) and y >= nn

    def fiil_govdeleri(self, s, t):
        """s+t kesiminde t'nin başına gelebilecek fiil gövdeleri (gövde, ünlüyle biter mi), en güçlüsü önde:
        arıyor -> ara- (ar- değil), gidiyor -> git-, yiyecek -> ye-."""
        aday = [(s, s[-1] in UNLU)]
        if t[0] in UNLU and s[-1] == "d":
            aday.append((s[:-1] + "t", False))
        if re.match(f"{I}yor", t):
            aday += [(s + "a", False), (s + "e", False)]
        if s in ("yi", "di") and t[0] == "y":
            aday.append((s[0] + "e", True))
        aday = [(g, u) for g, u in aday if g in self.fiil and g not in FIIL_DEGIL]
        return sorted(aday, key=lambda a: -self.fiil[a[0]])

    def cekimli_fiil(self, s):
        """s çekimli bir fiil biçimi mi (yardı = yar+dı, gider = git+er): isim gövdesi olamaz."""
        for i in range(len(s) - 1, 1, -1):
            for v, unlu in self.fiil_govdeleri(s[:i], s[i:]):
                if CEKIMLI[unlu].fullmatch(s[i:]):
                    return True
        return False

    def isim_mi(self, s):
        if self.tf.get(s, 0) < self.isim_esik or s in GOVDE_OLMAZ or (len(s) < 3 and s not in KISA_KOK):
            return False
        return (s not in self.fiil or s in KISA_KOK or s in FIIL_DEGIL or s in LEKSIK or self.cogullu_hal(s)
                or self.hal_alir(s))       # ara (araya, arada) hem isim hem fiil; bak- (bakın != bak+ın) değil

    def isim_gecer(self, x, s, g, t):
        """g+t isim çözümlemesi kabul edilir mi (x = s+t, g = s ya da yumuşaması/ünlü düşmesi geri alınmış s)."""
        tf = self.tf.get
        nx = tf(x, 0)
        if self.cogullu_hal(x):                                         # dükkan != dük+kan, kelime != kel+ime
            return False
        if self.cekimli_fiil(x) and not self.hal_alir(x):               # kırdım: fiil çözümlemesi beklenir
            return False
        if HAL_YA_DA_KOPULA.fullmatch(t) and self.hal_alir(x):          # gürültü != gürül+tü, kaptan != kap+tan
            return False
        if g == s and self.cekimli_fiil(g) and not self.hal_alir(g):    # yardım != yardı+m
            return False
        if g in self.ad and tf(g, 0) < nx:                              # arasında != Aras+ında, karla != Karl+a
            return False
        if BELIRSIZ_ISIM.fullmatch(t):                                  # ayı != ay+ı, kadın != kat+ın
            if self.yalin_cogul(x) or (x[-1] in UNLU and self.y_kaynastirir(x)):
                return False
            if (10 if BELIRSIZ_IYELIK.fullmatch(t) else 100) * tf(g, 0) < nx:   # doğum != doğu+m
                return False
            if len(t) == 1 and s[-1] in "syn" and s[-2] in UNLU and tf(s[:-1], 0) >= tf(s, 0):
                return False                                            # gagası != gagas+ı
        return True

    def adaylar(self, x):
        """(gövde, tür) adayları, en uzun gövde önce."""
        sozcuk = self.cogullu_hal(x)
        for i in range(len(x) - 1, 0, -1):
            s, t = x[:i], x[i:]
            for g, unlu in self.fiil_govdeleri(s, t):
                if not FIIL_KUYRUK[unlu].fullmatch(t):
                    continue
                if sozcuk and not SIFAT_FIIL.fullmatch(t):             # parmak != par+mak, kalıp != kal+ıp
                    continue
                if CEKIMLI[unlu].fullmatch(t) and not SIFAT_FIIL.fullmatch(t) and self.hal_alir(x):
                    continue                                            # yardım != yar+dım, yer != ye+r
                yield g, "fiil"
                break
            else:
                isimler = [(s, s[-1] in UNLU)]
                if t[0] in UNLU and s[-1] in YUMUSAMA:                  # kitabı -> kitap, rengi -> renk
                    isimler.append((s[:-1] + YUMUSAMA[s[-1]], False))
                if t[0] in UNLU and s in DUSME:                         # ağzı -> ağız
                    isimler.append((DUSME[s], False))
                if t[0] in UNLU and len(s) >= 3 and s[-1] == s[-2] and s[-1] not in UNLU:
                    isimler.append((s[:-1], False))                     # sırrı -> sır, hakkı -> hak
                for g, unlu in isimler:
                    if self.isim_mi(g) and ISIM_KUYRUK[unlu].fullmatch(t) and self.isim_gecer(x, s, g, t):
                        yield g, "isim"
                        break

    def kok(self, w):
        w = w.translate(SAPKA)
        if w in self._on:
            return self._on[w]
        if w in ZAMIR:
            k = ZAMIR[w]
        elif w in KAPALI or w in LEKSIK:
            k = w
        elif w in self.fiil and w not in FIIL_DEGIL and self.tf.get(w, 0) < self.fiil[w] and not self.cogullu_hal(w):
            k = w + "-"                                          # yalın fiil (emir): koş, gel; eski, kuru isim kalır
        else:
            x, tur = w, "isim"
            while tur == "isim" and x not in LEKSIK:
                aday = next(self.adaylar(x), None)
                if aday is None:
                    break
                x, tur = aday
            k = x + "-" if tur == "fiil" else x
        self._on[w] = k
        return k


FIIL_KANIT = {   # ayırt edici fiil ekleri: (ünsüzle biten gövdeden sonra, ünlüyle biten gövdeden sonra)
    "yor": ([f"{u}yor" for u in "ıiuü"], ["yor"]),
    "mak": (["mak", "mek", "makta", "mekte", "maktan", "mekten"],) * 2,
    "maya": (["maya", "meye", "mayı", "meyi"],) * 2,        # tasmaya, mamayı gibi isimlerle çakışabilir
    "ip": (["ıp", "ip", "up", "üp"], ["yıp", "yip", "yup", "yüp"]),
    "arak": (["arak", "erek"], ["yarak", "yerek"]),
    "inca": (["ınca", "ince", "unca", "ünce"], ["yınca", "yince", "yunca", "yünce"]),
    "di": (["dı", "di", "du", "dü", "tı", "ti", "tu", "tü"], ["dı", "di", "du", "dü"]),    # tek başına ayırt etmez
}
GUCLU_KANIT = ("yor", "mak", "maya", "ip", "arak", "inca")


def fiil_kokleri(tf, en_az_tf=5):
    """Fiil gövdeleri -> temel kanıt (-mak ailesi + -dı sıklığı). Gövde en az iki ayrı ayırt edici ekle (-yor,
    -mak, -maya/-mayı, -ıp, -arak, -ınca) ya da biriyle ve 20+ kez -dı ile geçmeli; temel kanıt bütün kanıtın
    %0,5'inden az olmamalı (oyn+mayı yazım hatası, par+mak elenir). İki harfli ünsüz+ünlü gövde yalnız ye-, de-.
    Olumsuz (-ma), yeterlik (-abil, -ama), -a/-e ve kaynaştırma (oynay-) gövdeleri, asıl gövde fiilse atılır.
    Ünlüyle biten gövdeye doğrudan -yor (okuyor) ancak gövdenin ünlüsüz hâli fiil değilse sayılır (geçiyor
    geçi- değil geç-)."""
    def say(yor_unlu, onceki):
        kanit = collections.defaultdict(collections.Counter)
        for w, n in tf.items():
            for sinif, (unsuz, unlu) in FIIL_KANIT.items():
                for e in set(unsuz + unlu):
                    if not w.endswith(e) or len(w) <= len(e):
                        continue
                    s = w[:-len(e)]
                    if sinif == "yor":
                        if e == "yor":                         # okuyor -> oku-, yürüyor -> yürü-
                            if yor_unlu and s[-1] in UNLU and s[:-1] not in onceki:
                                kanit[s][sinif] += n
                        else:                                 # koşuyor -> koş-; oynuyor -> oyna-; biliyor -> bil-
                            for g in (s, s + "a", s + "e"):
                                kanit[g][sinif] += n
                        continue
                    if sinif not in ("mak", "maya", "di") and (e in unlu) != (s[-1] in UNLU):
                        continue
                    kanit[s][sinif] += n
                    if e[0] in UNLU and s[-1] == "d":        # gidip, ederek -> git-, et-
                        kanit[s[:-1] + "t"][sinif] += n
        return kanit

    def gecer(g, k):
        guclu = sum(1 for c in GUCLU_KANIT if k[c])
        top = sum(k.values())
        bicim = len(g) >= 3 or (len(g) == 2 and (g[0] in UNLU or g in ("ye", "de")))
        return (bicim and top >= en_az_tf and (guclu >= 2 or (guclu >= 1 and k["di"] >= 20))
                and k["mak"] + k["di"] >= max(3, 0.005 * top))

    ilk = {g for g, k in say(False, set()).items() if gecer(g, k)}
    kanit = say(True, ilk)
    fiil = {g: k["mak"] + k["di"] for g, k in kanit.items() if gecer(g, k)}

    def turemis(g):
        for ek in ("ma", "me", "yama", "yeme", "ama", "eme", "abil", "ebil", "yabil", "yebil"):
            if g.endswith(ek) and g[:-len(ek)] in fiil:
                return True
        if g[-1] in "ae" and g[:-1] in fiil:                  # bula- (bul+a-madı) atılır, kapa- (kapadı) kalır
            return kanit[g]["di"] < 0.05 * kanit[g[:-1]]["di"]
        if g[-1] == "y" and g[:-1] in fiil and g[-2] in UNLU and not kanit[g]["mak"]:
            return True                                        # oynay- (oyna+y)
        return False
    return {g: n for g, n in fiil.items() if not turemis(g)}
