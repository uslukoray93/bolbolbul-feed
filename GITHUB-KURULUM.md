# GitHub Actions ile Kurulum (Ücretsiz, Sunucusuz)

Sunucu kiralamana gerek yok. GitHub her gün feed'i üretip yayınlar.
**Toplam süre: ~15 dakika. Aylık maliyet: 0 TL.**

---

## Adım 1 — GitHub hesabı

Hesabın yoksa: https://github.com/signup (ücretsiz)

---

## Adım 2 — Depo (repository) oluştur

1. https://github.com/new adresine git
2. Bilgileri doldur:

   | Alan | Değer |
   |---|---|
   | Repository name | `bolbolbul-feed` |
   | Görünürlük | **Public** ⚠️ (Private'ta ücretsiz Pages çalışmaz) |
   | Add a README | ❌ işaretleme |

3. **Create repository**

> **Public olması sorun mu?** Hayır. İçinde sadece dönüştürücü kod var.
> Feed'in zaten herkese açık bir URL'de — Google'ın erişebilmesi için
> açık olmak zorunda. Şifre/müşteri verisi yok.

---

## Adım 3 — Dosyaları yükle

**Kolay yol (tarayıcıdan):**

1. Yeni depoda **"uploading an existing file"** bağlantısına tıkla
2. Bu 4 dosyayı sürükle:
   - `feed_duzelt.py`
   - `kategori_eslesme.py`
   - `OKUBENI.md`
   - `.gitignore`
3. **Commit changes**

4. Şimdi workflow dosyası — bunu ayrı yapmak gerekiyor (klasör içinde):
   - **Add file → Create new file**
   - Dosya adı kutusuna tam olarak şunu yaz:
     ```
     .github/workflows/feed.yml
     ```
     (eğik çizgileri yazdıkça klasörler otomatik oluşur)
   - `feed.yml` dosyasının içeriğini kopyala-yapıştır
   - **Commit changes**

**Terminal bilenler için:**
```bash
cd bolbolbul-feed
git init && git add -A && git commit -m "feed donusturucu"
git branch -M main
git remote add origin https://github.com/KULLANICI-ADIN/bolbolbul-feed.git
git push -u origin main
```

---

## Adım 4 — GitHub Pages'i aç

1. Depoda **Settings** sekmesi
2. Sol menüden **Pages**
3. **Source** → **GitHub Actions** seç
4. Kaydet

---

## Adım 5 — İlk çalıştırma

1. Depoda **Actions** sekmesi
2. Sol menüden **"Feed Guncelle"**
3. Sağdaki **"Run workflow"** → **Run workflow**
4. 1-2 dakika bekle, yeşil ✅ görene kadar

Bittiğinde çalışmaya tıklayınca özet görünür:
```
### Feed guncellendi
- Urun: 5755
- Boyut: 12M
- URL: https://kullaniciadin.github.io/bolbolbul-feed/google-feed.xml
```

**Bu URL'yi not al** — Merchant Center'a bunu vereceksin.

---

## Adım 6 — Merchant Center'a ekle

**Veri kaynakları → Ürün kaynağı ekle → "Dosyadan" / "Zamanlanmış getirme"**

| Alan | Değer |
|---|---|
| Kaynak adı | `Bolbolbul Ana Feed` |
| Dosya URL'si | `https://kullaniciadin.github.io/bolbolbul-feed/google-feed.xml` |
| Getirme sıklığı | **Günlük** |
| Getirme saati | **06:00** |
| Saat dilimi | İstanbul |
| Ülke / Dil | Türkiye / Türkçe |

**Kaydet ve şimdi getir**

🔴 Eski feed kaynağını Merchant Center'dan **sil** — yoksa "yinelenen ürün" hatası alırsın.

---

## Çalışma düzeni

```
Her gece 04:00 (TR)  →  GitHub feed'i bolbolbul.com'dan çeker
                     →  temizler, doğrular
                     →  yayınlar
Her sabah 06:00      →  Google feed'i alır
```

Doğrulama başarısız olursa (site çökmüş, 4000'den az ürün, bozuk XML)
**yayınlamaz, eski feed yerinde kalır.** Merchant Center hesabın korunur.

---

## Kontrol

- **Actions** sekmesi → son çalışmalar (yeşil ✅ / kırmızı ❌)
- Hata olursa GitHub kayıtlı e-postana otomatik uyarı yollar
- Elle çalıştırmak: Actions → Feed Guncelle → Run workflow

---

## Saat değiştirmek

`.github/workflows/feed.yml` içinde:
```yaml
- cron: '0 1 * * *'    # 01:00 UTC = 04:00 Türkiye
```
UTC yazılır, Türkiye saati **UTC+3**. Örnek: 02:00 TR istiyorsan `'0 23 * * *'`.

---

## Sınırlar

| | GitHub ücretsiz | Senin kullanımın |
|---|---|---|
| Actions dakikası | Public depoda **sınırsız** | ~2 dk/gün |
| Pages boyutu | 1 GB | 12 MB |
| Pages trafiği | 100 GB/ay | ~400 MB/ay |

Rahatça sığıyor.
