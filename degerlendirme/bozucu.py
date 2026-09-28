"""Kanarya üretici (KUSURSUZ_VERI.md Adım 0g, 'Hakem düzeni / KANARYA').

Kabul edilmiş ya da altın setteki bir hikâyeye (taban) merceğin türünden TEK, küçük ve akıcı bir kusur ekler; her
adayı kapi.py'den (K1–K9, K11) geçirir. Kodun yakaladığı aday atılır (o tür o tabanda kanarya olamaz) ve sıradaki
tür denenir. Kanarya kaydı gerçek hikâyelerle aynı biçimde kimlik taşır ('urun/<figür>#sha1[:10]'); hangi kaydın
kanarya olduğu yalnız bu kayıttadır ('ad_alani': 'kanarya'). Kanarya eğitim klasörüne ya da izin listesine yazılmaz.

Mercek türleri (yalnız kodun göremediği kusurlar; kod bunları yakalarsa aday atılır):
  M: cozum_sil (çözüm cümlesi silinir), sacma_sebep (sorun cümlesine saçma 'çünkü'), celiski (sonradan geçen
     nesnenin rengi/boyu değişir), cozum_yana (çözüm cümlesinin öznesi yan olur), ikinci_sorun (çözülmeyen ikinci
     sorun), sebepsiz_nesne (açıklanmadan beliren nesne)
  D: tamlama (iyelik eki silinir: 'kuş yuvası' -> 'kuş yuva'), ozne_fiil (cansız özneye canlı fiili),
     konusan (replikte konuşan değişir), zamir (iki karakterli bağlamda özne 'O' olur), kendi_kendine (adsız
     kendi kendine replik)
  K: iliski (kart dışı akrabalık: 'Niloya aslında Murat'ın kızıydı'), ozellik_aykiri (figürün kart özelliğine
     aykırı davranış), yer_aykiri (yer tarifine aykırı sahne), yetenek_esya (kartta olmayan yetenek ya da eşya),
     tehlike (listede olmayan sözcükle taklit edilir tehlike, alay, korkutucu öğe ya da kalıp yargı)
Biçimsel türler (BICIMSEL; kanarya OLAMAZ, yalnız kod birim testinde kapıların %100 yakaladığını göstermek için):
  kesme_eki (Tosbi'nın), sertlesme (koşdu), yalin_yor, yalin_mis (tırnak dışı), sapka (hâlâ), baska_figur,
  tohum_disi_yan, kart_disi_canli (keçi), ertesi_sabah, hastaydi.

Kullanım: .venv/bin/python degerlendirme/bozucu.py uret <yazar dosyası> --tohum <tohum.jsonl> --lens M|D|K
              [--tur <tür>] [--tohum-sayi 2026] [--cikti kanarya.jsonl] [--taslak-kart]
          .venv/bin/python degerlendirme/bozucu.py bicimsel <yazar dosyası> --tohum <tohum.jsonl> [--taslak-kart]
              (her biçimsel türü her tabana uygular; kapıların yakalama tablosunu yazar)
Kütüphane: kanarya(taban_kayit, tohum, lens, bg, rng) -> kayıt ya da None; bicimsel(taban_kayit, tohum, tur, bg, rng)
"""
import argparse
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import kapi  # noqa: E402
import sade_sozluk  # noqa: E402
import urun_kayit as uk  # noqa: E402
from urun_kayit import kucuk  # noqa: E402

UNLU = "aeıioöuü"
SERT = "çfhkpsşt"
H = kapi.H
YUMUSAMA = {"p": "b", "ç": "c", "t": "d", "k": "ğ"}
DUZENSIZ_FIIL = {"git": "gid", "et": "ed", "tat": "tad", "güt": "güd"}   # ünlüyle başlayan ekten önce
RENK = ["kırmızı", "mavi", "sarı", "yeşil", "beyaz", "mor", "turuncu", "pembe"]
ZIT = {"büyük": "küçük", "küçük": "büyük", "uzun": "kısa", "kısa": "uzun", "ağır": "hafif", "hafif": "ağır",
       "dolu": "boş", "boş": "dolu", "ıslak": "kuru", "kuru": "ıslak", "sıcak": "soğuk", "soğuk": "sıcak",
       "temiz": "kirli", "kirli": "temiz", "yeni": "eski", "eski": "yeni", "kalın": "ince", "ince": "kalın",
       "kocaman": "küçücük", "küçücük": "kocaman", "yumuşak": "sert", "sert": "yumuşak"}
SACMA_SEBEP = ["çünkü çimenler yeşildi", "çünkü bulutlar beyazdı", "çünkü taşlar griydi", "çünkü gökyüzü maviydi"]
SEBEPSIZ = ["ip", "kova", "sepet", "kutu", "fener", "mendil", "yastık", "şemsiye"]
KENDI_KENDINE = ['"Bunu ben yapabilirim," dedi kendi kendine.', '"Hadi, biraz daha deneyelim," dedi kendi kendine.',
                 '"Bir yolunu bulmalıyım," dedi kendi kendine.']
# ikinci sorunda kaybolamayacak (taşınmaz ya da sahnenin parçası olan) adlar
SABIT = {"ağaç", "çalı", "dal", "kum", "su", "güneş", "gökyüzü", "deniz", "dağ", "orman", "park", "ev", "kabuk",
         "teker", "bahçe", "çit", "yol", "tepe", "yokuş", "taş", "kaya", "dalga", "rüzgar", "hava", "bulut", "çimen",
         "kar", "buz", "pencere", "kapı", "duvar", "yer", "kenar", "kıyı", "şato", "saray", "sabah", "gün", "akşam",
         "burun", "kulak"}
