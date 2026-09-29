# -*- coding: utf-8 -*-
"""
kategori_eslesme.py icindeki TUM Google kategori ID'lerini
Google'in resmi taksonomi listesine karsi dogrular.

Kullanim: python3 kategori_dogrula.py
Cikis kodu 0 = hepsi gecerli, 1 = gecersiz ID var.
"""
import re, sys, os, urllib.request

TAXO_URL = "https://www.google.com/basepages/producttype/taxonomy-with-ids.tr-TR.txt"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kategori_eslesme import KATEGORI_ESLESME

print("Resmi taksonomi indiriliyor...")
req = urllib.request.Request(TAXO_URL, headers={'User-Agent': 'Mozilla/5.0'})
ham = urllib.request.urlopen(req, timeout=60).read().decode('utf-8')

gecerli = {}
for ln in ham.split('\n'):
    m = re.match(r'^(\d+)\s*-\s*(.+)$', ln.strip())
    if m:
        gecerli[int(m.group(1))] = m.group(2)
print(f"  {len(gecerli)} gecerli kategori yuklendi\n")

hatali = []
for ad, kid in sorted(KATEGORI_ESLESME.items()):
    if kid not in gecerli:
        hatali.append((ad, kid))

print(f"Toplam eslesme : {len(KATEGORI_ESLESME)}")
print(f"Gecerli        : {len(KATEGORI_ESLESME) - len(hatali)}")
print(f"GECERSIZ       : {len(hatali)}")

if hatali:
    print("\nGECERSIZ ID'LER:")
    for ad, kid in hatali:
        print(f"  {kid:>7}  <-  {ad}")
    sys.exit(1)

# Kullanilan ID'leri ve yollarini goster
print("\nKULLANILAN KATEGORILER:")
ters = {}
for ad, kid in KATEGORI_ESLESME.items():
    ters.setdefault(kid, []).append(ad)
for kid in sorted(ters, key=lambda k: -len(ters[k])):
    print(f"  {kid:>7}  ({len(ters[kid]):2d} tip)  {gecerli[kid]}")

print("\nTUM ID'LER GECERLI")
