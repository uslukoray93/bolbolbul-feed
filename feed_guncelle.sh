#!/bin/bash
# ============================================================
#  bolbolbul.com -> Google Merchant Center feed guncelleyici
#  Her gun cron ile calisir, temiz feed uretir.
# ============================================================
set -uo pipefail

# ---- AYARLAR (sunucuya gore degistir) ----
KLASOR="/opt/bolbolbul-feed"                    # scriptlerin oldugu yer
YAYIN="/var/www/html/google-feed.xml"           # web'den erisilecek dosya
LOG="$KLASOR/feed.log"
MIN_URUN=4000                                   # bu sayinin altinda yayinlama (guvenlik)
# ------------------------------------------

mkdir -p "$KLASOR"
cd "$KLASOR" || exit 1

zaman() { date '+%Y-%m-%d %H:%M:%S'; }
log()   { echo "[$(zaman)] $*" >> "$LOG"; }

log "=== Feed guncelleme basladi ==="

GECICI="$KLASOR/google-feed.yeni.xml"

# 1) Feed'i indir ve donustur
if ! python3 "$KLASOR/feed_duzelt.py" --cikti "$GECICI" --stoksuz-cikar >> "$LOG" 2>&1; then
    log "HATA: Donusturucu basarisiz. Eski feed korunuyor."
    exit 1
fi

# 2) XML gecerli mi?
if ! python3 -c "import xml.etree.ElementTree as ET; ET.parse('$GECICI')" 2>>"$LOG"; then
    log "HATA: Uretilen XML bozuk. Eski feed korunuyor."
    rm -f "$GECICI"
    exit 1
fi

# 3) Urun sayisi makul mu? (kaynak feed cokerse yarim dosya yayinlamayalim)
ADET=$(grep -c "<item>" "$GECICI" || echo 0)
if [ "$ADET" -lt "$MIN_URUN" ]; then
    log "HATA: Sadece $ADET urun var (min $MIN_URUN). Eski feed korunuyor."
    rm -f "$GECICI"
    exit 1
fi

# 4) Yedekle + atomik yayinla
[ -f "$YAYIN" ] && cp -f "$YAYIN" "$KLASOR/google-feed.yedek.xml"
mv -f "$GECICI" "$YAYIN"
chmod 644 "$YAYIN"

BOYUT=$(du -h "$YAYIN" | cut -f1)
log "BASARILI: $ADET urun yayinlandi ($BOYUT)"
log "=== Bitti ==="

# 5) Log dosyasini sinirla (son 2000 satir)
tail -n 2000 "$LOG" > "$LOG.tmp" && mv -f "$LOG.tmp" "$LOG"
