"""Train one ablation arm and report val loss at matched core-parameter budget."""

import argparse
import hashlib
import json
import math
import os
import time

import numpy as np
import torch
import torch.nn.functional as F

from model import Config, TinyLM, make_model

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# A vocabulary variant keeps its tokenizer and token bins together.
DATA = Path(os.environ.get("TS_DATA", ROOT / "data" / "tinystories"))
RUNS = str(ROOT / "runs")


def variant_dir(vocab_size):
    return DATA / f"vocab-{vocab_size}"


def get_device():
    if torch.backends.mps.is_available():
        return "mps"
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"


def hikaye_araliklari(dataset, split):
    """prepare_ft2'nin yazdığı oyuncak hikâyesi aralıkları [bas, son) (int64, artan) ya da (None, None).
    bas: başlıktan önceki EOT'nin konumu (yoksa başlığın başı), son: hikâyenin kendi EOT'sinin bir ötesi."""
    b, s = dataset / f"{split}_bas.npy", dataset / f"{split}_son.npy"
    if not (b.exists() and s.exists()):
        return None, None
    bas, son = np.load(b).astype(np.int64), np.load(s).astype(np.int64)
    data = np.memmap(dataset / f"{split}.bin", dtype=np.uint16, mode="r")
    # .bin yeniden yazılıp .npy eski kaldıysa aralıklar yanlış yere düşer: her hikâye aynı token'la (EOT) bitmeli
    if len(bas) != len(son) or (len(son) and (son[-1] > len(data) or len(np.unique(data[son - 1])) != 1)):
        raise SystemExit(f"{b.name}/{s.name} {split}.bin ile uyuşmuyor; prepare_ft2'yi yeniden koşun")
    return bas, son


def hizala_basa(ix, bas, son):
    """--hizala toy (E2): bir oyuncak hikâyesinin [bas_j, son_j) aralığına düşen başlangıç bas_j'ye çekilir;
    bas_j <= i olduğundan i + seq_len + 1 <= len sınırı korunur. Genel metne düşenler değişmez."""
    if not len(bas):
        return ix
    j = np.searchsorted(bas, ix, side="right") - 1
    jj = np.maximum(j, 0)
    return np.where((j >= 0) & (ix < son[jj]), bas[jj], ix)


