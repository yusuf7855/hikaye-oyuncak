"""Ürün hikâyesinin kanonik kaydı, normalizasyonu, sha1 kimliği ve TEK serileştirme fonksiyonu.

KUSURSUZ_VERI.md Adım 0e ve 2 ("Kayıt ve başlık biçimini sabitleme"). kapi.py, bozucu.py, veri_hakem.py ve
prepare_ft2 (--yalniz) eğitim dizgisini YALNIZ buradaki dizgi() ile üretir; hakemlenen alanlar = eğitilen alanlar.

Kanonik kayıt (kanonik()): {"figur", "yer", "yan": [kısa ad, ...], "sorun", "cozum", "govde"}
  figur : ürün figürünün adı, kartta yazdığı gibi ("Tosbi", "Örümcek Adam")
  yer   : kartın yer etiketi ("orman", "dağ", "şato")
  yan   : tohumdaki yanların karttaki kısa adları, tohumdaki sırayla ("Murat", "dedesi", "baykuş"); yansız: []
  sorun, cozum : plan satırının iki yarısı; govde : hikâye (tek paragraf)
  Tema, tohum kimliği ve '@degisim' eğitime girmez, kanonik kayda da girmez.
Normalizasyon (normallestir(); hakemden önceki tek deterministik değişiklik, hakem alıntısına da uygulanır):
  Unicode NFC; “ ” „ -> "; ’ ‘ -> '; satır sonu \\n; bölünmez boşluk ve sekme -> boşluk; art arda boşluk teke iner;
  şapka yalnız DONUSEN_KOKLER listesindeki köklerle başlayan kelimelerde düzleşir (rüzgâr -> rüzgar,
  kâğıdı -> kağıdı). Listede olmayan şapka (eşsesli üreten 'hâlâ' dahil) olduğu gibi kalır; K3 reddeder.
Kimlik: 'urun/<figür kimliği>#' + sha1[:10]; sha1 = kanonik JSON'un (sort_keys, ayraç ',' ':', ensure_ascii=False,
  UTF-8) sha1'i. Figür kimliği kart kimliğiyle aynı ASCII biçimdir (Örümcek Adam -> orumcek_adam, Maşa -> masa).
Eğitim dizgisi (dizgi()), research/tinystories/prepare_ft2.py baslik() ile aynı iskelet:
  'Karakter: Tosbi | Yer: orman | Yan: baykuş\\nSorun: <sorun>\\nÇözüm: <çözüm>\\n\\n<gövde>'
  plan=False -> Sorun/Çözüm satırları yok; yan_alani=False ya da yan [] -> ' | Yan: …' yok. Dört biçim aynı kaydın
  deterministik alt kümeleridir. Hangi kopyanın planlı olacağını planli_mi() (sha1 + kopya no + tohum) belirler.
Yazar dosyası (KILAVUZ Kural 10; ayristir() / blok_yaz()):
  ### <Figür> | <yer> | <yan, yan>      (yansızsa üçüncü alan '-')
  @plan: <sorun> | <çözüm>
  @tohum: <tohum kimliği>
  @degisim: <eski kelime> -> <yeni kelime>   (isteğe bağlı; tohum kelimesi değişikliği, en çok 1)
  @onarim: <ebeveyn sha1>                    (yalnız onarım adayında: reddedilen ebeveynin sha1'i; kayda girmez)
  <gövde: tek satır, tek paragraf>
  Hikâyeler arasında boş satır. Başka '@' satırı ya da sıra dışı satır biçim hatasıdır (K1).
Cümle (cumleler()): K2'nin ve hakem 'cumle_no'sunun ortak bölmesi. Cümle . ! ? … (ve ardından gelebilen kapanış
  tırnağı) ile biter, ancak ardından boşluk ve büyük harf, rakam ya da açılış tırnağı gelirse ('"Gel!" dedi Tosbi.'
  tek cümledir). Gövde cümleleri 1'den numaralanır, plan satırı 0'dır.

Kullanım: .venv/bin/python degerlendirme/urun_kayit.py <yazar dosyası> [--dizgi] [--plan 0|1] [--yan 0|1] [--json]
"""
import argparse
import hashlib
import json
import re
import sys
import unicodedata

