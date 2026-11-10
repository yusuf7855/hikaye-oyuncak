"""kws.h denemesi: C çıkarımı PyTorch int8 başvurusuyla (ses/kws/ortak.py) aynı mı?

  .venv/bin/python firmware/hikaye_oyuncak/tools/kws_test.py [--model ses_kws_veri/calisma/qat.pt] [--ses a.wav]

--model yoksa eğitilmemiş (ölçekleri kalibre) rastgele model denenir. --ses yoksa sınama verisinden (varsa) ya da
yapay sesten 40 sn'lik bir akış kurulur. Denetlenenler:
  1. yalnız ağ: aynı int8 öznitelikle C logitleri == PyTorch tamsayı logitleri (bit bit)
  2. öznitelik: C (float32 FFT) ile numpy arasında farklı int8 değer oranı (yuvarlama sınırı; çok küçük olmalı)
  3. uçtan uca (ses -> logit): argmax eşitliği, en büyük logit farkı
  4. olaylar: C (kare kare ve rastgele büyük parçalarla) == Python SonIslem
  5. C++ olarak da derlenir (.ino ile aynı derleyici kipi)
Ayrıca sahte nicemlemeli PyTorch modelinin (QAT) tamsayı başvurusuyla argmax uyumu yazılır.
"""
import argparse
import glob
import io
import os
import pickle
import subprocess
import sys
import tempfile

import numpy as np
import torch

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.abspath(os.path.join(BURASI, "..", "..", ".."))
sys.path.insert(0, os.path.join(KOK, "ses", "kws"))
import ortak as O  # noqa: E402
import disa_aktar as D  # noqa: E402


def deneme_sesi(sure_s=40, tohum=0):
    rng = np.random.default_rng(tohum)
    n = sure_s * O.SR
    x = rng.normal(0, 1, n) * 10 ** (rng.uniform(-4, -2.5))
    parcalar = sorted(glob.glob(os.path.join(KOK, "ses_kws_veri", "ham", "poz_sinama_*.pkl")))
    if parcalar:
        import soundfile as sf
        d = pickle.load(open(parcalar[0], "rb"))
        t = int(0.5 * O.SR)
        for o in d:
            v = o["varyant"][-1]
            y, _ = sf.read(io.BytesIO(v["flac"]), dtype="float32")
            if t + len(y) >= n:
                break
            x[t: t + len(y)] += y * 10 ** rng.uniform(-1.3, -0.3)
            t += len(y) + int(rng.uniform(0.2, 1.5) * O.SR)
        kaynak = os.path.basename(parcalar[0])
    else:
        t = np.arange(n) / O.SR
        for k in range(12):
            a = int(rng.uniform(0, sure_s - 1) * O.SR)
            L = int(rng.uniform(0.2, 1.0) * O.SR)
            f0 = rng.uniform(150, 400)
            seg = sum(np.sin(2 * np.pi * f0 * h * t[:L] * (1 + 0.3 * t[:L])) / h for h in range(1, 8))
            x[a: a + L] += seg * np.hanning(L) * 10 ** rng.uniform(-1.5, -0.5) / 3
        kaynak = "yapay"
    x[int(n * 0.9):] *= 30  # sona doğru kırpılma
    return (np.clip(x, -1, 1) * 32767).astype(np.int16), kaynak