class HizaliDogrulama:
    """val_hizali (E2): her doğrulama hikâyesi kendi başından (başlıktan önceki EOT) okunur ve yalnızca gövde
    token'larının (başlığı bitiren "\n\n"den sonrası, son EOT hariç) kaybı sayılır; hikâyenin ilk/orta/son
    üçte biri ayrıca. Token ağırlıklı ortalama; seq_len'e sığmayan kuyruk sayılmaz. Rastgelelik kullanmaz."""

    def __init__(self, dataset, seq_len, nl):
        data = np.memmap(dataset / "val.bin", dtype=np.uint16, mode="r")
        bas, son = hikaye_araliklari(dataset, "val")
        self.diziler = []
        for b, s in zip(bas, son):
            seq = np.asarray(data[b:s], dtype=np.int64)
            w = np.flatnonzero((seq[:-1] == nl) & (seq[1:] == nl))
            if not len(w):
                continue
            k = int(w[0]) + 2          # gövdenin ilk token'ı
            n = len(seq) - 1 - k       # gövde token sayısı (EOT hariç)
            if n < 3:
                continue
            r = np.arange(n)
            ucte = np.full(len(seq), -1, dtype=np.int64)
            ucte[k:k + n] = (r >= n // 3).astype(np.int64) + (r >= (2 * n) // 3)
            self.diziler.append((seq[:seq_len + 1], ucte[:seq_len + 1]))

    @torch.no_grad()
    def __call__(self, model, batch_size, device):
        model.eval()
        top, say = np.zeros(3), np.zeros(3)
        for i in range(0, len(self.diziler), batch_size):
            grup = self.diziler[i:i + batch_size]
            T = max(len(q) for q, _ in grup) - 1
            x = np.zeros((len(grup), T), dtype=np.int64)
            y = np.full((len(grup), T), -1, dtype=np.int64)
            u = np.full((len(grup), T), -1, dtype=np.int64)
            for r, (q, ucte) in enumerate(grup):
                x[r, :len(q) - 1], y[r, :len(q) - 1], u[r, :len(q) - 1] = q[:-1], q[1:], ucte[1:]
            logits, _ = model(torch.from_numpy(x).to(device))
            nll = F.cross_entropy(logits.reshape(-1, logits.size(-1)).float(),
                                  torch.from_numpy(y).to(device).reshape(-1), ignore_index=-1,
                                  reduction="none").view(len(grup), T).cpu().numpy()
            for c in range(3):
                top[c] += nll[u == c].sum()
                say[c] += (u == c).sum()
        model.train()
        return {"tum": float(top.sum() / say.sum()), "ilk_ucte": float(top[0] / say[0]),
                "orta_ucte": float(top[1] / say[1]), "son_ucte": float(top[2] / say[2])}


class Batcher:
    def __init__(self, split, batch_size, seq_len, device, dataset, seed=0, hizala=None):
        # The bins are uint16. Reading a wider vocabulary through that dtype
        # yields plausible token ids rather than an error, so check before
        # opening.
        self.data = np.memmap(dataset / f"{split}.bin", dtype=np.uint16, mode="r")
        self.bs, self.sl, self.device = batch_size, seq_len, device
        # Batch order is part of the run. Without the seed here, torch.manual_seed
        # fixes initialisation only and two runs at the same --seed still see
        # different data order. Validation keeps a fixed stream so every arm is
        # scored on identical batches.
        self.rng = np.random.default_rng(1234 if split == "val" else seed)
        self.bas = self.son = None
        if hizala == "toy":
            self.bas, self.son = hikaye_araliklari(dataset, split)
            if self.bas is None:
                raise SystemExit(f"--hizala toy: {dataset}/{split}_bas.npy yok; veriyi prepare_ft2 ile yeniden hazırlayın")

    def __call__(self):
        ix = self.rng.integers(0, len(self.data) - self.sl - 1, self.bs)
        if self.bas is not None:
            ix = hizala_basa(ix, self.bas, self.son)
        x = np.stack([self.data[i : i + self.sl] for i in ix]).astype(np.int64)
        y = np.stack([self.data[i + 1 : i + 1 + self.sl] for i in ix]).astype(np.int64)
        return torch.from_numpy(x).to(self.device), torch.from_numpy(y).to(self.device)


@torch.no_grad()
def evaluate(model, batcher, iters):
    model.eval()
    batcher.rng = np.random.default_rng(1234)  # same val batches for every arm
    losses = [model(*batcher())[1].item() for _ in range(iters)]
    model.train()
    return sum(losses) / len(losses)


def lr_at(step, total, peak, warmup):
    if step < warmup:
        return peak * (step + 1) / warmup
    p = (step - warmup) / max(1, total - warmup)
    return 0.1 * peak + 0.9 * peak * 0.5 * (1 + math.cos(math.pi * p))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--arm",
        required=True,
        choices=["baseline", "ple", "ple_notable", "fatembed", "bigcore"],
    )
    ap.add_argument("--target-core", type=int, default=1_500_000)
    ap.add_argument("--steps", type=int, default=4000)
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--seq-len", type=int, default=512)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--warmup", type=int, default=200)
    ap.add_argument("--eval-every", type=int, default=250)
    ap.add_argument("--eval-iters", type=int, default=40)
    ap.add_argument("--ple-dim", type=int, default=64)
    ap.add_argument("--d-model", type=int, default=128)
    ap.add_argument("--n-layers", type=int, default=6)
    ap.add_argument("--n-heads", type=int, default=4)
    ap.add_argument("--fixed-ffn", type=int, default=None,
                    help="pin ffn_hidden and skip the core solver (table-scaling sweep)")
    # Published experiments always pass --vocab; the default is for ad-hoc runs.
    ap.add_argument("--vocab", type=int, default=32768)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--tag", default="")
    ap.add_argument("--ckpt-every", type=int, default=250,
                    help="write a resumable checkpoint every N steps; a rerun with the same "
                         "arguments continues from it")
    ap.add_argument("--init-from", default=None,
                    help="start from another run's weights (e.g. fine-tuning on a new dataset)")
    ap.add_argument("--qat-emb", action="store_true",
                    help="quantization-aware training for the tied embedding/head: the forward pass "
                         "sees it on the exporter's int4 grid (straight-through gradients), so the "
                         "model adapts to the precision the device actually stores")
    ap.add_argument("--hizala", choices=["toy"], default=None,
                    help="E2: a training window that starts inside a toy story is moved to that story's "
                         "start (the EOT before its header); general-text windows are unchanged. Needs "
                         "train_bas.npy/train_son.npy from prepare_ft2")
    args = ap.parse_args()

    # Before anything expensive: the tokenizer that produced these bins. Its
    # hash is what lets the exporter and sampler refuse a mismatched tokenizer
    # later, and a checkpoint written without it cannot be tied to one. Failing
    # here costs nothing; failing after a 30-minute run costs the run.
    if not 0 < args.vocab <= 65536:
        raise SystemExit(f"--vocab must be 1..65536; the token bins are uint16 "
                         f"and are memmapped as uint16")

    dataset = variant_dir(args.vocab)
    tok_path = dataset / "tokenizer.json"
    if not os.path.exists(tok_path):
        raise SystemExit(
            f"{tok_path} missing. The bins this run trains on came from it, and "
            f"without its hash the checkpoint cannot be tied to a tokenizer. "
            f"Run: python -m research.tinystories.prepare --vocab {args.vocab}")
    tok_sha = hashlib.sha256(open(tok_path, "rb").read()).hexdigest()

    torch.manual_seed(args.seed)
    device = get_device()
    os.makedirs(RUNS, exist_ok=True)

    base = Config(seq_len=args.seq_len, ple_dim=args.ple_dim, vocab_size=args.vocab,
                  d_model=args.d_model, n_layers=args.n_layers, n_heads=args.n_heads)
    model = make_model(args.arm, args.target_core, base, fixed_ffn=args.fixed_ffn).to(device)
    budget = model.param_budget()
    cfg = model.cfg

    if args.qat_emb:
        import torch.nn.functional as F

        def fake_int4(w, group=128):
            # Mirrors export.quant_pack: symmetric int4 in [-7, 7], one fp16 scale per
            # row-group of `group` columns.
            rows, cols = w.shape
            pad = (-cols) % group
            x = F.pad(w, (0, pad)).reshape(rows, -1, group)
            sc = (x.abs().amax(-1, keepdim=True) / 7).clamp_min(1e-8).half().float()
            q = (torch.clamp(torch.round(x / sc), -7, 7) * sc).reshape(rows, -1)[:, :cols]
            return w + (q - w).detach()

        emb, head = model.tok_emb, model.head
        emb.forward = lambda idx: F.embedding(idx, fake_int4(emb.weight))
        head.forward = lambda h: F.linear(h, fake_int4(head.weight))
        print("QAT: tok_emb/head see int4 weights in the forward pass")

    # No weight decay on 1-D params (norms) or on lookup tables.
    decay, no_decay = [], []
    for n, p in model.named_parameters():
        (no_decay if p.ndim < 2 or "table" in n or "tok_emb" in n else decay).append(p)
    opt = torch.optim.AdamW(
        [{"params": decay, "weight_decay": 0.1}, {"params": no_decay, "weight_decay": 0.0}],
        lr=args.lr,
        betas=(0.9, 0.95),
    )

    train_b = Batcher("train", args.batch_size, args.seq_len, device, dataset,
                      seed=args.seed, hizala=args.hizala)
    val_b = Batcher("val", args.batch_size, args.seq_len, device, dataset)
    # val_hizali: only when prepare_ft2 wrote the story spans; the "val" metric itself is unchanged.
    val_hiz = None
    if hikaye_araliklari(dataset, "val")[0] is not None:
        from tokenizers import Tokenizer
        nl = Tokenizer.from_file(str(tok_path)).encode("\n").ids
        if len(nl) == 1:
            val_hiz = HizaliDogrulama(dataset, args.seq_len, nl[0])

    name = f"{args.arm}{'-' + args.tag if args.tag else ''}-s{args.seed}"
    history, best = [], float("inf")
    t0 = time.time()
    ckpt_path = os.path.join(RUNS, f"{name}.ckpt.pt")
    progress_path = os.path.join(RUNS, f"{name}.progress.json")
    start_step, elapsed_before = 0, 0.0

    if args.init_from:
        init = torch.load(args.init_from, map_location=device, weights_only=False)
        if init.get("tokenizer_sha256") != tok_sha:
            raise SystemExit(f"--init-from {args.init_from} was trained with a different tokenizer")
        model.load_state_dict(init["state"])
        print(f"initialised from {args.init_from}")

    # Resume: the batch stream restarts from a step-derived seed, so a resumed run sees
    # different (but equally random) batches than an uninterrupted one would have.
    if os.path.exists(ckpt_path):
        ck = torch.load(ckpt_path, map_location=device, weights_only=False)
        if ck.get("tokenizer_sha256") != tok_sha or ck.get("steps") != args.steps:
            raise SystemExit(f"{ckpt_path} belongs to a different run (tokenizer or --steps "
                             f"differ); move it away to start fresh")
        model.load_state_dict(ck["state"])
        opt.load_state_dict(ck["opt"])
        start_step, history, best = ck["step"] + 1, ck["history"], ck["best"]
        elapsed_before = ck.get("elapsed", 0.0)
        train_b.rng = np.random.default_rng(args.seed * 1_000_003 + start_step)
        print(f"resumed {name} at step {start_step}")

    def save_ckpt(step):
        tmp = ckpt_path + ".tmp"
        torch.save({"state": model.state_dict(), "opt": opt.state_dict(), "step": step,
                    "steps": args.steps, "history": history, "best": best,
                    "elapsed": elapsed_before + time.time() - t0,
                    "tokenizer_sha256": tok_sha, "cfg": cfg.__dict__}, tmp)
        os.replace(tmp, ckpt_path)

    speed = None  # EMA of seconds per step, for the progress file
    last_t = time.time()

    def write_progress(step, loss, status="training"):
        tmp = progress_path + ".tmp"
        with open(tmp, "w") as f:
            json.dump({"name": name, "status": status, "step": step, "steps": args.steps,
                       "train_loss": loss, "sec_per_step": speed,
                       "eta_seconds": speed * (args.steps - step - 1) if speed else None,
                       "elapsed": elapsed_before + time.time() - t0,
                       "updated": time.time(), "history": history,
                       "params": budget}, f)
        os.replace(tmp, progress_path)

    for step in range(start_step, args.steps):
        lr = lr_at(step, args.steps, args.lr, args.warmup)
        for g in opt.param_groups:
            g["lr"] = lr
        x, y = train_b()
        _, loss = model(x, y)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()

        if step % args.eval_every == 0 or step == args.steps - 1:
            vl = evaluate(model, val_b, args.eval_iters)
            best = min(best, vl)
            tok = (step + 1) * args.batch_size * args.seq_len
            history.append({"step": step, "tokens": tok, "train": loss.item(), "val": vl})
            print(
                f"{name} step {step:5d} | tok {tok / 1e6:6.1f}M | train {loss.item():.4f} "
                f"| val {vl:.4f} | ppl {math.exp(vl):7.2f} | {time.time() - t0:5.0f}s",
                flush=True,
            )
            if val_hiz is not None:
                vh = val_hiz(model, args.batch_size, device)
                history[-1]["val_hizali"] = vh
                print(f"{name} step {step:5d} | val_hizali {vh['tum']:.4f} | ilk/orta/son üçte "
                      f"{vh['ilk_ucte']:.4f} {vh['orta_ucte']:.4f} {vh['son_ucte']:.4f}", flush=True)

        now = time.time()
        dt, last_t = now - last_t, now
        if dt < 60:  # ignore gaps from sleep/eval spikes in the ETA
            speed = dt if speed is None else 0.95 * speed + 0.05 * dt
        if step % 10 == 0 or step == args.steps - 1:
            write_progress(step, loss.item())
        if (step + 1) % args.ckpt_every == 0 and step != args.steps - 1:
            save_ckpt(step)

    result = {
        "arm": args.arm,
        "seed": args.seed,
        "tag": args.tag,
        "config": {k: v for k, v in cfg.__dict__.items()},
        "training": {
            "batch_size": args.batch_size,
            "steps": args.steps,
            "lr": args.lr,
            "warmup": args.warmup,
            "eval_every": args.eval_every,
            "eval_iters": args.eval_iters,
            "target_core": args.target_core,
            "fixed_ffn": args.fixed_ffn,
            "seed": args.seed,
        },
        "tokenizer_sha256": tok_sha,
        "params": budget,
        "final_val": history[-1]["val"],
        "best_val": best,
        "final_ppl": math.exp(history[-1]["val"]),
        "tokens_seen": args.steps * args.batch_size * args.seq_len,
        "steps": args.steps,
        "wall_seconds": time.time() - t0,
        "history": history,
    }
    with open(os.path.join(RUNS, f"{name}.json"), "w") as f:
        json.dump(result, f, indent=2)
    # Identity and schedule live only in the filename and the sidecar JSON
    # otherwise, so a checkpoint copied over another name, or trained on a
    # different schedule, would pass every content check.
    torch.save({"cfg": cfg.__dict__, "state": model.state_dict(),
                "tokenizer_sha256": tok_sha,
                "seed": args.seed, "tag": args.tag, "name": name,
                "training": result["training"]},
               os.path.join(RUNS, f"{name}.pt"))
    write_progress(args.steps - 1, history[-1]["train"], status="done")
    if os.path.exists(ckpt_path):
        os.remove(ckpt_path)
    print(f"{name} DONE core={budget['core']:,} table={budget['table']:,} "
          f"val={result['final_val']:.4f} ppl={result['final_ppl']:.2f}")


if __name__ == "__main__":
    main()
