#!/bin/bash
# ============================================================
#  TEK KOMUTLUK SUNUCU KURULUMU
#  Kullanim:  sudo bash kurulum.sh
# ============================================================
set -e

KLASOR="/opt/bolbolbul-feed"
WEBROOT="/var/www/html"

echo "==> Klasorler olusturuluyor..."
mkdir -p "$KLASOR"
mkdir -p "$WEBROOT"

echo "==> Dosyalar kopyalaniyor..."
cp -f feed_duzelt.py kategori_eslesme.py feed_guncelle.sh "$KLASOR/"
chmod +x "$KLASOR/feed_guncelle.sh"

echo "==> Python kontrol ediliyor..."
python3 --version || { echo "HATA: python3 kurulu degil. 'apt install python3' calistirin."; exit 1; }

echo "==> Ilk feed uretiliyor (birkac dakika surebilir)..."
bash "$KLASOR/feed_guncelle.sh"

echo "==> Cron gorevi ekleniyor (her gun 04:00)..."
CRON_SATIR="0 4 * * * /bin/bash $KLASOR/feed_guncelle.sh"
( crontab -l 2>/dev/null | grep -v "bolbolbul-feed" ; echo "$CRON_SATIR" ) | crontab -

echo ""
echo "============================================================"
echo "  KURULUM TAMAM"
echo "============================================================"
echo "  Feed dosyasi : $WEBROOT/google-feed.xml"
echo "  Log          : $KLASOR/feed.log"
echo "  Cron         : her gun 04:00"
echo ""
echo "  Merchant Center'a verecegin URL:"
echo "    https://SENIN-DOMAININ/google-feed.xml"
echo "============================================================"
