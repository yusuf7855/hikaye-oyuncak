"""Hikâye Oyuncağı — kart arayüzü.

ESP32-S3 kartındaki hikâye yazılımını seri porttan (115200) okur ve tarayıcıda canlı gösterir.
Çalıştırma: python arayuz/app.py   (tarayıcı kendiliğinden açılır: http://127.0.0.1:5055)
"""
import codecs
import json
import os
import queue
import re
import threading
import time
import webbrowser
from datetime import datetime

import serial
import serial.tools.list_ports
from flask import Flask, Response, jsonify, request, send_file

KLASOR = os.path.dirname(os.path.abspath(__file__))
GECMIS = os.path.join(KLASOR, "hikayeler.jsonl")
ADRES, PORT_NO = "127.0.0.1", 5055

BASLIK_RE = re.compile(r"^=== (.+?) \| (.+?) \| (\d+) aday ===$")
ADAY_RE = re.compile(r"^aday (\d+)/(\d+): (.*)$")
SON_RE = re.compile(r"--- (\d+) aday, toplam (\d+) token ([\d.]+) s = ([\d.]+) token/s ---")
SON_ISARET = "\n\n--- "
BILGI_ONEK = ("model:", "PSRAM:", "model.bin:", "boş:", "HATA", "model bölümü", "model okunamadı", "mmap")


