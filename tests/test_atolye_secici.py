"""web/atolye.html ürün seçicisi (JS urunPuanla) = degerlendirme/urun_uret.puanla (Python).

Gerçek model adayları (c3ft_urun740 / c3ft_urun1030s2 üretimlerinden, tests/atolye_secici_vakalar.json; kadro_cezalari
ve takinti_cezasi'nı tetikleyenler dahil) iki tarafta puanlanır: puanlar 1e-6 içinde, ceza etiketleri (biçim farkı
ayıklanmış: Python liste repr'i '['a', 'b']' / JS 'a, b') aynı olmalı. JS kodu atolye.html'deki seçici bölümünden
(KATALOG'dan token çözmeye kadar) alınır; meta.urun'un seçici kısmı web/paketle.urun_secici() ile kurulur.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "degerlendirme"))
sys.path.insert(0, str(ROOT / "web"))
NODE = shutil.which("node")
VAKALAR = Path(os.environ.get("ATOLYE_SECICI_VAKALAR", Path(__file__).with_name("atolye_secici_vakalar.json")))


def secici_kodu():
    s = (ROOT / "web" / "atolye.html").read_text(encoding="utf-8")
    a, b = s.index("const KATALOG = {"), s.index("// ---- token çözme")
    return s[a:b]


JS_KOSUCU = r"""
const girdi = JSON.parse(require("fs").readFileSync(0, "utf8"));
SOZLUK = new Set(require("fs").readFileSync(girdi.sozluk, "utf8").split("\n"));
const U = girdi.U;
const out = girdi.adaylar.map(a => {
  const fig = U.figurler.find(f => f.kimlik === a.figur);
  const r = urunPuanla({ ...a, ort: a.lp }, fig, a.yer, U);
  return { puan: r.puan, liste: r.liste };
});
process.stdout.write(JSON.stringify(out));
"""


def js_puanlar(adaylar):
    import paketle
    with tempfile.TemporaryDirectory() as d:
        js = os.path.join(d, "k.js")
        Path(js).write_text(secici_kodu() + "\n" + JS_KOSUCU, encoding="utf-8")
        girdi = json.dumps({"U": paketle.urun_secici(), "adaylar": adaylar, "sozluk": str(ROOT / "web" / "sozluk.txt")})
        r = subprocess.run([NODE, js], input=girdi, capture_output=True, text=True, check=True)
        return json.loads(r.stdout)


def etiket(s):
    """Biçim farkını ayıkla: Python "yanlış isim ['X', 'Y']" / "x3" = JS "yanlış isim: X, Y" / "×3"."""
    return " ".join(re.sub(r"[\[\]'\",:]", " ", s.replace("×", "x")).split())


@unittest.skipUnless(NODE and VAKALAR.exists() and (ROOT / "web" / "sozluk.txt").exists()
                     and (ROOT / "degerlendirme" / "sozluk.pkl").exists(), "node, vakalar ya da sözlük yok")
class UrunSeciciAyni(unittest.TestCase):
    def test_python_js_ayni(self):
        import urun_uret as u
        adaylar = json.loads(VAKALAR.read_text(encoding="utf-8"))
        js = js_puanlar(adaylar)
        self.assertEqual(len(js), len(adaylar))
        fark, yeni_kural = [], 0
        for a, j in zip(adaylar, js):
            puan, c = u.puanla(a, a["figur"], a["yer"])
            py = sorted((round(p, 6), etiket(e)) for p, e in c)
            jj = sorted((round(p, 6), etiket(e)) for p, e in j["liste"])
            if abs(puan - j["puan"]) > 1e-6 or py != jj:
                fark.append((a["figur"], a["metin"][:60], puan, j["puan"], sorted(set(py) ^ set(jj))))
            yeni_kural += any(k in e for _, e in c for k in ("kendine sesleniyor", "kartta olmayan", "takıntılı", "kendi kendine"))
        self.assertFalse(fark, f"{len(fark)}/{len(adaylar)} fark, ilkleri {fark[:3]}")
        self.assertGreater(yeni_kural, 5)  # vakalar yeni kuralları gerçekten tetikliyor


if __name__ == "__main__":
    unittest.main()
