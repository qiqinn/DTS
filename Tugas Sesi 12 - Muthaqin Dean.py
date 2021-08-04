#0728088701
from datetime import datetime 

nidn = input("Masukkan NIDN anda : ")
bulan = datetime.strptime(nidn[4:6], "%m")

try:
    if len(nidn) == 10 and nidn.isnumeric():
        print(nidn.isnumeric())
        print("Anda tedaftar pada LLDIKTI", nidn[1])
        print("Anda lahir pada tanggal", nidn[2:4], bulan.strftime("%B"), 1900+int(nidn[6:8]))
        print("Anda adalah orang ke", nidn[9], "yang lahir pada tanggal tersebut diwilayah", nidn[1]) 
    else:
        print("Input yang dimasukkan tidak valid")     
except:
    print("Input yang dimasukkan tidak valid")