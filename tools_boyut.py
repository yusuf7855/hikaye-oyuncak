"""Aday model boyutları: parametre, flash boyutu ve ESP32-S3 hız TAHMİNİ.

Hız, RESULTS.md'deki gerçek ölçümle (V_out=25353, d=96, L=6, F=66, P=128 → 94.9 ms/token:
head 59.4 | attn 20.5 | ffn 6.5 | ple 6.4 | input 2.2) orantılanarak tahmin edilir. Head PSRAM
bant genişliğiyle sınırlı (V·d bayt int8), diğerleri MAC sayısıyla ölçeklenir. Kartta ölçülene
kadar ±%30 belirsiz kabul et.
"""
import math, sys
sys.path.insert(0, "src")
from model import Config, TinyLM

FLASH = 15_597_568          # model bölümü (partitions.csv)
T = 150                     # attention için ortalama bağlam uzunluğu
REF = dict(V=25353, d=96, L=6, F=66, P=128)

def ms(V, d, L, F, P):
    r = REF
    head = 59.4 * (V * d) / (r["V"] * r["d"])
    attn = 20.5 * (4 * d * d * L + 2 * T * d * L) / (4 * r["d"] ** 2 * r["L"] + 2 * T * r["d"] * r["L"])
    ffn = 6.5 * (d * F * L) / (r["d"] * r["F"] * r["L"])
    ple = 6.4 * (d * P * L) / (r["d"] * r["P"] * r["L"])
    return head + attn + ffn + ple + 2.2, head

def q4(rows, cols):  # int4 + satır başına ceil(cols/128) fp16 ölçek
    return rows * math.ceil(cols / 2) + rows * math.ceil(cols / 128) * 2

def flash(m, cfg):
    tot = 0
    for n, p in m.named_parameters():
        if n == "head.weight" or p.ndim < 2:
            tot += 0 if n == "head.weight" else p.numel() * 4
        else:
            tot += q4(p.shape[0], p.shape[1])
    return tot + 56

adaylar = [("şu anki (TR)", 32768, 96, 6, 66, 128), ("A", 32768, 128, 8, 256, 64), ("B", 16384, 128, 8, 256, 128),
           ("C", 16384, 128, 10, 320, 64), ("D", 16384, 160, 8, 320, 64), ("E", 24576, 128, 8, 256, 64),
           ("F", 16384, 144, 10, 288, 64)]
print(f"{'aday':14}{'V':>7}{'d':>5}{'L':>4}{'F':>5}{'P':>5}{'çekirdek':>11}{'tablo':>12}{'flash MB':>10}{'ms/tok':>8}{'tok/s':>7}  sığar?")
for ad, V, d, L, F, P in adaylar:
    cfg = Config(arm="ple", vocab_size=V, d_model=d, n_layers=L, ffn_hidden=F, ple_dim=P, n_heads=4)
    m = TinyLM(cfg); b = m.param_budget()
    t, head = ms(V, d, L, F, P); fb = flash(m, cfg)
    print(f"{ad:14}{V:>7}{d:>5}{L:>4}{F:>5}{P:>5}{b['core']:>11,}{b['table']:>12,}{fb/1e6:>10.2f}{t:>8.0f}{1000/t:>7.1f}  {'evet' if fb <= FLASH else 'HAYIR'}")
