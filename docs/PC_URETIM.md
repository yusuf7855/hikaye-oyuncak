# PC'de eş zamanlı hikâye üretimi

Buluttaki oturum `urun_v2` veri setini üretiyor (dal `claude/wonderful-pasteur-x7seiq`, sonra `main`).
PC'deki Claude Code **ayrı bir veri seti (`urun_v3`) ve ayrı bir dal (`pc-uretim`)** üzerinde çalışır; böylece iki
taraf aynı dosyalara yazmaz ve çakışmaz. Tohumlar farklı sayıyla (`--tohum 2028`) üretilir, hikâyeler tekrar etmez.
İki setin kabul edilen hikâyeleri eğitimden önce birleştirilir.

## 1. Kurulum (bir kez)

```bash
git clone https://github.com/yusuf7855/hikaye-oyuncak.git
cd hikaye-oyuncak
git checkout -b pc-uretim origin/main
python3 -m venv .venv
.venv/bin/pip install numpy tokenizers zemberek-python==0.2.3 "setuptools<70"
```

Denetim: `.venv/bin/python -m unittest tests.test_veri_hakem tests.test_urun_kapi` hatasız bitmeli.

## 2. Veri setini başlat (bir kez)

```bash
.venv/bin/python degerlendirme/veri_hakem.py kart-kontrol urun_v3 --kilitle
.venv/bin/python degerlendirme/veri_hakem.py tohum urun_v3 --figur hepsi --n 400 --tohum 2028
git add -A && git commit -m "urun_v3: kartlar ve tohumlar" && git push -u origin pc-uretim
```

## 3. Claude Code'a verilecek komut

Depo klasöründe `claude` açıp şunu yaz (yolu kendi klasörünle değiştir):

> scripts/uretim_akisi.js iş akışını Workflow aracıyla şu args ile çalıştır:
> {"ad": "urun_v3", "hedef": 50, "tur": 8, "dal": "pc-uretim", "repo": "/Users/<kullanıcı>/hikaye-oyuncak"}

İş akışı her turda: kod kapısı → hakem partileri (hakem başına 10 hikâye) → karar → onarım/yazım istemleri →
yazar ve düzelticiler; her turun sonunda `pc-uretim` dalına commit ve push yapar.

## Notlar

- Aynı hesabı kullanan iki oturum aynı kullanım sınırını paylaşır: iş hızlanır ama sınıra daha çabuk varılır.
- Hakem ve yazım kuralları (`degerlendirme/HAKEM_*.md`, `KILAVUZ_URUN.md`, kartlar) iki tarafta aynı olmalı;
  bunlar değişirse `git pull origin main` ile PC dalına alınır.
