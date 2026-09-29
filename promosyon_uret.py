# -*- coding: utf-8 -*-
"""
Google Merchant Center PROMOSYON feed'i uretir.

Urun feed'inden ayri, kendi basina bir XML. Icinde tek bir promosyon var:
"Vade farksiz 6 taksit" - tum urunlere uygulanir.

Google Promotions ozelligi Turkiye'de DESTEKLENIR (installment alaninin
aksine). Urun kartinin altinda "Ozel teklif" baglantisi olarak gorunur.

Kullanim: python3 promosyon_uret.py --cikti yayin/promosyonlar.xml
"""
import argparse, os
from datetime import datetime, timedelta, timezone

# ---- PROMOSYON AYARLARI ----
PROMO_ID      = "TAKSIT6"
BASLIK        = "Vade farksız 6 taksit"
# Google'in kabul ettigi sabit kodlar:
#   GENERIC_OFFER = genel teklif (taksit/kampanya icin uygun)
PROMO_TIPI    = "GENERIC_OFFER"
URUN_KAPSAMI  = "ALL_PRODUCTS"        # tum urunler
KANALLAR      = "ONLINE"
ULKE          = "TR"
GUN_SAYISI    = 365                    # kac gun gecerli
# -----------------------------


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cikti', default='promosyonlar.xml')
    ap.add_argument('--gun', type=int, default=GUN_SAYISI)
    args = ap.parse_args()

    bas = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    bit = bas + timedelta(days=args.gun)
    # Google ISO 8601 formati ister: 2026-09-29T00:00:00+03:00
    def iso(d):
        return d.astimezone(timezone(timedelta(hours=3))).strftime('%Y-%m-%dT%H:%M:%S%z')[:-2] + ':00'

    hedef = os.path.dirname(os.path.abspath(args.cikti))
    os.makedirs(hedef, exist_ok=True)

    with open(args.cikti, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<rss version="2.0" xmlns:g="http://base.google.com/ns/1.0">\n')
        f.write('  <channel>\n')
        f.write('    <title>Bolbolbul Promosyonlar</title>\n')
        f.write('    <link>https://www.bolbolbul.com</link>\n')
        f.write('    <description>Google Merchant Center promosyon feed</description>\n')
        f.write('    <item>\n')
        f.write(f'      <g:promotion_id>{PROMO_ID}</g:promotion_id>\n')
        f.write(f'      <g:product_applicability>{URUN_KAPSAMI}</g:product_applicability>\n')
        f.write(f'      <g:offer_type>{PROMO_TIPI}</g:offer_type>\n')
        f.write(f'      <g:long_title>{BASLIK}</g:long_title>\n')
        f.write(f'      <g:promotion_effective_dates>{iso(bas)}/{iso(bit)}</g:promotion_effective_dates>\n')
        f.write(f'      <g:redemption_channel>{KANALLAR}</g:redemption_channel>\n')
        f.write('    </item>\n')
        f.write('  </channel>\n</rss>\n')

    print("=" * 58)
    print(f"  PROMOSYON FEED HAZIR: {args.cikti}")
    print("=" * 58)
    print(f"  Promosyon ID : {PROMO_ID}")
    print(f"  Baslik       : {BASLIK}")
    print(f"  Kapsam       : tum urunler")
    print(f"  Gecerlilik   : {iso(bas)}")
    print(f"                 {iso(bit)}")
    print("=" * 58)


if __name__ == '__main__':
    main()
