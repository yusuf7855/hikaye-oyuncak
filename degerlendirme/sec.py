"""Aday hikâye seçici: oyuncak boştayken K aday üretir, en yüksek puanlıyı okur.

puan = kural cezaları (her biri basit metin kontrolü, ESP32'de de ucuz) + 2 × ortalama log-olasılık.
"""
import os
import pickle
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from baslangic import KAR, YABANCI  # noqa: E402

TUM_ISIM = {k["isim"] for k in KAR.values()}
_SOZLUK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sozluk.pkl")
SOZLUK = pickle.load(open(_SOZLUK, "rb")) if os.path.exists(_SOZLUK) else None  # kartta ~700 KB flash'ta
BUYUK = re.compile(r"[A-ZÇĞİÖŞÜ][a-zçğıöşü]+")
HAYVAN = ["kuş", "sincap", "yengeç", "fare", "tavşan", "kedi", "köpek", "ayı", "tilki", "kurbağa", "balık", "kelebek",
          "karınca", "baykuş", "kaplumbağa", "penguen", "dinozor", "ejderha", "aslan",
          "inek", "koyun", "tavuk", "ördek", "yunus", "maymun", "zürafa", "kirpi", "salyangoz", "uğur böceği"]


def cezalar(metin, kimlikler, n_token=0, n_max=240, bitti=None):
    """bitti: model hikâye sonu token'ı üretti mi. Bilinmiyorsa (None) n_token >= n_max yarım sayılır;
    ama bağlam sınırında kesilen hikâye n_max'a hiç ulaşmayabilir, o yüzden bilindiğinde bitti kullanılır."""
    isimler = [KAR[k]["isim"] for k in kimlikler]
    c = []
    for n in isimler:
        if len(re.findall(rf"\b{n}\b", metin)) < 2:
            c.append((3, f"{n} hikâyede yeterince yok"))
        if re.search(rf"\b{n}\b,?\s+{n}['’]", metin):
            c.append((2, f"kendine gönderme {n}"))
    son = metin[int(len(metin) * 0.6):]  # son %40: figür burada da olmalı (hakem: "figür yarıda kayboluyor")
    for n in isimler:
        if not re.search(rf"\b{n}\b", son):
            c.append((3, f"{n} sonda yok"))
        if re.search(rf"\b{n}\b\s+ve\s+{n}\b", metin):
            c.append((3, f"'{n} ve {n}'"))
    ilk_yari, ikinci_yari = metin[:len(metin) // 2].lower(), metin[len(metin) // 2:].lower()
    yeni = [h for h in HAYVAN if re.search(rf"\b{h}", ikinci_yari) and not re.search(rf"\b{h}", ilk_yari)
            and h not in {KAR[k]["tur"] for k in kimlikler}]
    if yeni:
        c.append((1.5 * len(yeni), f"sonradan beliren karakter {yeni}"))
    konusan = re.findall(r'["”]\s*(?:diye \w+|dedi|sordu)\s+([A-ZÇĞİÖŞÜa-zçğıöşü]+)', metin)
    if any(a == b for a, b in zip(konusan, konusan[1:])):
        c.append((1, "aynı konuşmacı üst üste"))
    yanlis = (set(BUYUK.findall(metin)) & ((TUM_ISIM - set(isimler)) | set(YABANCI)))
    if yanlis:
        c.append((2, f"yanlış isim {sorted(yanlis)}"))
    cumleler = [s.strip() for s in re.split(r"(?<=[.!?])\s+", metin) if s.strip()]
    if len(cumleler) != len(set(cumleler)):
        c.append((1, "tekrarlanan cümle"))
    kesik = (not bitti) if bitti is not None else n_token >= n_max
    if not metin.rstrip().endswith((".", "!", '"', "”")) or kesik:
        c.append((2, "yarım son"))
    if len(metin.split()) < 50:
        c.append((2, "çok kısa"))
    kelimeler = re.findall(r"[a-zçğıöşüâîû]+", metin.lower())
    if SOZLUK is not None:
        bilinmeyen = [w for w in kelimeler if w not in SOZLUK]
        if bilinmeyen:
            c.append((1.5 * len(bilinmeyen), f"uydurma kelime {bilinmeyen[:4]}"))
    uclu = [tuple(kelimeler[i:i + 3]) for i in range(len(kelimeler) - 2)]
    tekrar = len(uclu) - len(set(uclu))
    if tekrar > 2:
        c.append((0.5 * (tekrar - 2), f"tekrar eden ifade x{tekrar}"))
    return c


YER_KELIME = {"orman": r"\borman", "deniz": r"\b(?:deniz|kumsal|sahil|kıyı)", "ev": r"\bev(?:de|e|in|i|den|imiz)?\b",
              "park": r"\bpark", "sato": r"\bşato", "dag": r"\bda(?:ğ|ğı|ğa|ğda|ğın)\b"}


def yer_cezasi(metin, yer):
    """Seçilen yer yerine başka bir yerde biten hikâye (hakem: 'şatoda başlayıp ormanda bitiyor')."""
    son = metin[int(len(metin) * 0.5):].lower()
    kendi = len(re.findall(YER_KELIME[yer], metin.lower()))
    baska = max((len(re.findall(p, son)) for y, p in YER_KELIME.items() if y != yer), default=0)
    return 1.5 if kendi == 0 or baska > kendi else 0


def puanla(metin, kimlikler, ort_logp=0.0, n_token=0, yer=None, bitti=None):
    ceza = sum(p for p, _ in cezalar(metin, kimlikler, n_token, bitti=bitti)) + (yer_cezasi(metin, yer) if yer else 0)
    return -ceza + 2 * ort_logp
