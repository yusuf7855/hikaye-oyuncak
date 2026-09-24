# Modeller

Büyük eğitim dosyaları (`runs/`, `hf_*/`) depoya girmez; buradakiler yeniden üretmesi pahalı olanlar.

| Dosya | Ne | Boyut |
|---|---|---|
| `c2_onegitim_fp16.pt` | C2 ön-eğitimi (V16384 d160 L10 F320 P96, 24 000 adım, Türkçe TinyStories), ağırlıklar fp16 | 48 MB |
| `c2_tokenizer.json` | Bu modelin tokenizer'ı (`prepare_tr2.py`; figür isimleri tek token) — aşağıdaki bütün C2 modelleri bunu kullanır | 1.2 MB |
| `c2_onegitim_6000/` | Ön-eğitimin 6000. adımı (v1 ve v2 ara ince ayarlarının başlangıcı) | 48 MB |
| `c2tmp/` | v0 · altyapı testi (ön-eğitimin 500. adımı, ince ayarsız) | 59 MB |
| `c2ara/` | v1 · önizleme (6000 + 1500 adım ince ayar; hakem 4.74/10) | 59 MB |
| `c2ara_tema/` | v2 · tema (E1, reddedildi; hakem 4.17/10) | 59 MB |

Her model klasöründe: `agirliklar_fp16.pt` (ince ayara devam için), `model.bin` (kartta çalışan 4-bit model),
`golden.txt` (C motoru doğrulaması: `./gen_verify model.bin golden.txt`), `bilgi.json`. Yeni bir modeli eklemek:
`PYTHONPATH=src .venv/bin/python modeller/kaydet.py <etiket>`.

fp16 kaydın fp32 ile farkı ölçülemeyecek kadar küçük (doğrulama kaybı 2.37008 → 2.37009). Ön-eğitim ~5.5 saat
(4 çekirdek CPU) sürdü; genel Türkçe doğrulamada perplexity 9.14.

Bu kayıttan ince ayara devam etmek (ön-eğitimi yeniden çalıştırmadan):

```bash
mkdir -p runs data/tr2_tinystories/vocab-16384
cp modeller/c2_onegitim_fp16.pt runs/ple-c2-s0.pt
cp modeller/c2_tokenizer.json data/tr2_tinystories/vocab-16384/tokenizer.json
# genel Türkçe token dosyaları (train.bin/val.bin) için: prepare_tr2.py (README'deki veri indirme adımı)
PAKET="--satir-yasak --eot-on" ./ince_ayar_c2.sh c2ft --bolme data/bolme.json --blok-eot
```

Bütünlük: `cd modeller && sha256sum -c SHA256SUMS`
