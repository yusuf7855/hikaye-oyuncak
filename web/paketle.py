"""Dışa aktarılmış bir modeli tarayıcı test arayüzü için paketle.

Kullanım: .venv/bin/python web/paketle.py <sürüm> <model_dizini>
  model_dizini: model.bin + tokenizer.json (export.py çıktısı, ör. hf_c2ft)
Çıktı: web/m/<sürüm>/model.b64.txt (gzip + base64 model.bin; yayın yeri ikili dosya sunmuyor) ve meta.json
  meta.json: token tablosu (çözmek için), her figür/yer birleşimi için başlık token'ları
  (baslangic.prompt_idler ile, eğitimdeki gibi), yasaklanacak isim token'ları, katalog.
Arayüz kendi tokenizer'ını taşımaz: kodlanması gereken her şey (başlıklar, isimler) burada hazırlanır.
"""
import base64
import gzip
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from tokenizers import Tokenizer  # noqa: E402
from baslangic import KAR, KATALOG, SIRA, YABANCI, prompt_idler  # noqa: E402


def isim_idleri(tok, isim):
    """Bir ismi üretmeyi engelleyen token'lar: ismin tek token hâli ya da (çok parçalıysa) büyük harfli
    ilk parçası - baslangic.yasak_idler ile aynı kural."""
    idler = set()
    for v in (" " + isim, isim):
        enc = tok.encode(v).ids
        ilk = tok.decode([enc[0]]).strip()
        if len(enc) == 1 or (ilk[:1].isupper() and len(ilk) >= 3):
            idler.add(enc[0])
    return sorted(idler)


def main():
    surum, model_dir = sys.argv[1], sys.argv[2]
    tok = Tokenizer.from_file(os.path.join(model_dir, "tokenizer.json"))
    out = os.path.join(HERE, "m", surum)
    os.makedirs(out, exist_ok=True)
    ham = open(os.path.join(model_dir, "model.bin"), "rb").read()
    with open(os.path.join(out, "model.b64.txt"), "wb") as f:
        f.write(base64.b64encode(gzip.compress(ham, 9, mtime=0)))

    vocab = [None] * tok.get_vocab_size()
    for s, i in tok.get_vocab().items():
        vocab[i] = s
    yerler = [y["kimlik"] for y in KATALOG["yerler"]]
    prompts = {}
    for i, a in enumerate(SIRA):
        for grup in [[a]] + [[a, b] for b in SIRA[i + 1:]]:
            for y in yerler:
                prompts[",".join(grup) + "|" + y] = prompt_idler(tok, grup, y)
    isimler = [k["isim"] for k in KAR.values()] + YABANCI
    meta = {
        "surum": surum,
        "eot": tok.token_to_id("<|endoftext|>"),
        "vocab": vocab,
        "prompts": prompts,
        "isim_yasak": {n: isim_idleri(tok, n) for n in isimler},
        "yabanci": YABANCI,
    }
    json.dump(meta, open(os.path.join(out, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False,
              separators=(",", ":"))
    # Uydurma kelime kontrolü için sözlük (degerlendirme/sozluk_olustur.py çıktısı), düz metin
    pkl = os.path.join(ROOT, "degerlendirme", "sozluk.pkl")
    if os.path.exists(pkl):
        import pickle
        with open(os.path.join(HERE, "sozluk.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(sorted(pickle.load(open(pkl, "rb")))))
    else:
        print("UYARI: degerlendirme/sozluk.pkl yok; arayüz uydurma kelime cezası vermeyecek")
    print(f"{out}: model {len(ham) / 1e6:.1f} MB -> model.b64.txt "
          f"{os.path.getsize(os.path.join(out, 'model.b64.txt')) / 1e6:.1f} MB, "
          f"meta.json {os.path.getsize(os.path.join(out, 'meta.json')) / 1e6:.2f} MB, {len(prompts)} başlık")


if __name__ == "__main__":
    main()
