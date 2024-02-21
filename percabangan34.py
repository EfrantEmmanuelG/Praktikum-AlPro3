angka_1 = input("Masukkan sisi pertama: ")
angka_2 = input("Masukkan sisi kedua: ")
angka_3 = input("Masukkan sisi ketiga: ")

try:
    angka_1 = int(angka_1)
    angka_2 = int(angka_2)
    angka_3 = int(angka_3)
    if angka_1 == angka_2 and angka_1 == angka_3 and angka_2 == angka_3:
        print("3 sisi sama")

    elif angka_1 == angka_2:
        print("2 sisi sama")

    elif angka_1 == angka_3:
        print("2 sisi sama")

    elif angka_3 == angka_2:
        print("2 sisi sama")
        
    else:
        print("Tidak ada yang sama.")
        
except:
    print("Inputan anda salah!")