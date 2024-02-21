#Format inputan salah pada contoh 3.3
a = input("Masukkan bilangan pertama: ")
b = input("Masukkan bilangan kedua: ")
c = input("Masukkan bilangan ketiga: ")

try:
    a = int(a)
    b = int(b)
    c = int(c)
    if a > b and a > c:
        print("Bilangan terbesar adalah ", a)

    elif b > a and b > c:
        print("Bilangan terbesar adalah ", b)
        
    elif c > a and c > b:
        print("Bilangan terbesar adalah ", c)
        
except:
    print("Inputan anda salah")