# -*- coding: utf-8 -*-
"""
bolbolbul.com product_type -> Google Product Taxonomy ID eslemesi

TUM ID'LER RESMI LISTEDEN DOGRULANDI:
https://www.google.com/basepages/producttype/taxonomy-with-ids.tr-TR.txt
(Google_Product_Taxonomy_Version: 2021-09-21)

Dogrulama: python3 kategori_dogrula.py
"""

KATEGORI_ESLESME = {
    # ---- Su motorlari / pompalar
    # 500102 Hirdavat > Techizat Pompalari > Laginn, Kanalizasyon ve Atik Su Pompalari
    "Elektrikli Su Motoru": 500102,
    "Su Motoru Parçaları": 500102,
    "Benzinli Su Motoru": 500102,
    "Dizel Su Motoru": 500102,
    "Su Motoru ve Pompalar": 500102,

    # ---- Zincirli testere / agac kesme
    # 3610 Ev ve Bahce > Cim ve Bahce > Elektrikli Bahce Ekipmanlari > Zincirli Testereler
    "Benzinli Ağaç Kesme Makinesi": 3610,
    "Akülü Ağaç Kesme Makinesi": 3610,
    "Elektrikli Ağaç Kesme Makinesi": 3610,
    "Ağaç Kesme Makinesi": 3610,
    "Benzinli Ağaç Budama Makinesi": 3610,
    "Akülü Ağaç Budama Makinesi": 3610,
    # 4565 ... > Elektrikli Bahce Ekipman Aksesuarlari > Zincirli Testere Aksesuarlari
    "Ağaç Kesme Makinesi Parçaları": 4565,
    "Akülü Budama Makinesi Parçaları": 4565,
    "Zincir Bileme Makinesi": 4565,

    # ---- Tirpan (yabanci ot temizleme)
    # 1223 Ev ve Bahce > Cim ve Bahce > Elektrikli Bahce Ekipmanlari > Yabanci Ot Temizleme Makineleri
    "Benzinli Tırpan": 1223,
    "Akülü Tırpan": 1223,
    "Elektrikli Tırpan": 1223,
    "Motorlu Tırpan Parçaları": 4566,   # Cim Bicme Makinesi Aksesuarlari

    # ---- Cim bicme
    # 6789 ... > Elektrikli Bahce Ekipmanlari > Vakumlu Cim Bicme Makineleri
    "Benzinli Çim Biçme Makinesi": 6789,
    "Elektrikli Çim Biçme Makinesi": 6789,
    "Akülü Çim Biçme Makinesi": 6789,
    "Çim Biçme Makinesi": 6789,
    "Benzinli Çayır Biçme Makinesi": 6789,
    "Dizel Çayır Biçme Makinesi": 6789,
    # 4566 ... > Elektrikli Bahce Ekipman Aksesuarlari > Cim Bicme Makinesi Aksesuarlari
    "Çim Biçme Makinesi Parçaları": 4566,
    "Çayır Biçme Makinesi Parçaları": 4566,

    # ---- Motorlar / elektrikli bahce ekipmani (ust kategori)
    # 3798 Ev ve Bahce > Cim ve Bahce > Elektrikli Bahce Ekipmanlari
    "4 Zamanlı Motorlar": 3798,
    "2 Zamanlı Motorlar": 3798,
    "Karıştırıcılar": 3798,
    "Elektrikli Vinç": 3798,
    "Bahçe Makineleri": 3798,

    # ---- Toprak isleme / capa
    # 2204 ... > Elektrikli Fidan Dikme ve Tohum Atma Makineleri
    "Benzinli Çapa Makinesi": 2204,
    "Dizel Çapa Makinesi": 2204,
    "Çapa Makinesi": 2204,
    "Çapa Makinesi Parçaları": 2204,
    "Benzinli Toprak Havalandırma Makinesi": 2204,
    "Elektrikli Toprak Havalandırma Makinesi": 2204,
    "Fide Dikici ve Sökücü": 2204,
    "Toprak Burgu Makinesi": 2204,
    "Toprak Burgu Parçaları": 2204,
    "Toprak Delme Aparatı": 2204,

    # ---- Ilaclama (bahce sulama/purkurtme)
    # 3568 Ev ve Bahce > Cim ve Bahce > Sulama ve Tarimsal Sulama
    "Benzinli İlaçlama Makinesi": 3568,
    "Akülü İlaçlama Makinesi": 3568,
    "Elektrikli İlaçlama Makinesi": 3568,
    "İlaçlama Makinesi Parçaları": 3568,
    "İlaçlama Pompası": 3568,
    "Sprey Besin Solüsyonu": 3568,
    "Hortum ve Toplama Ürünleri": 2313,   # Bahce Hortumlari
    "Hortum Bağlantıları": 4718,          # Bahce Hortumu Baglanti Parcalari ve Vanalari
    "Fıskiyeler": 7561,                   # Bahce Sulayicilar ve Kafalari
    "Su Zamanlayıcı": 1302,               # Sprinkler Kumandalari

    # ---- Jenerator
    # 1218 Hirdavat > Elektrik Sarf Malzemeleri > Jeneratorler
    "Benzinli Jeneratör": 1218,
    "Dizel Jeneratör": 1218,
    "İnverter": 1218,
    "Jeneratör Parçaları": 4709,          # Jenerator Aksesuarlari

    # ---- Budama makasi / bahce el aletleri
    # 3841 ... > Bahcecilik > Bahce Aletleri > Budama Makaslari
    "Budama Makası": 3841,
    "Akülü Ağaç Budama Makası": 3841,
    "Aşı Makası": 3841,
    "Çim Çit Makası": 3841,
    "Budama Testeresi": 6967,             # Budama Testereleri
    "Hasat Bıçakları": 505292,            # Bahce Oraklari ve Palalari
    "Çapa, Kazma, Kürek": 4000,           # Ekme Bicme Aletleri
    "Tırmık ve Dirgen": 3071,             # Bahce Tirmiklari
    "Bahçe Seti": 3173,                   # Bahce Aletleri
    "Çöp Toplama Aparatı": 3173,
    "Odun Taşıma Aleti": 3616,            # El Arabalari
    "Gübre": 3828,                        # Gubre Serpme Makineleri

    # ---- Cit kesme
    # 3120 ... > Elektrikli Bahce Ekipmanlari > Cit Budama Makineleri
    "Benzinli Çit Kesme Makinesi": 3120,
    "Akülü Çit Kesme Makinesi": 3120,
    "Elektrikli Çit Kesme Makinesi": 3120,
    "Çit Kesme Makinesi Parçaları": 3120,

    # ---- Yaprak ufleme
    # 3340 ... > Elektrikli Bahce Ekipmanlari > Yaprak Ufleme Makineleri
    "Benzinli Yaprak Toplama Üfleme Makinesi": 3340,
    "Akülü Yaprak Toplama Üfleme Makinesi": 3340,
    "Elektrikli Yaprak Toplama Üfleme Makinesi": 3340,
    "Yaprak Toplama Üfleme Makinesi": 3340,
    "Yaprak Toplama Üfleme Parçaları": 3340,

    # ---- Dal ogutme / kar kureme
    "Benzinli Yaprak Dal Öğütme Makinesi": 3798,
    "Elektrikli Yaprak Dal Öğütme Makinesi": 3798,
    "Yaprak Dal Öğütme Makinesi": 3798,
    "Dal Öğütme Makinesi Parçaları": 3798,
    "Kar Küreme Makinesi": 1541,          # Kar Ufleme Makineleri

    # ---- Hayvancilik
    # 6990 Is ve Endustri > Tarim > Hayvancilik > Ciftlik Hayvani Yemlikleri ve Suluklari
    "Otomatik Hayvan Sulukları": 6990,
    "Sağım Makinesi Aksesuarları": 6990,
    "Süt Sağma Makinesi": 6990,
    "Koyun Kırkma Makinesi": 6990,
    "Yem Hazırlama Makinesi": 6990,
    "Elektrikli Çit Sistemleri": 6990,

    # ---- Hasat makineleri (bahce el aletleri ust)
    "Zeytin Hasat Makinesi": 3173,
    "Hasat Makinesi Parçaları": 3173,
    "Ceviz Hasat Makinesi": 3173,
    "Çay Toplama Makinesi": 3173,
    "Hasat Makinesi": 3173,
    "Bitki Bağlama Makinesi": 3173,

    # ---- Tekne
    # 1130 Tasitlar ve Parcalar > Tasitlar > Jetski > Kisisel Jetski
    "Tekne Motoru Parçaları": 1130,
    "Tekne Motoru": 1130,
    "Tekne ve Yat Malzemeleri": 1130,

    # ---- Aku / sarj
    # 2978 Elektronik > Elektronik Alet Aksesuarlari > Guc > Yakit Pilleri
    "Akü ve Şarj Aletleri": 2978,

    # ---- Matkap / vidalama
    # 1217 Hirdavat > Aletler > Matkaplar
    "Matkaplar": 1217,
    "Akülü Vidalama": 1217,
    "Karot Makinesi": 1217,

    # ---- Testere
    # 1235 Hirdavat > Aletler > Testereler
    "Ahşap ve Metal Kesme": 1235,
    "Beton Kesme Makinesi": 1235,
    "Daire Testere": 3224,                # Dairesel El Testereleri
    "Dekupaj Testere": 3725,              # Dekupaj Testereleri
    "Tilki Kuyruğu": 3594,                # El Testereleri

    # ---- Kesici / makas
    # 1180 Hirdavat > Aletler > Kesiciler
    "Metal Kesme Makası": 1180,
    "Yan Keski": 1180,
    "Kargaburun": 1180,
    "Pense": 1180,

    # ---- Kirici / cekic
    # 1186 Hirdavat > Aletler > Cekicler
    "Kırıcı Delici ve Kırıcı": 505364,    # Elektrikli Cekicler
    "Çekiç ve Balyoz": 1186,
    "Çivi ve Zımba Çakma": 1186,
    "Balta ve Nacak": 1171,               # Baltalar

    # ---- Taslama / zimpara / polisaj
    "Taşlamalar": 1219,                   # Taslama Makineleri
    "Zımpara Makinesi": 1188,             # Zimpara Makineleri
    "El Zımparası": 4419,                 # Zimpara Bloklari
    "Polisaj Makinesi": 1188,

    # ---- Diger el aletleri
    "Tornavida": 1203,                    # Tornavidalar
    "Somun Sıkma Makineleri": 1195,       # Lokma Uclu Tornavidalar
    "Anahtar Takımı": 6965,               # El Aleti Takimlari
    "Diğer El Aletleri": 1167,            # Hirdavat > Aletler
    "Perçin": 1167,
    "Pafta Makinesi": 1167,
    "Kontrol Kalemi": 1167,
    "Planyalar": 1187,                    # El Planyalari
    "Freze": 5587,                        # Cok Islevli Elektrikli Aletler
    "Boya Tabancaları": 5587,
    "Sıcak Hava Tabancası": 5587,

    # ---- Olcum
    # 1305 Hirdavat > Aletler > Olcum Aletleri ve Sensorler
    "Lazer Ölçüm Cihazı": 1305,
    "Su Terazisi": 1305,
    "Şerit Metre": 1305,

    # ---- Diger guc aletleri
    "Hava Kompresörü": 2015,              # Kompresorler
    "Kaynak Makinesi": 1238,              # Kaynak Tabancalari ve Plazma Kesme
    "Basınçlı Yıkama Makinesi": 1226,     # Basincli Yikama Makineleri

    # ---- Gida isleme
    # 730 Ev ve Bahce > Mutfak ve Yemek > Mutfak Aletleri
    "Meyve Kurutma Makinesi": 730,
    "Meyve Pres Makinesi": 730,
    "Meyve Dilimleme Makinesi": 730,
    "Salça Makinesi": 730,
    "Hamur Karma Makinesi": 730,
    "Yayık Makinesi": 730,
    "Öğütme Makinesi": 730,
    "Airfryer &amp; Fritözler": 730,
    "Vakumlu Paketleme Makinesi": 730,

    # ---- Giyim
    "İş Ayakkabısı": 187,                 # Giyim ve Aksesuar > Ayakkabi
    "Bahçıvan Şapka &amp; Bere &amp; Eldiven": 167,  # Giyim Aksesuarlari

    # ---- Bakim / kimyasal
    "Bahçe Makine Yağları": 2820,         # Motorlu Tasit Motor Parcalari
    "Köpek Kırkma Makinesi": 2975,        # Kozmetik Aletleri
}
