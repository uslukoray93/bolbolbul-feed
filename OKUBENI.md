# Bolbolbul → Google Merchant Center Feed Dönüştürücü

Ticimax'ın ürettiği XML'i Google Merchant Center'ın kabul ettiği temiz feed'e çevirir.
Her gün otomatik çalışır, güncel feed'i yayınlar.

---

## Düzeltilen 8 sorun

| # | Sorun | Çözüm |
|---|---|---|
| 1 | `[installment] desteklenmiyor` (kırmızı) | Blok tamamen kaldırılır |
| 2 | `Geçersiz para birimi [price]` | `2.904,69` → `2904.69`, kargoya `TRY` eklenir |
| 3 | `Geçersiz google_product_category` | 147 kategori → Google taksonomi ID'leri |
| 4 | Kargo ülkesi yok | `<g:country>TR</g:country>` eklenir |
| 5 | Açıklamalar ham HTML | Düz metne çevrilir, 5000 kr'a kırpılır |
| 6 | `identifier_exists` yanlış | Marka+MPN kontrolüyle `yes`/`no` |
| 7 | Bozuk/eksik ürünler | Atlanır, log'a yazılır |
| 8 | Kaynak feed çökerse | Eski feed korunur (güvenlik kontrolü) |
| 9 | Stokta olmayan ürünler | Feed dışı bırakılır (varsayılan **açık**) |

**Not:** "Yerel envanter verileri eksik" hatası feed'le ilgili DEĞİL —
Merchant Center → Eklentiler'den "Ücretsiz yerel listelemeler"i kaldırman gerekiyor.

---

## Kurulum (Linux sunucu)

```bash
# 1) Dosyaları sunucuya at
scp feed_duzelt.py kategori_eslesme.py feed_guncelle.sh kurulum.sh kullanici@sunucu:/tmp/

# 2) Sunucuda çalıştır
ssh kullanici@sunucu
cd /tmp && sudo bash kurulum.sh
```

Kurulum: klasörleri açar, ilk feed'i üretir, cron'u kurar (her gün 04:00).

### Ayarları değiştirmek
`feed_guncelle.sh` içindeki üst kısım:
```bash
KLASOR="/opt/bolbolbul-feed"            # script konumu
YAYIN="/var/www/html/google-feed.xml"   # web'den erişilecek yol
MIN_URUN=4000                           # bu sayının altında yayınlama
```
Nginx/Apache web kökün farklıysa `YAYIN` satırını düzelt.

### Stoksuz ürünler
Varsayılan olarak **stokta olmayanlar feed'e girmiyor** (`--stoksuz-cikar` açık).
Hepsini feed'de istersen `feed_guncelle.sh` satır 26'dan `--stoksuz-cikar` ifadesini
sil ve `MIN_URUN=8000` yap.

---

## Merchant Center'a yükleme

1. **Merchant Center → Veri kaynakları → Ürün kaynağı ekle**
2. **"Dosyadan"** / **"Zamanlanmış getirme"** seç
3. Bilgileri gir:

   | Alan | Değer |
   |---|---|
   | Kaynak adı | `Bolbolbul Ana Feed` |
   | Dosya URL'si | `https://SENIN-DOMAININ/google-feed.xml` |
   | Getirme sıklığı | **Günlük** |
   | Getirme saati | **06:00** (cron 04:00'te bitiyor) |
   | Saat dilimi | İstanbul |
   | Ülke | Türkiye |
   | Dil | Türkçe |

4. **Kaydet ve şimdi getir**

> Eski/bozuk feed kaynağını Merchant Center'dan **sil**, yoksa aynı ürünler
> iki kaynaktan gelir ve çakışma hatası alırsın.

---

## Kontrol komutları

```bash
tail -50 /opt/bolbolbul-feed/feed.log          # log oku
grep -c "<item>" /var/www/html/google-feed.xml # ürün say
bash /opt/bolbolbul-feed/feed_guncelle.sh      # elle çalıştır
crontab -l                                      # cron kontrol
```

---

## Elle kullanım (test için)

```bash
python3 feed_duzelt.py                    # indir + dönüştür
python3 feed_duzelt.py --stoksuz-cikar    # stokta olmayanları çıkar
python3 feed_duzelt.py --girdi eski.xml   # yerel dosyadan
```

---

## Kalan tek iş: görseller

~950 ürünün görseli 500x500 altında (çoğu 400x400 yedek parça).
Google'ın son tarihi: **31 Ocak 2027**. Feed'le çözülemez,
Ticimax'ta görselleri yeniden yüklemen gerekiyor. Acil değil.
