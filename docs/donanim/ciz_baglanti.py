"""Bağlantı şeması (baglanti.svg) ve blok şeması (blok.svg) üretir. Yalnız standart kütüphane.

    python docs/donanim/ciz_baglanti.py

Pin haritası docs/URUN_TANIMI.md ile aynıdır (değişirse önce orası, sonra burası ve firmware/donanim.h).
"""
import os

BURASI = os.path.dirname(os.path.abspath(__file__))

RENK = {
    "kırmızı": "#d62728", "siyah": "#222222", "turuncu": "#ff8c00", "sarı": "#d4a800", "yeşil": "#2ca02c",
    "mavi": "#1f77b4", "mor": "#9467bd", "beyaz": "#9a9a9a", "kahverengi": "#8c564b", "gri": "#6f6f6f",
}

# DevKitC-1 J1 başlığı (Espressif kullanıcı kılavuzu v1.1, J1 1..22)
J1 = ["3V3", "3V3", "RST", "GPIO4", "GPIO5", "GPIO6", "GPIO7", "GPIO15", "GPIO16", "GPIO17", "GPIO18",
      "GPIO8", "GPIO3", "GPIO46", "GPIO9", "GPIO10", "GPIO11", "GPIO12", "GPIO13", "GPIO14", "5V", "GND"]

# (J1 ucu, modül, modül ucu, renk, kablo, açıklama)
SINYAL = [
    (4, "MAX98357A", "BCLK", "sarı", "26 AWG", "I2S0 BCLK"),
    (5, "MAX98357A", "LRC", "yeşil", "26 AWG", "I2S0 LRC (WS)"),
    (6, "MAX98357A", "DIN", "mavi", "26 AWG", "I2S0 DIN"),
    (7, "MAX98357A", "SD", "beyaz", "26 AWG", "SD: LOW = uyku, HIGH = sol kanal"),
    (8, "INMP441", "SCK", "sarı", "26 AWG", "I2S1 SCK"),
    (9, "INMP441", "WS", "yeşil", "26 AWG", "I2S1 WS"),
    (10, "INMP441", "SD", "mavi", "26 AWG", "I2S1 SD (veri)"),
    (11, "74AHCT1G125", "2 A", "mor", "26 AWG", "halka verisi 3,3 V"),
    (15, "RC522", "RST", "gri", "26 AWG", "RC522 RST"),
    (16, "RC522", "SDA", "kahverengi", "26 AWG", "SPI SS"),
    (17, "RC522", "MOSI", "mavi", "26 AWG", "SPI MOSI"),
    (18, "RC522", "SCK", "sarı", "26 AWG", "SPI SCK"),
    (19, "RC522", "MISO", "yeşil", "26 AWG", "SPI MISO"),
]

MODUL = {   # ad: (x, y_üst, uçlar (sol kenar), alt başlık)
    "MAX98357A": (930, 120, ["LRC", "BCLK", "DIN", "GAIN", "SD", "GND", "VIN"], "I2S yükselteç (Adafruit 3006)"),
    "INMP441": (930, 330, ["SCK", "WS", "L/R", "SD", "VDD", "GND"], "I2S MEMS mikrofon, 3,3 V!"),
    "RC522": (930, 510, ["SDA", "SCK", "MOSI", "MISO", "IRQ", "GND", "RST", "3.3V"], "NFC okuyucu 13,56 MHz, 3,3 V"),
    "74AHCT1G125": (930, 760, ["1 OE", "2 A", "3 GND", "5 VCC"], "seviye çevirici 3,3→5 V (SOT-23-5)"),
}
ADIM = 24
Y_5V, Y_3V3, Y_GND = 62, 88, 960
DEV_X, DEV_Y = 330, 150


def pin_y_dev(no):
    return DEV_Y + 20 + (no - 1) * 25


def pin_y_mod(ad, uc):
    x, y, uclar, _ = MODUL[ad]
    return y + 34 + uclar.index(uc) * ADIM


