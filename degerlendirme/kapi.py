"""Kod kapıları: K1–K9 ve K11 (ret), K10 (yalnız rapor), K12 (kota; arayüz). KUSURSUZ_VERI.md Adım 0f, 5 ve
'Otomatik kontroller'. Bir hikâye ancak K1–K9 ve K11'de SIFIR ihlalle geçer; her ihlal kod + açıklama taşır.

Girdi: yazar dosyası bloğu (urun_kayit.ayristir) ya da kanonik kayıt + tohum kaydı. Adımlar (Adım 5):
  (1) normalizasyon (urun_kayit.normallestir), (2) kanonik kayıt ve sha1 kimlik, (3) kapılar sırayla.
Tohum kaydı (veri_hakem.py tohum üretir; JSON satırı): {"id", "figur", "yer", "yan": [kısa ad, ...],
  "ozellik": <kartta anahtar_kok>, "isim", "fiil" ('koş-' ya da 'koşmak'), "sifat", ...}; diğer alanlar okunmaz.

Kapılar (kod: açıklama; ayrıntı docs/KUSURSUZ_VERI.md):
  K1 biçim ve sahne   başlık/plan/tohum satırları, figür 14'ten biri, yer kartta ve tohumdaki, yan tohumdaki,
                      plan 3–9 küçük harfli kelime ve özel adsız, tek paragraf, tırnak dengeli, son . ! ya da ",
                      zaman atlaması ifadesi 0
  K2 uzunluk          gövde 70–100 kelime, cümle (tırnak içi dahil) <= 12 kelime, hf_c3ft_v6 ile gövde <= 150
                      token, en uzun eğitim dizgisi + EOT <= 200 token
  K3 sade sözlük      (plan + gövde) nadir (<20) <= 2, çok nadir (<5) <= 1, ön eğitimde < 20 görülmüş token 0
                      (adlar ve izinli dünya kökleri hariç), şapka 0 ('hâlâ' dahil), Ateşman >= 75 (ikincil)
  K4 kapalı dünya     büyük harfli ad ∈ {figür} ∪ {tohumdaki adlı yanlar}; öteki figürler, çıkarılanlar, eski 12,
                      kartın yasak adları, başka kartların yanları, sec.YABANCI ret; TEKİL canlı/rol lemması
                      (canli_rol.json) ∈ {figür türü} ∪ {tohum yanlarının yüzey biçimleri ve türü} ∪ {izinli dünya
                      kökleri, tohum dışı yanların türleri hariç}; belirsiz kelime (canli_rol.json) yalnız açık
                      cansız/oyuncak anlamında; cümle başındaki yaygın kelime sıfat olarak ('Kara bulutlar') ad
                      sayılmaz; tohumdaki her yan metinde; figür adı ilk 2 cümlede
                      ve son %40'ta; kartın yasak düzenli ifadeleri 0; tohum özelliğinin anahtar ifadesi >= 1;
                      tohumdaki isim, fiil ve sıfat lemmaları gövdede ('@degisim' ile en çok biri değişebilir)
  K5 biçimbilim       Zemberek çözümlemesi (kurulu değilse ATLANIR ve sonuçta 'atlanan' olarak yazılır);
                      kesme ekinin okunuşa uyumu (Tosbi'nın, Chase'den ret); sertleşme (koşdu, ağaçdan);
                      zaman kuralı: tırnak dışındaki yüklemin son zaman eki -dı (yalın -yor, -mış, -acak, geniş
                      zaman, -dır, var/yok/değil ret; -mış/-acak sıfat-fiilleri ve 'yiyecek' gibi adlar yüklem değil)
  K6 işaretler        ret değil, hakeme not: bitişik de/da ve ki şüphesi, çoğul arka plan canlıları, cansız
                      anlamda geçen belirsiz kelimeler (karakter anlamı K4 retidir), sec.py ve kontrol.py'nin sezgisel olay kuralları
  K7 güvenlik/sağlık  sec.GUVENLIK + ek kalıplar + hastalık kökleri; 'kanadı' yalnız vücut parçasından sonra kanama
  K8 tekrar           aynı cümle, 3-gram tekrarı > 2, 'X ve X', kekeme tekrar, kendine gönderme, kendine adıyla
                      seslenme, aynı konuşmacının ardışık iki cümlede konuşması, iki kez tanıtma
  K9 yakın kopya      havuza karşı: birebir, kelime 3-gram Jaccard >= 0,5, ROUGE-L >= 0,7
  K10 model kaybı     RAPOR (bu sürümde hesaplanmaz: k10_kayip() arayüzü)
  K11 kimlik/sürüm    'urun/<figür>#sha1[:10]'; beklenen sha1 tutmalı; kart onaylı olmalı (--taslak-kart ile
                      geçici izin, sonuçta 'taslak_kart': true); sözlük/tokenizer eşleşmesi; bileşen sha256'ları
  K12 kota            Aşama 1'de: KotaSayaci arayüzü

Kullanım: .venv/bin/python degerlendirme/kapi.py denetle <yazar dosyası> --tohum <tohum.jsonl> [--havuz <jsonl>]
                [--taslak-kart] [--json]
          .venv/bin/python degerlendirme/kapi.py surum [--json]
          nice -n 19 .venv/bin/python degerlendirme/kapi.py yanlis-alarm [--n 200] [--tohum 2026] [--ayrinti <yol>]
Kütüphane: bg = Baglam(); sonuc = denetle(blok, tohum, bg, havuz=(), taslak_kart=False)
"""
import argparse
import collections
import hashlib
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import sade_sozluk  # noqa: E402
import sec  # noqa: E402  (baslangic.py'yi de yükler: YABANCI)
import urun_kayit as uk  # noqa: E402
from urun_kayit import kucuk  # noqa: E402

KART = os.path.join(ROOT, "data", "urun_kartlari.json")
FIGUR = os.path.join(ROOT, "data", "urun_figurleri.json")
ESKI_FIGUR = os.path.join(ROOT, "data", "karakterler.json")
CANLI_ROL = os.path.join(ROOT, "data", "canli_rol.json")
TOHUM_KELIME = os.path.join(ROOT, "data", "tohum_kelimeleri.json")
IZINLI_KELIME = os.path.join(ROOT, "data", "izinli_kelimeler.json")          # henüz yok; varsa sürüme girer
ZEMBEREK_BEYAZ = os.path.join(ROOT, "data", "zemberek_beyaz_liste.txt")     # henüz yok; varsa sürüme girer
K2_TOKENIZER = os.path.join(ROOT, "hf_c3ft_v6", "tokenizer.json")
HAKEM = [os.path.join(HERE, f"HAKEM_{m}.md") for m in "MDK"]

HARF = "a-zçğıöşüâîû"
BUYUK = "A-ZÇĞİÖŞÜÂÎÛ"
H = f"{BUYUK}{HARF}"
UNLU = "aeıioöuüâîû"
SERT = "çfhkpsşt"
SAPKA = str.maketrans("âîû", "aiu")

ESIK = {"kelime": (70, 100), "cumle_kelime": 12, "token_govde": 150, "token_dizgi": 200, "nadir": 2,
        "cok_nadir": 1, "az_token": 20, "az_token_rapor": 200, "atesman": 75.0, "jaccard": 0.5, "rouge_l": 0.7,
        "uclu_tekrar": 2, "plan_kelime": (3, 9)}

# ---------------------------------------------------------------- K1: zaman atlaması (Kural 2; tasarım listesi +
# aynı anlamdaki çoğul/-ca biçimleri)
SAYI = r"(?:\d+|bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|birkaç|birçok|kaç)"
ZAMAN_ATLAMA = [
    (re.compile(r"\bertesi\b"), "ertesi"),
    (re.compile(rf"\b{SAYI}\s+(?:gün|hafta|ay|yıl)\s+(?:sonra|geçti|boyunca)\b"), "<sayı> gün/hafta/ay sonra"),
    (re.compile(r"\b(?:günler|haftalar|aylar|yıllar)\s+(?:sonra|geçti|boyunca)\b"), "günler sonra"),
    (re.compile(r"\b(?:akşama|sabaha)\s+kadar\b"), "akşama/sabaha kadar"),
    (re.compile(r"\bbütün\s+gün(?:ü|ünü)?\b"), "bütün gün"),
    (re.compile(r"\bo\s+gece\b"), "o gece"),
    (re.compile(r"\b(?:günlerce|haftalarca|aylarca|yıllarca)\b"), "günlerce"),
    (re.compile(r"\bher\s+sabah\b"), "her sabah"),
]
PLAN_BICIM = re.compile(rf"^[{HARF}]+(?:,? [{HARF}]+)*$")

# ---------------------------------------------------------------- K5
# sertleşme: sert ünsüzden sonra d/c (koşdu, ağaçdan); derlemde gerçek kelime olanlar
SERTLESME = re.compile(rf"[{SERT}][dc][aeıioöuü]")
SERTLESME_IZIN = ("takdir", "takdim", "akciğer", "dikdörtgen", "tehdit", "mahcup", "gökdelen", "dikdik", "akdeniz")
KONUSMA = ("dedi", "sordu", "bağırdı", "fısıldadı", "seslendi", "söyledi", "yanıtladı", "düşündü", "haykırdı",
           "mırıldandı", "açıkladı", "ekledi", "cevapladı", "diye")
# konuşma devriği ('"Gel," dedi annesi.'): cümle sonundaki ad atlanıp konuşma fiiline bakılır
KONUSMA_KOK = ("de-", "sor-", "bağır-", "fısılda-", "seslen-", "söyle-", "yanıtla-", "düşün-", "haykır-",
               "mırıldan-", "açıkla-", "ekle-", "cevapla-", "ver-", "anlat-", "sevin-", "gül-")
