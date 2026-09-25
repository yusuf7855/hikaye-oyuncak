# Eğitime kendi bilgisayarında devam etmek

Eğitim internet ve Claude gerektirmez. Kod, veri ve başlangıç modeli GitHub'da
(`yusuf7855/hikaye-oyuncak`, dal `claude/wonderful-pasteur-x7seiq`).

## Gerekenler

- **Mac** ya da **Linux**. **Windows**'ta WSL (Ubuntu) kurun: PowerShell'de `wsl --install`, sonra aşağıdakileri
  Ubuntu penceresinde yapın.
- Yaklaşık 2 GB boş disk, 8 GB RAM.
- Ekran kartı gerekmez. NVIDIA (CUDA) ya da Apple M çip (MPS) varsa eğitim kendiliğinden onu kullanır ve çok hızlanır.
  Yalnız işlemciyle bir ince ayar (3000 adım) 4 çekirdekte yaklaşık 45 dakika sürer.

## Kurulum (bir kez)

```bash
# Ubuntu/WSL: sudo apt install git xz-utils build-essential curl
curl -LsSf https://astral.sh/uv/install.sh | sh        # Python paket yöneticisi (uv)
git clone -b claude/wonderful-pasteur-x7seiq https://github.com/yusuf7855/hikaye-oyuncak.git
cd hikaye-oyuncak
uv sync                                                # .venv içine torch, tokenizers, numpy
./yerel_kurulum.sh                                     # veriyi açar, kontrol eder, C araçlarını derler
```

## Eğitimi başlatmak

Başlangıç noktası, GitHub'daki ön-eğitimli model: `modeller/c2_onegitim_fp16.pt`. Tur 1 (E4) komutu:

```bash
BAZ=modeller/c2_onegitim_fp16.pt EK_TRAIN="" PAKET='--plan --satir-yasak --eot-on' \
  ./ince_ayar_c2.sh c2ft_e4 --bolme data/bolme.json --blok-eot \
  --plan data/oyuncak_plan/plan.jsonl --plan-orani 0.7 --genel-token 4000000
```

- İlerleme ekrana ve `runs/ple-c2ft_e4-s0.progress.json` dosyasına yazılır.
- Yarıda kesilirse aynı komutu tekrar çalıştırın; son kayıttan (her 250 adımda bir) devam eder.
- Bitince `hf_c2ft_e4/model.bin` oluşur (ESP32 modeli) ve C doğrulaması otomatik yapılır.

## Sonucu geri göndermek

```bash
.venv/bin/python modeller/kaydet.py c2ft_e4             # modeller/c2ft_e4/ altına ağırlıklar + model.bin
git add modeller && git commit -m "c2ft_e4 yerelde eğitildi" && git push
```

Sonra bana "c2ft_e4'ü yerelde eğittim, GitHub'a gönderdim" deyin. Hikâyeleri üretip hakemlere ben veririm. Hakem
değerlendirmesi Claude gerektirir; eğitim gerektirmez.

## Kendi bilgisayarında hikâye üretmek

```bash
.venv/bin/python degerlendirme/uret.py hf_c2ft_e4 deneme --aday 8 --baslik plan --satir-yasak --eot-on
# -> degerlendirme/deneme/hikayeler.json (36 hikâye)
```
