#!/usr/bin/env python3
"""E3 plan etiketlerini denetler. Kurallar: data/oyuncak_plan/KILAVUZ.md.

Kullanım:
    python data/oyuncak_plan/kontrol.py <etiketler.jsonl> [--ozet] [--veri web/veri.json]

Her satır web/veri.json'daki hikâyesine karşı denetlenir.
  HATA  : kural kesin çiğnenmiş; satır reddedilir, ajana geri gider.
  UYARI : kesin olmayan şüphe (ör. zaman eki tanınmadı); satır geçer ama gözden geçirilmeli.
Varsayılan çıktı satır satır HATA/UYARI listesi + kısa özet. --ozet: satır listesi yerine yalnızca özet,
dağılımlar ve bozuk hikâyelerin listesi. Herhangi bir HATA varsa çıkış kodu 1, yoksa 0.

Konum kuralı başka araçlarda da buradan kullanılmalı (olay.py plan_uyum_%, sec.py plan_cezasi):
    from kontrol import plan_uyumu   # plan_uyumu(metin, anahtar_sorun, anahtar_cozum) -> (sorun_ok, cozum_ok)
"""
import argparse
import collections
import json
import os
import re
import signal
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
VERI = os.path.join(ROOT, "web", "veri.json")

sys.dont_write_bytecode = True  # depoya __pycache__ bırakma
sys.path.insert(0, ROOT)
from baslangic import KAR, YABANCI  # noqa: E402

ALANLAR = ("id", "sorun", "cozum", "anahtar_sorun", "anahtar_cozum", "yardimci", "yok", "bozuk", "bozuk_neden")
PLAN_ALANLARI = ("sorun", "cozum", "anahtar_sorun", "anahtar_cozum")
EN_AZ_KELIME, EN_COK_KELIME = 3, 9
KOK_UZ = 5            # anahtar eşleşmesi: ilk 5 harf
SIK_ESIK = 0.30       # kökü hikâyelerin bu oranından fazlasında geçen anahtar ayırt edici değil (UYARI)
NEDEN_EN_COK = 25     # bozuk_neden en fazla bu kadar kelime


def kucuk(s):
    """degerlendirme/sec.py:kucuk ile aynı Türkçe küçük harf (I->ı, İ->i, sonra lower). sec.py içe aktarılmıyor:
    o modül sözlük ve seçici bağımlılıklarını yükler."""
    return s.replace("I", "ı").replace("İ", "i").lower()


HARF = "a-zçğıöşüâîû"
KELIME = re.compile(rf"[{HARF}]+")
TEK_KELIME = re.compile(rf"^[{HARF}]+$")
PLAN_BICIM = re.compile(rf"^[{HARF}]+(?:,? [{HARF}]+)*$")          # küçük harf, tek boşluk, virgül yalnızca kelime sonunda
YARDIMCI_BICIM = re.compile(rf"^[{HARF}]+(?: [{HARF}]+){{0,3}}$")  # 1–4 kelime


def kelimeler(metin):
    """Konum ölçüsünün kelime listesi (sec.py ile aynı bölme): küçük harf, [a-zçğıöşüâîû]+ parçaları.
    "Pamuk'un" -> "pamuk", "un"."""
    return KELIME.findall(kucuk(metin))


def kok(kelime):
    return kucuk(kelime)[:KOK_UZ]


def konumlar(ws, anahtar):
    """anahtar kökünün (ilk 5 harf; kısa kelimede kelimenin tamamı) önek olarak geçtiği kelime sıraları."""
    k = kok(anahtar)
    return [i for i, w in enumerate(ws) if w.startswith(k)]


def ilk60(i, n):
    return 10 * i < 6 * n


def son60(i, n):
    return 10 * i >= 4 * n


