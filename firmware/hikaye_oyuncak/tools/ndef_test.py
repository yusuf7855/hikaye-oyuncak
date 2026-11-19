"""Ayar kartının NDEF kaydını (ayar_karti.h) C'den bağımsız bir çözücüyle denetler.

C tarafı (ayar_karti_tlv) küçük bir programla derlenip birkaç ağ adı / şifre / MAC için TLV alanını onaltılık yazar. Bu
betik baytları NFC Forum Type 2 TLV kurallarına, NDEF kayıt başlığına ve Wi-Fi Simple Configuration (WSC 2.0,
"Configuration Token") öznitelik yapısına göre baştan çözer ve beklenen değerlerle karşılaştırır:
  - TLV: 03 L <mesaj> FE, sonu 00; toplam 4'ün katı ve sayfa 36'dan önce biter (oyuncağın kaydı orada)
  - NDEF: tek kayıt, MB=ME=1, SR=1, IL=0, TNF=2 (MIME), tür "application/vnd.wfa.wsc"
  - WSC: Version 0x10, Credential {Network Index 1, SSID, Authentication Type 0x0020 (WPA2-Personal),
    Encryption Type 0x0008 (AES), Network Key, MAC Address}, Vendor Extension (WFA 00 37 2A, Version2 0x20)
  - Android'in ayrıştırıcısı (NfcWifiProtectedSetup) Credential'ı en üst düzeyde arar; SSID ve Network Key zorunlu.

Kullanım: python firmware/hikaye_oyuncak/tools/ndef_test.py   (çıkış kodu 0: geçti)
"""
import os
import subprocess
import sys
import tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
SKETCH = os.path.dirname(TOOLS)

C = r'''
#include <stdio.h>
#include <stdlib.h>
#include "ayar_karti.h"
int main(int argc, char **argv) {
  uint8_t mac[6], out[256];
  for (int i = 0; i < 6; i++) { char h[3] = {argv[3][2 * i], argv[3][2 * i + 1], 0}; mac[i] = (uint8_t)strtol(h, NULL, 16); }
  int n = ayar_karti_tlv(argv[1], argv[2], mac, out, sizeof out);
  if (n < 0) { printf("YOK\n"); return 0; }
  for (int i = 0; i < n; i++) printf("%02x", out[i]);
  printf("\n");
  return 0;
}
'''

hatalar = []


def dene(kosul, mesaj):
    if not kosul:
        hatalar.append(mesaj)
        print("  HATA:", mesaj)
    return kosul


def wsc_coz(b):
    """WSC öznitelikleri: [(tür, değer)] (tür ve uzunluk 2'şer bayt, büyük uçlu)."""
    i, r = 0, []
    while i < len(b):
        if i + 4 > len(b):
            raise ValueError("yarım öznitelik başlığı")
        t, n = int.from_bytes(b[i:i + 2], "big"), int.from_bytes(b[i + 2:i + 4], "big")
        if i + 4 + n > len(b):
            raise ValueError(f"öznitelik 0x{t:04x} taşıyor")
        r.append((t, b[i + 4:i + 4 + n]))
        i += 4 + n
    return r


def tlv_coz(b):
    """Type 2 TLV alanı -> NDEF mesajı (NULL TLV'leri atlar, FE'de durur)."""
    i, mesaj, son = 0, None, False
    while i < len(b):
        t = b[i]
        if t == 0x00:
            i += 1
            continue
        if t == 0xFE:
            son = True
            break
        n = b[i + 1]
        if n == 0xFF:
            raise ValueError("3 baytlık uzunluk beklenmiyordu")
        if t == 0x03:
            mesaj = b[i + 2:i + 2 + n]
        i += 2 + n
    return mesaj, son, i


