# print("soal nomor 3")
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