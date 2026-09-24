"""Uydurma-kelime kontrolü için Türkçe kelime sözlüğü (eğitim verisinde ≥3 kez geçen kelimeler).
Kullanım: python degerlendirme/sozluk_olustur.py   ->  degerlendirme/sozluk.pkl"""
import collections, glob, os, pickle, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
kucuk = lambda s: s.replace("I", "ı").replace("İ", "i").lower()  # sec.kucuk ile aynı
say = collections.Counter()
with open(os.path.join(ROOT, "data/tr_tinystories/raw/tr-tinystories.txt"), encoding="utf-8") as f:
    for line in f:
        say.update(re.findall(r"[a-zçğıöşüâîû]+", kucuk(line)))
for p in glob.glob(os.path.join(ROOT, "data/oyuncak_*/*.txt")):
    say.update(re.findall(r"[a-zçğıöşüâîû]+", kucuk(open(p, encoding="utf-8").read())))
sozluk = {w for w, c in say.items() if c >= 3}
pickle.dump(sozluk, open(os.path.join(ROOT, "degerlendirme/sozluk.pkl"), "wb"))
print(len(sozluk), "kelime")