IKINCI_SORUN = ["O sırada gökyüzü karardı ve yağmur başladı.", "O sırada {ad} çok acıktı."]
YER_AYKIRI = {"orman": "Ormanda tek bir ağaç bile yoktu.", "dağ": "Dağda hiç yokuş yoktu, her yer düzdü.",
              "deniz": "Kıyıda hiç kum ve su yoktu.", "ev": "Evin ortasında kocaman bir göl vardı.",
              "park": "Parkta hiç ağaç ve oyuncak yoktu.", "şato": "Şato küçücük bir çadır gibiydi."}
YETENEK = {"hayvan": ["{ad} kanatlarını açıp biraz uçtu.", "{ad} cebinden küçük bir fener çıkardı."],
           "insan": ["{ad} cebinden sihirli bir kalem çıkardı.", "{ad} kanatlarını açıp biraz uçtu."]}
TEHLIKE = {"ev": ["{ad} sandalyenin üstüne çıkıp dolabın tepesine uzandı."],
           "dis": ["{ad} tek başına suyun en derin yerine doğru yürüdü.", "{ad} yüksek bir kayanın ucuna kadar çıktı."],
           "korku_dis": ["Ağaçların arasında karanlık bir gölge dolaştı.",
                         "Birden uzaktan garip ve korkunç bir ses geldi."],
           "korku_ic": ["Birden kapının arkasından garip bir ses geldi.", "Karanlık köşede korkunç bir gölge dolaştı."],
           "kalip": ["Kızlar böyle işleri hiç yapamazdı.", "Kızlar top oynamayı hiç bilmezdi."]}
# figürün kart özelliğine aykırı davranış (kartın yasak düzenli ifadelerine takılmayan biçimde)
OZELLIK_AYKIRI = {
    "Niloya": ["Niloya hiçbir şeyi merak etmedi.", "Niloya şarkı söylemeyi hiç sevmezdi."],
    "Maşa": ["Maşa bütün sabah hiç kıpırdamadan oturdu.", "Maşa reçeli hiç sevmezdi."],
    "Pepee": ["Pepee yeni şeyleri hiç sevmezdi.", "Pepee dans etmeyi hiç sevmezdi."],
    "Keloğlan": ["Keloğlan işini yarıda bırakıp gitti.", "Keloğlan kimseye doğruyu söylemedi."],
    "Doru": ["Doru çok yavaş ve korkak bir attı.", "Doru kimseye yardım etmek istemedi."],
    "Hayri": ["Hayri yemek yemeyi hiç sevmezdi.", "Hayri baklava yemeyi hiç sevmezdi."],
    "Şakir": ["Şakir o gün şapkasız dolaştı.", "Şakir maceradan hiç hoşlanmazdı."],
    "Elsa": ["Elsa buzdan hiçbir şey yapamadı.", "Elsa kar ve buzdan hiç hoşlanmazdı."],
    "Chase": ["Chase kuralları hiç dinlemedi.", "Chase hiçbir kokuyu alamadı."],
    "Örümcek Adam": ["Örümcek Adam hiç ağ atamadı.", "Örümcek Adam duvara hiç çıkamadı."],
    "Tosbi": ["Tosbi bir anda dalın yanına vardı.", "Tosbi hiç beklemek istemedi ve hemen kızdı."],
    "Tekir": ["Tekir hiçbir şeyi merak etmezdi.", "Tekir hiçbir şeye bakmak istemedi."],
    "Pamuk": ["Pamuk zıplamayı hiç sevmezdi.", "Pamuk havucu hiç sevmezdi."],
    "Karabaş": ["Karabaş arkadaşını orada bırakıp gitti.", "Karabaş top oynamayı hiç sevmezdi."],
}
TURLER = {"M": ["cozum_sil", "sacma_sebep", "celiski", "cozum_yana", "ikinci_sorun", "sebepsiz_nesne"],
          "D": ["tamlama", "ozne_fiil", "konusan", "zamir", "kendi_kendine"],
          "K": ["iliski", "ozellik_aykiri", "yer_aykiri", "yetenek_esya", "tehlike"]}
BICIMSEL = {"kesme_eki": "K5.kesme_eki", "sertlesme": "K5.sertlesme", "yalin_yor": "K5.zaman",
            "yalin_mis": "K5.zaman", "sapka": "K3.sapka", "baska_figur": "K4.baska_figur",
            "tohum_disi_yan": ("K4.tohum_disi_yan", "K4.canli_rol"), "kart_disi_canli": "K4.canli_rol",
            "ertesi_sabah": "K1.zaman", "hastaydi": "K7.saglik"}


# ---------------------------------------------------------------- Türkçe biçim üretimi

def son_unlu(s):
    for c in reversed(kucuk(s)):
        if c in UNLU:
            return c
    return "e"


def u2(s):
    return "a" if son_unlu(s) in "aıou" else "e"


def u4(s):
    return {"a": "ı", "ı": "ı", "e": "i", "i": "i", "o": "u", "u": "u", "ö": "ü", "ü": "ü"}[son_unlu(s)]


