"""Dışa aktarılmış bir modeli tarayıcı test arayüzü için paketle.

Kullanım: .venv/bin/python web/paketle.py <sürüm> <model_dizini> [--tema] [--plan] [--pencere govde] [--satir-yasak]
  model_dizini: model.bin + tokenizer.json (export.py çıktısı, ör. hf_c2ft)
  --tema: model "| Tema: <tema>" başlığıyla eğitildi (prepare_ft2 --tema); arayüz tema seçtirir
  --plan: model önce planı yazar (prepare_ft2 --plan, E3): istem prompts_bas + plan_ek ("\nSorun:") olur,
          arayüz planı nl nl'ye (nl_id) kadar ayrı üretir (gen.c -S)
  --pencere govde: başlık token'ları tekrar cezası penceresine girmez (gen.c -P)
  --satir-yasak: hikâye gövdesinde satır sonu token'ları yasak (gen.c -N)
  --eot-on: istem, eğitimdeki gibi <|endoftext|> ile başlar (prompt_idler eot=True)
  --urun: ürün modeli (c3ft_urun*): eski oyuncak kataloğu yerine data/urun_kartlari.json'daki çizgi film figürleri
          (degerlendirme/urun_uret.py ile birebir): istemler urun_uret.istem, figür başına yasaklı adlar
          urun_uret.kadro_disi ('$' = urun_uret.KELIME_BASI), plan modu, gövdede urun_uret.SATIR_YASAK, istem tekrar
          penceresi dışında (gen -P). --plan/--eot-on/--satir-yasak/--pencere govde bu modda kendiliğinden geçerli.
Çıktı: web/m/<sürüm>/model.b64.txt (gzip + base64 model.bin; yayın yeri ikili dosya sunmuyor) ve meta.json
  meta.json: token tablosu (çözmek için), her figür/yer birleşimi için başlık token'ları
  (baslangic.prompt_idler ile, eğitimdeki gibi), yasaklanacak isim token'ları, katalog.
Arayüz kendi tokenizer'ını taşımaz: kodlanması gereken her şey (başlıklar, isimler) burada hazırlanır.
"""
import argparse
import base64
import gzip
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
from tokenizers import Tokenizer  # noqa: E402
from baslangic import KAR, KATALOG, SIRA, TEMALAR, YABANCI, baslangic, prompt_idler  # noqa: E402


def isim_idleri(tok, isim):
    """Bir ismi üretmeyi engelleyen token'lar: ismin tek token hâli ya da (çok parçalıysa) büyük harfli
    ilk parçası - baslangic.yasak_idler ile aynı kural."""
    idler = set()
    for v in (" " + isim, isim):
        enc = tok.encode(v).ids
        ilk = tok.decode([enc[0]]).strip()
        if len(enc) == 1 or (ilk[:1].isupper() and len(ilk) >= 3):
            idler.add(enc[0])
    return sorted(idler)


def _urun_uret():
    sys.path.insert(0, os.path.join(ROOT, "degerlendirme"))
    import urun_uret
    return urun_uret


def urun_secici():
    """meta.urun'un seçici (atolye.html urunPuanla) ve süzgeç için gereken kısmı: figürler (kart yerleri ve yanları,
    yasaklı adlar, kadro_cezalari'nın kadro/izinli kümeleri) ve ad kümeleri. Ad mantığı urun_uret'ten gelir.
    Tokenizer istemez (tests/test_atolye_secici.py bunu doğrudan kullanır)."""
    u = _urun_uret()
    figurler, tum = [], set()
    for kimlik in u.FIGURLER:
        k = u.KARTLAR[kimlik]
        # urun_uret.kadro_cezalari: kadro = figur_adlari; izinli = kadro ∪ kartın büyük harfli rol yüzeyleri
        # ('Anne', 'Dede') ∪ bunların kelimeleri (kadro_cezalari'ndaki ifadenin aynısı)
        kadro = u.figur_adlari(kimlik)
        rol = {s for y in k["yanlar"] for s in y["yuzey_bicimleri"] if s[:1].isupper()}
        izinli = kadro | rol | {w for a in kadro | rol for w in a.split()}
        figurler.append({
            "kimlik": kimlik, "ad": k["ad"]["deger"], "tur": k.get("tur", {}).get("deger", ""),
            "yerler": [y["etiket"] for y in k["yerler"]], "yanlar": [y["kisa_ad"] for y in k["yanlar"]],
            # isim_suzgec.h biçimi: kelime başı olabilen adlar '$' ile (gen -Y dosyasının ad satırları)
            "yasak": [a + ("$" if u.kelime_basi_mi(a) else "") for a in u.kadro_disi(kimlik)],
            "kadro": sorted(kadro), "izinli": sorted(izinli),
        })
        tum |= kadro
    return {
        "figurler": figurler,
        "tum_isim": sorted(tum),     # sec.TUM_ISIM'in ürün hâli (urun_uret.puanla)
        # kadro_cezalari'nın tum_urun'u: bütün ürün adları + yabancı adlar + eski oyuncak adları ('kartta olmayan ad'
        # bunları saymaz; kadro dışı olanlar 'yanlış isim' kuralında)
        "tum_ad": sorted(tum | set(YABANCI) | {x["isim"] for x in KAR.values()}),
        "takinti_haric": sorted(u.TAKINTI_HARIC),  # takinti_cezasi
        "yer_anahtar": u.YER_ANAHTAR,
    }


