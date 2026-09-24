"""v2 yazım kuyruğu. `python birim.py al N` -> sıradaki N birimi 'calisiyor' yapar ve ajan talimatlarını yazar.
`python birim.py bitti <id>` / `python birim.py durum`."""
import fcntl, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
KUYRUK = os.path.join(HERE, "KUYRUK.json")
KAT = {c["kimlik"]: c for c in json.load(open(os.path.join(HERE, "..", "karakterler.json"), encoding="utf-8"))["karakterler"]}
ASCII = {"şato": "sato", "dağ": "dag"}
YOL = HERE
ORTAK = f"""Sen çocuk hikâyesi yazarısın. Başka ajan başlatma; işi kendin yap.
1. Kılavuzu oku ve HARFİYEN uygula: {YOL}/KILAVUZ.md  (özellikle: 90–140 kelime, ilk cümlede isim+tür+yer,
   sadece figürlerin ismi olur, başka isim yok, tek zaman -dı'lı geçmiş) VE 12–19 numaralı v3 ek kurallarının HEPSİ."""


def talimat(u):
    if u["tip"] == "tek":
        c = KAT[u["kar"]]
        y1, y2 = u["yerler"]
        f1, f2 = (f"{YOL}/{c['kimlik']}_{ASCII.get(y, y)}.txt" for y in (y1, y2))
        return f"""{ORTAK}
2. Figür: **{c['isim']}** ({c['tur']}; {c['ozellik']}). Tek figürlü hikâyeler.
3. {y1} için 10 hikâye → {f1}
   {y2} için 10 hikâye → {f2}
   Her dosyayı tek Write ile yaz. 20 hikâyede 20 farklı tema kullan (kılavuzdaki listeden).
   Başlık biçimi: ### {c['tur']} | <yer> | <tema>
4. Bitince: cd {YOL} && ../../.venv/bin/python kontrol.py {c['kimlik']}_ — SADECE KENDİ iki dosyandaki SORUN satırlarını düzelt (başka dosyaya dokunma), tekrar çalıştır.
Rapor: sadece dosya adları, hikâye sayıları ve son kontrol.py özeti."""
    ikililer = []
    for a, b in u["ikililer"]:
        A, B = KAT[a], KAT[b]
        ikililer.append(f"   - **{A['isim']}** ({A['tur']}; {A['ozellik']}) + **{B['isim']}** ({B['tur']}; {B['ozellik']})\n"
                        f"     başlık: ### {A['tur']}, {B['tur']} | <yer> | <tema>  → {YOL}/cift_{a}_{b}.txt")
    return f"""{ORTAK}
2. İki figürlü hikâyeler. Her ikili için 6 hikâye, ikili başına bir dosya (tek Write ile):
{chr(10).join(ikililer)}
3. Her ikilinin 6 hikâyesi 6 farklı yerde geçsin (orman, deniz, ev, park, şato, dağ — her biri bir kez); temalar farklı olsun.
   İki karakter de ilk iki cümlede isim+türle tanıtılır, ikisi de sonuna kadar aktif olur ve birlikte hareket eder.
4. Bitince: cd {YOL} && ../../.venv/bin/python kontrol.py cift_ — SADECE KENDİ dosyalarındaki SORUN satırlarını düzelt (başka dosyaya dokunma), tekrar çalıştır.
Rapor: sadece dosya adları, hikâye sayıları ve son kontrol.py özeti."""


def main():
    kilit = open(KUYRUK + ".lock", "w")
    fcntl.flock(kilit, fcntl.LOCK_EX)  # birden çok işçi ajan aynı anda kuyruk alabilir
    q = json.load(open(KUYRUK, encoding="utf-8"))
    kom = sys.argv[1] if len(sys.argv) > 1 else "durum"
    if kom == "al":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        for u in [u for u in q if u["durum"] == "bekliyor"][:n]:
            u["durum"] = "calisiyor"
            print(f"===== {u['id']}\n{talimat(u)}\n")
    elif kom == "bitti":
        for u in q:
            if u["id"] == sys.argv[2]:
                u["durum"] = "bitti"
    say = {d: sum(u["durum"] == d for u in q) for d in ("bekliyor", "calisiyor", "bitti")}
    json.dump(q, open(KUYRUK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"[kuyruk] {say}", file=sys.stderr)


if __name__ == "__main__":
    main()
