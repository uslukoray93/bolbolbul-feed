# -*- coding: utf-8 -*-
"""
bolbolbul.com Ticimax XML -> Google Merchant Center uyumlu temiz feed

Duzeltilen sorunlar:
  1. <g:installment>       -> kaldirilir (TR formatli amount + desteklenmeyen hedef)
  2. <g:shipping>          -> country=TR eklenir, price para birimli (0.00 TRY)
  3. google_product_category -> Google taksonomi ID'si ile degistirilir
  4. <g:description>       -> HTML temizlenir, duz metne cevrilir (5000 kr limiti)
  5. identifier_exists     -> markali urun mantigina gore duzeltilir
  6. Stokta olmayanlar     -> istege bagli haric tutulur (--stoksuz-cikar)
  7. <g:product_type>      -> korunur (raporlama icin degerli)
  8. Gecersiz/eksik alanli -> item atlanir, rapor edilir

Kullanim:
  python3 feed_duzelt.py                      # indir + duzelt
  python3 feed_duzelt.py --stoksuz-cikar      # stokta olmayanlari da cikar
  python3 feed_duzelt.py --girdi feed.xml     # yerel dosyadan
"""
import re, sys, html, argparse, urllib.request
from datetime import datetime, timezone
from xml.sax.saxutils import escape

import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kategori_eslesme import KATEGORI_ESLESME

FEED_URL = "https://www.bolbolbul.com/XMLExport/7A041F8F4AEC48D8A7E878A0FCC7CD1D"

# ---- Kargo kurali ----
# Bu tutar ve uzerindeki urunlerde kargo bedava (0 TL) olarak isaretlenir.
UCRETSIZ_KARGO_ESIGI = 1000.0

# Test/deneme urunleri: basligi bu kaliplardan birine uyanlar feed disi.
# (Ticimax panelinde acik kalan deneme kayitlari Google'a gitmesin)
TEST_URUN_KALIPLARI = re.compile(
    r'\b(deneme|test [uü]r[uü]n|[oö]rnek [uü]r[uü]n|dummy|xxx|sil(inecek)?)\b',
    re.IGNORECASE)

# Gercek marka olmayan, jenerik/yedek parca markalari:
# bunlarda GTIN/MPN guvenilir degil -> identifier_exists=no
JENERIK_MARKALAR = {
    "DİĞER", "DIGER", "GENEL", "MUADİL", "MUADIL", "İTHAL", "ITHAL",
    "GENERIC", "OEM", "YERLİ", "YERLI",
}


