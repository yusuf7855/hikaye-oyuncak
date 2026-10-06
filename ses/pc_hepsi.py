"""Kendi bilgisayarınızda (NVIDIA ekran kartı, ör. RTX 4090; Windows ya da Linux) ses modelinin bütün eğitimi, sırayla.

  python ses/pc_hepsi.py            # hepsi; yarıda kalırsa aynı komutla kaldığı yerden sürer
  python ses/pc_hepsi.py akustik    # yalnız bir aşama: veri | hazirla | akustik | vocoder | gta | paket

Aşamalar: [1] 25 bin cümle seçilen sesle (ses/referans_ses.mp3, VoxCPM2) -> ses_veri/mp3, [2] hazırlık (mel, perde),
[3] akustik, [4] vocoder, [5] GTA ince ayar, [6] deneme.wav + ses.bin (karta 0xBB0000).
Günlükler ve kayıtlar ses_calisma/ altında. Kurulum: ses/README.md "Kendi bilgisayarınızda".
"""
import os
import subprocess
import sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable
IS = str(min(8, os.cpu_count() or 4))


def calistir(ad, args, gunluk=None):
    print(f"\n=== {ad} ===", flush=True)
    if gunluk:
        with open(os.path.join(KOK, "ses_calisma", gunluk), "a", encoding="utf-8") as g:
            p = subprocess.Popen([PY, *args], cwd=KOK, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 text=True, encoding="utf-8", errors="replace")
            for satir in p.stdout:
                g.write(satir)
                g.flush()
                if any(k in satir for k in ("000 |", "==", "devam", "cihaz", "bitti", "rror", "başlangıç")):
                    print(satir, end="", flush=True)
            if p.wait():
                sys.exit(f"{ad} hata verdi; ayrıntı ses_calisma/{gunluk}")
    elif subprocess.call([PY, *args], cwd=KOK):
        sys.exit(f"{ad} hata verdi")


def main():
    asama = sys.argv[1] if len(sys.argv) > 1 else "hepsi"
    sec = lambda a: asama in ("hepsi", a)  # noqa: E731
    os.makedirs(os.path.join(KOK, "ses_calisma"), exist_ok=True)
    import torch
    if not torch.cuda.is_available():
        sys.exit("CUDA'lı PyTorch bulunamadı (ekran kartı görünmüyor): ses/README.md kurulum adımına bakın")
    print("ekran kartı:", torch.cuda.get_device_name(0), flush=True)
    if sec("veri"):
        calistir("[1/6] 25 bin cümle seslendiriliyor (VoxCPM2)", ["ses/veri_uret_vox.py", "--cikti", "ses_veri"])
    if sec("hazirla"):
        calistir("[2/6] hazırlık: 16 kHz, mel, perde", ["ses/hazirla.py", "--veri", "ses_veri", "--is", IS])
    if sec("akustik"):
        calistir("[3/6] akustik model (metin -> mel)", ["ses/egit_akustik.py", "--is", IS], "akustik.log")
    if sec("vocoder"):
        calistir("[4/6] vocoder (mel -> ses)", ["ses/egit_vocoder.py", "--is", IS, "--adim", "600000"], "vocoder.log")
    if sec("gta"):
        calistir("[5/6] vocoder ince ayar (GTA)",
                 ["ses/egit_vocoder.py", "--gta", "--cikti", "ses_calisma/vocoder_gta", "--adim", "30000",
                  "--sadece-mel", "0", "--lr", "1e-4", "--baslangic", "ses_calisma/vocoder/son.pt", "--is", IS],
                 "gta.log")
    if sec("paket"):
        v = "ses_calisma/vocoder_gta/son.pt"
        calistir("[6/6] deneme.wav", ["ses/sentezle.py", "--vocoder", v, "--cikti", "deneme.wav", "--kuant"])
        calistir("[6/6] ses.bin", ["ses/disa_aktar.py", "--akustik", "ses_calisma/akustik/son.pt", "--vocoder", v,
                                   "--cikti", "ses.bin", "--altin", "ses_altin.bin"])
        print("\nBİTTİ: deneme.wav'ı dinleyin; ses.bin karta 0xBB0000 adresine yüklenir (firmware/hikaye_oyuncak/README.md)")


if __name__ == "__main__":
    main()