def buyuk_bas(s):
    return {"i": "İ", "ı": "I"}.get(s[:1], s[:1].upper()) + s[1:]


def hece(s):
    return sum(c in UNLU for c in kucuk(s))


def yumusat(k):
    """Ünlüyle başlayan ekten önce çok heceli adların sonundaki p ç t k yumuşar (kitap -> kitab-, renk -> reng-)."""
    if hece(k) > 1 and k[-1] in YUMUSAMA:
        return k[:-1] + ("g" if k.endswith("nk") else YUMUSAMA[k[-1]])
    return k


def iyelik3(k):
    return k + "s" + u4(k) if k[-1] in UNLU else yumusat(k) + u4(k)


def ad_eki(ad, okunus, hal):
    """Özel ad + kesme + hâl eki, okunuşa göre (Chase -> Chase'in, Chase'ten; Tosbi -> Tosbi'nin)."""
    ok = kucuk(okunus)
    unlu, sert = ok[-1] in UNLU, ok[-1] in SERT
    ek = {"in": ("n" if unlu else "") + u4(ok) + "n", "i": ("y" if unlu else "") + u4(ok),
          "e": ("y" if unlu else "") + u2(ok), "de": ("t" if sert else "d") + u2(ok),
          "den": ("t" if sert else "d") + u2(ok) + "n", "le": ("y" if unlu else "") + "l" + u2(ok)}[hal]
    return f"{ad}'{ek}"


def de_da(k):
    return "da" if son_unlu(k) in "aıou" else "de"


def ek_fiil_gecmis(k):
    """kızı -> kızıydı, çocuğu -> çocuğuydu."""
    return k + ("y" if k[-1] in UNLU else "") + ("t" if k[-1] in SERT else "d") + u4(k)


def gecmis_govde(w):
    """'bekledi' -> 'bekle', 'koştu' -> 'koş' (3. tekil -dı); değilse None."""
    return w[:-2] if re.search(r"[dt][ıiuü]$", w) and len(w) > 3 else None


def mis_bicimi(govde):
    return govde + "m" + u4(govde) + "ş"


def yor_bicimi(govde):
    if govde in ("de", "ye"):
        return govde[0] + "iyor"
    if govde[-1] in "ae":
        g = govde[:-1]
        return g + u4(g) + "yor"
    if govde[-1] in "ıiuü":
        return govde + "yor"
    g = DUZENSIZ_FIIL.get(govde, govde)
    return g + u4(g) + "yor"


# ---------------------------------------------------------------- metin yardımcıları

def _cs(kayit):
    return uk.cumleler(kayit["govde"])


def _yeni(kayit, cumleler_):
    k = dict(kayit)
    k["yan"] = list(kayit["yan"])
    k["govde"] = " ".join(c for c in cumleler_ if c)
    return k


def _anlatim(c):
    return '"' not in c


def _kokler(metin, bg):
    return {bg.kok(w).rstrip("-") for w in sade_sozluk.kelimeler(metin)}


def _en_cok_ortak(cs, hedef, bg, aralik):
    """aralik içindeki cümlelerden hedef metinle en çok kök paylaşanın sırası (0 ortaksa None)."""
    h = _kokler(hedef, bg) - {"bir", "ve", "o", "bu", "çok"}
    puan = [(len(_kokler(cs[i], bg) & h), i) for i in aralik if 0 <= i < len(cs)]
    puan = [p for p in puan if p[0] > 0]
    return max(puan)[1] if puan else None


def _ekle(cs, i, cumle):
    return cs[:i] + [cumle] + cs[i:]


def _kucuk_bas(c, bg):
    """Cümlenin başına bir şey eklenecekse ilk harfi küçült (ad değilse)."""
    w = re.match(rf"[{H}]+", c)
    if w and not bg.ad_gibi(w.group(0)) and w.group(0)[0].isupper():
        return kucuk(c[0]) + c[1:]
    return c


def _dunya(kayit, bg):
    return bg.dunya(kayit["figur"])


def _yan_adi(kayit, bg, konusan=False):
    d = _dunya(kayit, bg)
    ys = [y for y in kayit["yan"] if y in d.yanlar and (not konusan or kapi._olgu(d.yanlar[y]["konusur"]))]
    return ys[0] if ys else None


