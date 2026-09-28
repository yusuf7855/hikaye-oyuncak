"""Sade sözlük (KUSURSUZ_VERI.md Adım 0a; K3 kapısı ve yazarın kelime listesi).

Türkçe TinyStories ön eğitim metninden (c3'ün gördüğü train.bin bölümü) kelime biçimi (yüzey) ve kök sıklıkları,
token sıklıkları ve ad biçimleri çıkarılır.

Kullanım: nice -n 19 .venv/bin/python degerlendirme/sade_sozluk.py olustur --nadir 20 --cok-nadir 5 --az-token 200
                [--sik 3000] [--kok otomatik|ek|zemberek|f5]           (~1 dk, tek çekirdek, torch yok)
          (depodaki sözlük: --sik 3000 --kok ek; Zemberek kuruluyken "otomatik" zemberek seçer)
          .venv/bin/python degerlendirme/sade_sozluk.py olc <metin|dosya> [--haric Tosbi,baykuş] [--json]
          .venv/bin/python degerlendirme/sade_sozluk.py dogrula [--tokenizer hf_c3ft_v6/tokenizer.json]
Çıktı: data/sade_sozluk.json    yuzey (tf >= --cok-nadir; listede olmayan biçim daha az geçer), kok, sik (sıklık
                                sırası), kok_ornek, fiil (gövde -> -mak/-dı kanıtı), adlar (biçim -> ad oranı),
                                token_sayim (train.bin'de token başına), az_token, esikler, kok_yontemi, kaynak
                                (ham metin, train/val.bin, tokenizer ve K2 tokenizer sha256'ları, denetim) ve
                                sha256 ('sha256' dışındaki içeriğin kanonik JSON'unun sha256'sı; dosya sha256'sı
                                ayrıca K11 sürümüne girer)
       data/sade_sozluk_sik.txt  --sik (3000) sık kök, alfabe sırasıyla (fiil kökleri '-' ile biter: koş-, oyna-);
                                sha256'sı sözlükte (sik_txt_sha256)

Kaynak: data/tr_tinystories/raw/tr-tinystories.txt; prepare_tr2 bu metni <|endoftext|> ile böler, tokenize edip
data/tr2_tinystories/vocab-16384/train.bin + val.bin yazar (son %0,5 val). Sayım yalnız train.bin'e tam giren
hikâyelerle yapılır (train.bin'deki EOT sayısı); ilk 50 hikâyenin yeniden tokenize edilip train.bin'in başıyla
aynı çıktığı ve ham metindeki hikâye sayısının train+val EOT sayısına eşit olduğu denetlenir, tutmazsa durur.

Kelime: sec.kucuk ile küçültülür; kesmeden sonraki ek atılır ('Lily'nin' -> 'lily'); şapka yüzeyde korunur
(K3 şapkayı ayrıca reddeder), kökte düzleştirilir (rüzgâr -> rüzgar). Cümle ortasında çoğunlukla büyük harfle
geçen biçimler (Lily, Tim; oran >= 0,5) ad sayılır, kök sayımına girmez.

Kök (--kok otomatik): zemberek-python kuruluysa onun lemması (fiil 'koşmak' -> 'koş-'), değilse 'ek soyma'.
KUSURSUZ_VERI.md bir kök kesme kuralı tanımlamıyor; eski ölçümlerdeki 5 harf kesmesi (OLAY_ORGUSU_PLANI.md,
'F5 kök') --kok f5 ile seçilebilir ama kısa kökleri böler (koştu/koşuyor/koşmak üç ayrı 'kök'), yazar listesi
için kullanılmaz. Ek soyma: kelimenin sonundan Türkçe çekim ekleri (isim: çoğul, iyelik, hâl, ki, ek-fiil, kişi;
fiil: olumsuzluk, yeterlik, zaman, ek-zaman, kişi, sıfat-fiil, zarf-fiil) gövdenin son harfine uygun kaynaştırma
kurallarıyla kesilir; en uzun geçerli gövde seçilip kalan kelimeyle tekrarlanır. İsim gövdesi derlemde yalın
geçmeli; fiil gövdesi derlemde ayırt edici fiil ekleriyle (-yor, -mak, -maya, -ıp, -arak, -ınca; -dı yardımcı)
geçmeli. Ünsüz yumuşaması (kitabı -> kitap), -yor daralması (oynuyor -> oyna-), ünlü düşmesi (ağzı -> ağız) ve
ikiz ünsüz (sırrı -> sır) geri alınır. Kelimenin kendisinin kök olduğunu gösteren derlem kanıtı (çoğul + hâl:
kelimeleri; hâl: yardıma; y-kaynaştırma: ayıya) kesmeyi durdurur (kelime != kel+ime, yardım != yar+dım,
ayı != ay+ı). Birkaç sözlükleşmiş kelime (LEKSIK: dondurma, yemek, öğretmen...), zamir çekimleri (ZAMIR) ve
kapalı sınıf kelimeler (KAPALI) sabittir. Kök yöntemi ve sürümü json'a yazılır; yöntem değişirse sözlük ve ona
bağlı listeler (canli_rol.json, tohum_kelimeleri.json) yeni sürümdür.

olc (kapi.py import eder: from sade_sozluk import yukle; yukle().olc(metin, haric=...)):
  nadir     : tr-tinystories'te --nadir (20) kereden az geçen kelime biçimleri (K3: hikâye başına <= 2)
  cok_nadir : --cok-nadir (5) kereden az geçenler (K3: <= 1)
  liste_disi: kökü sade_sozluk_sik.txt'de olmayan kelimeler (yazım kılavuzu Kural 7: <= 2)
  az_token  : ön eğitimde --az-token kereden az görülmüş BPE token'ları, adlarınki hariç. K3 metni '20 kereden az'
              diyor; token_sayim tam olduğu için kapi.py başka eşik de uygulayabilir.
  sapkali   : şapkalı harf taşıyan kelimeler (normalizasyondan sonra K3: 0; 'hâlâ' dahil)
  kokler    : sayılan her kelimenin kökü
Liste değerleri geçiş sırasıyla, tekrarlarıyla döner (hikâye başına sayı = len).
haric: adlar ve izinli dünya kökleri (küçük harfle; kesme eki atılmış yüzey, düzleştirilmiş biçim ya da kök eşleşir).
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
            f"|m{A}l{I}(?:y{D}{I}{KISI_DI}?|ym{I}ş|y{I}m|s{I}n|y{I}z|s{I}n{I}z|l{A}r)?"
            f"|s{A}(?:{KISI_DI}|y{D}{I}{KISI_DI}?)?"                                        # gelse(ydim)
            f"|{y}{A}l{I}m|{y}{A}y{I}m|s{I}n(?:l{A}r)?|{y}{I}n(?:{I}z)?)")                 # gelelim, gelsin, gelin


def _adlasma(unlu):
    """mastar, sıfat-fiil, zarf-fiil (+ isim çekimi)"""
    y = "y" if unlu else ""
    return (f"(?:m{A}k(?:t{A}(?:n|y?{D}{I})?|l{A})?|m{A}{_isim_kuyrugu(True)}?|{y}{A}n{_isim_kuyrugu(False)}?"
            f"|{D}{I}[kğ]{_isim_kuyrugu(False)}?|{y}{A}{C}{A}[kğ]{_isim_kuyrugu(False)}?"
            f"|{y}{I}p|{y}{A}r{A}k|{y}{I}n{C}{A}(?:y{A})?|{D}{I}k{C}{A})")             # büyüdükçe


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
SIFAT_FIIL = re.compile(f"(?:m{A}|y?{A}m{A}|y?{A}bil)?(?:(?:y?{A}n|{D}{I}[kğ]|y?{A}{C}{A}[kğ]){_isim_kuyrugu(False)}?"
                        f"|m{A}{_isim_kuyrugu(True)}?)")
# ^ koşanları, yaptıkları, koşmaları: sıfat-fiil ve ad-fiil çoğul ve hâl alır (koşmak almaz)
YETERSIZ = re.compile(f"y?{A}m{A}")                        # yapama (tek başına)
CEKIMLI_GUCLU = re.compile(f"(?:m{A}|y?{A}m{A}|y?{A}bil)?(?:{D}{I}|m{I}ş|{I}?yor|m{I}yor|y?{A}{C}{A}[kğ]).*")
GENIS_R = re.compile(f"r(?:{_isim_kuyrugu(False)})?")          # -r geniş zaman / -ler çoğul çakışması
EMIR_COGUL = re.compile(f"(?:m{A})?y?{I}n")                   # durun, gidin, korkmayın; koyun, kalın, yakın değil
HAL_YA_DA_KOPULA = re.compile(f"[yn]?{I}|[yn]?{A}|{D}{A}n?|y?l{A}|{_kopula(True)}|{_kopula(False)}")
BELIRSIZ_ISIM = re.compile(f"{I}|{A}|{I}?[mn]|s{I}|y{I}|y{A}|n{I}|n{A}|l{A}|{I}n|{I}z")   # ayı = ay+ı mı?
BELIRSIZ_IYELIK = re.compile(f"{I}?[mn]|{I}z")           # doğum = doğu+m mu? (1./2. kişi iyelik, sıkı eşik)
YUMUSAMA = {"b": "p", "c": "ç", "d": "t", "ğ": "k", "g": "k"}   # kitabı, ağacı, kanadı, köpeği, rengi
DUSME = {"ağz": "ağız", "burn": "burun", "oğl": "oğul", "aln": "alın", "göğs": "göğüs", "boyn": "boyun",
         "karn": "karın", "akl": "akıl", "gönl": "gönül", "beyn": "beyin", "ism": "isim", "resm": "resim",
         "şehr": "şehir", "nehr": "nehir", "zehr": "zehir", "fikr": "fikir", "kayb": "kayıp", "sabr": "sabır",
         "ömr": "ömür", "vakt": "vakit", "koyn": "koyun", "bağr": "bağır", "omz": "omuz", "özr": "özür",
         "keşf": "keşif", "kasd": "kasıt", "hükm": "hüküm"}
IKIZ = {"sırr": "sır", "hakk": "hak", "hiss": "his", "aff": "af", "zann": "zan", "tıbb": "tıp", "hatt": "hat",
        "redd": "ret", "şıkk": "şık", "üss": "üs"}
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
ELLE = {"der": "de-", "derken": "de-", "dersin": "de-", "derim": "de-",     # der != dere'nin kökü
        "adı": "ad", "adını": "ad", "adına": "ad", "adında": "ad", "adındaki": "ad", "adıyla": "ad"}   # at değil
KAPALI = {"için", "bile", "ama", "ile", "gibi", "kadar", "diye", "hala", "hâlâ", "hepsi", "hep", "yine", "şimdi",
          "sonra", "önce", "belki", "sadece", "hemen", "birden", "birlikte", "neden", "niye", "nasıl", "nerede",
          "nereye", "ne", "kim", "kimse", "hiç", "henüz", "artık", "daha", "en", "çok", "az", "ise", "ancak", "fakat",
          "çünkü", "eğer", "ki", "de", "da", "mi", "mı", "mu", "mü", "ve", "veya", "ya", "yani", "işte", "evet",
          "hayır", "tamam", "lütfen", "merhaba", "teşekkürler", "iyi", "kendi", "bir", "biri", "birisi", "aniden",
          "sonunda", "birbirine", "birbirini", "birbirlerine", "birbirlerini", "hiçbir", "herkes", "her", "bazı",
          "anda", "hani", "haydi", "hadi", "göre", "hatta", "elbette"}
GOVDE_OLMAZ = {"için", "ama", "ile", "diye", "hala", "hâlâ", "bile", "ise", "de", "da", "ki", "mi", "mı", "mu", "mü",
               "ya", "ve", "en", "anda", "sonunda", "aniden", "hani"}   # içinde != için+de
LEKSIK = {"dondurma", "yemek", "ekmek", "kızartma", "çıkartma", "dolma", "sarma", "çakmak", "kaymak", "yiyecek",
          "içecek", "salıncak", "gelecek", "kazan", "yazar", "doğan", "uçurtma", "oyuncak", "kaydırak",
          "koca", "ucuz", "kısa", "karar", "yaratık", "yaramaz", "kovan", "katır", "sağır", "diken", "sıkıcı",
          "yapıştırıcı", "soğutucu", "verici", "korkutucu", "öğretmen", "düşman", "şişman", "eğitmen", "kaşık",
          "çakıl", "kıyı", "yapı", "bakkal", "yazı", "çizim", "kaptan", "dayı"}   # sözlükleşmiş
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
        self.ad = dict(ad) if isinstance(ad, dict) else dict.fromkeys(ad, 1.0)   # biçim -> ad oranı
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
        n = [g(x + h, 0) for h in HAL_KESIN[x[-1] in UNLU]]
        return sum(k >= 2 for k in n) >= 2 and sum(n) >= max(3, 0.01 * g(x, 0))   # kısa tek başına kıs+a değil

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
        """s -dı, -mış, -yor ya da -acak ile çekimli bir fiil biçimi mi (yardı = yar+dı, geldi, gidiyor): isim
        gövdesi olamaz. Geniş zaman, dilek-şart ve emir okumaları sayılmaz (insan != in+san, serin != ser+in)."""
        for i in range(len(s) - 1, 1, -1):
            if not CEKIMLI_GUCLU.fullmatch(s[i:]):
                continue
            for v, unlu in self.fiil_govdeleri(s[:i], s[i:]):
                if CEKIMLI[unlu].fullmatch(s[i:]):
                    return True
        return False

    def isim_mi(self, s):
        if self.tf.get(s, 0) < self.isim_esik or s in GOVDE_OLMAZ or (len(s) < 3 and s not in KISA_KOK):
            return False
        return (s not in self.fiil or s in KISA_KOK or s in FIIL_DEGIL or s in LEKSIK or self.cogullu_hal(s)
                or self.hal_alir(s) or self.tf.get(s, 0) >= self.fiil[s])
        # ^ ara (araya, arada), ekşi (yalın kullanımı fiil kanıtından sık) hem isim hem fiil; bak- (bakın) değil

    def isim_gecer(self, x, s, g, t, onarim="ham"):
        """g+t isim çözümlemesi kabul edilir mi (x = s+t; g = s ya da onarim: 'yumusama' kitab -> kitap,
        'dusme' ağz -> ağız, 'ikiz' sırr -> sır)."""
        tf = self.tf.get
        nx = tf(x, 0)
        if self.cogullu_hal(x):                                         # dükkan != dük+kan, kelime != kel+ime
            return False
        if HAL_YA_DA_KOPULA.fullmatch(t) and self.hal_alir(x):          # gürültü != gürül+tü, kaptan != kap+tan
            return False
        if g == s and self.cekimli_fiil(g) and not self.hal_alir(g):    # yardım != yardı+m
            return False
        if g == s and g in self.ad and (1 if self.ad[g] >= 0.9 else 10) * tf(g, 0) < nx:
            return False                                                # arasında != Aras+ında; kafası = kafa+sı
        if (onarim == "yumusama" and self.isim_mi(s[:-1]) and tf(s[:-1], 0) > tf(g, 0)
                and ISIM_KUYRUK[s[-2] in UNLU].fullmatch(x[len(s) - 1:])):
            return False                                                # karada = kara+da, karat+a değil
        if BELIRSIZ_ISIM.fullmatch(t):                                  # ayı != ay+ı, kadın != kat+ın
            if self.yalin_cogul(x) or (x[-1] in UNLU and self.y_kaynastirir(x)):
                return False
            oran = 10 if BELIRSIZ_IYELIK.fullmatch(t) or (onarim == "yumusama" and t in ("a", "e")) else 100
            if onarim in ("ham", "yumusama") and oran * tf(g, 0) < nx:
                return False                                            # doğum != doğu+m, koca != koç+a
            if len(t) == 1 and s[-1] in "syn" and s[-2] in UNLU and tf(s, 0) < 20 and tf(s[:-1], 0) >= tf(s, 0):
                return False                                            # gagası != gagas+ı (saray+ı kalır)
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
                if (CEKIMLI[unlu].fullmatch(t) and not SIFAT_FIIL.fullmatch(t) or YETERSIZ.fullmatch(t)) \
                        and self.hal_alir(x):
                    continue                                            # yardım != yar+dım, sinema != sin+eme
                if EMIR_COGUL.fullmatch(t) and (self.yalin_cogul(x) or self.tf.get(x, 0) > 0.05 * self.fiil[g]):
                    continue                                            # koyun != koy+un, kalın != kal+ın
                if (g[-2:] in ("la", "le") and GENIS_R.fullmatch(t) and self.isim_mi(g[:-2])
                        and self.tf.get(g[:-2], 0) > self.fiil[g]):
                    continue                                            # gözler = göz+ler, gözle+r değil
                yield g, "fiil"
                break
            else:
                isimler = [(s, s[-1] in UNLU, "ham")]
                if t[0] in UNLU and s[-1] in YUMUSAMA:                  # kitabı -> kitap, rengi -> renk
                    isimler.append((s[:-1] + YUMUSAMA[s[-1]], False, "yumusama"))
                if t[0] in UNLU and s in DUSME:                         # ağzı -> ağız
                    isimler.append((DUSME[s], False, "dusme"))
                if t[0] in UNLU and s in IKIZ:
                    isimler.append((IKIZ[s], False, "ikiz"))            # sırrı -> sır, hakkı -> hak (bitti değil)
                for g, unlu, onarim in isimler:
                    if self.isim_mi(g) and ISIM_KUYRUK[unlu].fullmatch(t) and self.isim_gecer(x, s, g, t, onarim):
                        yield g, "isim"
                        break

    def kok(self, w):
        w = w.translate(SAPKA)
        if w in self._on:
            return self._on[w]
        if w in ZAMIR:
            k = ZAMIR[w]
        elif w in ELLE:
            k = ELLE[w]
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
                    if sinif == "di":                         # ünlüden sonra yalnız -dı (bileti = bilet+i)
                        if s[-1] in UNLU and e not in unlu:
                            continue
                    elif sinif not in ("mak", "maya") and (e in unlu) != (s[-1] in UNLU):
                        continue
                    kanit[s][sinif] += n
                    if e[0] in UNLU and s[-1] == "d":        # gidip, ederek -> git-, et-
                        kanit[s[:-1] + "t"][sinif] += n
        return kanit

    def gecer(g, k):
        guclu = sum(1 for c in GUCLU_KANIT if k[c] >= 5)     # tek tük yazım hatası kanıt sayılmaz
        top = sum(k.values())
        bicim = len(g) >= 3 or (len(g) == 2 and (g[0] in UNLU or g in ("ye", "de")))
        return (bicim and top >= en_az_tf and (guclu >= 2 or (guclu >= 1 and k["di"] >= 20))
                and k["mak"] + k["di"] >= max(3, 0.005 * top))

    ilk = {g for g, k in say(False, set()).items() if gecer(g, k)}
    kanit = say(True, ilk)
    fiil = {g: k["mak"] + k["di"] for g, k in kanit.items() if gecer(g, k)}

    def asil(b):                                              # ed -> et, yi -> ye
        return b in fiil or (b[-1:] == "d" and b[:-1] + "t" in fiil) or b in ("yi", "di")

    def turemis(g):
        for ek in ("ma", "me", "yama", "yeme", "ama", "eme", "abil", "ebil", "yabil", "yebil"):
            if g.endswith(ek) and len(g) > len(ek) and asil(g[:-len(ek)]):
                return True
        if g[-1] in "ae" and g[:-1] in fiil:                  # bula- (bul+a-madı) atılır, kapa- (kapadı) kalır
            return kanit[g]["di"] < 0.05 * kanit[g[:-1]]["di"]
        if g[-1] == "y" and g[:-1] in fiil and g[-2] in UNLU and not kanit[g]["mak"]:
            return True                                        # oynay- (oyna+y)
        return False
    return {g: n for g, n in fiil.items() if not turemis(g)}


class F5Kokcu:
    """Tasarımın eski ölçümlerindeki kök: ilk 5 harf (OLAY_ORGUSU_PLANI.md 'ilk 5 harf kök eşleşmesi')."""

    def kok(self, w):
        return w.translate(SAPKA)[:5]


class ZemberekKokcu:
    """zemberek-python lemması; çözümlenemeyen kelimede ek soyma köküne düşer. Fiil lemması 'koşmak' -> 'koş-'."""

    def __init__(self, yedek):
        from zemberek import TurkishMorphology
        self.m = TurkishMorphology.create_with_defaults()
        self.yedek = yedek
        self._on = {}

    def kok(self, w):
        w = w.translate(SAPKA)
        if w not in self._on:
            analiz = list(self.m.analyze(w))
            if not analiz:
                self._on[w] = self.yedek.kok(w)
            else:
                item = analiz[0].item
                lemma = kucuk(item.lemma).translate(SAPKA)
                fiil = "Verb" in str(item.primary_pos)
                self._on[w] = re.sub("m[ae]k$", "", lemma) + "-" if fiil else lemma
        return self._on[w]


def zemberek_surumu():
    try:
        from importlib.metadata import version
        return version("zemberek-python")
    except Exception:
        return None


# ---------------------------------------------------------------- oluştur

YABANCI = {"the", "and", "was", "to", "they", "he", "she", "it", "is", "of", "in", "you", "off", "be", "we", "my",
           "old", "buy", "yes", "no", "oh", "a", "aaa", "aaah", "ooo", "mmm", "hmm"}   # sık listeye girmez (it- girer)


def ad_bicimleri(c, esik=0.5, en_az=5):
    """Cümle ortasında çoğunlukla büyük harfle geçen biçimler -> ad oranı (cümle ortası büyük / cümle ortası).
    Lily, Tim, Ayşe ~1,0; Pamuk, Kafa gibi karakter adı da olan sözcükler 0,5-0,9."""
    tf, b, o = c["tf"], c["buyuk"], c["orta_buyuk"]
    oran = {w: o[w] / max(1, n - b[w] + o[w]) for w, n in tf.items() if o[w] >= en_az}
    return {w: round(r, 3) for w, r in oran.items() if r >= esik}


def duz_sayim(yuzey):
    """Şapkası düzleştirilmiş sıklık (kök bulmak için): rüzgâr + rüzgar."""
    d = collections.Counter()
    for w, n in yuzey.items():
        d[w.translate(SAPKA)] += n
    return dict(d)


def kokcu_kur(yontem, yuzey, fiil, adlar):
    ek = Kokcu(duz_sayim(yuzey), fiil, adlar)
    if yontem == "f5":
        return F5Kokcu()
    if yontem == "zemberek":
        return ZemberekKokcu(ek)
    return ek


def kok_yontemi_sec(istenen):
    """otomatik: zemberek-python kurulu ve küçük bir öz-denetimden geçiyorsa Zemberek, değilse ek soyma."""
    if istenen != "otomatik":
        return istenen
    try:
        z = ZemberekKokcu(F5Kokcu())
        if z.kok("kitabı") == "kitap" and z.kok("koşuyordu") == "koş-" and z.kok("annesine") == "anne":
            return "zemberek"
        print("zemberek öz-denetimi tutmadı; ek soyma kullanılıyor", file=sys.stderr)
    except Exception as e:   # kurulu değil ya da API farklı
        if not isinstance(e, ImportError):
            print(f"zemberek kullanılamadı ({e!r}); ek soyma kullanılıyor", file=sys.stderr)
    return "ek"


TR_SIRA = {h: i for i, h in enumerate("abcçdefgğhıijklmnoöprsştuüvyz")}


def tr_anahtar(w):
    return [TR_SIRA.get(h, 100 + ord(h)) for h in w]


def olustur(args):
    import numpy as np
    from tokenizers import Tokenizer
    t0 = time.time()
    yontem = kok_yontemi_sec(args.kok)
    tok_yol = os.path.join(TS2, "tokenizer.json")
    tok = Tokenizer.from_file(tok_yol)
    tr, va = token_sayimi()
    denetim = kaynak_denetimi(tok, tr, va)
    n_ham = sum(1 for _ in hikayeler())
    denetim["ham_hikaye"] = n_ham
    if not denetim["ilk_hikayeler_ayni"] or n_ham != denetim["train_eot"] + denetim["val_eot"]:
        sys.exit(f"ham metin ile bin/tokenizer tutmuyor: {denetim}")
    print(f"kaynak denetimi tamam: {denetim} ({time.time() - t0:.0f} s)", file=sys.stderr)

    c = say(denetim["train_eot"])
    print(f"sayım: {c['n_hikaye']} hikâye, {c['n_kelime']:,} kelime, {len(c['tf']):,} biçim "
          f"({time.time() - t0:.0f} s)", file=sys.stderr)
    adlar = ad_bicimleri(c)
    yuzey = {w: n for w, n in c["tf"].items() if n >= args.cok_nadir}
    fiil = fiil_kokleri(duz_sayim(c["tf"]))
    kokcu = kokcu_kur(yontem, yuzey, fiil, adlar)
    kok = collections.Counter()
    uye = collections.defaultdict(list)
    for w, n in yuzey.items():
        if w in adlar:
            continue
        k = kokcu.kok(w)
        kok[k] += n
        uye[k].append((n, w))
    print(f"kök: {len(kok):,} ({yontem}), fiil gövdesi: {len(fiil)} ({time.time() - t0:.0f} s)", file=sys.stderr)

    def listeye_girer(k):
        g = k.rstrip("-")
        return (len(g) >= 2 or g == "o") and k not in YABANCI and not re.search("[âîû]", g)
    sik = [k for k, _ in sorted(kok.items(), key=lambda kv: (-kv[1], kv[0])) if listeye_girer(k)][:args.sik]
    sik_esik = kok[sik[-1]]

    tokfreq = np.bincount(np.asarray(tr), minlength=tok.get_vocab_size()).tolist()
    az = [i for i, n in enumerate(tokfreq) if n < args.az_token and tok.id_to_token(i) != EOT]
    sik_metin = (f"# sade_sozluk_sik.txt: Türkçe TinyStories ön eğitiminde en sık {len(sik)} kök "
                 f"(kök sıklığı >= {sik_esik}), alfabe sırasıyla.\n"
                 f"# Fiil kökleri '-' ile biter (koş- = koşmak, koştu, koşuyor). Kök yöntemi: {yontem}.\n"
                 f"# Yazım kılavuzu Kural 7: kelimeler bu listeden; hikâye başına en çok 2 liste dışı kelime.\n"
                 f"# Üreten: degerlendirme/sade_sozluk.py olustur; sıklıklar data/sade_sozluk.json'da.\n"
                 + "".join(k + "\n" for k in sorted(sik, key=tr_anahtar)))
    with open(args.sik_cikti, "w", encoding="utf-8") as f:
        f.write(sik_metin)
    k2 = sha256_dosya(K2_TOKENIZER) if os.path.exists(K2_TOKENIZER) else None
    d = {
        "aciklama": "Sade sözlük (KUSURSUZ_VERI.md Adım 0a, K3). yuzey: kelime biçimi -> ön eğitim train.bin "
                    "hikâyelerindeki sıklık (yalnız >= esikler.cok_nadir; listede olmayan biçim < cok_nadir). "
                    "kok: kök -> sıklık (adlar hariç). sik: sık kök listesi (sıklık sırası). fiil: fiil gövdesi -> "
                    "temel kanıt (-mak ve -dı biçimleri). token_sayim: train.bin'de token kimliği başına sayım. "
                    "sha256: 'sha256' alanı dışındaki içeriğin kanonik JSON'unun (sort_keys, ayraç ',' ':', "
                    "ensure_ascii=False) sha256'sı.",
        "surum": 1,
        "esikler": {"nadir": args.nadir, "cok_nadir": args.cok_nadir, "az_token": args.az_token,
                    "sik": args.sik, "sik_kok_en_az": sik_esik, "ad_orani": 0.5},
        "kok_yontemi": {"ad": yontem, "surum": "ek_soyma_1" if yontem == "ek" else
                        (zemberek_surumu() if yontem == "zemberek" else "f5")},
        "kaynak": {"ham": os.path.relpath(HAM, ROOT), "ham_sha256": sha256_dosya(HAM),
                   "train_bin_sha256": sha256_dosya(os.path.join(TS2, "train.bin")),
                   "val_bin_sha256": sha256_dosya(os.path.join(TS2, "val.bin")),
                   "tokenizer": os.path.relpath(tok_yol, ROOT), "tokenizer_sha256": sha256_dosya(tok_yol),
                   "k2_tokenizer": os.path.relpath(K2_TOKENIZER, ROOT), "k2_tokenizer_sha256": k2,
                   "denetim": denetim, "hikaye": c["n_hikaye"], "kelime": c["n_kelime"],
                   "bicim": len(c["tf"]), "token": int(len(tr))},
        "yuzey": dict(sorted(yuzey.items())),
        "adlar": {w: r for w, r in sorted(adlar.items()) if w in yuzey},
        "fiil": dict(sorted(fiil.items())),
        "kok": dict(sorted(kok.items())),
        "kok_ornek": {k: [w for _, w in sorted(uye[k], reverse=True)[:5]] for k in sik},
        "sik": sik,
        "sik_txt_sha256": hashlib.sha256(sik_metin.encode()).hexdigest(),
        "token_sayim": tokfreq,
        "az_token": az,
    }
    d["sha256"] = icerik_sha256(d)
    with open(args.cikti, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, sort_keys=True, indent=0)
        f.write("\n")
    print(f"yazıldı: {args.cikti} (sha256 {d['sha256'][:12]}), {args.sik_cikti} ({len(sik)} kök, en az {sik_esik}); "
          f"az token (<{args.az_token}): {len(az)}; {time.time() - t0:.0f} s", file=sys.stderr)


# ---------------------------------------------------------------- ölç (kapi.py bunu kullanır)

class Sozluk:
    def __init__(self, d, yol=None):
        self.d = d
        self.yol = yol
        self.esik = d["esikler"]
        self.tf = d["yuzey"]
        self.sik = set(d["sik"])
        self.adlar = d["adlar"]
        self.token_sayim = d["token_sayim"]
        self.kokcu = kokcu_kur(d["kok_yontemi"]["ad"], self.tf, d["fiil"], self.adlar)
        self._tok = None

    def kok(self, w):
        return self.kokcu.kok(kucuk(w))

    def tokenizer(self):
        if self._tok is None:
            from tokenizers import Tokenizer
            self._tok = Tokenizer.from_file(os.path.join(ROOT, self.d["kaynak"]["tokenizer"]))
        return self._tok

    def olc(self, metin, haric=(), token=True):
        """Metindeki nadir / çok nadir / liste dışı kelimeler, az görülmüş token'lar ve şapkalı kelimeler.
        haric: adlar ve izinli dünya kökleri (yüzey biçimi, düzleştirilmiş biçim ya da kökü eşleşen atlanır)."""
        haric_k = {kucuk(h).translate(SAPKA) for h in haric}
        haric_k |= {kucuk(p).translate(SAPKA) for h in haric for p in h.split()}
        ws = kelimeler(metin)
        say = [w for w in ws if w.translate(SAPKA) not in haric_k and self.kok(w).rstrip("-") not in haric_k]
        nadir = [w for w in say if self.tf.get(w, 0) < self.esik["nadir"]]
        cok_nadir = [w for w in say if self.tf.get(w, 0) < self.esik["cok_nadir"]]
        liste_disi = [w for w in say if self.kok(w) not in self.sik]
        sonuc = {"kelime": len(ws), "sayilan": len(say), "nadir": nadir, "cok_nadir": cok_nadir,
                 "liste_disi": liste_disi, "sapkali": [w for w in ws if re.search("[âîû]", w)],
                 "kokler": {w: self.kok(w) for w in dict.fromkeys(say)}}
        if token:
            tok = self.tokenizer()
            ad_tok = set()
            for h in haric:
                for v in (h, " " + h, h[:1].upper() + h[1:], " " + h[:1].upper() + h[1:]):
                    ad_tok |= set(tok.encode(v).ids)
            ids = tok.encode(metin).ids
            sonuc["az_token"] = [tok.decode([i]) for i in ids
                                 if self.token_sayim[i] < self.esik["az_token"] and i not in ad_tok]
        return sonuc


_YUKLU = {}


def yukle(yol=CIKTI):
    """data/sade_sozluk.json'u yükler (süreç içinde önbellekli)."""
    if yol not in _YUKLU:
        with open(yol, encoding="utf-8") as f:
            _YUKLU[yol] = Sozluk(json.load(f), yol)
    return _YUKLU[yol]


