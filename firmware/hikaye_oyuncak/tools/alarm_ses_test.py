"""Alarm sesi: ayar sayfasının JavaScript kodlayıcısı (ayar_sayfa.h) ile kartın C kodu (alarm_ses.h) aynı mı?

1. Sayfadaki ses işleme işlevleri (adpcm, crc32, sekizK, paketle) ayar_sayfa.h'den kesilip Node'da çalıştırılır:
   44,1 kHz iki kanallı yapay bir "şarkı" (ezgi + gürültü) tek kanala ve 8 kHz'e indirilir, düzlenir, paketlenir.
2. C (alarm_ses.h): aynı 8 kHz örnekler adpcm_kodla ile kodlanır -> JavaScript'in ADPCM baytlarıyla bayt bayt aynı
   olmalı; CRC-32 aynı; başlık alarm_ses_baslik_gecerli'den geçer; adpcm_coz ile çözülen ses özgün sese yakın
   (SNR); 16 kHz'e çıkarma (alarm_ses_iki_kat) parça parça ile tek seferde aynı.
3. Paket dosyası (alarm.eko) urun_akis_test.py'nin yükleme denemesi için de yazılır (--paket YOL).

Kullanım: python firmware/hikaye_oyuncak/tools/alarm_ses_test.py [--paket YOL]   (çıkış kodu 0: geçti)
"""
import argparse
import math
import os
import re
import struct
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
SKETCH = os.path.dirname(TOOLS)

NODE = r'''
const fs = require('fs');
eval(fs.readFileSync(process.argv[2], 'utf8'));
// yapay şarkı: 44,1 kHz, 2 kanal, 14 s; sayfa en çok SN saniye alır
const sr = 44100, L = sr * 14, a = new Float32Array(L), b = new Float32Array(L);
let r = 12345;
const rnd = () => { r = (r * 1103515245 + 12345) & 0x7fffffff; return r / 0x7fffffff - 0.5; };
for (let i = 0; i < L; i++) {
  const t = i / sr, nota = [262, 294, 330, 349, 392][Math.floor(t * 2) % 5];
  a[i] = 0.5 * Math.sin(2 * Math.PI * nota * t) * Math.exp(-((t * 2) % 1) * 3) + 0.05 * rnd();
  b[i] = 0.3 * Math.sin(2 * Math.PI * nota * 2 * t) * Math.exp(-((t * 2) % 1) * 3) + 0.05 * rnd();
}
const buf = { sampleRate: sr, numberOfChannels: 2, length: L, getChannelData: c => (c ? b : a) };
const SN = +process.argv[4];
const y = sekizK(buf, 1.5, SN);
const p = paketle(y, process.argv[5]);
fs.writeFileSync(process.argv[3], Buffer.from(p));
// paketin öncesi: düzlenmiş 8 kHz int16 (C aynı örnekleri kodlasın diye paketle'nin içindeki x'i yeniden kurarız)
let tepe = 0; for (const v of y) tepe = Math.max(tepe, Math.abs(v));
const g = tepe > 1e-4 ? 29000 / tepe : 0, z = 160, x = new Int16Array(y.length);
for (let i = 0; i < y.length; i++) { const f = Math.min(1, i / z, (y.length - 1 - i) / z); x[i] = Math.round(y[i] * g * f); }
fs.writeFileSync(process.argv[3] + '.pcm', Buffer.from(x.buffer));
'''