def plan_uyumu(metin, anahtar_sorun, anahtar_cozum):
    """(sorun_ok, cozum_ok).
    sorun_ok: anahtar_sorun kökünün İLK geçişi metnin ilk %60'ında (kelime sırası i, 10*i < 6*N).
    cozum_ok: anahtar_cozum kökü, anahtar_sorun'un ilk geçişinden SONRA ve son %60'ta (10*i >= 4*N) en az bir
    kez geçiyor. anahtar_sorun kökü metinde hiç yoksa yalnızca son %60 şartı aranır."""
    ws = kelimeler(metin)
    n = len(ws)
    s = konumlar(ws, anahtar_sorun)
    s0 = s[0] if s else -1
    sorun_ok = bool(s) and ilk60(s0, n)
    cozum_ok = any(i > s0 and son60(i, n) for i in konumlar(ws, anahtar_cozum))
    return sorun_ok, cozum_ok


# --- yasak kelimeler -----------------------------------------------------------------------------------------
# Ad çekim ekleri (küçültme, çoğul, iyelik, hâl). "kız" + ek: kızı, kıza, kızlar, kızcağız; ama kızdı, kızak,
# kızgın, kızıl eşleşmez. "ayı" + ek: ayıyı, ayının; ama ayın, ayıp eşleşmez.
EK = (r"(?:[cç][ıiuü][kğ]|c[ae]ğ[ıi]z)?"                     # küçültme: kedicik, ayıcığı, kızcağız
      r"(?:l[ae]r)?"
      r"(?:[ıiuü]m|[ıiuü]n|s?[ıiuü]|l[ae]r[ıi]|[ıiuü]?m[ıiuü]z|[ıiuü]?n[ıiuü]z)?"
      r"(?:y?[ıiuü]|y?[ae]|n[ıiuü]|n[ae]|[dt][ae]|nd[ae]|[dt][ae]n|nd[ae]n|n?[ıiuü]n|y?l[ae]|ki)?")


def _tur_kalibi(tur):
    govdeler = [tur] + ([tur[:-1] + "ğ"] if tur.endswith("k") else [])   # köpek -> köpeğe, köpeği
    return re.compile(rf"^(?:{'|'.join(govdeler)}){EK}$")


TURLER = {k["tur"]: _tur_kalibi(k["tur"]) for k in KAR.values()}
ISIM_KIMLIK = {kucuk(k["isim"]): k["kimlik"] for k in KAR.values()}
TUR_KIMLIK = {k["tur"]: k["kimlik"] for k in KAR.values()}
# Türkçede sıradan kelime olan figür adları: bal (yiyecek), can (canı sıkıldı), alev, pamuk, kızıl (renk).
BELIRSIZ = {"bal", "can", "alev", "pamuk", "kızıl"}
KESIN_ISIM = [i for i in ISIM_KIMLIK if i not in BELIRSIZ]
BELIRSIZ_KALIP = {i: re.compile(rf"^{i}{EK}$") for i in BELIRSIZ}
YABANCI_K = {kucuk(y) for y in YABANCI}

# Anahtar olamayacak kelimeler: işlev kelimeleri, konuşma fiilleri, hafif fiiller, mutlu son kelimeleri.
DURAK = {"bir", "ve", "ile", "çok", "daha", "en", "gün", "dedi", "diye", "sordu", "sonra", "ama", "çünkü", "için",
         "gibi", "kadar", "hep", "her", "bu", "şu", "o", "onu", "ona", "onun", "ne", "de", "da", "ki", "mi", "mı",
         "mu", "mü", "hem", "ya", "iki", "hemen", "sonunda", "artık", "oldu", "oldular", "olmuştu", "etti",
         "ettiler", "yaptı", "vardı", "yoktu", "adında"}
DURAK_KOK = {"birli", "ikisi", "mutlu", "sevin", "yaşar"}   # birlikte, ikisi, mutlu, sevindi, yaşardı

