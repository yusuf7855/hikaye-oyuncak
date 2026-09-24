"""Türkçe TinyStories (esat-krky/TinyStories_Turkish) için prepare.py'yi yerel dosyayla çalıştırır.

Kullanım: TS_DATA=data/tr_tinystories python -m research.tinystories.prepare_tr --vocab 32768
"""
import sys

from . import prepare

prepare.RAW = prepare.DATA / "raw" / "tr-tinystories.txt"
prepare.download = lambda: print(f"yerel veri: {prepare.RAW}")

if __name__ == "__main__":
    sys.exit(prepare.main())