def _cozum_cumlesi(kayit, bg):
    cs = _cs(kayit)
    return _en_cok_ortak(cs, kayit["cozum"], bg, range(max(2, len(cs) // 3), len(cs) - 1))


def _sorun_cumlesi(kayit, bg):
    cs = _cs(kayit)
    return _en_cok_ortak(cs, kayit["sorun"], bg, range(0, min(4, len(cs))))


# ---------------------------------------------------------------- M

def m_cozum_sil(kayit, tohum, bg, rng):
    i = _cozum_cumlesi(kayit, bg)
    if i is None:
        return None
    cs = _cs(kayit)
    return _yeni(kayit, cs[:i] + cs[i + 1:]), f"çözüm cümlesi silindi: {cs[i]!r}", [i + 1]   # silinenin yeri


def m_sacma_sebep(kayit, tohum, bg, rng):
    i = _sorun_cumlesi(kayit, bg)
    if i is None:
        return None
    cs = _cs(kayit)
    c = cs[i]
    if not _anlatim(c):
        return None
    sebep = rng.choice(SACMA_SEBEP)
    if " çünkü " in c:
        yeni = re.sub(r"çünkü [^.!?]*", sebep, c, count=1)
    else:
        yeni = re.sub(r"([.!?]+)$", rf", {sebep}\1", c)
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"sorunun sebebi saçma: {yeni!r}", [i + 1]


def m_celiski(kayit, tohum, bg, rng):
    cs = _cs(kayit)
    for i, c in enumerate(cs):
        for m in re.finditer(rf"(?<![{H}])({'|'.join(RENK + list(ZIT))}) (?:bir )?([{H}]+)", c):
            sifat, isim = m.group(1), m.group(2)
            isim_k = bg.kok(isim)
            if isim_k.endswith("-"):
                continue
            yeni_sifat = ZIT.get(sifat) or rng.choice([r for r in RENK if r != sifat])
            for j in range(len(cs) - 1, i, -1):
                for m2 in re.finditer(rf"(?<![{H}])(?:{sifat} )?({re.escape(isim_k)}[{H}]*)", kucuk(cs[j])):
                    if bg.kok(m2.group(1)) != isim_k:
                        continue
                    bas = m2.start()
                    isim_metin = cs[j][m2.start(1):m2.end(1)]
                    sifat_metin = yeni_sifat
                    if cs[j][bas].isupper():              # cümle başı: büyük harf sıfata geçer
                        isim_metin, sifat_metin = kucuk(isim_metin[0]) + isim_metin[1:], buyuk_bas(yeni_sifat)
                    yeni = cs[j][:bas] + f"{sifat_metin} {isim_metin}" + cs[j][m2.end():]
                    return (_yeni(kayit, cs[:j] + [yeni] + cs[j + 1:]),
                            f"çelişki: önce {sifat} {isim}, sonra {yeni_sifat}: {yeni!r}", [i + 1, j + 1])
    return None


def m_cozum_yana(kayit, tohum, bg, rng):
    yan = _yan_adi(kayit, bg)
    i = _cozum_cumlesi(kayit, bg)
    if yan is None or i is None:
        return None
    d = _dunya(kayit, bg)
    cs = _cs(kayit)
    c = cs[i]
    yan_bas = buyuk_bas(yan)
    if re.match(rf"{re.escape(d.ad)}(?![{H}'])", c):
        yeni = yan_bas + c[len(d.ad):]
    elif not re.search(rf"(?<![{H}]){re.escape(kucuk(yan))}", kucuk(c)) and _anlatim(c):
        yeni = f"{yan_bas} {_kucuk_bas(c, bg)}"
    else:
        return None
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"çözüm yana geçti: {yeni!r}", [i + 1]


def m_ikinci_sorun(kayit, tohum, bg, rng):
    i = _sorun_cumlesi(kayit, bg)
    if i is None:
        return None
    cs = _cs(kayit)
    sorun_k = _kokler(kayit["sorun"], bg)
    kelimeler = sade_sozluk.kelimeler(kayit["govde"])
    adaylar = []
    for w in kelimeler:
        k = bg.kok(w)
        if (k in bg.tohum_kelime["isim"] and k not in sorun_k and k not in bg.canli and k not in bg.rol
                and k not in SABIT and kelimeler.count(w) == 1 and k not in _kokler(kayit["cozum"], bg)):
            adaylar.append(k)
    if adaylar:
        n = rng.choice(sorted(set(adaylar)))
        yeni = f"O sırada {n} {de_da(n)} kayboldu."
    else:
        yeni = rng.choice(IKINCI_SORUN).format(ad=_dunya(kayit, bg).ad)
        if _kokler(yeni, bg) & _kokler(kayit["govde"], bg) - {"o", "sıra", "çok", "ve"}:
            return None
    return _yeni(kayit, _ekle(cs, i + 1, yeni)), f"çözülmeyen ikinci sorun: {yeni!r}", [i + 2]


def m_sebepsiz_nesne(kayit, tohum, bg, rng):
    i = _cozum_cumlesi(kayit, bg)
    if i is None:
        return None
    kokler = _kokler(kayit["govde"], bg)
    adaylar = [x for x in SEBEPSIZ if x not in kokler]
    if not adaylar:
        return None
    x = rng.choice(adaylar)
    yeni = f"Tam o sırada yerde bir {x} belirdi."
    return _yeni(kayit, _ekle(_cs(kayit), i, yeni)), f"sebepsiz beliren nesne: {yeni!r}", [i + 1]


# ---------------------------------------------------------------- D

def _ilgi_eki_mi(w, bg):
    """w ilgi (tamlayan) ekli mi: kumun, ağacın, Spin'in, onun."""
    if "'" in w:
        return re.fullmatch(r"n?[ıiuü]n", w.split("'", 1)[1]) is not None
    if w in ("onun", "bunun", "şunun"):
        return True
    k = bg.kok(w)
    if k.endswith("-") or k == w:
        return False
    return w == (k + "n" + u4(k) + "n" if k[-1] in UNLU else yumusat(k) + u4(k) + "n")


def d_tamlama(kayit, tohum, bg, rng):
    """Belirtili tamlamada tamlananın iyelik eki silinir: 'kumun üstüne' -> 'kumun üste', 'Spin'in şapkası' ->
    'Spin'in şapka' (yalın, yönelme ve belirtme hâlleri)."""
    cs = _cs(kayit)
    adaylar = []
    for i, c in enumerate(cs):
        for m in re.finditer(rf"(?<![{H}])([{H}]+(?:'[{kapi.HARF}]+)?) ([{kapi.HARF}]+)(?![{H}'])", c):
            w1, w2 = m.group(1), m.group(2)
            if not _ilgi_eki_mi(kucuk(w1), bg):
                continue
            taban = bg.kok(w2)
            if taban.endswith("-") or len(taban) < 2 or taban == w2:
                continue
            iy = iyelik3(taban)
            yalin = taban
            yonelme = (taban + "y" + u2(taban)) if taban[-1] in UNLU else yumusat(taban) + u2(taban)
            belirtme = (taban + "y" + u4(taban)) if taban[-1] in UNLU else yumusat(taban) + u4(taban)
            karsilik = {iy: yalin, iy + "n" + u2(iy): yonelme}
            if belirtme != iy:                    # ipini -> ipi, iyelikli yalınla aynı olur: kusur değil anlam kayar
                karsilik[iy + "n" + u4(iy)] = belirtme
            if w2 in karsilik:
                adaylar.append((i, m.start(2), m.end(2), karsilik[w2], m.group(0)))
    if not adaylar:
        return None
    i, a, b, yeni_w, eski = rng.choice(adaylar)
    yeni = cs[i][:a] + yeni_w + cs[i][b:]
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"tamlama eki silindi: {eski!r} -> {yeni!r}", [i + 1]


def d_ozne_fiil(kayit, tohum, bg, rng):
    cs = _cs(kayit)
    adaylar = []
    for i, c in enumerate(cs):
        if not _anlatim(c) or i == 0:
            continue
        ks = re.findall(rf"[{H}]+(?:'[{kapi.HARF}]+)?", c)
        if len(ks) < 2:
            continue
        ozne, son = kucuk(ks[0]), ks[-1]
        if "'" in ks[0] or bg.kok(ozne) != ozne or ozne in bg.canli or ozne in bg.rol or bg.ad_gibi(ks[0]):
            continue
        if ozne not in bg.tohum_kelime["isim"] or not bg.kok(son).endswith("-") or not gecmis_govde(kucuk(son)):
            continue
        if re.search(r"l[ae]r$", kucuk(son)[:-2]):
            continue
        yonelme = any(re.search(r"(?:y?[ae])$", kucuk(w)) and not bg.kok(kucuk(w)).endswith("-") for w in ks[1:-1])
        adaylar.append((i, son, "yürüdü" if yonelme else "gülümsedi"))
    if not adaylar:
        return None
    i, son, fiil = rng.choice(adaylar)
    yeni = re.sub(rf"{re.escape(son)}([.!?]*)$", rf"{fiil}\1", cs[i])
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"cansız özneye canlı fiili: {yeni!r}", [i + 1]


def _konusmacilar(kayit, bg):
    d = _dunya(kayit, bg)
    kim = {kucuk(d.ad): d.ad}
    for y in kayit["yan"]:
        if y in d.yanlar and kapi._olgu(d.yanlar[y]["konusur"]):
            for b in d.yan_bicimleri(d.yanlar[y]):
                kim[kucuk(b)] = y
    return kim


def d_konusan(kayit, tohum, bg, rng):
    kim = _konusmacilar(kayit, bg)
    kisiler = sorted(set(kim.values()))
    if len(kisiler) < 2:
        return None
    cs = _cs(kayit)
    adaylar = []
    for i, c in enumerate(cs):
        m = re.search(rf'"\s*(?:diye\s+)?(?:dedi|sordu|bağırdı|fısıldadı|seslendi)\s+([{H}]+(?: [{H}]+)?)([.!?])$', c)
        if not m:
            continue
        ad = next((a for a in (m.group(1), m.group(1).split()[0]) if kucuk(a) in kim), None)
        if ad is None:
            continue
        simdi = kim[kucuk(ad)]
        yeni_kim = next(k for k in kisiler if k != simdi)
        adaylar.append((i, m.start(1), m.start(1) + len(ad), yeni_kim, simdi))
    if not adaylar:
        return None
    i, a, b, yeni_kim, eski = rng.choice(adaylar)
    yeni = cs[i][:a] + yeni_kim + cs[i][b:]
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"konuşan değişti: {eski} -> {yeni_kim}: {yeni!r}", [i + 1]


def d_zamir(kayit, tohum, bg, rng):
    kim = _konusmacilar(kayit, bg)
    d = _dunya(kayit, bg)
    for y in kayit["yan"]:
        if y in d.yanlar:
            for b in d.yan_bicimleri(d.yanlar[y]):
                kim.setdefault(kucuk(b), y)
    if len(set(kim.values())) < 2:
        return None
    cs = _cs(kayit)
    adaylar = []
    for i in range(2, len(cs) - 1):
        c = cs[i]
        m = re.match(rf"([{H}]+(?: [{H}]+)?)(?![{H}'])", c)
        if not m or not _anlatim(c):
            continue
        ad = next((a for a in (m.group(1), m.group(1).split()[0]) if kucuk(a) in kim), None)
        if ad is None:
            continue
        onceki = kucuk(cs[i - 1])
        baskalari = {v for k, v in kim.items() if re.search(rf"(?<![{H}]){re.escape(k)}", onceki)}
        if len(baskalari) >= 2:
            adaylar.append((i, len(ad)))
    if not adaylar:
        return None
    i, n = rng.choice(adaylar)
    yeni = "O" + cs[i][n:]
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"zamir belirsiz: {yeni!r}", [i + 1]


def d_kendi_kendine(kayit, tohum, bg, rng):
    i = _cozum_cumlesi(kayit, bg)
    if i is None:
        return None
    yeni = rng.choice(KENDI_KENDINE)
    return _yeni(kayit, _ekle(_cs(kayit), i, yeni)), f"adsız kendi kendine replik: {yeni!r}", [i + 1]


# ---------------------------------------------------------------- K

def k_iliski(kayit, tohum, bg, rng):
    d = _dunya(kayit, bg)
    rel = [x for x in ("kız", "çocuk", "yavru") if x in d.tur]
    yan = next((y for y in kayit["yan"] if y in d.yanlar and y[:1].isupper() and d.yanlar[y]["tip"] == "adli"), None)
    cs = _cs(kayit)
    if rel and yan:
        r = rel[0]
        yeni = f"{d.ad} aslında {ad_eki(yan, d.okunuslar.get(yan, yan), 'in')} {ek_fiil_gecmis(iyelik3(r))}."
        return _yeni(kayit, _ekle(cs, 2, yeni)), f"kart dışı ilişki: {yeni!r}", [3]
    # iki yan: ilişki sözcükleri yer değiştirir (kuzeni Şila -> kardeşi Şila)
    ys = [d.yanlar[y] for y in kayit["yan"] if y in d.yanlar]
    iliski = {y["kisa_ad"]: [b for b in y.get("yuzey_bicimleri", []) if b[:1].islower() and b in bg.rol | {
        x + s for x in bg.rol for s in ("i", "ı", "u", "ü", "si", "sı")}] for y in ys}
    for a in ys:
        for b in ys:
            if a is b or not iliski.get(a["kisa_ad"]) or not iliski.get(b["kisa_ad"]):
                continue
            for i, c in enumerate(cs):
                for f in iliski[a["kisa_ad"]]:
                    m = re.search(rf"(?<![{H}]){re.escape(f)} {re.escape(a['kisa_ad'])}(?![{H}])", c)
                    if m:
                        g = next((x for x in iliski[b["kisa_ad"]] if x[-1] == f[-1]), iliski[b["kisa_ad"]][0])
                        yeni = c[:m.start()] + g + c[m.start() + len(f):]
                        return (_yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]),
                                f"kart dışı ilişki: {a['kisa_ad']} {f} -> {g}", [i + 1])
    return None


def k_ozellik_aykiri(kayit, tohum, bg, rng):
    s = OZELLIK_AYKIRI.get(kayit["figur"])
    i = _cozum_cumlesi(kayit, bg)
    if not s or i is None:
        return None
    yeni = rng.choice(s)
    return _yeni(kayit, _ekle(_cs(kayit), max(2, i - 1), yeni)), f"özelliğe aykırı: {yeni!r}", [max(2, i - 1) + 1]


def k_yer_aykiri(kayit, tohum, bg, rng):
    yeni = YER_AYKIRI.get(kayit["yer"])
    if not yeni:
        return None
    return _yeni(kayit, _ekle(_cs(kayit), 2, yeni)), f"yer tarifine aykırı: {yeni!r}", [3]


def k_yetenek_esya(kayit, tohum, bg, rng):
    d = _dunya(kayit, bg)
    tur = "hayvan" if any(t in bg.canli for t in d.tur) else "insan"
    yeni = rng.choice(YETENEK[tur]).format(ad=d.ad)
    i = _cozum_cumlesi(kayit, bg) or 3
    return _yeni(kayit, _ekle(_cs(kayit), i, yeni)), f"kartta olmayan yetenek/eşya: {yeni!r}", [i + 1]


def k_tehlike(kayit, tohum, bg, rng):
    d = _dunya(kayit, bg)
    ic = kayit["yer"] in ("ev", "şato")
    grup = rng.choice(["ev" if kayit["yer"] == "ev" else "dis", "korku_ic" if ic else "korku_dis", "kalip"])
    yeni = rng.choice(TEHLIKE[grup]).format(ad=d.ad)
    cs = _cs(kayit)
    i = min(3, len(cs) - 1)
    return _yeni(kayit, _ekle(cs, i, yeni)), f"taklit edilir tehlike / korku / kalıp yargı: {yeni!r}", [i + 1]


# ---------------------------------------------------------------- biçimsel (yalnız birim testi)

def b_kesme_eki(kayit, tohum, bg, rng):
    d = _dunya(kayit, bg)
    cs = _cs(kayit)
    for i, c in enumerate(cs):
        m = re.search(rf"(?<![{H}]){re.escape(d.ad)}'([{kapi.HARF}]+)", c)
        if m:
            ek = m.group(1)
            j = next((k for k, ch in enumerate(ek) if ch in UNLU), None)
            if j is None:
                continue
            ters = {"a": "e", "e": "a", "ı": "i", "i": "ı", "u": "ü", "ü": "u", "o": "ö", "ö": "o"}
            yeni_ek = ek[:j] + ters[ek[j]] + ek[j + 1:]
            yeni = c[:m.start(1)] + yeni_ek + c[m.end(1):]
            return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"kesme eki uyumsuz: {d.ad}'{yeni_ek}", [i + 1]
    return None


def b_sertlesme(kayit, tohum, bg, rng):
    cs = _cs(kayit)
    for i, c in enumerate(cs):
        for m in re.finditer(rf"(?<![{H}])([{kapi.HARF}]*[{SERT}])t([ıiuü])(?![{H}])", c):
            if bg.kok(m.group(0)).endswith("-"):
                yeni = c[:m.start()] + m.group(1) + "d" + m.group(2) + c[m.end():]
                return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"sertleşme: {m.group(1)}d{m.group(2)}", [i + 1]
    return None


def _anlatim_yuklemi(kayit, bg):
    """Tırnaksız bir cümlenin sonundaki yalın -dı'lı fiil (bekledi, koştu; -yordu, -mıştı, -ardı değil)."""
    cs = _cs(kayit)
    for i, c in enumerate(cs[1:], 1):
        if not _anlatim(c):
            continue
        m = re.search(rf"([{kapi.HARF}]+)([.!?]+)$", c)
        g = gecmis_govde(m.group(1)) if m else None
        if g and bg.kok(m.group(1)).endswith("-") and not re.search(r"(?:l[ae]r|yor|m[ıiuü]ş|[ae]c[ae]k|r)$", g):
            return cs, i, m
    return None


def b_yalin_yor(kayit, tohum, bg, rng):
    r = _anlatim_yuklemi(kayit, bg)
    if not r:
        return None
    cs, i, m = r
    w = yor_bicimi(gecmis_govde(m.group(1)))
    yeni = cs[i][:m.start(1)] + w + cs[i][m.end(1):]
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"tırnak dışı yalın -yor: {w}", [i + 1]


def b_yalin_mis(kayit, tohum, bg, rng):
    r = _anlatim_yuklemi(kayit, bg)
    if not r:
        return None
    cs, i, m = r
    w = mis_bicimi(gecmis_govde(m.group(1)))
    yeni = cs[i][:m.start(1)] + w + cs[i][m.end(1):]
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), f"tırnak dışı yalın -mış: {w}", [i + 1]