# Zaman: son kelime -dı/-di/-du/-dü/-tı/-ti/-tu/-tü (+lar/ler) ile bitmeli (gitti, buldular, yoktu, kaybolmuştu).
GECMIS = re.compile(r"[dt][ıiuü](?:l[ae]r)?$")
# Kesin geçmiş-dışı sonlar: -yor, -acak/-ecek, -mış, -malı, -dır, mastar -mak/-mek. Bunlar HATA; tanınmayan diğer
# sonlar (ör. -ar/-ır, ek almamış ad) UYARI: ad cümlesi olabilir, gözle bakılır.
GECMIS_DEGIL = re.compile(r"(?:yor(?:l[ae]r)?|[ae]c[ae]k(?:l[ae]r)?|m[ıiuü]ş(?:l[ae]r)?|m[ae]l[ıi](?:l[ae]r)?"
                          r"|[dt][ıiuü]r(?:l[ae]r)?|m[ae]k)$")
MUTLU_KOK = {"mutlu", "sevin"}
MUTLU_UYARI_KOK = {"mutlu", "sevin", "eğlen", "güldü", "gülüm", "teşek", "sarıl"}


class Denetim:
    def __init__(self):
        self.hatalar = []    # (kod, mesaj)
        self.uyarilar = []

    def hata(self, kod, mesaj):
        self.hatalar.append((kod, mesaj))

    def uyari(self, kod, mesaj):
        self.uyarilar.append((kod, mesaj))


def orijinal_kucuk_kelimeler(metin):
    """Metinde küçük harfle başlayan (yani özel ad olmayan) kelimeler: "Bal'ın balı" -> {"balı", ...}."""
    return {kucuk(w) for w in re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşüâîû]+", metin) if w[0] == kucuk(w[0])}


def yasak_kelime(d, alan, w, hikaye, buyuk=False):
    """Figür türü, figür adı, yabancı ad denetimi. w: küçük harfli tek kelime; buyuk: metinde büyük harfle mi yazılmış."""
    for tur, kalip in TURLER.items():
        if kalip.match(w):
            d.hata("tur", f"{alan}: '{w}' figür türü ('{tur}'); özneyi düşür, 'ikisi' ya da başka bir ad kullan")
            return
    for isim in KESIN_ISIM:
        if w.startswith(isim):
            d.hata("isim", f"{alan}: '{w}' figür adı")
            return
    for isim, kalip in BELIRSIZ_KALIP.items():
        if kalip.match(w):
            if buyuk:
                d.hata("isim", f"{alan}: '{w}' figür adı")
                return
            if ISIM_KIMLIK[isim] not in hikaye["k"] or w in hikaye["_kucuk"]:
                continue
            if w == isim and not any(k.startswith(isim) for k in hikaye["_kucuk"]):
                # figür hikâyede var ve kelime hikâyede hiç sıradan kelime olarak geçmiyor: çıplak ad
                d.hata("isim", f"{alan}: '{w}' figür adı")
                return
            d.uyari("isim_belirsiz", f"{alan}: '{w}' figür adı olabilir (hikâyede küçük harfle '{w}' geçmiyor)")
    if w in YABANCI_K:
        (d.hata if buyuk else d.uyari)("yabanci_isim", f"{alan}: '{w}' bir özel ad olabilir")


