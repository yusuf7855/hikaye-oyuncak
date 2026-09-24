"""Üretim ayarı ızgarası: uydurma kelime oranı + kural cezası (hakemsiz, hızlı)."""
import itertools, json, pickle, re, sys, os
sys.path.insert(0, "degerlendirme"); sys.path.insert(0, ".")
from tokenizers import Tokenizer
from uret import test_seti, uret
from sec import cezalar, kucuk
model = sys.argv[1] if len(sys.argv) > 1 else "hf_v2"
tok = Tokenizer.from_file(f"{model}/tokenizer.json")
sozluk = pickle.load(open("degerlendirme/sozluk.pkl", "rb"))
vakalar = test_seti()
def olc(temp, rep, k=40):
    bil = top = ceza = 0
    for i, (kim, yer) in enumerate(vakalar):
        _, metin, n, lp, bitti = uret(model, kim, yer, 500 + i, temp, rep, tok)
        w = re.findall(r"[a-zçğıöşüâîû]+", kucuk(metin)); top += len(w); bil += sum(x not in sozluk for x in w)
        ceza += sum(p for p, _ in cezalar(metin, kim, n, bitti=bitti))
    return 100 * bil / max(1, top), ceza / len(vakalar)
for temp, rep in itertools.product([0.4, 0.55, 0.7], [1.0, 1.05, 1.1, 1.15]):
    u, c = olc(temp, rep)
    print(f"temp {temp:<4} rep {rep:<4}  uydurma kelime %{u:.2f}   kural cezası/hikâye {c:.2f}", flush=True)
