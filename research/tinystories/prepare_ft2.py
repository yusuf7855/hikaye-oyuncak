"""v2 oyuncak ince ayar verisi (12 figür, tek + ikili, sabit isimler) + genel Türkçe dilim.

Başlık biçimi (firmware/arayüz de aynısını üretir; ikili sırası karakterler.json sırasıdır):
    "Karakter: tavşan | Yer: orman\n\n"            tek figür
    "Karakter: tavşan, tilki | Yer: orman\n\n"     iki figür
Her tek-figür kombinasyonundan ve her ikiliden 1 hikâye doğrulamaya ayrılır.
Eski (v1) 960 hikâye bilerek dışarıda: çok isimli oldukları için isim çorbasını geri öğretirler.

Kullanım: PYTHONPATH=src python -m research.tinystories.prepare_ft2 [--vocab 16384]
Çıktı: data/tr_ft2/vocab-<V>/{train,val}.bin + aynı tokenizer.json
"""
import argparse
import importlib.util
import json
import random
import shutil
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer

ROOT = Path(__file__).resolve().parents[2]
V2 = ROOT / "data" / "oyuncak_v2"
SIRA = [k["tur"] for k in json.load(open(ROOT / "data" / "karakterler.json", encoding="utf-8"))["karakterler"]]


def baslik(h):
    turler = sorted(h["turler"], key=SIRA.index)
    return f"Karakter: {', '.join(turler)} | Yer: {h['yer']}\n\n{h['metin']}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vocab", type=int, default=16384)
    ap.add_argument("--tekrar", type=int, default=6)
    ap.add_argument("--genel-token", type=int, default=8_000_000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--out", default="tr_ft2", help="data/<out>/vocab-<V> altına yaz")
    ap.add_argument("--kaynak", default="oyuncak_v2", help="virgülle ayrılmış hikâye klasörleri (data/ altında)")
    args = ap.parse_args()
    rng = random.Random(args.seed)

    hikayeler = []
    for kaynak in args.kaynak.split(","):
        d = ROOT / "data" / kaynak
        spec = importlib.util.spec_from_file_location(f"kontrol_{kaynak}", d / "kontrol.py")
        kontrol = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(kontrol)
        iyi, sorunlu = kontrol.oku()
        if sorunlu:
            print(f"UYARI: {kaynak}: {len(sorunlu)} sorunlu hikâye dışarıda bırakıldı")
        hikayeler += iyi

    gruplar = {}
    for h in hikayeler:
        anahtar = (h["turler"][0], h["yer"]) if len(h["turler"]) == 1 else tuple(sorted(h["turler"]))
        gruplar.setdefault(anahtar, []).append(h)
    egitim, dogrulama = [], []
    for k in sorted(gruplar, key=str):
        g = gruplar[k][:]
        rng.shuffle(g)
        dogrulama.append(g[0])
        egitim.extend(g[1:])

    src = ROOT / "data" / "tr_tinystories" / f"vocab-{args.vocab}"
    out = ROOT / "data" / args.out / f"vocab-{args.vocab}"
    out.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src / "tokenizer.json", out / "tokenizer.json")
    tok = Tokenizer.from_file(str(out / "tokenizer.json"))
    eot = tok.token_to_id("<|endoftext|>")

    def kodla(metinler):
        ids = []
        for enc in tok.encode_batch(metinler):
            ids.extend(enc.ids)
            ids.append(eot)
        return ids

    genel_kaynak = np.memmap(src / "train.bin", dtype=np.uint16, mode="r")
    if args.genel_token > 0:
        bas = rng.randrange(0, len(genel_kaynak) - args.genel_token - 1)
        while genel_kaynak[bas] != eot:
            bas += 1
        genel = genel_kaynak[bas + 1: bas + 1 + args.genel_token]
    else:
        genel = np.zeros(0, dtype=np.uint16)

    # Her tekrarda hikâye sırası karışık; oyuncak blokları genel verinin arasına dağıtılır.
    train = []
    for g in np.array_split(genel, args.tekrar):
        train.extend(g.tolist())
        blok = egitim[:]
        rng.shuffle(blok)
        train.extend(kodla([baslik(h) for h in blok]))
    val = kodla([baslik(h) for h in dogrulama])
    uzun = sum(1 for h in egitim if len(tok.encode(baslik(h)).ids) + 1 > 256)

    np.array(train, dtype=np.uint16).tofile(out / "train.bin")
    np.array(val, dtype=np.uint16).tofile(out / "val.bin")
    tek = sum(len(h["turler"]) == 1 for h in egitim)
    print(f"oyuncak: {len(egitim)} eğitim ({tek} tek, {len(egitim) - tek} ikili) / {len(dogrulama)} doğrulama; "
          f"x{args.tekrar} | 256 tokeni aşan hikâye: {uzun}")
    print(f"genel: {len(genel):,} token | toplam train {len(train):,} | val {len(val):,}")


if __name__ == "__main__":
    main()
