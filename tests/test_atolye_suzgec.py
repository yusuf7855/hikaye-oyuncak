"""web/atolye.html isim süzgeci (JS) = runtime/isim_suzgec.h (C).

1) isim_suzgec_test.c'deki sahte sözlük vakaları JS kodunda da aynı sonucu vermeli.
2) Gerçek tokenizer ve ürün figürlerinin yasaklı ad listeleriyle (urun_uret.kadro_disi, '$' işaretli) üretilmiş
   binlerce (önceki token'lar, aday) vakasında JS ve C kararları birebir aynı olmalı.
JS kodu atolye.html'deki <script id="suzgec-kodu"> bloğundan alınır (işçi ve sayfa aynı kodu kullanır).
"""
import json
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "degerlendirme"))
NODE = shutil.which("node")
TOKENIZER = ROOT / "hf_c3ft_urun740" / "tokenizer.json"


def suzgec_kodu():
    s = (ROOT / "web" / "atolye.html").read_text(encoding="utf-8")
    m = re.search(r'<script id="suzgec-kodu" type="text/plain">(.*?)</script>', s, re.S)
    assert m, "suzgec-kodu bloğu yok"
    return m.group(1)


# JS koşucusu: stdin'den {tok: [[bayt...]...], adlar: [...], vakalar: [[önceki..., aday]]} alır, 0/1 listesi yazar
JS_KOSUCU = r"""
const girdi = JSON.parse(require("fs").readFileSync(0, "utf8"));
const off = new Int32Array(girdi.tok.length + 1);
girdi.tok.forEach((b, i) => { off[i + 1] = off[i] + b.length; });
const bayt = new Uint8Array(off[girdi.tok.length]);
girdi.tok.forEach((b, i) => bayt.set(b, off[i]));
const out = girdi.vakalar.map(v => {
  const s = suzgecKur(bayt, off, girdi.adlar);
  for (const t of v.slice(0, -1)) suzgecEkle(s, t);
  return suzgecUygun(s, v[v.length - 1]) ? 1 : 0;
});
process.stdout.write(JSON.stringify(out));
"""

# C koşucusu: aynı girdiyi düz metin olarak okur (V, token baytları hex, ad sayısı, adlar, vaka satırları)
C_KOSUCU = r"""
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "isim_suzgec.h"
static int hx(int c) { return c <= '9' ? c - '0' : (c | 32) - 'a' + 10; }
int main(void) {
  static char satir[1 << 16]; int V, NA;
  if (scanf("%d\n", &V) != 1) return 2;
  char **tb = malloc(V * sizeof(char *)); int *tu = malloc(V * sizeof(int));
  for (int i = 0; i < V; i++) {
    if (!fgets(satir, sizeof satir, stdin)) return 2;
    int n = 0; while (satir[n] && satir[n] != '\n') n++;
    if (n == 1 && satir[0] == '-') n = 0;
    tu[i] = n / 2; tb[i] = malloc(n / 2 + 1);
    for (int j = 0; j < n / 2; j++) tb[i][j] = (char)(hx(satir[2 * j]) * 16 + hx(satir[2 * j + 1]));
  }
  if (scanf("%d\n", &NA) != 1) return 2;
  char **ad = malloc(NA * sizeof(char *)); int *au = malloc(NA * sizeof(int));
  for (int a = 0; a < NA; a++) {
    if (!fgets(satir, sizeof satir, stdin)) return 2;
    int n = 0; while (satir[n] && satir[n] != '\n') n++;
    ad[a] = malloc(n + 1); memcpy(ad[a], satir, n); ad[a][n] = 0; au[a] = n;
  }
  while (fgets(satir, sizeof satir, stdin)) {
    IsimSuzgec s; isim_suzgec_kur(&s, (const char *const *)tb, tu, V, (const char *const *)ad, au, NA);
    int ids[4096], n = 0; char *p = satir, *e;
    for (long v = strtol(p, &e, 10); e != p; v = strtol(p = e, &e, 10)) ids[n++] = (int)v;
    if (!n) continue;
    for (int i = 0; i < n - 1; i++) isim_suzgec_ekle(&s, ids[i]);
    putchar('0' + isim_suzgec_uygun(&s, ids[n - 1]));
  }
  return 0;
}
"""


def js_kararlar(tok, adlar, vakalar):
    with tempfile.TemporaryDirectory() as d:
        js = os.path.join(d, "k.js")
        Path(js).write_text(suzgec_kodu() + "\n" + JS_KOSUCU, encoding="utf-8")
        girdi = json.dumps({"tok": [list(b) for b in tok], "adlar": adlar, "vakalar": vakalar})
        r = subprocess.run([NODE, js], input=girdi, capture_output=True, text=True, check=True)
        return json.loads(r.stdout)


