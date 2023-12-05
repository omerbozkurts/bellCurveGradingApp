def ortalama_hesaplama(vize, final):
    return float(vize) * 0.4 + float(final) * 0.6

def geçme_kalma_durumu(student, genel_ortalama):
    for ogrenci in student:
        ad = ogrenci['ad']
        soyad = ogrenci['soyad']
        vize = float(ogrenci['vize'])
        final = float(ogrenci['final'])
        gecme_durumu = ogrenci['geçme_durumu']
        
        if ortalama_hesaplama(vize, final) < genel_ortalama:
            ogrenci['geçme_durumu'] = True
        else:
            ogrenci['geçme_durumu'] = False

        print("Öğrenci adı: {}, Soyadı: {}, Vize: {}, Final: {}, Geçme Durumu: {}".format(
            ad, soyad, vize, final,'Kaldı' if ogrenci['geçme_durumu'] else 'Geçti'
        ))

student = []
genel_ortalama = 0
ogrenci_sayisi = int(input("Kaç öğrenci için işlem yapacaksınız: "))

for i in range(ogrenci_sayisi):
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    vize = input("Öğrenci vize notu: ")
    final = input("Öğrenci final notu: ")
    gecme_durumu = False
    ogrenci = {"ad": ad, "soyad": soyad, "vize": vize, "final": final, "geçme_durumu": gecme_durumu}
    student.append(ogrenci)
    genel_ortalama += ortalama_hesaplama(vize,  final)

genel_ortalama = genel_ortalama / ogrenci_sayisi
geçme_kalma_durumu(student, genel_ortalama)