BAGLAC = {"ve", "ama", "fakat", "ancak", "çünkü", "sonra", "ya", "veya", "yoksa"}
GECMIS = re.compile(r"[dt][ıiuü](?:m|n|k|n[ıiuü]z|l[ae]r)?$")
YOR = re.compile(r"yor(?:um|sun|uz|sunuz|lar)?$")
MIS = re.compile(r"m[ıiuü]ş(?:[ıiuü]m|s[ıiuü]n|[ıiuü]z|s[ıiuü]n[ıiuü]z|l[ae]r)?$")
ACAK = re.compile(r"[ae]c(?:[ae]k|[ae]ğ[ıi]m|[ae]ks[ıi]n|[ae]ğ[ıi]z|[ae]kl[ae]r)$")
GENIS = re.compile(r"(?:[aeıiuü]r|m[ae]z)(?:[ıiuü]m|s[ıiuü]n|[ıiuü]z|l[ae]r)?$")
DIR = re.compile(r"[dt][ıiuü]r(?:l[ae]r)?$")
GEREKLILIK = re.compile(r"m[ae]l[ıi](?:y[ıi]m|s[ıi]n|y[ıi]z|l[ae]r)?$")
SIMDI_AD = {"var", "yok", "değil", "vardır", "yoktur", "değildir", "varlar", "yoklar"}
ACAK_AD = {"yiyecek", "içecek", "giyecek", "yatacak", "yiyecekler", "içecekler"}   # -acak biçimli adlar: yüklem değil

# ---------------------------------------------------------------- K7 (sec.GUVENLIK'e ek; tasarımdaki liste)
K7_GUVENLIK = [
    (re.compile(r"(?<![a-zçğıöşü])dizini(?![a-zçğıöşü])"), "dizini"),
    (re.compile(r"\bcanı\s+yan\w*"), "canı yandı"),
    (re.compile(r"\bsürüklen\w*"), "sürüklen-"),
    (re.compile(r"\bakıntı\w*"), "akıntı"),
    (re.compile(r"\b(?<!gözyaşlarına )boğul\w*"), "boğul-"),
    (re.compile(r"\byangın\w*"), "yangın"),
    (re.compile(r"\bbıça[kğ]\w*"), "bıçak"),
    (re.compile(r"\bila[çc]\w*"), "ilaç"),
    (re.compile(r"\byabancı\s+biri\w*"), "yabancı biri"),
    (re.compile(r"\bkana(?:mış|yan|yor|dığı|masın)\w*|\bkanatt[ıi]\w*"), "kanama"),
    (re.compile(r"\b(?:diz|el|elin|parma[kğ]|burn|burun|aya[kğ]|kol|baş|duda[kğ]|ağz|yüz|bacağ|bacak|kafa)"
                r"\w*\s+(?:[a-zçğıöşü]+\s+)?kanadı\b"), "vücut + kanadı"),
]
K7_SAGLIK = [
    (re.compile(r"\bhasta\w*"), "hasta"),
    (re.compile(r"\büşü(?!ş)\w*"), "üşü-"),
    (re.compile(r"\bhapşır\w*"), "hapşır-"),
    (re.compile(r"\böksür\w*"), "öksür-"),
    (re.compile(r"\bağrı\w*"), "ağrı"),
    (re.compile(r"\bbaşı[mn]?\s+dön\w*"), "başı dönüyor"),
    (re.compile(r"\bmide\w*\s+bulan\w*"), "midesi bulandı"),
    (re.compile(r"\bburn(?:u|um|un)\s+ak(?:ıyor|tı|ar|mış|ıyordu|mıştı)\w*"), "burnu akıyor"),
]
# sec.cezalar/olay_cezalari'nın kart adlarıyla çalışan hâli (K8) için
DIMINUTIF = re.compile(r"^(.+?)(?:c|ç)(?:ı|i|u|ü)(?:k|ğ)(?:ım|im|um|üm|ı|i|u|ü|lar|ler)?\w*$")
GENEL_ILISKI = {"arkadaş", "dost"}        # tohumda yan varsa o yana dönük sayılır
# canli_rol.json'da canlı/rol olarak geçen ama çocuk hikâyesinde çoğunlukla başka kelime olan eşsesliler: ret yerine
# belirsiz notu (karı = kar + belirtme eki; eşi = çorabın eşi). Liste canli_rol.json'a taşınınca buradan silinir.
ESSESLI_CANLI_ROL = {"karı": "kar + belirtme eki (karı temizledi)", "eş": "çift (çorabın eşi)"}
KONUSAN_NESNE = re.compile(r'(kabuk|taş|top|ağaç|çiçek)\w*,?\s+"'
                           r'|"\s*(?:dedi|diye sordu)\s+(?:kabuk|taş|top|ağaç|çiçek)')


def sha256_dosya(yol):
    return sade_sozluk.sha256_dosya(yol) if yol and os.path.exists(yol) else None