def urun_bolumu(tok):
    """meta.urun: urun_secici() + her figür × yer × (yan | yansız) için istem token'ları ve üretim ayarları."""
    u = _urun_uret()
    sec = urun_secici()
    istemler = {}
    for f in sec["figurler"]:
        for yer in f["yerler"]:
            for yan in f["yanlar"] + [None]:
                ids = u.istem(tok, f["ad"], yer, yan)
                assert tok.decode(ids[1:]) == f"Karakter: {f['ad']} | Yer: {yer}" + (f" | Yan: {yan}" if yan else "") + "\nSorun:"
                istemler[f"{f['kimlik']}|{yer}|{yan or ''}"] = ids
    return {
        **sec,
        "istemler": istemler,
        "nl": u.NL,
        "govde_yasak": u.SATIR_YASAK,
        "ayar": {"sicaklik": 0.5, "top_k": 40, "tekrar": 1.1, "n": 230, "aday": 4},
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("surum")
    ap.add_argument("model_dir")
    ap.add_argument("--tema", action="store_true")
    ap.add_argument("--plan", action="store_true", help="istem '\\nSorun:' ile biter, model önce planı yazar (E3)")
    ap.add_argument("--pencere", choices=["tum", "govde"], default="tum")
    ap.add_argument("--satir-yasak", action="store_true")
    ap.add_argument("--eot-on", action="store_true", help="istem <|endoftext|> ile başlar (E0'da benimsendi)")
    ap.add_argument("--urun", action="store_true", help="ürün modeli: çizgi film figürleri (urun_uret.py)")
    arg = ap.parse_args()
    surum, model_dir = arg.surum, arg.model_dir
    tok = Tokenizer.from_file(os.path.join(model_dir, "tokenizer.json"))
    out = os.path.join(HERE, "m", surum)
    os.makedirs(out, exist_ok=True)
    ham = open(os.path.join(model_dir, "model.bin"), "rb").read()
    with open(os.path.join(out, "model.b64.txt"), "wb") as f:
        f.write(base64.b64encode(gzip.compress(ham, 9, mtime=0)))

    vocab = [None] * tok.get_vocab_size()
    for s, i in tok.get_vocab().items():
        vocab[i] = s
    if arg.urun:
        urun = urun_bolumu(tok)
        meta = {
            "surum": surum,
            "eot": tok.token_to_id("<|endoftext|>"),
            "vocab": vocab,
            "baslik_bicimi": "urun",
            "pencere": "govde",           # gen -P
            "satir_yasak": urun["govde_yasak"],
            "nl_id": urun["nl"],
            "eot_on": True,               # urun.istemler <|endoftext|> ile başlar
            "yabanci": YABANCI,
            "urun": urun,
        }
        json.dump(meta, open(os.path.join(out, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False,
                  separators=(",", ":"))
        print(f"{out}: model {len(ham) / 1e6:.1f} MB, meta.json "
              f"{os.path.getsize(os.path.join(out, 'meta.json')) / 1e6:.2f} MB, {len(urun['figurler'])} figür, "
              f"{len(urun['istemler'])} istem (ürün)")
        return
    yerler = [y["kimlik"] for y in KATALOG["yerler"]]
    prompts = {}
    for i, a in enumerate(SIRA):
        for grup in [[a]] + [[a, b] for b in SIRA[i + 1:]]:
            for y in yerler:
                prompts[",".join(grup) + "|" + y] = prompt_idler(tok, grup, y)
    tema_ek = {}
    if arg.tema or arg.plan:
        # Başlık parça parça kurulur: prompts_bas[grup|yer] + temalar[t] + (nl2 | plan_ek). Birleşimlerin
        # hepsinde (tema: 9360, plan: 468, ikisi: 9360 daha) parçaların, başlığın tek parça kodlanmasıyla
        # (prompt_idler) aynı token'ları verdiği doğrulanır.
        def kodla_on(metin):
            enc = tok.encode(metin + "Bir")
            return [i for i, (_, son) in zip(enc.ids, enc.offsets) if son <= len(metin)]
        bas, temalar = {}, []
        for anahtar in prompts:
            grup, y = anahtar.split("|")
            bas[anahtar] = kodla_on(baslangic(grup.split(","), y, ilk_cumle=False).rstrip("\n"))
        nl2 = tok.encode("\n\nBir").ids[:2]
        if arg.tema:
            for t in TEMALAR:
                temalar.append({"ad": t, "ids": tok.encode(f" | Tema: {t}").ids})
            for anahtar in prompts:
                grup, y = anahtar.split("|")
                for t, ti in zip(TEMALAR, temalar):
                    assert bas[anahtar] + ti["ids"] + nl2 == prompt_idler(tok, grup.split(","), y, tema=t), (anahtar, t)
            tema_ek = {"prompts_bas": bas, "temalar": temalar, "nl2": nl2}
        else:
            tema_ek = {"prompts_bas": bas, "nl2": nl2}
        if arg.plan:
            # plan_ek: istemin "\nSorun:" kısmı, prompt_idler(plan=True) eksi düz başlık; gövde nl nl'den sonra başlar
            anahtar0 = next(iter(prompts))
            grup, y = anahtar0.split("|")
            plan_ek = prompt_idler(tok, grup.split(","), y, plan=True)[len(bas[anahtar0]):]
            assert nl2[0] == nl2[1] and plan_ek[:1] == nl2[:1], (nl2, plan_ek)
            for anahtar in prompts:
                grup, y = anahtar.split("|")
                assert bas[anahtar] + plan_ek == prompt_idler(tok, grup.split(","), y, plan=True), anahtar
                for t, ti in zip(TEMALAR, temalar):
                    assert (bas[anahtar] + ti["ids"] + plan_ek
                            == prompt_idler(tok, grup.split(","), y, tema=t, plan=True)), (anahtar, t)
            tema_ek.update({"plan_ek": plan_ek, "nl_id": nl2[0]})
    satir = sorted(i for i in range(tok.get_vocab_size())
                   if (d := tok.decode([i])) and not d.strip() and "\n" in d) if arg.satir_yasak else []
    isimler = [k["isim"] for k in KAR.values()] + YABANCI
    meta = {
        "surum": surum,
        "eot": tok.token_to_id("<|endoftext|>"),
        "vocab": vocab,
        "prompts": prompts,
        "isim_yasak": {n: isim_idleri(tok, n) for n in isimler},
        "yabanci": YABANCI,
        "baslik_bicimi": "plan" if arg.plan else "tema" if arg.tema else "eski",
        "pencere": arg.pencere,
        "satir_yasak": satir,
        "eot_on": arg.eot_on,
        **tema_ek,
    }
    json.dump(meta, open(os.path.join(out, "meta.json"), "w", encoding="utf-8"), ensure_ascii=False,
              separators=(",", ":"))
    # Uydurma kelime kontrolü için sözlük (degerlendirme/sozluk_olustur.py çıktısı), düz metin
    pkl = os.path.join(ROOT, "degerlendirme", "sozluk.pkl")
    if os.path.exists(pkl):
        import pickle
        with open(os.path.join(HERE, "sozluk.txt"), "w", encoding="utf-8") as f:
            f.write("\n".join(sorted(pickle.load(open(pkl, "rb")))))
    else:
        print("UYARI: degerlendirme/sozluk.pkl yok; arayüz uydurma kelime cezası vermeyecek")
    print(f"{out}: model {len(ham) / 1e6:.1f} MB -> model.b64.txt "
          f"{os.path.getsize(os.path.join(out, 'model.b64.txt')) / 1e6:.1f} MB, "
          f"meta.json {os.path.getsize(os.path.join(out, 'meta.json')) / 1e6:.2f} MB, {len(prompts)} başlık")


if __name__ == "__main__":
    main()
