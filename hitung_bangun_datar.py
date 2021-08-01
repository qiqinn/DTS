from sys import path

path.append('bangun_datar')

import lingkaran, persegi_panjang, segi_tiga

print("Pilih bangun datar yang akan dihitung luas dan kelilingnya :")
print("1. Lingkaran\n2. Persegi panjang \n3. Segi tiga")
opsi = int(input("Pilihan : "))

if opsi == 1:
    r = int(input("jari jari lingkaran : "))
    print("Luas lingkaran : ", lingkaran.luas(r))
    print("Keliling lingkaran : ", lingkaran.keliling(r))

elif opsi == 2:
    p = int(input("panjang persegi panjang : "))
    l = int(input("lebar persegi panjang : "))
    print("Luas persegi panjang : ", persegi_panjang.luas(p,l))
    print("Keliling persegi panjang : ", persegi_panjang.keliling(p,l))

elif opsi == 3:
    a = int(input("alas segi tiga : "))
    t = int(input("tiggi segi tiga : "))
    b = int(input("panjang sisi kedua :"))
    c = int(input("panjang sisi ketiga :"))
    print("Luas segi tiga : ", segi_tiga.luas(a,t))
    print("Keliling segi tiga : ", segi_tiga.keliling(a,b,c))



else:
    print("input tidak valid")