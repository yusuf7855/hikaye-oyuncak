"""ses.h denemesi: eğitilmemiş (rastgele) bir ses modeli kurar, ses/disa_aktar.py ile ses.bin + altın örnekler
yazar, tools/ses_test.c'yi derleyip C çıkarımını PyTorch'la (kartın ağırlıklarıyla) karşılaştırır.

  .venv/bin/python firmware/hikaye_oyuncak/tools/ses_test.py [--dizin /tmp/ses_deneme] [--akustik a.pt --vocoder v.pt]

--akustik/--vocoder verilirse rastgele model yerine o kayıtlar denenir (eğitilmiş model gelince aynı deneme).
C iki kez derlenir: varsayılan parça boyları ve çok küçük parçalar (SES_PARCA=5, SES_ALT=3; akış sınırlarını zorlar).
"""
import argparse
import os
import subprocess
import sys
import tempfile

import torch

BURASI = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.abspath(os.path.join(BURASI, "..", "..", ".."))
sys.path.insert(0, os.path.join(KOK, "ses"))
from model import Akustik, Vocoder  # noqa: E402

CUMLELER = [
    "Bir varmış bir yokmuş.",
    "\"Yardım eder misin?\" diye sordu karınca.",
    "Güneş batarken bütün arkadaşlar ağacın altında toplandı ve birlikte güldüler!",
    "o",
]


@torch.no_grad()
def rastgele_modeller(dizin, tohum=0):
    """Varsayılan boyutlarda rastgele modeller; küçük parametreler de sıfır/bir olmasın diye bozulur.
    Süreler gerçekçi (harf başına ~2-8 kare) olsun diye süre çıkışının bias'ı ayarlanır."""
    torch.manual_seed(tohum)
    ak, vo = Akustik(), Vocoder()
    for m in (ak, vo):
        for ad, p in m.named_parameters():
            if p.dim() == 1:
                p.add_(torch.randn_like(p) * (0.2 if "ln" in ad else 0.05))
    ak.tah_cikis.weight.mul_(3.0)
    ak.tah_cikis.bias[0] = 1.6             # exp(1.6) - 1 ~ 4 kare
    vo.cikis.bias[: vo.cikis.bias.numel() // 2] -= 3.0   # log genlik ~ -3
    ak.istat.copy_(torch.tensor([5.4, 0.25, -4.8, 1.7]))
    a, v = os.path.join(dizin, "akustik.pt"), os.path.join(dizin, "vocoder.pt")
    torch.save({"model": ak.state_dict()}, a)
    torch.save({"model": vo.state_dict()}, v)
    return a, v


def calistir(komut, **kw):
    print("$", " ".join(komut), flush=True)
    r = subprocess.run(komut, **kw)
    if r.returncode:
        sys.exit(r.returncode)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dizin", default=None)
    ap.add_argument("--akustik", default=None)
    ap.add_argument("--vocoder", default=None)
    ap.add_argument("--cc", default=os.environ.get("CC", "cc"))
    a = ap.parse_args()
    torch.set_num_threads(1)
    dizin = a.dizin or tempfile.mkdtemp(prefix="ses_deneme_")
    os.makedirs(dizin, exist_ok=True)
    if a.akustik and a.vocoder:
        ak, vo = a.akustik, a.vocoder
    else:
        ak, vo = rastgele_modeller(dizin)
    bin_, altin = os.path.join(dizin, "ses.bin"), os.path.join(dizin, "ses_altin.bin")
    komut = [sys.executable, os.path.join(KOK, "ses", "disa_aktar.py"), "--akustik", ak, "--vocoder", vo,
             "--cikti", bin_, "--altin", altin]
    for c in CUMLELER:
        komut += ["--cumle", c]
    calistir(komut, env=dict(os.environ, OMP_NUM_THREADS="1"))
    for ad, ek in (("varsayılan", []), ("küçük parça", ["-DSES_PARCA=5", "-DSES_ALT=3"])):
        exe = os.path.join(dizin, "ses_test" + ("_kucuk" if ek else ""))
        calistir([a.cc, "-std=c11", "-O2", "-Wall", "-Wextra", "-I" + os.path.dirname(BURASI), *ek, "-o", exe,
                  os.path.join(BURASI, "ses_test.c"), "-lm"])
        print(f"--- C çıkarımı ({ad})", flush=True)
        calistir([exe, bin_, altin])
    print(f"dosyalar: {dizin}")


if __name__ == "__main__":
    main()