def ndef_coz(m):
    """Tek kayıtlı NDEF mesajı -> (başlık bayrakları, tür, yük)."""
    h = m[0]
    mb, me, cf, sr, il, tnf = h >> 7 & 1, h >> 6 & 1, h >> 5 & 1, h >> 4 & 1, h >> 3 & 1, h & 7
    nt = m[1]
    if sr:
        ny, i = m[2], 3
    else:
        ny, i = int.from_bytes(m[2:6], "big"), 6
    if il:
        i += 1
    tur = m[i:i + nt]
    yuk = m[i + nt:i + nt + ny]
    if i + nt + ny != len(m):
        raise ValueError("mesajda artık bayt (tek kayıt beklenir)")
    return dict(mb=mb, me=me, cf=cf, sr=sr, il=il, tnf=tnf), tur, yuk


def main():
    d = tempfile.mkdtemp(prefix="ndef_")
    src, exe = os.path.join(d, "n.c"), os.path.join(d, "n")
    with open(src, "w") as f:
        f.write(C)
    subprocess.run(["cc", "-O2", "-Wall", "-I" + SKETCH, "-o", exe, src], check=True)
    vakalar = [("Masalci-Ayar-3F7A", "48201937", "24a160123f7a"),
               ("Masalci-Ayar-0000", "00000000", "000000000000"),
               ("A" * 32, "x" * 63, "ffffffffffff")]
    for ssid, sifre, mac in vakalar:
        out = subprocess.run([exe, ssid, sifre, mac], capture_output=True, text=True, check=True).stdout.strip()
        if ssid == "A" * 32:  # en uzun ad + şifre 128 bayta sığmaz: C reddetmeli
            dene(out == "YOK", f"sığmayan kayıt reddedilmedi: {len(out) // 2} B")
            continue
        b = bytes.fromhex(out)
        dene(len(b) % 4 == 0 and len(b) <= (36 - 4) * 4, f"TLV boyu {len(b)} (4'ün katı ve <= 128 olmalı)")
        mesaj, son, sonda = tlv_coz(b)
        dene(mesaj is not None and son, "NDEF TLV ya da sonlandırıcı yok")
        dene(all(x == 0 for x in b[sonda + 1:]), "sonlandırıcıdan sonra dolgu 00 değil")
        bay, tur, yuk = ndef_coz(mesaj)
        dene(bay == dict(mb=1, me=1, cf=0, sr=1, il=0, tnf=2), f"kayıt başlığı {bay}")
        dene(tur == b"application/vnd.wfa.wsc", f"tür {tur}")
        ust = wsc_coz(yuk)
        dene([t for t, _ in ust] == [0x104A, 0x100E, 0x1049], f"üst öznitelikler {[hex(t) for t, _ in ust]}")
        dene(dict(ust).get(0x104A) == b"\x10", "Version 1.0 değil")
        dene(dict(ust).get(0x1049) == bytes.fromhex("00372a000120"), "Vendor Extension (WFA, Version2 2.0) yanlış")
        kim = dict(wsc_coz(dict(ust)[0x100E]))
        dene(kim.get(0x1026) == b"\x01", "Network Index 1 değil")
        dene(kim.get(0x1045) == ssid.encode(), f"SSID {kim.get(0x1045)}")
        dene(kim.get(0x1003) == b"\x00\x20", "Authentication Type WPA2-Personal değil")
        dene(kim.get(0x100F) == b"\x00\x08", "Encryption Type AES değil")
        dene(kim.get(0x1027) == sifre.encode(), f"Network Key {kim.get(0x1027)}")
        dene(kim.get(0x1020) == bytes.fromhex(mac), f"MAC {kim.get(0x1020)}")
        print(f"  {ssid}: {len(b)} B TLV, NDEF {len(mesaj)} B, WSC {len(yuk)} B tamam")
    print(f"ndef_test.py: {'HATA ' + str(len(hatalar)) if hatalar else 'hepsi geçti'}")
    sys.exit(1 if hatalar else 0)


if __name__ == "__main__":
    main()
