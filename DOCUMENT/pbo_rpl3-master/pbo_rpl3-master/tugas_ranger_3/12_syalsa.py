import os

while True:
    print("===Operasi File===")
    print("1.Buat File")
    print("2.Isi File")
    print("3.Baca File")
    print("4.Hapus File")
    print("5.Selesai")

    pilih = input("Pilih Nomor[1/2/3/4/5]:")

    if pilih =='1':
        print("<<<<<Buat File>>>>>")
        try:
            file = input("Nama File Baru:")
            f = open(file,"w")
            print("File",file,"sudah dibuat")
            f.close()
        except:
            print("error?")
    elif pilih =='2':
        print("<<<<<Isi File>>>>>")
        try:
            file = input("Nama File:")
            with open(file,"w") as fp:
                data = input("Isi File:")
                print("File",file,"diisi oleh",data)
                fp.write(data)
                f.close()
        except:
            print("error?")
    elif pilih =='3':
        print("<<<<<Baca File>>>>>")
        try:
            file = input('Nama File:')
            with open(file,"r") as fp:
                line = fp.redline()
                while line:
                    print("Isi dari file",file,"adalah",line.strip())
                    line = fp.readline()
        except:
            print("error?")
    elif pilih =='4':
        print("<<<<<Hapus File>>>>>")
        try:
            file = input('Nama File:')
            os.remove(file)
            print("File",file,"sudah terhapus")
        except:
            print("error?")
    elif pilih =='5':
        print("<<<<<Selesai>>>>>")
        break
    else:
        print("Tidak ada pilihan untuk nomor",pilih)      