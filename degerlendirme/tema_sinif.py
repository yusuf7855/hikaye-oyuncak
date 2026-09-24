"""Tema sınıflayıcı: model tokenizer'ıyla token düzeyinde çok terimli Naive Bayes (20 tema, TEMALAR sırası).

Kullanım: python degerlendirme/tema_sinif.py <model_dizini> --dogrulama data/tr_<etiket>/vocab-16384/dogrulama.json
          [--haric dosya]
Eğitim: data/oyuncak_v2 + v3'ün geçerli hikâyeleri, dogrulama.json'daki (ve --haric'teki) kimlikler hariç; yani
modelin eğitim bölmesi. Doğruluk dogrulama.json'daki hikâyelerde ölçülür.
Özellik: en az 3 eğitim hikâyesinde geçen token'lar; figür ismi ve türü token'ları çıkarılır (geçişlerinin
yarısından fazlası bir isim/tür kelimesinin içindeyse): tema değil figür bilgisi taşırlar.
Ağırlık: log P(token | tema), alpha=0.5 yumuşatma, tema ekseninde ortalaması çıkarılır, 0.05 nat birimiyle int8.
Önsel yok (her tema eşit); karar argmax Σ w[token].
Çıktı: <model_dizini>/tema_nb.json (temalar, idler, w, doğruluk, eğitim dışı kimlikler) ve tema_nb.bin (cihaz):
  "TNB1", uint16 n_tema, uint16 n_satir, uint16 id[n_satir] (artan), int8 w[n_satir][n_tema]  (küçük uçlu)
E5'e kadar yalnızca ölçüm aracıdır (olay.py); seçicide kullanılmaz.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys

import numpy as np
from tokenizers import Tokenizer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from baslangic import KAR, TEMALAR  # noqa: E402
from research.tinystories.prepare_ft2 import kimlik_ver  # noqa: E402
from sec import kucuk  # noqa: E402

OLCEK = 0.05  # int8 birimi (nat)
HARF = "a-zçğıöşüâîû"
ISIM_RE = re.compile(r"(?<![A-Za-zÇĞİÖŞÜçğıöşüâîû])(?:" + "|".join(k["isim"] for k in KAR.values()) + rf")(?![{HARF}])")
# tür + küçültme/çoğul/durum ekleri; "kızdı", "ayırdı", "kuşku" gibi başka kelimeler eşleşmez
TUR_RE = re.compile(
    rf"(?<![{HARF}])(?:tavşan|kedi|köpe[kğ]|ayı|tilki|kuş|kaplumbağa|penguen|dinozor|ejderha|kız|oğlan)"
    r"(?:cık|cik|çık|çik|cuk|cük|cağız|ciğ|cığ|çığ|çiğ)?(?:lar|ler)?"
    r"(?:ı|i|u|ü|a|e|ın|in|un|ün|nın|nin|nun|nün|ya|ye|yı|yi|yu|yü|da|de|ta|te|dan|den|tan|ten|la|le|yla|yle"
    r"|sı|si|su|sü|nı|ni|nu|nü|na|ne|nda|nde|ndan|nden|ları|leri|ım|im|um|üm|ımız|imiz|umuz|ümüz)?"
    rf"(?![{HARF}])")
BOL = re.compile(r"(?<=[.!?])\s+|\n+")


def hikayeler(kaynaklar=("oyuncak_v2", "oyuncak_v3")):
    """Bütün geçerli oyuncak hikâyeleri, prepare_ft2 ile aynı kimliklerle: [{id, turler, yer, tema, metin, ...}]."""
    out = []
    for k in kaynaklar:
        d = os.path.join(ROOT, "data", k)
        spec = importlib.util.spec_from_file_location(f"kontrol_{k}", os.path.join(d, "kontrol.py"))
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        out += kimlik_ver(k, m.oku()[0])
    return out


def egitim_hikayeleri(nb_json):
    """tema_nb.json'un eğitim bölmesi (kopya ölçüsü de aynı hikâyelere bakar)."""
    disi = set(nb_json["egitim_disi"])
    return [h for h in hikayeler() if h["id"] not in disi]


