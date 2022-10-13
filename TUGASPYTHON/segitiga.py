a = int(input("masukkan maks jumlah kolom/baris : "))
x = 0 
for i in range(0, a):
    for j in range(0, x):
        # print(j, end='')
        print(' ',end='')
    x += 2
    for j in range(0, a):
        print('* ' , end='')
    a -= 1
    print('')
    

a = int(input("masukkan maks jumlah kolom/baris : "))
x = 2 * a - 2 
for i in range(0, a):
    for j in range(0, x):
        print(' ',end='')
    x -= 2
    for j in range(0, i + 1):
        print('* ', end='')
    print('')
 
a = int(input("masukkan maks jumlah kolom/baris : "))
x = a - 1 
for i in range(0, a):
    for j in range(0, x):
        print(' ', end='')
    x -= 1
    for j in range(0, i + 1):
        print('* ', end='')
 
    print('')
 
a = int(input("masukkan maks jumlah kolom/baris : "))
x = 0 
for i in range(0, a):
    for j in range(0, x):
        print(' ',end='')
    x += 1
    for j in range(0, a):
        print('* ' , end='')
    a -= 1
    print('')





 

 

