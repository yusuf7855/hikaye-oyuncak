"""İskeletli üretim: olay örgüsünün iskeletini kod kurar, model yalnız cümleleri tamamlar (uret.py'nin test setiyle).

Kullanım: python degerlendirme/iskelet.py <model_dizini> <çıktı_adı> [--aday K] [--temp 0.5] [--rep 1.1]
                                          [--satir-yasak] [--eot-on] [--dogrulama <dogrulama.json>]
Akış (her aday için; ayrıntı ve gerekçeler degerlendirme/ISKELET.md):
  1. Plan: istem uret.py --baslik plan ile aynı ("Karakter: X | Yer: Y\nSorun:"); model sorun satırını yazar (gen -e Ċ),
     "Çözüm:" kodla eklenir, model çözüm satırını yazar (gen -e Ċ), ardından Ċ Ċ. Plan tekrar penceresine girmez (gen -W).
  2. Giriş cümlesi şablondan: baslangic(ilk_cumle=True)'nun cümlesi ("<yer açılışı> Pamuk adında bembeyaz bir tavşan
     yaşardı."), katalogdaki biçimlerle; ek/ünlü uyumu uydurulmaz.
  3. Aşamalar (ASAMALAR): her aşamada kod cümlenin ilk kelimelerini ("Bir gün", "Sonunda", "O günden sonra", ...)
     metne ekler, model o cümleyi (ve aşamaya göre bir cümle daha) tamamlar; cümle sonu Python'da bulunur (cumle_sonlari:
     . ! ? ve tırnak kapanışından sonra, tırnak dışında, ardından büyük harf/tırnak/EOT gelince). Açılışlar eğitim
     hikâyelerindeki sıklıklarına göre (ağırlıklı, adayın seed'iyle) seçilir.
  4. Son aşama (kapanış) tek cümle; sonu iskelet belirler: kapanış cümlesi tamamlanınca bitti=true (bağlam dolup bir aşama
     yazılamazsa false). eot_son: modelin kapanıştan hemen sonra EOT'yi seçip seçmediği (yalnız tanı için).
  5. --aday K: vaka başına K tam iskelet hikâye (seed 1000·i+j), seçici sec.puanla (uret.py'deki gibi, plan ile).
Çıktı: degerlendirme/<çıktı_adı>/hikayeler.json  [{id, figurler, yer, baslik, metin, token, plan, plan_bozuk, iskelet}]
       <model_dizini>/adaylar_<çıktı_adı>.json    [{vaka, j, kim, yer, tema, metin, n, lp, bitti, plan, plan_bozuk,
                                                    iskelet, eot_son, n_cihaz}]
       (ayarları ayar_adaylar_<çıktı_adı>.json'da; aynı ayarla üretilmiş adaylar yeniden üretilmez)
  metin: yalnız hikâye gövdesi (başlık ve plan satırı yok). n: gövde token'ı (zorlanan + üretilen). lp: yalnız modelin
  ürettiği (tutulan) gövde token'larının ortalama log-olasılığı. n_cihaz: kartta işlenecek token (plan + gövde + her
  aşamada bir bakış token'ı); mevcut sistemle (uret.py: plan + gövde) hesap karşılaştırması için.
GEN ortam değişkeni başka bir gen derlemesini gösterebilir (varsayılan: depo kökündeki ./gen).
"""
import argparse, hashlib, json, os, random, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
from tokenizers import Tokenizer  # noqa: E402
from baslangic import KAR, baslangic, prompt_idler, yasak_idler  # noqa: E402
from uret import BOZUK_LP, GEN, _istem_ozeti, _sha, gen_kullanim, satir_idleri, satir_sonu, vakalar  # noqa: E402

BAGLAM = 256  # C2'nin seq_len'i (gen: istem en çok 255 token)