SURUM = "urun_kayit/1"          # serileştirme ve normalizasyon sürümü; kabul kaydına girer (K11)
ALANLAR = ("figur", "yer", "yan", "sorun", "cozum", "govde")

BUYUK = "A-ZÇĞİÖŞÜÂÎÛ"
KUCUK = "a-zçğıöşüâîû"
HARFLER = re.compile(rf"[{BUYUK}{KUCUK}]+")

# Şapkası düzleşen kökler (kelime bu köklerden biriyle başlıyorsa): eşsesli üretmeyenler. Yeni kök eklemek
# normalizasyonu, dolayısıyla sha1'leri değiştirir: SURUM artırılır ve K1/K4/sha1 bütün veriye yeniden koşulur.
DONUSEN_KOKLER = ("rüzgâr", "kâğıt", "kâğıd", "dükkân", "hikâye", "kâse", "tezgâh", "zekâ", "lâzım", "mekân",
                  "dâhil", "kâmil", "ilâç", "duâ", "yadigâr")
# Düzleşmeyenler (bilgi için; kod beyaz listeyle çalışır, bunlar listede olmadığı için zaten kalır): düzleşince
# başka bir kelime olurlar. 'hala' babanın kız kardeşidir; tr-tinystories'te 'hala' 10 749, 'hâlâ' 191 kez.
ESSESLI = ("hâlâ", "kâr", "âdet", "âlem", "âmâ", "hâl", "şûra", "yâr", "dâhi", "âşık", "hâkim", "askerî", "resmî")
_SAPKA = str.maketrans("âîûÂÎÛ", "aiuAİU")
_TIRNAK = str.maketrans({"“": '"', "”": '"', "„": '"', "’": "'", "‘": "'", " ": " ", "\t": " "})
ASCII = str.maketrans("çğıöşüâîûÇĞİÖŞÜÂÎÛ", "cgiosuaiuCGIOSUAIU")

HEADER = re.compile(r"^###[ \t]+(.*)$")
META = re.compile(r"^@([a-zçğıöşü_]+):[ \t]*(.*)$")
DEGISIM = re.compile(r"^(\S+)\s*->\s*(\S+)$")
ONARIM = re.compile(r"^[0-9a-f]{40}$")


def kucuk(s):
    """Türkçe küçük harf (sec.kucuk ile aynı): I -> ı, İ -> i."""
    return s.replace("I", "ı").replace("İ", "i").lower()


# ---------------------------------------------------------------- normalizasyon

def _sapka_duzle(m):
    w = m.group(0)
    if re.search("[âîûÂÎÛ]", w) and kucuk(w).startswith(DONUSEN_KOKLER):
        return w.translate(_SAPKA)
    return w


def normallestir(metin):
    """Hakemden önceki tek deterministik değişiklik (hakem alıntısına da aynısı uygulanır)."""
    if metin is None:
        return None
    s = unicodedata.normalize("NFC", metin).replace("\r\n", "\n").replace("\r", "\n").translate(_TIRNAK)
    s = HARFLER.sub(_sapka_duzle, s)
    s = "\n".join(re.sub(r" {2,}", " ", satir).strip() for satir in s.split("\n"))
    return s.strip()


def _yan_listesi(yan):
    if yan is None:
        return []
    if isinstance(yan, str):
        yan = [] if yan.strip() in ("", "-") else yan.split(",")
    return [normallestir(y) for y in yan if normallestir(y)]


def kanonik(figur, yer, yan, sorun, cozum, govde):
    """Normalleştirilmiş kanonik kayıt. yan: liste ya da 'a, b' / '-' dizgisi."""
    return {"figur": normallestir(figur or ""), "yer": normallestir(yer or ""), "yan": _yan_listesi(yan),
            "sorun": normallestir(sorun or ""), "cozum": normallestir(cozum or ""),
            "govde": normallestir(govde or "")}


