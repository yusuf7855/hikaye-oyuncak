"""Öğrenen seçici (Tur 2): hikâyenin hakem puanını tahmin eden küçük doğrusal katman.

Özellikler (kartta da ucuz): -(kural cezaları), gövde uzunluğu/100 ve modelin son gizli durumunun (çıkış normundan
sonra, head'in girdisi) gövde token'ları üstünden ortalaması (D = 160). Gizli durum C motorundan alınır (gen -H -G):
kartın hesapladığıyla aynı sayılar. Puan = w·((x - mu) / sd) + b; ESP32'de hikâye başına 160 toplama/token + bir
162'lik çarpım.

Kullanım:
  python degerlendirme/odul.py ozellik <model_dizini>          # etiketli hikâyelerin özellikleri -> <model>/odul_ozellik.json
  python degerlendirme/odul.py egit <model_dizini> [--lam 30] [--haric kol,kol] [--cikti odul.json]
      # kol-dışı çapraz doğrulama + <model>/odul.json; --haric: bu kolların etiketleri eğitime girmez (ör. seçimin
      # ölçüleceği havuzdan seçilmiş hikâyeler: sızıntı)
  python degerlendirme/odul.py sec <model_dizini> <havuz_adı> <yeni_kol> [--odul odul.json] [--dogrulama D]
      # <model>/adaylar_<havuz>.json'daki adayları öğrenen puanla seçer -> degerlendirme/<yeni_kol>/hikayeler.json
Etiketler: degerlendirme/*/puan_*.json (rubrik hakemleri; vaka başına hakem ortalaması) ve hikayeler.json'daki metin.
"""
import argparse
import collections
import glob
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, ROOT)
from tokenizers import Tokenizer  # noqa: E402
from baslangic import KAR, prompt_idler  # noqa: E402
from sec import cezalar, guvenlik_cezasi, yer_cezasi  # noqa: E402
from uret import plan_bol  # noqa: E402

GEN = os.path.join(ROOT, "gen")
ISIM = {v["isim"]: k for k, v in KAR.items()}


def kodla(tok, kim, yer, metin, plan=None):
    """(istem id'leri, gövdenin başladığı sıra). İstem: EOT + başlık (+ plan satırları) + gövde, eğitimdeki gibi."""
    p = plan_bol(plan) if plan else None
    bas = prompt_idler(tok, kim, yer, eot=True, plan_metni=p)
    govde = tok.encode(metin).ids
    return bas + govde, len(bas)


def gizli(model_bin, ids, bas):
    """C motoruyla gövde token'larının gizli durum ortalaması (gen -H -G, n = 0)."""
    ids = ids[:255]
    r = subprocess.run([GEN, model_bin, "0", "0.5", "40", "0", "1.0", "-H", "-G", str(bas)] + [str(i) for i in ids],
                       capture_output=True, text=True, check=True)
    satir = next(s for s in r.stderr.splitlines() if s.startswith("hid "))
    return [float(v) for v in satir.split()[1:]]


def ceza(metin, kim, yer, plan):
    c = sum(p for p, _ in cezalar(metin, kim, 0, bitti=True, plan=plan)) + yer_cezasi(metin, yer)
    g = guvenlik_cezasi(metin)
    return c + (g[0] if g else 0)


def vektor(o):
    return [-o["ceza"], o["n"] / 100] + o["h"]


def etiketler():
    """[(kol, id, hikâye, hakem ortalaması)]: puan dosyası olan her değerlendirme klasöründen."""
    out = []
    for d in sorted(glob.glob(os.path.join(HERE, "*", ""))):
        yol = os.path.join(d, "hikayeler.json")
        if not glob.glob(d + "puan_*.json") or not os.path.exists(yol):
            continue
        H = {h["id"]: h for h in json.load(open(yol, encoding="utf-8"))}
        p = collections.defaultdict(list)
        for f in glob.glob(d + "puan_*.json"):
            for r in json.load(open(f, encoding="utf-8")):
                p[r["id"]].append(r["puan"])
        for i, v in p.items():
            h = H[i]
            if all(f.split()[0] in ISIM for f in h["figurler"]):
                out.append((os.path.basename(d.rstrip("/")), i, h, sum(v) / len(v)))
    return out


def ozellik(model_dir):
    tok = Tokenizer.from_file(os.path.join(model_dir, "tokenizer.json"))
    mb = os.path.join(model_dir, "model.bin")
    out = []
    for kol, i, h, y in etiketler():
        kim = [ISIM[f.split()[0]] for f in h["figurler"]]
        plan = h.get("plan") if not h.get("plan_bozuk") else None
        ids, bas = kodla(tok, kim, h["yer"], h["metin"], plan)
        out.append({"kol": kol, "id": i, "y": y, "ceza": ceza(h["metin"], kim, h["yer"], plan),
                    "n": len(ids) - bas, "h": gizli(mb, ids, bas)})
    yol = os.path.join(model_dir, "odul_ozellik.json")
    json.dump(out, open(yol, "w"), ensure_ascii=False)
    print(f"{len(out)} etiketli hikâye -> {yol}")


