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
def kucuk(s):
    """Türkçe küçük harf: str.lower() "İ"yi "i" + birleşik nokta yapar ("İkisi" -> "i̇kisi"), kelime
    düzenli ifadesi onu "kisi" diye böler; "I" da "ı" olmalı."""
    return s.replace("I", "ı").replace("İ", "i").lower()


BUYUK = re.compile(r"[A-ZÇĞİÖŞÜ][a-zçğıöşü]+")
HAYVAN = ["kuş", "sincap", "yengeç", "fare", "tavşan", "kedi", "köpek", "ayı", "tilki", "kurbağa", "balık", "kelebek",
          "karınca", "baykuş", "kaplumbağa", "penguen", "dinozor", "ejderha", "aslan",
          "inek", "koyun", "tavuk", "ördek", "yunus", "maymun", "zürafa", "kirpi", "salyangoz", "uğur böceği"]


def cezalar(metin, kimlikler, n_token=0, n_max=240, bitti=None, plan=None):
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
    ilk_yari, ikinci_yari = kucuk(metin[:len(metin) // 2]), kucuk(metin[len(metin) // 2:])
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
    kelimeler = re.findall(r"[a-zçğıöşüâîû]+", kucuk(metin))
    if SOZLUK is not None:
        bilinmeyen = [w for w in kelimeler if w not in SOZLUK]
        if bilinmeyen:
            c.append((1.5 * len(bilinmeyen), f"uydurma kelime {bilinmeyen[:4]}"))
    uclu = [tuple(kelimeler[i:i + 3]) for i in range(len(kelimeler) - 2)]
    tekrar = len(uclu) - len(set(uclu))
    if tekrar > 2:
        c.append((0.5 * (tekrar - 2), f"tekrar eden ifade x{tekrar}"))
    return c + olay_cezalari(metin, isimler, plan)


# --- olay örgüsü kuralları (docs/HIKAYE_ANALIZI.md: E3 modelinin 50 hikâyesinde görülen hatalar) ---------------
# Her kural eğitim verisinin 2364 hikâyesinde denendi; yanlış alarm oranı HIKAYE_ANALIZI.md'de.
EK_ISIM = r"['’](?:y?[ıiuü]|y?[ae]|n?[ıiuü]n|n[ıiuü]n|[dt][ae]n?|l[ae])\b"   # Paytak'ı, Bal'ın, Karabaş'a, Dino'ya
# Eğitim verisinde geçen ikilemeler (paytak paytak, yavaş yavaş, üzgün üzgün, ...): bunların dışındaki "X X" kekeme
IKILEME = set("""paytak yavaş tek üzgün adım mutlu sık pırıl uzun ağır mışıl hızlı tekrar sakin için teker güle tıklım
tatlı çekingen ürkek tir birer utana parıl seve araya şırıl beyaz rahat yudum dilim ışıl geri hüzünlü pır uğraşa kaşık
derin kova kızgın usul sıkı azar sesli hayran köşe halsiz düşünceli tuhaf bol didik küskün sallaya diz suçlu tane güzel
dalgın ara kat ağaç yorgun koşa neşeli sevinçli minik küçük""".split())
# Figürün özelliği başka bir karaktere geçmesin: (desen, izin veren desen). İzin deseni hikâyede yoksa ceza.
KUS = (r"\b(?:kuş|cikcik|baykuş|serçe|güvercin|ördek|tavuk|martı|leylek|kaz\b|keklik|papağan|horoz|civciv|kartal|karga"
       r"|bülbül|kırlangıç|penguen|paytak)")
OZELLIK = [
    (r"\bgaga", KUS, "gaga ama kuş yok"),
    (r"kuyruğunu salla", r"\b(?:köpe|karabaş|kedi|tekir|tilki|kızıl|sincap|kuzu|keçi|alev|ejderha|dino|dinozor)",
     "kuyruk sallayan yok"),
    (r"baloncuk", r"\b(?:alev|ejderha|sabun)", "baloncuk ama Alev yok"),
    (r"burnunu sok", r"\b(?:tekir|kedi|karabaş|köpe)", "burnunu sokan yanlış karakter"),
    (r"kabuğunu (?:çıkar|bırak|at)", r"$^", "kabuğunu çıkaran kaplumbağa"),
]
# Sondaki ders cümlesinin değeri -> gövdede o değeri gösteren olay kelimeleri (eğitim hikâyelerinde ders adı çoğu kez
# yalnız sonda geçer, ama olay gövdededir: paylaşma dersi öncesinde bir şey verilir/bölünür).
DERS_KANIT = {
    "paylaş": r"paylaş|verdi|verme|uzattı|böl|ikiye|yarısı|ikram|ayırdı|birlikte (?:yedi|oyna|kullan)|sıra",
    "kıskan": r"kıskan|imren|kendisi(?:ni|nin)? de|yalnız kal|onu da|başkasıyla|yeni (?:bir )?arkada",
    "dürüst": r"dürüst|doğruyu|itiraf|kırdı|kırıl|devir|özür|sakla|yalan|suç",
    "sabır": r"sabır|sabırl|bekle|sıra|yavaş|acele|tekrar dene|denedi",
    "dikkat": r"dikkat|düştü|devir|kırıl|kaybol|çarp|takıl|kay(?:dı|ıp)",
    "özür": r"özür|kırdı|kırıl|devir|çarp|üzdü|bozdu",
    "cesar": r"cesar|cesur|kork|çekin|utan",
    "yardım": r"yardım|kurtar|çıkar|kaldır|taşı|destek|uzan|birlikte|getir|göster|düzelt|topla",
}
DERS = re.compile(r"(?:anladı|öğrendi|fark etti|anlamıştı|öğrenmişti)")
def plan_cezasi(plan):
    """E3 planı biçimsizse (iki 'Çözüm:', boş sorun/çözüm) ceza. Plan-hikâye kelime uyumu da denendi (sorun kelimeleri
    ilk %60'ta, çözümünkiler son %60'ta), ama genel kalite hakemlerinde seçimi kötüleştirdi: HIKAYE_ANALIZI.md."""
    m = re.fullmatch(r"Sorun:[ \t]*([^\n]*?)\s*\nÇözüm:[ \t]*([^\n]*?)\s*", plan)
    return [] if m and m.group(1) and m.group(2) else [(2, "plan bozuk")]


def olay_cezalari(metin, isimler, plan=None):
    c = []
    kmetin = kucuk(metin)
    cumleler = [s for s in re.split(r"(?<=[.!?])\s+", metin) if s.strip()]
    for n in isimler:
        if len(re.findall(rf"\b{n} adında", metin)) > 1:
            c.append((3, f"{n} iki kez tanıtılıyor"))
        # aynı cümlede özne ve nesne aynı figür: "Paytak geldiğinde Paytak'ı görünce", "Bal, Bal'ın elini tuttu".
        # Arada başka özne (tırnak, iki nokta, başka ad ya da hayvan) varsa geçerli: "Bal seslendi: ... Bal'ın yanına"
        for s in cumleler:
            m = re.search(rf"^(?:[A-ZÇĞİÖŞÜ]\w*\s+){{0,2}}{n}\b(?!['’])(.*?)\b{n}{EK_ISIM}", s)
            if m and not re.search(r"[\"“”:]|\b[A-ZÇĞİÖŞÜ]", m.group(1)) \
                    and not any(re.search(rf"\b{h}", kucuk(m.group(1))) for h in HAYVAN):
                c.append((2, f"{n} kendi kendine: {s[m.start():m.end()][:40]}"))
                break
        # başka karakter figürün adını kendi adı gibi söylüyor: '"Ben de Tekir" dedi tavşan'
        if re.search(rf"\b(?:[Bb]en de|[Bb]enim adım|[Aa]dım) {n}\b[^\"”]*[\"”]\s*(?:diye \w+|dedi|sordu)\s+(?!{n}\b)[a-zçğıöşü]",
                     metin):
            c.append((2, f"başkası kendini {n} diye tanıtıyor"))
    ozel = re.findall(r"(?<![.!?\"“] )(?<!^)\b([A-ZÇĞİÖŞÜ][a-zçğıöşü]+)['’]", metin)
    bilinmeyen = sorted({w for w in ozel if w not in TUM_ISIM})
    bas = re.findall(r"(?:^|[.!?]\s+)([A-ZÇĞİÖŞÜ][a-zçğıöşü]+)['’]", metin)  # cümle başı özel ad: "Minnoş'un ..."
    bilinmeyen = sorted(set(bilinmeyen) | {w for w in bas if w not in TUM_ISIM})
    if bilinmeyen:
        c.append((2, f"uydurma karakter adı {bilinmeyen[:3]}"))
    for desen, izin, ad in OZELLIK:
        if re.search(desen, kmetin) and not re.search(izin, kmetin):
            c.append((2, f"özellik karışması: {ad}"))
    uc = [m.group(1) for m in re.finditer(r"(?<![a-zçğıöşü])([a-zçğıöşü]+) \1 \1(?![a-zçğıöşü])", kmetin)
          if m.group(1) != "paytak"]
    iki = [m.group(1) for m in re.finditer(r"(?<![a-zçğıöşü])([a-zçğıöşü]+) \1(?![a-zçğıöşü])", kmetin)
           if m.group(1) not in IKILEME]
    obek = [m.group(1) for m in re.finditer(r"(?<![a-zçğıöşü])([a-zçğıöşü]+(?: [a-zçğıöşü]+){1,3})(?:,| ve)? \1(?![a-zçğıöşü])",
                                             kmetin) if m.group(1).split()[0] not in IKILEME]
    if uc or iki or obek:
        c.append((2 if uc or obek else 1, f"kekeme tekrar {(uc + obek + iki)[:2]}"))
    # sonda ders cümlesi hikâyede hiç geçmeyen bir değerden söz ediyor ("topu buldular ... paylaşmanın güzel olduğunu anladı")
    # sonda ders cümlesi, gövdede hiç olayı olmayan bir değerden söz ediyor: "topu buldular ... paylaşmanın güzel
    # olduğunu anladı" (hakem: "ders olaydan kopuk")
    for i in range(max(3, len(cumleler) - 3), len(cumleler)):
        s = kucuk(cumleler[i])
        if DERS.search(s):
            govde = kucuk(" ".join(cumleler[:i]))
            yok = [v for v, kanit in DERS_KANIT.items() if v in s and not re.search(kanit, govde)]
            if yok:
                c.append((1.5, f"ders olaydan kopuk ({yok[0]})"))
                break
    if plan is not None:
        c += plan_cezasi(plan)
    return c


# 3-6 yaşa uygun olmayan içerik (tam veri denetiminde bozukların ~yarısı): yaralanma, boğulma, derin su, tehlike.
# "gözyaşlarına boğuldu" deyimi hariç. Ürün yolunda (arayüz, kart) her zaman açık; hakem deneylerinde karşılaştırma
# tutarlılığı için isteğe bağlı (puanla(guvenlik=True)).
GUVENLIK = re.compile(r"(?<![a-zçğıöşü])(?:incit\w*|yaral\w*|(?<!gözyaşlarına )boğul\w*|kanıyor\w*|kanama\w*"
                      r"|acıyor\w*|derin su\w*|tehlike\w*"
                      r"|kan(?:lar)?(?![a-zçğıöşü])|diz\w* kana\w*|yara(?:sı|lar|ları)?(?![a-zçğıöşü])|yara band\w*"
                      r"|canı acı\w*)")


def guvenlik_cezasi(metin):
    bul = sorted(set(GUVENLIK.findall(kucuk(metin))))
    return (4.0, f"çocuğa uygun olmayan: {', '.join(bul[:3])}") if bul else None


YER_KELIME = {"orman": r"\borman", "deniz": r"\b(?:deniz|kumsal|sahil|kıyı)", "ev": r"\bev(?:de|e|in|i|den|imiz)?\b",
              "park": r"\bpark", "sato": r"\bşato", "dag": r"\bda(?:ğ|ğı|ğa|ğda|ğın)\b"}


def yer_cezasi(metin, yer):
    """Seçilen yer yerine başka bir yerde biten hikâye (hakem: 'şatoda başlayıp ormanda bitiyor')."""
    son = kucuk(metin[int(len(metin) * 0.5):])
    kendi = len(re.findall(YER_KELIME[yer], kucuk(metin)))
    baska = max((len(re.findall(p, son)) for y, p in YER_KELIME.items() if y != yer), default=0)
    return 1.5 if kendi == 0 or baska > kendi else 0


def puanla(metin, kimlikler, ort_logp=0.0, n_token=0, yer=None, bitti=None, guvenlik=False, plan=None):
    ceza = sum(p for p, _ in cezalar(metin, kimlikler, n_token, bitti=bitti, plan=plan)) + (yer_cezasi(metin, yer) if yer else 0)
    if guvenlik and (g := guvenlik_cezasi(metin)):
        ceza += g[0]
    return -ceza + 2 * ort_logp