class Svg:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.p = []

    def e(self, s):
        self.p.append(s)

    def cizgi(self, pts, renk, w=2.2, dash=None):
        d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.e(f'<polyline points="{d}" fill="none" stroke="{renk}" stroke-width="{w}" '
               f'stroke-linejoin="round"{da}/>')

    def yazi(self, x, y, s, boy=12, renk="#111", hiza="start", kalin=False, dondur=None):
        s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        k = ' font-weight="bold"' if kalin else ""
        r = f' transform="rotate({dondur} {x} {y})"' if dondur is not None else ""
        self.e(f'<text x="{x}" y="{y}" font-size="{boy}" fill="{renk}" text-anchor="{hiza}"{k}{r}>{s}</text>')

    def kutu(self, x, y, w, h, dolgu="#f4f6fa", kenar="#333", rx=6):
        self.e(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{dolgu}" stroke="{kenar}" '
               f'stroke-width="1.5"/>')

    def nokta(self, x, y, renk="#111", r=3.5):
        self.e(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{renk}"/>')

    def ok(self, x0, y0, x1, y1, renk="#333", w=2):
        self.e(f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{renk}" stroke-width="{w}" '
               f'marker-end="url(#ok)"/>')

    def yaz(self, yol):
        bas = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
               f'viewBox="0 0 {self.w} {self.h}" font-family="DejaVu Sans, Arial, sans-serif">\n'
               '<defs><marker id="ok" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">'
               '<path d="M0,0 L10,4 L0,8 z" fill="#333"/></marker></defs>\n'
               f'<rect width="{self.w}" height="{self.h}" fill="#ffffff"/>\n')
        with open(yol, "w", encoding="utf-8") as f:
            f.write(bas + "\n".join(self.p) + "\n</svg>\n")


