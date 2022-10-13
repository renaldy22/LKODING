##2141042_RENALDY LUTHFIANA HAKIM_PRAKTIKUM PEMROGRAMAN PHYTON_PHYTONSBT

#print("SOAL NOMOR 1")

print("keterangan usia boleh nonton film")
usia = int(input("masukkan usia penonton: "))

if usia > 17:
    print("dibolehkan menonton!!")
else:
    print("tidak boleh menonton")
    
    
# print("SOAL NOMOR 2")

print ("Terdapat 10 bilangan positif antara 0 sampai 100, tentukan angka ganjil terbesar!")
angka1=20
print ("Bilangan ke-1:", angka1)
angka2=33
print ("Bilangan ke-2:", angka2)
angka3=58
print ("Bilangan ke-3:", angka3)
angka4=60
print ("Bilangan ke-4:", angka4)
angka5=48
print ("Bilangan ke-5:", angka5)
angka6=87
print ("Bilangan ke-6:", angka6)
angka7=19
print ("Bilangan ke-7:", angka1)
angka8=77
print ("Bilangan ke-8:", angka8)
angka9=65
print ("Bilangan ke-9:", angka9)
angka10=45
print ("Bilangan ke-10:", angka10)
terbesar=0

if(angka1 % 2 != 0 and angka1>terbesar):
    terbesar=angka1
if(angka2 % 2 != 0 and angka2>terbesar):
    terbesar=angka2
if(angka3 % 2 != 0 and angka3>terbesar):
    terbesar=angka3
if(angka4 % 2 != 0 and angka4>terbesar):
    terbesar=angka4
if(angka5 % 2 != 0 and angka5>terbesar):
    terbesar=angka5
if(angka6 % 2 != 0 and angka6>terbesar):
    terbesar=angka6
if(angka7 % 2 != 0 and angka7>terbesar):
    terbesar=angka7
if(angka8 % 2 != 0 and angka8>terbesar):
    terbesar=angka8
if(angka9 % 2 != 0 and angka9>terbesar):
    terbesar=angka9
if(angka5 % 2 != 0 and angka10>terbesar):
    terbesar=angka10
print ("Angka ganjil terbesar adalah:", terbesar)



# print("SOAL NOMOR 3")


print("Silahkan masukkan data Anda!")
Nama=input("Nama:")
umur=int(input("Masukkan Umur:"))

if umur <= 5:
    print("Balita")
elif umur > 5 and umur <= 12:
    print ("Anak-anak")
elif umur > 12 and umur <= 18:
    print ("Remaja")
else:
    print ("Dewasa")
    
    
    
# print("soal nomor 4")
# print("menentukan komisi dia jika langganan atau bukan")

langganan = input("apakah anda langganan [yes or no]: ")
fotokopi = int(input("masukkan berapa lembar: "))

if langganan == 'yes':
    hitung = (fotokopi * 75)
else: 
    if  fotokopi < 100:
        hitung = (fotokopi * 100)
    else: 
        hitung = (fotokopi * 85)

print("Harga yang harus Anda bayar adalah Rp.", hitung)


# print("nomor 5")
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