def olc(metin, haric=(), yol=CIKTI, token=True):
    return yukle(yol).olc(metin, haric, token)


def dogrula(yol=CIKTI, sik_yol=SIK_CIKTI, tokenizer=K2_TOKENIZER):
    """Sözlüğün kendi sha256'sı, sık liste dosyası ve tokenizer eşleşmesi (Adım 0 birim testi 3). Hata listesi döner."""
    with open(yol, encoding="utf-8") as f:
        d = json.load(f)
    hata = []
    if icerik_sha256(d) != d.get("sha256"):
        hata.append("sözlük içeriği sha256'sıyla tutmuyor")
    if os.path.exists(sik_yol) and sha256_dosya(sik_yol) != d.get("sik_txt_sha256"):
        hata.append(f"{os.path.relpath(sik_yol, ROOT)} sözlükteki sha256'yla tutmuyor")
    for yol_t, alan in ((tokenizer, None), (os.path.join(ROOT, d["kaynak"]["tokenizer"]), "tokenizer_sha256")):
        if not os.path.exists(yol_t):
            hata.append(f"tokenizer yok: {yol_t}")
        elif sha256_dosya(yol_t) != d["kaynak"]["tokenizer_sha256"]:
            hata.append(f"tokenizer sha256 tutmuyor: {os.path.relpath(yol_t, ROOT)}")
    return hata


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    alt = ap.add_subparsers(dest="komut", required=True)
    o = alt.add_parser("olustur")
    o.add_argument("--nadir", type=int, default=20)
    o.add_argument("--cok-nadir", type=int, default=5)
    o.add_argument("--az-token", type=int, default=200)
    o.add_argument("--sik", type=int, default=3000, help="sık kök listesinin boyu")
    o.add_argument("--kok", choices=("otomatik", "ek", "zemberek", "f5"), default="otomatik")
    o.add_argument("--cikti", default=CIKTI)
    o.add_argument("--sik-cikti", default=SIK_CIKTI)
    m = alt.add_parser("olc")
    m.add_argument("metin", help="metin ya da dosya yolu")
    m.add_argument("--haric", default="", help="virgülle ayrılmış adlar ve izinli kelimeler")
    m.add_argument("--sozluk", default=CIKTI)
    m.add_argument("--json", action="store_true")
    v = alt.add_parser("dogrula")
    v.add_argument("--sozluk", default=CIKTI)
    v.add_argument("--tokenizer", default=K2_TOKENIZER)
    a = ap.parse_args()
    if a.komut == "olustur":
        os.environ.setdefault("RAYON_NUM_THREADS", "1")
        os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
        return olustur(a)
    if a.komut == "dogrula":
        hata = dogrula(a.sozluk, tokenizer=a.tokenizer)
        print("\n".join(hata) if hata else "tamam: sözlük sha256, sık liste ve tokenizer eşleşiyor")
        return 1 if hata else 0
    metin = open(a.metin, encoding="utf-8").read() if os.path.exists(a.metin) else a.metin
    haric = [h.strip() for h in a.haric.split(",") if h.strip()]
    r = olc(metin, haric, a.sozluk)
    if a.json:
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return 0
    e = yukle(a.sozluk).esik
    print(f"kelime {r['kelime']} (sayılan {r['sayilan']})")
    print(f"nadir (<{e['nadir']}): {len(r['nadir'])}  {' '.join(r['nadir'])}")
    print(f"çok nadir (<{e['cok_nadir']}): {len(r['cok_nadir'])}  {' '.join(r['cok_nadir'])}")
    print(f"liste dışı: {len(r['liste_disi'])}  " + " ".join(f"{w}({r['kokler'][w]})" for w in r["liste_disi"]))
    print(f"az token (<{e['az_token']}): {len(r['az_token'])}  {' '.join(r['az_token'])}")
    print(f"şapkalı: {len(r['sapkali'])}  {' '.join(r['sapkali'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
