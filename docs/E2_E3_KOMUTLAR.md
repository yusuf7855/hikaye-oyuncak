# E2 / E3 komutları (R tabanı c2ft hazır olduktan sonra)

> Birleşik testin çıktısından; ayrıntılar ve uyarılar için docs/OLAY_ORGUSU_PLANI.md ve docs/DENEYLER.md.

## Commands (after R = c2ft exists)
```
R_ARGS="--bolme data/bolme.json --blok-eot"   # exactly R's prepare_ft2 args
rm -f gen && cc -O3 -o gen runtime/host_verify/gen.c -lm   # adds -S/-W; identical output without them

# E2
EK_TRAIN='--hizala toy' PAKET='--satir-yasak --eot-on' ./ince_ayar_c2.sh c2ft_hiz $R_ARGS
.venv/bin/python degerlendirme/uret.py hf_c2ft_hiz c2ft_hiz --aday 8 --satir-yasak --eot-on
.venv/bin/python degerlendirme/otomatik.py hf_c2ft_hiz --ad c2ft_hiz --aday 8 --satir-yasak --eot-on
.venv/bin/python degerlendirme/olay.py hf_c2ft_hiz/adaylar_c2ft_hiz.json --model hf_c2ft
.venv/bin/python degerlendirme/hakem.py hazirla c2ft_hiz
.venv/bin/python degerlendirme/ikili.py hazirla c2ft_hiz c2ft    # later: ikili.py ozet c2ft_hiz c2ft
.venv/bin/python -c "import json
for t in ('c2ft','c2ft_hiz'): h=json.load(open(f'runs/ple-{t}-s0.json'))['history'][-1]; print(t, h['val'], h.get('val_hizali'))"
# optional ΔNLL stand-in (run for both c2ft and c2ft_hiz):
PYTHONPATH=src .venv/bin/python degerlendirme/kosul_duyarlilik.py --ckpt runs/ple-c2ft_hiz-s0.pt --veri data/tr_c2ft_hiz/vocab-16384/dogrulama.json --baslik eski --plan --plan-etiket data/oyuncak_plan/plan.jsonl

# E3 (EK_TRAIN='--hizala toy' only if E2 won)
EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on' ./ince_ayar_c2.sh c2ft_plan $R_ARGS --plan data/oyuncak_plan/plan.jsonl --plan-orani 0.7
D=data/tr_c2ft_plan/vocab-16384/dogrulama.json
.venv/bin/python degerlendirme/uret.py hf_c2ft_plan c2ft_plan_a --aday 8 --satir-yasak --eot-on                        # (a) without plan
.venv/bin/python degerlendirme/uret.py hf_c2ft_plan c2ft_plan --aday 8 --baslik plan --satir-yasak --eot-on            # (b)
.venv/bin/python degerlendirme/otomatik.py hf_c2ft_plan --ad c2ft_plan_a --aday 8 --satir-yasak --eot-on
.venv/bin/python degerlendirme/otomatik.py hf_c2ft_plan --ad c2ft_plan --aday 8 --baslik plan --satir-yasak --eot-on
.venv/bin/python degerlendirme/uret.py hf_c2ft_plan c2ft_plan_dog --aday 8 --baslik plan --dogrulama $D --satir-yasak --eot-on                           # (b) on val cases
.venv/bin/python degerlendirme/uret.py hf_c2ft_plan c2ft_plan_oracle --aday 8 --baslik plan --plan-kosul oracle --dogrulama $D --satir-yasak --eot-on    # (c)
for a in c2ft_plan_a c2ft_plan c2ft_plan_dog c2ft_plan_oracle; do .venv/bin/python degerlendirme/olay.py hf_c2ft_plan/adaylar_$a.json --model hf_c2ft; done
PYTHONPATH=src .venv/bin/python degerlendirme/kosul_duyarlilik.py --ckpt runs/ple-c2ft_plan-s0.pt --veri $D --plan
PYTHONPATH=src .venv/bin/python degerlendirme/kosul_duyarlilik.py --ckpt runs/ple-c2ft-s0.pt --veri data/tr_c2ft/vocab-16384/dogrulama.json --baslik eski --plan --plan-etiket data/oyuncak_plan/plan.jsonl   # placebo
.venv/bin/python degerlendirme/hakem.py hazirla c2ft_plan
.venv/bin/python degerlendirme/ikili.py hazirla c2ft_plan <önceki_en_iyi>
.venv/bin/python degerlendirme/ikili.py hazirla c2ft_plan_a <önceki_en_iyi>
```

How to read the E3 results:
- **`plan_uyum_%` ≥ 70:** a same-theme but wrong plan already scores about 51% on real stories, and a random plan 11.6%.
- **Last-third `plan_dNLL` ≥ 0.03:** c2ara, which never saw plans, already shows about 0.004 there (0.022 over the whole story), so read E3's number against that placebo.