def ridge(X, y, lam):
    mu, sd = X.mean(0), X.std(0) + 1e-6
    Z = (X - mu) / sd
    w = np.linalg.solve(Z.T @ Z + lam * np.eye(X.shape[1]), Z.T @ (y - y.mean()))
    return mu, sd, w, y.mean()


def egit(model_dir, lam, haric=(), cikti="odul.json"):
    O = [o for o in json.load(open(os.path.join(model_dir, "odul_ozellik.json"))) if o["kol"] not in haric]
    X = np.array([vektor(o) for o in O])
    y = np.array([o["y"] for o in O])
    kol = np.array([o["kol"] for o in O])
    pred = np.zeros(len(y))
    for k in np.unique(kol):  # bir kol dışarıda: hiç görmediği sürüm/ayar üstünde ölçülür
        t = kol != k
        mu, sd, w, b = ridge(X[t], y[t], lam)
        pred[~t] = ((X[~t] - mu) / sd) @ w + b
    kural = np.corrcoef(X[:, 0], y)[0, 1]
    print(f"n={len(y)}, {len(np.unique(kol))} kol | kol-dışı korelasyon: öğrenen {np.corrcoef(pred, y)[0, 1]:.3f}, "
          f"yalnız kurallar {kural:.3f}")
    mu, sd, w, b = ridge(X, y, lam)
    json.dump({"ozellik": "[-ceza, n/100, gizli ortalama (D)]", "lam": lam, "n": len(y),
               "mu": mu.round(6).tolist(), "sd": sd.round(6).tolist(), "w": w.round(6).tolist(), "b": round(b, 6)},
              open(os.path.join(model_dir, cikti), "w"))
    print(f"-> {model_dir}/{cikti}")


def puan(odul, ceza_, n, h):
    x = np.array([-ceza_, n / 100] + list(h))
    return float(((x - np.array(odul["mu"])) / np.array(odul["sd"])) @ np.array(odul["w"]) + odul["b"])


def sec(model_dir, havuz, yeni, odul_ad, dogrulama=None):
    from uret import vakalar  # noqa: E402
    odul = json.load(open(os.path.join(model_dir, odul_ad)))
    tok = Tokenizer.from_file(os.path.join(model_dir, "tokenizer.json"))
    mb = os.path.join(model_dir, "model.bin")
    A = json.load(open(os.path.join(model_dir, f"adaylar_{havuz}.json")))
    gruplar = collections.defaultdict(list)
    for a in A:
        gruplar[a["vaka"]].append(a)
    sonuc = []
    for i, (kim, yer, bilgi) in enumerate(vakalar(dogrulama)):
        en, en_p = None, None
        for a in gruplar[i]:
            if not a["metin"] or a.get("plan_bozuk"):
                continue
            ids, bas = kodla(tok, kim, yer, a["metin"], a.get("plan"))
            p = puan(odul, ceza(a["metin"], kim, yer, a.get("plan")), len(ids) - bas, gizli(mb, ids, bas))
            if en_p is None or p > en_p:
                en, en_p = a, p
        en = en or gruplar[i][0]
        sonuc.append({"id": i, "figurler": [KAR[k]["isim"] + " (" + KAR[k]["tur"] + ")" for k in kim], "yer": yer,
                      "baslik": f"Karakter: {', '.join(KAR[k]['tur'] for k in kim)} | Yer: {yer}", "metin": en["metin"],
                      "token": en["n"], "plan": en.get("plan"), "plan_bozuk": en.get("plan_bozuk", False),
                      "odul": round(en_p, 3) if en_p is not None else None,
                      **({"hikaye_id": bilgi["hikaye_id"]} if bilgi else {})})
    os.makedirs(os.path.join(HERE, yeni), exist_ok=True)
    json.dump(sonuc, open(os.path.join(HERE, yeni, "hikayeler.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(sonuc)} hikâye -> degerlendirme/{yeni}/hikayeler.json")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("komut", choices=["ozellik", "egit", "sec"])
    ap.add_argument("model_dir")
    ap.add_argument("havuz", nargs="?")
    ap.add_argument("yeni", nargs="?")
    ap.add_argument("--lam", type=float, default=30.0)
    ap.add_argument("--haric", default="")
    ap.add_argument("--cikti", default="odul.json")
    ap.add_argument("--odul", default="odul.json")
    ap.add_argument("--dogrulama", default=None)
    a = ap.parse_args()
    if a.komut == "ozellik":
        ozellik(a.model_dir)
    elif a.komut == "egit":
        egit(a.model_dir, a.lam, set(filter(None, a.haric.split(","))), a.cikti)
    else:
        sec(a.model_dir, a.havuz, a.yeni, a.odul, a.dogrulama)