C = r'''
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "alarm_ses.h"
int main(int argc, char **argv) {
  FILE *f = fopen(argv[1], "rb"); fseek(f, 0, SEEK_END); long nb = ftell(f); fseek(f, 0, SEEK_SET);
  uint8_t *p = malloc(nb); if (fread(p, 1, nb, f) != (size_t)nb) return 2; fclose(f);
  f = fopen(argv[2], "rb"); fseek(f, 0, SEEK_END); long nx = ftell(f) / 2; fseek(f, 0, SEEK_SET);
  int16_t *x = malloc(nx * 2); if (fread(x, 2, nx, f) != (size_t)nx) return 2; fclose(f);
  AlarmSesBaslik b; memcpy(&b, p, sizeof b);
  printf("gecerli %d\n", alarm_ses_baslik_gecerli(&b, 0xB000));
  printf("n %u nx %ld\n", b.n, nx);
  uint8_t *v = calloc(1, (nx + 1) / 2); Adpcm s = {0, 0};
  adpcm_kodla(&s, x, (int)nx, v);
  printf("ayni %d\n", nb == 64 + (nx + 1) / 2 && !memcmp(v, p + 64, (nx + 1) / 2));
  printf("crc %d\n", alarm_crc32(0, p + 64, (int)((nx + 1) / 2)) == b.crc);
  printf("ad %s\n", b.ad);
  int16_t *y = malloc(nx * 2); Adpcm d = {0, 0};
  for (long i = 0; i < nx; i += 512) adpcm_coz(&d, p + 64 + i / 2, (int)(nx - i < 512 ? nx - i : 512), y + i);
  double se = 0, sx = 0;
  for (long i = 0; i < nx; i++) { double e = y[i] - x[i]; se += e * e; sx += (double)x[i] * x[i]; }
  printf("snr %.2f\n", 10 * log10(sx / (se + 1e-9)));
  int16_t *u1 = malloc(nx * 4), *u2 = malloc(nx * 4), o1 = 0, o2 = 0;
  alarm_ses_iki_kat(&o1, y, (int)nx, u1);
  for (long i = 0; i < nx; i += 333) alarm_ses_iki_kat(&o2, y + i, (int)(nx - i < 333 ? nx - i : 333), u2 + 2 * i);
  printf("iki_kat %d\n", !memcmp(u1, u2, nx * 4));
  return 0;
}
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paket", help="paket dosyasını buraya da yaz (urun_akis_test.py yükleme denemesi)")
    a = ap.parse_args()
    sayfa = open(os.path.join(SKETCH, "ayar_sayfa.h"), encoding="utf-8").read()
    js = re.search(r"(var ADIM=.*?)\$\('ses_yukle'\)", sayfa, re.S).group(1)
    sn = int(re.search(r"#define ALARM_SES_SN (\d+)", open(os.path.join(SKETCH, "alarm_ses.h")).read()).group(1))
    d = tempfile.mkdtemp(prefix="alarm_ses_")
    jsy, nodey, pak = os.path.join(d, "f.js"), os.path.join(d, "n.js"), os.path.join(d, "alarm.eko")
    open(jsy, "w", encoding="utf-8").write(js)
    open(nodey, "w").write(NODE)
    subprocess.run(["node", nodey, jsy, pak, str(sn), "Deneme şarkısı (çok uzun bir dosya adı, kırk yedi baytı aşar)"],
                   check=True)
    src, exe = os.path.join(d, "c.c"), os.path.join(d, "c")
    open(src, "w").write(C)
    subprocess.run(["cc", "-O2", "-Wall", "-I" + SKETCH, "-o", exe, src, "-lm"], check=True)
    out = dict(s.split(" ", 1) for s in subprocess.run([exe, pak, pak + ".pcm"], capture_output=True, text=True,
                                                         check=True).stdout.strip().split("\n"))
    hatalar = []

    def dene(k, m):
        if not k:
            hatalar.append(m)
            print("  HATA:", m)

    n, nx = (int(v) for v in re.findall(r"\d+", out["n"]))
    dene(out["gecerli"] == "1", "başlık geçersiz")
    dene(n == nx == sn * 8000, f"örnek sayısı {n} / {nx} (beklenen {sn * 8000})")
    dene(out["ayni"] == "1", "JavaScript ve C ADPCM baytları farklı")
    dene(out["crc"] == "1", "CRC-32 tutmuyor")
    ad = out["ad"].encode("utf-8")
    dene(len(ad) <= 47 and "Deneme şarkısı".encode() in ad, f"ad {out['ad']!r}")
    snr = float(out["snr"])
    dene(snr > 20, f"ADPCM SNR {snr} dB (> 20 beklenir)")
    dene(out["iki_kat"] == "1", "16 kHz'e çıkarma parça parça farklı")
    boyut = os.path.getsize(pak)
    dene(boyut <= 0xB000, f"paket {boyut} B > alarm bölümü")
    print(f"  {n} örnek ({n / 8000:.1f} s), paket {boyut} B, ADPCM SNR {snr:.1f} dB, JS = C bayt bayt")
    if a.paket:
        with open(pak, "rb") as f, open(a.paket, "wb") as g:
            g.write(f.read())
    print(f"alarm_ses_test.py: {'HATA ' + str(len(hatalar)) if hatalar else 'hepsi geçti'}")
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