def c_kararlar(tok, adlar, vakalar):
    with tempfile.TemporaryDirectory() as d:
        kaynak, exe = os.path.join(d, "k.c"), os.path.join(d, "k")
        Path(kaynak).write_text(C_KOSUCU)
        subprocess.run(["cc", "-O2", "-I", str(ROOT / "runtime"), "-o", exe, kaynak], check=True)
        satirlar = [str(len(tok))] + [b.hex() or "-" for b in tok] + [str(len(adlar))] + adlar
        satirlar += [" ".join(map(str, v)) for v in vakalar]
        r = subprocess.run([exe], input="\n".join(satirlar) + "\n", capture_output=True, text=True, check=True)
        return [int(c) for c in r.stdout]


@unittest.skipUnless(NODE, "node yok")
class JsBirim(unittest.TestCase):
    """runtime/host_verify/isim_suzgec_test.c ile aynı vakalar, aynı beklentiler."""

    def test_c_vakalari(self):
        TOK = [" O", "laf", " Orman", " N", "il", "oya", "'ya", " Tim", "sah", " ile", ",", "’", "nin", '"',
               "Olaf", " Nil", "ü"]
        T = {k: i for i, k in enumerate(["O", "LAF", "ORMAN", "N", "IL", "OYA", "YA", "TIM", "SAH", "ILE", "VIRGUL",
                                          "KESME", "NIN", "TIRNAK", "OLAF", "NIL", "U"])}
        vakalar = [  # (ad, önceki, aday, beklenen)
            ("' O' serbest", [], "O", 1), ("' O'+'laf' red", ["O"], "LAF", 0),
            ("' Orman' serbest", [], "ORMAN", 1), ("'Olaf' metin başı red", [], "OLAF", 0),
            ("'\"Olaf' red", ["TIRNAK"], "OLAF", 0), ("' N'+'il' serbest", ["N"], "IL", 1),
            ("' Nil' serbest", [], "NIL", 1), ("' N'+'il'+'oya' red", ["N", "IL"], "OYA", 0),
            ("'ü'+'Olaf' kelime içi serbest", ["U"], "OLAF", 1), ("' Tim' tek başına serbest ($)", [], "TIM", 1),
            ("' Tim'+'sah' serbest ($)", ["TIM"], "SAH", 1), ("' Tim'+' ile' red ($)", ["TIM"], "ILE", 0),
            ("' Tim'+',' red ($)", ["TIM"], "VIRGUL", 0), ("' Tim'+'’' red ($)", ["TIM"], "KESME", 0),
            ("'’'+'Olaf' red", ["KESME"], "OLAF", 0),
        ]
        tok = [t.encode() for t in TOK]
        karar = js_kararlar(tok, ["Olaf", "Niloya", "Tim$"], [[T[x] for x in once] + [T[a]] for _, once, a, _ in vakalar])
        for (ad, _, _, bek), k in zip(vakalar, karar):
            self.assertEqual(k, bek, ad)


@unittest.skipUnless(NODE and shutil.which("cc") and TOKENIZER.exists(), "node, cc ya da ürün tokenizer'ı yok")
class JsCAyni(unittest.TestCase):
    """Gerçek tokenizer + ürün ad listeleri: JS ve C kararları birebir aynı."""

    def test_fark_yok(self):
        from tokenizers import Tokenizer
        import urun_uret as u
        tk = Tokenizer.from_file(str(TOKENIZER))
        harita = u._bayt_haritasi()
        V = tk.get_vocab_size()
        tok = [bytes(harita[c] for c in (tk.id_to_token(i) or "") if c in harita) for i in range(V)]
        rng = random.Random(7)
        toplam_red = 0
        for kimlik in ("elsa", "pepee", "niloya", "hayri"):
            adlar = [a + ("$" if u.kelime_basi_mi(a) else "") for a in u.kadro_disi(kimlik)]
            duz = [a.rstrip("$") for a in adlar]
            ekler = ["", "'nin", "’ın", " ile", ",", ".", "sah", "ya", "cık", " de", "!\"", "lar"]
            bas = ["", " ", "\"", "“", "Bir gün ", "ve ", "ü", "a"]
            metinler = [f"{rng.choice(bas)}{rng.choice(duz)}{rng.choice(ekler)} {rng.choice(duz)}{rng.choice(ekler)}"
                        for _ in range(120)]
            metinler += ["Karakter: Elsa | Yer: dağ | Yan: Olaf\nSorun: Timsah Balık Canı Sarayın Tom'un Dino"]
            vakalar = []
            for m in metinler:
                ids = [0] + tk.encode(m).ids
                for i in range(1, len(ids)):
                    vakalar.append(ids[:i + 1])                              # gerçek sonraki token
                    vakalar.append(ids[:i] + [rng.randrange(V)])             # rastgele aday
            js, c = js_kararlar(tok, adlar, vakalar), c_kararlar(tok, adlar, vakalar)
            self.assertEqual(len(js), len(vakalar))
            fark = [v for v, a, b in zip(vakalar, js, c) if a != b]
            self.assertFalse(fark, f"{kimlik}: {len(fark)} fark, ilki {fark[:1]}")
            toplam_red += js.count(0)
        self.assertGreater(toplam_red, 50)  # vakalar gerçekten ret içeriyor


if __name__ == "__main__":
    unittest.main()
