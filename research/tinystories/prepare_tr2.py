"""Türkçe TinyStories + oyuncak hikâyeleriyle tokenizer ve token dosyaları (C2).

prepare_tr'dan farkı: BPE, genel metnin yanında oyuncak hikâyelerini (v2 + v3) de --oyuncak-tekrar kez
görür. Böylece figür isimleri (" Paytak", " Cikcik", " Karabaş"...) ve türleri tek token olur;
küçük modelin çok parçalı bir ismi doğru hecelemesi gerekmez. Token dosyaları yalnızca genel
metinden üretilir (oyuncak hikâyeleri ince ayarda girer).

Kullanım: TS_DATA=data/tr2_tinystories PYTHONPATH=src python -m research.tinystories.prepare_tr2 --vocab 16384
Ham metin: data/tr_tinystories/raw/tr-tinystories.txt (README'deki indirme adımı)
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np
from tokenizers import Tokenizer, decoders, models, pre_tokenizers, trainers

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "tr_tinystories" / "raw" / "tr-tinystories.txt"
VAL_FRACTION = 0.005


def oyuncak_metinleri():
    metinler = []
    for kaynak in ("oyuncak_v2", "oyuncak_v3"):
        d = ROOT / "data" / kaynak
        spec = importlib.util.spec_from_file_location(f"kontrol_{kaynak}", d / "kontrol.py")
        kontrol = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(kontrol)
        iyi, _ = kontrol.oku()
        metinler += [h["metin"] for h in iyi]
    return metinler


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--vocab", type=int, default=16384)
    ap.add_argument("--out", default=str(ROOT / "data" / "tr2_tinystories"))
    ap.add_argument("--oyuncak-tekrar", type=int, default=4)
    args = ap.parse_args()
    out = Path(args.out) / f"vocab-{args.vocab}"
    out.mkdir(parents=True, exist_ok=True)

    text = RAW.read_text(encoding="utf-8", errors="ignore")
    text = text[: text.rfind("<|endoftext|>") + len("<|endoftext|>")]
    katalog = json.load(open(ROOT / "data" / "karakterler.json", encoding="utf-8"))
    isimler = [k["isim"] for k in katalog["karakterler"]]
    turler = [k["tur"] for k in katalog["karakterler"]]

    tok_path = out / "tokenizer.json"
    if tok_path.exists():
        tok = Tokenizer.from_file(str(tok_path))
        print(f"var: {tok_path}")
    else:
        oyuncak = "\n<|endoftext|>\n".join(oyuncak_metinleri())
        tok = Tokenizer(models.BPE(unk_token=None))
        tok.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=False)
        tok.decoder = decoders.ByteLevel()
        trainer = trainers.BpeTrainer(
            vocab_size=args.vocab, special_tokens=["<|endoftext|>"],
            initial_alphabet=pre_tokenizers.ByteLevel.alphabet(), show_progress=False)
        tok.train_from_iterator([text[: 40 * 1024 * 1024]] + [oyuncak] * args.oyuncak_tekrar, trainer=trainer)
        tok.save(str(tok_path))

    parcali = []
    for w in isimler + turler:
        for v in (" " + w, w):
            n = len(tok.encode(v).ids)
            if n > 1 and v.startswith(" "):
                parcali.append((v, n))
    print("çok parçalı isim/tür:", parcali or "yok")

    eot = tok.token_to_id("<|endoftext|>")
    docs = [d for d in text.split("<|endoftext|>") if d.strip()]
    ids = []
    for i in range(0, len(docs), 20000):
        for enc in tok.encode_batch(docs[i: i + 20000]):
            ids.extend(enc.ids)
            ids.append(eot)
        print(f"  {min(i + 20000, len(docs))}/{len(docs)}, {len(ids) / 1e6:.1f}M token", flush=True)
    arr = np.array(ids, dtype=np.uint16)
    n_val = int(len(arr) * VAL_FRACTION)
    arr[:-n_val].tofile(out / "train.bin")
    arr[-n_val:].tofile(out / "val.bin")
    print(f"train {len(arr) - n_val:,} / val {n_val:,} token; {len(text) / len(arr):.2f} bayt/token")


if __name__ == "__main__":
    sys.exit(main())
