"""Eğitilmiş bir modeli depoya kaydet: modeller/<etiket>/.

Kullanım: .venv/bin/python modeller/kaydet.py <etiket> [<etiket> ...]
  <etiket>: runs/ple-<etiket>-s0.pt (PyTorch) ve varsa hf_<etiket>/ (kartta çalışan dışa aktarım)
Yazar:
  agirliklar_fp16.pt  ağırlıklar fp16 (--init-from ile ince ayara devam edilebilir; fp32 ile kayıp farkı ~1e-5)
  model.bin           4-bit ESP32 modeli (export.py çıktısı), golden.txt ile birlikte
  bilgi.json          yapılandırma, adım, tokenizer özeti, son doğrulama kaybı
ve modeller/SHA256SUMS'u yeniler. Tokenizer tüm C2 modellerinde aynı: modeller/c2_tokenizer.json.
"""
import hashlib
import json
import os
import shutil
import sys

import torch

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BURA = os.path.join(KOK, "modeller")


def kaydet(etiket):
    hedef = os.path.join(BURA, etiket)
    os.makedirs(hedef, exist_ok=True)
    pt = os.path.join(KOK, "runs", f"ple-{etiket}-s0.pt")
    bilgi = {"etiket": etiket}
    if os.path.exists(pt):
        ck = torch.load(pt, map_location="cpu", weights_only=False)
        yeni = {"state": {k: (v.half() if v.is_floating_point() else v) for k, v in ck["state"].items()},
                "cfg": ck["cfg"], "tokenizer_sha256": ck["tokenizer_sha256"]}
        torch.save(yeni, os.path.join(hedef, "agirliklar_fp16.pt"))
        ilerleme = os.path.join(KOK, "runs", f"ple-{etiket}-s0.progress.json")
        son = json.load(open(ilerleme))["history"][-1] if os.path.exists(ilerleme) else None
        bilgi.update({"cfg": ck["cfg"], "tokenizer_sha256": ck["tokenizer_sha256"], "son_olcum": son})
    hf = os.path.join(KOK, f"hf_{etiket}")
    for ad in ("model.bin", "golden.txt"):
        if os.path.exists(os.path.join(hf, ad)):
            shutil.copyfile(os.path.join(hf, ad), os.path.join(hedef, ad))
    json.dump(bilgi, open(os.path.join(hedef, "bilgi.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(etiket, sorted(os.listdir(hedef)))


def ozetle():
    satirlar = []
    for kok, _, dosyalar in sorted(os.walk(BURA)):
        for ad in sorted(dosyalar):
            if ad in ("SHA256SUMS",) or ad.endswith((".py", ".md")) or "__pycache__" in kok:
                continue
            yol = os.path.join(kok, ad)
            h = hashlib.sha256(open(yol, "rb").read()).hexdigest()
            satirlar.append(f"{h}  {os.path.relpath(yol, BURA)}")
    open(os.path.join(BURA, "SHA256SUMS"), "w").write("\n".join(satirlar) + "\n")


if __name__ == "__main__":
    for e in sys.argv[1:]:
        kaydet(e)
    ozetle()