def yari_siniri(metin):
    """Cümle sayısına göre orta: ilk ⌊n/2⌋ cümleden sonraki ilk karakter (tek cümlede metnin ortası)."""
    sinirlar = [m.end() for m in BOL.finditer(metin) if 0 < m.start() and m.end() < len(metin)]
    k = (len(sinirlar) + 1) // 2
    return sinirlar[k - 1] if k >= 1 else len(metin) // 2


def figur_idleri(metinler, tok, esik=0.5):
    """Geçişlerinin en az `esik` kadarı bir figür ismi ya da tür kelimesiyle örtüşen token id'leri."""
    ic, tum = {}, {}
    for metin, enc in zip(metinler, tok.encode_batch(metinler)):
        spans = [m.span() for m in ISIM_RE.finditer(metin)] + [m.span() for m in TUR_RE.finditer(kucuk(metin))]
        for i, (a, b) in zip(enc.ids, enc.offsets):
            tum[i] = tum.get(i, 0) + 1
            if any(a < e and b > s for s, e in spans):
                ic[i] = ic.get(i, 0) + 1
    return sorted(i for i, n in ic.items() if n >= esik * tum[i])


def egit(docs, tok, min_df=3, alpha=0.5):
    """docs: [{metin, tema}]. Döner: (idler artan, w int8 [n, 20], haric_idler)."""
    metinler = [h["metin"] for h in docs]
    ids = [np.array(e.ids, dtype=np.int64) for e in tok.encode_batch(metinler)]
    V = tok.get_vocab_size()
    haric = figur_idleri(metinler, tok)
    df = np.zeros(V, dtype=np.int64)
    cnt = np.zeros((len(TEMALAR), V), dtype=np.float64)
    ti = {t: i for i, t in enumerate(TEMALAR)}
    for h, x in zip(docs, ids):
        df[np.unique(x)] += 1
        np.add.at(cnt[ti[h["tema"]]], x, 1)
    ozellik = df >= min_df
    ozellik[haric] = False
    idler = np.flatnonzero(ozellik)
    c = cnt[:, idler]
    logp = np.log((c + alpha) / (c.sum(1, keepdims=True) + alpha * len(idler)))
    logp -= logp.mean(0, keepdims=True)
    w = np.clip(np.round(logp / OLCEK), -127, 127).astype(np.int8).T
    return idler, w, haric


class TemaNB:
    """tema_nb.json'dan yüklenen sınıflayıcı. skor(ids) -> 20 tamsayı; uc_tema(metin) -> TEMALAR indeksleri."""

    def __init__(self, nb, tok):
        self.nb, self.tok = nb, tok
        self.W = np.zeros((tok.get_vocab_size(), len(nb["temalar"])), dtype=np.int32)
        self.W[np.array(nb["idler"], dtype=np.int64)] = np.array(nb["w"], dtype=np.int32)
        self.temalar = nb["temalar"]

    def skor(self, ids):
        return self.W[np.asarray(ids, dtype=np.int64)].sum(0) if len(ids) else np.zeros(len(self.temalar), np.int32)

    def uc_tema(self, metin):
        """(tam, ilk yarı, ikinci yarı) argmax temaları; yarılar tek kodlamadan cümle sınırında kesilir."""
        enc = self.tok.encode(metin)
        s = yari_siniri(metin)
        a = [i for i, (b, _) in zip(enc.ids, enc.offsets) if b < s]
        b = enc.ids[len(a):]
        return int(np.argmax(self.skor(enc.ids))), int(np.argmax(self.skor(a))), int(np.argmax(self.skor(b)))


def tokenizer_sha(model_dir):
    return hashlib.sha256(open(os.path.join(model_dir, "tokenizer.json"), "rb").read()).hexdigest()


