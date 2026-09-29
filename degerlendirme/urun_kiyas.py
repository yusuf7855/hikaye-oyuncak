"""Ürün modeli (c3ft_urun) ile eski tek figür modelinin (c3ft_tek) kör ikili kıyası için hikâye üret.

Kullanım: python degerlendirme/urun_kiyas.py --yeni hf_c3ft_urun --eski hf_c3ft_tek [--aday K] [--sadece-eski]
                                             [--istem-goster] [--yan dogrulama|bos]
  ardından: python degerlendirme/ikili.py hazirla urun_kiyas_yeni urun_kiyas_tek --parti 2 --hakem 1

Vakalar (urun_v2'deki 11 figür; yerler data/urun_kartlari.json 'yerler[].etiket' sırasıyla):
  ortak : eski modelin de eğitimde gördüğü figürler. Eski modelin bilgisi eğitim kaynağından çıkarılır:
          data/oyuncak_populer (kontrol.oku) eksi data/egitim_haric_tek.txt ve bolme.json (zincir_tek.sh ile aynı);
          bir figür için yer, hem ürün kartında hem eski eğitimde (>=1 hikâye) varsa kullanılır, kartın ilk 3'ü alınır.
          Yer adları iki modelde aynı sözcüklerdir (orman, dağ, ev, park, deniz, şato); eşleme özdeşliktir.
          Eski eğitimde hiç (figür, yer) çifti olmayan figür atlanır ve raporlanır.
  yeni  : eski modelin hiç görmediği figürler x kartın ilk 3 yeri; yalnız yeni model (mutlak rubrik için).
İstemler (ikisi de eğitim dizgisini üreten fonksiyonun kendisinden türetilir, elle yazılmaz):
  yeni : urun_kayit.dizgi(kayıt, plan=True, yan_alani=True)'nin '\\nSorun:'a kadarki öneki:
         'Karakter: Chase | Yer: dağ | Yan: Ryder\\nSorun:'  (yan boşsa ' | Yan: …' yok, eğitimdeki gibi).
         Yan: --yan dogrulama (varsayılan) -> o (figür, yer) için izin.txt'de 'dogrulama' işaretli (eğitimde
         görülmemiş) kaydın yan listesi (data/tr_c3ft_urun/.../dogrulama.json, yoksa kabul.jsonl + izin.txt);
         her (figür, yer) için tam bir doğrulama kaydı vardır. --yan bos -> Yan alanı yok.
  eski : prepare_ft2.baslik({'turler': [isim], 'yer': yer}, plan=...)'nin '\\nSorun:'a kadarki öneki:
         'Karakter: Chase | Yer: dağ\\nSorun:'  (popüler figürün başlıkta adı geçer; eski yol, --plan).
  Token'lar baslangic.prompt_idler'in yöntemiyle: önek + örnek devam (' top') birlikte kodlanır, yalnız öneke düşen
  token'lar alınır; başa <|endoftext|> (eot_on). Doğrulama: --istem-goster, gerçek bir kabul/eğitim hikâyesinin
  tam eğitim dizgisini de kodlayıp istem token'larının onun öneki olduğunu denetler (assert).
Örnekleme (iki modelde aynı; hf_c3ft_tek/ayar_adaylar_izgara_tek8.json'daki c3ft_tek ayarı): temp 0.5, rep 1.1,
  top_k 40, n 240, baslik plan (model planı kendisi yazar, gen -S Ċ), satir_yasak (gen -N), eot_on, pencere tum,
  gen -e EOT. Seed 1000·i+j (i vaka no, j aday no), iki modelde aynı. Yasaklı isimler (gen -b) vaka başına iki
  modelde aynı: baslangic'in 12 klasik figür adı + YABANCI, eksi figürün kartlarında (ürün kartı + eski popüler kart)
  ve yan listesinde geçen adlar (ör. Elsa'da Anna, Hayri'de Mert yasaklanmaz).
Seçim (--aday K, varsayılan 8 = izgara_tek8): K aday + degerlendirme/sec.py. sec.py klasik figür kataloğunu
  (baslangic.KAR) varsayar; popüler/ürün figürlerinde kimlik kuralları çalışsın diye figür süreç içinde geçici bir
  KAR girdisi olarak kaydedilir ve sec.cezalar'ın üç isim kuralı ('uydurma kelime', 'yanlış isim', 'uydurma
  karakter adı') aynı mantıkla, figürün izinli adları (kartlardaki büyük harfli kelimeler + yanlar) hariç tutularak
  yeniden hesaplanır (yoksa 'Niloya' sözlükte olmadığı için her geçişi uydurma kelime, Elsa'nın Anna'sı yanlış isim
  sayılırdı). Kalan kurallar, yer cezası ve 2·ort_logp sec.puanla ile aynı. Seçici iki modele aynı uygulanır.
  --aday 1: seçicisiz, tek örnek (seed 1000·i).
Çıktı (uret.py şeması; ikili.py yalnız 'metin'i hakeme verir, id iki kolda aynı tamsayı):
  degerlendirme/urun_kiyas_yeni/hikayeler.json        ortak vakalar, yeni model
  degerlendirme/urun_kiyas_tek/hikayeler.json         ortak vakalar, eski model
  degerlendirme/urun_kiyas_yeni_mutlak/hikayeler.json yeni vakalar, yeni model
  [{id, grup, figurler, yer, baslik, istem, yan, metin, token, plan, plan_bozuk, aday, puan}]  metin = yalnız
  gövde; yan = istemde verilen yan (eski modelde hep []); baslik iki kolda aynı 'Karakter: X | Yer: Y'.
  Her klasöre adaylar.json (bütün adaylar) ve ayar.json yazılır.
  --sadece-eski: yalnız eski modelle üretir (yeni model henüz yokken); yeni istemleri yine gösterilir.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, "web"))
from tokenizers import Tokenizer  # noqa: E402

import sec  # noqa: E402
import urun_kayit as uk  # noqa: E402
import uret  # noqa: E402
from baslangic import KAR, YABANCI, YER  # noqa: E402
from paketle import isim_idleri  # noqa: E402
from research.tinystories import prepare_ft2  # noqa: E402

FIGURLER = ["Niloya", "Maşa", "Pepee", "Keloğlan", "Doru", "Hayri", "Şakir", "Elsa", "Chase", "Örümcek Adam",
            "Hello Kitty"]
YER_SAYISI = 3
# c3ft_tek'in ayarı (hf_c3ft_tek/ayar_adaylar_izgara_tek8.json); aday sayısı --aday
AYAR = {"temp": 0.5, "rep": 1.1, "top_k": 40, "n": 240, "baslik": "plan", "pencere": "tum", "satir_yasak": True,
        "eot_on": True}
YER_KIMLIK = {y["ad"]: y["kimlik"] for y in YER.values()}  # 'dağ' -> 'dag' (sec.yer_cezasi)
KLASIK = [k["isim"] for k in KAR.values()]
KARTLAR = {k["ad"]["deger"]: k for k in json.load(open(os.path.join(ROOT, "data", "urun_kartlari.json"),
                                                        encoding="utf-8"))["kartlar"]}
POP_KART = {k["isim"]: k for k in json.load(open(os.path.join(ROOT, "data", "oyuncak_populer", "karakterler.json"),
                                                  encoding="utf-8"))}


# ---------------------------------------------------------------- eski modelin bildiği (figür, yer)

def eski_bilinen():
    """{(isim, yer): hikâye sayısı}: c3ft_tek'in eğitimine giren popüler hikâyeler (zincir_tek.sh: KAYNAK'taki
    oyuncak_populer, --haric data/egitim_haric_tek.txt, --bolme data/bolme.json)."""
    d = os.path.join(ROOT, "data", "oyuncak_populer")
    spec = importlib.util.spec_from_file_location("kontrol_oyuncak_populer", os.path.join(d, "kontrol.py"))
    kontrol = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(kontrol)
    iyi, _ = kontrol.oku()
    hik = prepare_ft2.kimlik_ver("oyuncak_populer", iyi)
    haric = {s.strip() for s in open(os.path.join(ROOT, "data", "egitim_haric_tek.txt"), encoding="utf-8") if s.strip()}
    b = json.load(open(os.path.join(ROOT, "data", "bolme.json"), encoding="utf-8"))
    haric |= set(b["dogrulama"]) | set(b["haric"])
    say = {}
    for h in hik:
        if h["id"] not in haric:
            anahtar = (h["turler"][0], h["yer"])
            say[anahtar] = say.get(anahtar, 0) + 1
    return say, hik


# ---------------------------------------------------------------- yeni modelin doğrulama kayıtları

def dogrulama_kayitlari(yeni_dir=None):
    """{(figür, yer): kanonik kayıt} (izin.txt'de 'dogrulama' işaretli). Önce data/tr_c3ft_urun/.../dogrulama.json
    (salt okunur), yoksa kabul.jsonl + izin.txt."""
    yol = os.path.join(ROOT, "data", "tr_c3ft_urun", "vocab-16384", "dogrulama.json")
    out = {}
    if os.path.exists(yol):
        for h in json.load(open(yol, encoding="utf-8")):
            k = uk.kanonik(h["turler"][0], h["yer"], h["yan"], h["sorun"], h["cozum"], h["metin"])
            assert uk.sha1(k) == h["sha1"], h["id"]
            out.setdefault((k["figur"], k["yer"]), k)
        return out, yol
    izin, _ = prepare_ft2.izin_oku(os.path.join(ROOT, "data", "urun_v2", "izin.txt"))
    for s in open(os.path.join(ROOT, "data", "urun_v2", "kabul.jsonl"), encoding="utf-8"):
        if s.strip():
            r = json.loads(s)
            if izin.get(r["sha1"]) == "dogrulama":
                out.setdefault((r["kayit"]["figur"], r["kayit"]["yer"]), r["kayit"])
    return out, "data/urun_v2/kabul.jsonl + izin.txt"


# ---------------------------------------------------------------- istemler

def on_ek(dizgi):
    """Eğitim dizgisinin '\\nSorun:'a kadarki öneki (plan modu istemi)."""
    i = dizgi.index("\nSorun: ")
    return dizgi[:i + len("\nSorun:")]


def istem_yeni(figur, yer, yan):
    return on_ek(uk.dizgi({"figur": figur, "yer": yer, "yan": list(yan), "sorun": "S", "cozum": "Ç", "govde": "G"},
                          plan=True, yan_alani=True))


def istem_eski(isim, yer):
    return on_ek(prepare_ft2.baslik({"turler": [isim], "yer": yer, "metin": "G"}, plan=("S", "Ç")))


def istem_idleri(tok, metin, eot=True):
    """baslangic.prompt_idler(plan=True) yöntemi: önek + ' top' kodlanır, öneke düşen token'lar alınır."""
    enc = tok.encode(metin + " top")
    ids = [i for i, (_, son) in zip(enc.ids, enc.offsets) if son <= len(metin)]
    return ([tok.token_to_id("<|endoftext|>")] if eot else []) + ids


def egitim_idleri(tok, dizgi):
    """Eğitimdeki gibi: önceki hikâyenin EOT'si + dizginin kendi kodlaması."""
    return [tok.token_to_id("<|endoftext|>")] + tok.encode(dizgi).ids


# ---------------------------------------------------------------- isimler, yasak ve seçici

_BUYUK = re.compile(r"[A-ZÇĞİÖŞÜ][a-zçğıöşüA-Z]+")


def izinli_adlar(figur, yan):
    """Figürün kartlarında büyük harfle geçen kelimeler + figür adı + yanlar (tek kelimeler)."""
    metin = json.dumps(KARTLAR.get(figur, {}), ensure_ascii=False)
    if figur in POP_KART:
        metin += json.dumps(POP_KART[figur], ensure_ascii=False)
    metin += " " + figur + " " + " ".join(yan)
    return set(_BUYUK.findall(metin))


def yasak(tok, izinli):
    """uret.yasak_idler'in listesi (12 klasik ad + YABANCI), figürün izinli adları hariç; paketle.isim_idleri kuralı."""
    idler = set()
    for n in KLASIK + YABANCI:
        if n not in izinli:
            idler.update(isim_idleri(tok, n))
    return sorted(idler)


_ISIM_KURALLARI = ("uydurma kelime", "yanlış isim", "uydurma karakter adı")


def puan(metin, figur, izinli, lp, n, yer, bitti, plan):
    """sec.puanla'nın ürün figürüne uyarlanmış hâli (bkz. modül açıklaması)."""
    kim = "urun:" + uk.figur_kimligi(figur)
    tur = KARTLAR[figur]["tur"]["deger"] if figur in KARTLAR else figur
    KAR[kim] = {"kimlik": kim, "isim": figur, "tur": tur}
    try:
        c = [x for x in sec.cezalar(metin, [kim], n, bitti=bitti, plan=plan) if not x[1].startswith(_ISIM_KURALLARI)]
    finally:
        del KAR[kim]
    bilinen = set(KLASIK) | izinli
    izinli_k = {sec.kucuk(w) for w in izinli}
    kelimeler = re.findall(r"[a-zçğıöşüâîû]+", sec.kucuk(metin))
    if sec.SOZLUK is not None:
        bil = [w for w in kelimeler if w not in sec.SOZLUK and w not in izinli_k]
        if bil:
            c.append((1.5 * len(bil), f"uydurma kelime {bil[:4]}"))
    yanlis = set(sec.BUYUK.findall(metin)) & ((set(KLASIK) | set(YABANCI)) - izinli)
    if yanlis:
        c.append((2, f"yanlış isim {sorted(yanlis)}"))
    ozel = re.findall(r"(?<![.!?\"“] )(?<!^)\b([A-ZÇĞİÖŞÜ][a-zçğıöşü]+)['’]", metin)
    bas = re.findall(r"(?:^|[.!?]\s+)([A-ZÇĞİÖŞÜ][a-zçğıöşü]+)['’]", metin)
    uyd = sorted({w for w in ozel + bas if w not in bilinen})
    if uyd:
        c.append((2, f"uydurma karakter adı {uyd[:3]}"))
    ceza = sum(p for p, _ in c) + sec.yer_cezasi(metin, YER_KIMLIK[yer])
    return -ceza + 2 * lp, [r for _, r in c]


# ---------------------------------------------------------------- üretim

def uret_bir(model_dir, ids, ban, seed, tok, satir):
    """uret.uret_plan'ın model-plan yolu, hazır istem token'larıyla (figür baslangic kataloğunda olmadığı için)."""
    son = tok.token_to_id("<|endoftext|>")
    nl = uret.satir_sonu(tok)
    pairs, err = uret._gen(model_dir, ids, ban, seed, AYAR["temp"], AYAR["rep"], tok, AYAR["n"],
                           AYAR["pencere"] == "govde", satir, plan_nl=nl)
    toks = [t for t, _ in pairs]
    k = next((k for k in range(len(toks) - 1) if toks[k] == nl and toks[k + 1] == nl), None)
    plan_c = pairs if k is None else pairs[:k]
    govde_c = [] if k is None else pairs[k + 2:]
    plan = ("Sorun:" + tok.decode([t for t, _ in uret._eot_kes(plan_c, son)[0]])).rstrip()
    bozuk = k is None or "plan_bozuk" in err.split()
    govde_c, bitti = uret._eot_kes(govde_c, son)
    metin = tok.decode([t for t, _ in govde_c]).strip()
    if bozuk or not metin:
        return {"metin": "", "n": 0, "lp": uret.BOZUK_LP, "bitti": False, "plan": plan, "plan_bozuk": True}
    return {"metin": metin, "n": len(govde_c), "lp": sum(l for _, l in govde_c) / len(govde_c), "bitti": bitti,
            "plan": plan, "plan_bozuk": False}


def vakalari_kur(yan_kipi):
    say, _ = eski_bilinen()
    dog, dog_kaynak = dogrulama_kayitlari()
    ortak, yeni, atlanan = [], [], []
    for f in FIGURLER:
        kart_yer = [y["etiket"] for y in KARTLAR[f]["yerler"]]
        eski_yer = [y for y in kart_yer if say.get((f, y), 0) > 0]
        eski_figur = any(k[0] == f for k in say)
        if eski_figur:
            if not eski_yer:
                atlanan.append((f, "eski eğitimde ürün kartının yerleriyle ortak yer yok"))
                continue
            yerler, grup = eski_yer[:YER_SAYISI], "ortak"
            if len(yerler) < YER_SAYISI:
                atlanan.append((f, f"yalnız {len(yerler)} ortak yer: {yerler}"))
        else:
            yerler, grup = kart_yer[:YER_SAYISI], "yeni"
        for y in yerler:
            kayit = dog.get((f, y))
            yan = (kayit["yan"] if kayit else []) if yan_kipi == "dogrulama" else []
            v = {"grup": grup, "figur": f, "yer": y, "yan": yan, "eski_n": say.get((f, y), 0),
                 "dog_sha1": uk.sha1(kayit) if kayit else None}
            (ortak if grup == "ortak" else yeni).append(v)
    for i, v in enumerate(ortak + yeni):
        v["id"] = i
    return ortak, yeni, atlanan, dog_kaynak


def kol(model_dir, ad, vakalar, K, istem_f, tok):
    """Bir model x vaka listesi -> degerlendirme/<ad>/{hikayeler,adaylar,ayar}.json."""
    satir = uret.satir_idleri(tok) if AYAR["satir_yasak"] else None
    if "[-S " not in uret.gen_kullanim():
        raise SystemExit(f"{uret.GEN} -S bilmiyor (eski derleme)")
    sonuc, hepsi = [], []
    for v in vakalar:
        izinli = izinli_adlar(v["figur"], v["yan"])
        metin_istem = istem_f(v)
        ids = istem_idleri(tok, metin_istem, AYAR["eot_on"])
        ban = yasak(tok, izinli)
        adaylar = []
        for j in range(K):
            h = {"vaka": v["id"], "j": j, **uret_bir(model_dir, ids, ban, 1000 * v["id"] + j, tok, satir)}
            if K > 1:
                h["puan"], h["cezalar"] = puan(h["metin"], v["figur"], izinli, h["lp"], h["n"], v["yer"],
                                               h["bitti"], h["plan"])
            adaylar.append(h)
        hepsi += adaylar
        h = max(adaylar, key=lambda x: x["puan"]) if K > 1 else adaylar[0]
        sonuc.append({"id": v["id"], "grup": v["grup"], "figurler": [v["figur"]], "yer": v["yer"],
                      "baslik": f"Karakter: {v['figur']} | Yer: {v['yer']}", "istem": metin_istem,
                      "yan": v["yan"] if " | Yan: " in metin_istem.split("\n")[0] else [],
                      "metin": h["metin"], "token": h["n"], "plan": h["plan"], "plan_bozuk": h["plan_bozuk"],
                      "aday": h["j"], **({"puan": round(h["puan"], 3)} if K > 1 else {})})
        print(f"  [{ad}] {v['id']:>2} {v['figur']} | {v['yer']}: aday {h['j']}, {h['n']} token"
              + (", PLAN BOZUK" if h["plan_bozuk"] else ""), file=sys.stderr, flush=True)
    d = os.path.join(HERE, ad)
    os.makedirs(d, exist_ok=True)
    sha = lambda p: hashlib.sha256(open(p, "rb").read()).hexdigest()[:16]  # noqa: E731
    for dosya, veri in (("hikayeler.json", sonuc), ("adaylar.json", hepsi),
                        ("ayar.json", {**AYAR, "aday": K, "model": model_dir,
                                       "model_sha": sha(os.path.join(model_dir, "model.bin")),
                                       "gen_sha": sha(uret.GEN), "tohum": "1000*id+j"})):
        with open(os.path.join(d, dosya), "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=1)
    print(f"{len(sonuc)} hikâye -> degerlendirme/{ad}/hikayeler.json", file=sys.stderr)


def istem_denetimi(tok_eski, tok_yeni, vakalar):
    """İstemleri göster; gerçek eğitim dizgileriyle karşılaştır (token öneki olmalı)."""
    print("=== İstem biçimleri (repr) ===")
    for v in vakalar:
        print(f"{v['id']:>2} {v['grup']:<5} yeni: {istem_yeni(v['figur'], v['yer'], v['yan'])!r}")
        if v["grup"] == "ortak":
            print(f"{'':>8} eski: {istem_eski(v['figur'], v['yer'])!r}")
    print("\n=== Yeni model: gerçek dizgi() ile karşılaştırma (kabul edilmiş eğitim hikâyeleri) ===")
    izin, _ = prepare_ft2.izin_oku(os.path.join(ROOT, "data", "urun_v2", "izin.txt"))
    kabul = [json.loads(s) for s in open(os.path.join(ROOT, "data", "urun_v2", "kabul.jsonl"), encoding="utf-8")
             if s.strip()]
    ornek = [r for r in kabul if izin.get(r["sha1"]) == "egitim"]
    secilen = [next(r for r in ornek if r["kayit"]["yan"]), next(r for r in ornek if not r["kayit"]["yan"]),
               next(r for r in ornek if r["kayit"]["figur"] == "Örümcek Adam")]
    for r in secilen:
        k = r["kayit"]
        assert uk.sha1(k) == r["sha1"]
        d = uk.dizgi(k, plan=True, yan_alani=True)
        ist = istem_yeni(k["figur"], k["yer"], k["yan"])
        ids, tam = istem_idleri(tok_yeni, ist), egitim_idleri(tok_yeni, d)
        print(f"{r['kimlik']}\n  dizgi(): {d[:len(ist) + 60]!r}…\n  istem  : {ist!r}\n  metin öneki: "
              f"{d.startswith(ist)}  token öneki: {tam[:len(ids)] == ids} ({len(ids)} token)")
        assert d.startswith(ist) and tam[:len(ids)] == ids, r["kimlik"]
    print("\n=== Eski model: gerçek prepare_ft2.baslik() ile karşılaştırma (c3ft_tek eğitim hikâyeleri) ===")
    say, hik = eski_bilinen()
    plan = {}
    for s in open(os.path.join(ROOT, "data", "oyuncak_plan", "plan_hepsi.jsonl"), encoding="utf-8"):
        if s.strip():
            p = json.loads(s)
            plan[p["id"]] = p
    haric = {s.strip() for s in open(os.path.join(ROOT, "data", "egitim_haric_tek.txt"), encoding="utf-8")}
    for isim in ("Elsa", "Örümcek Adam"):
        h = next(h for h in hik if h["turler"] == [isim] and h["id"] not in haric
                 and prepare_ft2.plani(plan, h) is not None)
        d = prepare_ft2.baslik(h, False, prepare_ft2.plani(plan, h))
        ist = istem_eski(isim, h["yer"])
        ids, tam = istem_idleri(tok_eski, ist), egitim_idleri(tok_eski, d)
        print(f"{h['id']}\n  baslik(): {d[:len(ist) + 60]!r}…\n  istem   : {ist!r}\n  metin öneki: "
              f"{d.startswith(ist)}  token öneki: {tam[:len(ids)] == ids} ({len(ids)} token)")
        assert d.startswith(ist) and tam[:len(ids)] == ids, h["id"]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--yeni", default="hf_c3ft_urun")
    ap.add_argument("--eski", default="hf_c3ft_tek")
    ap.add_argument("--aday", type=int, default=8, help="vaka başına aday (1: seçicisiz tek örnek)")
    ap.add_argument("--yan", choices=["dogrulama", "bos"], default="dogrulama")
    ap.add_argument("--sadece-eski", action="store_true", help="yalnız eski modelle üret (yeni model henüz yok)")
    ap.add_argument("--istem-goster", action="store_true", help="istemleri göster ve eğitim dizgileriyle denetle")
    ap.add_argument("--kuru", action="store_true", help="üretme; yalnız vakaları ve istemleri göster")
    a = ap.parse_args()
    a.yeni, a.eski = (p if os.path.isabs(p) else os.path.join(ROOT, p) for p in (a.yeni, a.eski))
    ortak, yeni, atlanan, dog_kaynak = vakalari_kur(a.yan)
    print(f"ortak figürler: {sorted({v['figur'] for v in ortak}, key=FIGURLER.index)}")
    print(f"yeni figürler : {sorted({v['figur'] for v in yeni}, key=FIGURLER.index)}")
    for f, neden in atlanan:
        print(f"UYARI {f}: {neden}")
    print(f"yan kaynağı: {dog_kaynak if a.yan == 'dogrulama' else 'yok (--yan bos)'}")
    for v in ortak + yeni:
        print(f"  {v['id']:>2} {v['grup']:<5} {v['figur']} | {v['yer']} | yan {v['yan']} | eski eğitimde "
              f"{v['eski_n']} hikâye")
    tok_eski = Tokenizer.from_file(os.path.join(a.eski, "tokenizer.json"))
    yeni_tok = os.path.join(a.yeni, "tokenizer.json")
    if not os.path.exists(yeni_tok):  # model henüz yok: prepare_ft2'nin tokenizer'ı (export aynısını kopyalar)
        yeni_tok = os.path.join(ROOT, "data", "tr_c3ft_urun", "vocab-16384", "tokenizer.json")
    tok_yeni = Tokenizer.from_file(yeni_tok)
    if a.istem_goster or a.kuru:
        istem_denetimi(tok_eski, tok_yeni, ortak + yeni)
    if a.kuru:
        return
    kol(a.eski, "urun_kiyas_tek", ortak, a.aday, lambda v: istem_eski(v["figur"], v["yer"]), tok_eski)
    if a.sadece_eski:
        return
    if not os.path.exists(os.path.join(a.yeni, "model.bin")):
        raise SystemExit(f"{a.yeni}/model.bin yok (eğitim bitmedi?); --sadece-eski ile yalnız eski model")
    istem_n = lambda v: istem_yeni(v["figur"], v["yer"], v["yan"])  # noqa: E731
    kol(a.yeni, "urun_kiyas_yeni", ortak, a.aday, istem_n, tok_yeni)
    kol(a.yeni, "urun_kiyas_yeni_mutlak", yeni, a.aday, istem_n, tok_yeni)


if __name__ == "__main__":
    main()