def baglanti():
    s = Svg(1440, 1010)
    s.yazi(20, 30, "Masal standı — bağlantı şeması (ESP32-S3-DevKitC-1 N16R8, pin haritası: docs/URUN_TANIMI.md)",
           18, kalin=True)
    # raylar
    s.cizgi([(150, Y_5V), (1400, Y_5V)], RENK["kırmızı"], 4)
    s.yazi(144, Y_5V + 5, "5V", 13, RENK["kırmızı"], hiza="end", kalin=True)
    s.cizgi([(300, Y_3V3), (940, Y_3V3)], RENK["turuncu"], 3.5)
    s.yazi(946, Y_3V3 + 4, "3V3 (DevKit LDO, ≤ 0,8 A)", 12, RENK["turuncu"], kalin=True)
    s.cizgi([(150, Y_GND), (1400, Y_GND)], RENK["siyah"], 4)
    s.yazi(144, Y_GND + 5, "GND", 13, hiza="end", kalin=True)
    s.yazi(160, Y_5V - 8, "5V rayı 22 AWG", 11, RENK["kırmızı"])
    s.yazi(160, Y_GND + 18, "GND 22 AWG — yıldız toprak: bütün GND'ler taşıyıcı karttaki tek noktada buluşur", 11)

    # USB-C girişi + PTC + TVS
    s.kutu(20, 150, 130, 170)
    s.yazi(85, 172, "USB-C dişi kart", 12, hiza="middle", kalin=True)
    s.yazi(85, 189, "5,1 kΩ CC1/CC2→GND", 10, hiza="middle")
    for i, (u, r) in enumerate((("VBUS", "kırmızı"), ("GND", "siyah"), ("CC1", "gri"), ("CC2", "gri"))):
        y = 215 + i * 24
        s.yazi(140, y + 4, u, 11, hiza="end")
        s.nokta(150, y, RENK[r], 3)
    s.yazi(85, 312, "5 V / 2 A adaptör", 10, hiza="middle")
    s.cizgi([(150, 215), (172, 215)], RENK["kırmızı"], 3)
    s.kutu(172, 205, 52, 20, "#ffe9d6", rx=3)
    s.yazi(198, 219, "PTC 2,5A", 10, hiza="middle")
    s.cizgi([(224, 215), (245, 215), (245, Y_5V)], RENK["kırmızı"], 3)
    s.nokta(245, Y_5V, RENK["kırmızı"])
    s.cizgi([(150, 239), (170, 239), (170, Y_GND)], RENK["siyah"], 3)
    s.nokta(170, Y_GND)
    s.cizgi([(245, 130), (275, 130), (275, 140)], RENK["kırmızı"], 2)
    s.nokta(245, 130, RENK["kırmızı"], 3)
    s.kutu(266, 140, 18, 36, "#fff", rx=2)
    s.yazi(286, 194, "TVS", 8)
    s.yazi(286, 205, "SMAJ5.0A", 8)
    s.cizgi([(275, 176), (275, 255), (170, 255)], RENK["siyah"], 1.5)
    s.nokta(170, 255, RENK["siyah"], 3)

    # DevKit
    s.kutu(DEV_X, DEV_Y - 10, 150, 22 * 25 + 30, "#eef3ff")
    for i, t in enumerate(("ESP32-S3-", "DevKitC-1", "N16R8")):
        s.yazi(DEV_X + 8, DEV_Y + 250 + i * 18, t, 13, kalin=True)
    s.yazi(DEV_X + 8, DEV_Y + 314, "J1 başlığı →", 10)
    xd = DEV_X + 150
    for i, ad in enumerate(J1, 1):
        y = pin_y_dev(i)
        s.yazi(xd - 6, y + 4, f"{i} {ad}", 11, hiza="end")
        s.nokta(xd, y, "#555", 2.5)
    s.yazi(DEV_X, DEV_Y + 22 * 25 + 40, "Kullanılmaz: 0, 3, 45, 46 (açılış), 19/20 (USB), 26–37 (flash/PSRAM),"
           " 43/44 (UART), 48/38 (RGB LED)", 11)

    # modüller
    for ad, (x, y, uclar, alt) in MODUL.items():
        h = 34 + len(uclar) * ADIM
        s.kutu(x, y, 150, h)
        s.yazi(x + 75, y + 18, ad, 13, hiza="middle", kalin=True)
        s.yazi(x + 75, y + h + 14, alt, 10, hiza="middle")
        for u in uclar:
            yy = pin_y_mod(ad, u)
            s.yazi(x + 8, yy + 4, u, 11)
            s.nokta(x, yy, "#555", 2.5)

    kanal = [524 + i * 24 for i in range(16)]
    for ki, (no, ad, uc, renk, awg, acik) in enumerate(SINYAL):
        yd = pin_y_dev(no)
        ym = pin_y_mod(ad, uc)
        xc = kanal[ki]
        s.cizgi([(xd, yd), (xc, yd), (xc, ym), (MODUL[ad][0], ym)], RENK[renk])
        s.yazi(842, ym - 4, f"GPIO{J1[no - 1][4:]}", 9, RENK[renk] if renk != "beyaz" else "#666")

    # güç: DevKit
    s.cizgi([(xd, pin_y_dev(1)), (492, pin_y_dev(1)), (492, Y_3V3)], RENK["turuncu"], 3)
    s.nokta(492, Y_3V3, RENK["turuncu"])
    s.cizgi([(xd, pin_y_dev(21)), (502, pin_y_dev(21)), (502, Y_5V)], RENK["kırmızı"], 3)
    s.nokta(502, Y_5V, RENK["kırmızı"])
    s.cizgi([(xd, pin_y_dev(22)), (512, pin_y_dev(22)), (512, Y_GND)], RENK["siyah"], 3)
    s.nokta(512, Y_GND)

    # güç: modüller
    guc = [("MAX98357A", "VIN", Y_5V, "kırmızı"), ("MAX98357A", "GND", Y_GND, "siyah"),
           ("INMP441", "VDD", Y_3V3, "turuncu"), ("INMP441", "GND", Y_GND, "siyah"),
           ("INMP441", "L/R", Y_GND, "siyah"),
           ("RC522", "3.3V", Y_3V3, "turuncu"), ("RC522", "GND", Y_GND, "siyah"),
           ("74AHCT1G125", "5 VCC", Y_5V, "kırmızı"), ("74AHCT1G125", "3 GND", Y_GND, "siyah"),
           ("74AHCT1G125", "1 OE", Y_GND, "siyah")]
    xg = [906, 914, 922]
    for ad, uc, yr, renk in guc:
        ym = pin_y_mod(ad, uc)
        idx = [g for g in guc if g[0] == ad].index((ad, uc, yr, renk))
        xc = xg[idx % 3]
        s.cizgi([(MODUL[ad][0], ym), (xc, ym), (xc, yr)], RENK[renk], 2.4)
        s.nokta(xc, yr, RENK[renk], 3)
    s.yazi(1090, pin_y_mod("MAX98357A", "GAIN") + 4, "GAIN boş = 9 dB", 10, "#666")
    s.yazi(1090, pin_y_mod("MAX98357A", "SD") + 4, "SD: LOW uyku, HIGH (3,3 V) = sol kanal", 10, "#666")
    s.yazi(1090, pin_y_mod("RC522", "IRQ") + 4, "IRQ boş", 10, "#666")
    s.yazi(1090, pin_y_mod("RC522", "SDA") + 4, "bileşen yüzü aşağı, kabloyla lehimli", 10, "#666")
    s.yazi(1090, pin_y_mod("INMP441", "L/R") + 4, "L/R → GND (sol kanal)", 10, "#666")
    s.yazi(1090, pin_y_mod("INMP441", "VDD") + 4, "VDD yalnız 3V3 (5 V bozar)", 10, RENK["kırmızı"])

    # hoparlör
    x, y = MODUL["MAX98357A"][0] + 150, MODUL["MAX98357A"][1]
    s.cizgi([(x, y + 60), (1200, y + 60)], RENK["kırmızı"], 2.4)
    s.cizgi([(x, y + 84), (1200, y + 84)], RENK["siyah"], 2.4)
    s.yazi(x + 6, y + 54, "+  (24 AWG, burgulu, ≤ 10 cm)", 9)
    s.yazi(x + 6, y + 100, "−", 10)
    s.e(f'<rect x="1200" y="{y + 52}" width="16" height="40" fill="#ddd" stroke="#333"/>')
    s.e(f'<polygon points="1216,{y + 52} 1250,{y + 30} 1250,{y + 114} 1216,{y + 92}" fill="#eee" stroke="#333"/>')
    s.yazi(1270, y + 66, "Hoparlör", 12, kalin=True)
    s.yazi(1270, y + 82, "4 Ω 3 W, Ø40", 11)
    s.yazi(1090, pin_y_mod("MAX98357A", "VIN") + 4, "+ 470 µF VIN–GND (amp ucunda)", 10)

    # seviye çevirici -> 330 Ω -> halka, 1000 µF
    x, y = MODUL["74AHCT1G125"][0] + 150, pin_y_mod("74AHCT1G125", "2 A")
    s.yazi(x - 8, y + 4, "4 Y", 11, hiza="end")
    s.nokta(x, y, "#555", 2.5)
    s.cizgi([(x, y), (1110, y)], RENK["mor"], 2.4)
    s.e(f'<rect x="1110" y="{y - 7}" width="40" height="14" fill="#fff6c8" stroke="#333"/>')
    s.yazi(1130, y - 12, "330 Ω", 11, hiza="middle")
    s.yazi(1130, y + 26, "halka ucunda", 9, hiza="middle")
    s.cizgi([(1150, y), (1220, y)], RENK["mor"], 2.4)
    s.kutu(1220, y - 40, 150, 130, "#fff4f4")
    s.yazi(1295, y - 22, "NeoPixel halka", 13, hiza="middle", kalin=True)
    s.yazi(1295, y - 8, "Ø104/Ø90, 35 LED (WS2812B)", 9, hiza="middle")
    s.yazi(1228, y + 4, "DIN", 11)
    s.nokta(1220, y, "#555", 2.5)
    for i, (u, r) in enumerate((("5V", "kırmızı"), ("GND", "siyah"))):
        yy = y + 28 + i * 28
        s.yazi(1362, yy + 4, u, 11, hiza="end")
        s.nokta(1370, yy, "#555", 2.5)
    s.cizgi([(1370, y + 28), (1392, y + 28), (1392, Y_5V)], RENK["kırmızı"], 3)
    s.nokta(1392, Y_5V, RENK["kırmızı"])
    s.cizgi([(1370, y + 56), (1380, y + 56), (1380, Y_GND)], RENK["siyah"], 3)
    s.nokta(1380, Y_GND)
    # 1000 µF: halkanın 5V düğümü (1392, y+28) ile GND hattı (1380) arasında
    s.cizgi([(1392, y + 28), (1410, y + 28), (1410, y + 66)], RENK["kırmızı"], 1.5)
    s.nokta(1392, y + 28, RENK["kırmızı"], 2.5)
    s.e(f'<rect x="1400" y="{y + 66}" width="20" height="3" fill="#333"/>')
    s.e(f'<rect x="1400" y="{y + 72}" width="20" height="3" fill="#999"/>')
    s.cizgi([(1410, y + 75), (1410, y + 84), (1380, y + 84)], RENK["siyah"], 1.5)
    s.nokta(1380, y + 84, RENK["siyah"], 2.5)
    s.yazi(1220, y + 120, "1000 µF 10–16 V", 11, kalin=True)
    s.yazi(1220, y + 134, "halkanın 5V–GND ucunda", 10)

    # açıklama
    s.yazi(20, 360, "Renkler (öneri):", 12, kalin=True)
    for i, (a, b) in enumerate([("kırmızı", "5 V (22 AWG)"), ("siyah", "GND (22 AWG)"), ("turuncu", "3V3"),
                                ("sarı", "saat: BCLK/SCK"), ("yeşil", "LRC/WS, MISO"), ("mavi", "veri: DIN/SD/MOSI"),
                                ("mor", "halka verisi"), ("kahverengi", "SPI SS"), ("gri", "RST"),
                                ("beyaz", "amp SD (kapatma)")]):
        y = 380 + i * 20
        s.cizgi([(24, y), (60, y)], RENK[a], 4)
        s.yazi(66, y + 4, f"{a}: {b}", 11)
    for i, t in enumerate(("Sinyal: 26 AWG silikon kablo.", "I2S ve SPI ≤ 15 cm.", "Mikrofon kablosu hoparlör/",
                           "amp kablolarından ayrı yoldan.", "Halka ve RC522 kabloları", "kapağa gider: 10 cm",
                           "servis payı bırakın.")):
        s.yazi(20, 600 + i * 15, t, 11)
    s.yaz(os.path.join(BURASI, "baglanti.svg"))


