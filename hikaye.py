"""Run the ESP32 TinyStories model on the PC. usage: hikaye.py [prompt] [--temp T] [--seed S] [--tokens N] [--greedy]"""
import argparse, os, random, subprocess, sys
from tokenizers import Tokenizer

here = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("prompt", nargs="?", default="Once upon a time")
ap.add_argument("--temp", type=float, default=0.8)
ap.add_argument("--topk", type=int, default=40)
ap.add_argument("--tokens", type=int, default=250)
ap.add_argument("--seed", type=int, default=None)
ap.add_argument("--greedy", action="store_true", help="cihazdaki gibi: hep ayni hikaye")
a = ap.parse_args()

tok = Tokenizer.from_file(os.path.join(here, "hf/tokenizer.json"))
ids = tok.encode(a.prompt).ids
seed = a.seed if a.seed is not None else random.randrange(1 << 30)
temp = 0 if a.greedy else a.temp
eos = {tok.token_to_id(t) for t in ("<|endoftext|>", "</s>", "<eos>") if tok.token_to_id(t) is not None}

p = subprocess.Popen([os.path.join(here, "gen"), os.path.join(here, "hf/model.bin"), str(a.tokens),
                      str(temp), str(a.topk), str(seed), "1.0", *map(str, ids)], stdout=subprocess.PIPE, text=True)
out, printed = list(ids), a.prompt
sys.stdout.write(printed)
for line in p.stdout:
    t = int(line)
    if t in eos: p.kill(); break
    out.append(t)
    text = tok.decode(out)
    sys.stdout.write(text[len(printed):]); sys.stdout.flush(); printed = text
p.wait()
print(f"\n\n[seed={seed}]")