def b_sapka(kayit, tohum, bg, rng):
    r = _anlatim_yuklemi(kayit, bg)
    if not r:
        return None
    cs, i, m = r
    yeni = cs[i][:m.start(1)] + "hâlâ " + cs[i][m.start(1):]
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), "şapka: hâlâ", [i + 1]


def _ekle_ortaya(kayit, cumle):
    cs = _cs(kayit)
    return _yeni(kayit, _ekle(cs, min(3, len(cs) - 1), cumle))


def b_baska_figur(kayit, tohum, bg, rng):
    aday = [f for f in bg.figurler if f != kayit["figur"] and not bg.yaygin(f)]
    f = rng.choice(aday)
    return _ekle_ortaya(kayit, f"Sonra {f} de oraya geldi."), f"başka ürün figürü: {f}", None


def b_tohum_disi_yan(kayit, tohum, bg, rng):
    d = _dunya(kayit, bg)
    aday = [y for y in d.yanlar if y not in kayit["yan"]]
    if not aday:
        return None
    y = rng.choice(aday)
    ad = y if y[:1].isupper() else f"bir {d.yanlar[y]['yuzey_bicimleri'][0]}" if d.yanlar[y]["tip"] == "isimsiz" else y
    return _ekle_ortaya(kayit, f"Sonra {ad} {de_da(ad)} oraya geldi."), f"tohumda olmayan yan: {y}", None


