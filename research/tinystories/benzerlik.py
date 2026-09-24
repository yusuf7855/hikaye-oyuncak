"""Sabit doğrulama bölmesi + sızıntı temizliği: data/bolme.json.

Doğrulama: prepare_ft2'nin seed 0 bölmesiyle aynı kural (her tek-figür (tür, yer) ve her ikili grubundan bir hikâye).
Sızıntı: bazı hikâyeler başka bir figür için isim değiştirilerek kopyalanmış; doğrulama hikâyesinin böyle bir kopyası
eğitimde kalırsa ölçüm iyimser olur. Figür isimleri ve türleri çıkarılmış metinler 5 harflik köklerle TF-IDF'e
çevrilir; herhangi bir doğrulama hikâyesine kosinüsü --esik'ten büyük olan eğitim hikâyeleri "haric" listesine girer.

Kullanım: PYTHONPATH=src python -m research.tinystories.benzerlik [--esik 0.6]
Sonra:    prepare_ft2 --bolme data/bolme.json   (doğrulama bu kimlikler, haric eğitimden çıkar)
"""
import argparse
import importlib.util
import json
import math
import random
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KATALOG = json.load(open(ROOT / "data" / "karakterler.json", encoding="utf-8"))
SILINECEK = {k["isim"].lower() for k in KATALOG["karakterler"]} | {k["tur"] for k in KATALOG["karakterler"]}


def kucuk(s):
    return s.replace("I", "ı").replace("İ", "i").lower()


def hikayeler():
    from research.tinystories.prepare_ft2 import kimlik_ver
    out = []
    for kaynak in ("oyuncak_v2", "oyuncak_v3"):
        d = ROOT / "data" / kaynak
        spec = importlib.util.spec_from_file_location(f"kontrol_{kaynak}", d / "kontrol.py")
        kontrol = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(kontrol)
        iyi, _ = kontrol.oku()
        out += kimlik_ver(kaynak, iyi)
    return out


def dogrulama_sec(hs, seed=0):
    """prepare_ft2 ile aynı gruplama ve seed: her gruptan karıştırılmış ilk hikâye."""
    rng = random.Random(seed)
    gruplar = {}
    for h in hs:
        anahtar = (h["turler"][0], h["yer"]) if len(h["turler"]) == 1 else tuple(sorted(h["turler"]))
        gruplar.setdefault(anahtar, []).append(h)
    secilen = []
    for k in sorted(gruplar, key=str):
        g = gruplar[k][:]
        rng.shuffle(g)
        secilen.append(g[0]["id"])
    return secilen


def vektor(metin, idf=None):
    kokler = [w[:5] for w in re.findall(r"[a-zçğıöşüâîû]+", kucuk(metin))
              if not any(w.startswith(s) for s in SILINECEK)]
    tf = Counter(kokler)
    if idf is None:
        return tf
    v = {k: c * idf.get(k, 0.0) for k, c in tf.items()}
    n = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {k: x / n for k, x in v.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--esik", type=float, default=0.6)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default=str(ROOT / "data" / "bolme.json"))
    a = ap.parse_args()
    hs = hikayeler()
    dog = set(dogrulama_sec(hs, a.seed))
    df = Counter()
    for h in hs:
        df.update(set(vektor(h["metin"])))
    idf = {k: math.log(len(hs) / c) for k, c in df.items()}
    vek = {h["id"]: vektor(h["metin"], idf) for h in hs}
    haric, en_yakin = [], {}
    for h in hs:
        if h["id"] in dog:
            continue
        v = vek[h["id"]]
        best = max(((sum(x * vek[d].get(k, 0.0) for k, x in v.items()), d) for d in dog))
        if best[0] > a.esik:
            haric.append(h["id"])
            en_yakin[h["id"]] = [best[1], round(best[0], 3)]
    json.dump({"esik": a.esik, "seed": a.seed, "dogrulama": sorted(dog), "haric": sorted(haric),
               "en_yakin": en_yakin}, open(a.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(dog)} doğrulama, {len(haric)} eğitim hikâyesi sızıntı diye dışarıda (kosinüs > {a.esik}) -> {a.out}")


if __name__ == "__main__":
    main()
