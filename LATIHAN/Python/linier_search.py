#linier search
#tanpa fungsi

# list = [20,30,7,1,4,7,3,9,90,11,24]
# cari = int(input("masukkan angka yang anda cari : "))
# counter = 0
# while counter != len(list):
#     if list[counter] == cari:
#         print("data yang di cari berada di data ke.",counter)
#     counter += 1
    
# if cari not in list:
#     print ("data tidak ada di list |||");

#linier search
#dengan fungsi

list = [20,30,7,1,4,7,3,9,90,11,24]
cari = int(input("masukkan angka yang anda cari : "))

#buat fungsi mencari data
def searchNumber (List,seacrh):
    counter = 0
    while counter != len(list):
        if list[counter] == cari:
            result = counter
        counter += 1
    return result

#pemanggilan fungsi
try :
    hasil = searchNumber(list,cari)
    if cari in list:
        print('number %s in index %s'% (cari,hasil))
except :
    print ("number tidak di temukan !!!")