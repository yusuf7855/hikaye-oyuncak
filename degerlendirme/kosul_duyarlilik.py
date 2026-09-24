"""Koşul duyarlılığı: doğrulama hikâyelerinin öğretmen zorlamalı NLL'i başlık koşuluna ne kadar bağlı (PyTorch, CPU).

Kullanım: PYTHONPATH=src python degerlendirme/kosul_duyarlilik.py --ckpt runs/ple-<etiket>-s0.pt \\
              --veri data/tr_<etiket>/vocab-16384/dogrulama.json [--eot] [--baslik oto|tema|eski] [--n N]
Tokenizer, dogrulama.json'un yanındaki tokenizer.json (checkpoint'in tokenizer özetiyle karşılaştırılır).
--baslik oto (varsayılan): modelin eğitildiği başlık biçimi yanındaki val.bin'in ilk başlığından okunur (temasız
eğitilmiş modelde EOT karşılaştırması eski başlıkla yapılmalı); tema/eski elle verilebilir (ör. plasebo ölçümü).
Her hikâye eğitimdeki gibi kodlanır (prepare_ft2.baslik: başlık + metin tek parça); yalnızca hikâye token'larının
NLL'i sayılır (başlık ve EOT hariç). Parçalar hikâye token sırasına göre: tum, ilk_yari, ikinci_yari, son_ucte_bir.
  tema  (--baslik tema): ΔNLL = ort. NLL(hikâye | 3 rastgele yanlış tema) − NLL(hikâye | doğru tema); >0: tema kullanılıyor
  --eot: ΔNLL = NLL(istem) − NLL(<|endoftext|> + istem); >0: EOT öneki NLL'i düşürüyor
Güven aralığı: hikâye düzeyinde eşli farkların ortalaması için %95 bootstrap (10000 örnek, sabit tohum). nat/token.
Çıktı: ekrana ve dogrulama.json'un yanına kosul_<checkpoint>_<tema|eski>[_eot].json
"""
import argparse
import hashlib
import json
import os
import random
import sys

import numpy as np
import torch
import torch.nn.functional as F
from tokenizers import Tokenizer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, "src"))
from baslangic import TEMALAR  # noqa: E402
from model import Config, TinyLM  # noqa: E402
from research.tinystories.prepare_ft2 import baslik  # noqa: E402

PARCALAR = ("tum", "ilk_yari", "ikinci_yari", "son_ucte_bir")


def baslik_bicimi(veri, tok):
    """dogrulama.json'un yanındaki val.bin'in ilk başlığında "| Tema:" varsa "tema", yoksa "eski"."""
    yol = os.path.join(os.path.dirname(os.path.abspath(veri)), "val.bin")
    if not os.path.exists(yol):
        raise SystemExit(f"{yol} yok: başlık biçimini --baslik tema|eski ile verin")
    ilk = tok.decode(np.fromfile(yol, dtype=np.uint16, count=64).tolist()).split("\n")[0]
    return "tema" if "| Tema:" in ilk else "eski"


def kodla(tok, h, tema, eot_id=None):
    """(ids, bas): eğitim satırının token'ları ve ilk hikâye token'ının indeksi; eot_id verilirse başa eklenir."""
    metin = baslik(dict(h, tema=tema), tema=tema is not None)
    enc = tok.encode(metin)
    sinir = len(metin) - len(h["metin"])
    bas = next(k for k, (s, _) in enumerate(enc.offsets) if s >= sinir)
    on = [eot_id] if eot_id is not None else []
    return on + enc.ids, bas + len(on)


@torch.no_grad()
def nll_toplu(model, diziler, B, T_max):
    """diziler: [(ids, bas)] -> her dizi için ids[bas:] token'larının NLL'i (np.ndarray). Boy sırasıyla toplanır."""
    out = [None] * len(diziler)
    sira = sorted(range(len(diziler)), key=lambda k: len(diziler[k][0]))
    for s in range(0, len(sira), B):
        grup = sira[s:s + B]
        T = min(T_max, max(len(diziler[k][0]) for k in grup)) - 1
        x = torch.zeros(len(grup), T, dtype=torch.long)
        y = torch.full((len(grup), T), -1, dtype=torch.long)
        for r, k in enumerate(grup):
            ids = diziler[k][0][:T + 1]
            x[r, :len(ids) - 1] = torch.tensor(ids[:-1])
            y[r, :len(ids) - 1] = torch.tensor(ids[1:])
        logits, _ = model(x)
        nll = F.cross_entropy(logits.reshape(-1, logits.size(-1)), y.reshape(-1), ignore_index=-1,
                              reduction="none").view(len(grup), T)
        for r, k in enumerate(grup):
            ids, bas = diziler[k]
            out[k] = nll[r, bas - 1:min(len(ids), T + 1) - 1].numpy().astype(np.float64)
    return out


