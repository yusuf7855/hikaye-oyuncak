"""Ay Dede'nin 15 sabit halk ninnisi: biçim (kıta, hece) ve yerlesik.h'nin ninniler.txt ile eşitliği."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARAC = os.path.join(ROOT, "firmware", "hikaye_oyuncak", "tools")
sys.path.insert(0, ARAC)
import ninniler as N  # noqa: E402


def test_ninniler_bicim():
    ninniler = N.oku()
    assert len(ninniler) == 15
    assert N.denetle(ninniler) == []
    assert ninniler[0][0] == "Dandini dandini dastana"


def test_yerlesik_guncel():
    r = subprocess.run([sys.executable, os.path.join(ARAC, "ninniler.py"), "--denetle"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_ninnide_yer_etiketi_yok():
    # ürün sahibi: ninnilere yer adıyla isim verilmez ("deniz ninnisi" gibi)
    for ad, _ in N.oku():
        assert "ninnisi" not in ad.lower() or ad.lower().startswith("ninni")