def plan_cumlesi(d, alan, deger, hikaye):
    """sorun/cozum cümlesini denetler; küçük harfli, yalnızca harflerden oluşan kelime listesini döndürür."""
    temiz = deger
    if re.search(r"[|\n\r]", deger):
        d.hata("cizgi_satir", f"{alan}: '|' ya da satır sonu içeriyor")
        temiz = re.sub(r"\s*[|\n\r]+\s*", " ", deger).strip()
    if temiz != kucuk(temiz):
        d.hata("buyuk_harf", f"{alan}: büyük harf var (özel ad ya da cümle başı): {deger!r}")
    yabanci_karakter = sorted(set(re.sub(rf"[{HARF} ,A-ZÇĞİÖŞÜ]", "", temiz)))
    if yabanci_karakter:
        d.hata("isaret", f"{alan}: izin verilmeyen karakter {''.join(yabanci_karakter)!r} (yalnızca harf, boşluk, virgül)")
    elif not PLAN_BICIM.match(kucuk(temiz)):
        d.hata("bicim", f"{alan}: boşluk/virgül biçimi bozuk (baş-son boşluk, çift boşluk ya da sonda virgül): {deger!r}")
    n = len(temiz.split())
    if not EN_AZ_KELIME <= n <= EN_COK_KELIME:
        d.hata("kelime_sayisi", f"{alan}: {n} kelime ({EN_AZ_KELIME}–{EN_COK_KELIME} olmalı)")
    orj = re.findall(r"[A-Za-zÇĞİÖŞÜçğıöşüâîû]+", temiz)
    ws = [kucuk(w) for w in orj]
    for o, w in zip(orj, ws):
        yasak_kelime(d, alan, w, hikaye, buyuk=o[0] != kucuk(o[0]))
    if ws:
        son = ws[-1]
        if GECMIS.search(son) and len(son) >= 3:
            pass
        elif GECMIS_DEGIL.search(son):
            d.hata("zaman", f"{alan}: son kelime '{son}' -dı'lı geçmiş zaman değil")
        else:
            d.uyari("zaman_belirsiz", f"{alan}: son kelime '{son}' -dı/-tı ile bitmiyor; ad cümlesi mi?")
    return ws


def anahtar_denetle(d, alan, anahtar, cumle_ws, hikaye, df):
    if not TEK_KELIME.match(anahtar):
        d.hata("anahtar_bicim", f"{alan}: '{anahtar}' tek kelime, küçük harf ve yalnızca harf olmalı")
        return False
    ok = True
    if len(anahtar) < 3:
        d.hata("anahtar_bicim", f"{alan}: '{anahtar}' çok kısa (en az 3 harf)")
        ok = False
    if anahtar in DURAK or kok(anahtar) in DURAK_KOK:
        d.hata("anahtar_durak", f"{alan}: '{anahtar}' sorunu/çözümü taşımayan genel bir kelime")
        ok = False
    n_hata = len(d.hatalar)
    yasak_kelime(d, alan, anahtar, hikaye)
    ok = ok and len(d.hatalar) == n_hata
    if anahtar not in hikaye["_kelime_kume"]:
        d.hata("anahtar_metinde_yok", f"{alan}: '{anahtar}' hikâyede bu biçimiyle geçmiyor (metindeki kelimeyi aynen yaz)")
        ok = False
    if cumle_ws is not None and not any(w.startswith(kok(anahtar)) for w in cumle_ws):
        cumle = alan.replace("anahtar_", "")
        d.hata("anahtar_cumlede_yok", f"{alan}: '{anahtar}' kökü ({kok(anahtar)}) {cumle} cümlesinde geçmiyor")
    if len(anahtar) < 4:
        d.uyari("anahtar_kisa", f"{alan}: '{anahtar}' kısa; kökü ilgisiz kelimelerle de eşleşebilir")
    oran = df.get(kok(anahtar), 0) / max(1, df["_n"])
    if oran > SIK_ESIK:
        d.uyari("anahtar_sik", f"{alan}: '{anahtar}' kökü çok yaygın (hikâyelerde oran %{100 * oran:.0f}); daha özgül bir kelime seç")
    return ok


def konum_denetle(d, hikaye, a_sorun, a_cozum):
    ws = hikaye["_kelimeler"]
    n = len(ws)
    s = konumlar(ws, a_sorun)
    c = konumlar(ws, a_cozum)
    if not s:
        return
    s0 = s[0]
    if not ilk60(s0, n):
        d.hata("konum_sorun", f"anahtar_sorun '{a_sorun}' ilk geçişi metnin %{100 * s0 / n:.1f} noktasında (ilk %60'ta olmalı)")
    uygun = [i for i in c if i > s0 and son60(i, n)]
    if not uygun:
        yerler = ", ".join(f"%{100 * i / n:.1f}" for i in c) or "yok"
        d.hata("konum_cozum", f"anahtar_cozum '{a_cozum}' anahtar_sorun'dan (%{100 * s0 / n:.1f}) sonra ve son %60'ta "
                              f"geçmiyor (geçtiği yerler: {yerler})")