def calistir(komut):
    r = subprocess.run(komut, capture_output=True, text=True)
    if r.returncode:
        print("$", " ".join(komut), "\n", r.stdout, r.stderr)
        sys.exit(r.returncode)
    return r.stdout + r.stderr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=None)
    ap.add_argument("--ses", default=None, help="wav (16 kHz mono) ya da ham int16")
    ap.add_argument("--dizin", default=None)
    a = ap.parse_args()
    dz = a.dizin or tempfile.mkdtemp(prefix="kws_test_")
    os.makedirs(dz, exist_ok=True)

    if a.model:
        net, k = D.yukle(a.model)
        net.qat_ac(True)
        son = k.get("son_islem", dict(esik_uyan=0.6, esik_komut=0.5, yumusat=4))
    else:
        net = D.rastgele_net()
        son = dict(esik_uyan=0.6, esik_komut=0.5, yumusat=4)
    net.eval()
    baslik = os.path.join(dz, "kws_model.h")
    D.baslik_yaz(net, son, baslik, "kws_test")
    tm = O.tamsayi_model(net)

    if a.ses:
        if a.ses.endswith(".wav"):
            import soundfile as sf
            pcm, sr = sf.read(a.ses, dtype="int16")
            assert sr == O.SR
        else:
            pcm = np.fromfile(a.ses, np.int16)
        kaynak = a.ses
    else:
        pcm, kaynak = deneme_sesi()
    pcm.astype(np.int16).tofile(os.path.join(dz, "ses.pcm"))
    q = O.oznitelik_np(pcm)
    q.tofile(os.path.join(dz, "oznitelik.i8"))
    print(f"ses: {kaynak}, {len(pcm) / O.SR:.1f} sn, {len(q)} kare")

    # Python başvurusu
    lg = O.tamsayi_ileri(tm, q).numpy()
    z = lg.astype(np.float64) * np.float32(tm["cikis"]["olcek"])
    p = np.exp(z - z.max(1, keepdims=True))
    p /= p.sum(1, keepdims=True)
    si = O.SonIslem(esik_uyan=son["esik_uyan"], esik_komut=son["esik_komut"], yumusat=son["yumusat"])
    olay_py = si.olaylar(p)
    with torch.no_grad():
        fq = net(torch.from_numpy(q.astype(np.float32) * O.S_GIRIS).T[None])[0].T.numpy()
    print(f"sahte nicemli PyTorch (QAT) ile tamsayı başvuru argmax uyumu: {(fq.argmax(1) == lg.argmax(1)).mean():.4f}")

    # C
    exe = os.path.join(dz, "kws_test")
    tanim = f'-DKWS_MODEL_BASLIK="{baslik}"'
    calistir(["cc", "-O2", "-std=c11", "-Wall", "-Wextra", "-Werror", "-I" + os.path.dirname(BURASI), tanim, "-o", exe,
              os.path.join(BURASI, "kws_test.c"), "-lm"])
    calistir(["c++", "-O2", "-fsyntax-only", "-Wall", "-Wextra", "-Werror", "-x", "c++", "-I" + os.path.dirname(BURASI),
              tanim, os.path.join(BURASI, "kws_test.c")])
    print("C ve C++ derlemesi tamam (uyarısız)")
    print(calistir([exe, os.path.join(dz, "ses.pcm"), os.path.join(dz, "oznitelik.i8"), dz, "7"]).strip())

    hata = 0
    ag = np.fromfile(os.path.join(dz, "c_ag_logit.i32"), np.int32).reshape(-1, O.SINIF_SAYISI)
    esit = ag.shape == lg.shape and np.array_equal(ag, lg)
    print(f"1. yalnız ağ (aynı öznitelik): {'BİT BİT AYNI' if esit else 'FARKLI'} ({ag.shape[0]} kare)")
    hata += not esit

    cq = np.fromfile(os.path.join(dz, "c_oznitelik.i8"), np.int8).reshape(-1, O.NMEL)
    fark = (cq.astype(int) != q.astype(int))
    print(f"2. öznitelik: farklı değer oranı {fark.mean():.2e}, en büyük fark {np.abs(cq.astype(int) - q).max()} adım")
    hata += fark.mean() > 1e-3 or np.abs(cq.astype(int) - q).max() > 1

    cl = np.fromfile(os.path.join(dz, "c_logit.i32"), np.int32).reshape(-1, O.SINIF_SAYISI)
    n = min(len(cl), len(lg))
    uyum = (cl[:n].argmax(1) == lg[:n].argmax(1)).mean()
    dl = np.abs(cl[:n].astype(np.int64) - lg[:n]).max() * tm["cikis"]["olcek"]
    yay = np.abs(lg).max() * tm["cikis"]["olcek"]
    print(f"3. uçtan uca: {len(cl)} / {len(lg)} kare, argmax uyumu {uyum:.4f}, en büyük logit farkı {dl:.4f} "
          f"(logit aralığı ±{yay:.1f})")
    hata += len(cl) != len(lg) or uyum < 0.995

    oc = [tuple(map(int, s.split())) for s in open(os.path.join(dz, "c_olay.txt"))]
    op = [int(s) for s in open(os.path.join(dz, "c_olay_parca.txt"))]
    print(f"4. olaylar: Python {olay_py[:8]}{'...' if len(olay_py) > 8 else ''} ({len(olay_py)}) | "
          f"C kare kare {len(oc)} | C büyük parçalar {len(op)}")
    ayni = [tuple(x) for x in olay_py] == oc and [o for _, o in oc] == op
    print("   olaylar", "AYNI" if ayni else "FARKLI")
    hata += not ayni
    print("SONUÇ:", "GEÇTİ" if hata == 0 else f"BAŞARISIZ ({hata})")
    sys.exit(1 if hata else 0)


if __name__ == "__main__":
    main()
