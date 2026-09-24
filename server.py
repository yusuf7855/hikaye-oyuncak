"""Hikâye oyuncağı test arayüzü. Çalıştır: .venv/bin/python server.py  ->  http://localhost:8765

Akış, oyuncakta olacağı gibi cümle cümle: model token üretir -> cümle bitince
Türkçe'ye çevrilir -> Piper (offline Türkçe ses) seslendirir. Çeviri geçici;
Türkçe model eğitilince bu adım kalkar.
"""
import glob, io, json, os, random, re, subprocess, sys, threading, time, wave
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import ctranslate2
import sentencepiece as spm
from piper import PiperVoice, SynthesisConfig
from tokenizers import Tokenizer

from baslangic import KAR, yasak_idler
TUR_KIMLIK = {k["tur"]: kid for kid, k in KAR.items()}

HERE = os.path.dirname(os.path.abspath(__file__))
PORT = 8765
# "tr": doğrudan Türkçe eğitilmiş model (çeviri yok). "en": orijinal İngilizce model + çeviri.
MODELS = {"oyuncak2": {"dir": "hf_v2", "translate": False}, "oyuncak": {"dir": "hf_trft", "translate": False}, "tr": {"dir": "hf_tr", "translate": False},
          "en": {"dir": "hf", "translate": True}}
_toks = {}


def model_files(name):
    m = MODELS[name]
    d = os.path.join(HERE, m["dir"])
    if name not in _toks:
        t = Tokenizer.from_file(os.path.join(d, "tokenizer.json"))
        _toks[name] = (t, {t.token_to_id(x) for x in ("<|endoftext|>", "</s>", "<eos>") if t.token_to_id(x) is not None})
    return os.path.join(d, "model.bin"), _toks[name][0], _toks[name][1], m["translate"]


def available_models():
    return [n for n, m in MODELS.items() if os.path.exists(os.path.join(HERE, m["dir"], "model.bin"))]

TR_DIR = os.path.join(HERE, "tr/translate-en_tr-1_5")
sp = spm.SentencePieceProcessor(model_file=os.path.join(TR_DIR, "sentencepiece.model"))
translator = ctranslate2.Translator(os.path.join(TR_DIR, "model"), device="cpu")
voice = PiperVoice.load(os.path.join(HERE, "voices/tr_TR-dfki-medium.onnx"))
voice_lock = threading.Lock()

# Cümle sonu: . ! ? (ardından isteğe bağlı tırnak) ve boşluk/satır sonu.
SENT_END = re.compile(r'[.!?]["”\']?(?=\s)|\n')


# Çevirmenin bilmediği çocuk dili kelimeleri: çeviriden önce bildiği karşılıklarla değiştir.
GLOSSARY = [(r"\bbunny\b", "rabbit"), (r"\bBunny\b", "Rabbit"), (r"\bbunnies\b", "rabbits"),
            (r"\bkitty\b", "cat"), (r"\bpuppy\b", "dog"), (r"\bdoggy\b", "dog"), (r"\bbirdie\b", "bird")]


def translate(en):
    for pat, rep in GLOSSARY:
        en = re.sub(pat, rep, en)
    res = translator.translate_batch([sp.encode(en, out_type=str)], beam_size=2)
    return sp.decode(res[0].hypotheses[0])


def split_ready(buf):
    """Tamamlanmış cümleleri ayır; açık tırnak içindeyken bölme."""
    out, start = [], 0
    for m in SENT_END.finditer(buf):
        piece = buf[start:m.end()]
        if (piece.count('"') + piece.count('“') + piece.count('”')) % 2:
            continue  # konuşma henüz kapanmadı
        if piece.strip():
            out.append(piece.strip())
        start = m.end()
    return out, buf[start:]