def blok():
    s = Svg(1100, 500)
    s.yazi(20, 30, "Masal standı — blok şeması", 18, kalin=True)

    def b(x, y, w, h, ust, alt="", dolgu="#eef3ff"):
        s.kutu(x, y, w, h, dolgu)
        s.yazi(x + w / 2, y + h / 2 - (4 if alt else -4), ust, 13, hiza="middle", kalin=True)
        if alt:
            s.yazi(x + w / 2, y + h / 2 + 14, alt, 10, hiza="middle")
    b(20, 230, 150, 70, "USB-C 5 V / 2 A", "arka giriş, 5,1 kΩ CC", "#fff4e0")
    b(220, 230, 120, 70, "PTC + TVS", "2,5 A · SMAJ5.0A", "#fff4e0")
    b(400, 200, 220, 130, "ESP32-S3-DevKitC-1", "N16R8 · LLM + ses + KWS")
    s.yazi(510, 300, "LDO 3V3 (SGM2212)", 10, hiza="middle")
    b(720, 60, 170, 60, "MAX98357A", "I2S0 · 5 V")
    b(940, 60, 140, 60, "Hoparlör", "Ø40 4 Ω 3 W", "#f2f2f2")
    b(720, 150, 170, 60, "INMP441", "I2S1 · 3,3 V")
    b(720, 240, 170, 60, "RC522", "SPI · 3,3 V")
    b(940, 240, 140, 60, "NTAG213 Ø25", "figür tabanında", "#f2f2f2")
    b(720, 340, 170, 60, "74AHCT1G125", "3,3 → 5 V · 330 Ω")
    b(940, 340, 140, 60, "NeoPixel halka", "Ø104 · 1000 µF", "#fff4f4")
    s.ok(170, 265, 218, 265)
    s.ok(340, 265, 398, 265)
    s.ok(620, 230, 718, 90)
    s.yazi(640, 140, "GPIO4/5/6/7", 10)
    s.ok(718, 180, 622, 250)
    s.yazi(640, 205, "GPIO15/16/17", 10)
    s.ok(620, 275, 718, 270)
    s.ok(718, 280, 622, 285)
    s.yazi(632, 265, "SPI 9–13", 10)
    s.ok(620, 310, 718, 370)
    s.yazi(640, 350, "GPIO18", 10)
    s.ok(890, 90, 938, 90)
    s.ok(890, 370, 938, 370)
    s.e('<line x1="890" y1="270" x2="938" y2="270" stroke="#333" stroke-width="2" stroke-dasharray="5,4"/>')
    s.yazi(900, 262, "13,56 MHz", 9)
    s.yazi(20, 430, "5 V rayı: DevKit (5V pini), MAX98357A VIN, 74AHCT1G125 VCC, halka.  3V3 rayı (DevKit LDO): "
           "RC522, INMP441.", 12)
    s.yazi(20, 452, "Akım bütçesi (en kötü an): halka 0,6 A (yazılım sınırı) + hoparlör 0,7 A + ESP32 0,35 A + RC522 "
           "0,1 A ≈ 1,75 A < 2 A.", 12)
    s.yazi(20, 474, "Mikrofon arkada üstte, hoparlör önde altta (≈125 mm); ses ve halka kabloları mikrofon "
           "kablosundan ayrı yoldan.", 12)
    s.yaz(os.path.join(BURASI, "blok.svg"))


if __name__ == "__main__":
    baglanti()
    blok()
    print("baglanti.svg, blok.svg yazıldı")