class Kart:
    """Seri bağlantı + çıktı ayrıştırıcı. Olayları tüm SSE dinleyicilerine dağıtır."""

    def __init__(self):
        self.ser = None
        self.port = None
        self.kilit = threading.Lock()
        self.dinleyiciler = []
        self.figurler, self.yerler, self.bilgi = [], [], []
        self._sifirla_ayristirici()

    def _sifirla_ayristirici(self):
        self.satir = ""          # tamamlanmamış satır (hikâye dışı)
        self.liste_modu = None   # "fig" | "yer" | None
        self.yeni_fig, self.yeni_yer = [], []
        self.hikaye = None       # sürmekte olan hikâye
        self.mesgul = False

    # ---- olay dağıtımı ----
    def yayinla(self, tur, veri):
        paket = f"event: {tur}\ndata: {json.dumps(veri, ensure_ascii=False)}\n\n"
        for q in list(self.dinleyiciler):
            q.put(paket)

    def durum(self):
        return {"bagli": self.ser is not None, "port": self.port, "mesgul": self.mesgul,
                "figurler": self.figurler, "yerler": self.yerler, "bilgi": self.bilgi}

    # ---- bağlantı ----
    def baglan(self, port):
        self.kes()
        s = serial.Serial()
        s.port, s.baudrate, s.timeout = port, 115200, 0.1
        s.dtr = False  # dtr/rts açık kalırsa kart yükleme moduna düşebilir
        s.rts = False
        s.open()
        self.ser, self.port = s, port
        self._sifirla_ayristirici()
        self.bilgi = []
        threading.Thread(target=self._oku, args=(s,), daemon=True).start()
        # Port açılınca kart çoğunlukla yeniden başlar ve listeyi kendisi yazar; yazmazsa "?" iste.
        threading.Thread(target=self._liste_iste, args=(s,), daemon=True).start()
        self.yayinla("durum", self.durum())

    def _liste_iste(self, s):
        time.sleep(4)
        if self.ser is s and not self.figurler:
            self.gonder("?")

    def kes(self):
        s, self.ser = self.ser, None
        if s:
            try:
                s.close()
            except Exception:
                pass
        self.port = None
        self.mesgul = False
        self.yayinla("durum", self.durum())

    def gonder(self, komut):
        if not self.ser:
            raise RuntimeError("Kart bağlı değil")
        with self.kilit:
            self.ser.write((komut + "\n").encode("utf-8"))
        self.yayinla("ham", f"\n>>> {komut}\n")

    # ---- okuma ----
    def _oku(self, s):
        coz = codecs.getincrementaldecoder("utf-8")(errors="replace")
        while self.ser is s:
            try:
                veri = s.read(512)
            except Exception as e:
                self.yayinla("hata", f"Seri port okunamadı: {e}")
                self.kes()
                return
            if not veri:
                continue
            metin = coz.decode(veri).replace("\r", "")
            if metin:
                self.yayinla("ham", metin)
                self._ayristir(metin)

    def _ayristir(self, metin):
        for ch in metin:
            if self.hikaye is not None:
                self._hikaye_karakter(ch)
                continue
            if ch == "\n":
                self._satir(self.satir)
                self.satir = ""
            else:
                self.satir += ch
        if self.hikaye is not None:
            self._hikaye_akit()

    def _satir(self, satir):
        s = satir.strip()
        if s == "Figürler:":
            self.liste_modu, self.yeni_fig = "fig", []
            return
        if s == "Yerler:":
            self.liste_modu, self.yeni_yer = "yer", []
            return
        m = re.match(r"^(\d+)\s+(.+)$", s)
        if self.liste_modu and m:
            (self.yeni_fig if self.liste_modu == "fig" else self.yeni_yer).append(
                {"no": int(m.group(1)), "ad": m.group(2)})
            return
        if self.liste_modu == "yer":
            self.figurler, self.yerler = self.yeni_fig, self.yeni_yer
            self.yayinla("durum", self.durum())
        self.liste_modu = None
        if s.startswith("=== Hikâye Oyuncağı"):
            self.bilgi = []
        if s.startswith(BILGI_ONEK):
            self.bilgi.append(s)
            self.yayinla("durum", self.durum())
        if s.startswith("Anlaşılmadı"):
            self.mesgul = False
            self.yayinla("hata", s)
            self.yayinla("durum", self.durum())
        m = BASLIK_RE.match(s)
        if m:
            figler = [f.strip() for f in m.group(1).split(" + ")]
            self.hikaye = {"figurler": figler, "yer": m.group(2), "aday": int(m.group(3)),
                           "ham": "", "gonderilen": 0, "adaylar": 0, "basladi": time.time()}
            self.mesgul = True
            self.yayinla("basla", {k: self.hikaye[k] for k in ("figurler", "yer", "aday")})
            self.yayinla("durum", self.durum())

    def _hikaye_karakter(self, ch):
        h = self.hikaye
        h["ham"] += ch
        if ch == "\n" and "Sorun:" not in h["ham"]:
            # hikâyeden önceki aday satırları (4 aday modunda)
            satirlar = h["ham"].split("\n")
            for sat in satirlar[h["adaylar"]:-1]:
                m = ADAY_RE.match(sat.strip())
                if m:
                    self.yayinla("aday", {"no": int(m.group(1)), "toplam": int(m.group(2)), "bilgi": m.group(3)})
            h["adaylar"] = len(satirlar) - 1
        m = SON_RE.search(h["ham"])
        if m and h["ham"].endswith("\n"):
            self._hikaye_bitir(m)

    def _metin(self, ham, bitti=False):
        i = ham.find("Sorun:")
        if i < 0:
            return ""
        t = ham[i:]
        j = t.find(SON_ISARET)
        if j >= 0:
            return t[:j]
        if bitti:
            return t
        # sondaki "\n\n--- " öneki olabilecek parçayı henüz gönderme
        for k in range(min(len(SON_ISARET), len(t)), 0, -1):
            if SON_ISARET.startswith(t[-k:]):
                return t[:-k]
        return t

    def _hikaye_akit(self):
        h = self.hikaye
        if h is None:
            return
        t = self._metin(h["ham"])
        if len(t) > h["gonderilen"]:
            self.yayinla("parca", t[h["gonderilen"]:])
            h["gonderilen"] = len(t)

    def _hikaye_bitir(self, m):
        h, self.hikaye = self.hikaye, None
        metin = self._metin(h["ham"], bitti=True)
        if len(metin) > h["gonderilen"]:
            self.yayinla("parca", metin[h["gonderilen"]:])
        plan, _, govde = metin.partition("\n\n")
        sorun = cozum = ""
        for sat in plan.split("\n"):
            if sat.startswith("Sorun:"):
                sorun = sat[6:].strip()
            elif sat.startswith("Çözüm:"):
                cozum = sat[6:].strip()
        kayit = {
            "tarih": datetime.now().isoformat(timespec="seconds"),
            "figurler": h["figurler"], "yer": h["yer"], "aday": int(m.group(1)),
            "token": int(m.group(2)), "sure_s": float(m.group(3)), "token_s": float(m.group(4)),
            "sorun": sorun, "cozum": cozum, "hikaye": govde.strip(),
        }
        if not govde.strip():
            # Plan ORNEKLE_PLAN_SINIR token'da bitmediyse kart durur ("plan bozuk"); metni olduğu gibi sakla.
            kayit.update(plan_bozuk=True, sorun="", cozum="", hikaye=metin.strip())
        with open(GECMIS, "a", encoding="utf-8") as f:
            f.write(json.dumps(kayit, ensure_ascii=False) + "\n")
        self.mesgul = False
        self.satir = ""
        self.yayinla("bitti", kayit)
        self.yayinla("durum", self.durum())


