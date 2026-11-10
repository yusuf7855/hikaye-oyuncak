"""Ses eğitimi izleme arayüzü — progress bar, tahmini süre, örnek ses oynatma."""
import os
import sys
import time
import subprocess
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from pathlib import Path

KOK = Path(__file__).parent.parent
SES_VERI = KOK / "ses_veri"
SES_CALISMA = KOK / "ses_calisma"
TOPLAM = 25000


def gpu_bilgisi():
    """NVIDIA GPU kullanım bilgisi."""
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used,memory.total", "--format=csv,noheader,nounits"],
            text=True, stderr=subprocess.DEVNULL
        ).strip()
        gpu, mem_used, mem_total = map(float, out.split(", "))
        return f"GPU: {gpu:.0f}%  |  VRAM: {mem_used:.0f}/{mem_total:.0f} MB"
    except Exception:
        return "GPU: ?"


def mp3_sayisi():
    """Tamamlanan mp3 dosya sayısı."""
    mp3_dir = SES_VERI / "mp3"
    if not mp3_dir.exists():
        return 0
    return len([f for f in mp3_dir.iterdir() if f.suffix == ".mp3"])


def asama_bilgisi():
    """Hangi aşamada olduğunu belirle."""
    mp3_count = mp3_sayisi()
    if mp3_count < TOPLAM:
        return 1, "Seslendirme (VoxCPM2)", mp3_count, TOPLAM

    # Diğer aşamalar için log dosyalarına bak
    if (SES_CALISMA / "akustik.log").exists():
        log = (SES_CALISMA / "akustik.log").read_text(encoding="utf-8", errors="ignore")
        if "bitti" not in log.lower():
            # Adım sayısını bul
            lines = log.strip().split("\n")
            for line in reversed(lines[-50:]):
                if "000 |" in line:
                    try:
                        adim = int(line.split("|")[0].strip().replace(" ", ""))
                        return 3, "Akustik model", adim, 150000
                    except:
                        pass
            return 3, "Akustik model", 0, 150000

    if (SES_CALISMA / "vocoder.log").exists():
        log = (SES_CALISMA / "vocoder.log").read_text(encoding="utf-8", errors="ignore")
        if "bitti" not in log.lower():
            lines = log.strip().split("\n")
            for line in reversed(lines[-50:]):
                if "adım" in line.lower() and "|" in line:
                    try:
                        adim = int(line.split("|")[0].replace("adım", "").strip())
                        return 4, "Vocoder", adim, 600000
                    except:
                        pass
            return 4, "Vocoder", 0, 600000

    if (SES_CALISMA / "gta.log").exists():
        return 5, "GTA ince ayar", 0, 30000

    return 2, "Hazırlık", 0, 100


class IzlemeArayuzu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ses Eğitimi İzleme")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e1e")

        self.baslangic = datetime.now()
        self.ilk_sayi = mp3_sayisi()

        self.olustur()
        self.guncelle()

    def olustur(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("green.Horizontal.TProgressbar", troughcolor="#333", background="#4CAF50")

        # Başlık
        tk.Label(self.root, text="Hikaye Oyuncağı — Ses Eğitimi",
                 font=("Segoe UI", 16, "bold"), fg="#fff", bg="#1e1e1e").pack(pady=15)

        # Aşama
        self.asama_label = tk.Label(self.root, text="Aşama: -",
                                     font=("Segoe UI", 12), fg="#aaa", bg="#1e1e1e")
        self.asama_label.pack()

        # Progress bar
        self.progress = ttk.Progressbar(self.root, length=400, mode="determinate",
                                         style="green.Horizontal.TProgressbar")
        self.progress.pack(pady=20)

        # Yüzde ve sayı
        self.yuzde_label = tk.Label(self.root, text="0%",
                                     font=("Segoe UI", 24, "bold"), fg="#4CAF50", bg="#1e1e1e")
        self.yuzde_label.pack()

        self.sayi_label = tk.Label(self.root, text="0 / 25000",
                                    font=("Segoe UI", 11), fg="#888", bg="#1e1e1e")
        self.sayi_label.pack()

        # Hız ve tahmini süre
        self.hiz_label = tk.Label(self.root, text="Hız: - cümle/dk",
                                   font=("Segoe UI", 10), fg="#666", bg="#1e1e1e")
        self.hiz_label.pack(pady=5)

        self.sure_label = tk.Label(self.root, text="Tahmini kalan: -",
                                    font=("Segoe UI", 10), fg="#666", bg="#1e1e1e")
        self.sure_label.pack()

        # GPU bilgisi
        self.gpu_label = tk.Label(self.root, text="GPU: -",
                                   font=("Segoe UI", 10), fg="#666", bg="#1e1e1e")
        self.gpu_label.pack(pady=10)

        # Örnek ses butonu
        self.ses_btn = tk.Button(self.root, text="Son Sesi Dinle",
                                  font=("Segoe UI", 10), bg="#333", fg="#fff",
                                  command=self.ses_oynat, state="disabled")
        self.ses_btn.pack(pady=10)

        # Durum
        self.durum_label = tk.Label(self.root, text="",
                                     font=("Segoe UI", 9), fg="#555", bg="#1e1e1e")
        self.durum_label.pack(side="bottom", pady=10)

    def ses_oynat(self):
        """Son üretilen sesi oynat."""
        mp3_dir = SES_VERI / "mp3"
        if mp3_dir.exists():
            files = sorted(mp3_dir.glob("*.mp3"), key=lambda f: f.stat().st_mtime, reverse=True)
            if files:
                os.startfile(str(files[0]))

    def guncelle(self):
        asama_no, asama_ad, tamamlanan, toplam = asama_bilgisi()

        yuzde = (tamamlanan / toplam * 100) if toplam > 0 else 0
        self.progress["value"] = yuzde
        self.yuzde_label.config(text=f"{yuzde:.1f}%")
        self.sayi_label.config(text=f"{tamamlanan:,} / {toplam:,}")
        self.asama_label.config(text=f"Aşama {asama_no}/6: {asama_ad}")

        # Hız hesapla
        gecen = (datetime.now() - self.baslangic).total_seconds() / 60
        yapilan = tamamlanan - self.ilk_sayi
        if gecen > 0.5 and yapilan > 0:
            hiz = yapilan / gecen
            kalan = (toplam - tamamlanan) / hiz if hiz > 0 else 0

            self.hiz_label.config(text=f"Hız: {hiz:.1f} cümle/dk")

            if kalan < 60:
                sure_str = f"{kalan:.0f} dakika"
            elif kalan < 1440:
                sure_str = f"{kalan/60:.1f} saat"
            else:
                sure_str = f"{kalan/1440:.1f} gün"
            self.sure_label.config(text=f"Tahmini kalan: {sure_str}")

        # GPU
        self.gpu_label.config(text=gpu_bilgisi())

        # Ses butonu
        if tamamlanan > 0:
            self.ses_btn.config(state="normal")

        # Durum
        self.durum_label.config(text=f"Son güncelleme: {datetime.now().strftime('%H:%M:%S')}")

        # 2 saniyede bir güncelle
        self.root.after(2000, self.guncelle)

    def calistir(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = IzlemeArayuzu()
    app.calistir()
