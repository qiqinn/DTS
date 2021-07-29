isPegawaiTetap = input("Apakah anda pegawai tetap (y/n) ?  ")

jamLembur = int(input("Masukkan jumlah jam lembur anda :"))

maxLembur = 20
if jamLembur > maxLembur:
    jamLembur = maxLembur

if isPegawaiTetap == 'y':
    gaji = 4500000 + (jamLembur * 50000)
elif isPegawaiTetap == 'n':
    gaji = (4500000 * 0.7) + (jamLembur * 30000)
else:
    print("Input yang anda masukkan tidak sesuai")

pajak = gaji * 0.01

print("Total gaji anda : Rp.", int(gaji-pajak))