# Aşamalar: (ad, [(açılış, eğitimdeki sayı)], hedef cümle sayısı). {A}: ilk figürün adı, {B}: ikincinin (ikili vakada).
# Sayılar data/oyuncak_v2 + oyuncak_v3'ten (c2ft_plan'ın ince ayar verisi, 2364 hikâye): cümlenin hikâyedeki göreli
# yerine göre (0 = ilk, 1 = son cümle) o açılışla başlayan cümle sayısı; tablo ISKELET.md'de. Ağırlık = sayı.
ASAMALAR_TEK = [
    ("ozellik", [("{A}", 1474)], 1),                              # ≤.25: cümlelerin çoğu figürün adıyla başlar
    ("sorun", [("Bir gün", 1175), ("Bir sabah", 176)], 2),        # ≤.25
    ("deneme", [("{A} önce", 224), ("{A} hemen", 206)], 1),       # ≤.5
    ("donum", [("Sonra", 147)], 2),                               # ≤.5
    ("cozum", [("Sonunda", 61), ("Kısa sürede", 40)], 1),         # ≤.75
    ("kapanis", [("O günden sonra", 230), ("Akşam olunca", 95)], 1),  # son cümle
]
ASAMALAR_IKILI = [
    ("ozellik", [("{A}", 1474)], 1),
    ("sorun", [("Bir gün", 1175), ("Bir sabah", 176)], 2),
    ("deneme", [("{A} önce", 224), ("{A} hemen", 206)], 1),
    ("donum", [("{B}", 147), ("Sonra", 147)], 2),                 # ikilide yardım çoğu kez öbür figürden gelir
    ("cozum", [("İkisi birlikte", 68), ("Sonunda", 61)], 1),      # ≤.75
    ("kapanis", [("O günden sonra", 230), ("Akşam olunca", 95)], 1),
]
SON_ASAMA = "kapanis"
N_CUMLE = {1: 48, 2: 80}  # aşama başına üretilecek en çok token (cümle sonu + bir bakış token'ı için pay)
N_PLAN_SATIR = 40         # plan satırı başına en çok token (gen -S'nin ORNEKLE_PLAN_SINIR'ı iki satır için 48)
TIRNAK = '"“”'
CUMLE_SONU = re.compile(r'[.!?]["”]?$')
SONRAKI = re.compile(r'\s+["“A-ZÇĞİÖŞÜ]')


