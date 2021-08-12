from math import pi

class Lingkaran:
    def luas(r):
        Luas = pi* (r**r)
        print("Luas lingkaran :", Luas)

    def keliling(r):
        Keliling = pi* (r**r)* (r+r)
        print("Keliling lingkaran :", Keliling)

class PersegiPanjang:
    def luas(p,l):
        Luas = p*l
        print("Luas persegi panjang :", Luas)
    
    def keliling(p,l):
        Keliling = (p+l) *2
        print("Keliling persegi panjang :", Keliling)

class SegiTiga:
    def luas(a,t):
        Luas = (a * t)/2
        print("Luas segi tiga :", Luas)

    def keliling(a, b, c):
        Keliling = a + b + c
        print("Keliling segi tiga :", Keliling)


class BangunDatar:
    r = float(input("Masukkan Jari-Jari Lingkaran: "))
    lLingkaran = Lingkaran.luas(r)
    kLingkaran = Lingkaran.keliling(r)

    print()

    p = float(input("Masukkan Panjang Persegi Panjang: "))
    l = float(input("Masukkan Lebar Persegi Panjang: "))
    lPersegiPanjang = PersegiPanjang.luas(p, l)
    kPersegiPanjang = PersegiPanjang.keliling(p, l)

    print()
    a = float(input("Masukkan Panjang Alas Segitiga: "))
    t = float(input("Masukkan Tinggi Segitiga: "))
    b = float(input("Masukkan Panjang Sisi Kedua: "))
    c = float(input("Masukkan Panjang Sisi Ketiga: "))
    luasSegiTiga = SegiTiga.luas(a, t)
    kelilingSegiTiga = SegiTiga.keliling(a,b,c)


BangunDatar()