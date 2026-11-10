"""
Vocoder eğitim watchdog - eğitim durursa otomatik yeniden başlatır.
PC açılışında çalıştırmak için: pythonw watchdog.py
"""
import subprocess
import time
import os
import sys
from pathlib import Path
from datetime import datetime

# Ayarlar
PROJE = Path(__file__).parent.parent
VENV_PYTHON = PROJE / ".venv" / "Scripts" / "python.exe"
EGIT_SCRIPT = PROJE / "ses" / "egit_vocoder.py"
CHECKPOINT = PROJE / "ses_calisma" / "vocoder" / "son.pt"
LOG_DOSYA = PROJE / "watchdog.log"
HEDEF_ADIM = 600000
KONTROL_ARASI = 120  # saniye

def log(mesaj):
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    satir = f"[{zaman}] {mesaj}"
    print(satir)
    with open(LOG_DOSYA, "a", encoding="utf-8") as f:
        f.write(satir + "\n")

def checkpoint_adim():
    """Checkpoint'tan mevcut adımı oku"""
    try:
        import torch
        c = torch.load(CHECKPOINT, map_location="cpu", weights_only=False)
        return c.get("adim", 0)
    except:
        return 0

def gpu_kullanımda():
    """GPU'da eğitim çalışıyor mu kontrol et"""
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-compute-apps=pid", "--format=csv,noheader"],
            capture_output=True, text=True, timeout=10
        )
        return len(result.stdout.strip()) > 0
    except:
        return False

def egitim_baslat():
    """Eğitimi arka planda başlat"""
    log("Eğitim başlatılıyor...")
    subprocess.Popen(
        [str(VENV_PYTHON), str(EGIT_SCRIPT), "--adim", str(HEDEF_ADIM), "--is", "0"],
        cwd=str(PROJE),
        creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == "win32" else 0
    )
    time.sleep(30)  # Başlaması için bekle

def main():
    log("Watchdog başlatıldı")
    log(f"Hedef: {HEDEF_ADIM} adım")

    son_adim = 0
    takılma_sayısı = 0

    while True:
        try:
            adim = checkpoint_adim()
            gpu = gpu_kullanımda()

            if adim >= HEDEF_ADIM:
                log(f"Eğitim tamamlandı! Adım: {adim}")
                break

            if not gpu:
                log(f"GPU boş, adım: {adim}. Eğitim başlatılıyor...")
                egitim_baslat()
                takılma_sayısı = 0
            elif adim == son_adim:
                takılma_sayısı += 1
                if takılma_sayısı >= 5:  # 5 kontrol = 10 dakika takılı
                    log(f"Eğitim takılmış (adım {adim}). Yeniden başlatılıyor...")
                    # GPU işlemlerini öldür
                    subprocess.run(["taskkill", "/F", "/IM", "python.exe"],
                                   capture_output=True, timeout=30)
                    time.sleep(10)
                    egitim_baslat()
                    takılma_sayısı = 0
            else:
                takılma_sayısı = 0
                log(f"Çalışıyor: {adim}/{HEDEF_ADIM} ({100*adim/HEDEF_ADIM:.1f}%)")

            son_adim = adim

        except Exception as e:
            log(f"Hata: {e}")

        time.sleep(KONTROL_ARASI)

    log("Watchdog kapandı")

if __name__ == "__main__":
    main()