def denetle(kayit, hikaye, df):
    d = Denetim()
    eksik = [a for a in ALANLAR if a not in kayit]
    fazla = [a for a in kayit if a not in ALANLAR]
    if eksik:
        d.hata("alan", f"eksik alan: {', '.join(eksik)}")
    if fazla:
        d.hata("alan", f"fazla alan: {', '.join(fazla)}")
    g = {a: kayit.get(a) for a in ALANLAR}

    for a in ("yok", "bozuk"):
        if not isinstance(g[a], bool):
            d.hata("tip", f"{a} true/false olmalı, {g[a]!r} yazılmış")
    for a in PLAN_ALANLARI + ("yardimci", "bozuk_neden"):
        if g[a] is not None and not isinstance(g[a], str):
            d.hata("tip", f"{a} metin ya da null olmalı")
            g[a] = None
        elif isinstance(g[a], str) and not g[a].strip():
            d.hata("tip", f"{a} boş metin; değer yoksa null yaz")
            g[a] = None

    # yok tutarlılığı
    if g["yok"] is True:
        dolu = [a for a in PLAN_ALANLARI if g[a] is not None]
        if dolu:
            d.hata("yok_tutarsiz", f"yok=true ama dolu: {', '.join(dolu)} (hepsi null olmalı)")
    elif g["yok"] is False:
        bos = [a for a in PLAN_ALANLARI if g[a] is None]
        if bos:
            d.hata("yok_tutarsiz", f"yok=false ama boş: {', '.join(bos)}")

    # bozuk tutarlılığı
    if g["bozuk"] is True and g["bozuk_neden"] is None:
        d.hata("bozuk_tutarsiz", "bozuk=true ama bozuk_neden yok")
    if g["bozuk"] is False and g["bozuk_neden"] is not None:
        d.hata("bozuk_tutarsiz", "bozuk=false ama bozuk_neden dolu (null olmalı)")
    if g["bozuk_neden"] is not None:
        if "\n" in g["bozuk_neden"] or "|" in g["bozuk_neden"]:
            d.hata("neden_bicim", "bozuk_neden '|' ya da satır sonu içeriyor")
        if len(g["bozuk_neden"].split()) > NEDEN_EN_COK:
            d.hata("neden_bicim", f"bozuk_neden {len(g['bozuk_neden'].split())} kelime (en fazla {NEDEN_EN_COK})")

    if hikaye is None:
        return d

    # sorun / cozum
    cumle = {}
    for a in ("sorun", "cozum"):
        if g[a] is not None:
            cumle[a] = plan_cumlesi(d, a, g[a], hikaye)
    if g["sorun"] is not None and g["cozum"] is not None and kucuk(g["sorun"]).strip() == kucuk(g["cozum"]).strip():
        d.hata("ayni_cumle", "sorun ve cozum aynı")
    if "cozum" in cumle and cumle["cozum"]:
        cws = cumle["cozum"]
        if kok(cws[-1]) in MUTLU_KOK or re.search(r"\bmutlu ol", kucuk(g["cozum"])):
            d.hata("mutlu_son", "cozum mutlu sonu anlatıyor; sorunu çözen eylemi yaz")
        elif any(kok(w) in MUTLU_UYARI_KOK for w in cws):
            d.uyari("mutlu_kelime", "cozum mutlu son/teşekkür kelimesi içeriyor; sorunu çözen eylem mi?")

    # anahtarlar
    a_ok = {}
    for a, c in (("anahtar_sorun", "sorun"), ("anahtar_cozum", "cozum")):
        if g[a] is not None:
            a_ok[a] = anahtar_denetle(d, a, g[a], cumle.get(c), hikaye, df)
    if g["anahtar_sorun"] is not None and g["anahtar_cozum"] is not None:
        k1, k2 = kok(g["anahtar_sorun"]), kok(g["anahtar_cozum"])
        if k1.startswith(k2) or k2.startswith(k1):
            d.hata("anahtar_ayni", f"anahtar_sorun ve anahtar_cozum aynı kökten ({k1}/{k2})")
        elif a_ok.get("anahtar_sorun") and a_ok.get("anahtar_cozum"):
            konum_denetle(d, hikaye, g["anahtar_sorun"], g["anahtar_cozum"])

    # yardimci
    y = g["yardimci"]
    if y is not None:
        if not YARDIMCI_BICIM.match(y):
            d.hata("yardimci_bicim", f"yardimci: {y!r} 1–4 küçük harfli kelime olmalı (özel ad yok)")
        else:
            yws = y.split()
            if "bir" in yws:
                d.hata("yardimci_bicim", "yardimci: 'bir' yazma ('küçük bir yengeç' -> 'küçük yengeç')")
            for w in yws:
                belirsiz_ad = w in BELIRSIZ and ISIM_KIMLIK[w] in hikaye["k"] and w not in hikaye["_kucuk"]
                if any(w.startswith(i) for i in KESIN_ISIM) or belirsiz_ad:
                    d.hata("yardimci_figur", f"yardimci: '{w}' figür adı; figürler yardımcı değildir")
            bas = yws[-1]
            for tur, kalip in TURLER.items():
                if kalip.match(bas) and TUR_KIMLIK[tur] in hikaye["k"]:
                    d.hata("yardimci_figur", f"yardimci: '{bas}' hikâyenin kendi figürünün türü")
            if bas not in hikaye["_kelime_kume"]:
                d.hata("yardimci_metinde_yok", f"yardimci: '{bas}' hikâyede bu biçimiyle geçmiyor")
            eksik_y = [w for w in yws[:-1] if w != "bir" and w not in hikaye["_kelime_kume"]]
            if eksik_y:
                d.uyari("yardimci_metinde_yok", f"yardimci: {', '.join(eksik_y)} hikâyede geçmiyor")
    return d