def b_kart_disi_canli(kayit, tohum, bg, rng):
    izin = kapi._canli_izin(_dunya(kayit, bg), kayit["yan"], bg)
    hayvan = next(h for h in ("keçi", "kuzu", "tilki") if h not in izin)
    return _ekle_ortaya(kayit, f"Sonra bir {hayvan} de oraya geldi."), f"kart dışı canlı: {hayvan}", None


def b_ertesi_sabah(kayit, tohum, bg, rng):
    cs = _cs(kayit)
    i = next((j for j in range(2, len(cs) - 1) if _anlatim(cs[j])), None)
    if i is None:
        return None
    yeni = "Ertesi sabah " + _kucuk_bas(cs[i], bg)
    return _yeni(kayit, cs[:i] + [yeni] + cs[i + 1:]), "zaman atlaması: ertesi sabah", [i + 1]


def b_hastaydi(kayit, tohum, bg, rng):
    return _ekle_ortaya(kayit, f"O gün {_dunya(kayit, bg).ad} biraz hastaydı."), "hastalık: hastaydı", None


ISLEM = {"cozum_sil": m_cozum_sil, "sacma_sebep": m_sacma_sebep, "celiski": m_celiski, "cozum_yana": m_cozum_yana,
         "ikinci_sorun": m_ikinci_sorun, "sebepsiz_nesne": m_sebepsiz_nesne, "tamlama": d_tamlama,
         "ozne_fiil": d_ozne_fiil, "konusan": d_konusan, "zamir": d_zamir, "kendi_kendine": d_kendi_kendine,
         "iliski": k_iliski, "ozellik_aykiri": k_ozellik_aykiri, "yer_aykiri": k_yer_aykiri,
         "yetenek_esya": k_yetenek_esya, "tehlike": k_tehlike,
         "kesme_eki": b_kesme_eki, "sertlesme": b_sertlesme, "yalin_yor": b_yalin_yor, "yalin_mis": b_yalin_mis,
         "sapka": b_sapka, "baska_figur": b_baska_figur, "tohum_disi_yan": b_tohum_disi_yan,
         "kart_disi_canli": b_kart_disi_canli, "ertesi_sabah": b_ertesi_sabah, "hastaydi": b_hastaydi}


