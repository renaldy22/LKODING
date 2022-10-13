##SOAL No 1
usia = 0
usia = int(input("masukan usia anda : "))
if  usia < 17:
    print("Anda tidak boleh menonton film ini")
else:
    print("Anda boleh menonton film ini")

##SOAL No 2
terbesar =int (0)
angka1 =int (20)
angka2 =int (33)
angka3 =int (58)
angka4 =int (60)
angka5 =int (48)
angka6 =int (87)
angka7 =int (19)
angka8 =int (77)
angka9 =int (65)
angka10 =int (45)
if((angka1%2!=0) and (angka1>terbesar)):
    terbesar=angka1
if((angka2%2!=0) and (angka2>terbesar)):
    terbesar=angka2
if((angka3%2!=0) and (angka3>terbesar)):
    terbesar=angka3
if((angka4%2!=0) and (angka4>terbesar)):
    terbesar=angka4
if((angka5%2!=0) and (angka5>terbesar)):
    terbesar=angka5
if((angka6%2!=0) and (angka6>terbesar)):
    terbesar=angka6
if((angka7%2!=0) and (angka7>terbesar)):
    terbesar=angka7
if((angka8%2!=0) and (angka8>terbesar)):
    terbesar=angka8
if((angka9%2!=0) and (angka9>terbesar)):
    terbesar=angka9
if((angka10%2!=0) and (angka10>terbesar)):
    terbesar=angka10
print ("angka ganjil terbesar adalah: ", terbesar)

##SOAL No 3
usia = 0
usia = int(input("masukan usia anda : "))
if  usia <= 5:
    print("golongan balita")
elif  usia >5 and usia<12:
    print("golongan anak-anak")
elif  usia >12 and usia< 18:
    print("golongan remaja")
else:
    print("golongan dewasa")
    
##SOAL No 4
Status = str (input("Apakah anda langganan di sini? "))
JLF = int(input("Masukkan jumlah halaman yang mau difotokopi: "))
HPP = int
TH = int
if (Status == "ya")or(Status == "Ya"):
    HPP = 75
elif (Status == "tidak")or(Status == "Tidak"):
    if (JLF < 100):
        HPP = 100
    else:
        HPP = 85
TH = JLF * HPP
print ("Harga yang harus anda bayar adalah Rp.",TH)

##SOAL No 5
nama = str (input("Masukan Nama anda: "))
kelas = str (input("Masukan Kelas anda: "))
jurusan = str (input("Masukan Jurusan anda: "))
nilaiKehadiran = int (input("Masukan NIlai Kehadiran anda: " ))
nilaitugas = int (input("Masukan NIlai Tugas anda: "))
nilaiUTS = int (input ("Masukan NIlai UTS anda: " ))
nilaiUAS = int (input ("Masukan NIlai UAS anda: "))
nilaiAkhir = (nilaiKehadiran*10/100)+(nilaitugas*20/100)+(nilaiUTS*30/100)+(nilaiUAS*40/100)
if nilaiAkhir >=86 and nilaiAkhir <=100:
    indeks="A"
if nilaiAkhir >=81 and nilaiAkhir <=85:
    indeks="B+"
if nilaiAkhir >=65 and nilaiAkhir <=80:
    indeks="B"
if nilaiAkhir >=60 and nilaiAkhir <=64:
    indeks="C+"
if nilaiAkhir >=55 and nilaiAkhir <=59:
    indeks="C"
if nilaiAkhir >=45 and nilaiAkhir <=54:
    indeks="D"
if nilaiAkhir >=0 and nilaiAkhir <=44:
    indeks="E"
print ("nama:",nama,",","kelas:",kelas,",","jurusan:",jurusan,",","Nilai Akhir:",nilaiAkhir,",","indeks:",indeks)