def veri_yukle(yol):
    hikayeler = {}
    for h in json.load(open(yol, encoding="utf-8")):
        ws = kelimeler(h["m"])
        h["_kelimeler"] = ws
        h["_kelime_kume"] = set(ws)
        h["_kucuk"] = orijinal_kucuk_kelimeler(h["m"])
        hikayeler[h["id"]] = h
    df = collections.Counter()
    for h in hikayeler.values():
        df.update({w[:L] for w in h["_kelime_kume"] for L in range(3, KOK_UZ + 1) if len(w) >= L})
    df["_n"] = len(hikayeler)
    return hikayeler, df


def main():
    ap = argparse.ArgumentParser(description="E3 plan etiketlerini (JSONL) web/veri.json'a karşı denetler.")
    ap.add_argument("etiketler", help="her satırı bir JSON kaydı olan etiket dosyası")
    ap.add_argument("--ozet", action="store_true", help="satır satır liste yerine yalnızca özet ve dağılımlar")
    ap.add_argument("--veri", default=VERI, help="hikâye verisi (varsayılan web/veri.json)")
    arg = ap.parse_args()
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)   # "| head" ile kesilince iz yığını basma

    hikayeler, df = veri_yukle(arg.veri)
    hata_say, uyari_say = collections.Counter(), collections.Counter()
    goruldu = {}
    kayitlar = []
    hatali_satir = satir_sayisi = 0
    cikti = []

    with open(arg.etiketler, encoding="utf-8-sig") as f:
        for no, satir in enumerate(f, 1):
            if not satir.strip():
                continue
            satir_sayisi += 1
            d = Denetim()
            kid = "?"
            try:
                kayit = json.loads(satir)
                if not isinstance(kayit, dict):
                    raise ValueError("satır bir JSON nesnesi değil")
            except ValueError as e:
                d.hata("json", f"JSON okunamadı: {e}")
                kayit = None
            if kayit is not None:
                kid = kayit.get("id", "?")
                hikaye = None
                if not isinstance(kid, str):
                    d.hata("id", f"id metin olmalı: {kid!r}")
                elif kid not in hikayeler:
                    d.hata("id", f"id web/veri.json'da yok: {kid}")
                else:
                    hikaye = hikayeler[kid]
                    if kid in goruldu:
                        d.hata("id_tekrar", f"id {goruldu[kid]}. satırda da var")
                    else:
                        goruldu[kid] = no
                sonuc = denetle(kayit, hikaye, df)
                d.hatalar += sonuc.hatalar
                d.uyarilar += sonuc.uyarilar
                if not d.hatalar:
                    kayitlar.append(kayit)
            for kod, _ in d.hatalar:
                hata_say[kod] += 1
            for kod, _ in d.uyarilar:
                uyari_say[kod] += 1
            if d.hatalar:
                hatali_satir += 1
            for tur, liste in (("HATA", d.hatalar), ("UYARI", d.uyarilar)):
                for kod, mesaj in liste:
                    cikti.append(f"satır {no} [{kid}] {tur} {kod}: {mesaj}")

    if not arg.ozet:
        for c in cikti:
            print(c)
        if cikti:
            print()

    n_gecerli = len(kayitlar)
    yok = sum(k["yok"] is True for k in kayitlar)
    bozuk = [k for k in kayitlar if k["bozuk"] is True]
    yardimci = sum(k["yardimci"] is not None for k in kayitlar)
    kume = collections.Counter(i.split("/")[0] for i in hikayeler)
    kapsam = collections.Counter(i.split("/")[0] for i in goruldu)
    yuzde = lambda a, b: f"%{100 * a / b:.1f}" if b else "%0"  # noqa: E731
    print(f"== özet: {arg.etiketler} ==")
    print(f"satır: {satir_sayisi} | geçerli: {n_gecerli} | hatalı satır: {hatali_satir} | "
          f"hata: {sum(hata_say.values())} | uyarı: {sum(uyari_say.values())}")
    print(f"geçerlilerde yok: {yok} ({yuzde(yok, n_gecerli)}) | bozuk: {len(bozuk)} ({yuzde(len(bozuk), n_gecerli)}) | "
          f"yardimci dolu: {yardimci}")
    print(f"kapsam: {len(goruldu)}/{len(hikayeler)} hikâye (" +
          ", ".join(f"{k} {kapsam[k]}/{kume[k]}" for k in sorted(kume)) + ")")
    if hata_say:
        print("hatalar: " + ", ".join(f"{k} {v}" for k, v in hata_say.most_common()))
    if uyari_say:
        print("uyarılar: " + ", ".join(f"{k} {v}" for k, v in uyari_say.most_common()))

    if arg.ozet and kayitlar:
        planli = [k for k in kayitlar if k["yok"] is False]
        for a in ("sorun", "cozum"):
            say = collections.Counter(len(k[a].split()) for k in planli)
            print(f"{a} kelime sayısı: " + " ".join(f"{n}:{say[n]}" for n in sorted(say)))
        for a in ("anahtar_sorun", "anahtar_cozum"):
            say = collections.Counter(kok(k[a]) for k in planli)
            print(f"en sık {a} kökleri: " + ", ".join(f"{w} {v}" for w, v in say.most_common(12)))
        uyum = sum(all(plan_uyumu(hikayeler[k["id"]]["m"], k["anahtar_sorun"], k["anahtar_cozum"])) for k in planli)
        print(f"plan_uyumu (geçerli planlı satırlarda): {uyum}/{len(planli)}")
        if bozuk:
            print("bozuk hikâyeler:")
            for k in bozuk:
                print(f"  {k['id']}: {k['bozuk_neden']}")

    sys.exit(1 if hata_say else 0)


if __name__ == "__main__":
    main()
