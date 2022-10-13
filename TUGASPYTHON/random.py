print("soal nomor 2")
print("menentukan angka ganjil terbesar")

angka = [20,30,58,60,48,87,19,77,65,45]
nilai = []
for i in angka:
    if i % 2 == 1:
        nilai.append(i)
nilai.sort()
print(nilai[-1])