def yukle(model_dir):
    """<model_dizini>/tema_nb.json + tokenizer.json -> TemaNB (tokenizer farklıysa uyarır)."""
    nb = json.load(open(os.path.join(model_dir, "tema_nb.json"), encoding="utf-8"))
    if nb.get("tokenizer_sha256") != tokenizer_sha(model_dir):
        print(f"UYARI: {model_dir}/tema_nb.json başka bir tokenizer ile öğrenilmiş", file=sys.stderr)
    return TemaNB(nb, Tokenizer.from_file(os.path.join(model_dir, "tokenizer.json")))


def dogruluk(nb, docs):
    ti = {t: i for i, t in enumerate(nb.temalar)}
    r = np.array([(ti[h["tema"]], *nb.uc_tema(h["metin"])) for h in docs])
    y, tam, a, b = r.T
    yuz = lambda x: round(100 * float(np.mean(x)), 1)  # noqa: E731
    return {"n": len(docs), "tam_%": yuz(tam == y), "ilk_yari_%": yuz(a == y), "ikinci_yari_%": yuz(b == y),
            "iki_yari_dogru_%": yuz((a == y) & (b == y)), "iki_yari_ayni_tema_%": yuz(a == b),
            "ceza_alan_%": yuz((tam != y) | (a != y) | (b != y))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir")
    ap.add_argument("--dogrulama", required=True, help="prepare_ft2'nin yazdığı dogrulama.json")
    ap.add_argument("--haric", default=None, help="eğitimden de çıkarılan kimlikler (prepare_ft2 --haric dosyası)")
    ap.add_argument("--min-df", type=int, default=3)
    ap.add_argument("--alpha", type=float, default=0.5)
    a = ap.parse_args()
    tok = Tokenizer.from_file(os.path.join(a.model_dir, "tokenizer.json"))
    dogrulama = json.load(open(a.dogrulama, encoding="utf-8"))
    disi = {h["id"] for h in dogrulama}
    if a.haric:
        disi |= {s.strip() for s in open(a.haric, encoding="utf-8") if s.strip()}
    tum = hikayeler()
    egitim = [h for h in tum if h["id"] not in disi]
    eksik = {h["id"] for h in dogrulama} - {h["id"] for h in tum}
    if eksik:
        print(f"UYARI: {len(eksik)} doğrulama kimliği veride yok (ör. {sorted(eksik)[:3]})", file=sys.stderr)
    idler, w, haric = egit(egitim, tok, a.min_df, a.alpha)
    nb = {"temalar": TEMALAR, "olcek": OLCEK, "alpha": a.alpha, "min_df": a.min_df,
          "tokenizer_sha256": tokenizer_sha(a.model_dir), "dogrulama": a.dogrulama,
          "egitim_disi": sorted(disi), "n_egitim": len(egitim), "haric_idler": haric,
          "haric_tokenler": [tok.decode([i]) for i in haric], "idler": idler.tolist(), "w": w.tolist()}
    nb["dogruluk"] = dogruluk(TemaNB(nb, tok), dogrulama)
    bin_yol = os.path.join(a.model_dir, "tema_nb.bin")
    with open(bin_yol, "wb") as f:
        f.write(b"TNB1" + np.array([len(TEMALAR), len(idler)], "<u2").tobytes())
        f.write(idler.astype("<u2").tobytes() + w.astype(np.int8).tobytes())
    nb["bin_bayt"] = os.path.getsize(bin_yol)
    json.dump(nb, open(os.path.join(a.model_dir, "tema_nb.json"), "w", encoding="utf-8"), ensure_ascii=False)
    print(f"{len(egitim)} eğitim hikâyesi, {len(idler)} özellik token'ı, {len(haric)} figür token'ı çıkarıldı: "
          f"{' '.join(nb['haric_tokenler'])}")
    print(f"{bin_yol}: {nb['bin_bayt']:,} bayt")
    print("doğrulama:", json.dumps(nb["dogruluk"], ensure_ascii=False))


if __name__ == "__main__":
    main()