def parcala(v):
    L = len(v)
    return {"tum": v.mean(), "ilk_yari": v[:L // 2].mean(), "ikinci_yari": v[L // 2:].mean(),
            "son_ucte_bir": v[(2 * L) // 3:].mean()}


def ozet(farklar, tohum=0, n_boot=10000):
    """farklar: hikâye başına eşli fark -> ortalama, %95 bootstrap aralığı, standart hata."""
    d = np.asarray(farklar)
    rng = np.random.default_rng(tohum)
    boot = d[rng.integers(0, len(d), (n_boot, len(d)))].mean(1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    return {"ort": round(float(d.mean()), 4), "ga95": [round(float(lo), 4), round(float(hi), 4)],
            "se": round(float(d.std(ddof=1) / np.sqrt(len(d))), 4), "sifiri_icermiyor": bool(lo > 0 or hi < 0)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ckpt", required=True, help="runs/ple-<etiket>-s0.pt")
    ap.add_argument("--veri", required=True, help="prepare_ft2'nin yazdığı dogrulama.json")
    ap.add_argument("--eot", action="store_true", help="EOT öneki ile öneksiz NLL'i de karşılaştır")
    ap.add_argument("--baslik", choices=["oto", "tema", "eski"], default="oto",
                    help="doğru başlık biçimi; oto: val.bin'den; eski: tema karşılaştırması yapılmaz")
    ap.add_argument("--yanlis", type=int, default=3, help="hikâye başına yanlış tema sayısı")
    ap.add_argument("--n", type=int, default=None, help="yalnız ilk N hikâye (hızlı deneme)")
    ap.add_argument("--batch", type=int, default=8)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    torch.set_num_threads(1)

    tok_yol = os.path.join(os.path.dirname(os.path.abspath(a.veri)), "tokenizer.json")
    ck = torch.load(a.ckpt, map_location="cpu", weights_only=False, mmap=True)
    sha = hashlib.sha256(open(tok_yol, "rb").read()).hexdigest()
    if ck.get("tokenizer_sha256") not in (None, sha):
        raise SystemExit(f"{tok_yol} bu checkpoint'in tokenizer'ı değil")
    cfg = Config(**ck["cfg"])
    model = TinyLM(cfg)
    model.load_state_dict(ck["state"])
    model.eval()
    tok = Tokenizer.from_file(tok_yol)
    eot_id = tok.token_to_id("<|endoftext|>")
    if a.baslik == "oto":
        a.baslik = baslik_bicimi(a.veri, tok)
        print(f"başlık biçimi (val.bin): {a.baslik}", file=sys.stderr)

    hik = json.load(open(a.veri, encoding="utf-8"))[:a.n]
    rng = random.Random(a.seed)
    dogru_tema = (lambda h: h["tema"]) if a.baslik == "tema" else (lambda h: None)
    diziler, anahtar = [], []  # anahtar: (hikâye, koşul)
    for i, h in enumerate(hik):
        kosullar = [("dogru", dogru_tema(h), None)]
        if a.baslik == "tema":
            kosullar += [(f"yanlis{j}", t, None)
                         for j, t in enumerate(rng.sample([t for t in TEMALAR if t != h["tema"]], a.yanlis))]
        if a.eot:
            kosullar.append(("eot", dogru_tema(h), eot_id))
        for ad, tema, on in kosullar:
            diziler.append(kodla(tok, h, tema, on))
            anahtar.append((i, ad))
    uzun = sum(len(ids) > cfg.seq_len for ids, _ in diziler)
    if uzun:
        print(f"UYARI: {uzun} dizi {cfg.seq_len} token'dan uzun, kesildi", file=sys.stderr)
    nll = dict(zip(anahtar, nll_toplu(model, diziler, a.batch, cfg.seq_len)))
    govde = {k: diziler[j][0][diziler[j][1]:] for j, k in enumerate(anahtar)}
    farkli = sum(govde[k] != govde[(k[0], "dogru")] for k in anahtar)
    if farkli:
        print(f"UYARI: {farkli} koşulda hikâye token'ları doğru başlıktakinden farklı kodlandı", file=sys.stderr)

    p = {i: {ad: parcala(v) for (j, ad), v in nll.items() if j == i} for i in range(len(hik))}
    sonuc = {"ckpt": a.ckpt, "veri": a.veri, "n": len(hik), "baslik": a.baslik,
             "ort_token": round(float(np.mean([len(govde[(i, "dogru")]) for i in range(len(hik))])), 1),
             "nll_dogru": {c: round(float(np.mean([p[i]["dogru"][c] for i in p])), 4) for c in PARCALAR}}
    if a.baslik == "tema":
        sonuc["tema_dNLL"] = {c: ozet([np.mean([p[i][f"yanlis{j}"][c] for j in range(a.yanlis)]) - p[i]["dogru"][c]
                                       for i in p], a.seed) for c in PARCALAR}
    if a.eot:
        sonuc["eot_dNLL"] = {c: ozet([p[i]["dogru"][c] - p[i]["eot"][c] for i in p], a.seed) for c in PARCALAR}
    ad = os.path.splitext(os.path.basename(a.ckpt))[0]
    cikti = os.path.join(os.path.dirname(os.path.abspath(a.veri)), f"kosul_{ad}_{a.baslik}{'_eot' if a.eot else ''}.json")
    json.dump(sonuc, open(cikti, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(sonuc, ensure_ascii=False, indent=1))
    print(f"-> {cikti}", file=sys.stderr)


if __name__ == "__main__":
    main()
