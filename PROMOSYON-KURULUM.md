# Promosyon Feed'i Kurulumu — "Vade farksız 6 taksit"

Google'ın `installment` alanı Türkiye'de **desteklenmiyor** (feed'e koyunca
"bu ürün için desteklenmiyor" hatası veriyordu, o yüzden kaldırdık).

Taksit bilgisini göstermenin Türkiye'de **desteklenen** yolu:
**Merchant Promotions (Promosyonlar)**. Ürün kartının altında
"Özel teklif" bağlantısı çıkar, tıklayınca promosyon metni görünür.

---

## Adım 1 — Promosyonlar özelliğini aç

Bu özellik **başvuru gerektirir**, otomatik açık değil.

1. Merchant Center → sol menüden **Büyüme** (veya **Pazarlama**)
2. **Promosyonlar**'a tıkla
3. **Başlayın** / **Promosyonları etkinleştir** butonuna bas
4. Formu doldur:
   - Ülke: **Türkiye**
   - Web sitesi: `https://www.bolbolbul.com`
5. Gönder

**Onay süresi: 1-3 iş günü.** Google e-posta ile haber verir.

> Menüde "Promosyonlar" göremiyorsan: Merchant Center'ın yeni
> sürümünde **Kampanyalar → Promosyonlar** altında olabilir.
> Bulamazsan hesabın henüz uygun değildir, Google destekle iletişime geç.

---

## Adım 2 — Promosyon feed'ini ekle (onay geldikten SONRA)

**Veri kaynakları → Ürün kaynağı ekle → "Dosyadan" / "Zamanlanmış getirme"**

| Alan | Değer |
|---|---|
| Kaynak türü | **Promosyonlar** ⚠️ (ürün değil!) |
| Kaynak adı | `Bolbolbul Promosyonlar` |
| Dosya URL'si | `https://uslukoray93.github.io/bolbolbul-feed/promosyonlar.xml` |
| Getirme sıklığı | Günlük |
| Getirme saati | 06:00 / İstanbul |
| Ülke | Türkiye |

⚠️ Kaynak türünü **Promosyonlar** seçmeyi unutma. Ürün kaynağı olarak
eklersen çalışmaz.

---

## Adım 3 — Bekle

Promosyon onayı **1-3 gün** sürer. Onaylanınca ürün kartlarında
"Özel teklif" bağlantısı görünmeye başlar.

---

## Promosyon metnini değiştirmek

`promosyon_uret.py` dosyasının üst kısmı:

```python
PROMO_ID      = "TAKSIT6"
BASLIK        = "Vade farksız 6 taksit"
GUN_SAYISI    = 365
```

`BASLIK`'ı değiştir, commit et — ertesi gün otomatik yayınlanır.

**Google'ın başlık kuralları:**
- En fazla 60 karakter
- Ünlem, TAMAMI BÜYÜK HARF, "tıkla", "hemen al" gibi ifadeler yasak
- Net ve doğru olmalı — gerçekten 6 taksit yapmıyorsan reddedilir

---

## Birden fazla promosyon eklemek

Şu an tek promosyon var. İkinci bir tane (örn. "1000 TL üzeri kargo bedava")
eklemek istersen söyle, `promosyon_uret.py`'yi çoklu promosyona çeviririm.

> Not: Kargo bedava zaten **ürün feed'inde** `<g:shipping>` ile
> tanımlı — Google ürün kartında otomatik "Ücretsiz kargo" yazar.
> Ayrıca promosyon eklemeye gerek yok.
