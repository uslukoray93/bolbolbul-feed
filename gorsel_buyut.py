# -*- coding: utf-8 -*-
"""
500x500 altindaki urun gorsellerini 800x800'e buyutup yayin klasorune koyar.
Feed donusturucu bu gorseller icin Ticimax yerine GitHub Pages adresini kullanir.

NEDEN: Ticimax CDN'inde 'buyuk' klasoru zaten en buyuk surum; /orjinal/ yok,
?width= parametresi calismiyor. Yani kaynakta 400x400 olan dosya 400x400.
Google 31 Ocak 2027'den sonra 500x500 altini gostermeyecek.

BU GECICI BIR KOPRU COZUMDUR. Kalici cozum: Ticimax'a yuksek cozunurluklu
gorselleri yeniden yuklemek.

Kullanim:
  python3 gorsel_buyut.py --feed yayin/google-feed.xml --klasor yayin/img \
      --taban https://uslukoray93.github.io/bolbolbul-feed/img --limit 50
"""
import re, os, sys, json, argparse, struct, subprocess, urllib.request, hashlib
from concurrent.futures import ThreadPoolExecutor

HEDEF = 800          # cikti boyutu (kare)
ESIK  = 500          # bu boyutun altindakiler islenir
UA    = {'User-Agent': 'Mozilla/5.0'}


def olc(url):
    """Gorselin (genislik, yukseklik) degerini indirmeden okur."""
    try:
        r = urllib.request.Request(url, headers={**UA, 'Range': 'bytes=0-6000'})
        b = urllib.request.urlopen(r, timeout=20).read()
    except Exception:
        return None
    if b[:8] == b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II', b[16:24])
    if b[:2] == b'\xff\xd8':
        i = 2
        while i < len(b) - 9:
            if b[i] != 0xFF:
                i += 1; continue
            m = b[i + 1]
            if m in (0xC0,0xC1,0xC2,0xC3,0xC5,0xC6,0xC7,0xC9,0xCA,0xCB,0xCD,0xCE,0xCF):
                h, w = struct.unpack('>HH', b[i+5:i+9]); return (w, h)
            if m in (0xD8, 0xD9) or 0xD0 <= m <= 0xD7:
                i += 2; continue
            i += 2 + struct.unpack('>H', b[i+2:i+4])[0]
    return None


def dosya_adi(url):
    """URL'den benzersiz, sabit dosya adi uretir."""
    ad = url.rsplit('/', 1)[-1]
    kok, uzanti = os.path.splitext(ad)
    if uzanti.lower() not in ('.png', '.jpg', '.jpeg'):
        uzanti = '.png'
    ozet = hashlib.md5(url.encode()).hexdigest()[:8]
    kok = re.sub(r'[^A-Za-z0-9._-]', '-', kok)[:60]
    return f"{kok}-{ozet}{uzanti}"


def buyut(url, hedef_yol):
    """Gorseli indirip HEDEF x HEDEF olcusune buyutur. Basarili ise True."""
    try:
        r = urllib.request.Request(url, headers=UA)
        veri = urllib.request.urlopen(r, timeout=60).read()
        if len(veri) < 500:
            return False
        with open(hedef_yol, 'wb') as f:
            f.write(veri)
        # sips: macOS yerlesik. Linux'ta (GitHub Actions) ImageMagick kullanilir.
        if sys.platform == 'darwin':
            k = subprocess.run(['sips', '-z', str(HEDEF), str(HEDEF), hedef_yol,
                                '-o', hedef_yol],
                               capture_output=True, timeout=60)
        else:
            k = subprocess.run(['convert', hedef_yol, '-resize',
                                f'{HEDEF}x{HEDEF}!', hedef_yol],
                               capture_output=True, timeout=60)
        if k.returncode != 0:
            os.path.exists(hedef_yol) and os.remove(hedef_yol)
            return False
        return os.path.getsize(hedef_yol) > 500
    except Exception:
        os.path.exists(hedef_yol) and os.remove(hedef_yol)
        return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--feed',   required=True, help='islenecek google-feed.xml')
    ap.add_argument('--klasor', required=True, help='buyutulmus gorsellerin klasoru')
    ap.add_argument('--taban',  required=True, help='gorsellerin yayin URL tabani')
    ap.add_argument('--limit',  type=int, default=0, help='0=sinirsiz (test icin 50)')
    ap.add_argument('--filtre', default=None,
                    help='sadece basliginda bu metin gecen urunleri isle (ornek: zeytin)')
    args = ap.parse_args()

    os.makedirs(args.klasor, exist_ok=True)
    kayit_yolu = os.path.join(args.klasor, '_kayit.json')
    kayit = {}
    if os.path.exists(kayit_yolu):
        try:
            kayit = json.load(open(kayit_yolu, encoding='utf-8'))
        except Exception:
            kayit = {}

    d = open(args.feed, encoding='utf-8').read()
    urunler = []
    for it in re.findall(r'<item>.*?</item>', d, re.S):
        u = re.search(r'<g:image_link>(.*?)</g:image_link>', it, re.S)
        i = re.search(r'<g:id>(\d+)</g:id>', it)
        if not (u and i):
            continue
        if args.filtre:
            t = re.search(r'<g:title>(.*?)</g:title>', it, re.S)
            if not t or args.filtre.lower() not in t.group(1).lower():
                continue
        urunler.append((i.group(1), u.group(1).strip()))

    print(f"Feed: {len(urunler)} urun")

    # Kayittakileri atla, kalanlari olc
    olculecek = [(p, u) for p, u in urunler if u not in kayit]
    print(f"  kayitta: {len(kayit)} | olculecek: {len(olculecek)}")

    with ThreadPoolExecutor(max_workers=25) as ex:
        boyutlar = list(ex.map(lambda x: olc(x[1]), olculecek))

    kucukler = [(p, u) for (p, u), b in zip(olculecek, boyutlar)
                if b and (b[0] < ESIK or b[1] < ESIK)]
    # olculemeyenleri ve buyukleri kayda gec (bir daha olcme)
    for (p, u), b in zip(olculecek, boyutlar):
        if b and b[0] >= ESIK and b[1] >= ESIK:
            kayit[u] = None       # yeterince buyuk -> dokunma

    print(f"  {ESIK}x{ESIK} alti: {len(kucukler)}")
    if args.limit:
        kucukler = kucukler[:args.limit]
        print(f"  TEST MODU -> ilk {len(kucukler)} tanesi islenecek")

    basarili = hatali = 0
    for n, (pid, url) in enumerate(kucukler, 1):
        ad = dosya_adi(url)
        yol = os.path.join(args.klasor, ad)
        if buyut(url, yol):
            kayit[url] = f"{args.taban.rstrip('/')}/{ad}"
            basarili += 1
        else:
            hatali += 1
        if n % 10 == 0 or n == len(kucukler):
            print(f"    {n}/{len(kucukler)}  basarili:{basarili} hatali:{hatali}")

    with open(kayit_yolu, 'w', encoding='utf-8') as f:
        json.dump(kayit, f, ensure_ascii=False, indent=1)

    degistirilen = sum(1 for v in kayit.values() if v)
    print("=" * 58)
    print(f"  Buyutulen (bu calisma): {basarili}")
    print(f"  Hatali                : {hatali}")
    print(f"  Toplam yayindaki      : {degistirilen}")
    print(f"  Kayit dosyasi         : {kayit_yolu}")
    print("=" * 58)


if __name__ == '__main__':
    main()
