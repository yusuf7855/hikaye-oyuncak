"""Oyuncak ince ayar verisi: Claude Code'un yazdığı hikâyeler + genel Türkçe veriden bir dilim.

Her hikâye "Karakter: <k> | Yer: <y>" başlığıyla başlar; model düğme seçimine göre hikâye
kurmayı buradan öğrenir. Her kombinasyondan 1 hikâye doğrulama için ayrılır (ezber ölçümü).
Oyuncak hikâyeleri --tekrar kez çoğaltılır, genel veriden --genel-token kadar eklenir ki model
genel Türkçesini unutmasın.

Kullanım: PYTHONPATH=src python -m research.tinystories.prepare_ft
Çıktı: data/tr_ft/vocab-32768/{train,val}.bin + aynı tokenizer.json (hash eşleşmesi için kopya)
"""
import argparse
import os
import random
import shutil
import sys
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "data" / "tr_tinystories" / "vocab-32768"
OUT = ROOT / "data" / "tr_ft" / "vocab-32768"
sys.path.insert(0, str(ROOT / "data" / "oyuncak_hikayeleri"))
import kontrol  # noqa: E402


def baslik(h):
    return f"Karakter: {h['karakter']} | Yer: {h['yer']}\n\n{h['metin']}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tekrar", type=int, default=8)
    ap.add_argument("--genel-token", type=int, default=8_000_000)
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    rng = random.Random(args.seed)

    hikayeler, sorunlu = kontrol.oku()
    if sorunlu:
        raise SystemExit(f"{len(sorunlu)} sorunlu hikâye var; önce kontrol.py ile düzelt")
    gruplar = {}
    for h in hikayeler:
        gruplar.setdefault((h["karakter"], h["yer"]), []).append(h)
    egitim, dogrulama = [], []
    for k in sorted(gruplar):
        g = gruplar[k][:]
        rng.shuffle(g)
        dogrulama.append(g[0])
        egitim.extend(g[1:])

    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC / "tokenizer.json", OUT / "tokenizer.json")
    tok = Tokenizer.from_file(str(OUT / "tokenizer.json"))
    eot = tok.token_to_id("<|endoftext|>")

    def kodla(metinler):
        ids = []
        for enc in tok.encode_batch(metinler):
            ids.extend(enc.ids)
            ids.append(eot)
        return ids

    oyuncak = kodla([baslik(h) for h in egitim])
    # Genel veri: ana eğitim setinden rastgele bir pencere, hikâye sınırından başlayarak.
    genel_kaynak = np.memmap(SRC / "train.bin", dtype=np.uint16, mode="r")
    bas = rng.randrange(0, len(genel_kaynak) - args.genel_token - 1)
    while genel_kaynak[bas] != eot:
        bas += 1
    genel = genel_kaynak[bas + 1: bas + 1 + args.genel_token]

    # Oyuncak hikâyelerini parça parça genel verinin arasına dağıt (tek blok halinde değil).
    parcalar = [oyuncak] * args.tekrar
    genel_parca = np.array_split(genel, len(parcalar))
    train = []
    for o, g in zip(parcalar, genel_parca):
        train.extend(g.tolist())
        train.extend(o)
    val = kodla([baslik(h) for h in dogrulama])

    np.array(train, dtype=np.uint16).tofile(OUT / "train.bin")
    np.array(val, dtype=np.uint16).tofile(OUT / "val.bin")
    print(f"oyuncak: {len(egitim)} eğitim / {len(dogrulama)} doğrulama hikâyesi, "
          f"{len(oyuncak):,} token x{args.tekrar}")
    print(f"genel: {len(genel):,} token | toplam train {len(train):,} | val {len(val):,}")


if __name__ == "__main__":
    main()
