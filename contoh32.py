#Format inputan salah pada contoh 3.2
bilangan = input("Masukkan suatu bilangan: ")

try:
    bilangan = int(bilangan)
    if bilangan > 0:
            print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except:
    print("Inputan anda salah")