# ---------------------------------------------------------------- ana giriş

def uygula(kayit, tohum, tur, bg, rng):
    """(yeni kayıt, açıklama, değişen cümle no'ları) ya da None (tür bu tabana uygulanamıyor)."""
    return ISLEM[tur](kayit, tohum, bg, rng)


def denetle(kayit, tohum, bg, degisim=None, taslak_kart=False):
    return kapi.denetle({**kayit, "degisim": degisim}, tohum, bg, taslak_kart=taslak_kart)


def kanarya(taban, tohum, lens, bg, rng, tur=None, degisim=None, taslak_kart=False, atilan=None):
    """taban: kanonik kayıt (koddan geçmiş, kabul ya da altın). Merceğin türleri karışık sırayla denenir; kodun
    yakaladığı aday atılır (atilan listesine (tür, ihlal kodları) yazılır). Kanarya kaydı ya da None döner."""
    turler = [tur] if tur else rng.sample(TURLER[lens], len(TURLER[lens]))
    for t in turler:
        r = uygula(taban, tohum, t, bg, rng)
        if r is None:
            continue
        aday, aciklama, cumle_no = r
        if aday["govde"] == taban["govde"]:
            continue
        s = denetle(aday, tohum, bg, degisim, taslak_kart)
        if not s["gecti"]:
            if atilan is not None:
                atilan.append((t, sorted({x["kod"] for x in s["ihlaller"]})))
            continue
        return {"kimlik": s["kimlik"], "ad_alani": "kanarya", "sha1": s["sha1"], "lens": lens, "tur": t,
                "aciklama": aciklama, "degisen_cumle": cumle_no, "taban": uk.kimlik(taban),
                "taban_sha1": uk.sha1(taban), "tohum": (tohum or {}).get("id"), "degisim": degisim, "kayit": aday,
                "kapi": {"gecti": True, "surum": s["surum"], "notlar": s["notlar"],
                         "taslak_kart": s["taslak_kart"]}}
    return None