kart = Kart()
app = Flask(__name__)


@app.get("/")
def ana():
    return send_file(os.path.join(KLASOR, "index.html"))


@app.get("/api/portlar")
def portlar():
    liste = []
    for p in serial.tools.list_ports.comports():
        if "Bluetooth" in p.device or "debug-console" in p.device:
            continue
        liste.append({"ad": p.device, "aciklama": p.description or "",
                      "esp": (p.vid == 0x303A) or "usbmodem" in p.device or "ttyACM" in p.device})
    liste.sort(key=lambda p: not p["esp"])
    return jsonify(liste)


@app.get("/api/durum")
def durum():
    return jsonify(kart.durum())


@app.post("/api/baglan")
def baglan():
    port = (request.json or {}).get("port")
    try:
        kart.baglan(port)
    except Exception as e:
        return jsonify({"hata": f"{port} açılamadı: {e}"}), 400
    return jsonify(kart.durum())


@app.post("/api/kes")
def kes():
    kart.kes()
    return jsonify(kart.durum())


@app.post("/api/yaz")
def yaz():
    v = request.json or {}
    if kart.mesgul:
        return jsonify({"hata": "Kart şu an yazıyor, bitmesini bekleyin."}), 409
    if v.get("rastgele"):
        komut = "r"
    else:
        figler = [int(f) for f in v.get("figurler", []) if f]
        if not 1 <= len(figler) <= 2 or len(set(figler)) != len(figler):
            return jsonify({"hata": "Bir ya da iki farklı figür seçin."}), 400
        komut = f"{','.join(map(str, figler))} {int(v['yer'])}"
        aday = int(v.get("aday", 1))
        if aday > 1:
            komut += f" {aday}"
    try:
        kart.gonder(komut)
    except Exception as e:
        return jsonify({"hata": str(e)}), 400
    kart.mesgul = True
    kart.yayinla("durum", kart.durum())
    return jsonify({"komut": komut})


@app.post("/api/komut")
def komut():
    try:
        kart.gonder((request.json or {}).get("komut", "").strip())
    except Exception as e:
        return jsonify({"hata": str(e)}), 400
    return jsonify({"ok": True})


@app.get("/api/gecmis")
def gecmis():
    kayitlar = []
    if os.path.exists(GECMIS):
        with open(GECMIS, encoding="utf-8") as f:
            for sat in f:
                if sat.strip():
                    try:
                        kayitlar.append(json.loads(sat))
                    except ValueError:
                        pass
    return jsonify(kayitlar[::-1])


@app.get("/api/olaylar")
def olaylar():
    q = queue.Queue()
    kart.dinleyiciler.append(q)

    def akis():
        try:
            yield f"event: durum\ndata: {json.dumps(kart.durum(), ensure_ascii=False)}\n\n"
            while True:
                try:
                    yield q.get(timeout=15)
                except queue.Empty:
                    yield ": canli\n\n"
        finally:
            kart.dinleyiciler.remove(q)

    return Response(akis(), mimetype="text/event-stream; charset=utf-8",
                    headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


if __name__ == "__main__":
    url = f"http://{ADRES}:{PORT_NO}"
    print(f"Hikâye arayüzü: {url}  (kapatmak için Ctrl+C)")
    if not os.environ.get("TARAYICI_ACMA"):
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()
    app.run(host=ADRES, port=PORT_NO, threaded=True, debug=False)