def gen_cagir(model_dir, ids, n, seed, temp, rep, ban, satir=None, dur=None, pencere_k=None):
    """gen'i bir kez çağırır ([(token, logp)]). dur: gen -e; satir: gen -N; pencere_k: gen -W."""
    ek = (["-N", ",".join(map(str, satir))] if satir else []) + (["-e", str(dur)] if dur is not None else [])
    ek += ["-W", str(pencere_k)] if pencere_k is not None else []
    r = subprocess.run([GEN, os.path.join(model_dir, "model.bin"), str(n), str(temp), "40", str(seed), str(rep),
                        "-b", ",".join(map(str, ban)), *ek, "-l", *map(str, ids)], capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit(f"gen hata verdi: {r.stderr.strip()}")
    return [(int(a), float(b)) for a, b in (l.split() for l in r.stdout.split("\n") if l.strip())]


def cumle_sonlari(tok, toks, son):
    """Üretilen token'larda cümle sonları: k listesi, toks[:k] tam cümle(ler) biter. Cümle sonu: metin . ! ? (ve
    kapanan tırnak) ile biter, tırnaklar dengeli (tırnak içindeki "Gel. Arayalım," bölünmez) ve ardından boşluk + büyük
    harf ya da açılan tırnak gelir ('"Merhaba." dedi' bölünmez), ya da sonraki token EOT'dir. Aşama cümle başında
    başladığından tırnak sayımı aşamanın başından yapılır."""
    sonlar = []
    for k, t in enumerate(toks):
        if t == son:
            break
        metin = tok.decode(toks[:k + 1])
        if not CUMLE_SONU.search(metin) or sum(metin.count(c) for c in TIRNAK) % 2:
            continue
        if k + 1 < len(toks) and (toks[k + 1] == son or SONRAKI.match(tok.decode(toks[k + 1:k + 3]))):
            sonlar.append(k + 1)
    return sonlar


def asamalar(kim):
    return ASAMALAR_IKILI if len(kim) > 1 else ASAMALAR_TEK


def acilis_sec(rng, bank, kim):
    """Bankadan eğitimdeki sıklığa göre ağırlıklı açılış; {A}/{B} figür adlarıyla (yalın hâl, ek yok)."""
    a = rng.choices([b for b, _ in bank], weights=[s for _, s in bank])[0]
    adlar = [KAR[k]["isim"] for k in kim]
    return a.format(A=adlar[0], B=adlar[-1])


def giris_cumlesi(kim, yer):
    """baslangic'in şablon ilk cümlesi (katalogdaki açılış/isim/sıfat, eğitimdeki tanıtım kalıbı)."""
    return baslangic(kim, yer, ilk_cumle=True).split("\n\n", 1)[1].strip()


def iskelet_uret(model_dir, kim, yer, seed, temp, rep, tok, eot=False, satir=None):
    """Tek aday. Döner: {metin, n, lp, bitti, plan, plan_bozuk, iskelet, eot_son, n_cihaz}."""
    son = tok.token_to_id("<|endoftext|>")
    nl = satir_sonu(tok)
    ban = yasak_idler(tok, kim)
    rng = random.Random(seed)
    # 1. plan: model yazar (uret.py plan modu gibi), satır satır; "Çözüm:" kodla eklenir, plan hep iki satır biçiminde
    bas = prompt_idler(tok, kim, yer, eot=eot, plan=True)
    cozum_ids = tok.encode("Çözüm:").ids
    sorun = gen_cagir(model_dir, bas, N_PLAN_SATIR, seed * 16, temp, rep, ban, dur=nl, pencere_k=len(bas))
    ctx = bas + [t for t, _ in sorun]
    bozuk = not sorun or sorun[-1][0] != nl or len(sorun) < 2
    cozum = [] if bozuk else gen_cagir(model_dir, ctx + cozum_ids, N_PLAN_SATIR, seed * 16 + 1, temp, rep, ban,
                                        dur=nl, pencere_k=len(bas))
    bozuk = bozuk or not cozum or cozum[-1][0] != nl or len(cozum) < 2
    plan = ("Sorun:" + tok.decode([t for t, _ in sorun if t != nl]) + "\nÇözüm:"
            + tok.decode([t for t, _ in cozum if t != nl])).rstrip()
    if bozuk:
        return {"metin": "", "n": 0, "lp": BOZUK_LP, "bitti": False, "plan": plan, "plan_bozuk": True,
                "iskelet": [], "eot_son": False, "n_cihaz": len(sorun) + len(cozum)}
    ctx = ctx + cozum_ids + [t for t, _ in cozum] + [nl]  # plan "…\nÇözüm: Ç\n" + ikinci Ċ: gövde başlar
    n_plan = len(sorun) + len(cozum_ids) + len(cozum) + 1
    # 2. giriş cümlesi (şablon); gövde başı eğitimdeki gibi boşluksuz ("Ormanın", "\n\n"den sonra)
    govde = tok.encode(giris_cumlesi(kim, yer)).ids
    ctx += govde
    uretilen, iskelet, bitti, kesik, bakis, eot_son = [], [], False, False, 0, False
    # 3. aşamalar
    for s, (ad, bank, m) in enumerate(asamalar(kim)):
        acilis = acilis_sec(rng, bank, kim)
        a_ids = tok.encode(" " + acilis).ids
        n = min(N_CUMLE[m], BAGLAM - 1 - len(ctx) - len(a_ids))
        if n < 8:
            kesik = True  # bağlam doldu: kalan aşamalar yazılamaz
            break
        ciftler = gen_cagir(model_dir, ctx + a_ids, n, seed * 16 + 2 + s, temp, rep, ban, satir=satir, dur=son)
        toks = [t for t, _ in ciftler]
        sonlar = cumle_sonlari(tok, toks, son)
        if not sonlar:
            kesik = True  # cümle bitmedi (çok uzun ya da bağlam sonu): bu aşama atılır, hikâye burada biter
            break
        k = sonlar[min(m, len(sonlar)) - 1]
        eot_geldi = k < len(toks) and toks[k] == son
        bakis += 1
        ctx += a_ids + toks[:k]
        govde += a_ids + toks[:k]
        uretilen += ciftler[:k]
        iskelet.append({"asama": ad, "acilis": acilis, "cumle": min(m, len(sonlar))})
        # ara aşamada EOT: model erken bitirmek istedi; cümle tamam, sonraki aşamalar yine zorlanır (EOT metne girmez)
        if ad == SON_ASAMA:
            bitti, eot_son = True, eot_geldi  # sonu iskelet belirler: kapanış cümlesi tamamsa hikâye bitti
    metin = tok.decode(govde).strip()
    lp = sum(l for _, l in uretilen) / max(1, len(uretilen))
    return {"metin": metin, "n": len(govde), "lp": lp, "bitti": bitti and not kesik, "plan": plan,
            "plan_bozuk": False, "iskelet": iskelet, "eot_son": eot_son, "n_cihaz": n_plan + len(govde) + bakis}


def _iskelet_ozeti():
    """Aşama tanımı ve bu dosya: değişirse havuz eskir."""
    return hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()[:16]


def aday_havuzu(model_dir, ad, K, temp, rep, tok, satir_yasak=False, eot_on=False, dogrulama=None, vaka_sinir=None):
    """Vaka başına K iskelet aday (seed 1000·i+j), <model_dir>/adaylar_<ad>.json. vaka_sinir: yalnız ilk N vaka
    (küçük deneme). Aynı ayarlı havuzdaki adaylar yeniden üretilmez."""
    vk = vakalar(dogrulama)[:vaka_sinir]
    yol = os.path.join(model_dir, f"adaylar_{ad}.json")
    ayar_yol = os.path.join(model_dir, f"ayar_adaylar_{ad}.json")
    satir = satir_idleri(tok) if satir_yasak else None
    ayar = {"model": _sha(os.path.join(model_dir, "model.bin")), "gen": _sha(GEN),
            "istem": _istem_ozeti(tok, "plan", eot_on, satir, "model", dogrulama), "temp": temp, "rep": rep,
            "top_k": 40, "baslik": "plan", "satir_yasak": satir_yasak, "eot_on": eot_on, "iskelet": _iskelet_ozeti()}
    if dogrulama:
        ayar["dogrulama"] = _sha(dogrulama)
    if "[-e " not in gen_kullanim() or "[-W " not in gen_kullanim():
        raise SystemExit(f"{GEN} -e/-W bilmiyor (eski derleme); GEN=<yeni derleme> ile çalıştırın")
    eski = {}
    if os.path.exists(yol) and os.path.exists(ayar_yol):
        onceki = json.load(open(ayar_yol, encoding="utf-8"))
        if onceki == ayar:
            eski = {(h["vaka"], h["j"]): h for h in json.load(open(yol, encoding="utf-8"))}
        else:
            fark = sorted(k for k in ayar if onceki.get(k) != ayar[k])
            print(f"{yol}: ayarlar farklı ({', '.join(fark)}), adaylar yeniden üretiliyor", file=sys.stderr)
    havuz, yeni = [], 0
    for i, (kim, yer, bilgi) in enumerate(vk):
        adaylar = []
        for j in range(K):
            h = eski.get((i, j))
            if h is None or h["kim"] != kim or h["yer"] != yer:
                h = {"vaka": i, "j": j, "kim": kim, "yer": yer, "tema": None,
                     **iskelet_uret(model_dir, kim, yer, 1000 * i + j, temp, rep, tok, eot=eot_on, satir=satir)}
                if bilgi is not None:
                    h["hikaye_id"] = bilgi["hikaye_id"]
                eski[(i, j)] = h
                yeni += 1
            adaylar.append(h)
        havuz.append(adaylar)
    if yeni:
        json.dump([eski[k] for k in sorted(eski)], open(yol, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
        json.dump(ayar, open(ayar_yol, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{yol}: {sum(map(len, havuz))} aday, {yeni} yeni üretildi", file=sys.stderr)
    return havuz


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("model_dir")
    ap.add_argument("ad")
    ap.add_argument("--aday", type=int, default=1)
    ap.add_argument("--temp", type=float, default=0.5)
    ap.add_argument("--rep", type=float, default=1.1)
    ap.add_argument("--satir-yasak", action="store_true", help="gövdede satır sonu token'ları yasak (gen -N)")
    ap.add_argument("--eot-on", action="store_true", help="istemin başına <|endoftext|>")
    ap.add_argument("--dogrulama", default=None,
                    help="test seti yerine bu dogrulama.json'un planlı hikâyelerinin (turler, yer) ikilileri")
    ap.add_argument("--vaka-sinir", type=int, default=None, help="yalnız ilk N vaka (küçük deneme)")
    a = ap.parse_args()
    tok = Tokenizer.from_file(os.path.join(a.model_dir, "tokenizer.json"))
    from sec import puanla  # noqa: E402
    havuz = aday_havuzu(a.model_dir, a.ad, a.aday, a.temp, a.rep, tok, a.satir_yasak, a.eot_on, a.dogrulama,
                        a.vaka_sinir)
    sonuc = []
    for i, (kim, yer, _) in enumerate(vakalar(a.dogrulama)[:a.vaka_sinir]):
        adaylar = havuz[i]
        h = (max(adaylar, key=lambda x: puanla(x["metin"], kim, x["lp"], x["n"], yer, x["bitti"], plan=x["plan"]))
             if a.aday > 1 else adaylar[0])
        sonuc.append({"id": i, "figurler": [KAR[k]["isim"] + " (" + KAR[k]["tur"] + ")" for k in kim], "yer": yer,
                      "baslik": baslangic(kim, yer, ilk_cumle=False).strip(), "metin": h["metin"], "token": h["n"],
                      **{k: h[k] for k in ("plan", "plan_bozuk", "hikaye_id", "iskelet") if k in h}})
    os.makedirs(os.path.join(HERE, a.ad), exist_ok=True)
    json.dump(sonuc, open(os.path.join(HERE, a.ad, "hikayeler.json"), "w", encoding="utf-8"), ensure_ascii=False,
              indent=1)
    print(f"{len(sonuc)} hikâye -> degerlendirme/{a.ad}/hikayeler.json")


if __name__ == "__main__":
    main()