def kart_sha1(kart):
    metin = json.dumps(kart, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha1(metin.encode()).hexdigest()


def _olgu(x):
    return x.get("deger") if isinstance(x, dict) else x


def _desen(ifade):
    """Kelime sınırlı düzenli ifade (Türkçe harfler kelimenin parçası)."""
    return re.compile(rf"(?<![{H}]){re.escape(ifade).replace(chr(92) + ' ', r'\s+')}(?![{H}])")


# ---------------------------------------------------------------- bağlam (bir kez yüklenir)

class Baglam:
    """Kartlar, listeler, sade sözlük, K2 tokenizer'ı, Zemberek ve sürüm bilgisi."""

    def __init__(self, kart=KART, zemberek=True):
        self.kart_yolu = kart
        with open(kart, encoding="utf-8") as f:
            self.kart_dosyasi = json.load(f)
        self.kartlar = {_olgu(k["ad"]): k for k in self.kart_dosyasi["kartlar"]}
        with open(FIGUR, encoding="utf-8") as f:
            fig = json.load(f)
        self.figurler = [f["ad"] for f in fig["populer"] + fig["temel"]]
        self.cikarilanlar = list(fig["cikarilanlar"])
        with open(ESKI_FIGUR, encoding="utf-8") as f:
            self.eski = [k["isim"] for k in json.load(f)["karakterler"]]
        with open(CANLI_ROL, encoding="utf-8") as f:
            cr = json.load(f)
        self.canli, self.rol, self.belirsiz = set(cr["canli"]), set(cr["rol"]), set(cr["belirsiz"])
        # belirsizlerin cansız/oyuncak kalıpları (kullanıcı kararı: karakter olarak yasak, nesne olarak serbest)
        self.nesne_kaliplari = {w: [re.compile(k) for k in (v.get("nesne_kaliplari") or [])]
                                for w, v in cr["belirsiz"].items() if isinstance(v, dict)}
        with open(TOHUM_KELIME, encoding="utf-8") as f:
            tk = json.load(f)
        self.tohum_kelime = {"isim": set(tk["isim"]), "fiil": set(tk["fiil"]), "sifat": set(tk["sifat"])}
        self.tohum_kategori = {w: k for k, ws in tk.get("kategori", {}).items() for w in ws}   # kelime -> kategori
        self.canli_gerektirir = dict(tk.get("canli_gerektirir", {}))
        self.sozluk = sade_sozluk.yukle()
        self.sozluk_hatalari = sade_sozluk.dogrula()
        self._tok = None
        self.zemberek, self.zemberek_neden = (None, "istenmedi") if not zemberek else _zemberek_yukle()
        self.beyaz = set()
        if os.path.exists(ZEMBEREK_BEYAZ):
            with open(ZEMBEREK_BEYAZ, encoding="utf-8") as f:
                self.beyaz = {kucuk(s.strip()) for s in f if s.strip() and not s.startswith("#")}
        self._dunya = {}
        self.surum = surum_bilgisi(self)
        self.surum_ozeti = hashlib.sha256(json.dumps(self.surum, sort_keys=True).encode()).hexdigest()[:16]

    def tokenizer(self):
        if self._tok is None:
            from tokenizers import Tokenizer
            self._tok = Tokenizer.from_file(K2_TOKENIZER)
        return self._tok

    def kok(self, w):
        return self.sozluk.kok(w)

    def dunya(self, figur):
        if figur not in self._dunya:
            self._dunya[figur] = Dunya(self.kartlar[figur], self)
        return self._dunya[figur]

    def yaygin(self, ad):
        """Ad aynı zamanda sık bir ortak kelime mi (Pamuk, Bal, Can, Kara): cümle başında büyük harfle geçmesi ad
        olduğunu göstermez; yalnız cümle ortasında ya da kesme ekiyle ad sayılır."""
        w = kucuk(ad)
        tf = self.sozluk.tf.get(w, 0)
        return tf * (1 - (self.sozluk.adlar.get(w) or 0)) >= 50

    def urun_adlari(self):
        """Ürünün bütün adları (küçük harf): figürler, eski ve çıkarılan figürler, kart yanları ve kartların yasak
        adları. Çok kelimeli adlardan yalnız yaygın olmayan kelimeler girer ('Kara Vezir' -> vezir)."""
        if not hasattr(self, "_urun_adlari"):
            adlar = self.figurler + self.eski + self.cikarilanlar
            for k in self.kartlar.values():
                adlar += [y["kisa_ad"] for y in k["yanlar"] if y["tip"] == "adli"]
                adlar += [a["ad"] for a in k.get("yasaklar", {}).get("adlar", []) if not a.get("belirsiz")]
            self._urun_adlari = {kucuk(p) for a in adlar for p in a.split() if " " not in a or not self.yaygin(p)}
        return self._urun_adlari

    def ad_gibi(self, w):
        """Cümle başındaki büyük harfli kelime ad mı: sözlükte ad olarak geçiyor ya da kelime ve kökü nadir."""
        low = kucuk(w)
        if low in self.sozluk.adlar:
            return True
        s = self.sozluk
        return s.tf.get(low, 0) < 20 and s.d["kok"].get(s.kok(low), 0) < 20


_ZEMBEREK = []


def _zemberek_yukle():
    """(çözümleyici, neden); süreç içinde bir kez yüklenir (yükleme ~5 sn)."""
    if not _ZEMBEREK:
        _ZEMBEREK.append(_zemberek_kur())
    return _ZEMBEREK[0]


def _zemberek_kur():
    try:
        from zemberek import TurkishMorphology
    except Exception as e:  # kurulu değil
        return None, f"zemberek yok ({type(e).__name__}: {e})"
    try:
        return TurkishMorphology.create_with_defaults(), None
    except Exception as e:
        return None, f"zemberek yüklenemedi ({e!r})"


def surum_bilgisi(bg):
    """K11: bileşenlerin içerik sha256'ları. Git hash'i yetmez (commit edilmemiş değişikliği göstermez)."""
    import baslangic
    kod = {os.path.relpath(m.__file__, ROOT): sha256_dosya(m.__file__)
           for m in (sys.modules[__name__], uk, sade_sozluk, sec, baslangic)}
    veri = {os.path.relpath(y, ROOT): sha256_dosya(y) for y in
            (CANLI_ROL, TOHUM_KELIME, IZINLI_KELIME, ZEMBEREK_BEYAZ, sade_sozluk.CIKTI, sade_sozluk.SIK_CIKTI,
             bg.kart_yolu, FIGUR, ESKI_FIGUR, *HAKEM)}
    try:
        from importlib.metadata import version
        zv = version("zemberek-python")
    except Exception:
        zv = None
    return {"kod": kod, "veri": veri, "serilestirme": uk.SURUM,
            "kartlar": {kimlik: kart_sha1(k) for kimlik, k in
                        ((k["kimlik"], k) for k in bg.kart_dosyasi["kartlar"])},
            "tokenizer": {"k2": sha256_dosya(K2_TOKENIZER),
                          "sozluk": bg.sozluk.d["kaynak"]["tokenizer_sha256"]},
            "sade_sozluk_icerik": bg.sozluk.d.get("sha256"), "zemberek": zv,
            "kok_yontemi": bg.sozluk.d.get("kok_yontemi")}


class Dunya:
    """Bir figürün kartından türetilen kümeler."""

    def __init__(self, kart, bg):
        self.kart = kart
        self.ad = _olgu(kart["ad"])
        self.okunus = _olgu(kart.get("okunus")) or kucuk(self.ad)
        self.tur = kart["tur"].get("lemmalar") or [_olgu(kart["tur"])]
        self.yerler = [y["etiket"] for y in kart["yerler"]]
        self.yanlar = {y["kisa_ad"]: y for y in kart["yanlar"]}
        self.izinli = list(kart.get("izinli_dunya_kokleri", []))
        self.ozellik = {o["anahtar_kok"]: o for o in kart["ozellikler"]}
        self.kurallar = [(k["kural"], re.compile(d)) for k in kart.get("dunya_kurallari", [])
                         for d in k.get("yasak_duzenli_ifadeler", [])]
        self.k7_izinli = [re.compile(d) for d in kart.get("k7_izinli", [])]   # figüre özel K7 beyaz listesi
        self.okunuslar = {self.ad: self.okunus}
        for y in kart["yanlar"]:
            self.okunuslar[y["kisa_ad"]] = y.get("okunus") or kucuk(y["kisa_ad"])

    def yan_bicimleri(self, y):
        return [y["kisa_ad"]] + list(y.get("yuzey_bicimleri", []))


# ---------------------------------------------------------------- yardımcılar

def _cumle_basi(metin, i):
    j = i - 1
    while j >= 0 and metin[j] in " \n\t(":
        j -= 1
    return j < 0 or metin[j] in '.!?…:"'


def _tirnak_disi(metin):
    """Tırnak dışı metin; tırnak içi '¶' ile değiştirilir (dengesiz tırnakta son açılış metnin sonuna kadar sürer)."""
    parca = metin.split('"')
    return " ".join(p if i % 2 == 0 else " ¶ " for i, p in enumerate(parca))


def _kelime_konum(metin):
    return [(m.group(0), m.start(), m.end()) for m in re.finditer(rf"[{H}]+(?:'[{HARF}]+)?|¶", metin)]


def atesman(metin):
    """Ateşman okunabilirliği: 198,825 − 40,175·(hece/kelime) − 2,610·(kelime/cümle)."""
    ks = re.findall(rf"[{H}]+", metin)
    if not ks:
        return 0.0
    hece = sum(sum(c in UNLU for c in kucuk(k)) for k in ks)
    n_cumle = max(1, len(uk.cumleler(metin)))
    return round(198.825 - 40.175 * hece / len(ks) - 2.610 * len(ks) / n_cumle, 1)


def _ihlal(liste, kod, aciklama):
    liste.append({"kod": kod, "kapi": kod.split(".")[0], "aciklama": aciklama})


def _not(liste, kod, mercek, aciklama):
    liste.append({"kod": kod, "mercek": mercek, "aciklama": aciklama})


# ---------------------------------------------------------------- K1

def k1(blok, kayit, tohum, bg, ih):
    for h in blok.get("bicim_hatalari", []):
        _ihlal(ih, "K1.bicim", h)
    if kayit["figur"] not in bg.figurler:
        _ihlal(ih, "K1.figur", f"figür 14 ürün figüründen biri değil: {kayit['figur']!r}")
        return
    if kayit["figur"] not in bg.kartlar:
        _ihlal(ih, "K1.figur", f"figürün kartı yok: {kayit['figur']}")
        return
    d = bg.dunya(kayit["figur"])
    if tohum is None:
        _ihlal(ih, "K1.tohum", f"tohum kaydı bulunamadı: {blok.get('tohum')!r}")
    else:
        if blok.get("tohum") != tohum.get("id"):
            _ihlal(ih, "K1.tohum", f"@tohum {blok.get('tohum')!r} tohum kaydıyla tutmuyor ({tohum.get('id')!r})")
        if tohum.get("figur") != kayit["figur"]:
            _ihlal(ih, "K1.tohum", f"tohumun figürü {tohum.get('figur')!r}, başlıkta {kayit['figur']!r}")
        if kayit["yer"] != tohum.get("yer"):
            _ihlal(ih, "K1.yer", f"yer {kayit['yer']!r} tohumdaki yer değil ({tohum.get('yer')!r})")
        if kayit["yan"] != list(tohum.get("yan", [])):
            _ihlal(ih, "K1.yan", f"yan {kayit['yan']} tohumdaki yan değil ({tohum.get('yan')})")
    if kayit["yer"] not in d.yerler:
        _ihlal(ih, "K1.yer", f"yer {kayit['yer']!r} kartta yok ({', '.join(d.yerler)})")
    for y in kayit["yan"]:
        if y not in d.yanlar:
            _ihlal(ih, "K1.yan", f"yan {y!r} kartta yok")
    adlar = {kucuk(w) for a in bg.figurler + bg.eski + bg.cikarilanlar if not bg.yaygin(a) for w in a.split()}
    adlar |= {kucuk(w) for w in kayit["figur"].split() if not bg.yaygin(w)}
    for k in bg.kartlar.values():
        adlar |= {kucuk(w) for y in k["yanlar"] if y["tip"] == "adli" for w in y["kisa_ad"].split()
                  if not bg.yaygin(w)}
    for ad, p in (("sorun", kayit["sorun"]), ("çözüm", kayit["cozum"])):
        n = len(p.split())
        if not PLAN_BICIM.match(p) or not ESIK["plan_kelime"][0] <= n <= ESIK["plan_kelime"][1]:
            _ihlal(ih, "K1.plan", f"plan {ad} {n} kelime ya da küçük harf dışı karakter: {p[:50]!r}")
        ozel = [w for w in re.findall(rf"[{H}]+", p) if kucuk(w) in adlar]
        if ozel:
            _ihlal(ih, "K1.plan_ad", f"plan {ad} özel ad içeriyor: {ozel}")
    g = kayit["govde"]
    if "\n" in g:
        _ihlal(ih, "K1.paragraf", "gövde tek paragraf değil")
    if g.count('"') % 2:
        _ihlal(ih, "K1.tirnak", "tırnaklar dengesiz")
    if not g or g[-1] not in '.!"':
        _ihlal(ih, "K1.son", f"son karakter . ! ya da \" değil: {g[-15:]!r}")
    elif g[-1] == '"' and not re.search(r'[.!?…]"$', g):
        _ihlal(ih, "K1.son", f"tırnakla biten son cümle noktalamasız: {g[-15:]!r}")
    metin = kucuk(f"{kayit['sorun']} {kayit['cozum']} {g}")
    for desen, ad in ZAMAN_ATLAMA:
        m = desen.search(metin)
        if m:
            _ihlal(ih, "K1.zaman", f"zaman atlaması ({ad}): {m.group(0)!r}")


# ---------------------------------------------------------------- K2

def k2(kayit, bg, ih, rapor):
    g = kayit["govde"]
    n = len(g.split())
    rapor["kelime"] = n
    if not ESIK["kelime"][0] <= n <= ESIK["kelime"][1]:
        _ihlal(ih, "K2.uzunluk", f"gövde {n} kelime (70–100)")
    cs = uk.cumleler(g)
    rapor["cumle"] = len(cs)
    for i, c in enumerate(cs, 1):
        nk = len([t for t in c.split() if re.search(rf"[{H}0-9]", t)])
        if nk > ESIK["cumle_kelime"]:
            _ihlal(ih, "K2.cumle", f"cümle {i} {nk} kelime (<= 12): {c[:60]!r}")
    tok = bg.tokenizer()
    tg = len(tok.encode(g).ids)
    td = len(tok.encode(uk.dizgi(kayit, plan=True, yan_alani=True)).ids) + 1
    rapor["token_govde"], rapor["token_dizgi"] = tg, td
    if tg > ESIK["token_govde"]:
        _ihlal(ih, "K2.token", f"gövde {tg} token (<= 150)")
    if td > ESIK["token_dizgi"]:
        _ihlal(ih, "K2.token", f"en uzun eğitim dizgisi + EOT {td} token (<= 200)")


# ---------------------------------------------------------------- K3

def haric_listesi(kayit, bg):
    """K3'te sayılmayanlar: figür adı, tohum yanlarının kısa adları ve yüzey biçimleri, izinli dünya kökleri."""
    if kayit["figur"] not in bg.kartlar:
        return [kayit["figur"]]
    d = bg.dunya(kayit["figur"])
    h = [d.ad]
    for y in kayit["yan"]:
        if y in d.yanlar:
            h += d.yan_bicimleri(d.yanlar[y])
    return h + d.izinli


def az_token(bg, kayit, haric, esik):
    """[(token, ön eğitim sayısı)]: eğitim dizgisinin (planlı, Yan alanlı) plan ve gövde token'larından ön eğitimde
    esik'ten az görülenler. Token'lar dizginin içinde sayılır (plan başındaki kelime ' rüzgar' olarak kodlanır);
    başlığın sabit kalıbı ile adların ve izinli köklerin token'ları hariç (sade_sozluk.Sozluk.olc ile aynı dışlama)."""
    tok = bg.sozluk.tokenizer()
    ad_tok = set()
    for h in haric:
        for v in (h, " " + h, h[:1].upper() + h[1:], " " + h[:1].upper() + h[1:]):
            ad_tok |= set(tok.encode(v).ids)
    d = uk.dizgi(kayit, plan=True, yan_alani=True)
    b_sorun = d.index("\nSorun: ") + len("\nSorun: ")
    b_cozum = d.index("\nÇözüm: ", b_sorun) + len("\nÇözüm: ")
    b_govde = d.index("\n\n", b_cozum) + 2
    alanlar = [(b_sorun, b_sorun + len(kayit["sorun"])), (b_cozum, b_cozum + len(kayit["cozum"])), (b_govde, len(d))]
    say = bg.sozluk.token_sayim
    enc = tok.encode(d)
    return [(tok.decode([i]), say[i]) for i, (s, e) in zip(enc.ids, enc.offsets)
            if say[i] < esik and i not in ad_tok and any(s < b and e > a for a, b in alanlar)]


def k3(kayit, bg, ih, rapor):
    haric = haric_listesi(kayit, bg)
    metin = f"{kayit['sorun']} {kayit['cozum']} {kayit['govde']}"
    o = bg.sozluk.olc(metin, haric=haric, token=False)
    rapor.update({"nadir": o["nadir"], "cok_nadir": o["cok_nadir"], "liste_disi": o["liste_disi"]})
    if len(o["nadir"]) > ESIK["nadir"]:
        _ihlal(ih, "K3.nadir", f"tr-tinystories'te 20'den az geçen {len(o['nadir'])} kelime (<= 2): {o['nadir']}")
    if len(o["cok_nadir"]) > ESIK["cok_nadir"]:
        _ihlal(ih, "K3.cok_nadir", f"5'ten az geçen {len(o['cok_nadir'])} kelime (<= 1): {o['cok_nadir']}")
    if o["sapkali"]:
        _ihlal(ih, "K3.sapka", f"normalizasyondan sonra şapkalı kelime: {o['sapkali']}")
    az = az_token(bg, kayit, haric, ESIK["az_token_rapor"])
    az20 = [t for t, n in az if n < ESIK["az_token"]]
    rapor["az_token_200"], rapor["az_token_20"] = [t for t, _ in az], az20
    if az20:
        _ihlal(ih, "K3.az_token", f"ön eğitimde 20'den az görülmüş token: {az20}")
    a = atesman(kayit["govde"])
    rapor["atesman"] = a
    if a < ESIK["atesman"]:
        _ihlal(ih, "K3.atesman", f"Ateşman {a} (>= 75)")


# ---------------------------------------------------------------- K4

def _izinli_adlar(d, yanlar):
    """Metinde büyük harfle geçebilecek kelimeler (küçük harfle): figür adı ve türü (Kraliçe Elsa) + tohum
    yanlarının adları, yüzey biçimleri ve türleri."""
    izin = {kucuk(w) for x in [d.ad] + d.tur for w in re.findall(rf"[{H}]+(?:-[{H}]+)*", x)}
    for y in yanlar:
        if y in d.yanlar:
            for b in d.yan_bicimleri(d.yanlar[y]) + [_olgu(d.yanlar[y].get("tur")) or ""]:
                izin |= {kucuk(w) for w in re.findall(rf"[{H}]+(?:-[{H}]+)*", b)}
    return izin


def yasak_adlar(bg, figur, yanlar):
    """(ifade, tür, belirsiz) listesi: bu figürün tohumlu hikâyesinde geçemeyecek adlar."""
    d = bg.dunya(figur)
    izin = _izinli_adlar(d, yanlar)
    liste = []

    def ekle(ifade, tur, belirsiz=False):
        if all(kucuk(w) in izin for w in re.findall(rf"[{H}]+(?:-[{H}]+)*", ifade)):
            return
        liste.append((ifade, tur, belirsiz or bg.yaygin(ifade)))
    for f in bg.figurler:
        if f != figur:
            ekle(f, "baska_figur")
    for f in bg.cikarilanlar:
        ekle(f, "cikarilan_figur")
    for f in bg.eski:
        if f != figur:
            ekle(f, "eski_figur")
    for a in d.kart.get("yasaklar", {}).get("adlar", []):
        ekle(a["ad"], "kart_yasak", bool(a.get("belirsiz")))
    for y in d.kart["yanlar"]:
        if y["kisa_ad"] not in yanlar and y["tip"] == "adli":
            for b in d.yan_bicimleri(y):
                if b[:1].isupper():
                    ekle(b, "tohum_disi_yan")
    for k in bg.kartlar.values():
        if _olgu(k["ad"]) == figur:
            continue
        for y in k["yanlar"]:
            if y["tip"] == "adli" and y["kisa_ad"][:1].isupper():
                ekle(y["kisa_ad"], "baska_kartin_yani")
        for a in k.get("yasaklar", {}).get("adlar", []):
            ekle(a["ad"], "baska_kartin_yasagi", bool(a.get("belirsiz")))
    for n in sec.YABANCI:
        ekle(n, "yabanci_ad")
    return liste


def yabanci_adlar(bg):
    """sec.YABANCI'nın ürün yanlarından ayıklanmış hâli (Adım 0f: 'Anna', 'Mert' ürün yanıdır). Tohumlu hikâyede
    kapı zaten tohum yanlarını önce izinli sayar; bu liste secici.h gibi tohumsuz yasak listeleri içindir."""
    yanlar = {w for k in bg.kartlar.values() for y in k["yanlar"] for b in [y["kisa_ad"]] + y.get("yuzey_bicimleri", [])
              for w in b.split()}
    return [n for n in sec.YABANCI if n not in yanlar and n not in bg.figurler]


def _canli_izin(d, yanlar, bg):
    """Tekil geçebilecek canlı/rol lemmaları."""
    izin = set(d.tur)
    tohum_disi = set()
    for ad, y in d.yanlar.items():
        hedef = izin if ad in yanlar else tohum_disi
        for b in d.yan_bicimleri(y) + [_olgu(y.get("tur")) or ""]:
            for w in re.findall(rf"[{H}]+", b):
                hedef |= {kucuk(w), bg.kok(kucuk(w))}
    izin |= {k for k in d.izinli if k not in tohum_disi - izin}
    return izin


def _ad_kaldir(metin, ifadeler):
    """İfadeleri (küçük harfli metinde, kesme ekleriyle birlikte) boşlukla örter; uzunluk korunur."""
    for i in sorted(ifadeler, key=len, reverse=True):
        metin = re.sub(rf"(?<![{H}]){re.escape(kucuk(i))}(?:'[{HARF}]+)?(?![{H}])",
                       lambda m: " " * len(m.group(0)), metin)
    return metin


def _canli_rol_lemma(w, bg):
    """Kelime bir canlı/rol lemması mı (kök, kendisi ya da küçültmesi): lemma ya da None."""
    k = bg.kok(w)
    if k.endswith("-"):
        return None
    adaylar = [k, w]
    m = DIMINUTIF.match(w)
    if m:
        adaylar += [m.group(1), bg.kok(m.group(1))]
    return next((a for a in adaylar if (a in bg.canli or a in bg.rol) and a not in ESSESLI_CANLI_ROL), None)


def belirsiz_nesne_mi(low, bas, son, lemma, bg):
    """Belirsiz kelimenin bu geçişi açıkça cansız/oyuncak anlamında mı: önündeki iki kelimede 'oyuncak', hemen
    ardından bir canlı/rol ismi (sıfat kullanımı: 'yaşlı at'; o isim ayrıca denetlenir) ya da canli_rol.json'daki
    nesne kalıplarından biri geçişi kapsıyor ('bir sürü', 'meşe palamudu')."""
    once = re.findall(rf"[{HARF}]+", low[max(0, bas - 40):bas])[-2:]
    if "oyuncak" in once:
        return True
    if re.match(r" {2,}", low[son:]):          # ardından örtülmüş figür/yan adı: 'Bilge Tosbi' (addaki sıfat)
        return True
    sonra = re.match(rf"\s+([{HARF}]+)", low[son:])
    if sonra and _canli_rol_lemma(sonra.group(1), bg):
        return True
    return any(m.start() <= bas and son <= m.end()
               for k in bg.nesne_kaliplari.get(lemma, []) for m in k.finditer(low))


def canli_rol_tara(govde, d, yanlar, bg):
    """(ihlaller, notlar): tekil kart dışı canlı/rol, çoğul canlı ve belirsiz kelimeler. Belirsiz kelime (canli_rol.json
    'belirsiz') kullanıcı kararıyla KARAKTER olarak yasaktır: açıkça cansız/oyuncak anlamında değilse ihlaldir
    (lemma, 'belirsiz:' önekiyle); cansızsa K merceğine not gider. Kartın izinli dünya kökü olanlar (Rafadan
    Tayfa'da 'bakkal', Doru'da 'sürü') ve eşsesliler (karı, eş) yalnız nottur."""
    ifadeler = [d.ad] + [b for y in yanlar if y in d.yanlar for b in d.yan_bicimleri(d.yanlar[y])]
    low = _ad_kaldir(kucuk(govde.replace("’", "'")), ifadeler)
    izin = _canli_izin(d, yanlar, bg)
    if "kardeş" in izin:                                   # kız kardeşi: 'kız' ayrı bir karakter değil
        low = re.sub(r"\b(kız|erkek)(?=\s+kardeş)", lambda m: " " * len(m.group(0)), low)
    low = sade_sozluk.KESME_EKI.sub(lambda m: " " * len(m.group(0)), low)   # konum korunur (kelimeler() ile aynı)
    hayvan_var = any(t in bg.canli for t in izin)
    ih, nt = [], []
    for km in sade_sozluk.KELIME.finditer(low):
        w = km.group(0)
        k = bg.kok(w)
        if k.endswith("-"):
            continue
        adaylar = [k, w]
        m = DIMINUTIF.match(w)
        if m:
            adaylar += [m.group(1), bg.kok(m.group(1))]
        isabet = [a for a in adaylar if (a in bg.canli or a in bg.rol) and a not in ESSESLI_CANLI_ROL]
        if w == "at" and re.match(r"\s*(?:[.!?,;:\"'”)]|$)", low[km.end():]):
            continue                                       # cümle sonundaki yalın 'at' emirdir: 'Önce sen at!'
        if not isabet:
            b = [a for a in adaylar if a in bg.belirsiz or a in ESSESLI_CANLI_ROL]
            if not b:
                continue
            if b[0] in ESSESLI_CANLI_ROL or b[0] in izin or belirsiz_nesne_mi(low, km.start(), km.end(), b[0], bg):
                nt.append(("belirsiz", w, b[0]))
            else:
                ih.append((w, "belirsiz:" + b[0]))
            continue
        lemma = isabet[0]
        if w.startswith(lemma) and w[len(lemma):].startswith(("lar", "ler")):
            nt.append(("cogul", w, lemma))
        elif lemma in izin or (lemma in GENEL_ILISKI and yanlar) or (lemma == "hayvan" and hayvan_var):
            continue
        else:
            ih.append((w, lemma))
    return ih, nt


def _sifat_kullanimi(g, son, w, bg):
    """Cümle başındaki büyük harfli yaygın kelime ad değil de sıfat mı ('Kara bulutlar', 'Pamuk gibi'): ardından
    küçük harfli, fiil ya da bağlaç olmayan bir kelime gelir. Ürün adları (figür, yan, eski ve çıkarılan figürler)
    yalnız 'gibi' ile sıfat sayılır: 'Pamuk koştu' da 'Pamuk çok sevindi' de ad kalır."""
    sonra = re.match(rf" +([{HARF}]+)", g[son:])
    if not sonra:
        return False
    s = sonra.group(1)
    if s == "gibi":
        return True
    if not bg.yaygin(w) or kucuk(w) in bg.urun_adlari() or s in BAGLAC | {"ile", "da", "de", "ki", "ise"}:
        return False
    return not bg.kok(s).endswith("-")


def _var_mi(desen, metin):
    return re.search(rf"(?<![{H}]){desen}(?![{H}])", metin) is not None


def _lemma_var(lemma, govde, bg):
    """Tohum lemması gövdede var mı (kök eşleşmesi; fiil 'koş-')."""
    lemma = kucuk(lemma)
    if lemma.endswith(("mak", "mek")) and not lemma.endswith("-"):
        lemma = lemma[:-3] + "-"
    govde_k = sade_sozluk.kelimeler(govde)
    kok = lemma.rstrip("-")
    for w in govde_k:
        wk = bg.kok(w)
        if wk == lemma or w == kok or (not lemma.endswith("-") and wk == kok):
            return True
        if len(kok) >= 4 and w.startswith(kok) and wk.rstrip("-").startswith(kok):
            return True
    return False


def k4(blok, kayit, tohum, bg, ih, nt):
    if kayit["figur"] not in bg.kartlar:
        return
    d = bg.dunya(kayit["figur"])
    g = kayit["govde"]
    yanlar = kayit["yan"]
    izin = _izinli_adlar(d, yanlar)
    # adlar: açık yasak listesi
    raporlanan = set()
    for ifade, tur, belirsiz in yasak_adlar(bg, kayit["figur"], yanlar):
        for m in _desen(ifade).finditer(g):
            kesme = g[m.end():m.end() + 1] == "'"
            if belirsiz and _cumle_basi(g, m.start()) and not kesme:
                continue
            _ihlal(ih, f"K4.{tur}", f"{tur.replace('_', ' ')}: {ifade}")
            raporlanan |= {kucuk(w) for w in ifade.split()}
            break
    # adlar: genel kural (büyük harfli her ad izinli kümede)
    bilinmeyen = []
    for m in re.finditer(rf"(?<![{H}])([{BUYUK}][{H}]*(?:-[{H}]+)*)('[{HARF}]+)?", g):
        w = m.group(1)
        low = kucuk(w)
        if low in izin or low in raporlanan or low in bilinmeyen:
            continue
        if _cumle_basi(g, m.start()) and not m.group(2) and (not bg.ad_gibi(w) or _sifat_kullanimi(g, m.end(), w, bg)):
            continue
        bilinmeyen.append(low)
        _ihlal(ih, "K4.ad", f"izinli olmayan ad: {w} (izinli: {d.ad}" + (f", {', '.join(yanlar)})" if yanlar else ")"))
    # canlı / rol
    kotu, notlar = canli_rol_tara(g, d, yanlar, bg)
    for w, lemma in dict.fromkeys(kotu):
        if lemma.startswith("belirsiz:"):
            _ihlal(ih, "K4.belirsiz", f"belirsiz kelime karakter olarak yasak (yalnız açık cansız/oyuncak anlamı "
                                      f"geçer: 'oyuncak {lemma[9:]}'): {w}")
        else:
            _ihlal(ih, "K4.canli_rol", f"kart/tohum dışı tekil canlı ya da rol: {w} ({lemma})")
    for tur, w, lemma in dict.fromkeys(notlar):
        if tur == "cogul":
            _not(nt, "K6.cogul_canli", "K,D", f"çoğul canlı (arka plan olmalı; konuşmaz, olaya katılmaz): {w}")
        else:
            _not(nt, "K6.belirsiz", "K", f"belirsiz kelime cansız/oyuncak anlamında olmalı; canlı, konuşan ya da "
                                         f"rol ise K6 ihlalidir: {w} ({lemma})")
    # tohumdaki her yan metinde
    kelimeler = sade_sozluk.kelimeler(g)
    kokler = {bg.kok(w) for w in kelimeler} | set(kelimeler)
    for y in yanlar:
        if y not in d.yanlar:
            continue
        var = False
        for b in d.yan_bicimleri(d.yanlar[y]):
            if " " in b or "-" in b:
                var |= _var_mi(re.escape(kucuk(b)).replace(r"\ ", r"\s+"), kucuk(g))
            else:
                var |= kucuk(b) in kokler or bg.kok(kucuk(b)) in kokler
        if not var:
            _ihlal(ih, "K4.yan_sayisi", f"tohumdaki yan metinde yok: {y}")
    # figür adı ilk 2 cümlede ve son %40'ta
    ad_d = _desen(d.ad)
    cs = uk.cumleler(g)
    if not ad_d.search(" ".join(cs[:2])):
        _ihlal(ih, "K4.figur_bas", f"{d.ad} ilk 2 cümlede yok")
    if not ad_d.search(g[int(len(g) * 0.6):]):
        _ihlal(ih, "K4.figur_son", f"{d.ad} son %40'ta yok")
    # kartın yasak düzenli ifadeleri (plan ve gövde)
    for kural, desen in d.kurallar:
        for alan in (kayit["sorun"], kayit["cozum"], g):
            m = desen.search(alan)
            if m:
                _ihlal(ih, "K4.dunya_kurali", f"{kural} -> {m.group(0)!r}")
                break
    if tohum is None:
        return
    # tohum özelliği
    oz = tohum.get("ozellik")
    if oz not in d.ozellik:
        _ihlal(ih, "K4.ozellik", f"tohum özelliği kartta yok: {oz!r}")
    elif not re.search(d.ozellik[oz]["anahtar_ifade"], kucuk(g)):
        _ihlal(ih, "K4.ozellik", f"tohum özelliğinin anahtar kökü gövdede yok: {oz}")
    # tohum kelimeleri
    beklenen = {"isim": tohum.get("isim"), "fiil": tohum.get("fiil"), "sifat": tohum.get("sifat")}
    deg = blok.get("degisim")
    if deg:
        eski, yeni = (kucuk(x) for x in deg)
        tur = next((t for t, v in beklenen.items() if v and _ayni_lemma(v, eski)), None)
        if tur is None:
            _ihlal(ih, "K4.degisim", f"@degisim: {eski!r} tohum kelimesi değil")
        else:
            yeni_l = _fiil_bicimi(yeni) if tur == "fiil" else yeni
            if yeni_l not in bg.tohum_kelime[tur]:
                _ihlal(ih, "K4.degisim", f"@degisim: {yeni!r} tohum_kelimeleri.json {tur} listesinde değil")
            beklenen[tur] = yeni_l
    for tur, lemma in beklenen.items():
        if not lemma:
            _ihlal(ih, "K4.tohum_kelime", f"tohumda {tur} yok")
        elif not _lemma_var(lemma, g, bg):
            _ihlal(ih, "K4.tohum_kelime", f"tohum {tur}i gövdede yok: {lemma}")


def _fiil_bicimi(w):
    w = kucuk(w)
    return w if w.endswith("-") else (w[:-3] + "-" if w.endswith(("mak", "mek")) else w + "-")


def _ayni_lemma(a, b):
    a, b = kucuk(a), kucuk(b)
    return a == b or a.rstrip("-") == b.rstrip("-") or (a.endswith("-") and _fiil_bicimi(a) == _fiil_bicimi(b))


# ---------------------------------------------------------------- K5

def _son_unlu(s):
    for c in reversed(s):
        if c in UNLU:
            return c.translate(SAPKA)
    return "e"


def _beklenen_unlu(onceki, unlu):
    if unlu in "ae":
        return "a" if onceki in "aıou" else "e"
    if unlu in "ıiuü":
        return {"a": "ı", "ı": "ı", "e": "i", "i": "i", "o": "u", "u": "u", "ö": "ü", "ü": "ü"}[onceki]
    return unlu


def kesme_eki_hatasi(okunus, ek):
    """Kesmeden sonraki ekin okunuşa uyumu: ünlü uyumu, kaynaştırma ve sertleşme. Hata açıklaması ya da None."""
    ok = kucuk(okunus).translate(SAPKA).replace("-", " ").strip()
    ek = kucuk(ek).translate(SAPKA)
    if not ek or not ok:
        return None
    son = ok[-1]
    unlu_son = son in UNLU
    if unlu_son and ek[0] in UNLU:
        return "ünlüyle biten addan sonra kaynaştırma ünsüzü yok"
    if not unlu_son and re.match(r"y[aeıiuü]", ek):
        return "ünsüzle biten addan sonra 'y' kaynaştırması"
    if not unlu_son and re.match(r"n[ıiuü]n", ek):
        return "ünsüzle biten addan sonra -nın"
    if son in SERT and ek[0] in "dc":
        return "sert ünsüzden sonra d/c (t/ç olmalı)"
    if son not in SERT and ek[0] in "tç" and len(ek) > 1 and ek[1] in UNLU:
        return "yumuşak sesten sonra t/ç (d/c olmalı)"
    govde = re.sub(r"(?:y?ken|ki)$", "", ek) or ek
    onceki = _son_unlu(ok)
    for c in govde:
        if c in UNLU:
            b = _beklenen_unlu(onceki, c)
            if c != b:
                return f"ünlü uyumu: '{c}' yerine '{b}' (okunuş {okunus!r})"
            onceki = c
    return None


def sertlesme_hatalari(metin, bg=None):
    """Sert ünsüzden sonra d/c (koşdu, ağaçdan). Adlar atlanır: cümle ortasında büyük harfle başlayanlar ve cümle
    başında sözlükte ad olarak geçenler (Cikcik)."""
    out = []
    for m in re.finditer(rf"(?<![{H}])[{H}]+", metin):
        w = kucuk(m.group(0))
        if m.group(0)[0].isupper() and (not _cumle_basi(metin, m.start()) or (bg and w in bg.sozluk.adlar)):
            continue
        if SERTLESME.search(w) and not w.startswith(SERTLESME_IZIN):
            out.append(m.group(0))
    return out


def zaman_sinifi(w, bg):
    """Kelimenin (tırnak dışı yüklem adayı) zaman sınıfı: 'gecmis', 'yor', 'mis', 'acak', 'genis', 'dir',
    'gereklilik', 'ad_simdi' ya da None (yüklem değil / bilinmiyor)."""
    if "'" in w:                       # ad + ek: yüklem ekin kendisidir (Tosbi'ydi, Tosbi'dir)
        ek = kucuk(w.split("'", 1)[1])
        return "gecmis" if GECMIS.search(ek) else "dir" if DIR.search(ek) else "mis" if MIS.search(ek) else None
    w = kucuk(w)
    if w in SIMDI_AD:
        return "ad_simdi"
    if GECMIS.search(w):
        return "gecmis"
    if YOR.search(w) and re.search(rf"[{UNLU}]yor", w):
        return "yor"
    k = bg.kok(w)
    fiil = k.endswith("-")
    if MIS.search(w) and fiil:
        return "mis"
    if ACAK.search(w) and (fiil or w not in ACAK_AD):     # 'gelecek' kökçüde ad; yüklem yerinde gelecek zaman
        return "acak"
    if GEREKLILIK.search(w) and fiil:
        return "gereklilik"
    if fiil and (GENIS.search(w) and not w.endswith(("lar", "ler"))
                 or re.search(r"(?:[aeıiuü]r|m[ae]z)l[ae]r$", w)):
        return "genis"
    if DIR.search(w) and not (fiil and w == k.rstrip("-")):
        govde = re.sub(r"[dt][ıiuü]r(?:l[ae]r)?$", "", w)
        if bg.sozluk.tf.get(govde, 0) >= 20 or bg.kok(govde) != govde:     # çıtır, bayır: -dır değil
            return "dir"
    return None


# askıda ek: ara yüklem, cümle sonu yüklemiyle aynı görünüşü taşıyıp -dı'yı ona bırakır (yüzüyor, eğleniyorlardı)
ASKI = {"yor": re.compile(r"yor(?:l[ae]r)?d[uıiü]"), "acak": re.compile(r"[ae]c[ae](?:kt|kl[ae]rd)[ıi]"),
        "mis": re.compile(r"m[ıiuü]ş(?:t|l[ae]rd)[ıiuü]"),
        "genis": re.compile(r"(?:[aeıiuü]r|m[ae]z)(?:l[ae]r)?d[ıiuü]")}


def zaman_ihlalleri(govde, bg):
    """K5 zaman kuralı: [(kelime, sınıf, cümle)]. Tırnak dışındaki her cümlenin son yüklemi (konuşma devriği
    '… dedi Tosbi' ise konuşma fiili) ve ara yan cümle sonundaki -yor/-acak yüklemleri; ara yüklem, cümle sonu
    aynı görünüşün -dı'lısıyla bitiyorsa (koşuyor, zıplıyor ve gülüyordu) askıda ek sayılır."""
    sonuc = []
    disari = _tirnak_disi(govde)
    for cumle in re.split(r"[.!?…]+", disari):
        ks = [w for w, _, _ in _kelime_konum(cumle)]
        if not [w for w in ks if w != "¶"]:
            continue
        # son yüklem: son kelime; son kelime yüklem değilse yalnız konuşma devriği ('… dedi Tosbi', '… diyor
        # annesi') için geriye en çok 3 kelime bakılır (yapılmış, parlak bir kaydırak: sıfat-fiil yüklem değil)
        son_sinif, son_kelime = None, None
        sozcuk = [w for w in ks if w != "¶"]
        s = zaman_sinifi(sozcuk[-1], bg)
        if s is not None:
            son_sinif, son_kelime = s, sozcuk[-1]
        else:
            for w in reversed(sozcuk[-4:-1]):
                if bg.kok(kucuk(w)) in KONUSMA_KOK and zaman_sinifi(w, bg):
                    son_sinif, son_kelime = zaman_sinifi(w, bg), w
                    break
        # '… biliyordu ki … vardır': son yüklem 'ki' ile bağlanan içerik cümlesinin; ana yüklem -dı'lıysa geçer
        ki = [j for j, w in enumerate(ks) if kucuk(w) == "ki" and j > 0]
        ana_gecmis = bool(ki) and zaman_sinifi(ks[ki[0] - 1], bg) == "gecmis"
        if son_sinif not in (None, "gecmis") and not ana_gecmis:
            sonuc.append((son_kelime, son_sinif, cumle.strip()))
        # ara yan cümleler: virgül, noktalı virgül, iki nokta, tırnak ya da bağlaçtan önceki -yor/-acak
        for m in re.finditer(rf"([{H}]+)(?=\s*(?:[,;:¶]|\s(?:{'|'.join(BAGLAC)})\b))", cumle):
            w = m.group(1)
            if w == son_kelime and m.end() >= len(cumle.rstrip()) - 1:
                continue
            s = zaman_sinifi(w, bg)
            if s not in ("yor", "acak"):
                continue
            sonra = cumle[m.end():].lstrip(" ,;:¶").split()
            if sonra[:1] == ["diye"] or (sonra[:1] and sonra[0] in ("mu", "mı", "mi", "mü") and sonra[1:2] == ["diye"]):
                continue
            if son_sinif == "gecmis" and son_kelime and ASKI[s].search(kucuk(son_kelime)):
                continue
            sonuc.append((w, s, cumle.strip()))
    return sonuc


def k5(kayit, bg, ih, nt, atlanan, bilinmeyen):
    g = kayit["govde"]
    d = bg.dunya(kayit["figur"]) if kayit["figur"] in bg.kartlar else None
    # (a) Zemberek çözümlemesi
    if bg.zemberek is None:
        atlanan.append({"kod": "K5.cozumleme", "neden": bg.zemberek_neden})
        atlanan.append({"kod": "K6.zemberek_belirsiz", "neden": bg.zemberek_neden})
    else:
        izin = haric_listesi(kayit, bg)
        izin_k = {kucuk(w) for i in izin for w in i.split()}
        for w in dict.fromkeys(sade_sozluk.kelimeler(f"{kayit['sorun']} {kayit['cozum']} {g}")):
            if w in izin_k or w in bg.beyaz:
                continue
            analiz = list(bg.zemberek.analyze(w))
            if not analiz:
                bilinmeyen.append(w)
                _ihlal(ih, "K5.cozumleme", f"Zemberek çözümleyemedi: {w}")
            elif len({str(a.item.lemma) for a in analiz}) > 2:
                _not(nt, "K6.zemberek_belirsiz", "D", f"birden çok çözümleme: {w}")
    # (b) kesme eki
    okunuslar = dict(d.okunuslar) if d else {}
    for m in re.finditer(rf"(?<![{H}])([{BUYUK}][{H}]*(?:[- ][{BUYUK}][{H}]*)*)'([{HARF}]+)", g):
        ad = m.group(1)
        son_ad = re.split(r"[ ]", ad)[-1]
        ok = okunuslar.get(ad) or okunuslar.get(son_ad) or kucuk(son_ad)
        h = kesme_eki_hatasi(ok, m.group(2))
        if h:
            _ihlal(ih, "K5.kesme_eki", f"{m.group(0)}: {h}")
    # (c) sertleşme
    for m in sertlesme_hatalari(f"{kayit['sorun']} {kayit['cozum']} {g}", bg):
        _ihlal(ih, "K5.sertlesme", f"sertleşme: {m}")
    # (d) zaman kuralı
    for w, s, c in zaman_ihlalleri(g, bg):
        _ihlal(ih, "K5.zaman", f"tırnak dışı yüklem -dı'lı değil ({s}): {w!r} — {c[:60]!r}")


# ---------------------------------------------------------------- K6 (not)

def k6(kayit, bg, nt):
    g = kayit["govde"]
    for m in re.finditer(rf"([{BUYUK}][{H}]+)'([dt][ae])\s+([{HARF}]+)", g):
        if bg.kok(m.group(3)).endswith("-"):
            _not(nt, "K6.bitisik_de", "D", f"bitişik de/da olabilir: {m.group(0)!r}")
    for m in re.finditer(rf"\b(ben|sen|biz|siz|onlar)(de|da)\s+([{HARF}]+)", kucuk(g)):
        if bg.kok(m.group(3)).endswith("-"):
            _not(nt, "K6.bitisik_de", "D", f"bitişik de/da olabilir: {m.group(0)!r}")
    for w in sade_sozluk.kelimeler(g):
        if w.endswith("ki") and len(w) > 4 and bg.sozluk.tf.get(w, 0) < 5 and bg.kok(w[:-2]).endswith("-"):
            _not(nt, "K6.bitisik_ki", "D", f"bitişik 'ki' olabilir: {w}")
    kg = kucuk(g)
    ikileme = [m.group(1) for m in re.finditer(r"(?<![a-zçğıöşü])([a-zçğıöşü]+) \1(?![a-zçğıöşü])", kg)
               if m.group(1) not in sec.IKILEME]
    if ikileme:
        _not(nt, "K6.ikileme", "D", f"ikileme ya da kekeme tekrar: {ikileme[:3]}")
    if KONUSAN_NESNE.search(g):
        _not(nt, "K6.konusan_nesne", "K,M", "konuşan nesne olabilir")
    yer = kayit["yer"]
    anahtar = {"şato": "sato", "dağ": "dag"}.get(yer, yer)
    if anahtar in sec.YER_KELIME and sec.yer_cezasi(g, anahtar):
        _not(nt, "K6.yer", "M", f"hikâye {yer} dışında bitiyor olabilir (M8)")
    for desen, izin, ad in sec.OZELLIK:
        if re.search(desen, kg) and not re.search(izin, kg):
            _not(nt, "K6.ozellik_karismasi", "K", ad)
    cs = uk.cumleler(g)
    for i in range(max(3, len(cs) - 3), len(cs)):
        s = kucuk(cs[i])
        if sec.DERS.search(s):
            govde = kucuk(" ".join(cs[:i]))
            yok = [v for v, kanit in sec.DERS_KANIT.items() if v in s and not re.search(kanit, govde)]
            if yok:
                _not(nt, "K6.ders", "M", f"ders olaydan kopuk olabilir ({yok[0]})")
                break


# ---------------------------------------------------------------- K7

def guvenlik_eslesmeleri(metin, d=None):
    """[(tür, kalıp, eşleşme)]: sec.GUVENLIK + K7 ek kalıpları + hastalık kökleri (küçük harfli metinde).
    Kartın 'k7_izinli' ifadelerinin (figüre özel beyaz liste) içinde kalan eşleşmeler sayılmaz."""
    low = kucuk(metin)
    bul = [("guvenlik", "sec.GUVENLIK", m) for m in sec.GUVENLIK.finditer(low)]
    bul += [("guvenlik", ad, m) for desen, ad in K7_GUVENLIK for m in desen.finditer(low)]
    bul += [("saglik", ad, m) for desen, ad in K7_SAGLIK for m in desen.finditer(low)]
    izin = [m.span() for iz in (d.k7_izinli if d is not None else []) for m in iz.finditer(low)]
    return [(t, ad, m.group(0)) for t, ad, m in bul
            if not any(a <= m.start() and m.end() <= b for a, b in izin)]


def k7(kayit, bg, ih):
    d = bg.dunya(kayit["figur"]) if kayit["figur"] in bg.kartlar else None
    for alan in (kayit["sorun"], kayit["cozum"], kayit["govde"]):
        for tur, ad, es in guvenlik_eslesmeleri(alan, d):
            _ihlal(ih, f"K7.{tur}", f"{ad}: {es!r}")


# ---------------------------------------------------------------- K8

def konusmacilar(govde, adlar):
    """Cümle başına konuşan: [(cümle no, konuşan|None, tırnak içi metin)] (tırnak içeren cümleler için).
    adlar: {yüzey biçimi (küçük harf): kimlik}."""
    out = []
    for i, c in enumerate(uk.cumleler(govde), 1):
        tirnak = re.findall(r'"([^"]*)"', c)
        if not tirnak:
            continue
        disari = _tirnak_disi(c)
        ks = [w for w, _, _ in _kelime_konum(disari)]
        kim = None
        fiil_i = next((j for j, w in enumerate(ks) if kucuk(w) in KONUSMA), None)
        if fiil_i is not None:
            for w in ks[fiil_i + 1:] + list(reversed(ks[:fiil_i])):
                a = adlar.get(kucuk(w.split("'")[0]))
                if a and "'" not in w:
                    kim = a
                    break
        elif ks and ks[0] != "¶":
            kim = adlar.get(kucuk(ks[0].split("'")[0])) if "'" not in ks[0] else None
        out.append((i, kim, " ".join(tirnak)))
    return out


def k8(kayit, bg, ih):
    g = kayit["govde"]
    cs = uk.cumleler(g)
    norm = [re.sub(rf"[^{H} ]", "", kucuk(c)).strip() for c in cs]
    tekrar = [c for c, n in collections.Counter(norm).items() if n > 1 and c]
    if tekrar:
        _ihlal(ih, "K8.ayni_cumle", f"aynı cümle iki kez: {tekrar[0][:50]!r}")
    kel = re.findall(r"[a-zçğıöşüâîû]+", kucuk(g))
    uclu = [tuple(kel[i:i + 3]) for i in range(len(kel) - 2)]
    n_tekrar = len(uclu) - len(set(uclu))
    if n_tekrar > ESIK["uclu_tekrar"]:
        en = collections.Counter(uclu).most_common(1)[0][0]
        _ihlal(ih, "K8.uclu", f"3-gram tekrarı {n_tekrar} (<= 2), en sık: {' '.join(en)!r}")
    kg = kucuk(g)
    m = re.search(r"(?<![a-zçğıöşü])([a-zçğıöşü]+) ve \1(?![a-zçğıöşü])", kg)
    if m:
        _ihlal(ih, "K8.x_ve_x", f"'X ve X': {m.group(0)!r}")
    uc = [m.group(1) for m in re.finditer(r"(?<![a-zçğıöşü])([a-zçğıöşü]+) \1 \1(?![a-zçğıöşü])", kg)]
    obek = [m.group(1) for m in re.finditer(r"(?<![a-zçğıöşü])([a-zçğıöşü]+(?: [a-zçğıöşü]+){1,3})(?:,| ve)? \1"
                                            r"(?![a-zçğıöşü])", kg) if m.group(1).split()[0] not in sec.IKILEME]
    if uc or obek:
        _ihlal(ih, "K8.kekeme", f"kekeme tekrar: {(uc + obek)[:2]}")
    if kayit["figur"] not in bg.kartlar:
        return
    d = bg.dunya(kayit["figur"])
    adli = [d.ad] + [y for y in kayit["yan"] if y in d.yanlar and y[:1].isupper()]
    for n in adli:
        e = re.escape(n)
        if re.search(rf"(?<![{H}]){e},?\s+{e}'", g):
            _ihlal(ih, "K8.kendine_gonderme", f"kendine gönderme: '{n}, {n}'…'")
        if len(re.findall(rf"(?<![{H}]){e} adında", g)) > 1:
            _ihlal(ih, "K8.tanitim", f"{n} iki kez tanıtılıyor")
        if re.search(rf"(?:[Bb]en de|[Bb]enim adım|[Aa]dım) {e}\b[^\"]*\"\s*(?:diye \w+|dedi|sordu)"
                     rf"\s+(?!{e}\b)[a-zçğıöşü]", g):
            _ihlal(ih, "K8.tanitim", f"başkası kendini {n} diye tanıtıyor")
        for s in cs:
            m = re.search(rf"^(?:[{BUYUK}]\w*\s+){{0,2}}{e}(?!['’])(?![{H}])(.*?)(?<![{H}]){e}{sec.EK_ISIM}", s)
            if m and not re.search(rf"[\"“”:]|(?<![{H}])[{BUYUK}]", m.group(1)) \
                    and not any(re.search(rf"\b{h}", kucuk(m.group(1))) for h in sec.HAYVAN):
                _ihlal(ih, "K8.kendine_gonderme", f"{n} aynı cümlede hem özne hem nesne: {s[:50]!r}")
                break
    # konuşan ve kendine seslenme
    adlar = {}
    for b in [d.ad] + [x for y in kayit["yan"] if y in d.yanlar for x in d.yan_bicimleri(d.yanlar[y])]:
        kim = d.ad if b == d.ad else next(y for y in kayit["yan"]
                                          if y in d.yanlar and b in d.yan_bicimleri(d.yanlar[y]))
        adlar[kucuk(b.split()[-1])] = kim
        adlar[kucuk(b)] = kim
    kons = konusmacilar(g, adlar)
    for i, kim, soz in kons:
        if kim and kim[:1].isupper() and re.search(rf"(?<![{H}]){re.escape(kim)}(?![{H}])", soz):
            _ihlal(ih, "K8.kendine_seslenme", f"{kim} kendine adıyla sesleniyor (cümle {i})")
    for (i1, k1_, _), (i2, k2_, _) in zip(kons, kons[1:]):
        if i2 == i1 + 1 and k1_ and k1_ == k2_:
            _ihlal(ih, "K8.ust_uste", f"{k1_} art arda iki cümlede konuşuyor ({i1}, {i2})")


# ---------------------------------------------------------------- K9

def _lcs(a, b):
    onceki = [0] * (len(b) + 1)
    for x in a:
        simdi = [0]
        for j, y in enumerate(b):
            simdi.append(onceki[j] + 1 if x == y else max(onceki[j + 1], simdi[j]))
        onceki = simdi
    return onceki[-1]


def yakin_kopya(govde, havuz):
    """[(kod, açıklama)]: havuz = [(kimlik, gövde)]."""
    a = re.findall(rf"[{HARF}]+", kucuk(govde))
    a3 = {tuple(a[i:i + 3]) for i in range(len(a) - 2)}
    ca = collections.Counter(a)
    out = []
    for kim, h in havuz:
        b = re.findall(rf"[{HARF}]+", kucuk(h))
        if a == b:
            out.append(("K9.kopya", f"birebir kopya: {kim}"))
            continue
        b3 = {tuple(b[i:i + 3]) for i in range(len(b) - 2)}
        j = len(a3 & b3) / max(1, len(a3 | b3))
        if j >= ESIK["jaccard"]:
            out.append(("K9.jaccard", f"3-gram Jaccard {j:.2f} >= 0,5: {kim}"))
            continue
        ortak = sum((ca & collections.Counter(b)).values())
        if 2 * ortak / max(1, len(a) + len(b)) < ESIK["rouge_l"]:
            continue
        lcs = _lcs(a, b)
        f = 2 * lcs / max(1, len(a) + len(b))
        if f >= ESIK["rouge_l"]:
            out.append(("K9.rouge", f"ROUGE-L {f:.2f} >= 0,7: {kim}"))
    return out


# ---------------------------------------------------------------- K10, K11, K12

def k10_kayip(kayit, model=None):
    """K10 (RAPOR, kapı değil): c3 ön eğitim modeliyle gövdede token başına kayıp, ad token'ları hariç. Bu
    sürümde hesaplanmaz (CPU'da nice -n 19 ile ayrı koşulacak); None döner."""
    return None


def k11(kayit, blok, bg, ih, taslak_kart):
    beklenen = blok.get("beklenen_sha1")
    s = uk.sha1(kayit)
    if beklenen and beklenen != s:
        _ihlal(ih, "K11.sha1", f"kanonik kaydın sha1'i {s[:10]}, beklenen {beklenen[:10]}")
    kart = bg.kartlar.get(kayit["figur"])
    if kart is not None and not kart.get("onayli") and not taslak_kart:
        _ihlal(ih, "K11.kart_onay", f"{kayit['figur']} kartı onaylı değil (onayli: false)")
    for h in bg.sozluk_hatalari:
        _ihlal(ih, "K11.sozluk", h)
    eksik = [y for y, v in bg.surum["veri"].items() if v is None and not y.endswith(
        (os.path.basename(IZINLI_KELIME), os.path.basename(ZEMBEREK_BEYAZ)))]
    if eksik or bg.surum["tokenizer"]["k2"] is None:
        _ihlal(ih, "K11.bilesen", f"bileşen dosyası yok: {eksik or [K2_TOKENIZER]}")


class KotaSayaci:
    """K12 (Aşama 1'de): figür başına yürüyen sayaçlar; kotayı aşan kusursuz hikâye yedek havuza gider.
    Arayüz: ekle(kayit, tohum) -> [(kod, açıklama)] (aşılan kotalar), durum() -> {figür: {oran...}}."""
    ESIKLER = {"son_cumle_cunku": 0.15, "son_cumle_duygu": 0.50, "adinda_acilis": 0.15, "acilis_4gram": 0.20,
               "o_gunden_sonra": 0.05, "plan_sorunu": 0.10, "tohum_payi_sapma": 0.05}

    def ekle(self, kayit, tohum=None):
        raise NotImplementedError("K12 kotaları Aşama 1'de eklenecek (KUSURSUZ_VERI.md Adım 10)")

    def durum(self):
        raise NotImplementedError("K12 kotaları Aşama 1'de eklenecek (KUSURSUZ_VERI.md Adım 10)")


# ---------------------------------------------------------------- ana giriş

def denetle(girdi, tohum, bg, havuz=(), taslak_kart=False):
    """girdi: urun_kayit.ayristir bloğu ya da kanonik kayıt (dict, ALANLAR). tohum: tohum kaydı ya da None.
    havuz: K9 için [(kimlik, gövde)]. Dönüş: kimlik, sha1, gecti, ihlaller, notlar, atlanan, rapor, surum."""
    if "govde" in girdi and "bicim_hatalari" in girdi:
        blok = girdi
        kayit = uk.kayit(blok)
    else:
        kayit = uk.kanonik(*(girdi[a] for a in uk.ALANLAR))
        blok = {"tohum": (tohum or {}).get("id"), "degisim": girdi.get("degisim"), "bicim_hatalari": [],
                "beklenen_sha1": girdi.get("beklenen_sha1")}
    ih, nt, atlanan, bilinmeyen = [], [], [], []
    rapor = {}
    k1(blok, kayit, tohum, bg, ih)
    k2(kayit, bg, ih, rapor)
    k3(kayit, bg, ih, rapor)
    k4(blok, kayit, tohum, bg, ih, nt)
    k5(kayit, bg, ih, nt, atlanan, bilinmeyen)
    k6(kayit, bg, nt)
    k7(kayit, bg, ih)
    k8(kayit, bg, ih)
    for kod, ac in yakin_kopya(kayit["govde"], havuz):
        _ihlal(ih, kod, ac)
    if not havuz:
        atlanan.append({"kod": "K9", "neden": "havuz boş (Aşama 1'de kabul havuzu)"})
    k11(kayit, blok, bg, ih, taslak_kart)
    rapor["K10_kayip"] = k10_kayip(kayit)
    return {"kimlik": uk.kimlik(kayit), "sha1": uk.sha1(kayit), "tohum": blok.get("tohum"),
            "gecti": not ih, "ihlaller": ih, "notlar": nt, "atlanan": atlanan, "bilinmeyen_kelimeler": bilinmeyen,
            "rapor": rapor, "taslak_kart": bool(taslak_kart), "surum": bg.surum_ozeti, "serilestirme": uk.SURUM}


def tohum_oku(yol):
    t = {}
    with open(yol, encoding="utf-8") as f:
        for s in f:
            if s.strip():
                k = json.loads(s)
                t[k["id"]] = k
    return t


# ---------------------------------------------------------------- yanlış alarm ölçümü (Adım 0 birim testi 2)

def yanlis_alarm(n=200, tohum=2026, ayrinti=None):
    """tr-tinystories'ten n rastgele hikâyede (tohumlu rezervuar örneklemi) K5 zaman kuralı, K5 sertleşme, K7
    ve K1 zaman atlaması eşleşmeleri. Ayrıntı dosyası elle etiketlemek içindir (her satır: kural, kelime, bağlam)."""
    rng = random.Random(tohum)
    orn = []
    for i, h in enumerate(sade_sozluk.hikayeler()):
        if len(orn) < n:
            orn.append((i, h))
        else:
            j = rng.randrange(i + 1)
            if j < n:
                orn[j] = (i, h)
    orn.sort()
    bg = Baglam(zemberek=False)
    say = collections.Counter()
    hikaye = collections.Counter()
    satirlar = []
    for i, h in orn:
        g = uk.normallestir(h).replace("\n", " ")
        g = re.sub(" {2,}", " ", g)
        kural = {
            "K5.zaman": [(w, s, c) for w, s, c in zaman_ihlalleri(g, bg)],
            "K5.sertlesme": [(w, "", "") for w in sertlesme_hatalari(g, bg)],
            "K7": [(es, tur + ":" + ad, "") for tur, ad, es in guvenlik_eslesmeleri(g)],
            "K1.zaman": [(m.group(0), ad, "") for desen, ad in ZAMAN_ATLAMA for m in desen.finditer(kucuk(g))],
        }
        for k, v in kural.items():
            say[k] += len(v)
            hikaye[k] += bool(v)
            for w, s, c in v:
                baglam = c or _baglam(g, w)
                satirlar.append(f"{k}\t{i}\t{w}\t{s}\t{baglam}")
    ozet = {"n_hikaye": len(orn), "tohum": tohum, "eslesme": dict(say), "hikaye": dict(hikaye),
            "hikaye_orani": {k: round(v / len(orn), 3) for k, v in hikaye.items()}}
    if ayrinti:
        with open(ayrinti, "w", encoding="utf-8") as f:
            f.write("kural\thikaye\tkelime\tsinif\tbaglam\n" + "\n".join(satirlar) + "\n")
    return ozet


def _baglam(metin, w, pay=50):
    i = kucuk(metin).find(kucuk(w))
    return metin[max(0, i - pay):i + len(w) + pay].replace("\t", " ") if i >= 0 else ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    alt = ap.add_subparsers(dest="komut", required=True)
    d = alt.add_parser("denetle")
    d.add_argument("dosya")
    d.add_argument("--tohum", required=True, help="tohum JSONL (her satır bir tohum kaydı)")
    d.add_argument("--havuz", default=None, help="K9 havuzu: JSONL (kimlik, govde)")
    d.add_argument("--taslak-kart", action="store_true", help="onaysız kartla dene (sonuçta taslak_kart: true)")
    d.add_argument("--json", action="store_true")
    s = alt.add_parser("surum")
    s.add_argument("--json", action="store_true")
    y = alt.add_parser("yanlis-alarm")
    y.add_argument("--n", type=int, default=200)
    y.add_argument("--tohum", type=int, default=2026)
    y.add_argument("--ayrinti", default=None)
    a = ap.parse_args()
    if a.komut == "surum":
        bg = Baglam()
        print(json.dumps({"ozet": bg.surum_ozeti, **bg.surum}, ensure_ascii=False, indent=None if a.json else 1))
        return 0
    if a.komut == "yanlis-alarm":
        print(json.dumps(yanlis_alarm(a.n, a.tohum, a.ayrinti), ensure_ascii=False, indent=1))
        return 0
    bg = Baglam()
    tohumlar = tohum_oku(a.tohum)
    havuz = []
    if a.havuz:
        with open(a.havuz, encoding="utf-8") as f:
            havuz = [(r["kimlik"], r["govde"]) for r in map(json.loads, filter(str.strip, f))]
    with open(a.dosya, encoding="utf-8") as f:
        bloklar = uk.ayristir(f.read())
    gecen, atlanan = 0, set()
    for b in bloklar:
        r = denetle(b, tohumlar.get(b["tohum"]), bg, havuz, a.taslak_kart)
        gecen += r["gecti"]
        atlanan |= {x["kod"] for x in r["atlanan"]}
        if a.json:
            print(json.dumps(r, ensure_ascii=False))
        else:
            print(f"{r['kimlik']}  {'GEÇTİ' if r['gecti'] else 'RET'}  (satır {b['satir']}, tohum {b['tohum']})")
            for x in r["ihlaller"]:
                print(f"   {x['kod']}: {x['aciklama']}")
            for x in r["notlar"]:
                print(f"   not {x['kod']} [{x['mercek']}]: {x['aciklama']}")
    if not a.json:
        print(f"{gecen}/{len(bloklar)} geçti; atlanan: {', '.join(sorted(atlanan)) or '-'}; sürüm {bg.surum_ozeti}")
    return 0 if gecen == len(bloklar) else 1


if __name__ == "__main__":
    sys.exit(main())