def metni_temizle(ham: str, limit: int = 5000) -> str:
    """HTML etiketli aciklamayi Google'in kabul ettigi duz metne cevirir."""
    s = html.unescape(html.unescape(ham))          # feed'de cift-escape var
    s = re.sub(r'(?is)<(script|style).*?</\1>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>', '\n', s)
    s = re.sub(r'(?i)</(p|div|li|tr|h[1-6])\s*>', '\n', s)
    s = re.sub(r'(?i)</(small|span|td)\s*>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)                  # kalan tum etiketler
    s = html.unescape(s)
    s = s.replace(' ', ' ').replace('\r', '')
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    s = '\n'.join(ln.strip() for ln in s.split('\n'))
    s = s.strip()
    if len(s) > limit:
        kes = s[:limit]
        nokta = kes.rfind('. ')
        s = (kes[:nokta + 1] if nokta > limit * 0.6 else kes).strip()
    return s


def fiyat_normalize(ham: str) -> str | None:
    """'26142.20 TRY' / '2.904,69 TRY' -> '26142.20 TRY' (nokta ondalik)."""
    if not ham:
        return None
    s = html.unescape(ham).strip()
    m = re.match(r'^([\d.,\s]+)\s*([A-Za-z]{3})?$', s)
    if not m:
        return None
    sayi, birim = m.group(1).strip(), (m.group(2) or 'TRY').upper()
    sayi = sayi.replace(' ', '')
    if ',' in sayi and '.' in sayi:                  # 2.904,69 -> TR formati
        sayi = sayi.replace('.', '').replace(',', '.')
    elif ',' in sayi:                                # 904,69
        sayi = sayi.replace(',', '.')
    try:
        deger = float(sayi)
    except ValueError:
        return None
    if deger <= 0:
        return None
    return f"{deger:.2f} {birim}"


def alan(item: str, etiket: str) -> str | None:
    m = re.search(r'<g:%s>(.*?)</g:%s>' % (etiket, etiket), item, re.S)
    return m.group(1).strip() if m else None


def tum_alanlar(item: str, etiket: str) -> list[str]:
    return [x.strip() for x in
            re.findall(r'<g:%s>(.*?)</g:%s>' % (etiket, etiket), item, re.S)]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--girdi', default=None, help='Yerel XML dosyasi (yoksa indirilir)')
    ap.add_argument('--cikti', default='google-feed.xml')
    ap.add_argument('--stoksuz-cikar', action='store_true',
                    help='out of stock urunleri feed disi birak')
    args = ap.parse_args()

    if args.girdi:
        print(f"Okunuyor: {args.girdi}")
        ham = open(args.girdi, encoding='utf-8-sig').read()
    else:
        print(f"Indiriliyor: {FEED_URL}")
        req = urllib.request.Request(FEED_URL, headers={'User-Agent': 'Mozilla/5.0'})
        ham = urllib.request.urlopen(req, timeout=300).read().decode('utf-8-sig')
    print(f"  {len(ham)/1024/1024:.1f} MB okundu")

    items = re.findall(r'<item>.*?</item>', ham, re.S)
    print(f"  {len(items)} urun bulundu\n")

    cikti, atlanan, sayac = [], [], {
        'kategori_eslesti': 0, 'kategori_bos': 0, 'installment_silindi': 0,
        'kargo_bedava': 0, 'kargo_ucretli': 0, 'aciklama_temizlendi': 0,
        'stoksuz_atlandi': 0, 'ident_no': 0, 'test_atlandi': 0,
    }

    for it in items:
        pid   = alan(it, 'id')
        baslik = html.unescape(alan(it, 'title') or '').strip()
        link  = alan(it, 'link')
        resim = alan(it, 'image_link')
        stok  = (alan(it, 'availability') or '').lower().strip()
        fiyat = fiyat_normalize(alan(it, 'price'))
        marka = html.unescape(alan(it, 'brand') or '').strip()
        mpn   = html.unescape(alan(it, 'mpn') or '').strip()
        ptype = html.unescape(alan(it, 'product_type') or '').strip()

        # --- zorunlu alan kontrolu ---
        if not (pid and baslik and link and resim and fiyat):
            eksik = [a for a, v in (('id', pid), ('title', baslik), ('link', link),
                                    ('image_link', resim), ('price', fiyat)) if not v]
            atlanan.append((pid or '?', baslik[:40], 'eksik: ' + ','.join(eksik)))
            continue

        # --- test/deneme urunu mu ---
        if TEST_URUN_KALIPLARI.search(baslik):
            atlanan.append((pid, baslik[:40], 'test/deneme urunu'))
            sayac['test_atlandi'] += 1
            continue

        if stok not in ('in stock', 'out of stock', 'preorder', 'backorder'):
            stok = 'in stock'
        if args.stoksuz_cikar and stok == 'out of stock':
            sayac['stoksuz_atlandi'] += 1
            continue

        # --- aciklama ---
        acik = metni_temizle(alan(it, 'description') or '')
        if not acik:
            acik = baslik
        else:
            sayac['aciklama_temizlendi'] += 1

        # --- kategori eslemesi ---
        kat_id = KATEGORI_ESLESME.get(ptype)
        if kat_id:
            sayac['kategori_eslesti'] += 1
        else:
            sayac['kategori_bos'] += 1   # bos birak -> Google otomatik siniflandirir

        # --- tanimlayici mantigi ---
        gercek_marka = marka and marka.upper() not in JENERIK_MARKALAR
        ident = 'yes' if (gercek_marka and mpn) else 'no'
        if ident == 'no':
            sayac['ident_no'] += 1

        # --- kargo ---
        # Esik ve uzeri -> bedava (0.00 TRY). Altinda -> kaynaktaki tutar.
        fiyat_sayi = float(fiyat.split()[0])
        if fiyat_sayi >= UCRETSIZ_KARGO_ESIGI:
            kargo_ham = '0.00 TRY'
            sayac['kargo_bedava'] += 1
        else:
            kargo_ham = None
            ksec = re.search(r'<g:shipping>(.*?)</g:shipping>', it, re.S)
            if ksec:
                kf = re.search(r'<g:price>(.*?)</g:price>', ksec.group(1), re.S)
                if kf:
                    kargo_ham = fiyat_normalize(kf.group(1))
            if kargo_ham:
                sayac['kargo_ucretli'] += 1
        if '<g:installment>' in it:
            sayac['installment_silindi'] += 1

        # --- ek gorseller (max 10, ana gorselle ayni olanlar haric) ---
        ekler, gorulen = [], {resim}
        for u in tum_alanlar(it, 'additional_image_link'):
            u = html.unescape(u).strip()
            if u and u not in gorulen:
                gorulen.add(u); ekler.append(u)
            if len(ekler) >= 10:
                break

        # --- XML uret ---
        p = ['    <item>']
        p.append(f'      <g:id>{escape(pid)}</g:id>')
        p.append(f'      <g:title>{escape(baslik[:150])}</g:title>')
        p.append(f'      <g:description>{escape(acik)}</g:description>')
        p.append(f'      <g:link>{escape(html.unescape(link))}</g:link>')
        p.append(f'      <g:image_link>{escape(html.unescape(resim))}</g:image_link>')
        for u in ekler:
            p.append(f'      <g:additional_image_link>{escape(u)}</g:additional_image_link>')
        p.append(f'      <g:availability>{stok}</g:availability>')
        p.append(f'      <g:price>{fiyat}</g:price>')
        p.append('      <g:condition>new</g:condition>')
        if marka:
            p.append(f'      <g:brand>{escape(marka[:70])}</g:brand>')
        if mpn:
            p.append(f'      <g:mpn>{escape(mpn[:70])}</g:mpn>')
        p.append(f'      <g:identifier_exists>{ident}</g:identifier_exists>')
        if kat_id:
            p.append(f'      <g:google_product_category>{kat_id}</g:google_product_category>')
        if ptype:
            p.append(f'      <g:product_type>{escape(ptype)}</g:product_type>')
        if kargo_ham:
            p.append('      <g:shipping>')
            p.append('        <g:country>TR</g:country>')
            p.append(f'        <g:price>{kargo_ham}</g:price>')
            p.append('      </g:shipping>')
        p.append('    </item>')
        cikti.append('\n'.join(p))

    simdi = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')
    import os
    hedef_klasor = os.path.dirname(os.path.abspath(args.cikti))
    os.makedirs(hedef_klasor, exist_ok=True)
    with open(args.cikti, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">\n')
        f.write('  <channel>\n')
        f.write('    <title>Bolbolbul - Bahce ve Tarim Makineleri</title>\n')
        f.write('    <link>https://www.bolbolbul.com</link>\n')
        f.write('    <description>Bolbolbul.com Google Merchant Center urun feed</description>\n')
        f.write(f'    <lastBuildDate>{simdi}</lastBuildDate>\n')
        f.write('\n'.join(cikti))
        f.write('\n  </channel>\n</rss>\n')

    boyut = os.path.getsize(args.cikti) / 1024 / 1024

    print("=" * 62)
    print(f"  TEMIZ FEED HAZIR: {args.cikti}")
    print("=" * 62)
    print(f"  Yazilan urun            : {len(cikti)}")
    print(f"  Atlanan (eksik alan)    : {len(atlanan)}")
    if args.stoksuz_cikar:
        print(f"  Atlanan (stokta yok)    : {sayac['stoksuz_atlandi']}")
    print(f"  Dosya boyutu            : {boyut:.1f} MB")
    print("-" * 62)
    print(f"  Kategori eslesti        : {sayac['kategori_eslesti']}")
    print(f"  Kategori bos (oto)      : {sayac['kategori_bos']}")
    print(f"  installment silindi     : {sayac['installment_silindi']}")
    print(f"  Test/deneme atlandi     : {sayac['test_atlandi']}")
    print(f"  Kargo BEDAVA (>={UCRETSIZ_KARGO_ESIGI:.0f} TL): {sayac['kargo_bedava']}")
    print(f"  Kargo ucretli           : {sayac['kargo_ucretli']}")
    print(f"  Aciklama HTML temizlendi: {sayac['aciklama_temizlendi']}")
    print(f"  identifier_exists=no    : {sayac['ident_no']}")
    print("=" * 62)
    if atlanan:
        print("\n  Atlanan urunler (ilk 10):")
        for a in atlanan[:10]:
            print(f"    #{a[0]:8s} {a[1]:42s} {a[2]}")
        if len(atlanan) > 10:
            print(f"    ... +{len(atlanan)-10} adet daha")


if __name__ == '__main__':
    main()