def bicimsel(taban, tohum, tur, bg, rng, degisim=None, taslak_kart=False):
    """Biçimsel kusur (birim testi): (aday kayıt, açıklama, beklenen kod(lar), kapı sonucu) ya da None."""
    r = uygula(taban, tohum, tur, bg, rng)
    if r is None:
        return None
    aday, aciklama, _ = r
    return aday, aciklama, BICIMSEL[tur], denetle(aday, tohum, bg, degisim, taslak_kart)


def _tabanlar(yol, tohum_yolu):
    tohumlar = kapi.tohum_oku(tohum_yolu)
    with open(yol, encoding="utf-8") as f:
        return [(uk.kayit(b), tohumlar.get(b["tohum"]), b["degisim"]) for b in uk.ayristir(f.read())]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    alt = ap.add_subparsers(dest="komut", required=True)
    u = alt.add_parser("uret")
    b = alt.add_parser("bicimsel")
    for p in (u, b):
        p.add_argument("dosya")
        p.add_argument("--tohum", required=True)
        p.add_argument("--taslak-kart", action="store_true")
        p.add_argument("--tohum-sayi", type=int, default=2026)
    u.add_argument("--lens", required=True, choices=sorted(TURLER))
    u.add_argument("--tur", default=None)
    u.add_argument("--cikti", default=None, help="kanarya JSONL (ayrı ad alanı; eğitim klasörüne yazılmaz)")
    a = ap.parse_args()
    bg = kapi.Baglam()
    rng = random.Random(a.tohum_sayi)
    tabanlar = _tabanlar(a.dosya, a.tohum)
    if a.komut == "bicimsel":
        yakalanan = toplam = 0
        for kayit, tohum, deg in tabanlar:
            if not denetle(kayit, tohum, bg, deg, a.taslak_kart)["gecti"]:
                print(f"taban kapıdan geçmiyor, atlandı: {uk.kimlik(kayit)}")
                continue
            for t in BICIMSEL:
                r = bicimsel(kayit, tohum, t, bg, rng, deg, a.taslak_kart)
                if r is None:
                    print(f"  {uk.kimlik(kayit)} {t}: uygulanamadı")
                    continue
                _, ac, bek, s = r
                kodlar = {x["kod"] for x in s["ihlaller"]}
                ok = bool(kodlar & ({bek} if isinstance(bek, str) else set(bek)))
                toplam += 1
                yakalanan += ok
                print(f"  {uk.kimlik(kayit)} {t}: {'YAKALANDI' if ok else 'KAÇTI'} ({ac}; {sorted(kodlar)})")
        print(f"biçimsel: {yakalanan}/{toplam} beklenen kapıda yakalandı")
        return 0 if toplam and yakalanan == toplam else 1
    out = open(a.cikti, "a", encoding="utf-8") if a.cikti else sys.stdout
    for kayit, tohum, deg in tabanlar:
        atilan = []
        k = kanarya(kayit, tohum, a.lens, bg, rng, a.tur, deg, a.taslak_kart, atilan)
        for t, kodlar in atilan:
            print(f"atıldı (kod yakaladı): {uk.kimlik(kayit)} {t} {kodlar}", file=sys.stderr)
        if k:
            out.write(json.dumps(k, ensure_ascii=False) + "\n")
        else:
            print(f"kanarya üretilemedi: {uk.kimlik(kayit)} ({a.lens})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