def kanonik_json(kayit):
    eksik = [a for a in ALANLAR if a not in kayit]
    if eksik or set(kayit) - set(ALANLAR):
        fazla = sorted(set(kayit) - set(ALANLAR))
        raise ValueError(f"kanonik kayıt alanları {ALANLAR} olmalı; eksik {eksik}, fazla {fazla}")
    return json.dumps({a: kayit[a] for a in ALANLAR}, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha1(kayit):
    return hashlib.sha1(kanonik_json(kayit).encode("utf-8")).hexdigest()


def figur_kimligi(figur):
    """Kart kimliğiyle aynı ASCII biçim: 'Örümcek Adam' -> 'orumcek_adam', 'Maşa' -> 'masa'."""
    return re.sub(r"[^a-z0-9]+", "_", kucuk(normallestir(figur)).translate(ASCII)).strip("_")


def kimlik(kayit, ad_alani="urun"):
    """'urun/<figür>#<sha1[:10]>'. Kanaryalar ayrı ad alanında tutulur ama hakeme aynı biçimle gider."""
    return f"{ad_alani}/{figur_kimligi(kayit['figur'])}#{sha1(kayit)[:10]}"


# ---------------------------------------------------------------- TEK serileştirme

def dizgi(kayit, plan=True, yan_alani=True):
    """Eğitim dizgisi (EOT'suz). prepare_ft2.baslik() iskeleti: başlık [+ plan] + '\\n\\n' + gövde."""
    bas = f"Karakter: {kayit['figur']} | Yer: {kayit['yer']}"
    if yan_alani and kayit["yan"]:
        bas += f" | Yan: {', '.join(kayit['yan'])}"
    if plan:
        bas += f"\nSorun: {kayit['sorun']}\nÇözüm: {kayit['cozum']}"
    return f"{bas}\n\n{kayit['govde']}"


def dizgiler(kayit):
    """Aynı kaydın dört biçimi: {(plan, yan_alani): dizgi}."""
    return {(p, y): dizgi(kayit, p, y) for p in (True, False) for y in (True, False)}


def planli_mi(kayit_sha1, kopya, oran=0.7, tohum=0):
    """Bu kopya plan satırlarıyla mı yazılır: sha1, kopya numarası ve tohumdan deterministik (sıra bağımsız)."""
    h = hashlib.sha256(f"{tohum}:{kayit_sha1}:{kopya}".encode()).hexdigest()
    return int(h[:13], 16) / 16 ** 13 < oran


# ---------------------------------------------------------------- cümle

_CUMLE_SONU = re.compile(rf'[.!?…]+"?(?=\s+"?[{BUYUK}0-9])')


def cumleler(metin):
    """Cümle listesi (K2 ve hakem cumle_no aynı bölmeyi kullanır; gövde cümleleri 1'den numaralanır)."""
    parca, bas = [], 0
    for m in _CUMLE_SONU.finditer(metin):
        parca.append(metin[bas:m.end()].strip())
        bas = m.end()
    parca.append(metin[bas:].strip())
    return [p for p in parca if p]


# ---------------------------------------------------------------- yazar dosyası

def ayristir(metin):
    """Yazar dosyası -> blok listesi. Her blok: satir, figur, yer, yan (liste), sorun, cozum, tohum, degisim
    ((eski, yeni) ya da None), onarim (ebeveyn sha1 ya da None), govde (ham), bicim_hatalari (K1'e gider), ham (bloğun metni). Normalizasyon yapılmaz;
    kanonik kayıt için kayit(blok)."""
    satirlar = metin.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    baslar = [i for i, s in enumerate(satirlar) if HEADER.match(s)]
    on = "\n".join(satirlar[:baslar[0]] if baslar else satirlar).strip()
    bloklar = []
    if on:
        bloklar.append({"satir": 1, "figur": None, "yer": None, "yan": [], "sorun": None, "cozum": None,
                        "tohum": None, "degisim": None, "onarim": None, "govde": on, "bicim_hatalari": ["başlıksız metin"], "ham": on})
    for j, i in enumerate(baslar):
        son = baslar[j + 1] if j + 1 < len(baslar) else len(satirlar)
        bloklar.append(_blok(satirlar[i:son], i + 1))
    return bloklar


def _blok(satirlar, satir_no):
    b = {"satir": satir_no, "figur": None, "yer": None, "yan": [], "sorun": None, "cozum": None, "tohum": None,
         "degisim": None, "onarim": None, "govde": "", "bicim_hatalari": [], "ham": "\n".join(satirlar).strip()}
    hata = b["bicim_hatalari"]
    alanlar = [a.strip() for a in HEADER.match(satirlar[0]).group(1).split("|")]
    if len(alanlar) != 3:
        hata.append(f"başlık 3 alan değil ('### Figür | yer | yan', yansızsa '-'): {len(alanlar)} alan")
    b["figur"] = alanlar[0] if alanlar else None
    b["yer"] = alanlar[1] if len(alanlar) > 1 else None
    b["yan"] = _yan_listesi(alanlar[2]) if len(alanlar) > 2 else []
    sira, govde, meta_bitti = [], [], False
    for s in satirlar[1:]:
        m = META.match(s)
        if not meta_bitti and m:
            anahtar, deger = m.group(1), m.group(2).strip()
            sira.append(anahtar)
            if anahtar == "plan":
                parca = [p.strip() for p in deger.split("|")]
                if len(parca) != 2:
                    hata.append("@plan satırı tam bir '|' içermeli")
                b["sorun"], b["cozum"] = parca[0], ("|".join(parca[1:]) if len(parca) > 1 else None)
            elif anahtar == "tohum":
                b["tohum"] = deger
            elif anahtar == "degisim":
                d = DEGISIM.match(deger)
                if d:
                    b["degisim"] = (d.group(1), d.group(2))
                else:
                    hata.append("@degisim biçimi '<eski> -> <yeni>' olmalı")
            elif anahtar == "onarim":
                if ONARIM.match(deger):
                    b["onarim"] = deger
                else:
                    hata.append("@onarim biçimi '<ebeveyn sha1 (40 onaltılık)>' olmalı")
            else:
                hata.append(f"bilinmeyen satır @{anahtar}")
            continue
        if not s.strip() and not govde:
            continue
        meta_bitti = True
        govde.append(s)
    while govde and not govde[-1].strip():
        govde.pop()
    b["govde"] = "\n".join(govde).strip()
    beklenen = ["plan", "tohum"] + [k for k in ("degisim", "onarim") if k in sira]
    if sira != beklenen:
        hata.append(f"satır sırası {sira} (beklenen {beklenen}: başlık, @plan, @tohum[, @degisim][, @onarim], "
                    "gövde)")
    if any(META.match(s) or HEADER.match(s) for s in govde):
        hata.append("gövdede '@' ya da '###' satırı")
    return b


def kayit(blok):
    """Blok -> normalleştirilmiş kanonik kayıt."""
    return kanonik(blok["figur"], blok["yer"], blok["yan"], blok["sorun"], blok["cozum"], blok["govde"])


def blok_yaz(kayit, tohum, degisim=None, onarim=None):
    """Kanonik kayıt -> yazar dosyası bloğu (ayristir'in tersi)."""
    satir = [f"### {kayit['figur']} | {kayit['yer']} | {', '.join(kayit['yan']) or '-'}",
             f"@plan: {kayit['sorun']} | {kayit['cozum']}", f"@tohum: {tohum}"]
    if degisim:
        satir.append(f"@degisim: {degisim[0]} -> {degisim[1]}")
    if onarim:
        satir.append(f"@onarim: {onarim}")
    return "\n".join(satir + [kayit["govde"]]) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("dosya")
    ap.add_argument("--dizgi", action="store_true", help="eğitim dizgisini yaz")
    ap.add_argument("--plan", type=int, default=1)
    ap.add_argument("--yan", type=int, default=1)
    ap.add_argument("--json", action="store_true", help="kanonik kayıtları JSON satırı olarak yaz")
    a = ap.parse_args()
    with open(a.dosya, encoding="utf-8") as f:
        bloklar = ayristir(f.read())
    for b in bloklar:
        k = kayit(b)
        if a.json:
            print(json.dumps({"kimlik": kimlik(k), "sha1": sha1(k), "tohum": b["tohum"], "degisim": b["degisim"],
                              "bicim_hatalari": b["bicim_hatalari"], "kayit": k}, ensure_ascii=False))
        elif a.dizgi:
            print(dizgi(k, bool(a.plan), bool(a.yan)) + "\n<|endoftext|>")
        else:
            print(f"{kimlik(k)}  satır {b['satir']}  tohum {b['tohum']}"
                  + (f"  BİÇİM: {'; '.join(b['bicim_hatalari'])}" if b["bicim_hatalari"] else ""))


if __name__ == "__main__":
    sys.exit(main())
