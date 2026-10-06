# Windows bilgisayarda (RTX 4090) Claude Code ile çalışmak — adım adım

Amaç: Excalibur bilgisayarda Claude Code'u kurup ses modelini ekran kartıyla eğitmek; kart USB ile bağlıysa ESP32'ye
yazılımı da oradan yüklemek. Claude Code depodaki `CLAUDE.md` dosyasını kendisi okur: projeyi ve sıradaki işleri
oradan öğrenir, ayrıca anlatmanız gerekmez.

## 1. Bir kez kurulacaklar (~20 dk)

1. **NVIDIA sürücüsü** güncel olsun (GeForce Experience → Sürücüler → Güncelle).
2. **Git**: https://git-scm.com/download/win — kurulumda varsayılanlarla "Next". (Git Bash da gelir.)
3. **Python 3.11**: https://www.python.org/downloads/release/python-3119/ → "Windows installer (64-bit)".
   İlk ekranda **"Add python.exe to PATH"** kutusunu işaretleyin.
4. **Claude Code**: Başlat menüsünden **PowerShell**'i açıp:
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```
   Kurulum bitince PowerShell'i kapatıp yeniden açın.
5. **Arduino IDE 2** (kartı bu bilgisayardan yükleyecekseniz): https://www.arduino.cc/en/software

## 2. Depoyu indirin ve Claude'u başlatın

PowerShell'de:
```powershell
cd $HOME\Documents
git clone -b claude/wonderful-pasteur-x7seiq https://github.com/yusuf7855/hikaye-oyuncak.git
cd hikaye-oyuncak
claude
```
- `git clone` GitHub girişi isterse açılan tarayıcı penceresinden giriş yapın.
- `claude` ilk açılışta Claude hesabınızla giriş ister (tarayıcı açılır). Aynı hesabı kullanın.

## 3. Claude'a ne yazacaksınız

Şunu yapıştırmanız yeterli:

> CLAUDE.md'yi oku. Bu bilgisayarda RTX 4090 var. Önce ses ortamını kur (.venv, CUDA'lı PyTorch, voxcpm), sonra
> `python ses/pc_hepsi.py` ile ses eğitimini arka planda başlat. İlk 250 cümleden sonra toplam süreyi söyle ve
> birkaç örnek sesi bana dinlet.

Claude komut çalıştırmadan önce izin ister; "Yes" (ya da bu oturum için hep izin ver) deyin.

Kart USB'ye takılıysa ayrıca:

> ESP32 kartı COM portuna bağlı. firmware/hikaye_oyuncak/README.md'ye göre yazılımı derle, model.bin'i yükle, seri
> monitörden açılış çıktısını ve bir hikâyeyi bana göster.

## 4. Bilmeniz gerekenler

- Eğitim saatler–1-2 gün sürebilir; bilgisayarın **uyku modunu kapatın** (Ayarlar → Sistem → Güç → Uyku: Hiçbir zaman).
- Bilgisayar kapanırsa: PowerShell → `cd $HOME\Documents\hikaye-oyuncak` → `claude` → "ses eğitimine kaldığı yerden
  devam et". Eğitim kaldığı yerden sürer.
- Disk: ses verisi + eğitim ~10–15 GB yer ister.
- Bu bilgisayardaki Claude oturumu buluttaki oturumdan ayrıdır: buradaki konuşmayı bilmez, ama `CLAUDE.md` ve
  `docs/` içindeki notlar her şeyi anlatır. Yeni bulgular commit edilip GitHub'a gönderilirse iki taraf da görür.