def egitim_durumu():
    """runs/*.progress.json dosyaları + eğitim süreci çalışıyor mu + oyuncak hikâyesi sayıları."""
    runs = []
    for yol in sorted(glob.glob(os.path.join(HERE, "runs", "*.progress.json")), key=os.path.getmtime, reverse=True):
        try:
            d = json.load(open(yol))
        except (OSError, ValueError):
            continue
        d["age"] = time.time() - d.get("updated", 0)
        runs.append(d)
    ps = subprocess.run(["pgrep", "-f", "research.tinystories.train"], capture_output=True, text=True)
    hikaye = {"gecerli": 0, "sorunlu": 0, "kombinasyon": 0, "hedef": 1248, "hedef_kombi": 138}
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("kontrol_v2", os.path.join(HERE, "data", "oyuncak_v2", "kontrol.py"))
        kontrol = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(kontrol)
        iyi, kotu = kontrol.oku()
        tek = {(h["turler"][0], h["yer"]) for h in iyi if len(h["turler"]) == 1}
        cift = {tuple(sorted(h["turler"])) for h in iyi if len(h["turler"]) == 2}
        hikaye.update(gecerli=len(iyi), sorunlu=len(kotu), kombinasyon=len(tek) + len(cift))
    except Exception as e:
        hikaye["hata"] = str(e)
    return {"runs": runs, "calisiyor": bool(ps.stdout.strip()), "hikaye": hikaye}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        url = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        if url.path == "/":
            self.reply(200, "text/html; charset=utf-8", open(os.path.join(HERE, "ui.html"), "rb").read())
        elif url.path == "/generate":
            self.generate(q)
        elif url.path == "/tts":
            self.tts(q)
        elif url.path == "/api/karakterler":
            self.reply(200, "application/json", open(os.path.join(HERE, "data", "karakterler.json"), "rb").read())
        elif url.path == "/api/modeller":
            self.reply(200, "application/json", json.dumps(available_models()).encode())
        elif url.path == "/egitim":
            self.reply(200, "text/html; charset=utf-8", open(os.path.join(HERE, "egitim.html"), "rb").read())
        elif url.path == "/api/egitim":
            self.reply(200, "application/json", json.dumps(egitim_durumu()).encode())
        else:
            self.send_error(404)

    def do_POST(self):
        if urlparse(self.path).path == "/api/egitim/baslat":
            r = subprocess.run([os.path.join(HERE, "egit_c1.sh")], capture_output=True, text=True)
            self.reply(200, "application/json", json.dumps({"mesaj": (r.stdout or r.stderr).strip()}).encode())
        else:
            self.send_error(404)

    def reply(self, code, ctype, body):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def tts(self, q):
        text = q.get("text", "").strip()
        if not text:
            return self.send_error(400)
        cfg = SynthesisConfig(length_scale=float(q.get("length", 1.0)))
        bio = io.BytesIO()
        with voice_lock, wave.open(bio, "wb") as w:
            voice.synthesize_wav(text, w, syn_config=cfg)
        try:
            self.reply(200, "audio/wav", bio.getvalue())
        except (BrokenPipeError, ConnectionResetError):
            pass

    def send_event(self, obj):
        self.wfile.write(f"data: {json.dumps(obj, ensure_ascii=False)}\n\n".encode())
        self.wfile.flush()

    def generate(self, q):
        name = q.get("model", "tr")
        if name not in available_models():
            name = "en"
        bin_path, tok, EOS, do_translate = model_files(name)
        # Sadece baştaki boşlukları at: oyuncak başlığının sonundaki "\n\n" modelin beklediği biçimin parçası.
        prompt = q.get("prompt", "").lstrip() or ("Once upon a time" if name == "en" else "Bir zamanlar")
        temp = 0.0 if q.get("greedy") == "1" else float(q.get("temp", 0.8))
        topk = int(q.get("topk", 40))
        n = int(q.get("tokens", 250))
        seed = int(q["seed"]) if q.get("seed", "").strip() else random.randrange(1 << 30)
        rep = float(q.get("rep", 1.0))

        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()

        ids = tok.encode(prompt).ids
        # Figür başlığı varsa: okutulmayan figürlerin ve yabancı isimlerin token'ları yasaklanır
        # (ölçüm: yanlış/yabancı isim %47 -> %0, figür sadakati %88 -> %93).
        ban = []
        m = re.match(r"Karakter: (.+?) \|", prompt)
        if m and name == "oyuncak2":
            kim = [TUR_KIMLIK[t.strip()] for t in m.group(1).split(",") if t.strip() in TUR_KIMLIK]
            ban = ["-b", ",".join(map(str, yasak_idler(tok, kim)))] if kim else []
        p = subprocess.Popen(
            [os.path.join(HERE, "gen"), bin_path, str(n), str(temp),
             str(topk), str(seed), str(rep), *ban, *map(str, ids)],
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        out, printed, made, t0 = list(ids), "", 0, time.time()
        base = tok.decode(ids)
        buf = "" if prompt.startswith("Karakter:") else base  # figür başlığı okunmaz/gösterilmez

        def flush(sentences):
            for en in sentences:
                self.send_event({"en": en, "tr": translate(en)} if do_translate else {"en": "", "tr": en})

        try:
            self.send_event({"seed": seed, "model": name})
            for line in p.stdout:
                t = int(line)
                if t in EOS:
                    break
                out.append(t)
                made += 1
                text = tok.decode(out)
                full_new = text[len(base):]
                buf += full_new[len(printed):]
                printed = full_new
                self.send_event({"tokens": made})
                ready, buf = split_ready(buf)
                flush(ready)
            flush([buf.strip()] if buf.strip() else [])
            dt = time.time() - t0
            self.send_event({"done": True, "tokens": made, "tps": made / dt if dt else 0, "seed": seed})
        except (BrokenPipeError, ConnectionResetError):
            pass
        finally:
            p.kill()


if __name__ == "__main__":
    print(f"Arayüz: http://localhost:{PORT}")
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
