print("nomor 5")
print("menentukan kelulusan nilai Ujian UTS")

nama = str(input("masukkan nama anda : "))
nim  = int(input("masukkan nim anda : "))
jurusan = str(input("masukkan jurusan anda : "))


uts = float(input("masukkan nilai UTS : "))
uas = float(input("masukkan nilai UAS : "))

if uts > 70:
    status = 'lulus'
    nilaiakhir = uts
    print("Hasil Nilai Akhir Mahasiswa")
    print("Nama:", nama)
    print("Kelas:", nim)
    print("Jurusan:", jurusan)
    print("Status:", status)
    print("Nilai Akhir", nilaiakhir)
elif uts <= 70:
    nilaiakhir = (uts*0.4)+(uas*0.6) 
    if nilaiakhir > 60:
        status = 'lulus'
        print("Hasil Nilai Akhir Mahasiswa")
        print("Nama:", nama)
        print("Kelas:", nim)
        print("Jurusan:", jurusan)
        print("Status:", status)
        print("Nilai Akhir", nilaiakhir)
    else :
        status = 'tidak lulus'
        print("Hasil Nilai Akhir Mahasiswa")
        print("Nama:", nama)
        print("Kelas:", nim)
        print("Jurusan:", jurusan)
        print("Status:", status)
        print("Nilai Akhir", nilaiakhir)



         