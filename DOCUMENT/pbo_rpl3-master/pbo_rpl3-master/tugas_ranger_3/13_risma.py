import os

while True:
    print("----OPERASI FILE----")
    print("1.Buat File")
    print("2.Isi File")
    print("3.Baca File")
    print("4.Hapus File")
    print("5.SELESAI")

    pilih = input("PILIH NOMOR[1/2/3/4/5] = ")

    if pilih == "1":
        print("---Buat File---")
        try:
            file = input("nama file baru= ")
            f = open(file,"w")
            print("File",file,"sudah dibuat")
            f.close()
        except:
            print("error?")
    elif pilih == "2":
        print("---Isi File---")
        try:
            file = input("nama file = ")
            with open(file,"w") as fp:
                data = input("isi file:")
                print("File",file,"diisi oleh",data)
                fp.write(data)
                f.close()
        except:
            print("error?")
    elif pilih == "3":
        print("---Baca File---")
        try:
            file = input("nama file = ")
            with open(file,"r") as fp:
                line = fp.readline()
                while line:
                    print("isi dari file",file,"adalah",line.strip())
                    line = fp.readline()
        except:
            print("error?")
    elif pilih == "4":
        print("---Hapus File---")
        try:
            nama = input("nama file yang akan dihapus = ")
            os.remove(nama)
            print("file",nama,"berhasil dihapus")
        except:
            print("error?")
    elif pilih == "5":
        print("---SELESAI---")
        break
    else:
        print("tidak ada nomor",pilih)    