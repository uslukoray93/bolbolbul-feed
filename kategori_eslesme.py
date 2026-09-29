# -*- coding: utf-8 -*-
"""
bolbolbul.com product_type -> Google Product Taxonomy ID eslemesi
147 kategorinin tamami elle eslendi.
Kaynak: Google product taxonomy (TR), https://support.google.com/merchants/answer/6324436
"""

KATEGORI_ESLESME = {
    # ---- Su motorlari / pompalar -> 1837 Hardware > Plumbing > Water Pumps
    "Elektrikli Su Motoru": 1837,
    "Su Motoru Parçaları": 1837,
    "Benzinli Su Motoru": 1837,
    "Dizel Su Motoru": 1837,
    "Su Motoru ve Pompalar": 1837,
    "İlaçlama Pompası": 1837,

    # ---- Zincirli testere / agac kesme -> 3103 Hardware > Tools > Chainsaws
    "Ağaç Kesme Makinesi Parçaları": 3103,
    "Benzinli Ağaç Kesme Makinesi": 3103,
    "Akülü Ağaç Kesme Makinesi": 3103,
    "Elektrikli Ağaç Kesme Makinesi": 3103,
    "Ağaç Kesme Makinesi": 3103,
    "Benzinli Ağaç Budama Makinesi": 3103,
    "Akülü Ağaç Budama Makinesi": 3103,
    "Akülü Budama Makinesi Parçaları": 3103,
    "Budama Testeresi": 3103,
    "Zincir Bileme Makinesi": 3103,

    # ---- Tirpan / cim kenari -> 6318 Home&Garden > Lawn&Garden > Outdoor Power Equipment > String Trimmers
    "Motorlu Tırpan Parçaları": 6318,
    "Benzinli Tırpan": 6318,
    "Akülü Tırpan": 6318,
    "Elektrikli Tırpan": 6318,

    # ---- Cim bicme -> 6317 Lawn Mowers
    "Çim Biçme Makinesi Parçaları": 6317,
    "Benzinli Çim Biçme Makinesi": 6317,
    "Elektrikli Çim Biçme Makinesi": 6317,
    "Akülü Çim Biçme Makinesi": 6317,
    "Çim Biçme Makinesi": 6317,
    "Benzinli Çayır Biçme Makinesi": 6317,
    "Dizel Çayır Biçme Makinesi": 6317,
    "Çayır Biçme Makinesi Parçaları": 6317,

    # ---- Motorlar / guc aleti parcalari -> 1361 Hardware > Tools > Power Tool Parts & Accessories
    "4 Zamanlı Motorlar": 1361,
    "2 Zamanlı Motorlar": 1361,

    # ---- Toprak isleme / capa -> 3878 Home&Garden > Lawn&Garden > Outdoor Power Equipment > Tillers
    "Çapa Makinesi Parçaları": 3878,
    "Benzinli Çapa Makinesi": 3878,
    "Dizel Çapa Makinesi": 3878,
    "Çapa Makinesi": 3878,
    "Benzinli Toprak Havalandırma Makinesi": 3878,
    "Elektrikli Toprak Havalandırma Makinesi": 3878,

    # ---- Ilaclama / pulverizator -> 6967 Home&Garden > Lawn&Garden > Watering&Irrigation > Sprayers
    "İlaçlama Makinesi Parçaları": 6967,
    "Benzinli İlaçlama Makinesi": 6967,
    "Akülü İlaçlama Makinesi": 6967,
    "Elektrikli İlaçlama Makinesi": 6967,

    # ---- Jenerator -> 1233 Hardware > Power & Electrical Supplies > Generators
    "Jeneratör Parçaları": 1233,
    "Benzinli Jeneratör": 1233,
    "Dizel Jeneratör": 1233,
    "İnverter": 1233,

    # ---- Budama makasi -> 3568 Home&Garden > Lawn&Garden > Garden Tools > Pruning Shears
    "Budama Makası": 3568,
    "Akülü Ağaç Budama Makası": 3568,
    "Aşı Makası": 3568,

    # ---- Hayvancilik / sagim -> 3568 yok; 505288 Business&Industrial > Agriculture > Livestock Supplies
    "Sağım Makinesi Aksesuarları": 505288,
    "Süt Sağma Makinesi": 505288,
    "Koyun Kırkma Makinesi": 505288,
    "Otomatik Hayvan Sulukları": 505288,
    "Elektrikli Çit Sistemleri": 505288,
    "Yem Hazırlama Makinesi": 505288,

    # ---- Hasat makineleri -> 1298 Business&Industrial > Agriculture > Agricultural Machinery
    "Zeytin Hasat Makinesi": 1298,
    "Hasat Makinesi Parçaları": 1298,
    "Ceviz Hasat Makinesi": 1298,
    "Çay Toplama Makinesi": 1298,
    "Hasat Makinesi": 1298,
    "Bitki Bağlama Makinesi": 1298,
    "Fide Dikici ve Sökücü": 1298,
    "Bahçe Makineleri": 1298,

    # ---- Tekne -> 1130 Sporting Goods > Outdoor Recreation > Boating > Boat Parts
    "Tekne Motoru Parçaları": 1130,
    "Tekne Motoru": 1130,
    "Tekne ve Yat Malzemeleri": 1130,

    # ---- Aku / sarj -> 2978 Electronics > Electronics Accessories > Power > Battery Chargers
    "Akü ve Şarj Aletleri": 2978,

    # ---- Matkap -> 1187 Hardware > Tools > Drills
    "Matkaplar": 1187,
    "Akülü Vidalama": 1187,
    "Toprak Burgu Parçaları": 1187,
    "Toprak Burgu Makinesi": 1187,
    "Toprak Delme Aparatı": 1187,
    "Karot Makinesi": 1187,

    # ---- Yaprak ufleme -> 6790 Home&Garden > Lawn&Garden > Outdoor Power Equipment > Leaf Blowers
    "Yaprak Toplama Üfleme Parçaları": 6790,
    "Benzinli Yaprak Toplama Üfleme Makinesi": 6790,
    "Akülü Yaprak Toplama Üfleme Makinesi": 6790,
    "Elektrikli Yaprak Toplama Üfleme Makinesi": 6790,
    "Yaprak Toplama Üfleme Makinesi": 6790,

    # ---- Dal ogutme -> 6273 Home&Garden > Lawn&Garden > Outdoor Power Equipment > Chippers
    "Benzinli Yaprak Dal Öğütme Makinesi": 6273,
    "Elektrikli Yaprak Dal Öğütme Makinesi": 6273,
    "Yaprak Dal Öğütme Makinesi": 6273,
    "Dal Öğütme Makinesi Parçaları": 6273,

    # ---- Is ayakkabisi -> 187 Apparel&Accessories > Shoes
    "İş Ayakkabısı": 187,
    "Bahçıvan Şapka &amp; Bere &amp; Eldiven": 167,  # Apparel > Clothing Accessories

    # ---- Balta / nacak -> 1236 Hardware > Tools > Axes
    "Balta ve Nacak": 1236,
    "Odun Taşıma Aleti": 1236,

    # ---- Taslama / zimpara -> 1235 Hardware > Tools > Grinders / 1242 Sanders
    "Taşlamalar": 1235,
    "Zımpara Makinesi": 1242,
    "El Zımparası": 1242,
    "Polisaj Makinesi": 1242,

    # ---- Cit kesme -> 6788 Home&Garden > Lawn&Garden > Outdoor Power Equipment > Hedge Trimmers
    "Çit Kesme Makinesi Parçaları": 6788,
    "Benzinli Çit Kesme Makinesi": 6788,
    "Akülü Çit Kesme Makinesi": 6788,
    "Elektrikli Çit Kesme Makinesi": 6788,
    "Çim Çit Makası": 6788,

    # ---- Sulama / hortum -> 2802 Home&Garden > Lawn&Garden > Watering&Irrigation > Garden Hoses
    "Hortum ve Toplama Ürünleri": 2802,
    "Hortum Bağlantıları": 2802,
    "Fıskiyeler": 2802,
    "Su Zamanlayıcı": 2802,
    "Sprey Besin Solüsyonu": 6967,

    # ---- Kesme / testere -> 1235 Saws family
    "Ahşap ve Metal Kesme": 1218,   # Hardware > Tools > Saws
    "Beton Kesme Makinesi": 1218,
    "Dekupaj Testere": 1218,
    "Tilki Kuyruğu": 1218,
    "Daire Testere": 1218,
    "Metal Kesme Makası": 1167,     # Hardware > Tools > Cutters
    "Hasat Bıçakları": 1167,

    # ---- Kirici / delici -> 1180 Hardware > Tools > Hammers (Demolition)
    "Kırıcı Delici ve Kırıcı": 1180,
    "Çekiç ve Balyoz": 1180,
    "Çivi ve Zımba Çakma": 1180,

    # ---- El aletleri / bahce -> 3173 Home&Garden > Lawn&Garden > Garden Tools
    "Çapa, Kazma, Kürek": 3173,
    "Tırmık ve Dirgen": 3173,
    "Bahçe Seti": 3173,
    "Çöp Toplama Aparatı": 3173,

    # ---- Gida isleme makineleri -> 730 Home&Garden > Kitchen&Dining > Kitchen Appliances
    "Meyve Kurutma Makinesi": 730,
    "Meyve Pres Makinesi": 730,
    "Meyve Dilimleme Makinesi": 730,
    "Salça Makinesi": 730,
    "Hamur Karma Makinesi": 730,
    "Yayık Makinesi": 730,
    "Öğütme Makinesi": 730,
    "Airfryer &amp; Fritözler": 730,
    "Vakumlu Paketleme Makinesi": 730,

    # ---- El aletleri (tornavida/pense vb) -> 1209 Hardware > Tools > Hand Tools family
    "Somun Sıkma Makineleri": 1215,   # Wrenches
    "Tornavida": 1216,                # Screwdrivers
    "Pense": 1214,                    # Pliers
    "Kargaburun": 1214,
    "Yan Keski": 1214,
    "Anahtar Takımı": 1215,
    "Diğer El Aletleri": 1209,
    "Perçin": 1209,
    "Pafta Makinesi": 1209,
    "Kontrol Kalemi": 1209,

    # ---- Olcum -> 1305 Hardware > Tools > Measuring Tools & Sensors
    "Lazer Ölçüm Cihazı": 1305,
    "Su Terazisi": 1305,
    "Şerit Metre": 1305,

    # ---- Diger guc aletleri
    "Hava Kompresörü": 1226,      # Hardware > Tools > Air Compressors
    "Kaynak Makinesi": 1244,      # Hardware > Tools > Welding Equipment
    "Basınçlı Yıkama Makinesi": 3242,  # Pressure Washers
    "Karıştırıcılar": 1361,
    "Boya Tabancaları": 1361,
    "Sıcak Hava Tabancası": 1361,
    "Planyalar": 1361,
    "Freze": 1361,
    "Elektrikli Vinç": 1361,
    "Kar Küreme Makinesi": 6791,  # Snow Blowers

    # ---- Kimyasal / bakim
    "Bahçe Makine Yağları": 2620,   # Vehicles&Parts > Vehicle Maintenance > Fluids&Chemicals
    "Gübre": 2985,                  # Home&Garden > Lawn&Garden > Fertilizers
    "Köpek Kırkma Makinesi": 2975,  # Animals&Pet Supplies > Pet Grooming
}
