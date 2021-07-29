arr = []
n = x = int(input("Banyaknya element : "))
for i in range(0,n):
    x = int(input("Nilai element ke - "+ str(i+1)+ " : "))
    arr.append(x)


#fungsi menghitung rata-rata(mean)
def mean(l):
  sum = 0
  for ele in l:
    sum = sum + ele
  return sum / n

rataRata = mean(arr)

#tiap elemen data dikurang rata - rata dan dikuadratkan
res = [(ele - rataRata) ** 2 for ele in arr]

#fungsi menghitung semua elemen list
def sumList(l):
  sum = 0
  for ele in l:
    sum = sum + ele
  return sum

sigma = sumList(res)

stdDeviasi = (sigma / n) ** 0.5
print ("Standar Deviasi :", stdDeviasi)